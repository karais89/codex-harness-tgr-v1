# 현재 상태

## 프로젝트

Tiny Garden Restore

저장소: `codex-harness-tgr-v1`

## 현재 단계

Creative 컨셉 단계 재정의 계획 검토

이 저장소는 Unity 프로젝트와 최소 Codex 하네스를 준비했고, creative/art 워크플로우 문서 구조와 엄격 모드 라우팅 규칙을 적용했습니다. 다만 현재 creative 브레인스토밍 산출물이 사용자가 원한 가벼운 컨셉 탐색보다 세부 gameplay design 사양에 가깝게 수렴한 문제가 확인되었습니다. 현재는 creative 단계를 다시 정의하고 기존 creative 산출물 상태를 정리하기 위한 ExecPlan을 검토 중입니다. 아직 player-facing gameplay design은 승인되지 않았고, gameplay 구현도 시작하지 않았습니다.

## 활성 계획

`exec-plans/002-creative-concept-reset.md`

이 계획은 creative/art/design 분리 원칙은 유지하되, creative 브레인스토밍이 세부 design 사양으로 너무 빨리 굳지 않도록 creative 단계를 가벼운 컨셉 탐색 중심으로 재정의하는 계획입니다. 현재 상태는 `구현 승인 대기`입니다.

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

## 다음 단계

1. `exec-plans/002-creative-concept-reset.md`를 검토합니다.
2. 구현 승인 여부를 확인합니다.
3. 승인되면 `docs/creative/README.md`를 가벼운 컨셉 탐색 중심으로 갱신합니다.
4. 승인되면 현재 `작은 분수 복구 노드 퍼즐` creative 산출물을 폐기 또는 보류 상태로 정리합니다.
5. 아트 방향 논의가 시작되면 `docs/art/README.md`를 먼저 읽습니다.
6. gameplay 구현 기준으로 승격하려면 `docs/design/core-beliefs.md` 인터뷰와 승인 절차를 먼저 진행합니다.

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
