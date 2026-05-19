# Creative Idea Board Workflow

## 목적

이 ExecPlan은 현재의 `creative`와 `art` 분류가 사용자가 원한 가벼운 브레인스토밍 흐름보다 무거운 승인 게이트처럼 느껴지는 문제를 고친다.

완료 후에는 `docs/creative`가 한 게임의 세부 기획서를 너무 빨리 만드는 공간이 아니라, 여러 게임 아이디어를 카드처럼 꺼내고 비교하고 고르는 아이디어 보드로 작동해야 한다. `docs/art`는 처음부터 에셋 승인 단계처럼 동작하지 않고, 선택했거나 흥미로운 후보의 시각 상상을 확장하는 단계로 작동해야 한다.

이 계획은 gameplay design 계획이 아니다. `docs/design` 승인 상태를 바꾸지 않고, Unity 씬, C# 코드, 실제 이미지 생성, Unity 에셋 사용을 하지 않는다.

## 진행 상황

- 상태: 구현 승인 대기
- [x] 현재 `creative`와 `art` 분류가 원래 의도보다 무겁다는 문제를 사용자와 논의했다.
- [x] 첫 단계는 "한 게임의 구체화"가 아니라 "여러 게임 아이디어를 자유롭게 뽑고 고르는 보드"라는 합의를 확인했다.
- [x] creative 단계에서 조작, 규칙, 성공/실패, 화면 아이디어도 러프한 후보 메모로 허용한다는 합의를 확인했다.
- [x] creative 산출물은 보드형 문서로 운영하고, 초기에는 점수표나 우선순위 평가표를 두지 않는다는 합의를 확인했다.
- [x] art는 creative 카드 안에 "아트/분위기 상상"을 가볍게 적고, 후보 선택 후 별도 art 문서로 확장한다는 합의를 확인했다.
- [x] 공유된 이해 검증을 완료했다.
- [x] ExecPlan 생성 승인을 받았다.
- [ ] 구현 승인을 받는다.
- [ ] `docs/creative/README.md`를 아이디어 보드 중심으로 갱신한다.
- [ ] `AGENTS.md`의 creative/art 라우팅 규칙을 새 흐름에 맞게 보정한다.
- [ ] `docs/art/README.md`를 선택 후보의 시각 확장 단계 중심으로 보정한다.
- [ ] 기존 `docs/creative` 문서를 보드형 흐름과 충돌하지 않게 정리한다.
- [ ] `docs/decisions.md`에 creative 아이디어 보드와 art 확장 흐름 결정을 기록한다.
- [ ] `docs/current-state.md`를 최종 상태에 맞게 갱신한다.
- [ ] 검증을 완료한다.
- [ ] 회고를 작성한다.

## 맥락

Repository: `codex-harness-tgr-v1`

Project name: `Tiny Garden Restore`

현재 저장소는 최소 Codex 하네스와 `creative`, `art`, `design`, `ExecPlan`, `implementation` 분리 규칙을 갖고 있다. `exec-plans/002-creative-concept-reset.md`를 통해 creative 단계가 세부 gameplay design 사양으로 너무 빨리 굳는 문제를 한 번 보정했다.

하지만 사용자는 이번 논의에서 현재 `creative`와 `art` 분류가 여전히 처음 목적과 상반된다고 느낀다고 설명했다. 처음 목적은 일반적인 `기획 -> 아트 -> 개발` 프로세스를 구축하는 것이었고, 특히 첫 기획 단계에서는 어떤 게임을 만들지에 대한 여러 아이디어를 자유롭게 브레인스토밍하고 선택하고 싶었다.

현재 문서들은 design과 implementation으로 잘못 넘어가지 않게 막는 문구가 강하다. 그 결과 `creative`가 아이디어 발산 작업장보다 승인 게이트처럼 읽히고, `art`도 시각 상상보다 에셋 사용 승인 경계가 먼저 보인다.

이번 계획의 핵심 합의는 다음과 같다.

- `creative`는 여러 게임 아이디어를 카드처럼 쌓는 아이디어 보드다.
- creative 카드에는 감정, 소재, 러프한 플레이 상상, 조작, 규칙, 성공/실패, 화면 아이디어를 적을 수 있다.
- creative 카드의 gameplay 요소는 모두 확정 사양이 아니라 후보 메모다.
- 초기 보드에는 점수표나 우선순위 평가표를 두지 않는다.
- `art`는 creative 카드 안에서 "아트/분위기 상상"을 가볍게 적고, 후보를 선택했거나 명시적으로 더 보고 싶을 때 별도 art 문서로 확장한다.
- `design`부터 구현 기준으로 승격한다.

`docs/design/core-beliefs.md`는 여전히 `상태: 작성 전`이며, 이 계획은 gameplay design 또는 gameplay 구현을 시작하지 않는다.

## 계획

1. `docs/creative/README.md`를 갱신한다.
   - creative의 역할을 "가벼운 컨셉 탐색"에서 한 단계 더 명확히 하여 "아이디어 보드"로 설명한다.
   - creative가 여러 게임 아이디어를 카드처럼 꺼내고 비교하고 선택하는 공간이라고 쓴다.
   - 조작, 규칙, 성공/실패, 화면 아이디어도 러프한 후보 메모로 허용한다고 명시한다.
   - 기존의 강한 금지 표현은 "확정 사양으로 취급하지 않는다"는 표현으로 바꾼다.
   - 초기에는 점수표나 우선순위 평가표를 두지 않고, 후보가 충분히 쌓인 뒤 필요하면 별도 비교 기준을 논의한다고 쓴다.
   - 카드 기본 항목을 제안한다: `ID`, `이름`, `한 줄 아이디어`, `플레이어가 느낄 감정`, `대략의 플레이 상상`, `아트/분위기 상상`, `좋은 점`, `걱정되는 점`, `상태`.

2. `AGENTS.md`를 갱신한다.
   - 엄격 모드 라우팅의 `creative` 설명을 아이디어 보드 중심으로 바꾼다.
   - creative 단계에서 gameplay 요소를 언급할 수 있지만 후보 메모로만 다룬다고 명시한다.
   - "Creative 단계에서는 행동 횟수, 자원량, 성공/실패 조건, UI 조작..."을 확정 금지로만 쓰는 현재 문구를 보정한다.
   - design으로 넘어가는 기준은 "후보 메모를 구현 기준으로 승격하려는 경우"로 설명한다.

3. `docs/art/README.md`를 갱신한다.
   - art의 역할을 "선택했거나 흥미로운 후보의 시각 상상을 확장하는 공간"으로 보정한다.
   - creative 카드 안에는 `아트/분위기 상상`만 가볍게 적고, 이미지 프롬프트나 생성 기록은 후보 선택 후 또는 사용자가 명시적으로 요청한 뒤 확장한다고 설명한다.
   - 생성 이미지와 Unity 에셋 사용 승인 경계는 유지하되, 문서의 첫 인상이 승인 게이트가 아니라 시각 탐색이 되도록 문구 순서를 조정한다.

4. 기존 `docs/creative` 문서를 정리한다.
   - `docs/creative/01-brainstorming.md`가 아이디어 보드로 읽히도록 현재 구조를 보정한다.
   - 폐기된 `작은 분수 복구 노드 퍼즐` 기록은 폐기 기록으로 남기되, 새 보드형 흐름과 충돌하지 않게 배치한다.
   - `docs/creative/02-concept-candidates.md`와 `docs/creative/03-concept-brief.md`가 있다면, 아이디어 보드에서 후보 선택 후 사용하는 보조 문서로 설명을 맞춘다.
   - 점수표나 우선순위 평가표는 추가하지 않는다.

5. `docs/decisions.md`를 갱신한다.
   - creative를 아이디어 보드로 운영한다는 장기 결정을 기록한다.
   - creative 카드의 gameplay 요소는 후보 메모이며, design 승격 전에는 구현 기준이 아니라는 결정을 기록한다.
   - art는 후보 선택 후 시각 확장 단계로 쓰며, creative 카드 안에서는 가벼운 분위기 상상만 둔다는 결정을 기록한다.

6. `docs/current-state.md`를 갱신한다.
   - 현재 단계와 활성 계획을 `exec-plans/003-creative-idea-board-workflow.md` 기준으로 갱신한다.
   - gameplay design과 Unity 구현은 아직 시작하지 않았다고 유지한다.
   - 다음 단계는 사용자의 구현 승인 후 creative/art 문서 규칙을 아이디어 보드 흐름으로 갱신하는 것이라고 쓴다.

7. 검증 결과와 회고를 이 ExecPlan에 기록한다.

## 검증

터미널에서 다음을 확인한다.

```bash
test -f docs/creative/README.md
test -f docs/art/README.md
test -f AGENTS.md
test -f docs/current-state.md
test -f docs/decisions.md
test -f exec-plans/003-creative-idea-board-workflow.md
rg -n "아이디어 보드|후보 메모|확정 사양|아트/분위기|점수표|우선순위|design" AGENTS.md docs/creative docs/art docs/current-state.md docs/decisions.md exec-plans/003-creative-idea-board-workflow.md
git diff --check
git status --short
```

수동으로 다음을 확인한다.

1. `docs/creative/README.md`가 creative를 승인 게이트가 아니라 여러 게임 아이디어를 뽑고 고르는 보드로 설명한다.
2. creative 단계에서 조작, 규칙, 성공/실패, 화면 아이디어가 러프한 후보 메모로 허용된다.
3. 해당 후보 메모가 design 승인 전 구현 기준이 아님이 명확하다.
4. 초기 creative 보드에 점수표나 우선순위 평가표가 추가되지 않았다.
5. `docs/art/README.md`가 후보 선택 후 시각 확장 흐름을 설명한다.
6. `docs/design/core-beliefs.md` 상태는 바꾸지 않았다.
7. Unity 씬, C# 코드, 실제 이미지 파일은 변경하지 않았다.

이 계획은 다음이 모두 참일 때 완료한다.

- creative 아이디어 보드 운영 방식이 `docs/creative/README.md`, `AGENTS.md`, `docs/decisions.md`에 기록되어 있다.
- art 확장 흐름이 `docs/art/README.md`와 `docs/decisions.md`에 기록되어 있다.
- 기존 creative 문서가 새 보드형 흐름과 충돌하지 않는다.
- `docs/current-state.md`가 활성 계획과 다음 단계를 정확히 설명한다.
- 검증 절차와 결과가 이 ExecPlan에 기록되어 있다.
- commit 후 `git status`가 clean이다.

현재 검증 결과:

- 작성 전.

## 결정 기록

- 결정:
  `creative`는 여러 게임 아이디어를 카드처럼 쌓고 고르는 아이디어 보드로 운영한다.
- 근거:
  사용자의 원래 목적은 한 게임을 바로 구체화하는 것이 아니라, 어떤 게임을 만들지에 대한 여러 방안을 자유롭게 브레인스토밍하고 선택하는 것이었다.
- 날짜:
  2026-05-19

- 결정:
  creative 단계에서는 조작, 규칙, 성공/실패, 화면 아이디어도 러프하게 적을 수 있다.
- 근거:
  이런 요소를 전부 금지하면 게임 아이디어 발산 자체가 막힌다. 문제는 gameplay 요소를 말하는 것이 아니라, 그것을 확정 사양이나 구현 기준으로 너무 빨리 취급하는 것이다.
- 날짜:
  2026-05-19

- 결정:
  초기 creative 보드에는 점수표나 우선순위 평가표를 두지 않는다.
- 근거:
  초반부터 점수표를 두면 발산보다 평가 모드가 먼저 작동할 수 있다. `좋은 점`, `걱정되는 점`, `상태` 정도로 시작하고, 후보가 충분히 쌓인 뒤 필요하면 비교 기준을 별도로 논의한다.
- 날짜:
  2026-05-19

- 결정:
  art는 creative 카드 안에 가벼운 `아트/분위기 상상`을 두고, 후보 선택 후 별도 art 문서로 확장한다.
- 근거:
  처음부터 이미지 프롬프트나 레퍼런스 기록까지 붙이면 아이디어 발산보다 시각 확정이 먼저 올 수 있다.
- 날짜:
  2026-05-19

## 예상 밖 발견

- 작성 전.

## 회고

작성 전.
