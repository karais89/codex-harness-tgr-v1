# 결정 사항

## 2026-05-19

### 접두어 기반 실험 이름을 사용한다

결정:
`codex-harness-tgr-v1`를 GitHub 저장소 이름과 Unity 프로젝트 폴더 이름으로 사용한다.

근거:
접두어를 사용하면 실험 유형이 먼저 보이며, 여러 실험 저장소를 쉽게 훑어볼 수 있다.

### 최소 Codex 하네스로 시작한다

결정:
`README.md`, `AGENTS.md`, `PLANS.md`, `docs/current-state.md`, `docs/decisions.md`, `docs/design/README.md`, `docs/design/core-beliefs.md`, `exec-plans/000-bootstrap.md`를 최소 Codex 하네스로 사용한다.

근거:
초기 bootstrap 단계는 작게 유지해야 한다. MCP, 사용자 정의 skill, hook, subagent는 실제 워크플로우 마찰이 생길 때까지 보류한다.

### 상태 문서와 결정 문서를 AGENTS와 PLANS를 통해 관리한다

결정:
`docs/current-state.md`와 `docs/decisions.md`를 워크플로우 문서로 취급하며, `AGENTS.md`와 `PLANS.md`의 읽기 및 업데이트 규칙에 연결한다.

근거:
상태 문서와 결정 문서는 Codex가 언제 읽고 언제 업데이트해야 하는지 알고 있을 때만 신뢰할 수 있다.

### 계획 내부 결정과 장기 프로젝트 결정을 분리한다

결정:
각 ExecPlan의 `결정 기록`에는 해당 계획 안에서 내려진 선택을 기록하고, 단일 계획을 넘어 유지되어야 하는 결정은 `docs/decisions.md`에 기록한다.

근거:
이 방식은 임시 실행 맥락과 장기 프로젝트 규칙을 분리한다.

### 000-bootstrap을 표준 bootstrap 검증 계획으로 사용한다

결정:
`exec-plans/000-bootstrap.md`를 표준 bootstrap 단계 검증 ExecPlan으로 사용한다.

근거:
첫 gameplay 작업을 시작하기 전에 Unity 프로젝트 생성, GitHub 연결, 최소 Codex 하네스 준비 상태를 확인할 안정적인 기준 계획이 bootstrap 단계에 하나 있어야 한다.

### 모든 저장소 문서는 한글로 작성한다

결정:
저장소에 작성하거나 갱신하는 모든 문서는 한글로 작성한다.

근거:
프로젝트 문서 언어를 한글로 통일하면 상태, 결정, 계획을 더 일관되게 읽고 유지할 수 있다.

### 사소하지 않은 작업은 인터뷰와 공유된 이해 검증을 먼저 수행한다

결정:
게임플레이, Unity 씬, 워크플로우, 구조 변경 같은 사소하지 않은 작업은 `grill-me` 방식 인터뷰와 공유된 이해 검증을 거친 뒤 ExecPlan 생성 여부를 확인한다.

근거:
사용자가 처음부터 완성된 프롬프트를 작성하지 않아도 Codex가 중요한 결정 분기를 질문으로 끌어내고, 구현 전에 같은 작업을 상상하고 있는지 확인할 수 있어야 한다.

### ExecPlan 생성 승인과 구현 승인을 분리한다

결정:
사소하지 않은 작업은 ExecPlan 생성 승인과 구현 승인 게이트를 분리한다. 새 ExecPlan은 기본적으로 `구현 승인 대기` 상태로 시작하고, Codex 자체 리뷰와 사용자 검토용 요약 뒤 구현 승인을 확인한다.

근거:
계획 작성에 동의한 것과 구현 시작에 동의한 것은 다르다. 두 단계를 분리해야 범위가 조용히 확장되거나 사용자가 검토하기 전에 구현이 시작되는 문제를 줄일 수 있다.

### `docs/design`은 승인된 design 기준 폴더로 사용한다

결정:
`docs/design`은 단계 계획 문서 폴더가 아니라 승인된 플레이어 경험과 게임 규칙 기준 문서 폴더로 사용한다.

근거:
단계 계획은 언제 구현할 것인지를 다루고, design 문서는 무엇을 만들 것인지와 어떤 player-facing 규칙을 지킬 것인지를 다룬다.

### Gameplay ExecPlan은 승인된 design 기준 없이는 만들지 않는다

결정:
Player-facing gameplay ExecPlan은 승인된 `docs/design/core-beliefs.md`와 해당 작업의 플레이어 경험 또는 게임 규칙을 정의하는 승인된 design 문서 최소 1개 없이는 작성하지 않는다.

근거:
`core-beliefs.md`는 프로젝트 방향 기준일 뿐이다. 실제 gameplay ExecPlan은 Codex가 새 player-facing 규칙을 발명하지 않도록 작업별 승인 design 문서를 함께 참조해야 한다.

### 하네스 확장은 보류한다

결정:
초기 bootstrap 단계와 첫 gameplay 검증 전까지 hooks, MCP, custom skills, subagents 같은 하네스 확장을 하지 않는다. 단, 실제 실패가 반복되어 진행이 막힐 때만 하네스 보강을 검토한다.

근거:
이 프로젝트의 초기 목적은 최소 Codex 하네스로 Unity 개발 워크플로우가 작동하는지 확인하는 것이다. 하네스 확장을 먼저 늘리면 gameplay 루프 검증보다 도구 구조가 먼저 복잡해질 수 있다.

### creative, art, design 문서 역할을 분리한다

결정:
`docs/creative`는 아이디어 발산, 후보 압축, 기획 초안 도출을 위한 작업장으로 사용한다. `docs/art`는 아트 방향, 이미지 프롬프트, 생성 이미지 기록을 위한 공간으로 사용한다. `docs/design`은 기존처럼 구현 기준으로 삼을 수 있는 승인된 player-facing design 사양을 보관한다.

근거:
기획과 아트 탐색 결과를 곧바로 구현 사양으로 취급하면 Codex가 아이디어, 레퍼런스, 승인된 규칙을 섞을 수 있다. 세 폴더의 역할을 분리해야 실제 협업처럼 발산, 시각 탐색, 사양 확정, 구현 계획을 반복할 수 있다.

### creative/art 영향은 엄격 모드로 라우팅한다

결정:
creative, art, design, ExecPlan 중 어디에 속하는지 애매한 요청은 Codex가 파일을 수정하지 않고 먼저 사용자에게 질문한다.

근거:
이 프로젝트의 목적은 빠른 구현보다 Codex가 기획, 아트, design, 개발 경계를 흐리지 않고 협업 흐름을 유지할 수 있는지 검증하는 것이다. 애매한 변경을 조용히 design 또는 implementation으로 넘기지 않아야 한다.

### 생성 이미지는 검토 가치가 있는 것만 저장한다

결정:
`docs/art/images/`에는 채택 또는 검토 가치가 있는 이미지만 저장한다. 실패작, 반복 생성물, 단순 실험 이미지는 기본 저장 대상이 아니다. 저장한 이미지는 `docs/art/03-generated-results.md`에 파일명, 프롬프트, 채택/보류/폐기 이유를 기록한다.

근거:
생성 이미지를 모두 저장하면 `docs/art/images/`가 추적 불가능한 덤프 폴더가 된다. 남긴 이미지마다 왜 남겼는지 기록해야 이후 art direction, design, Unity asset 사용 여부를 판단할 수 있다.

### 생성 이미지는 별도 승인 전 Unity 에셋이 아니다

결정:
생성 이미지는 `docs/art`에 기록된 art 후보 또는 참고 자료일 뿐이며, 실제 Unity 에셋으로 사용하려면 별도 design 또는 ExecPlan 승인 절차를 거친다.

근거:
이미지가 마음에 든다는 판단과 player-facing 화면 기준 또는 Unity asset 사용 승인은 다르다. 이 경계를 분리해야 이미지 생성 결과가 조용히 구현 기준으로 승격되는 문제를 줄일 수 있다.

### `grill-me`를 공통 discovery protocol로 사용한다

결정:
creative, art, design, ExecPlan 작업에서 공통으로 사용할 인터뷰 프로토콜은 `docs/workflows/grill-me.md`에 둔다.

근거:
각 영역 문서에 인터뷰 규칙을 따로 복사하면 질문 방식, 승인 기준, 종료 조건이 쉽게 어긋난다. 공통 프로토콜을 두면 Codex가 아이디어, 아트, design, 실행 계획을 모두 공유된 이해에 도달할 때까지 같은 방식으로 캐물을 수 있다.

### `grill-me`는 `mattpocock/skills` 기준으로 유지한다

결정:
공통 discovery protocol의 기준은 `mattpocock/skills`의 `grill-me`로 삼는다. `deep-interview`는 이번 프로토콜의 기준으로 채택하지 않는다. 로컬 문서는 원문 기준과 Unity 하네스 검증을 위한 로컬 확장을 구분해 기록한다.

근거:
이 프로젝트의 목적은 빠른 요구사항 정리가 아니라 pre-production 과정에서 암묵적 결정과 판단 기준을 충분히 캐내는 것이다. `deep-interview`식 절제된 요구사항 정리는 일반 작업에는 유용하지만, 이 하네스에서는 질문을 조기 종료할 위험이 있다. 다만 원문은 매우 짧은 행동 규칙이므로, 로컬 확장은 원문보다 강한 별도 출처처럼 보이지 않게 범위를 명시해야 한다.

### Grill-Me는 먼저 workflow 문서로 검증한다

결정:
이번 단계에서는 custom skill을 추가하지 않고, `docs/workflows/grill-me.md`를 repo-local workflow protocol로 사용한다.

근거:
현재 저장소는 MCP, custom skill, hook, subagent를 보류한다는 결정을 유지하고 있다. 실제 creative/art/design/ExecPlan 흐름에서 반복 사용해 본 뒤 skill 승격 여부를 판단하는 편이 안전하다.
