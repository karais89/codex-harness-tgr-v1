# M6 경량 하네스 평가 (2026-05-21)

## 목적

이 문서는 M0부터 M5까지의 결과를 기준으로, Tiny Garden Restore v1의 경량 Codex 하네스가 1차 목적에 충분했는지 평가합니다.

이번 평가는 저장소 증거만으로 판정하지 않습니다. 사용자가 확정한 판단을 1차 근거로 두고, M0~M5 체크리스트와 Unity MCP 최신 조회 결과를 보조 증거로 사용합니다.

## 최종 판단

- 판정: 충분
- 이유: M0~M5를 완료했고, 작은 Unity 2D playable loop를 `AGENTS.md`, Codex 기본 Plan mode, ExecPlan 원문 참조, Unity MCP, 짧은 프롬프트 중심의 경량 구성으로 끝까지 구현하고 검증했습니다.
- 유지할 항목: `AGENTS.md`, Codex 기본 Plan mode, Unity MCP, 3줄 이하 작업 프롬프트, 한글 문서/보고 규칙
- ExecPlan 판단: 기본값으로 쓰지 않고, 복합 기능이나 큰 리팩터링에서만 참조합니다.
- 주요 한계: MCP와 자동 검증만으로 실제 화면 판독 품질을 충분히 보장하기 어렵습니다.
- M7 권고: 비교 가치 확인을 위해 작은 Unity 검증 Skill 실험 1개를 진행하고, Hooks는 보류합니다.

## 사용자 판단 요약

이번 M6의 기준 판단은 다음과 같습니다.

- M0~M5를 완주했으므로 현재 경량 하네스는 1차 목적에 충분했습니다.
- `AGENTS.md`는 범위 통제, 한국어 문서 규칙, ExecPlan 사용 조건을 잡는 기본 규칙으로 유지할 가치가 있습니다.
- Codex 기본 Plan mode와 3줄 이하 프롬프트는 작은 Unity 작업을 나누고 검증 결과를 요구하는 데 충분했습니다.
- ExecPlan은 유용하지만 상시 기본값으로 쓰면 무겁습니다. 복합 작업이나 큰 리팩터링에서만 참조합니다.
- Unity MCP는 Scene, GameObject, Console 상태 확인에 실질적으로 도움이 되었지만, 실제 화면 판독과 조작감 확인은 별도 보완이 필요합니다.
- Skill은 다음 단계에서 작은 Unity 검증용으로 1개만 실험할 가치가 있고, Hooks는 현재 반복 불편이 크지 않아 보류합니다.

## M0~M5 검토 요약

| 마일스톤 | 판정 | 근거 요약 |
| --- | --- | --- |
| M0 기준 문서 정리 | 완료 | `README.md`, `AGENTS.md`, `docs/project-goal.md`, `.agent/PLANS.md`가 존재하고, 경량 하네스 실험 목적이 문서화되었습니다. |
| M1 Unity MCP 연결 확인 | 완료 | `com.gamelovers.mcp-unity` resolve, `localhost:8090` MCP 응답, Console log 왕복, package / asset 조회, Scene 정보, Play Mode smoke test를 확인했습니다. |
| M1.5 기획/아트 기준 정리 | 완료 | 기획 문서, 아트 컨셉, 이미지 프롬프트, 컨셉 이미지, 확정 결정 기록이 준비되었고 M2~M5 구현 기준이 고정되었습니다. |
| M2 Tiny Garden 기본 Scene 구성 | 완료 | `SampleScene`에 `TinyGardenRoot`, `GardenArea`, `Player`, 세 복구 대상 구역이 있고, compact square layout과 저장 상태를 확인했습니다. |
| M3 Player 이동 구현 | 완료 | `PlayerMovement`가 `Player`에 연결되었고, Play Mode smoke runner로 입력 주입 후 위치 변화를 확인했습니다. |
| M4 복구 대상 상호작용 구현 | 완료 | `WeedTargetArea`에서 근처 거리 조건과 `E` 1회 입력으로 즉시 복구되는 흐름을 Play Mode에서 확인했습니다. |
| M5 첫 playable loop 완성 | 완료 | 세 복구 대상 모두 `RestoreTarget`을 갖고, `GardenLoopController`가 전체 완료 조건과 `Garden Restored` 표시를 관리하며, 끝까지 Play Mode 검증했습니다. |

## 최신 Unity 조회 증거

M6 실행 중 Unity는 조회만 수행했습니다.

- Unity MCP `get_scene_info`: active scene은 `SampleScene`, path는 `Assets/Scenes/SampleScene.unity`, `Build Index=0`, `Is Dirty=false`, `Is Loaded=true`, `Root Count=3`입니다.
- Unity MCP `get_console_logs(logType=error, includeStackTrace=false)`: `[]`, Console error `0개`입니다.
- Unity MCP `get_gameobject("TinyGardenRoot")`: `TinyGardenRoot`가 active 상태이며, 하위에 `RestoreTargets`, `GardenArea`, `Player`가 있습니다. `RestoreTargets`에는 `GardenLoopController`가 있고, `WeedTargetArea`, `WiltedFlowerTargetArea`, `DirtyTileTargetArea`는 모두 `SpriteRenderer`와 `RestoreTarget`을 갖습니다.

## 하네스 항목별 평가

| 항목 | 실제 사용 여부 | 도움이 된 시점 | 복잡도 증가 여부 | 다음 프로젝트 유지 여부 | 보강 필요 여부 |
| --- | --- | --- | --- | --- | --- |
| `AGENTS.md` | 사용했습니다. | 변경 범위 통제, 한국어 문서 규칙, ExecPlan 사용 조건, 검증 중심 진행을 정하는 데 도움이 되었습니다. | 낮습니다. 저장소 기본 규칙으로 충분했습니다. | 유지합니다. | 현재 수준으로 충분합니다. |
| Codex 기본 Plan mode | 사용했습니다. | 구현 전 계획, 단계별 확인, 완료 보고에서 변경 파일과 Unity 검증 결과를 묶는 데 도움이 되었습니다. | 낮습니다. 별도 workflow 없이도 작은 작업을 나누기에 충분했습니다. | 유지합니다. | 큰 작업에서는 ExecPlan 참조만 추가합니다. |
| ExecPlan 원문 참조 | 제한적으로 사용했습니다. | M2~M5를 한 번에 묶어 실험한 보고서에서 절차와 증거 기록에는 도움이 되었습니다. | 기본값으로 쓰면 높습니다. 작은 마일스톤에는 과합니다. | 참조 파일로 유지합니다. | 복합 작업이나 큰 리팩터링에서만 사용합니다. |
| Unity MCP | 사용했습니다. | MCP 연결, Console error 조회, package / asset 확인, Scene 저장 상태, GameObject 구성, Play Mode smoke 증거 확인에 도움이 되었습니다. | 중간입니다. Unity 상태를 직접 조회할 수 있어 비용 대비 효용이 컸지만, 검증 runner와 실제 조작 사이의 차이는 남았습니다. | 유지합니다. | 화면 판독 품질은 screenshot 또는 사람 검수로 보강합니다. |
| 3줄 이하 작업 프롬프트 | 사용했습니다. | M1~M5처럼 한 번에 하나의 목표를 지시하고, 단순 구현과 검증 보고를 요구하는 데 충분했습니다. | 낮습니다. 지시가 짧아 범위 확장을 줄였습니다. | 유지합니다. | 여러 마일스톤을 한 번에 묶는 요청은 피합니다. |
| 한글 문서/보고 규칙 | 사용했습니다. | 체크리스트, 기획/아트 기준, 완료 증거, 회고 판단을 사용자가 바로 검토하기 쉽게 만들었습니다. | 낮습니다. 문서 작성 비용은 있었지만 판단 근거가 명확해졌습니다. | 유지합니다. | 용어만 계속 일관되게 관리합니다. |

## Skill / Hooks 판단

| 항목 | 판단 |
| --- | --- |
| Skill | 지금까지 필수는 아니었습니다. 다만 Console error, Scene dirty 상태, 핵심 GameObject 존재 여부, playable loop smoke 결과처럼 반복된 Unity 검증이 있었으므로 M7에서 작은 Unity 검증 Skill 1개를 실험할 가치가 있습니다. |
| Hooks | 현재는 보류합니다. C# 변경 뒤 자동 format/lint 보고가 유용할 수는 있지만, M0~M5에서는 반복 불편이 크지 않았고 hook 자체가 하네스 복잡도를 키울 가능성이 있습니다. |

## 한계와 보완

- Unity MCP는 Scene과 컴포넌트 상태 확인에는 강하지만, 실제 Game view가 사용자가 읽기 좋은 화면인지까지 보장하지는 못했습니다.
- 자동 smoke runner는 로직 검증에는 유효하지만, 실제 물리 키보드 입력과 조작감을 완전히 대체하지 못합니다.
- 다음 프로젝트에서는 milestone 완료 전 screenshot 또는 Game view 캡처를 별도 판독 기준으로 두는 편이 좋습니다.

## 다음 조치

1. M7에서 작은 Unity 검증 Skill 1개만 실험합니다.
2. Hooks는 C# 변경 반복이 더 커질 때 다시 검토합니다.
3. v2 문서를 작성한다면 M6의 판단을 기준으로, 경량 하네스 기본값은 유지하고 화면 판독 검증만 보강합니다.

## 검증 기록

- 확인한 체크리스트: `docs/milestones/M0-checklist.md`, `docs/milestones/M1-checklist.md`, `docs/milestones/M1.5-checklist.md`, `docs/milestones/M2-checklist.md`, `docs/milestones/M3-checklist.md`, `docs/milestones/M4-checklist.md`, `docs/milestones/M5-checklist.md`, `docs/milestones/M6-checklist.md`
- 확인한 보고서: `docs/reports/execplan-trigger-test-summary-2026-05-20.md`, `docs/reports/project-goal-v2-document-plan-2026-05-20.md`
- 실행한 명령: `rg --files docs`, `Get-Content`, `git status --short`
- Unity MCP 조회: `get_scene_info`, `get_console_logs(logType=error, includeStackTrace=false)`, `get_gameobject("TinyGardenRoot")`
- 확인 날짜: 2026-05-21 KST
