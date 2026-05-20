# M1 체크리스트 - Unity MCP 연결 확인

## 목적

이 문서는 `docs/project-goal.md`의 `M1. Unity MCP 연결 확인` 완료 기준을 작은 확인 항목으로 나누어, M1 완료 여부를 체크리스트만으로 판정하기 위해 작성합니다.

M1의 목표는 Codex가 Unity MCP를 통해 Unity Editor 상태를 확인할 수 있는지 검증하는 것입니다.

## 적용 MCP

- MCP 패키지: `CoderGamester/mcp-unity`
- Unity dependency: `com.gamelovers.mcp-unity`
- 고정 커밋: `a32e47d4ec8731685394dd562aa6f4f119f2bf79`
- 기본 서버 설정: `localhost:8090`
- Codex 설정 파일: `.codex/config.toml`
- Unity 설정 파일: `ProjectSettings/McpUnitySettings.json`

## 완료 판정 규칙

- 필수 체크리스트의 모든 항목이 완료되어야 M1을 완료로 판정합니다.
- 각 항목은 Unity MCP 또는 Unity Editor에서 확인한 방법과 완료 증거를 함께 남깁니다.
- Unity MCP 연결, Console log 조회, package / asset 조회, Scene 정보, Play Mode 가능 여부 중 하나라도 확인하지 못하면 M1을 완료로 판정하지 않습니다.
- Scene 정보나 Play Mode를 MCP 도구만으로 직접 확인할 수 없으면 Unity Editor로 보완 확인하고, MCP 한계를 `미확인/예외`에 기록합니다.
- 파일을 수정하지 않는 확인 작업이므로, 변경 파일이 생기면 이유를 `미확인/예외`에 기록합니다.

## 필수 체크리스트

- [x] M1-01: Unity 프로젝트가 열립니다.
  - 확인 방법: Unity Editor에서 이 저장소 프로젝트가 열려 있는지 확인합니다.
  - 완료 증거: Unity MCP가 이 저장소의 Unity Editor에서 응답했습니다. Unity 로그에 `codex-harness-tgr-v1` 프로젝트의 `TestResults.xml` 저장 경로가 기록되었습니다.
- [x] M1-02: MCP 패키지가 resolve됩니다.
  - 확인 방법: Package Manager resolve 후 `Packages/packages-lock.json`에 `com.gamelovers.mcp-unity`가 있고 Unity Console에 MCP 관련 compile error가 없는지 확인합니다.
  - 완료 증거: `Packages/packages-lock.json`에 `com.gamelovers.mcp-unity`가 `https://github.com/CoderGamester/mcp-unity.git#a32e47d4ec8731685394dd562aa6f4f119f2bf79`로 기록되어 있습니다. Unity Console error는 `0개`입니다.
- [x] M1-03: MCP 서버 설정이 local-only입니다.
  - 확인 방법: `ProjectSettings/McpUnitySettings.json`에서 `Port`가 `8090`, `AllowRemoteConnections`가 `false`인지 확인합니다.
  - 완료 증거: `Port`는 `8090`, `AllowRemoteConnections`는 `false`, `NpmExecutablePath`는 빈 문자열입니다. 비밀값이나 개인 절대경로는 없습니다.
- [x] M1-04: Codex project-local 설정이 존재합니다.
  - 확인 방법: `.codex/config.toml`의 `mcp_servers.mcp-unity`가 `node`와 상대 PackageCache 경로를 사용하는지 확인합니다.
  - 완료 증거: `command = "node"`, `args = ["Library/PackageCache/com.gamelovers.mcp-unity@a32e47d4ec87/Server~/build/index.js"]`로 설정되어 있고 절대경로가 없습니다.
- [x] M1-05: Unity MCP 연결 상태를 확인합니다.
  - 확인 방법: `Tools > MCP Unity > Server Window`에서 서버를 시작하고 Codex MCP 응답 또는 연결 상태를 확인합니다.
  - 완료 증거: Unity Console 로그에 `[MCP Unity] WebSocket server started successfully on localhost:8090.` 및 `WebSocket client connected`가 기록되었고, Codex에서 MCP 도구 응답을 받았습니다.
- [x] M1-06: Console log 조회와 log 왕복을 확인합니다.
  - 확인 방법: `get_console_logs`로 로그를 읽고, `send_console_log`로 `mcp smoke test`를 보낸 뒤 다시 조회합니다.
  - 완료 증거: `send_console_log` 응답은 `Message displayed: mcp smoke test`였고, 이후 `get_console_logs`에서 `[MCP]: mcp smoke test` 로그를 확인했습니다.
- [x] M1-07: package / asset 리소스를 조회할 수 있습니다.
  - 확인 방법: `unity://packages`, `unity://assets` 같은 조회성 리소스를 확인합니다.
  - 완료 증거: `unity://packages`에서 `com.gamelovers.mcp-unity`가 `version: 1.3.0`, `source: Git`, `state: installed`로 조회되었습니다. `unity://assets`에서 `Retrieved 10658 assets`가 기록되었고 대표 asset으로 `Assets/Scenes/SampleScene.unity`를 확인했습니다.
- [x] M1-08: 현재 Scene 정보를 읽을 수 있습니다.
  - 확인 방법: Unity MCP 또는 Unity Editor로 현재 활성 Scene 이름과 경로를 조회합니다.
  - 완료 증거: `get_scene_info` 응답은 활성 Scene 이름이 빈 문자열이고 경로가 `(unsaved)`, `Build Index: -1`, `Is Loaded: true`, `Root Count: 1`입니다.
- [x] M1-09: Console error를 확인할 수 있습니다.
  - 확인 방법: Unity MCP 또는 Unity Console에서 error 목록을 확인합니다.
  - 완료 증거: `get_console_logs(logType=error, includeStackTrace=false)` 응답은 빈 배열입니다. error는 `0개`입니다.
- [x] M1-10: Play Mode 실행 가능 여부를 확인합니다.
  - 확인 방법: Unity MCP 또는 Unity Editor에서 Play Mode 진입 가능 여부를 확인합니다.
  - 완료 증거: `execute_menu_item`으로 `Tools/Codex/M1/Run Play Mode Smoke Test`를 실행했고, Unity Console에서 `[M1 PlayMode Smoke] entered Play Mode token=20260520T090821264Z` 및 `[M1 PlayMode Smoke] completed token=20260520T090821264Z` 로그를 확인했습니다.

## 검증 증거

- 확인한 파일: `docs/milestones/M1-checklist.md`, `Packages/packages-lock.json`, `ProjectSettings/McpUnitySettings.json`, `.codex/config.toml`, `Assets/Editor/M1PlayModeSmokeTest.cs`
- 실행한 명령: `Get-Content`, `git status --short`, `rg`
- Unity 또는 도구에서 확인한 결과: MCP 서버 `localhost:8090` 응답, Console log 조회와 `mcp smoke test` 왕복 성공, `unity://packages` 및 `unity://assets` 조회 성공, 활성 Scene 정보 조회 성공, Play Mode smoke test 성공, Console error `0개`
- 확인 날짜: 2026-05-20 18:08 KST

## 미확인/예외

- 이 MCP 버전에는 Play Mode 전용 도구가 없어서, M1 확인용 Editor-only 메뉴 `Tools/Codex/M1/Run Play Mode Smoke Test`를 추가해 `execute_menu_item`으로 검증했습니다.
- `unity://packages`와 `unity://assets`는 최초 조회 때 timeout이 있었으나, 재시도 후 모두 조회에 성공했습니다.
- 확인 과정에서 Unity가 `ProjectSettings/SceneTemplateSettings.json`을 새로 생성했습니다. 생성 시각은 2026-05-20 17:35 KST이며, PlayMode Test Runner 실행 시점과 일치합니다.

## 최종 판정

- 판정: 완료
- 판정 근거: M1 필수 체크리스트 `M1-01`부터 `M1-10`까지 모두 확인했고, Unity MCP 연결, Console log 왕복, package / asset 조회, Scene 정보, Console error, Play Mode 실행 가능 여부 증거를 모두 기록했습니다.
- 다음 조치: M2 착수 전 변경 파일을 검토하고 커밋 여부를 결정합니다.
