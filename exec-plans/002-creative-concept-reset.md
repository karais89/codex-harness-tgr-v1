# Creative Concept Reset

## 목적

이 ExecPlan은 현재 `docs/creative` 산출물이 너무 빨리 gameplay 세부 사양으로 굳어진 문제를 고치고, creative 단계를 가벼운 컨셉 탐색 단계로 다시 정의한다.

완료 후에는 Codex가 creative 브레인스토밍에서 수치, UI, 상태명, 성공 조건, 조작 방식 같은 design 세부를 확정하지 않고, 게임의 정서, 재미의 방향, 소재, 피하고 싶은 느낌, 후보적 상상만 다룰 수 있어야 한다.

이 계획은 gameplay design 계획이 아니다. `docs/design` 승인 상태를 바꾸지 않고, Unity 씬, C# 코드, 실제 이미지 생성, Unity 에셋 사용을 하지 않는다.

## 진행 상황

- 상태: 구현 승인 대기
- [x] 현재 creative 산출물이 원하는 컨셉 브레인스토밍보다 세부 design 사양에 가깝다는 문제를 사용자와 논의했다.
- [x] 공유된 이해 검증을 완료했다.
- [x] ExecPlan 생성 승인을 받았다.
- [ ] 구현 승인을 받는다.
- [ ] `docs/creative/README.md`를 가벼운 컨셉 탐색 중심으로 갱신한다.
- [ ] 현재 `작은 분수 복구 노드 퍼즐` creative 산출물을 폐기 또는 보류 상태로 정리한다.
- [ ] `docs/decisions.md`에 creative와 design 경계에 대한 장기 결정을 기록한다.
- [ ] `docs/current-state.md`를 최종 상태에 맞게 갱신한다.
- [ ] 검증을 완료한다.
- [ ] 회고를 작성한다.

## 맥락

Repository: `codex-harness-tgr-v1`

Project name: `Tiny Garden Restore`

현재 저장소는 `36b26444658c991053d5ad24c3ffda61b53652fe` 커밋에서 creative/art/design/ExecPlan/implementation을 분리하는 문서 구조를 도입했다. 그 뒤 `docs/creative/01-brainstorming.md`, `docs/creative/02-concept-candidates.md`, `docs/creative/04-brainstorming-qna-2026-05-19.md`에 첫 playable 후보로 `작은 분수 복구 노드 퍼즐`을 기록했다.

사용자는 원래 creative 브레인스토밍이 다음을 다루는 가벼운 컨셉 단계이기를 원했다.

- 어떤 느낌의 게임인지
- 어떤 재미를 상상하는지
- 어떤 생각으로 기획하는지
- 어떤 감정이나 인상을 남기고 싶은지
- 어떤 방향은 피하고 싶은지

하지만 현재 creative 산출물은 다음처럼 player-facing gameplay design에 가까운 세부를 포함한다.

- 행동 횟수 4회
- 노드 수 6개
- 성공 경로
- `잠김`, `복구 가능`, `복구됨` 상태명
- `복구하기` 버튼
- 성공/실패 문구
- Reset 버튼
- 힌트 유무

이런 항목은 creative가 아니라 `docs/design`에서 사용자 인터뷰와 공유된 이해 검증을 거쳐 다뤄야 할 구현 기준 후보에 가깝다. 따라서 이번 계획은 creative/art/design 분리 원칙은 유지하되, creative 단계의 정의와 문서 규칙을 다시 잡는다.

`docs/design/core-beliefs.md`는 여전히 `상태: 작성 전`이며, 이 계획은 gameplay design 또는 gameplay 구현을 시작하지 않는다.

## 계획

1. `docs/creative/README.md`를 갱신한다.
   - creative의 역할을 "가벼운 컨셉 탐색"으로 명확히 쓴다.
   - creative가 다루는 항목을 정리한다: 정서, 감각, 소재, 재미 후보, 플레이어에게 남기고 싶은 인상, 피하고 싶은 방향, 아직 열어 둘 가능성.
   - creative에서 확정하지 않을 항목을 명시한다: 수치, 성공/실패 조건, UI 조작, 상태명, 노드 수, 맵 구조, 밸런스, 구현 방식.
   - creative 결과가 design으로 넘어가려면 별도 design 절차가 필요하다고 다시 강조한다.

2. 현재 creative 산출물을 정리한다.
   - `docs/creative/01-brainstorming.md`의 `작은 분수 복구 노드 퍼즐` 기록을 확정 후보처럼 보이지 않게 정리한다.
   - 사용자가 원한 컨셉 탐색과 맞지 않았다는 이유를 기록한다.
   - 추천 표현은 `폐기`다. 이유는 이 산출물이 이후 세션에서 다시 구현 사양처럼 오해될 위험이 크기 때문이다.
   - 필요하면 `docs/creative/02-concept-candidates.md`의 `C-01`도 같은 상태로 맞춘다.
   - `docs/creative/04-brainstorming-qna-2026-05-19.md`는 원문 기록으로 보존하되, "폐기된 방향의 근거 기록"임을 앞부분에 표시한다.

3. `docs/decisions.md`를 갱신한다.
   - creative는 design spec 작성 전의 컨셉 탐색 단계로 유지한다는 장기 결정을 기록한다.
   - 행동 횟수, 상태명, 조작 방식, 성공/실패 조건, UI 피드백, 맵 구조는 creative에서 확정하지 않고 design 절차로 넘긴다는 결정을 기록한다.

4. `docs/current-state.md`를 갱신한다.
   - 현재 단계가 creative 후보 정리가 아니라 creative workflow 보정 또는 creative reset 진행 중임을 반영한다.
   - 활성 계획을 `exec-plans/002-creative-concept-reset.md`로 갱신한다.
   - 다음 단계는 구현 승인 후 creative 문서 규칙과 기존 산출물 상태를 정리하는 것이라고 쓴다.
   - gameplay design과 구현은 아직 시작하지 않았다고 유지한다.

5. 검증 결과와 회고를 이 ExecPlan에 기록한다.

## 검증

터미널에서 다음을 확인한다.

```bash
test -f docs/creative/README.md
test -f docs/creative/01-brainstorming.md
test -f docs/creative/02-concept-candidates.md
test -f docs/creative/04-brainstorming-qna-2026-05-19.md
test -f docs/current-state.md
test -f docs/decisions.md
rg -n "가벼운 컨셉|확정하지|design|폐기|작은 분수 복구 노드 퍼즐" docs/creative docs/current-state.md docs/decisions.md exec-plans/002-creative-concept-reset.md
git diff --check
git status --short
```

수동으로 다음을 확인한다.

1. `docs/creative/README.md`가 creative를 세부 gameplay 사양 작성 단계로 설명하지 않는다.
2. 현재 `작은 분수 복구 노드 퍼즐` 산출물이 채택 후보처럼 남아 있지 않다.
3. 행동 횟수, 노드 수, 상태명, 조작 방식, 성공/실패 조건은 creative에서 확정할 수 없는 항목으로 분류되어 있다.
4. `docs/design/core-beliefs.md` 상태는 바꾸지 않았다.
5. Unity 씬, C# 코드, 실제 이미지 파일은 변경하지 않았다.

이 계획은 다음이 모두 참일 때 완료한다.

- creative와 design의 경계가 `docs/creative/README.md`와 `docs/decisions.md`에 기록되어 있다.
- 현재 creative 산출물의 상태가 사용자 의도와 맞지 않는 방향으로 정리되어 있다.
- `docs/current-state.md`가 활성 계획과 다음 단계를 정확히 설명한다.
- 검증 절차와 결과가 이 ExecPlan에 기록되어 있다.
- commit 후 `git status`가 clean이다.

## 결정 기록

- 결정:
  creative/art/design 분리 원칙은 유지하고, 현재 creative 산출물과 creative 단계 규칙만 보정한다.
- 근거:
  문제는 폴더 분리 자체가 아니라 creative 브레인스토밍이 너무 빨리 design spec으로 수렴한 데 있다.
- 날짜:
  2026-05-19

- 결정:
  현재 `작은 분수 복구 노드 퍼즐` 산출물은 폐기 상태로 정리하는 것을 기본안으로 삼는다.
- 근거:
  보류로 남기면 이후 세션에서 다시 유효한 concept 후보처럼 사용될 위험이 있다. 사용자가 원한 것은 더 가벼운 컨셉 탐색이므로, 이 산출물은 반례로 남기는 편이 안전하다.
- 날짜:
  2026-05-19

## 예상 밖 발견

- 없음.

## 회고

아직 구현 승인 전이다.

