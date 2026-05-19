# Creative 문서 규칙

## 역할

`docs/creative`는 아이디어 발산, 후보 압축, 기획 초안 도출을 위한 작업장이다.

이 폴더의 문서는 확정 구현 사양이 아니다. Creative 산출물은 이후 `docs/design` 문서의 재료가 될 수 있지만, 그 자체로 gameplay ExecPlan이나 Unity 구현 기준이 되지 않는다.

Creative 작업은 단순 기록 요청이 아닌 한 `docs/workflows/grill-me.md`의 `Grill-Me Discovery Protocol`로 시작한다. Codex는 아이디어 목록을 바로 쓰지 않고, 사용자의 암묵적 기획 기준과 선택 기준을 먼저 질문으로 캐낸다.

## 먼저 읽기

Codex는 다음 작업을 시작하기 전에 이 문서를 읽는다.

- 게임 아이디어 브레인스토밍
- 기획 후보 정리
- 선택, 보류, 폐기 이유 기록
- concept brief 작성 또는 갱신
- creative 결과를 design 기준으로 넘길지 판단하는 작업

이 문서와 함께 `docs/workflows/grill-me.md`를 읽는다.

## 문서 흐름

Creative 작업은 기본적으로 다음 단계별 문서에 기록한다.

1. `01-brainstorming.md`: 아이디어 발산과 가능성 넓히기
2. `02-concept-candidates.md`: 후보 압축, 선택/보류/폐기 이유
3. `03-concept-brief.md`: 현재 채택한 기획 초안

각 문서는 `상태: 작성 전`으로 시작할 수 있다. 이 상태의 문서는 아직 실제 기획 산출물이 아니라 placeholder다.

## Grill-Me Discovery

Codex는 creative 작업에서 다음 decision branch가 닫히기 전에는 후보 압축이나 concept brief 작성으로 넘어가지 않는다.

- 이 게임 또는 실험의 정체성
- 플레이어가 느껴야 하는 감정과 리듬
- 초기 단계에서 하지 않을 것
- 브레인스토밍을 넓힐 기준
- 후보를 선택, 보류, 폐기할 기준
- concept brief로 넘길 수 있는 최소 합의
- design 문서로 넘기면 안 되는 미확정 아이디어

질문은 한 번에 하나만 한다. 각 질문에는 현재 이해, 막힌 결정, 질문, 추천 답안을 포함한다.

## 엄격 모드

Creative 작업 중 다음이 애매하면 Codex는 파일을 수정하지 않고 사용자에게 먼저 질문한다.

- 단순 아이디어 기록인지, 기획 초안에 반영할 내용인지
- creative 기록인지, `docs/design`의 구현 기준을 바꾸는 내용인지
- 새 후보를 추가할지, 기존 후보를 선택/보류/폐기할지
- concept brief를 갱신할지, 후속 design 문서 생성을 논의할지

질문 예:

```text
이 내용은 creative 후보로만 기록할까요,
아니면 구현 기준인 docs/design까지 바꾸는 변경으로 볼까요?
```

## Design으로 넘어가는 조건

Creative 문서의 내용이 플레이어 경험, 게임 규칙, 목표, 조작, 피드백, 화면 상태, 구현 기준을 바꾸면 `docs/design` 갱신 절차로 넘어가야 한다.

이때 Codex는 creative 문서를 그대로 확정 사양처럼 사용하지 않는다. 먼저 사용자와 공유된 이해를 검증하고, 명시 승인된 내용만 `docs/design` 문서에 반영한다.

## 금지 사항

- Creative 아이디어를 근거로 gameplay 구현을 바로 시작하지 않는다.
- `03-concept-brief.md`를 승인된 design 문서처럼 사용하지 않는다.
- 폐기 또는 보류된 아이디어를 조용히 구현 범위에 포함하지 않는다.
- 사용자 승인 없이 creative 산출물을 `상태: 승인됨`인 design 기준으로 바꾸지 않는다.
