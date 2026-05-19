# 현재 상태

## 프로젝트

Tiny Garden Restore

저장소: `codex-harness-tgr-v1`

## 현재 단계

Grill-Me Discovery Protocol Setup

이 저장소는 Unity 프로젝트와 최소 Codex 하네스를 준비했고, creative/art 워크플로우 문서 구조 위에 `grill-me` 기반 공통 discovery protocol을 연결하는 단계입니다. 아직 player-facing gameplay design은 승인되지 않았고, gameplay 구현도 시작하지 않았습니다.

## 활성 계획

`exec-plans/002-grill-me-discovery-protocol.md`

이 계획은 creative, art, design, ExecPlan 작업이 공유된 이해에 도달할 때까지 `grill-me` 방식 인터뷰를 거치도록 공통 workflow protocol을 도입하는 계획입니다. 현재 상태는 `완료`입니다.

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
- `exec-plans/002-grill-me-discovery-protocol.md`의 구현 승인을 받았습니다.
- `docs/workflows/grill-me.md`를 공통 discovery protocol 문서로 추가했습니다.
- `AGENTS.md`, `PLANS.md`, `docs/creative/README.md`, `docs/art/README.md`, `docs/design/README.md`가 공통 protocol을 참조하도록 연결했습니다.
- `exec-plans/002-grill-me-discovery-protocol.md`의 검증과 회고를 완료했습니다.

## 다음 단계

1. 다음 creative 작업부터 `docs/workflows/grill-me.md`와 `docs/creative/README.md`를 함께 읽고 브레인스토밍을 시작합니다.
2. Codex는 아이디어 목록을 바로 쓰지 않고, 공유된 이해가 닫힐 때까지 한 번에 하나씩 질문합니다.
3. 아트 방향 논의가 시작되면 `docs/workflows/grill-me.md`와 `docs/art/README.md`를 함께 읽습니다.

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
