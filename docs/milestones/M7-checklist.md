# M7 체크리스트 - 선택 실험: Skill / Hooks 검토

## 목적

이 문서는 `docs/project-goal.md`의 `M7. 선택 실험: Skill / Hooks 검토` 완료 기준을 작은 확인 항목으로 나누어, M7 진행 여부와 완료 여부를 체크리스트만으로 판정하기 위해 작성합니다.

M7의 목표는 1차 playable loop 완료 후 M6 평가에서 필요성이 확인된 항목만 작게 실험하는 것입니다. 이번 M7에서는 M6 결론에 따라 작은 Unity 검증 Skill 1개만 실험하고 Hooks는 보류했습니다.

## 완료 판정 규칙

- M7은 필수 마일스톤이 아니므로 M6 평가 전에는 `보류`로 둡니다.
- M6 평가에서 Skill 또는 Hooks 필요성이 확인된 항목만 진행합니다.
- 각 실험은 작게 진행해야 하며, playable loop 개선보다 하네스 설정이 커지면 중단합니다.
- 실험 결과가 다음 프로젝트 판단에 도움이 되어야 M7을 완료로 판정합니다.
- M6 평가에서 필요성이 없다고 판단되면, 실험을 하지 않고 `진행하지 않음`으로 판정할 수 있습니다.

## 필수 체크리스트

- [x] M7-01: M6 평가에서 필요성이 확인된 항목만 진행합니다.
  - 확인 방법: M6 평가 결과에서 Skill / Hooks 필요 여부를 확인했습니다.
  - 완료 증거: `docs/reports/m6-lightweight-harness-evaluation-2026-05-21.md`에서 작은 Unity 검증 Skill 1개 실험, Hooks 보류를 권고했습니다.
- [x] M7-02: Skill 실험 여부를 결정합니다.
  - 확인 방법: 반복되는 Unity 검증 작업이 있었는지 확인했습니다.
  - 완료 증거: Console error, Scene dirty 상태, 핵심 GameObject 구성, Play Mode smoke 결과 확인이 반복되어 Skill 실험을 진행했습니다.
- [x] M7-03: Skill을 진행한다면 작게 만듭니다.
  - 확인 방법: instruction-only skill로 제한하고 별도 `scripts/`, `assets/`, `references/`를 만들지 않았습니다.
  - 완료 증거: `.codex\skills\tiny-garden-playmode-check`에 `SKILL.md`, `agents/openai.yaml`만 생성했습니다.
- [x] M7-04: Hooks 실험 여부를 결정합니다.
  - 확인 방법: C# 파일 변경 후 반복되는 기계적 검사가 있었는지 확인했습니다.
  - 완료 증거: M6 판단대로 현재 반복 불편이 작아 Hooks는 보류했습니다.
- [x] M7-05: Hooks를 진행한다면 보고 전용으로 시작합니다.
  - 확인 방법: Hooks를 진행하지 않았으므로 hook 파일, 자동 수정, 자동 실행을 만들지 않았습니다.
  - 완료 증거: 생성한 hook 경로 없음. 자동 수정 없음.
- [x] M7-06: 각 실험은 다음 프로젝트 판단에 도움이 됩니다.
  - 확인 방법: 생성한 Skill을 직접 읽고 Unity MCP 검증에 한 번 사용했습니다.
  - 완료 증거: Skill은 작은 Unity 상태 검증 체크리스트로 유지할 가치가 있고, Hooks는 반복 비용이 커질 때 재검토하기로 기록했습니다.
- [x] M7-07: playable loop 개선보다 하네스 설정이 커지면 중단합니다.
  - 확인 방법: 게임 코드, Scene, ProjectSettings를 수정하지 않고 조회와 기존 메뉴 실행만 수행했습니다.
  - 완료 증거: Skill은 instruction-only로 유지했고 Hooks는 만들지 않아 범위가 작게 유지되었습니다.

## 검증 증거

- 확인한 파일:
  - `docs/reports/m6-lightweight-harness-evaluation-2026-05-21.md`
  - `.codex\skills\tiny-garden-playmode-check\SKILL.md`
  - `.codex\skills\tiny-garden-playmode-check\agents\openai.yaml`
  - `docs/reports/m7-skill-hooks-experiment-2026-05-21.md`
- 실행한 명령:
  - `python C:\Users\Lonpeach\.codex\skills\.system\skill-creator\scripts\init_skill.py tiny-garden-playmode-check --path C:\Users\Lonpeach\.codex\skills ...`
  - `Move-Item <기존 글로벌 skill 경로> .codex\skills\tiny-garden-playmode-check`
  - `D:\tmp\m7-skill-validate-venv\Scripts\python.exe C:\Users\Lonpeach\.codex\skills\.system\skill-creator\scripts\quick_validate.py .codex\skills\tiny-garden-playmode-check`
- Unity 또는 도구에서 확인한 결과:
  - `quick_validate.py`: `Skill is valid!`
  - Unity MCP `get_scene_info`: active scene `Assets/Scenes/SampleScene.unity`, `Is Dirty=false`, `Is Loaded=true`
  - Unity MCP `recompile_scripts`: script recompile 성공, warning 0개
  - Unity MCP `get_console_logs(logType=error, includeStackTrace=false)`: smoke 전후 error `[]`
  - Unity MCP `get_gameobject("TinyGardenRoot")`: `PlayerMovement`, 세 `RestoreTarget`, `GardenLoopController` 존재
  - Unity MCP `execute_menu_item`: `Tools/Codex/M1/Run Play Mode Smoke Test` 실행 성공
  - Unity Console info log: `[M1 PlayMode Smoke] completed token=20260521T020256828Z`
- 확인 날짜: 2026-05-21 KST

## 미확인/예외

- 새 skill의 자동 trigger 여부는 새 Codex 세션에서 확인하는 편이 정확하므로 이번 M7에서는 직접 `SKILL.md`를 읽어 사용한 결과까지만 확인했습니다.
- 처음 생성 위치는 사용자 글로벌 skill 경로였으나, 프로젝트 skill 의도에 맞춰 `.codex\skills\tiny-garden-playmode-check`로 이동했고 글로벌 복사본은 제거했습니다.
- 기본 Python 환경에서는 `yaml.safe_load`가 없는 `yaml` 모듈이 잡혀 `quick_validate.py`가 실패했습니다. 프로젝트나 전역 Python을 수정하지 않고 `D:\tmp\m7-skill-validate-venv` 임시 venv에 PyYAML을 설치해 검증을 통과시킨 뒤, 해당 임시 venv는 삭제했습니다.
- 실제 키보드 조작감은 MCP와 기존 smoke 메뉴만으로 직접 확인하지 못했습니다.
- Game view에서 `Garden Restored`가 사람 눈에 읽기 좋게 보이는지는 직접 확인하지 못했습니다.
- 별도 runtime smoke runner 없이 세 대상 전체 복구를 현재 세션에서 재연하는 것은 확인하지 않았습니다.

## 최종 판정

- 판정: Skill 실험 완료, Hooks 보류
- 판정 근거: M6 권고에 따라 작은 Unity 검증 Skill을 생성하고 실제 Unity MCP 검증에 사용했습니다. Hooks는 현재 반복 불편이 작고 하네스 복잡도를 키울 가능성이 있어 만들지 않았습니다.
- 다음 조치: 다음 Unity 프로젝트에서 반복 검증이 다시 필요하면 `tiny-garden-playmode-check`를 작은 체크리스트로 재사용하고, Hooks는 C# 변경 후 기계적 검사가 반복될 때 다시 검토합니다.
