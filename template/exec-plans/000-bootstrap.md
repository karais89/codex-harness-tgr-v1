# Bootstrap 단계 검증

## 목적

이 ExecPlan은 `{{REPOSITORY_NAME}}`의 bootstrap 단계 상태를 검증한다.

bootstrap 단계의 목적은 Unity 프로젝트가 존재하고, GitHub remote가 연결되어 있으며, 최소 Codex 하네스 문서가 존재하고 사용할 수 있는지 확인하는 것이다.

최소 하네스는 다음 파일로 구성된다.

- `README.md`
- `AGENTS.md`
- `PLANS.md`
- `docs/current-state.md`
- `docs/decisions.md`
- `docs/design/README.md`
- `docs/design/core-beliefs.md`
- `exec-plans/000-bootstrap.md`

이 계획은 gameplay 구현 계획이 아니다. 이 계획은 Unity 씬, C# gameplay 코드, gameplay 규칙, 새 패키지, MCP, custom skill, hook, subagent, architecture 확장, game specification을 추가하지 않는다.

## 진행 상황

- 상태: 구현 승인 대기
- [ ] Unity 프로젝트가 존재한다.
- [ ] Unity {{UNITY_VERSION}}에서 프로젝트가 열린다.
- [ ] Git 저장소가 존재한다.
- [ ] GitHub `origin` remote가 `{{GITHUB_REMOTE}}`를 가리킨다.
- [ ] `README.md`가 존재하고 저장소 목적, 현재 단계, 제외 범위를 설명한다.
- [ ] `AGENTS.md`가 존재하고 Codex 작업 규칙, 읽기 순서, 문서 갱신 규칙, 완료 기준을 설명한다.
- [ ] `PLANS.md`가 존재하고 ExecPlan 규칙, 필수 섹션, living document 기대치, 검증 규칙을 설명한다.
- [ ] `docs/current-state.md`가 존재하고 현재 단계, 활성 계획, 다음 단계를 설명한다.
- [ ] `docs/decisions.md`가 존재하고 오래 유지할 프로젝트 결정을 기록한다.
- [ ] `docs/design/README.md`가 존재한다.
- [ ] `docs/design/core-beliefs.md`가 `상태: 작성 전` placeholder로 존재한다.
- [ ] `exec-plans/000-bootstrap.md`가 표준 bootstrap 단계 검증 계획으로 존재한다.
- [ ] `git status`가 clean이거나 남은 변경이 명확히 기록되어 있다.
- [ ] bootstrap 중 gameplay 구현, Unity 씬 변경, 새 패키지, MCP, custom skill, hook, subagent를 추가하지 않았다.

## 맥락

Repository: `{{REPOSITORY_NAME}}`

Project name: `{{PROJECT_NAME}}`

Unity version: `{{UNITY_VERSION}}`

GitHub remote: `{{GITHUB_REMOTE}}`

Current stage: `{{CURRENT_STAGE}}`

이 저장소는 최소 Codex 하네스를 새 Unity 프로젝트에 적용하는 단계다. Bootstrap 검증이 끝나기 전에는 gameplay 구현을 시작하지 않는다.

## 계획

1. 필수 문서가 존재하는지 확인한다.
2. `docs/current-state.md`가 현재 단계와 활성 계획을 정확히 가리키는지 확인한다.
3. `docs/decisions.md`에 장기 하네스 결정이 기록되어 있는지 확인한다.
4. `docs/design/core-beliefs.md`가 `상태: 작성 전` placeholder인지 확인한다.
5. Unity 프로젝트가 열리는지 확인한다.
6. GitHub `origin` remote와 worktree 상태를 확인한다.
7. bootstrap 범위에서 벗어난 변경이 없는지 확인한다.
8. 검증 결과에 따라 `진행 상황`, `예상 밖 발견`, `회고`를 갱신한다.
9. 프로젝트 상태가 바뀌면 `docs/current-state.md`를 갱신한다.

## 검증

터미널에서 다음을 확인한다.

```bash
git remote -v
git status --short
test -f README.md
test -f AGENTS.md
test -f PLANS.md
test -f docs/current-state.md
test -f docs/decisions.md
test -f docs/design/README.md
test -f docs/design/core-beliefs.md
test -f exec-plans/000-bootstrap.md
```

Unity Editor에서 다음을 확인한다.

1. Unity {{UNITY_VERSION}}에서 저장소 루트 폴더를 연다.
2. `Assets/Scenes/SampleScene.unity`가 열린다.
3. Console에 project-load 또는 compile error가 없다.
4. 검증 중 gameplay 구현, 씬 수정, 패키지 추가를 하지 않는다.

bootstrap 단계 검증은 다음이 모두 참일 때 통과한다.

- Unity 프로젝트가 정상적으로 열린다.
- GitHub remote가 연결되어 있다.
- 최소 하네스 문서가 모두 존재한다.
- `docs/design/core-beliefs.md`는 `상태: 작성 전`으로 남아 있다.
- `git status`가 clean이거나 남은 변경이 명확히 기록되어 있다.
- bootstrap 중 gameplay 구현이나 하네스 확장을 하지 않았다.

## 결정 기록

- 결정:
  `exec-plans/000-bootstrap.md`를 표준 bootstrap 단계 검증 계획으로 사용한다.
- 근거:
  첫 gameplay 작업 전에 Unity 프로젝트, GitHub 연결, 최소 문서 하네스, design placeholder, worktree 상태를 확인할 안정적인 기준 계획이 필요하다.
- 날짜:
  {{DECISION_DATE}}

- 결정:
  이 계획은 bootstrap 검증만 다루고 gameplay 구현을 포함하지 않는다.
- 근거:
  첫 gameplay 작업은 bootstrap 검증과 승인된 design 기준이 생긴 뒤 별도 ExecPlan에서 다뤄야 한다.
- 날짜:
  {{DECISION_DATE}}

## 예상 밖 발견

- 아직 없음.

## 회고

아직 완료되지 않았다.

완료 시 다음을 요약한다.

- 완료한 것
- 완료하지 못한 것
- 배운 것
- 다음에 해야 할 것
- 다음 계획을 시작할 준비가 되었는지 여부
