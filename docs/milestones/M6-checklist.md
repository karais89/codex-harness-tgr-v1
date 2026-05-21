# M6 체크리스트 - 경량 하네스 평가

## 목적

이 문서는 `docs/project-goal.md`의 `M6. 경량 하네스 평가` 완료 기준을 작은 확인 항목으로 나누어, M6 완료 여부를 체크리스트만으로 판정하기 위해 작성합니다.

M6의 목표는 M0~M5까지의 작업 결과를 기준으로 경량 하네스가 충분했는지 평가하는 것입니다.

## 완료 판정 규칙

- M0~M5 작업 결과를 검토한 뒤에만 M6를 완료로 판정합니다.
- 필수 평가 항목 6개를 모두 평가해야 합니다.
- 각 평가 항목은 `실제로 사용했는가`, `언제 도움이 되었는가`, `오히려 복잡도를 늘렸는가`, `다음 프로젝트에서도 유지할 것인가`, `보강이 필요한가`를 기준으로 판단합니다.
- Skill / Hooks가 지금 필요한지도 명확히 판단해야 합니다.
- 평가 근거가 없거나 M0~M5 결과가 충분히 확인되지 않았으면 M6를 완료로 판정하지 않습니다.

## 필수 체크리스트

- [x] M6-01: M0~M5 작업 결과를 검토합니다.
  - 확인 방법: M0~M5 체크리스트와 실제 변경 결과를 확인합니다.
  - 완료 증거: 검토한 체크리스트 경로와 각 마일스톤 판정 요약을 기록합니다.
  - 확인 결과: `docs/reports/m6-lightweight-harness-evaluation-2026-05-21.md`에 M0, M1, M1.5, M2, M3, M4, M5의 완료 판정과 근거 요약을 기록했습니다.
- [x] M6-02: `AGENTS.md`를 평가합니다.
  - 확인 방법: 작업 중 `AGENTS.md`가 실제로 도움이 되었는지 평가 기준 5개로 판단합니다.
  - 완료 증거: 사용 여부, 도움 된 지점, 복잡도 영향, 유지 여부, 보강 필요 여부를 기록합니다.
  - 확인 결과: `AGENTS.md`는 범위 통제, 한국어 문서 규칙, ExecPlan 사용 조건, 검증 중심 진행에 도움이 되었고 다음 프로젝트에서도 유지하기로 판단했습니다.
- [x] M6-03: Codex 기본 Plan mode를 평가합니다.
  - 확인 방법: M0~M5 작업에서 Plan mode 흐름이 충분했는지 평가 기준 5개로 판단합니다.
  - 완료 증거: 사용 사례와 유지/보강 판단을 기록합니다.
  - 확인 결과: 기본 Plan mode와 짧은 프롬프트 흐름은 작은 Unity 작업을 단계별로 진행하고 검증 결과를 남기기에 충분했으며 유지하기로 판단했습니다.
- [x] M6-04: ExecPlan 원문 참조를 평가합니다.
  - 확인 방법: `.agent/PLANS.md`가 필요한 상황과 필요하지 않은 상황을 구분합니다.
  - 완료 증거: 실제 참조 여부와 다음 프로젝트 적용 판단을 기록합니다.
  - 확인 결과: ExecPlan은 복합 작업과 큰 리팩터링에서만 참조하고, 작은 마일스톤의 기본값으로는 쓰지 않기로 판단했습니다.
- [x] M6-05: Unity MCP를 평가합니다.
  - 확인 방법: `CoderGamester/mcp-unity`가 Unity 작업과 검증에서 도움이 되었는지 평가 기준 5개로 판단합니다.
  - 완료 증거: 연결, Console log 왕복, package / asset 조회, Scene 확인, Play Mode 검증에서의 효과와 MCP로 직접 확인하지 못한 범위를 기록합니다.
  - 확인 결과: Unity MCP는 Scene, GameObject, Console error, Play Mode smoke 증거 확인에 도움이 되었고 유지합니다. 다만 실제 화면 판독 품질은 screenshot 또는 사람 검수로 보강해야 합니다.
- [x] M6-06: 3줄 이하 작업 프롬프트를 평가합니다.
  - 확인 방법: M0~M5 작업 지시가 짧은 프롬프트로 충분했는지 확인합니다.
  - 완료 증거: 실제 프롬프트 예시와 충분/부족 판단을 기록합니다.
  - 확인 결과: 3줄 이하 프롬프트는 한 번에 하나의 목표, 단순 구현, 검증 결과 보고를 요구하는 데 충분했으며 유지하기로 판단했습니다.
- [x] M6-07: 한글 문서/보고 규칙을 평가합니다.
  - 확인 방법: 새 문서와 작업 보고가 한글 규칙에 맞았는지 확인합니다.
  - 완료 증거: 한글 문서/보고가 작업 흐름에 준 영향을 기록합니다.
  - 확인 결과: 한글 체크리스트와 보고 규칙은 완료 증거와 사용자 판단을 검토하기 쉽게 했으며 유지하기로 판단했습니다.
- [x] M6-08: Skill / Hooks 필요 여부를 판단합니다.
  - 확인 방법: M0~M5에서 반복 검증이나 기계적 검사가 충분히 반복되었는지 확인합니다.
  - 완료 증거: Skill / Hooks를 지금 실험할지, 다음 프로젝트로 미룰지 판단을 기록합니다.
  - 확인 결과: M7에서 작은 Unity 검증 Skill 1개를 비교 실험하고, Hooks는 현재 반복 불편이 크지 않아 보류하기로 판단했습니다.

## 검증 증거

- 확인한 파일: `docs/milestones/M0-checklist.md`, `docs/milestones/M1-checklist.md`, `docs/milestones/M1.5-checklist.md`, `docs/milestones/M2-checklist.md`, `docs/milestones/M3-checklist.md`, `docs/milestones/M4-checklist.md`, `docs/milestones/M5-checklist.md`, `docs/milestones/M6-checklist.md`, `docs/project-goal.md`, `docs/reports/execplan-trigger-test-summary-2026-05-20.md`, `docs/reports/project-goal-v2-document-plan-2026-05-20.md`, `docs/reports/m6-lightweight-harness-evaluation-2026-05-21.md`
- 실행한 명령: `rg --files docs`, `Get-Content`, `git status --short`
- Unity 또는 도구에서 확인한 결과: Unity MCP `get_scene_info` 기준 active scene은 `SampleScene`, path는 `Assets/Scenes/SampleScene.unity`, `Is Dirty=false`, `Is Loaded=true`, `Root Count=3`입니다. `get_console_logs(logType=error, includeStackTrace=false)` 결과는 `[]`로 Console error `0개`입니다. `get_gameobject("TinyGardenRoot")`로 `TinyGardenRoot`, `GardenArea`, `Player`, `RestoreTargets`, 세 복구 대상과 관련 컴포넌트가 존재함을 확인했습니다.
- 확인 날짜: 2026-05-21 KST

## 미확인/예외

- Unity MCP와 기존 smoke runner는 실제 화면 판독 품질을 완전히 보장하지 못합니다. M7 또는 v2에서는 screenshot 또는 Game view 사람 검수를 별도 보강 기준으로 검토합니다.

## 최종 판정

- 판정: 완료
- 판정 근거: M6 필수 체크리스트 `M6-01`부터 `M6-08`까지 모두 평가했고, `docs/reports/m6-lightweight-harness-evaluation-2026-05-21.md`에 M0~M5 검토, 하네스 항목별 평가, Unity 최신 조회 증거, Skill / Hooks 판단을 기록했습니다.
- 다음 조치: M7에서 작은 Unity 검증 Skill 1개를 실험하고, Hooks는 반복 불편이 커질 때 다시 검토합니다.
