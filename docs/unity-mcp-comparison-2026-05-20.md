# Unity MCP 비교 및 M1 적용 기록

## 조사 기준

- 조사 일자: 2026-05-20
- 현재 프로젝트 Unity 버전: `6000.4.6f1`
- 1차 목표: Codex와 Unity MCP를 연결해 작은 Unity 2D playable loop 개발 흐름을 검증한다.
- 주 MCP 클라이언트: Codex CLI
- 적용 대상 환경: M1 Mac, Unity `6000.4.6f1` 계열

이번 적용에서는 기능이 가장 많은 서버보다, Codex CLI와 project-local 설정이 단순하고 작은 하네스에서 검증하기 쉬운 서버를 우선했다.

## 평가 기준

| 항목 | 가중치 |
|---|---:|
| Codex 적합성 | 25% |
| 설치 단순성 | 20% |
| 보안/운영 리스크 | 15% |
| Unity 도구 충분성 | 15% |
| M1/macOS 적합성 | 10% |
| 유지보수 | 10% |
| 현재 Unity `6000.4.6f1` 호환성 | 5% |

## 점수표

| 후보 | 점수 | 핵심 판단 |
|---|---:|---|
| [`CoderGamester/mcp-unity`](https://github.com/CoderGamester/mcp-unity) | 8.2/10 | Codex CLI 설정, Unity 6 적합성, 단순한 Node 기반 구조가 현재 프로젝트에 가장 적합 |
| [`CoplayDev/unity-mcp`](https://github.com/CoplayDev/unity-mcp) | 8.0/10 | 도구 범위와 커뮤니티는 좋지만 telemetry, Python/uv, 더 큰 운영 표면이 부담 |
| [`IvanMurzak/Unity-MCP`](https://github.com/IvanMurzak/Unity-MCP) | 7.8/10 | Apple Silicon 지원과 기능은 강하지만 path 공백 제한, 자동 바이너리 다운로드, 고권한 기능이 부담 |

## 후보별 검토

### 1. CoderGamester/mcp-unity

- 설치 방식: Unity Package Manager에 Git dependency를 추가하고, Unity 메뉴 `Tools > MCP Unity > Server Window`에서 서버 설정을 생성한다.
- 적용 dependency: `com.gamelovers.mcp-unity`
- 고정 커밋: `a32e47d4ec8731685394dd562aa6f4f119f2bf79`
- 의존성: Unity 패키지와 Node.js 18 이상 중심의 구성이며, Python/uv 운영 부담이 없다.
- 도구/리소스: Console log 조회, Unity package/resource 조회, asset 조회, console log 전송 같은 smoke test에 필요한 조회성 기능을 우선 검증하기 좋다.
- 유지보수: [`tags`](https://github.com/CoderGamester/mcp-unity/tags)가 있고, 2026-05-18 기준 project-local Codex/Cursor/Claude Code auto-config 변경이 포함된 main 커밋을 사용할 수 있다.
- 보안/운영 리스크: telemetry는 확인되지 않았다. 기본 서버는 `localhost:8090`로 두고 원격 연결 옵션을 켜지 않으면 현재 하네스 목적에는 운영 표면이 작다.

판단: 이번 프로젝트의 1차 목표에는 기능 범위가 충분하고, Codex CLI project-local 설정 문서화가 가장 직접적이므로 우선 적용한다.

### 2. CoplayDev/unity-mcp

- 설치 방식: Unity 쪽 패키지와 별도 MCP 서버 구성을 함께 맞추는 방식이다.
- 의존성: Python/uv 기반 운영 요소가 있어 현재 경량 하네스에는 준비해야 할 도구가 더 많다.
- 도구/리소스: build, profiler, physics, VFX 등 광범위한 Unity 자동화 도구가 강점이다.
- 유지보수: [`tags`](https://github.com/CoplayDev/unity-mcp/tags)가 있고 커뮤니티/기능 범위는 세 후보 중 가장 강한 편이다.
- 보안/운영 리스크: telemetry와 넓은 도구 표면 때문에 작은 playable loop 검증 단계에서는 운영 정책을 더 분명히 해야 한다.

판단: 장기적으로는 가장 강한 후보일 수 있지만, 이번 M1 경량 검증에는 과하다. CoderGamester 적용 후 도구 한계가 분명해질 때 재검토한다.

### 3. IvanMurzak/Unity-MCP

- 설치 방식: Unity 통합과 서버 바이너리 구성을 포함하는 방식이다.
- 의존성: 자동 바이너리 다운로드 흐름이 있어 재현성과 감사 관점에서 추가 확인이 필요하다.
- 도구/리소스: Apple Silicon 지원과 넓은 Unity 조작 기능은 장점이다.
- 유지보수: 공개 README 기준으로 기능 설명과 설치 문서가 충분하다.
- 보안/운영 리스크: 경로 공백 제한, 자동 다운로드, 고권한 기능이 현재 프로젝트의 단순 검증 목적에는 부담이다.

판단: M1 지원은 매력적이지만, 현재 Windows 작업 경로와 향후 Mac 경로 모두에서 경로 제약을 신경 써야 한다. 이번 1차 적용에서는 보류한다.

## 최종 선택

1차 적용 후보는 `CoderGamester/mcp-unity`다.

현재 프로젝트의 `Packages/manifest.json`에는 다음 dependency를 추가한다.

```json
"com.gamelovers.mcp-unity": "https://github.com/CoderGamester/mcp-unity.git#a32e47d4ec8731685394dd562aa6f4f119f2bf79"
```

`Packages/packages-lock.json`은 Unity Package Manager가 패키지를 resolve할 때 생성 또는 갱신한다.

## 현재 적용 상태

- `Packages/manifest.json`에 `com.gamelovers.mcp-unity` dependency를 추가했다.
- `Packages/packages-lock.json`에는 같은 커밋 hash `a32e47d4ec8731685394dd562aa6f4f119f2bf79`로 resolve된 항목이 생성되어 있다.
- `.codex/config.toml`에는 project-local MCP 설정이 생성되어 있고, `Library/PackageCache/com.gamelovers.mcp-unity@a32e47d4ec87/Server~/build/index.js` 상대 경로를 사용한다.
- `ProjectSettings/McpUnitySettings.json`에는 `Port: 8090`, `AllowRemoteConnections: false`, `AutoStartServer: true`가 기록되어 있다.
- 위 설정 파일에서 비밀값이나 개인 절대경로는 확인되지 않았다.

## M1 적용 절차

1. M1 Mac에서 이 프로젝트를 Unity `6000.4.6f1` 계열로 연다.
2. Package Manager resolve가 끝날 때까지 기다린다.
3. Unity Console에 `com.gamelovers.mcp-unity` 관련 compile error가 없는지 확인한다.
4. `Tools > MCP Unity > Server Window`를 연다.
5. 기본 WebSocket 포트는 `8090`, bind는 `localhost`로 유지한다.
6. 원격 연결 옵션은 켜지 않는다.
7. 서버 창에서 설정 생성 또는 Configure 버튼을 실행한다.
8. 생성된 Codex CLI 설정은 project-local `.codex/config.toml`을 우선 사용한다.
9. 생성된 설정에 개인 절대경로가 들어가면 상대 경로로 바꾸고 이 문서나 후속 작업 로그에 기록한다.
10. Unity가 `ProjectSettings/McpUnitySettings.json`을 생성하면 `localhost`/`8090` 같은 기본 연결 정보만 있는지 확인한다. 비밀값이나 개인 절대경로가 있으면 커밋 전에 제거한다.

## Smoke Test

1. `Tools > MCP Unity > Server Window`에서 `Start Server`를 실행한다.
2. `localhost:8090` 연결 상태가 정상인지 확인한다.
3. Codex CLI에서 프로젝트 trust를 승인한다.
4. 파괴적 작업 없이 조회성 호출부터 검증한다.
   - `get_console_logs`
   - `unity://packages`
   - `unity://assets`
5. `send_console_log`로 `mcp smoke test`를 보낸다.
6. 다시 console log를 조회해 왕복 연결을 확인한다.

## 실패 시 기록할 정보

- 실패 단계
- Unity Console 오류
- MCP server log
- Node 버전
- Unity PackageCache 안의 `com.gamelovers.mcp-unity` 경로
- 생성된 `.codex/config.toml`의 경로 형식

## 근거 링크

- [CoderGamester README](https://github.com/CoderGamester/mcp-unity)
- [CoderGamester tags](https://github.com/CoderGamester/mcp-unity/tags)
- [CoplayDev README](https://github.com/CoplayDev/unity-mcp)
- [CoplayDev tags](https://github.com/CoplayDev/unity-mcp/tags)
- [IvanMurzak README](https://github.com/IvanMurzak/Unity-MCP)
