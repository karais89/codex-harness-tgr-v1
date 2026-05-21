# M7 Skill / Hooks 실험 결과 (2026-05-21)

## 목적

M6의 "작은 Unity 검증 Skill 1개 실험, Hooks 보류" 판단을 M7에서 실제로 확인했습니다. 이번 실험은 Tiny Garden Restore의 게임 기능을 고치지 않고, 반복 Unity 검증 루틴을 Codex skill로 묶을 가치가 있는지만 확인하는 범위로 제한했습니다.

## 생성한 Skill

- 경로: `.codex\skills\tiny-garden-playmode-check`
- 파일: `SKILL.md`, `agents/openai.yaml`
- 형태: instruction-only skill
- 만들지 않은 항목: `scripts/`, `assets/`, `references/`
- 기본 프롬프트: `Use $tiny-garden-playmode-check to verify Tiny Garden Restore in Unity.`

`SKILL.md`는 다음 검증만 수행하도록 작성했습니다.

- Unity MCP 연결 상태
- active scene path와 dirty 상태
- script recompile 결과와 Console error
- `PlayerMovement`, `RestoreTarget`, `GardenLoopController` 구성
- `Tools/Codex/M1/Run Play Mode Smoke Test` 실행 결과
- MCP만으로 확인하지 못한 조작감, Game view 판독, 전체 복구 재연 범위의 미확인 보고

## 구조 검증

- `skill-creator`의 `init_skill.py`로 skill을 생성했습니다.
- 처음 생성 위치는 사용자 글로벌 skill 경로였으나, 프로젝트 skill 의도에 맞춰 `.codex\skills\tiny-garden-playmode-check`로 이동했고 글로벌 복사본은 제거했습니다.
- 기본 Python 환경에서는 `yaml.safe_load`가 없는 `yaml` 모듈이 로드되어 `quick_validate.py`가 실패했습니다.
- 프로젝트와 전역 Python을 수정하지 않기 위해 `D:\tmp\m7-skill-validate-venv` 임시 venv를 만들고 PyYAML만 설치했습니다.
- 임시 venv에서 실행한 `quick_validate.py` 결과는 `Skill is valid!`입니다.
- 검증 후 해당 임시 venv는 삭제했습니다.

## 실제 사용 결과

생성한 `SKILL.md`를 직접 읽고 그 절차대로 Unity MCP 검증을 실행했습니다.

### 통과

- Unity MCP `get_scene_info`
  - active scene: `SampleScene`
  - path: `Assets/Scenes/SampleScene.unity`
  - `Is Dirty=false`
  - `Is Loaded=true`
- Unity MCP `recompile_scripts`
  - script recompile 성공
  - warning 0개
- Unity MCP `get_console_logs(logType=error, includeStackTrace=false)`
  - smoke 실행 전 error `[]`
  - smoke 실행 후 error `[]`
- Unity MCP `get_gameobject("TinyGardenRoot")`
  - `TinyGardenRoot/Player`에 `PlayerMovement` 존재
  - `WeedTargetArea`, `WiltedFlowerTargetArea`, `DirtyTileTargetArea`에 각각 `RestoreTarget` 존재
  - `TinyGardenRoot/RestoreTargets`에 `GardenLoopController` 존재
- Unity MCP `execute_menu_item`
  - `Tools/Codex/M1/Run Play Mode Smoke Test` 실행 성공
  - Console info log에서 `[M1 PlayMode Smoke] completed token=20260521T020256828Z` 확인

### 실패

- 없음.

### 미확인

- 실제 키보드 조작감.
- Game view에서 `Garden Restored`가 사람 눈에 읽기 좋게 보이는지.
- 별도 runtime smoke runner 없이 세 대상 전체 복구를 현재 세션에서 재연하는 것.
- 새 Codex 세션에서 skill이 자동 trigger되는지 여부.

## Hooks 판단

Hooks는 생성하지 않았습니다. M0~M5에서는 C# 변경 후 반복되는 기계적 검사 불편이 크지 않았고, 지금 Hooks를 만들면 playable loop 개선보다 하네스 설정이 커질 가능성이 큽니다.

다음 프로젝트에서도 기본값은 보류입니다. C# 변경 후 formatting, analyzer, 테스트 안내 같은 보고 전용 검사가 반복될 때만 다시 검토합니다.

## 다음 프로젝트 도입 판단

- Skill: 유지 후보입니다. Unity MCP로 scene, Console, 핵심 GameObject, 기존 smoke 메뉴를 확인하는 반복 작업을 작게 묶는 데 도움이 됐습니다.
- Hooks: 보류합니다. 현재 반복 비용보다 설정 비용과 운영 복잡도가 더 큽니다.

## 최종 판정

Skill 실험 완료, Hooks 보류.

게임 코드, Scene, ProjectSettings는 수정하지 않았습니다.
