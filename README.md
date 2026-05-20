# Tiny Garden Restore

Tiny Garden Restore는 작은 정원을 복구하는 Unity 2D 게임입니다.

이 저장소의 1차 목적은 큰 게임을 완성하는 것이 아니라, 아주 작은 정원 복구 playable loop를 만들면서 Codex 경량 하네스가 실제 Unity 개발에 충분한지 검증하는 것입니다.

이 프로젝트는 `codex-harness-dbz-v0`의 하네스를 더 강하게 만드는 프로젝트가 아닙니다.  
오히려 v0에서 확인한 문서/계획 중심 흐름을 줄이고, 더 가벼운 구성으로도 Unity 작업이 가능한지 확인합니다.

## 프로젝트 목적

이 저장소의 1차 목적은 다음 조합으로 Tiny Garden Restore의 첫 playable loop를 만드는 것입니다.

- Karpathy Guidelines 기반 `AGENTS.md`
- Codex 기본 Plan mode
- OpenAI ExecPlan 원문 참조 파일
- CoderGamester Unity MCP (`com.gamelovers.mcp-unity`)
- 최소한의 프로젝트 문서

이 프로젝트의 핵심은 하네스 구성요소를 많이 넣는 것이 아닙니다.  
먼저 작은 게임 루프를 실제로 완성하고, 그 과정에서 현재 구성이 충분한지 확인하는 것입니다.

## 게임 방향

Tiny Garden Restore는 방치된 작은 정원을 조금씩 복구하는 2D 게임입니다.

초기 playable loop는 다음 감각을 목표로 합니다.

- 플레이어는 작은 정원 안에서 움직입니다.
- 정원에는 `잡초`, `시든 꽃`, `더러운 타일` 복구 대상이 존재합니다.
- 플레이어는 대상 근처에서 `E`를 눌러 정원을 조금씩 복구합니다.
- 세 복구 대상을 모두 처리하면 하루 또는 스테이지가 완료됩니다.
- 게임은 작고 명확해야 하며, 처음부터 복잡한 성장/경제/스테이지 시스템을 만들지 않습니다.

## M1.5 Creative Gate

M1.5는 M1 Unity MCP 연결 확인과 M2 Scene 구성 사이의 필수 게이트입니다.

이 단계는 무거운 GDD나 ExecPlan이 아닙니다.
M2~M5 구현자가 임의로 게임 방향을 다시 해석하지 않도록, 최소 기획/아트 기준만 문서로 고정합니다.

M1.5 확정값은 다음입니다.

- 시점: `top-down`
- Player: 작은 정원사
- 복구 대상: `잡초`, `시든 꽃`, `더러운 타일`
- 상호작용: 대상 근처에서 `E`
- 컨셉 이미지는 구현용 에셋이 아니라 참고용

## 1차 playable loop 예시

구체 규칙은 M1.5 확정값을 따르되, 구현 방식만 가장 단순하게 정합니다.

예상 loop는 다음과 같습니다.

1. 플레이어가 작은 정원 Scene에서 시작합니다.
2. 플레이어가 이동합니다.
3. 플레이어가 `잡초`, `시든 꽃`, `더러운 타일` 근처에서 `E`로 상호작용합니다.
4. 복구 대상의 상태가 바뀝니다.
5. 세 복구 대상이 모두 처리되면 완료 메시지가 표시됩니다.

이 루프는 예시이지만 복구 대상과 상호작용 방식은 M1.5 확정값을 따릅니다.

## 핵심 실험 질문

이 프로젝트는 다음 질문에 답하기 위해 진행합니다.

1. `AGENTS.md` 중심의 얇은 지침만으로 Codex가 Unity 작업을 진행할 수 있는가?
2. Codex 기본 Plan mode만으로 작은 작업 계획과 구현 흐름이 충분한가?
3. Unity MCP를 통해 Unity Editor 작업과 검증 흐름을 실제로 연결할 수 있는가?
4. ExecPlan은 기본값이 아니라 복잡한 작업에서만 참조해도 충분한가?
5. Superpowers, gstack, grill-me 같은 큰 workflow skill 없이도 작은 playable loop를 만들 수 있는가?

## 이번 프로젝트에서 우선하지 않는 것

이번 프로젝트는 Codex 하네스의 모든 구성요소를 처음부터 검증하는 프로젝트가 아닙니다.

초기 실험에서는 다음을 기본값으로 사용하지 않습니다.

- Superpowers
- gstack
- grill-me
- custom skill
- hooks
- subagent
- 별도 memory 문서
- 과도한 design gate
- 모든 작업에 대한 ExecPlan 강제

단, 1차 playable loop가 완료된 뒤 필요성이 있거나 비교 가치가 있으면 다음 항목을 보조 실험으로 가볍게 확인할 수 있습니다.

- Skill
- Hooks

Memory는 이번 프로젝트의 명시적 실험 대상에서 제외합니다.  
이미 Codex에서 켜져 있고, 효과를 독립적으로 측정하기 어렵기 때문입니다.

## 기본 구성

초기 기준 파일은 다음과 같습니다.

```text
.
├── README.md
├── AGENTS.md
├── docs/project-goal.md
├── .agent/
│   └── PLANS.md
├── Assets/
├── Packages/
└── ProjectSettings/
```

## 주요 파일 역할

### `README.md`

프로젝트의 목적, 게임 방향, 전체 실험 방향을 설명합니다.

외부 사람이 이 저장소를 봤을 때, 이 프로젝트가 단순한 Unity 게임 프로젝트가 아니라 Codex 경량 하네스 검증 프로젝트라는 것을 이해할 수 있어야 합니다.

### `AGENTS.md`

Codex가 이 저장소에서 따라야 할 기본 작업 지침입니다.

기본 내용은 Karpathy Guidelines를 사용합니다.  
추가로 이 프로젝트에서 새로 작성하는 문서와 작업 보고는 한글로 작성한다는 지침을 둡니다.

### `.agent/PLANS.md`

OpenAI Codex ExecPlan 문서의 원문 참조 파일입니다.

이 파일은 모든 작업에 사용하는 기본 절차가 아닙니다.  
복잡한 기능, 큰 리팩터링, 여러 세션에 걸친 작업이 필요할 때 참조합니다.

### `docs/project-goal.md`

이 프로젝트의 마일스톤, 작업 흐름, 예상 프롬프트, 평가 기준을 정리한 문서입니다.

이 문서는 상세 게임 기획서가 아니라 경량 하네스 실험 기준표입니다.

## 기본 작업 방식

작업은 Codex 기본 Plan mode에서 시작합니다.

기본 흐름은 다음과 같습니다.

1. 사용자가 3줄 이하의 짧은 작업 프롬프트를 작성합니다.
2. Codex가 Plan mode에서 작업 계획을 제안합니다.
3. 사용자가 계획을 확인합니다.
4. Codex가 구현합니다.
5. Unity MCP 또는 Unity Editor에서 검증합니다.
6. Codex가 변경 파일, 검증 결과, 남은 위험을 보고합니다.

작은 작업은 별도의 ExecPlan 없이 진행합니다.  
복잡한 기능, 큰 리팩터링, 여러 세션에 걸친 작업이 필요할 때만 `.agent/PLANS.md`를 참조합니다.

## Unity MCP

이 프로젝트는 Unity 작업 검증을 위해 `CoderGamester/mcp-unity`를 기본 MCP로 사용합니다.

선정 근거와 후보 비교는 `docs/unity-mcp-comparison-2026-05-20.md`에 기록합니다. 현재 Unity 패키지는 `Packages/manifest.json`에서 `com.gamelovers.mcp-unity`를 특정 커밋으로 고정합니다.

Unity MCP를 통해 다음을 확인합니다.

- Unity Editor와 Codex 연결 가능 여부
- Unity Console log 조회와 log 왕복 전송 가능 여부
- Unity package / asset 리소스 조회 가능 여부
- Scene / GameObject / Play Mode 확인이 MCP로 가능한지 여부
- MCP가 직접 제공하지 않는 확인 항목을 Unity Editor 검증으로 보완할 수 있는지 여부

M1의 첫 smoke test는 파괴적 작업 없이 `get_console_logs`, `unity://packages`, `unity://assets`, `send_console_log` 순서로 진행합니다. 기본 연결은 `localhost:8090`을 사용하고 원격 연결은 켜지 않습니다.

## 문서 작성 규칙

이 프로젝트에서 새로 작성하는 문서와 작업 보고는 한글로 작성합니다.

단, 외부 원문을 보존하기 위해 추가한 참조 파일은 원문 언어를 유지할 수 있습니다.

## 1차 성공 기준

이 프로젝트는 다음 조건을 만족하면 1차 성공으로 봅니다.

- Codex가 `AGENTS.md`를 기반으로 작업 방향을 이해한다.
- Codex 기본 Plan mode로 작은 Unity 작업을 진행할 수 있다.
- Unity MCP를 통해 Unity 작업 또는 검증을 수행할 수 있다.
- Tiny Garden Restore의 작은 playable loop가 구현된다.
- 작업 완료 후 변경 파일, 구현 내용, 검증 결과가 보고된다.
- ExecPlan 없이도 작은 작업을 진행할 수 있는지 판단할 수 있다.
- Superpowers, gstack, grill-me 없이도 기본 개발 루프가 가능한지 판단할 수 있다.

## 1차 실패 기준

다음 상황이 반복되면 현재 구성이 부족하다고 판단합니다.

- Codex가 작은 작업도 진행하지 못하고 계속 멈춘다.
- Unity 작업보다 하네스 설정에 더 많은 시간이 든다.
- 작업보다 문서와 절차 관리가 더 커진다.
- Codex가 요청하지 않은 구조나 기능을 과도하게 추가한다.
- Tiny Garden Restore의 게임 방향과 다른 임의의 게임을 만든다.
- Unity에서 확인 가능한 결과물이 나오지 않는다.
- 다음 작업으로 이어가기 어려울 정도로 맥락이 사라진다.

## 1차 완료 후 선택 실험

1차 playable loop가 완료된 뒤, 필요성이 있으면 다음 항목을 보조 실험으로 확인합니다.

### Skill

반복되는 Unity 검증 루틴이 생겼을 때, 아주 작은 skill로 분리할 가치가 있는지 확인합니다.

예시:

- `unity-playmode-check`
- `unity-console-check`

Skill은 게임 개발 전체 workflow가 아니라, 반복되는 작은 검증 절차만 대상으로 합니다.

### Hooks

C# 파일 변경 후 반복되는 기계적 검사를 자동화할 수 있는지 확인합니다.

예시:

- 변경 파일 목록 확인
- C# formatting check
- lint 또는 analyzer warning 확인
- 테스트 명령 안내

처음부터 자동 수정하지 않습니다.  
먼저 검사와 보고만 수행하고, 수정은 별도 작업으로 진행합니다.

## 최종 산출물

이 프로젝트의 최종 산출물은 다음입니다.

1. Tiny Garden Restore의 작은 Unity playable loop
2. 경량 하네스 사용 결과
3. Codex Plan mode와 Unity MCP의 실전 사용 평가
4. ExecPlan이 필요한 상황과 필요하지 않은 상황의 구분
5. Skill / Hooks를 다음 프로젝트에서 도입할지에 대한 판단
6. Superpowers, gstack, grill-me 같은 큰 workflow skill 도입 여부 판단
