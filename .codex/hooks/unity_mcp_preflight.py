#!/usr/bin/env python3
"""Report-only Unity MCP preflight for Codex hooks."""

from __future__ import annotations

import json
import os
import queue
import re
import subprocess
import sys
import threading
import time
import tomllib
from pathlib import Path
from typing import Any


CHECKS = ".codex/config.toml, MCP package path, MCP response, get_scene_info"
NO_ACTIONS = "No auto-fix, Unity menu, recompile, or test run was performed."
PROMPT_TERMS = re.compile(
    r"(\bcsharp\b|\bmcp\b|\bscene\b|\bscenes\b|\basset\b|\bassets\b|\bunity\b|\.cs\b|\.unity\b|\.prefab\b|유니티|씬|에셋)",
    re.IGNORECASE,
)
UNITY_PATCH_MARKERS = re.compile(
    r"(Assets[\\/]|ProjectSettings[\\/]|Packages[\\/]|\.cs\b|\.unity\b|\.prefab\b|\.asmdef\b|\.asset\b)",
    re.IGNORECASE,
)


class PreflightError(Exception):
    def __init__(self, stage: str, reason: str) -> None:
        super().__init__(reason)
        self.stage = stage
        self.reason = reason


def main() -> int:
    event = "UserPromptSubmit"
    try:
        hook_input = read_hook_input()
        event = str(hook_input.get("hook_event_name") or event)
        if not should_run(hook_input):
            return 0

        project_root = find_project_root(hook_input)
        result = run_preflight(project_root)
        emit_context(event, build_pass_message(result))
    except PreflightError as exc:
        emit_context(event, build_warning(exc.stage, exc.reason))
    except Exception as exc:  # Keep this hook report-only even for unexpected failures.
        emit_context(event, build_warning("MCP response", f"unexpected hook error: {exc}"))
    return 0


def read_hook_input() -> dict[str, Any]:
    raw = sys.stdin.read()
    if not raw.strip():
        return {}
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise PreflightError("MCP response", f"invalid hook input JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise PreflightError("MCP response", "hook input was not a JSON object")
    return data


def should_run(hook_input: dict[str, Any]) -> bool:
    event = hook_input.get("hook_event_name")
    if event == "UserPromptSubmit":
        prompt = str(hook_input.get("prompt") or "")
        return bool(PROMPT_TERMS.search(prompt) or "c#" in prompt.lower())

    if event == "PreToolUse":
        tool_name = str(hook_input.get("tool_name") or "")
        if tool_name.startswith("mcp__mcp_unity__"):
            return True
        if tool_name != "apply_patch":
            return False
        return bool(UNITY_PATCH_MARKERS.search(tool_input_text(hook_input.get("tool_input"))))

    return False


def tool_input_text(tool_input: Any) -> str:
    if isinstance(tool_input, dict):
        parts: list[str] = []
        for key in ("command", "patch", "path", "file_path", "content"):
            value = tool_input.get(key)
            if value is not None:
                parts.append(str(value))
        if parts:
            return "\n".join(parts)
    if isinstance(tool_input, str):
        return tool_input
    try:
        return json.dumps(tool_input)
    except TypeError:
        return str(tool_input)


def find_project_root(hook_input: dict[str, Any]) -> Path:
    script_path = Path(__file__).resolve()
    candidates: list[Path] = []
    if len(script_path.parents) >= 3:
        candidates.append(script_path.parents[2])

    cwd = hook_input.get("cwd") or os.getcwd()
    try:
        cwd_path = Path(str(cwd)).resolve()
        candidates.extend([cwd_path, *cwd_path.parents])
    except OSError:
        pass

    for candidate in candidates:
        if (candidate / ".codex" / "config.toml").is_file():
            return candidate
    return Path.cwd().resolve()


def run_preflight(project_root: Path) -> Any:
    server_config = read_mcp_server_config(project_root)
    command = str(server_config.get("command") or "")
    args = server_config.get("args")
    if not command or not isinstance(args, list) or not all(isinstance(arg, str) for arg in args):
        raise PreflightError(".codex/config.toml", "mcp-unity command and args must be configured")

    package_arg = find_package_arg(args)
    package_path = Path(package_arg)
    if not package_path.is_absolute():
        package_path = project_root / package_path
    if not package_path.is_file():
        raise PreflightError("MCP package path", f"missing server entry point: {package_arg}")

    return call_get_scene_info(command, args, project_root)


def read_mcp_server_config(project_root: Path) -> dict[str, Any]:
    config_path = project_root / ".codex" / "config.toml"
    try:
        with config_path.open("rb") as config_file:
            config = tomllib.load(config_file)
    except FileNotFoundError as exc:
        raise PreflightError(".codex/config.toml", "config file was not found") from exc
    except tomllib.TOMLDecodeError as exc:
        raise PreflightError(".codex/config.toml", f"invalid TOML: {exc}") from exc

    server_config = config.get("mcp_servers", {}).get("mcp-unity")
    if not isinstance(server_config, dict):
        raise PreflightError(".codex/config.toml", "missing [mcp_servers.mcp-unity]")
    return server_config


def find_package_arg(args: list[str]) -> str:
    for arg in args:
        if arg.endswith((".js", ".mjs", ".cjs")):
            return arg
    if args:
        return args[0]
    raise PreflightError(".codex/config.toml", "mcp-unity args did not include a server path")


def call_get_scene_info(command: str, args: list[str], project_root: Path) -> Any:
    stderr_lines: list[str] = []
    output_queue: queue.Queue[tuple[str, str]] = queue.Queue()
    proc = subprocess.Popen(
        [command, *args],
        cwd=str(project_root),
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,
    )

    try:
        assert proc.stdout is not None
        assert proc.stderr is not None
        assert proc.stdin is not None
        start_reader(proc.stdout, "stdout", output_queue)
        start_reader(proc.stderr, "stderr", output_queue)

        send_json(
            proc,
            {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {},
                    "clientInfo": {
                        "name": "codex-unity-mcp-preflight",
                        "version": "0.1.0",
                    },
                },
            },
        )
        initialize_response = read_response(proc, output_queue, stderr_lines, 1, "MCP response")
        ensure_jsonrpc_success(initialize_response, "MCP response")

        send_json(proc, {"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}})
        time.sleep(0.75)
        send_json(
            proc,
            {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/call",
                "params": {"name": "get_scene_info", "arguments": {}},
            },
        )
        tool_response = read_response(proc, output_queue, stderr_lines, 2, "get_scene_info")
        ensure_jsonrpc_success(tool_response, "get_scene_info")
        result = tool_response.get("result")
        if isinstance(result, dict) and result.get("isError"):
            raise PreflightError("get_scene_info", extract_result_text(result) or "tool returned isError")
        return result
    except OSError as exc:
        raise PreflightError("MCP response", f"could not start MCP server: {exc}") from exc
    finally:
        stop_process(proc)


def start_reader(stream: Any, name: str, output_queue: queue.Queue[tuple[str, str]]) -> None:
    def read_lines() -> None:
        for line in iter(stream.readline, ""):
            output_queue.put((name, line.rstrip("\r\n")))

    thread = threading.Thread(target=read_lines, daemon=True)
    thread.start()


def send_json(proc: subprocess.Popen[str], payload: dict[str, Any]) -> None:
    if proc.stdin is None:
        raise PreflightError("MCP response", "MCP server stdin was not available")
    proc.stdin.write(json.dumps(payload, separators=(",", ":")) + "\n")
    proc.stdin.flush()


def read_response(
    proc: subprocess.Popen[str],
    output_queue: queue.Queue[tuple[str, str]],
    stderr_lines: list[str],
    response_id: int,
    stage: str,
) -> dict[str, Any]:
    deadline = time.monotonic() + 10
    invalid_stdout: list[str] = []
    while time.monotonic() < deadline:
        if proc.poll() is not None and output_queue.empty():
            reason = f"MCP server exited with code {proc.returncode}"
            details = recent_text(stderr_lines or invalid_stdout)
            if details:
                reason = f"{reason}: {details}"
            raise PreflightError(stage, reason)

        try:
            source, line = output_queue.get(timeout=0.1)
        except queue.Empty:
            continue

        if source == "stderr":
            if line:
                stderr_lines.append(line)
            continue

        if not line.strip():
            continue
        try:
            message = json.loads(line)
        except json.JSONDecodeError:
            invalid_stdout.append(line)
            continue
        if isinstance(message, dict) and message.get("id") == response_id:
            return message

    details = recent_text(stderr_lines or invalid_stdout)
    reason = "timed out waiting for JSON-RPC response"
    if details:
        reason = f"{reason}: {details}"
    raise PreflightError(stage, reason)


def ensure_jsonrpc_success(message: dict[str, Any], stage: str) -> None:
    if "error" in message:
        raise PreflightError(stage, describe_jsonrpc_error(message["error"]))
    if "result" not in message:
        raise PreflightError(stage, "JSON-RPC response did not include a result")


def describe_jsonrpc_error(error: Any) -> str:
    if isinstance(error, dict):
        message = error.get("message")
        code = error.get("code")
        if message and code is not None:
            return f"{message} (code {code})"
        if message:
            return str(message)
    return str(error)


def stop_process(proc: subprocess.Popen[str]) -> None:
    if proc.stdin:
        try:
            proc.stdin.close()
        except OSError:
            pass
    if proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=2)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait(timeout=2)


def build_pass_message(result: Any) -> str:
    summary = summarize_scene_info(result)
    if summary:
        summary = f" {summary}."
    return f"[unity-mcp-preflight] PASS: Unity MCP preflight succeeded.{summary} Checked only {CHECKS}. {NO_ACTIONS}"


def build_warning(stage: str, reason: str) -> str:
    return (
        "[unity-mcp-preflight] WARNING: Unity/C# work requested, but Unity MCP preflight failed "
        f"at {stage}: {reason}. Checked only {CHECKS}. {NO_ACTIONS}"
    )


def summarize_scene_info(result: Any) -> str:
    text = extract_result_text(result)
    scene_match = re.search(r"Assets[/\\][^\s\"']+?\.unity", text)
    dirty_match = re.search(r"is\s*dirty[\"'\s:=]+(true|false)", text, re.IGNORECASE)
    parts: list[str] = []
    if scene_match:
        parts.append(f"Scene={scene_match.group(0)}")
    if dirty_match:
        parts.append(f"Is Dirty={dirty_match.group(1).lower()}")
    if parts:
        return "; ".join(parts)
    if text:
        return "get_scene_info responded successfully"
    return ""


def extract_result_text(result: Any) -> str:
    if isinstance(result, dict):
        content = result.get("content")
        if isinstance(content, list):
            texts = []
            for item in content:
                if isinstance(item, dict) and isinstance(item.get("text"), str):
                    texts.append(item["text"])
            if texts:
                return "\n".join(texts)
    try:
        return json.dumps(result, ensure_ascii=False)
    except TypeError:
        return str(result)


def recent_text(lines: list[str]) -> str:
    return " | ".join(line for line in lines[-3:] if line)[-500:]


def emit_context(event: str, message: str) -> None:
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": event,
                    "additionalContext": message,
                }
            },
            separators=(",", ":"),
        )
    )


if __name__ == "__main__":
    raise SystemExit(main())
