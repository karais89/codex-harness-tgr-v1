# M1 체크리스트 - Unity MCP 연결 확인

## 목적

이 문서는 `docs/project-goal.md`의 `M1. Unity MCP 연결 확인` 완료 기준을 작은 확인 항목으로 나누어, M1 완료 여부를 체크리스트만으로 판정하기 위해 작성합니다.

M1의 목표는 Codex가 Unity MCP를 통해 Unity Editor 상태를 확인할 수 있는지 검증하는 것입니다.

## 완료 판정 규칙

- 필수 체크리스트의 모든 항목이 완료되어야 M1을 완료로 판정합니다.
- 각 항목은 Unity MCP 또는 Unity Editor에서 확인한 방법과 완료 증거를 함께 남깁니다.
- Unity MCP 연결, Scene 정보, Console error, Play Mode 가능 여부 중 하나라도 확인하지 못하면 M1을 완료로 판정하지 않습니다.
- 파일을 수정하지 않는 확인 작업이므로, 변경 파일이 생기면 이유를 `미확인/예외`에 기록합니다.

## 필수 체크리스트

- [ ] M1-01: Unity 프로젝트가 열립니다.
  - 확인 방법: Unity Editor에서 이 저장소 프로젝트가 열려 있는지 확인합니다.
  - 완료 증거: Unity Editor 프로젝트 경로 또는 열린 프로젝트 이름을 기록합니다.
- [ ] M1-02: Unity MCP 연결 상태를 확인합니다.
  - 확인 방법: Unity MCP 도구로 Editor 연결 상태를 조회합니다.
  - 완료 증거: 연결 성공 메시지, MCP 응답, 또는 연결 상태 로그를 기록합니다.
- [ ] M1-03: 현재 Scene 정보를 읽을 수 있습니다.
  - 확인 방법: Unity MCP로 현재 활성 Scene 이름과 경로를 조회합니다.
  - 완료 증거: 활성 Scene 이름과 경로를 기록합니다.
- [ ] M1-04: Console error를 확인할 수 있습니다.
  - 확인 방법: Unity MCP 또는 Unity Console에서 error 목록을 확인합니다.
  - 완료 증거: error 개수와 주요 메시지를 기록합니다. error가 없으면 `0개`로 기록합니다.
- [ ] M1-05: Play Mode 실행 가능 여부를 확인합니다.
  - 확인 방법: Unity MCP 또는 Unity Editor에서 Play Mode 진입 가능 여부를 확인합니다.
  - 완료 증거: Play Mode 진입 성공 여부와 실패 시 메시지를 기록합니다.

## 검증 증거

- 확인한 파일:
- 실행한 명령:
- Unity 또는 도구에서 확인한 결과:
- 확인 날짜:

## 미확인/예외

- 아직 Unity MCP 연결 확인을 수행하지 않았습니다.

## 최종 판정

- 판정: 미완료
- 판정 근거: M1 필수 체크리스트가 아직 검증되지 않았습니다.
- 다음 조치: Unity 프로젝트를 열고 Unity MCP로 연결 상태, 현재 Scene, Console error, Play Mode 가능 여부를 확인합니다.
