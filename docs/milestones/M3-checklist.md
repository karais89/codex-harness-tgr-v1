# M3 체크리스트 - Player 이동 구현

## 목적

이 문서는 `docs/project-goal.md`의 `M3. Player 이동 구현` 완료 기준을 작은 확인 항목으로 나누어, M3 완료 여부를 체크리스트만으로 판정하기 위해 작성합니다.

M3의 목표는 작은 정원 안에서 Player가 키보드 입력으로 움직일 수 있게 하는 것입니다.

## 완료 판정 규칙

- 필수 체크리스트의 모든 항목이 완료되어야 M3를 완료로 판정합니다.
- 각 항목은 Player 오브젝트, 연결된 이동 스크립트, Play Mode 검증 증거를 함께 남깁니다.
- 키보드 입력 이동을 Play Mode에서 확인하지 못하거나 Console error가 남아 있으면 M3를 완료로 판정하지 않습니다.
- M3는 Player 이동까지만 다루며, 복구 대상 상호작용은 M4 항목으로 남깁니다.

## 필수 체크리스트

- [x] M3-01: Player 오브젝트가 존재합니다.
  - 확인 방법: Unity MCP `get_gameobject`로 `TinyGardenRoot/Player`를 조회했습니다.
  - 완료 증거: Scene 경로는 `Assets/Scenes/SampleScene.unity`, 오브젝트 이름은 `Player`입니다.
- [x] M3-02: Player에 이동 스크립트가 연결됩니다.
  - 확인 방법: Unity MCP `get_gameobject`로 Player 컴포넌트 목록을 확인했습니다.
  - 완료 증거: `Assets/Scripts/PlayerMovement.cs`가 `PlayerMovement` 컴포넌트로 연결되어 있고 `moveSpeed`는 `2.5`입니다.
- [x] M3-03: 키보드 입력으로 이동할 수 있습니다.
  - 확인 방법: Play Mode에서 임시 Editor smoke runner로 Input System `W` 키 상태를 주입하고, Unity MCP `get_gameobject`로 Player 위치 변화를 확인했습니다.
  - 완료 증거: `W` 입력 주입 후 Player 위치가 `(-2.00, -1.55, 0.00)`에서 `(-2.00, -1.50, 0.00)`로 위쪽으로 이동했습니다.
- [x] M3-04: Play Mode에서 동작을 확인합니다.
  - 확인 방법: Unity Editor Play Mode에 진입한 뒤 Player 이동 결과를 확인하고 Edit Mode로 복귀했습니다.
  - 완료 증거: Unity Console에 `[M3 PlayerMovement Smoke] entered Play Mode initial=(-2.00, -1.55, 0.00)` 로그가 남았고, Play Mode 중 MCP 조회에서 Player의 `y` 좌표 증가를 확인했습니다.
- [x] M3-05: Console error가 없습니다.
  - 확인 방법: 최종 상태에서 Unity MCP `get_console_logs`를 `logType=error`, `includeStackTrace=false`로 조회했습니다.
  - 완료 증거: 최종 error 로그 결과는 `[]`, 즉 `0개`입니다.

## 검증 증거

- 확인한 파일:
  - `Assets/Scripts/PlayerMovement.cs`
  - `Assets/Scenes/SampleScene.unity`
  - `docs/milestones/M3-checklist.md`
- 실행한 명령:
  - `git status --short`
  - `rg --files`
  - Unity MCP `execute_menu_item`: `Assets/Refresh`
  - Unity MCP `recompile_scripts`
  - Unity MCP `get_scene_info`
  - Unity MCP `update_component`: `TinyGardenRoot/Player`에 `PlayerMovement` 연결
  - Unity MCP `get_gameobject`: `TinyGardenRoot/Player` 조회
  - Unity MCP `get_console_logs`: error 로그 조회
- Unity 또는 도구에서 확인한 결과:
  - active scene은 `Assets/Scenes/SampleScene.unity`입니다.
  - `TinyGardenRoot/Player`에 `Transform`, `SpriteRenderer`, `PlayerMovement`가 연결되어 있습니다.
  - Play Mode 중 `W` 입력 주입으로 Player `y` 좌표가 `-1.55`에서 `-1.50`으로 증가했습니다.
  - 최종 Console error는 `0개`입니다.
- 확인 날짜:
  - 2026-05-21 00:03 KST, Unity Console/MCP 로그 기준

## 미확인/예외

- MCP에서 실제 물리 키를 누르는 방식은 사용할 수 없어, Unity Input System의 `W` 키 상태를 Play Mode에서 주입해 이동을 검증했습니다.
- 검증 중 잘못된 Unity 메뉴 경로 `Edit/Play` 실행 시도가 일시적으로 Console error를 만들었지만, 이는 프로젝트 코드 오류가 아니며 Console을 정리한 뒤 최종 error `0개`를 재확인했습니다.

## 최종 판정

- 판정: 완료
- 판정 근거: M3 필수 체크리스트 M3-01부터 M3-05까지 모두 완료되었고, Player 이동 및 최종 Console error `0개`를 확인했습니다.
- 다음 조치: M4에서 정원 경계, 충돌, 복구 대상 상호작용 등 다음 범위 기능을 구현합니다.
