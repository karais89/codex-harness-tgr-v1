# M4 체크리스트 - 복구 대상 상호작용 구현

## 목적

이 문서는 `docs/project-goal.md`의 `M4. 복구 대상 상호작용 구현` 완료 기준을 작은 확인 항목으로 나누어, M4 완료 여부를 체크리스트만으로 판정하기 위해 작성합니다.

M4의 목표는 Player가 정원 안의 복구 대상과 상호작용하고, 상호작용 후 복구 대상의 상태가 바뀌게 하는 것입니다.

## 완료 판정 규칙

- 필수 체크리스트의 모든 항목이 완료되어야 M4를 완료로 판정합니다.
- 각 항목은 복구 대상 오브젝트, 상호작용 방식, 상태 변화, Play Mode 검증 증거를 함께 남깁니다.
- 상호작용 후 상태 변화가 Scene에서 보이지 않거나 Console error가 있으면 M4를 완료로 판정하지 않습니다.
- M4는 `잡초`, `시든 꽃`, `더러운 타일` 중 하나 이상의 복구 대상에 대해 `근처 거리 조건 + E 1회 입력 즉시 복구` 상호작용을 확인하는 단계이며, 세 대상 완료 메시지는 M5 항목으로 남깁니다.

## 필수 체크리스트

- [x] M4-01: 복구 대상 오브젝트가 존재합니다.
  - 확인 방법: Unity Hierarchy에서 복구 대상 역할의 오브젝트를 확인합니다.
  - 완료 증거: `TinyGardenRoot/RestoreTargets/WeedTargetArea`가 존재하며 위치는 `(-1.75, 1.2, 0)`, Scene 경로는 `Assets/Scenes/SampleScene.unity`입니다.
- [x] M4-02: Player가 복구 대상과 상호작용할 수 있습니다.
  - 확인 방법: Play Mode에서 Player가 복구 대상 근처에 있을 때 `E` 1회 입력으로 즉시 복구되는지 확인합니다.
  - 완료 증거: 임시 Play Mode smoke runner에서 Player를 `WeedTargetArea` 위치로 이동해 거리 `0`, `interactionDistance=1` 조건을 만들고, Input System 가상 키보드의 `E` 1회 입력 상태를 주입했습니다. 로그 확인: `isPressed=True`, `wasPressedThisFrame=True`, `PASS WeedTargetArea SpriteRenderer.enabled == false after one E input`.
- [x] M4-03: 상호작용 후 복구 대상의 상태가 바뀝니다.
  - 확인 방법: 상호작용 전후의 오브젝트 상태를 비교합니다.
  - 완료 증거: 상호작용 후 `WeedTargetArea`의 `SpriteRenderer.enabled`가 `false`가 되어 잡초 스프라이트가 비활성화됩니다.
- [x] M4-04: 상태 변화가 Scene에서 확인됩니다.
  - 확인 방법: Unity Scene 또는 Game view에서 상태 변화가 시각적으로 확인되는지 봅니다.
  - 완료 증거: Play Mode smoke runner가 Scene 내 `WeedTargetArea`의 `SpriteRenderer.enabled == false`를 확인했습니다. 별도 화면 캡처는 남기지 않았습니다.
- [x] M4-05: Play Mode에서 확인 가능합니다.
  - 확인 방법: Unity Play Mode에서 처음부터 상호작용까지 직접 실행합니다.
  - 완료 증거: Unity Play Mode에서 `SampleScene`을 열고 임시 smoke runner로 Player 위치 이동, `E` 1회 입력 주입, `RestoreTarget` 실행 결과를 확인했습니다. 검증용 임시 파일은 최종 diff에서 제거했습니다.
- [x] M4-06: Console error가 없습니다.
  - 확인 방법: Play Mode 실행 전후 Unity Console error를 확인합니다.
  - 완료 증거: 최종 `get_console_logs(logType=error)` 결과가 빈 배열이며 Console error는 `0개`입니다.

## 검증 증거

- 확인한 파일:
  - `Assets/Scripts/RestoreTarget.cs`
  - `Assets/Scenes/SampleScene.unity`
  - `docs/milestones/M4-checklist.md`
- 실행한 명령/도구:
  - Unity MCP `recompile_scripts`: 최종 0 warning, 0 error
  - Unity MCP `get_gameobject("TinyGardenRoot/Player")`: `PlayerMovement` 유지 확인
  - Unity MCP `get_gameobject("TinyGardenRoot/RestoreTargets/WeedTargetArea")`: `SpriteRenderer`, `RestoreTarget`, `player=Player`, `interactionDistance=1` 확인
  - Unity MCP `get_console_logs(logType=error)`: `[]`
  - 임시 Play Mode smoke runner: `E` 1회 입력 상태 주입 후 `WeedTargetArea SpriteRenderer.enabled == false` 확인
- Unity 또는 도구에서 확인한 결과:
  - `WeedTargetArea`에 `RestoreTarget`이 연결되었습니다.
  - `RestoreTarget.player`는 `TinyGardenRoot/Player`를 참조합니다.
  - `WiltedFlowerTargetArea`, `DirtyTileTargetArea`는 M5 범위로 남겨 두고 변경하지 않았습니다.
  - 검증용 임시 smoke runner 파일은 삭제되어 최종 diff에 남지 않습니다.
- 확인 날짜: 2026-05-21 KST

## 미확인/예외

- 수동 키보드 조작 대신 Unity MCP 환경에서 임시 Play Mode smoke runner를 사용했습니다. MCP로 실제 키 입력을 직접 보내기 어려워 Input System 가상 키보드 상태를 주입해 `E` 1회 입력 조건을 검증했습니다.
- 세 복구 대상 전체 처리와 `Garden Restored` 표시는 M5 범위입니다.

## 최종 판정

- 판정: 완료
- 판정 근거: `WeedTargetArea`에서 `근처 거리 조건 + E 1회 입력 + 즉시 SpriteRenderer 비활성화`가 Play Mode smoke runner로 검증되었고, 최종 Console error가 `0개`입니다.
- 다음 조치: M5에서 나머지 복구 대상 처리와 전체 복구 완료 표시를 구현합니다.
