# 현재 상태

## 프로젝트

Tiny Garden Restore

저장소: `codex-harness-tgr-v1`

## 현재 단계

Creative 컨셉 단계 재정의 완료

이 저장소는 Unity 프로젝트와 최소 Codex 하네스를 준비했고, creative/art 워크플로우 문서 구조와 엄격 모드 라우팅 규칙을 적용했습니다. 현재는 creative 단계를 가벼운 컨셉 탐색 중심으로 재정의했고, 세부 gameplay design 사양으로 너무 빨리 수렴한 `작은 분수 복구 노드 퍼즐` creative 산출물은 폐기된 방향의 기록으로 정리했습니다. 아직 player-facing gameplay design은 승인되지 않았고, gameplay 구현도 시작하지 않았습니다.

## 활성 계획

`exec-plans/002-creative-concept-reset.md`

이 계획은 creative/art/design 분리 원칙은 유지하되, creative 브레인스토밍이 세부 design 사양으로 너무 빨리 굳지 않도록 creative 단계를 가벼운 컨셉 탐색 중심으로 재정의한 계획입니다. 현재 상태는 `완료`입니다.

## 완료됨

- Unity 프로젝트가 존재합니다.
- Git 저장소가 존재합니다.
- GitHub remote는 `https://github.com/karais89/codex-harness-tgr-v1.git`로 설정되어 있습니다.
- Unity 버전은 `6000.4.6f1`입니다.
- 최소 Codex 하네스 문서를 초기화했습니다.
- 사용자가 Unity Editor에서 프로젝트가 열리는 것을 수동으로 확인했습니다.
- `exec-plans/000-bootstrap.md`의 bootstrap 검증을 완료 상태로 갱신했습니다.
- `exec-plans/001-creative-art-workflow.md`의 구현 승인을 받았습니다.
- `docs/creative/`와 `docs/art/`의 기본 문서 구조를 추가했습니다.
- creative/art/design/ExecPlan 영향이 애매하면 질문하는 엄격 모드 라우팅 규칙을 추가했습니다.
- `exec-plans/001-creative-art-workflow.md`의 검증과 회고를 완료했습니다.
- `docs/creative/01-brainstorming.md`에 작은 분수 복구 노드 퍼즐 아이디어를 1차 기록했습니다.
- `docs/creative/02-concept-candidates.md`에 `C-01. 작은 분수 복구 노드 퍼즐` 후보를 정리했습니다.
- `docs/creative/04-brainstorming-qna-2026-05-19.md`에 브레인스토밍 질문과 답변 원문 기록을 별도 저장했습니다.
- 현재 creative 산출물이 가벼운 컨셉 탐색보다 세부 gameplay design 사양에 가깝다는 문제를 확인했습니다.
- `exec-plans/002-creative-concept-reset.md`를 작성하고 구현 승인 대기 상태로 두었습니다.
- `exec-plans/002-creative-concept-reset.md`의 구현 승인을 받았습니다.
- `docs/creative/README.md`를 가벼운 컨셉 탐색 중심으로 갱신했습니다.
- `AGENTS.md`에 creative 단계에서 세부 gameplay design 사양을 확정하지 않는다는 경계를 추가했습니다.
- `docs/creative/01-brainstorming.md`, `docs/creative/02-concept-candidates.md`, `docs/creative/04-brainstorming-qna-2026-05-19.md`에서 `작은 분수 복구 노드 퍼즐` 방향을 폐기된 기록으로 표시했습니다.
- `docs/decisions.md`에 creative 단계와 design 단계의 경계, `작은 분수 복구 노드 퍼즐` 폐기 결정을 기록했습니다.

## 다음 단계

1. 다음 creative 브레인스토밍은 `docs/creative/README.md`의 가벼운 컨셉 탐색 기준에 맞춰 다시 시작합니다.
2. 현재 채택한 concept 후보는 없으므로, 새 후보를 만들기 전에는 정서, 감각, 소재, 재미 후보, 피하고 싶은 방향을 먼저 탐색합니다.
3. 아트 방향 논의가 시작되면 `docs/art/README.md`를 먼저 읽습니다.
4. gameplay 구현 기준으로 승격하려면 `docs/design/core-beliefs.md` 인터뷰와 승인 절차를 먼저 진행합니다.

## 아직 하지 않음

- `docs/design/core-beliefs.md` 승인
- player-facing gameplay design 문서 작성 또는 승인
- gameplay ExecPlan 작성
- Unity 씬 변경
- C# gameplay 코드 추가
- 실제 이미지 생성
- 생성 이미지를 Unity 에셋으로 사용하는 작업
- Unity MCP
- custom skill
- hook
- subagent
- external package 추가

## 알려진 제한 사항

- `docs/design/core-beliefs.md`가 `상태: 작성 전`이면 gameplay ExecPlan이나 gameplay 구현 기준으로 사용할 수 없습니다.
- 첫 gameplay 작업은 bootstrap 검증, 승인된 core beliefs, 해당 gameplay에 필요한 승인 design 문서가 생긴 뒤에만 시작할 수 있습니다.
- Creative 산출물은 행동 횟수, 상태명, UI 조작, 성공/실패 조건 같은 세부 gameplay design 사양을 확정하지 않습니다.
