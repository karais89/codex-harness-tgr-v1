---
name: tiny-garden-playmode-check
description: Tiny Garden Restore Unity 검증 루틴. Use when Codex must check Unity MCP 연결 상태, active Scene/dirty 상태, Console error, PlayerMovement/RestoreTarget/GardenLoopController 구성, Tools/Codex/M1 Play Mode smoke 결과, 또는 MCP로 확인하지 못한 조작감/Game view/입력 재현 한계를 보고해야 할 때.
---

# Tiny Garden Playmode Check

## 개요

Tiny Garden Restore의 작은 Unity Play Mode 검증을 반복할 때 사용한다. 게임 코드, Scene, ProjectSettings를 수정하지 말고 조회와 기존 메뉴 실행만 수행한다.

## 절차

1. Unity MCP 연결을 확인한다.
   - `get_scene_info`가 응답하면 연결됨으로 본다.
   - 응답하지 않으면 실패로 기록하고 이후 Unity 조회는 진행하지 않는다.

2. Scene 상태를 확인한다.
   - active scene path가 `Assets/Scenes/SampleScene.unity`인지 확인한다.
   - `Is Dirty=false`인지 확인한다.

3. 스크립트와 Console error를 확인한다.
   - `recompile_scripts`를 실행한다.
   - `get_console_logs(logType=error, includeStackTrace=false)`로 error가 0개인지 확인한다.

4. 핵심 GameObject 구성을 확인한다.
   - `get_gameobject("TinyGardenRoot")` 또는 필요한 하위 경로 조회로 구조를 확인한다.
   - `TinyGardenRoot/Player`에 `PlayerMovement`가 있는지 확인한다.
   - `TinyGardenRoot/RestoreTargets/WeedTargetArea`, `WiltedFlowerTargetArea`, `DirtyTileTargetArea`에 각각 `RestoreTarget`이 있는지 확인한다.
   - `TinyGardenRoot/RestoreTargets`에 `GardenLoopController`가 있는지 확인한다.

5. 기존 Play Mode smoke 메뉴를 실행한다.
   - `execute_menu_item`으로 `Tools/Codex/M1/Run Play Mode Smoke Test`를 실행한다.
   - Console log에서 smoke test 완료 로그를 확인한다.
   - 실행 후 다시 Console error가 0개인지 확인한다.

## 판정 기준

- `통과`: MCP 조회 또는 기존 메뉴 실행 결과로 직접 확인된 항목.
- `실패`: 기대값과 다른 항목. 실패 항목에는 실제 값을 함께 적는다.
- `미확인`: MCP와 기존 smoke 메뉴만으로 직접 확인하지 못한 항목.

## 항상 미확인으로 남길 항목

- 실제 키보드 조작감.
- Game view에서 `Garden Restored`가 사람 눈에 읽기 좋게 보이는지.
- 별도 runtime smoke runner 없이 세 대상 전체 복구를 현재 세션에서 재연하는 것.

## 보고 형식

간단히 세 묶음으로 보고한다.

- `통과`: 확인된 항목과 핵심 값.
- `실패`: 실패 항목, 기대값, 실제 값.
- `미확인`: 위 한계 항목과 추가로 확인하지 못한 이유.

검증 과정에서 파일 저장, Scene 수정, ProjectSettings 변경, 새 runner 작성은 하지 않는다.
