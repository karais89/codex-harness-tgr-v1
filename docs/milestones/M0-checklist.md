# M0 체크리스트 - 기준 문서 정리

## 목적

이 문서는 `docs/project-goal.md`의 `M0. 기준 문서 정리` 완료 기준을 작은 확인 항목으로 나누어, M0 완료 여부를 체크리스트만으로 판정하기 위해 작성합니다.

M0의 목표는 Codex가 읽을 최소 기준 파일을 준비하는 것입니다.

## 완료 판정 규칙

- 필수 체크리스트의 모든 항목이 완료되어야 M0를 완료로 판정합니다.
- 각 항목은 확인 방법과 완료 증거를 함께 남깁니다.
- 검증 증거가 없거나 미확인 항목이 남아 있으면 M0를 완료로 판정하지 않습니다.
- `docs/project-goal.md`의 M0 완료 기준과 충돌하는 별도 기준을 추가하지 않습니다.

## 필수 체크리스트

- [x] M0-01: `README.md`가 존재합니다.
  - 확인 방법: 저장소 파일 목록에서 `README.md`를 확인합니다.
  - 완료 증거: `rg --files` 결과에 `README.md`가 포함되어 있습니다.
- [x] M0-02: `AGENTS.md`가 존재합니다.
  - 확인 방법: 저장소 파일 목록에서 `AGENTS.md`를 확인합니다.
  - 완료 증거: `rg --files` 결과에 `AGENTS.md`가 포함되어 있습니다.
- [x] M0-03: `docs/project-goal.md`가 존재합니다.
  - 확인 방법: 저장소 파일 목록에서 `docs/project-goal.md`를 확인합니다.
  - 완료 증거: `rg --files` 결과에 `docs/project-goal.md`가 포함되어 있습니다.
- [x] M0-04: `.agent/PLANS.md`가 존재합니다.
  - 확인 방법: `.agent/PLANS.md`를 직접 읽어 ExecPlan 원문 참조 파일인지 확인합니다.
  - 완료 증거: `.agent/PLANS.md`에 `Codex Execution Plans (ExecPlans)` 원문이 있습니다.
- [x] M0-05: 프로젝트 목적이 경량 하네스로 Tiny Garden Restore의 작은 Unity playable loop를 만드는 것이라고 설명되어 있습니다.
  - 확인 방법: `README.md`와 `docs/project-goal.md`의 프로젝트 목적 설명을 확인합니다.
  - 완료 증거: 두 문서 모두 Tiny Garden Restore의 작은 Unity 2D playable loop와 Codex 경량 하네스 검증 목적을 설명합니다.
- [x] M0-06: 불필요한 workflow 문서가 기본값으로 추가되지 않았습니다.
  - 확인 방법: 저장소 파일 목록과 기준 문서를 확인해 불필요한 workflow 문서가 있는지 확인합니다.
  - 완료 증거: Superpowers, gstack, grill-me, custom skill, hooks, subagent, memory 문서가 기본값으로 추가되어 있지 않습니다. 이번 요청으로 추가된 `docs/milestones` 문서는 M0 판정을 위한 산출물입니다.

## 검증 증거

- 확인한 파일: `README.md`, `AGENTS.md`, `docs/project-goal.md`, `.agent/PLANS.md`
- 실행한 명령: `rg --files`, `Get-Content -Raw README.md`, `Get-Content -Raw AGENTS.md`, `Get-Content -Raw docs/project-goal.md`, `Get-Content -Raw .agent/PLANS.md`
- 확인 결과: M0 완료 기준에 필요한 기준 파일이 모두 존재하고, 프로젝트 목적이 Tiny Garden Restore의 작은 playable loop와 경량 Codex 하네스 검증으로 설명되어 있습니다.
- 확인 날짜: 2026-05-20

## 미확인/예외

- `docs/project-goal.html`이 존재하지만, workflow 문서가 아니라 `docs/project-goal.md`의 HTML 산출물로 보입니다. 따라서 M0-06의 불필요한 workflow 문서에는 포함하지 않습니다.

## 최종 판정

- 판정: 완료
- 판정 근거: M0 필수 체크리스트 6개 항목이 모두 완료이며, 확인 방법과 완료 증거가 남아 있습니다.
- 다음 조치: 이후 마일스톤을 판정할 때 `docs/milestones/milestone-checklist-template.md`를 복제해 해당 마일스톤의 완료 기준을 작은 체크 항목으로 나눕니다.
