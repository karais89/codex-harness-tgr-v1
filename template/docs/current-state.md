# 현재 상태

## 프로젝트

{{PROJECT_NAME}}

저장소: `{{REPOSITORY_NAME}}`

## 현재 단계

{{CURRENT_STAGE}}

이 저장소는 Unity 프로젝트와 최소 Codex 하네스를 준비하는 단계입니다. 아직 player-facing gameplay design은 승인되지 않았고, gameplay 구현도 시작하지 않았습니다.

## 활성 계획

`exec-plans/000-bootstrap.md`

이 계획은 Unity 프로젝트 존재, GitHub remote, 최소 문서 하네스, design placeholder, worktree 상태, bootstrap 범위 제한을 검증합니다.

## 완료됨

- Unity 프로젝트가 존재합니다.
- Git 저장소가 존재합니다.
- GitHub remote는 `{{GITHUB_REMOTE}}`로 설정할 예정이거나 설정되어 있습니다.
- Unity 버전은 `{{UNITY_VERSION}}`로 기록할 예정입니다.
- 최소 Codex 하네스 문서를 초기화할 예정입니다.

## 다음 단계

1. `exec-plans/000-bootstrap.md`에 따라 bootstrap 단계 검증을 완료합니다.
2. `docs/current-state.md`와 `docs/decisions.md`를 실제 프로젝트 상태로 갱신합니다.
3. bootstrap 검증이 끝난 뒤 `docs/design/core-beliefs.md` 작성을 위한 사용자 인터뷰를 시작합니다.

## 아직 하지 않음

- `docs/design/core-beliefs.md` 승인
- player-facing gameplay design 문서 작성 또는 승인
- gameplay ExecPlan 작성
- Unity 씬 변경
- C# gameplay 코드 추가
- Unity MCP
- custom skill
- hook
- subagent
- external package 추가

## 알려진 제한 사항

- `docs/design/core-beliefs.md`가 `상태: 작성 전`이면 gameplay ExecPlan이나 gameplay 구현 기준으로 사용할 수 없습니다.
- 첫 gameplay 작업은 bootstrap 검증, 승인된 core beliefs, 해당 gameplay에 필요한 승인 design 문서가 생긴 뒤에만 시작할 수 있습니다.
