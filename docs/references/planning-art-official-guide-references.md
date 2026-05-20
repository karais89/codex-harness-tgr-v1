# 기획/아트 공식 가이드 레퍼런스

> 추천 저장 경로: `docs/references/planning-art-official-guide-references.md`  
> 작성일: 2026-05-20  
> 용도: Tiny Garden Restore의 `M1.5. 기획/아트 기준 정리` 단계에서 참고할 공식/검증 레퍼런스를 한 곳에 모아둔다.  
> 적용 범위: `docs/creative/tiny-garden-creative-spec.md`, `docs/art/tiny-garden-art-concept.md`, `docs/art/tiny-garden-image-prompts.md`, `docs/milestones/M1.5-checklist.md`

---

## 0. 이 문서를 사용하는 방식

M1.5는 무거운 GDD나 대규모 아트 바이블을 만드는 단계가 아니다.  
이 문서는 M2~M5 구현이 흔들리지 않도록 다음 기준을 고정하기 위한 레퍼런스다.

- 기획 문서 기준: Unity Learn의 간단 GDD 구조를 기준으로 한다.
- 플레이 감각 검증 기준: MDA 프레임워크를 보조 기준으로 사용한다.
- 아트 방향 기준: Unity Learn의 Art & Visuals 항목과 Unity Manual의 2D art style/perspective 기준을 사용한다.
- 이미지 프롬프트 기준: OpenAI 공식 Image Generation 문서와 GPT Image prompting guide를 사용한다.
- 문서 품질 기준: NASA 요구사항 작성 체크리스트를 “게임 문서용 검수 기준”으로 낮춰 적용한다.

M1.5 산출물은 다음 질문에 답할 수 있어야 한다.

1. 이 게임의 한 줄 정의는 무엇인가?
2. 플레이어는 무엇을 보고, 무엇을 누르고, 무엇이 바뀌는가?
3. 복구 대상은 정확히 무엇인가?
4. 어떤 시점과 어떤 아트 스타일로 보이게 할 것인가?
5. 생성 이미지는 어떤 기준으로 만들고, 어떤 기준으로 폐기할 것인가?
6. M2에서 Unity Scene을 만들 때 참조할 기준이 충분히 명확한가?

---

## 1. 기획 문서 / GDD 레퍼런스

### 1.1 Unity Learn — Create a Game Design Document

- URL: https://learn.unity.com/pathway/game-development/unit/planning-a-game/tutorial/game-dev-create-a-game-design-document
- 유형: Unity 공식 학습 문서
- 사용 목적: Tiny Garden Restore의 “경량 GDD / Creative Spec” 구조 기준

핵심 요지:

- GDD는 게임의 목표, 메커닉, 감각, 비주얼 방향, 개발 계획을 담는 living document다.
- GDD는 팀원, 플레이테스터, 포트폴리오 리뷰어에게 비전을 설명하는 커뮤니케이션 도구다.
- 디자인 결정의 기록이자, 문서화 과정에서 빈틈과 불일치를 발견하는 문제 해결 도구다.
- Unity의 간단 GDD 템플릿은 다음 항목을 포함한다.
  - Introduction: 이름, 제목, 한 문장 피치, 동사
  - Core Design Elements: 플레이어 목표, 규칙/메커닉, 난이도, core loop, feedback
  - Art & Visuals: 통일 색상, 영감 자료
  - Future Features: stretch goal과 기타 고려 사항
  - Optional: 장르, 타깃, 플랫폼, 수익화

Tiny Garden Restore 적용:

- `tiny-garden-creative-spec.md`는 Unity의 간단 GDD 중 다음만 채택한다.
  - 한 줄 정의
  - 플레이어 동사
  - 플레이어 목표
  - 규칙/메커닉
  - core loop
  - feedback
  - 하지 않을 것
- 다음 항목은 M1.5에서 제외한다.
  - 타깃 유저 분석
  - 경쟁작 분석
  - 수익화
  - LiveOps
  - 장문 세계관
  - 세부 레벨 디자인
  - 완성형 UI/Audio/Marketing 기획

M1.5 검수 기준:

- 한 줄 정의가 1문장으로 존재하는가?
- 플레이어의 핵심 행동이 명확한가?
- 최소 playable loop가 5단계 이하로 설명되는가?
- M2~M5 구현 범위를 넘어서는 항목이 “하지 않을 것”에 들어가 있는가?

---

### 1.2 Unity Learn — Game Design

- URL: https://learn.unity.com/pathway/game-development/unit/planning-a-game/tutorial/game-design
- 유형: Unity 공식 학습 문서
- 사용 목적: 기획 문서를 “아이디어 설명”이 아니라 “게임 구성 요소”로 정리하기 위한 기준

핵심 요지:

- 게임 디자인은 Unity/C#으로 구현하는 개발과 다르다.
- 게임은 goals, rules and mechanics, challenge, feedback 같은 구성 요소로 나눠 볼 수 있다.
- core loop는 플레이어 경험을 형성하는 핵심 구조다.

Tiny Garden Restore 적용:

- Goals: 세 복구 대상을 모두 복구한다.
- Rules and mechanics: 플레이어는 대상 근처에서 `E`를 눌러 복구한다.
- Challenge: M1.5~M5에서는 복잡한 실패나 시간 압박을 만들지 않는다. 대신 “대상 인식과 상태 변화”가 명확해야 한다.
- Feedback: 복구 전/후 시각 변화와 완료 표시가 있어야 한다.

M1.5 검수 기준:

- 목표, 규칙, 피드백이 서로 분리되어 적혀 있는가?
- challenge를 과하게 추가하지 않았는가?
- feedback이 구현 가능한 수준으로 정의되어 있는가?

---

### 1.3 MDA: A Formal Approach to Game Design and Game Research

- URL: https://aaai.org/papers/ws04-04-001-mda-a-formal-approach-to-game-design-and-game-research/
- 유형: AAAI Workshop Paper / 검증된 게임 디자인 프레임워크
- 사용 목적: “조용한 복구” 같은 감각을 구현 가능한 규칙과 연결하기 위한 보조 기준

핵심 요지:

- MDA는 Mechanics, Dynamics, Aesthetics로 게임을 나누어 이해한다.
- 게임 디자인, 개발, 비평, 연구 사이의 간극을 줄이기 위해 제안된 프레임워크다.

Tiny Garden Restore 적용:

| MDA | TGR 적용 |
|---|---|
| Aesthetics | 조용한 복구, 작지만 명확한 회복감, 아늑한 봄 정원 |
| Dynamics | 방치된 대상이 복구된 대상으로 바뀌며 장면이 정돈되는 흐름 |
| Mechanics | 이동, 근처 판정, `E` 입력, 대상 상태 전환, 완료 판정 |

M1.5 검수 기준:

- “조용한 복구”가 단순 감성어로 끝나지 않고, 상태 변화/피드백/상호작용으로 연결되는가?
- 플레이 감각과 실제 메커닉이 충돌하지 않는가?

---

## 2. 아트 방향 / 2D 비주얼 레퍼런스

### 2.1 Unity Learn — Fill out a Game Design Document: Art & Visuals

- URL: https://learn.unity.com/tutorial/fill-out-a-game-design-document
- 유형: Unity 공식 학습 문서
- 사용 목적: `tiny-garden-art-concept.md`의 최소 항목 기준

핵심 요지:

- Art & Visuals 섹션은 게임의 미적 요소를 다룬다.
- 포함 항목은 inspiration, concept art, unifying colors다.
- concept art는 직접 제작하거나 generative AI를 사용할 수 있다.
- 인터넷에서 참고 이미지를 큐레이션할 경우 출처와 크레딧을 남겨야 한다.
- 색상 체계는 분위기와 통일성에 영향을 주며, hex code 또는 RGB 값을 남기면 이후 참조하기 쉽다.

Tiny Garden Restore 적용:

- `tiny-garden-art-concept.md`에는 다음만 남긴다.
  - 스타일: cozy 2D
  - 시점: top-down
  - 팔레트: spring garden palette
  - 주요 실루엣: small gardener
  - 복구 전/후 대비 방식
  - 금지 요소
- 실제 색상은 M1.5에서 최소 4~6개 수준으로만 정한다.
- 생성 이미지는 구현용 최종 에셋이 아니라 concept reference로만 사용한다.

M1.5 검수 기준:

- 스타일, 시점, 팔레트가 분리되어 적혀 있는가?
- 이미지가 구현용 에셋이 아님을 명시했는가?
- 참고 이미지나 생성 이미지에 대한 출처/생성 정보 기록란이 있는가?

---

### 2.2 Unity Manual — Creating a 2D game

- URL: https://docs.unity3d.com/2022.3/Documentation/Manual/Quickstart2DCreate.html
- 유형: Unity 공식 매뉴얼
- 사용 목적: M2 Scene 구성 전에 시점과 아트 스타일을 먼저 정해야 하는 근거

핵심 요지:

- Unity 2D 게임을 만들기 전에 game perspective와 art style을 결정해야 한다.
- 2D 게임에서도 Unity Scene은 3D 공간이지만 일반적으로 z축을 무시하고 작업한다.
- 2D 개발에서 sprites, environment building, character animation, graphics, physics 2D, UI 등을 순서대로 이해해야 한다.

Tiny Garden Restore 적용:

- M1.5에서 시점은 `top-down`으로 고정한다.
- M1.5에서 스타일은 `cozy 2D`로 고정한다.
- M2에서는 Unity Scene과 카메라 구성을 이 기준에 맞춘다.
- M1.5에서는 Unity Scene이나 `Assets/`를 변경하지 않는다.

M1.5 검수 기준:

- M2에서 만들 Scene의 카메라/시점 기준이 명확한가?
- “2D top-down”과 맞지 않는 side-view/platformer 식 표현을 금지했는가?

---

### 2.3 Unity Manual — Art styles for 2D games

- URL: https://docs.unity3d.com/2023.2/Documentation/Manual/Quickstart2DArt.html
- 유형: Unity 공식 매뉴얼
- 사용 목적: `cozy 2D`를 Unity 2D art style 분류에 맞춰 설명하기 위한 기준

핵심 요지:

Unity는 2D art style 예시로 다음을 든다.

- Minimalist: flat colors, clean lines, high readability
- Pixel art: retro/pixelated style
- Illustrative: cartoon, stylized, realistic art style
- Pre-rendered 3D: 3D 툴로 만든 이미지를 Sprite로 사용하는 방식

Tiny Garden Restore 적용:

- TGR의 `cozy 2D`는 다음 조합으로 정의한다.
  - Illustrative 기반
  - Minimalist의 readable shape와 clean composition 일부 채택
  - Pixel art와 pre-rendered 3D는 M1.5 기준에서 제외
- 구현용 에셋이 아니라 컨셉 기준이므로 “정확한 화풍”보다 “읽히는 형태와 분위기”를 우선한다.

M1.5 검수 기준:

- 스타일 정의가 너무 넓지 않은가?
- Pixel art, realistic 3D render, side-view illustration처럼 다른 방향으로 오해될 표현을 금지했는가?
- 작은 화면에서도 복구 대상 3개가 구분될 정도로 readable shape를 강조했는가?

---

### 2.4 Unity Manual — Sprite Import Settings

- URL: https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-sprite.html
- 유형: Unity 공식 매뉴얼
- 사용 목적: 향후 M2 이후 실제 Sprite를 넣을 때 참고할 기술 기준

핵심 요지:

- Sprite texture type은 이미지 에셋을 Unity 2D 기능에서 사용할 수 있게 포맷한다.
- Sprite Mode는 Single, Multiple, Polygon 등을 지원한다.
- Pixels Per Unit은 Sprite 이미지의 픽셀과 Unity 월드 단위의 대응 관계를 정한다.
- Pivot은 Sprite의 local coordinate system 원점 위치다.

Tiny Garden Restore 적용:

- M1.5에서는 실제 Sprite import 기준까지 확정하지 않아도 된다.
- 단, M2 이후 placeholder/sprite를 넣을 때 다음 항목을 별도 문서에서 정하면 좋다.
  - Pixels Per Unit
  - Pivot 기준
  - Sprite Mode
  - Sorting Layer
  - 타일/오브젝트 크기 기준

M1.5 검수 기준:

- M1.5 문서가 실제 에셋 import 세부 설정까지 과하게 확장되지 않았는가?
- “컨셉 참고용 이미지”와 “Unity Sprite 에셋”을 구분했는가?

---

## 3. 이미지 생성 / GPT Image 프롬프트 레퍼런스

### 3.1 OpenAI API Docs — Image generation

- URL: https://developers.openai.com/api/docs/guides/image-generation
- 유형: OpenAI 공식 API 문서
- 사용 목적: GPT Image 기반 이미지 생성/편집의 공식 기능 기준

핵심 요지:

- OpenAI API는 텍스트 프롬프트로 이미지를 생성하거나 편집할 수 있다.
- GPT Image models에는 최신 이미지 생성 모델인 `gpt-image-2`가 포함된다.
- Image API는 단일 프롬프트에서 이미지를 생성/편집할 때 적합하다.
- Responses API는 대화형/멀티스텝 이미지 생성 및 편집 흐름에 적합하며, `gpt-5.5` 같은 mainline model에서 `image_generation` tool을 호출한다.
- Image API에서는 `gpt-image-2`를 직접 지정해 이미지를 생성할 수 있다.
- Responses API의 이미지 생성 호출은 성능 개선을 위해 프롬프트를 자동 보정할 수 있으며, 제공되는 경우 `revised_prompt` 필드에서 확인한다.
- 품질, 크기, 포맷, 압축 등을 조정할 수 있다.

Tiny Garden Restore 적용:

- M1.5 컨셉보드 1장은 단일 이미지 생성이므로 Image API의 `gpt-image-2` 또는 Responses API의 `image_generation` tool 중 더 단순한 쪽을 선택한다.
- 이미지 생성 자동화가 M1.5의 핵심 완료 조건은 아니다.
- Codex 환경에서 이미지 생성 도구를 직접 사용할 수 없으면, 사용자가 별도로 이미지를 생성해 `docs/art/images/`에 추가해도 된다.

M1.5 검수 기준:

- 프롬프트 문서에 사용 도구/모델/생성일 기록란이 있는가?
- Responses API를 사용했다면 `revised_prompt` 기록란이 있는가?
- 생성 이미지가 최종 에셋이 아니라 컨셉 참고용임을 명시했는가?

---

### 3.2 OpenAI Cookbook — GPT Image Generation Models Prompting Guide

- URL: https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide
- 유형: OpenAI 공식 Cookbook / GPT Image prompting guide
- 사용 목적: `tiny-garden-image-prompts.md`의 프롬프트 작성 기준

핵심 요지:

- `gpt-image-2`는 신규 빌드의 기본 선택지로 권장되는 고품질 이미지 모델이다.
- 프롬프트는 `Draw...` 또는 `Edit...`처럼 수행할 시각 작업을 직접 시작점으로 줄 수 있다.
- 프롬프트 형식은 minimal prompt, descriptive paragraph, JSON-like structure, instruction-style, tag-based 모두 가능하다.
- 중요한 것은 의도와 제약이 명확하고, 유지보수하기 쉬운 템플릿을 쓰는 것이다.
- 사람/캐릭터가 포함되면 scale, body framing, gaze, object interactions를 구체화하면 좋다.
- 금지/유지 조건은 명시적으로 적어야 한다. 예: no watermark, no extra text, no logos/trademarks.
- 긴 프롬프트를 한 번에 과하게 넣기보다, 깨끗한 base prompt에서 작은 변경으로 반복 개선하는 것이 디버깅하기 쉽다.

Tiny Garden Restore 적용:

- 프롬프트는 다음 구조를 권장한다.
  - Purpose
  - Scene
  - Must include
  - Style
  - Composition
  - Avoid
  - Output role
- 작은 정원사 캐릭터는 다음을 명시한다.
  - small gardener
  - top-down scale
  - simple recognizable silhouette
  - hat/apron/tool 같은 식별 요소
- 반드시 금지한다.
  - text
  - labels
  - watermark
  - UI
  - logo
  - combat
  - monsters
  - dark horror mood
  - photorealistic 3D render
  - side-view platformer perspective

M1.5 검수 기준:

- 프롬프트가 예쁜 이미지가 아니라 “M2 구현 기준을 고정하는 컨셉 이미지”를 만들도록 되어 있는가?
- `exactly three clear restoration targets`와 복구 대상 3개가 명시되어 있는가?
- top-down, cozy 2D, spring palette가 명시되어 있는가?
- 금지 요소가 명시되어 있는가?
- 한 번 생성 후 바로 확정하지 않고, 육안 검수/폐기 기준이 있는가?

---

### 3.3 OpenAI API Docs — Prompt guidance

- URL: https://developers.openai.com/api/docs/guides/prompt-guidance
- 유형: OpenAI 공식 API 문서
- 사용 목적: 문서/계획/시각 산출물 검증 프롬프트 기준

핵심 요지:

- 시각 산출물은 렌더링 후 layout, clipping, spacing, missing content, visual consistency를 검사해야 한다.
- 구현 계획은 요구사항이 어디에 반영되는지, 관련 파일/API/시스템, 상태 전이, 검증 명령 또는 체크, 실패 동작, open questions가 추적 가능해야 한다.
- 복잡한 프롬프트는 Role, Goal, Success criteria, Constraints, Output, Stop rules 같은 구조로 시작할 수 있다.

Tiny Garden Restore 적용:

- `tiny-garden-image-prompts.md`에는 생성 결과 검수 기준을 반드시 둔다.
- M1.5 checklist에는 “실제 이미지를 열어 육안 검수”를 포함한다.
- M2 이후 Codex 작업 계획은 M1.5 문서의 어떤 기준을 참조하는지 명시해야 한다.

M1.5 검수 기준:

- 이미지 검수 항목이 “예쁘다/별로다”가 아니라 관찰 가능한 기준인가?
- M2가 참조할 문서와 항목이 명확한가?

---

### 3.4 OpenAI API Docs — Using GPT-5.5

- URL: https://developers.openai.com/api/docs/guides/latest-model
- 유형: OpenAI 공식 API 문서
- 사용 목적: GPT-5.5 계열에 작업을 맡길 때의 프롬프트 운영 기준

핵심 요지:

- GPT-5.5는 명확한 목표, 성공 기준, 허용되는 side effect, evidence rule, output shape를 제공할 때 강하다.
- 지나치게 긴 단계별 절차보다 outcome-first prompt가 잘 맞는다.
- coding workflow에서는 reuse, test expectations, acceptance criteria, 언제 계속하고 언제 멈출지 등을 명확히 해야 한다.

Tiny Garden Restore 적용:

- M1.5 생성/수정 프롬프트는 다음을 포함한다.
  - 목표: M2 전 기획/아트 기준 고정
  - 성공 기준: 문서 존재, 충돌 없음, M2 참조 가능, 이미지 검수 가능
  - side effect 제한: Unity Scene/Assets/gameplay code 변경 금지
  - output shape: Markdown 파일 단위
- Codex에게 “긴 GDD를 만들어라”가 아니라 “M2 구현 기준으로 충분한 경량 문서를 만들어라”라고 지시한다.

M1.5 검수 기준:

- 작업 프롬프트가 결과물과 성공 기준을 먼저 말하는가?
- 허용되지 않는 변경 범위가 명확한가?

---

## 4. 요구사항 품질 / 문서 검증 레퍼런스

### 4.1 NASA — Appendix C: How to Write a Good Requirement

- URL: https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/
- 유형: NASA 공식 요구사항 작성 가이드
- 사용 목적: 기획/아트 문서를 “검증 가능한 문장”으로 만들기 위한 품질 기준

핵심 요지:

- `shall`은 requirement, `will`은 목적/사실 선언, `should`는 goal로 구분한다.
- requirement는 능동태로 작성하고, 일관된 용어를 사용해야 한다.
- 요구사항은 구현 방법이 아니라 필요한 것, 즉 WHAT을 말해야 한다.
- 문법/오타/스타일 규칙을 지키고, TBD를 최소화하며, 가정과 rationale을 함께 남겨야 한다.

Tiny Garden Restore 적용:

게임 문서에서는 NASA 문장 형식을 그대로 쓰기보다 다음처럼 낮춰 적용한다.

- 좋은 문장: “플레이어는 복구 대상 근처에서 `E`를 누르면 대상을 복구할 수 있어야 한다.”
- 나쁜 문장: “복구가 자연스럽고 기분 좋게 되면 좋겠다.”
- 좋은 문장: “복구 대상은 잡초, 시든 꽃, 더러운 타일 3개로 제한한다.”
- 나쁜 문장: “정원에 여러 가지 고칠 것이 있으면 좋겠다.”

M1.5 검수 기준:

- 각 요구사항이 눈으로 확인 가능하거나 Play Mode에서 확인 가능한가?
- “아늑한”, “조용한” 같은 감성어가 실제 상태 변화/색감/구성 기준으로 연결되는가?
- 구현 방법을 과하게 지정하지 않았는가?
- 문서마다 같은 용어를 쓰는가?

---

### 4.2 NASA — Technical Requirements Definition

- URL: https://www.nasa.gov/reference/4-2-technical-requirements-definition/
- 유형: NASA 공식 시스템 엔지니어링 문서
- 사용 목적: M1.5를 M2 전 baseline gate로 두는 근거

핵심 요지:

- 요구사항은 clear, correct, complete, achievable한 상태로 검증된 뒤 stakeholder agreement를 얻고 baseline화할 수 있다.
- 승인된 요구사항은 해결해야 할 문제와 요구사항을 완전하게 설명하는 기준 세트가 된다.

Tiny Garden Restore 적용:

- M1.5는 “기획/아트 baseline”이다.
- M1.5 완료 전에는 M2 Scene 구성을 시작하지 않는다.
- M1.5 완료 후 M2~M5는 이 문서를 참조해 구현한다.
- M1.5 이후 변경이 필요하면 `docs/decisions.md` 또는 해당 문서의 결정 기록에 남긴다.

M1.5 검수 기준:

- M1.5가 완료되면 M2 작업자가 무엇을 만들지 충분히 알 수 있는가?
- 변경이 생겼을 때 어디에 기록할지 정해져 있는가?

---

## 5. Tiny Garden Restore M1.5에 적용할 최소 문서 원칙

### 5.1 Creative Spec 원칙

`docs/creative/tiny-garden-creative-spec.md`는 다음만 포함한다.

- 목적
- 한 줄 정의
- 플레이 감각
- 플레이어 동사
- 최소 플레이 루프
- 복구 대상 3개
- 상호작용 방식
- 완료 조건
- 하지 않을 것
- 결정 기록

금지:

- 장문 세계관
- 캐릭터 서사
- 여러 스테이지
- 인벤토리/상점/경제
- 세이브/로드
- 복잡한 UI
- M2~M5 밖의 기능 설계

---

### 5.2 Art Concept 원칙

`docs/art/tiny-garden-art-concept.md`는 다음만 포함한다.

- 목적
- 스타일
- 시점
- 팔레트
- 작은 정원사 실루엣
- 복구 전/후 표현 기준
- 금지 요소
- 컨셉 이미지 사용 범위
- 결정 기록

금지:

- 최종 에셋 사양으로 오해될 정도의 세부 설정
- Sprite import 세부값 고정
- production art pipeline 설계
- 에셋 제작 일정
- 외부 에셋 구매/라이선스 검토

---

### 5.3 Image Prompt 원칙

`docs/art/tiny-garden-image-prompts.md`는 다음만 포함한다.

- 목적
- 사용 도구/모델 기록
- 최종 프롬프트
- `revised_prompt` 기록란
- 피해야 할 요소
- 생성 결과 검수 기준
- 생성 결과 기록
- 폐기/재생성 사유 기록

권장 프롬프트 시작:

```text
Draw one cozy top-down 2D concept board...
```

필수 금지어:

```text
No text, no labels, no watermark, no UI, no logo, no inventory icons, no shop,
no combat, no monsters, no dark horror mood, no photorealistic 3D render,
no side-view platformer perspective.
```

---

## 6. M1.5 체크리스트에 넣을 기준

`docs/milestones/M1.5-checklist.md`에는 다음 검수 항목을 넣는다.

```md
## 공식/검증 레퍼런스 반영
- [ ] 기획 문서 구조가 Unity Learn의 간단 GDD 구조를 기준으로 한다.
- [ ] 플레이 감각이 MDA 관점에서 Mechanics/Dynamics/Aesthetics로 연결된다.
- [ ] 아트 문서가 Unity Learn Art & Visuals 기준인 inspiration/concept art/unifying colors를 반영한다.
- [ ] 2D 시점과 아트 스타일 기준이 Unity Manual의 2D game/art style 문서와 충돌하지 않는다.
- [ ] 이미지 프롬프트 문서가 OpenAI Image Generation 및 GPT Image prompting guide의 명시적 제약/반복 검수 방식을 반영한다.
- [ ] 문서 요구사항이 NASA식 검수 기준에 맞게 명확하고, 일관되고, 확인 가능하다.
```

---

## 7. Codex에게 줄 수 있는 짧은 지시문

```md
M1.5 작업 시 `docs/references/planning-art-official-guide-references.md`를 먼저 읽어라.
이 단계는 무거운 GDD나 art bible을 만드는 단계가 아니다.
목표는 M2 Scene 구성 전에 Tiny Garden Restore의 경량 Creative Spec, Art Concept, Image Prompt 기준을 고정하는 것이다.
Unity Scene, Assets/, gameplay code는 수정하지 마라.
문서 요구사항은 눈으로 검수 가능하거나 M2~M5 구현 기준으로 사용할 수 있어야 한다.
공식/검증 레퍼런스는 Unity Learn, Unity Manual, OpenAI Image Generation/Prompt Guidance, NASA requirement checklist, MDA framework를 우선한다.
```

---

## 8. 레퍼런스 URL 목록

### Unity / Game Design

- Unity Learn — Create a Game Design Document  
  https://learn.unity.com/pathway/game-development/unit/planning-a-game/tutorial/game-dev-create-a-game-design-document

- Unity Learn — Game Design  
  https://learn.unity.com/pathway/game-development/unit/planning-a-game/tutorial/game-design

- Unity Learn — Fill out a Game Design Document  
  https://learn.unity.com/tutorial/fill-out-a-game-design-document

### Unity / 2D Art & Scene

- Unity Manual — Creating a 2D game  
  https://docs.unity3d.com/2022.3/Documentation/Manual/Quickstart2DCreate.html

- Unity Manual — Art styles for 2D games  
  https://docs.unity3d.com/2023.2/Documentation/Manual/Quickstart2DArt.html

- Unity Manual — Sprite texture import settings  
  https://docs.unity3d.com/6000.0/Documentation/Manual/texture-type-sprite.html

### OpenAI / Image & Prompting

- OpenAI API Docs — Image generation  
  https://developers.openai.com/api/docs/guides/image-generation

- OpenAI Cookbook — GPT Image Generation Models Prompting Guide  
  https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide

- OpenAI API Docs — Prompt guidance  
  https://developers.openai.com/api/docs/guides/prompt-guidance

- OpenAI API Docs — Using GPT-5.5  
  https://developers.openai.com/api/docs/guides/latest-model

### Requirements / Verification

- NASA — Appendix C: How to Write a Good Requirement  
  https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/

- NASA — Technical Requirements Definition  
  https://www.nasa.gov/reference/4-2-technical-requirements-definition/

### Game Design Framework

- AAAI — MDA: A Formal Approach to Game Design and Game Research  
  https://aaai.org/papers/ws04-04-001-mda-a-formal-approach-to-game-design-and-game-research/
