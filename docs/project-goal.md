좋아. 나는 두 번째 프로젝트 `codex-harness-tgr-v1`의 목표를 이렇게 잡는 게 가장 좋아 보여.

> **목표:**
> DBZ에서 검증한 최소 Codex 하네스를 두 번째 Unity 프로젝트에 이식하고, 이번에는 **게임플레이보다 “Unity 프로젝트를 반복 가능하게 기획·아트 탐색·설계·데이터화·구현·검증하는 v1 하네스”**를 검증한다.

DBZ는 이미 “작은 Unity 2D 퍼즐 게임을 Codex 기반 워크플로우로 끝까지 만들 수 있는가”를 검증한 실험이었고, README에도 DBZ의 중심 산출물이 큰 게임이 아니라 문서 읽기, 사용자 인터뷰, ExecPlan, 구현 승인, Unity 구현, 검증, 인수인계 흐름을 확인한 기록이라고 되어 있어. ([GitHub][1]) 현재 상태도 M5 공개 포트폴리오/회고 패키지까지 완료했고, 5 x 5 격자에서 `BOT`이 `BOX`를 주워 `GOAL`에 배달하는 최소 루프까지 플레이 가능한 상태로 정리되어 있어. ([GitHub][1])

## 내 추천: TGR은 “Tiny Garden Restore” 계열이 좋다

`TGR`을 임시로 **Tiny Garden Restore**라고 본다면, 두 번째 프로젝트로 꽤 적합해.

DBZ가 검증한 것은:

> “단일 플레이 루프를 Codex 하네스로 만들 수 있는가?”

TGR에서 검증해야 할 것은:

> “기획 브레인스토밍, 아트 방향 탐색, 상태 변화, 오브젝트 해금, 데이터 기반 진행까지 포함한 작은 Unity 게임을 Codex 하네스로 안정적으로 만들 수 있는가?”

즉, DBZ가 **움직임/승패/Retry** 실험이었다면, TGR은 **기획/아트/상태/진행/해금/연출/데이터** 실험으로 가는 게 좋아.

예를 들면 이런 게임이야.

> 작은 정원을 복구하는 2D/탑다운 미니 게임.
> 플레이어는 제한된 행동 횟수 안에서 잡초 제거, 꽃 심기, 장식물 복구 같은 작업을 수행한다.
> 특정 조건을 만족하면 정원 오브젝트가 `망가짐 → 정리됨 → 복구됨` 상태로 바뀌고, 다음 오브젝트가 해금된다.

이건 DBZ보다 조금 복잡하지만, 아직 충분히 작아. 그리고 네가 궁금해하던 SNG식 오브젝트 상태 변화, 꿈의 정원류의 복구/해금 연출, 데이터 관리까지 아주 작게 실험할 수 있어.

## TGR의 핵심 실험 질문

이번 프로젝트는 게임 하나를 크게 만드는 게 아니라, 아래 질문에 답하는 실험이어야 해.

1. **DBZ 하네스를 다른 Unity 프로젝트에 재사용할 수 있는가?**
2. **Codex가 사용자 인터뷰 없이 임의로 게임 규칙을 만들지 않게 막을 수 있는가?**
3. **기획 브레인스토밍, 후보 압축, concept brief를 구현 사양과 분리해서 기록할 수 있는가?**
4. **아트 방향, 이미지 프롬프트, 생성 이미지 결과를 design/implementation과 섞지 않고 관리할 수 있는가?**
5. **Unity 프로젝트 셋업, 폴더 구조, 데이터 구조, 검증 기준을 v1 하네스 문서로 고정할 수 있는가?**
6. **단순 코드 구현이 아니라, 상태 변화/해금/데이터 기반 진행을 안정적으로 구현하게 만들 수 있는가?**
7. **다음 프로젝트에도 복사 가능한 “Unity 전용 하네스 최소 세트”를 만들 수 있는가?**

DBZ 회고에서도 다음 프로젝트에 가져갈 규칙으로 `README.md`, `AGENTS.md`, `PLANS.md`, `docs/current-state.md`, `docs/decisions.md`를 먼저 읽고, 사소하지 않은 작업은 인터뷰와 공유된 이해 검증 뒤 ExecPlan을 만들며, ExecPlan 생성 승인과 구현 승인을 분리하라고 정리되어 있어. ([GitHub][2]) 또 DBZ 회고는 Unity MCP, custom skill, hooks, subagent는 아직 보류하고, 반복 마찰이 확인되면 다시 검토하자는 결론을 냈어. ([GitHub][2])

그래서 TGR v1은 처음부터 MCP/hooks/skill/subagent로 가기보다, **문서 하네스를 Unity 프로젝트에 더 특화하는 실험**으로 가는 게 좋아.

## TGR에서 DBZ보다 한 단계 올릴 부분

DBZ에서는 주로 “하네스가 작동하는가”를 봤다면, TGR에서는 아래 6개를 추가로 검증하면 좋겠어.

### 1. Creative 기획 흐름

DBZ에서는 구현 가능한 작은 루프를 바로 좁히는 흐름이 강했어. TGR에서는 실제 협업처럼 먼저 기획 아이디어를 넓히고, 후보를 압축하고, 기획 초안을 만드는 흐름을 문서로 남기는 게 좋아.

```text
docs/creative/README.md
docs/creative/01-brainstorming.md
docs/creative/02-concept-candidates.md
docs/creative/03-concept-brief.md
```

여기서 중요한 건 `docs/creative`가 확정 구현 사양이 아니라는 점이야.
아이디어와 후보는 작업장에 남기고, player-facing 규칙이나 구현 기준으로 쓸 내용만 별도 검증과 승인 후 `docs/design`으로 넘어가야 해.

### 2. Art 방향과 이미지 생성 기록

TGR은 완성 아트가 없어도 되지만, 아트 방향성과 이미지 생성 기록은 필요해.

```text
docs/art/README.md
docs/art/01-art-direction.md
docs/art/02-image-prompts.md
docs/art/03-generated-results.md
docs/art/images/
```

내용은 아주 작게 시작하면 돼.

```text
- 따뜻한 정원 복구 느낌
- 파스텔톤
- 2D top-down 또는 2.5D 느낌
- 임시 도형/텍스트 표식 허용
- 이미지 프롬프트와 생성 결과의 채택/보류/폐기 이유 기록
```

여기서 중요한 건 “아트를 잘 만드는 것”이 아니라, **Codex가 화면을 구성할 때 어떤 분위기를 기준으로 삼아야 하는지**와 **생성 이미지가 곧바로 Unity 에셋 또는 gameplay 사양이 아니라는 경계**를 고정하는 거야.

### 3. Unity Project Setup 문서화

DBZ에는 최소 하네스가 있었지만, Unity 전용 셋업 질문은 아직 약했어. TGR에는 이 문서가 들어가면 좋아.

```text
docs/unity/project-setup.md
```

여기에는 이런 선택을 기록해.

```text
- Unity 버전
- 2D/3D 여부
- URP 사용 여부
- 씬 구성 원칙
- 입력 방식
- UI 방식
- 데이터 방식
- 테스트 방식
- 금지할 패키지
- 수동 검증 방식
- Codex가 임의로 바꾸면 안 되는 설정
```

이게 v1의 핵심이야.
DBZ의 `AGENTS.md`, `PLANS.md`가 “작업 규칙”이었다면, TGR의 `docs/unity/project-setup.md`는 “Unity 프로젝트 선택지 고정 문서”가 되는 거지.

### 4. 데이터 기반 오브젝트 상태

TGR의 게임 목표는 복잡한 조작보다 이쪽이 좋아.

```text
GardenObject
- id
- displayName
- requiredResource
- prerequisiteObjectIds
- states: Locked / Dirty / Cleaned / Restored
```

또는 더 단순하게:

```text
정원 오브젝트 3개
- Broken Fountain
- Weed Patch
- Flower Bed

각 오브젝트 상태
- Locked
- Available
- Restored
```

DBZ는 `BOT`, `BOX`, `GOAL`의 규칙이 코드 안에 가까웠다면, TGR은 최소한의 데이터 정의를 둬서 Codex가 “데이터를 읽고 상태를 바꾸는 게임”을 만들게 하는 게 좋아.

### 5. 검증 기준 확장

DBZ에서는 Play Mode 체크리스트와 Edit Mode 테스트가 잘 작동했어. DBZ 회고에서도 수동 Play Mode 검증과 Edit Mode 테스트를 함께 두는 방식이 유효했다고 정리되어 있어. ([GitHub][2])

TGR에서는 검증을 이렇게 나누면 좋아.

```text
docs/verification/play-mode-checklist.md
docs/verification/data-state-checklist.md
```

검증 항목 예시:

```text
- 게임 시작 시 오브젝트 3개가 보인다.
- Locked 상태 오브젝트는 복구할 수 없다.
- Available 상태 오브젝트는 자원이 충분하면 복구할 수 있다.
- 복구 후 시각 상태가 바뀐다.
- 복구 후 다음 오브젝트가 해금된다.
- Retry 또는 Reset으로 초기 상태로 돌아간다.
- Console Error가 없다.
```

이러면 DBZ보다 한 단계 더 실무적인 검증이 돼.

### 6. 하네스 v1 평가 문서

TGR의 마지막 산출물은 게임 자체보다 이 문서가 중요해.

```text
docs/harness-v1-retrospective.md
```

여기서 평가할 질문은:

```text
- DBZ 하네스 재사용이 쉬웠는가?
- 어떤 문서는 그대로 복사 가능했는가?
- 어떤 문서는 프로젝트마다 다시 작성해야 했는가?
- Unity 전용 setup 문서는 효과가 있었는가?
- Codex가 임의로 게임 규칙을 만들려는 상황이 줄었는가?
- 데이터/상태 기반 구현에서 마찰이 생겼는가?
- 이제 local skill로 빼도 되는 반복 규칙이 생겼는가?
- hooks/MCP/subagent가 필요한 실제 근거가 생겼는가?
```

이 문서가 있어야 “v1 하네스 실험”이 끝났다고 볼 수 있어.

## 추천 마일스톤

나는 TGR을 이렇게 자르는 게 좋다고 봐.

```text
M0. Bootstrap & Harness Reuse Check
M0.5. Creative Planning & Art Direction Flow
M1. Core Beliefs & Game Loop Interview
M2. Unity Setup + Data Model
M3. First Playable Restore Loop
M4. Unlock / Visual State / Verification Loop
M5. Handoff + Harness v1 Retrospective
```

### M0. Bootstrap & Harness Reuse Check

목표:

```text
DBZ 하네스를 TGR에 이식하고, DBZ 전용 내용이 남아 있지 않은지 검증한다.
```

산출물:

```text
README.md
AGENTS.md
PLANS.md
docs/current-state.md
docs/decisions.md
docs/design/core-beliefs.md
docs/unity/project-setup.md
exec-plans/000-bootstrap.md
```

DBZ의 재사용 가이드에서도 최소 하네스 재사용 기준은 `.gitignore`, `README.md`, `AGENTS.md`, `PLANS.md`, `docs/current-state.md`, `docs/decisions.md`, `docs/design/README.md`, `docs/design/core-beliefs.md`, `exec-plans/000-bootstrap.md` 구조로 정리되어 있어. ([GitHub][3]) 그리고 새 프로젝트에서는 `README.md`, `docs/current-state.md`, `docs/decisions.md`, `core-beliefs.md`, `000-bootstrap.md`를 새 프로젝트 기준으로 초기화해야 한다고 되어 있어. ([GitHub][3])

### M0.5. Creative Planning & Art Direction Flow

목표:

```text
M1에서 gameplay 방향을 확정하기 전에, 기획 아이디어와 아트 방향을 별도 작업장에 기록하고 엄격 모드 라우팅 기준을 검증한다.
```

산출물:

```text
docs/creative/README.md
docs/creative/01-brainstorming.md
docs/creative/02-concept-candidates.md
docs/creative/03-concept-brief.md
docs/art/README.md
docs/art/01-art-direction.md
docs/art/02-image-prompts.md
docs/art/03-generated-results.md
docs/art/images/
exec-plans/001-creative-art-workflow.md
```

이 단계에서 Codex가 해야 할 일은 구현이 아니라 라우팅이야.

```text
creative/art 내용은 먼저 해당 폴더에 기록한다.
그 내용이 플레이어 경험이나 구현 기준을 바꾸면 docs/design 갱신 절차로 넘긴다.
그렇지 않으면 docs/design은 건드리지 않는다.
```

특히 이미지 생성 결과는 art 후보 또는 참고 자료일 뿐이야.
실제 Unity 에셋으로 쓰려면 별도 design 또는 ExecPlan 승인 절차가 필요해.

### M1. Core Beliefs & Game Loop Interview

목표:

```text
TGR이 어떤 게임인지 구현 전에 확정한다.
```

여기서 Codex가 해야 할 일은 구현이 아니라 질문이야.

질문 예시:

```text
1. 이 게임의 핵심 재미는 복구 자체인가, 퍼즐 해결인가, 자원 관리인가?
2. 플레이어 조작은 클릭인가, 격자 이동인가, 버튼 선택인가?
3. 오브젝트 상태는 몇 단계까지 둘 것인가?
4. 자원은 하나만 둘 것인가?
5. 실패 조건이 필요한가, 아니면 복구 완료만 볼 것인가?
6. 1분 안에 보여줄 수 있는 장면은 무엇인가?
```

DBZ 재사용 가이드도 새 프로젝트의 `core-beliefs.md`는 처음에 `상태: 작성 전`으로 두고, 사용자 인터뷰와 공유된 이해 검증 후에만 초안으로 작성하며, 명시 승인 뒤에만 승인 상태로 바꾸라고 정리해 두었어. ([GitHub][3])

### M2. Unity Setup + Data Model

목표:

```text
구현 전에 Unity 구조와 데이터 구조를 고정한다.
```

산출물:

```text
docs/unity/project-setup.md
docs/data/garden-object-model.md
docs/verification/data-state-checklist.md
```

이 단계에서 아직 본격 구현하지 않는 게 좋아.
TGR의 핵심은 “Codex가 구현 전에 선택지를 확인하고 고정하는가”니까.

### M3. First Playable Restore Loop

목표:

```text
정원 오브젝트 하나를 복구하는 최소 플레이 루프를 만든다.
```

M3 기준은 작게 잡아야 해.

```text
- Play Mode 시작
- 정원 화면 표시
- 자원 수치 표시
- 복구 가능한 오브젝트 1개 표시
- 버튼 또는 클릭으로 복구
- 자원 감소
- 오브젝트 상태 변화
- 완료 상태 표시
- Retry/Reset 가능
```

DBZ의 M1이 `Start → Move → Pickup → Deliver → Result → Retry`였다면, TGR의 M3는:

```text
Start → Select Object → Restore → State Change → Unlock/Complete → Retry
```

이 정도면 충분해.

### M4. Unlock / Visual State / Verification Loop

목표:

```text
복구 상태 변화와 해금 조건을 최소 2~3개 오브젝트로 확장한다.
```

여기서 TGR다운 맛이 나와.

```text
- 오브젝트 A 복구
- 오브젝트 B 해금
- 오브젝트 B 복구
- 정원 전체 Progress 증가
- 모든 오브젝트 복구 시 Clear
```

중요한 건 오브젝트 수가 아니라, **상태 변화가 데이터/검증 문서와 연결되는지**야.

### M5. Handoff + Harness v1 Retrospective

목표:

```text
새 Codex 세션이 문서만 읽고 현재 상태를 이어받을 수 있는지 확인하고, v1 하네스가 무엇을 얻었는지 정리한다.
```

DBZ에서도 M4 Handoff Test가 하네스가 실제로 다음 세션에 전달 가능한지 확인하는 좋은 마감 검증이었다고 회고되어 있어. ([GitHub][2]) TGR에서도 이건 반드시 넣는 게 좋아.

## 이번 프로젝트에서 하지 않는 게 좋은 것

나는 TGR v1에서 아래는 아직 보류하는 게 맞다고 봐.

```text
- Unity MCP 도입
- hooks 도입
- subagent 도입
- custom skill 설치
- 복잡한 Clean Architecture
- VContainer/R3/UniTask 도입
- 세이브/로드 본격 구현
- 상점/재화/인벤토리 확장
- 3D 전환
- 외부 에셋 대량 사용
```

이유는 단순해.
TGR의 목적은 **하네스 v1 검증**이지, 기술 스택 확장이 아니야.

DBZ의 결정 문서에서도 최소 Codex 하네스로 시작하고, MCP/custom skill/hook/subagent는 실제 워크플로우 마찰이 생길 때까지 보류한다고 되어 있어. ([GitHub][4]) 또 `grill-me`, `deep-interview`, `brainstorming` 같은 외부 skill은 설치하지 않고 인터뷰 방식의 참고 원칙으로만 사용한다고 정리되어 있어. ([GitHub][4])

그래서 TGR에서도 당장은 이렇게 가는 게 좋아.

> **skill을 만들지 말고, skill로 빼야 할 반복 규칙을 발견하는 프로젝트로 둔다.**

이게 중요해.
처음부터 local skill을 만들면 “정말 반복되는 문제인지”와 “그냥 이번 프로젝트 특수 문제인지”가 구분이 안 돼.

## TGR의 최종 성공 기준

TGR은 아래를 만족하면 성공이라고 보면 돼.

### 최소 성공

```text
- DBZ 하네스가 TGR에 이식됨
- DBZ 전용 문구가 제거됨
- TGR용 README/current-state/decisions/bootstrap이 정리됨
- core-beliefs가 작성 전 상태로 시작함
- Codex가 사용자 인터뷰 없이 게임 구현을 시작하지 않음
```

### 실질 성공

```text
- 인터뷰를 통해 TGR core-beliefs와 gameplay loop가 승인됨
- creative 브레인스토밍, concept 후보, concept brief 초안이 분리됨
- art direction, 이미지 프롬프트, 생성 결과 기록 기준이 생김
- Unity project setup 문서가 생김
- 데이터 기반 GardenObject 상태 모델이 생김
- Play Mode에서 오브젝트 1개 이상을 복구할 수 있음
- 수동 검증 체크리스트가 있음
```

### 완전 성공

```text
- 오브젝트 2~3개가 상태 변화/해금 흐름을 가짐
- Clear/Reset 흐름이 있음
- 데이터/상태 검증 기준이 있음
- 새 Codex 세션이 문서만 읽고 이어받을 수 있음
- docs/harness-v1-retrospective.md에 v1 평가가 정리됨
- 다음 프로젝트에서 template화할 후보와 아직 보류할 도구가 구분됨
```

## 내가 잡는 TGR의 한 문장 목표

이 문장을 README 상단 목표로 써도 될 정도야.

> **Tiny Garden Restore는 Codex Harness v1을 검증하기 위한 작은 Unity 2D 복구 게임 실험이다. 이 프로젝트의 목표는 큰 게임을 만드는 것이 아니라, 사용자 인터뷰, 기획 브레인스토밍, 아트 방향 탐색, Unity 셋업 결정, 데이터 기반 오브젝트 상태, Play Mode 검증, 세션 인수인계를 포함한 반복 가능한 Unity 개발 하네스를 검증하는 것이다.**

## 지금 바로 다음 단계

지금은 M0와 M0.5 이후라면, 다음 작업은 구현이 아니라 **creative 브레인스토밍과 core-beliefs 인터뷰 준비**야.

Codex에게 바로 던질 프롬프트는 이게 좋아.

```text
README.md, AGENTS.md, PLANS.md, docs/current-state.md, docs/decisions.md,
docs/creative/README.md, docs/creative/01-brainstorming.md,
docs/art/README.md, docs/art/01-art-direction.md,
docs/design/README.md, docs/design/core-beliefs.md,
exec-plans/000-bootstrap.md, exec-plans/001-creative-art-workflow.md를 읽어라.

이 프로젝트는 codex-harness-tgr-v1이다.

Delivery Bot Zero의 gameplay, 코드, 완료된 ExecPlan을 복사하지 마라.
현재 작업의 목적은 creative 브레인스토밍을 시작하기 전 상태를 점검하는 것이다.

다음을 수행하라.

1. 현재 저장소가 DBZ 하네스를 올바르게 초기화했는지 점검하라.
2. DBZ 전용 문구, DBZ 전용 결정, DBZ gameplay 기준이 남아 있는지 찾아라.
3. docs/current-state.md가 현재 TGR 상태를 정확히 설명하는지 점검하라.
4. docs/decisions.md에 남길 수 있는 장기 하네스 결정과 제거해야 할 DBZ 전용 결정을 구분하라.
5. docs/design/core-beliefs.md가 상태: 작성 전인지 확인하라.
6. 아직 gameplay 구현, Unity 씬 구현, 새 코드 작성은 하지 마라.
7. docs/creative와 docs/art가 구현 사양이 아니라 작업장으로 분리되어 있는지 확인하라.
8. 점검 결과를 요약하고, creative 브레인스토밍에서 먼저 확인해야 할 질문 목록을 제안하라.

파일을 수정하기 전에 어떤 파일을 수정할지와 수정 이유를 먼저 보고하라.
```

내 판단은 확실해.
**TGR은 DBZ보다 “조금 더 게임다운” 프로젝트가 아니라, “하네스 v1을 검증하기 위해 게임다운 요소를 조금 더 넣은 프로젝트”로 잡아야 해.** 그래야 두 번째 프로젝트가 끝났을 때 단순히 게임 하나가 아니라, 네가 계속 사용할 수 있는 Unity/Codex 개발 방식이 남는다.

[1]: https://github.com/karais89/codex-harness-dbz-v0 "GitHub - karais89/codex-harness-dbz-v0 · GitHub"
[2]: https://github.com/karais89/codex-harness-dbz-v0/blob/main/docs/harness-retrospective.md "codex-harness-dbz-v0/docs/harness-retrospective.md at main · karais89/codex-harness-dbz-v0 · GitHub"
[3]: https://github.com/karais89/codex-harness-dbz-v0/blob/main/docs/harness-reuse-guide.md "codex-harness-dbz-v0/docs/harness-reuse-guide.md at main · karais89/codex-harness-dbz-v0 · GitHub"
[4]: https://github.com/karais89/codex-harness-dbz-v0/blob/main/docs/decisions.md "codex-harness-dbz-v0/docs/decisions.md at main · karais89/codex-harness-dbz-v0 · GitHub"
