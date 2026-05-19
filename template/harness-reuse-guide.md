# Template Harness Reuse Guide

## 목적

이 문서는 `template/` 폴더를 실제 Unity 프로젝트 루트에 적용할 때 필요한 파일, 치환 값, 검증 기준을 정의한다.

이 파일은 `template/` 폴더 안의 문서를 사용하는 기준 문서다. 새 프로젝트를 설정할 때는 원본 v0 문서를 다시 해석해서 새로 쓰지 않고, 이 `template/` 폴더를 복사한 뒤 placeholder를 프로젝트 값으로 치환한다.

## 적용 대상

이 템플릿은 Unity 프로젝트가 이미 존재하는 저장소에 최소 Codex 하네스를 추가할 때 사용한다.

Unity 프로젝트 자체를 복제하는 템플릿이 아니므로 다음 폴더는 적용 대상이 아니다.

- `Assets/`
- `Packages/`
- `ProjectSettings/`
- `Library/`
- `Temp/`
- `Logs/`
- `UserSettings/`

## 필수 파일 트리

프로젝트 루트에 적용되는 최종 하네스 파일은 다음과 같아야 한다.

```text
project-root/
├─ .gitignore
├─ README.md
├─ AGENTS.md
├─ PLANS.md
├─ docs/
│  ├─ current-state.md
│  ├─ decisions.md
│  └─ design/
│     ├─ README.md
│     └─ core-beliefs.md
└─ exec-plans/
   └─ 000-bootstrap.md
```

## template 파일 역할

- `.gitignore`: Unity 생성물, `.worktree/`, `.utmp/`, 로그, TestRunner 생성물, OS 파일 제외 규칙이다.
- `README.md`: 프로젝트 목적, 현재 단계, 실행 방법, 문서 구조, 초기 성공 기준, 제외 범위를 설명한다.
- `AGENTS.md`: Codex 작업 규칙, 읽기 순서, Design Baseline Check, ExecPlan 흐름을 정의한다.
- `PLANS.md`: ExecPlan 작성, 승인, 검증, 완료 기준을 정의한다.
- `docs/current-state.md`: 현재 단계, 활성 계획, 완료됨, 다음 단계, 아직 하지 않음, 제한 사항을 기록한다.
- `docs/decisions.md`: 단일 계획을 넘어 유지할 하네스와 프로젝트 결정을 기록한다.
- `docs/design/README.md`: design 문서 상태, Core Beliefs 작성 절차, 조건부 design 문서 규약을 정의한다.
- `docs/design/core-beliefs.md`: 새 프로젝트에서는 `상태: 작성 전` placeholder로 시작한다.
- `exec-plans/000-bootstrap.md`: 첫 bootstrap 단계 검증 계획이다.

## 치환 값

적용 전에 다음 placeholder를 실제 프로젝트 값으로 치환한다.

| Placeholder | 의미 |
| --- | --- |
| `{{PROJECT_NAME}}` | 사람이 읽는 프로젝트 이름 |
| `{{REPOSITORY_NAME}}` | GitHub 저장소 이름과 Unity 프로젝트 폴더 이름 |
| `{{PROJECT_ONE_LINE_GOAL}}` | README 첫 문단의 한 문장 목표 |
| `{{PROJECT_GOAL_SUMMARY}}` | AGENTS.md에 넣을 짧은 목표 요약 |
| `{{CURRENT_STAGE}}` | 현재 단계 또는 bootstrap 단계 |
| `{{UNITY_VERSION}}` | `ProjectSettings/ProjectVersion.txt` 기준 Unity 버전 |
| `{{GITHUB_REMOTE}}` | GitHub origin remote URL |
| `{{DECISION_DATE}}` | 장기 결정을 기록한 날짜 |

## 적용 절차

1. 프로젝트 루트의 현재 worktree 상태를 확인한다.
2. `template/`의 필수 파일이 모두 있는지 확인한다.
3. 프로젝트 루트에 `docs/design/`과 `exec-plans/`가 없으면 만든다.
4. `template/` 파일을 프로젝트 루트의 동일 상대 경로로 복사한다.
5. placeholder를 실제 프로젝트 값으로 치환한다.
6. 기존 `.gitignore`가 있으면 OS 파일 ignore나 프로젝트 고유 ignore가 사라지지 않는지 확인한다.
7. `docs/design/core-beliefs.md`가 `상태: 작성 전`으로 남아 있는지 확인한다.
8. `exec-plans/000-bootstrap.md`가 bootstrap 검증만 다루고 gameplay 구현을 포함하지 않는지 확인한다.
9. `git status --short`로 적용된 파일 범위를 확인한다.

## TGR 적용 값

`codex-harness-tgr-v1`에는 다음 값을 사용한다.

| Placeholder | Value |
| --- | --- |
| `{{PROJECT_NAME}}` | Tiny Garden Restore |
| `{{REPOSITORY_NAME}}` | codex-harness-tgr-v1 |
| `{{PROJECT_ONE_LINE_GOAL}}` | Codex Harness v1을 검증하기 위한 작은 Unity 2D 복구 게임 실험 |
| `{{PROJECT_GOAL_SUMMARY}}` | 이전 v0 프로젝트에서 검증한 최소 Codex 하네스를 두 번째 Unity 프로젝트에 이식하고, Unity 프로젝트를 반복 가능하게 설계, 데이터화, 구현, 검증하는 v1 하네스를 검증하는 것 |
| `{{CURRENT_STAGE}}` | Bootstrap & Harness Reuse Check |
| `{{UNITY_VERSION}}` | 6000.4.6f1 |
| `{{GITHUB_REMOTE}}` | https://github.com/karais89/codex-harness-tgr-v1.git |
| `{{DECISION_DATE}}` | 2026-05-19 |

## 적용 후 검증

적용 후 다음을 확인한다.

```bash
find . -maxdepth 3 -type f \
  \( -path './README.md' \
  -o -path './AGENTS.md' \
  -o -path './PLANS.md' \
  -o -path './docs/current-state.md' \
  -o -path './docs/decisions.md' \
  -o -path './docs/design/README.md' \
  -o -path './docs/design/core-beliefs.md' \
  -o -path './exec-plans/000-bootstrap.md' \) -print | sort

rg -n '\{\{[A-Z0-9_]+\}\}' README.md AGENTS.md PLANS.md docs/current-state.md docs/decisions.md docs/design exec-plans
rg -n 'Delivery Bot Zero|DeliveryBotZero|codex-harness-dbz' README.md AGENTS.md PLANS.md docs/current-state.md docs/decisions.md docs/design exec-plans
git status --short
```

검증 통과 기준:

- 필수 파일 8개와 `.gitignore`가 프로젝트 루트에 존재한다.
- template placeholder가 루트 하네스 문서에 남아 있지 않다.
- 원본 프로젝트 전용 문구가 루트 하네스 문서에 남아 있지 않다.
- `docs/design/core-beliefs.md`는 `상태: 작성 전`이다.
- `exec-plans/000-bootstrap.md`는 gameplay 구현을 포함하지 않는다.
- `Assets/`, `Packages/`, `ProjectSettings/`는 template 적용으로 변경되지 않는다.

## template 유지 기준

이 파일과 `template/`의 실제 문서가 어긋나면 `template/` 문서와 이 가이드를 함께 갱신한다.

새 프로젝트 적용 결과 반복적으로 같은 문서와 치환값이 필요하다는 점이 확인되면, 이 `template/` 폴더를 다음 프로젝트의 source of truth로 사용할 수 있다.
