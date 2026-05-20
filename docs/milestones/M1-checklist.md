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

- [ ] M1-01: Unity 프로젝트가 열립니다.
  - 확인 방법: Unity Editor에서 이 저장소 프로젝트가 열려 있는지 확인합니다.
  - 완료 증거: Unity Editor 프로젝트 경로 또는 열린 프로젝트 이름을 기록합니다.
- [ ] M1-02: MCP 패키지가 resolve됩니다.
  - 확인 방법: Package Manager resolve 후 `Packages/packages-lock.json`에 `com.gamelovers.mcp-unity`가 있고 Unity Console에 MCP 관련 compile error가 없는지 확인합니다.
  - 완료 증거: package lock entry, Unity Console error 개수, 주요 메시지를 기록합니다.
- [ ] M1-03: MCP 서버 설정이 local-only입니다.
  - 확인 방법: `ProjectSettings/McpUnitySettings.json`에서 `Port`가 `8090`, `AllowRemoteConnections`가 `false`인지 확인합니다.
  - 완료 증거: 설정값과 비밀값/개인 절대경로가 없다는 확인을 기록합니다.
- [ ] M1-04: Codex project-local 설정이 존재합니다.
  - 확인 방법: `.codex/config.toml`의 `mcp_servers.mcp-unity`가 `node`와 상대 PackageCache 경로를 사용하는지 확인합니다.
  - 완료 증거: command, args 경로 형식, 절대경로 없음 여부를 기록합니다.
- [ ] M1-05: Unity MCP 연결 상태를 확인합니다.
  - 확인 방법: `Tools > MCP Unity > Server Window`에서 서버를 시작하고 Codex MCP 응답 또는 연결 상태를 확인합니다.
  - 완료 증거: 연결 성공 메시지, MCP 응답, 또는 연결 상태 로그를 기록합니다.
- [ ] M1-06: Console log 조회와 log 왕복을 확인합니다.
  - 확인 방법: `get_console_logs`로 로그를 읽고, `send_console_log`로 `mcp smoke test`를 보낸 뒤 다시 조회합니다.
  - 완료 증거: 조회 결과와 `mcp smoke test` 로그를 기록합니다.
- [ ] M1-07: package / asset 리소스를 조회할 수 있습니다.
  - 확인 방법: `unity://packages`, `unity://assets` 같은 조회성 리소스를 확인합니다.
  - 완료 증거: 조회 성공 여부와 대표 응답을 기록합니다.
- [ ] M1-08: 현재 Scene 정보를 읽을 수 있습니다.
  - 확인 방법: Unity MCP 또는 Unity Editor로 현재 활성 Scene 이름과 경로를 조회합니다.
  - 완료 증거: 활성 Scene 이름과 경로를 기록합니다.
- [ ] M1-09: Console error를 확인할 수 있습니다.
  - 확인 방법: Unity MCP 또는 Unity Console에서 error 목록을 확인합니다.
  - 완료 증거: error 개수와 주요 메시지를 기록합니다. error가 없으면 `0개`로 기록합니다.
- [ ] M1-10: Play Mode 실행 가능 여부를 확인합니다.
  - 확인 방법: Unity MCP 또는 Unity Editor에서 Play Mode 진입 가능 여부를 확인합니다.
  - 완료 증거: Play Mode 진입 성공 여부와 실패 시 메시지를 기록합니다.

## 검증 증거

- 확인한 파일:
- 실행한 명령:
- Unity 또는 도구에서 확인한 결과:
- 확인 날짜:

## 미확인/예외

- 아직 Unity MCP 연결 smoke test를 수행하지 않았습니다.

## 최종 판정

- 판정: 미완료
- 판정 근거: M1 필수 체크리스트가 아직 검증되지 않았습니다.
- 다음 조치: Unity 프로젝트를 열고 CoderGamester Unity MCP로 연결 상태, Console log 왕복, package / asset 조회, 현재 Scene, Play Mode 가능 여부를 확인합니다.
