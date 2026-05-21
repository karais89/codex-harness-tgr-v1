# M5 체크리스트 - 첫 playable loop 완성

## 목적

이 문서는 `docs/project-goal.md`의 `M5. 첫 playable loop 완성` 완료 기준을 작은 확인 항목으로 나누어, M5 완료 여부를 체크리스트만으로 판정하기 위해 작성합니다.

M5의 목표는 Tiny Garden Restore의 아주 작은 게임 루프를 처음부터 끝까지 플레이 가능한 상태로 완성하는 것입니다.

## 완료 판정 규칙

- 필수 체크리스트의 모든 항목이 완료되어야 M5를 완료로 판정합니다.
- 각 항목은 시작 상태, 플레이어 행동, 시작 시점부터 보이는 `잡초`/`시든 꽃`/`더러운 타일`, 세 대상 완료 조건, `Garden Restored` 완료 표시, Play Mode 검증 증거를 함께 남깁니다.
- Unity Play Mode에서 처음부터 끝까지 확인하지 못하거나 Console error가 있으면 M5를 완료로 판정하지 않습니다.
- M5는 작은 playable loop 완성이 목표이며, 복잡한 성장 시스템, 인벤토리, 상점, 여러 스테이지, 세이브/로드는 완료 기준에 포함하지 않습니다.

## 필수 체크리스트

- [x] M5-01: 시작 상태가 있습니다.
  - 확인 방법: Play Mode 시작 시 Player와 복구 대상들이 초기 상태로 배치되는지 확인합니다.
  - 완료 증거: `Assets/Scenes/SampleScene.unity`에서 `TinyGardenRoot/Player`가 시작 위치 `(-2, -1.55, 0)`에 있고, `RestoreTargets` 하위 세 대상이 모두 active 상태로 시작함을 Unity MCP `get_gameobject`로 확인했습니다.
- [x] M5-02: 플레이어 행동이 있습니다.
  - 확인 방법: Play Mode에서 Player 이동 또는 필요한 기본 행동을 확인합니다.
  - 완료 증거: `PlayerMovement`가 WASD/방향키 이동을 처리하고, Play Mode smoke runner에서 Player를 각 대상 위치로 이동시킨 뒤 Input System `E` 1회 입력으로 상호작용을 확인했습니다.
- [x] M5-03: `잡초`, `시든 꽃`, `더러운 타일` 복구 대상이 있습니다.
  - 확인 방법: Unity Hierarchy 또는 Game view에서 세 복구 대상이 시작 시점부터 모두 보이는지 확인합니다.
  - 완료 증거: `TinyGardenRoot/RestoreTargets/WeedTargetArea`, `WiltedFlowerTargetArea`, `DirtyTileTargetArea`가 모두 active이고 `SpriteRenderer.enabled=true`로 시작함을 확인했습니다.
- [x] M5-04: 세 복구 대상 완료 조건이 있습니다.
  - 확인 방법: `잡초`, `시든 꽃`, `더러운 타일` 처리 여부를 모두 판정하는 조건이 있는지 확인합니다.
  - 완료 증거: 세 대상 모두 `RestoreTarget`을 갖고 `player=Player`, `interactionDistance=1`로 설정되어 있습니다. `RestoreTargets`의 `GardenLoopController`가 자식 `RestoreTarget.IsRestored` 값을 모두 확인해 `IsComplete=true`로 전환합니다.
- [x] M5-05: 완료 결과가 표시됩니다.
  - 확인 방법: 모든 필수 복구 대상 처리 후 `Garden Restored` 단순 텍스트가 표시되는지 확인합니다.
  - 완료 증거: `GardenLoopController.OnGUI`가 완료 후 화면 상단 중앙에 `Garden Restored` 텍스트를 표시합니다. Play Mode smoke runner에서 `Garden Restored display condition=True`를 확인했습니다.
- [x] M5-06: Unity Play Mode에서 처음부터 끝까지 확인 가능합니다.
  - 확인 방법: Play Mode에서 시작, 이동, 복구 상호작용, 완료 표시까지 한 흐름으로 실행합니다.
  - 완료 증거: 임시 Play Mode smoke runner로 `WeedTargetArea`, `WiltedFlowerTargetArea`, `DirtyTileTargetArea` 순서로 Player 이동 후 Input System `E` 1회 입력을 주입했습니다. 세 대상 모두 `IsRestored=True`, `GardenLoopController.IsComplete=True`를 확인했습니다. 검증용 임시 파일은 제거했습니다.
- [x] M5-07: Console error가 없습니다.
  - 확인 방법: 전체 playable loop 실행 전후 Unity Console error를 확인합니다.
  - 완료 증거: 최종 Unity MCP `get_console_logs(logType=error)` 결과 `[]`로 Console error `0개`를 확인했습니다.

## 검증 증거

- 확인한 파일: `Assets/Scripts/RestoreTarget.cs`, `Assets/Scripts/GardenLoopController.cs`, `Assets/Scenes/SampleScene.unity`, `docs/milestones/M5-checklist.md`
- 실행한 명령/도구: Unity MCP `recompile_scripts`, `get_gameobject`, `get_scene_info`, `get_console_logs`, 임시 Play Mode smoke runner
- Unity 또는 도구에서 확인한 결과: script recompile `0 warning(s)`, Console error `0개`, Scene `Is Dirty=false`, `RestoreTargets`에 `GardenLoopController` 있음, 세 대상 모두 `RestoreTarget`과 `player=Player`, `interactionDistance=1` 설정됨, Play Mode smoke 결과 세 대상 `IsRestored=True` 및 `GardenLoopController.IsComplete=True`
- 확인 날짜: 2026-05-21

## 미확인/예외

- 없음.

## 최종 판정

- 판정: 완료
- 판정 근거: M5 필수 체크리스트 M5-01부터 M5-07까지 모두 구현 및 검증 완료했습니다.
- 다음 조치: M6 범위에서만 다음 기능을 진행합니다.
