# project-goal.md

## 프로젝트 이름

codex-harness-tgr-v1

## 게임 이름

Tiny Garden Restore

## 한 줄 정의

작은 정원을 복구하는 Unity 2D playable loop를 만들면서, Karpathy Guidelines 기반 `AGENTS.md`, Codex 기본 Plan mode, OpenAI ExecPlan 원문 참조, Unity MCP만으로 개발이 가능한지 검증하는 경량 하네스 실험 프로젝트입니다.

## 프로젝트 목적

이 프로젝트는 더 복잡한 하네스를 만드는 것이 목적이 아닙니다.

이 프로젝트는 `codex-harness-dbz-v0` 하네스의 확장판이 아니라, 작은 Unity playable loop에 필요한 최소 하네스 구성을 찾기 위한 경량화 실험입니다.

목적은 Tiny Garden Restore의 작은 playable loop를 실제로 만들면서, 최소한의 하네스 구성으로 Codex가 작업을 계획하고, 구현하고, 검증할 수 있는지 확인하는 것입니다.

## 게임 기본 방향

Tiny Garden Restore는 방치된 작은 정원을 조금씩 복구하는 2D 게임입니다.

초기 playable loop는 다음 요소만 다룹니다.

- 작은 정원 Scene
- 플레이어 이동
- 복구 대상
- 플레이어와 복구 대상의 상호작용
- 복구 상태 변화
- 모든 필수 복구 대상 처리 시 완료 표시

초기 단계에서는 다음을 만들지 않습니다.

- 복잡한 성장 시스템
- 인벤토리
- 상점
- 여러 스테이지
- 세이브/로드
- 복잡한 UI
- 장기 진행 경제
- 고급 아트 파이프라인

## 1차 검증 대상

1차 검증 대상은 다음입니다.

1. `AGENTS.md`
2. Codex 기본 Plan mode
3. Unity MCP
4. ExecPlan 원문 참조 파일
5. 3줄 이하의 짧은 작업 프롬프트

## 1차 검증 대상이 아닌 것

다음 항목은 1차 playable loop가 완료된 뒤에만 보조 실험으로 검토합니다.

- Skill
- Hooks
- Superpowers
- gstack
- grill-me
- subagent
- 복잡한 project memory 문서
- 큰 design gate

Memory는 이번 프로젝트의 명시적 실험 대상에서 제외합니다.  
이미 Codex에서 켜져 있고, 효과를 독립적으로 측정하기 어렵기 때문입니다.

즉, 이번 프로젝트의 우선순위는 다음과 같습니다.

```text
1. Tiny Garden Restore의 작은 Unity playable loop 완성
2. 경량 하네스가 충분했는지 평가
3. 필요하면 Skill / Hooks를 보조 실험으로 확인
```

## 기본 전제

- `AGENTS.md`는 Karpathy Guidelines를 기본으로 사용합니다.
- 프로젝트에서 새로 작성하는 문서와 작업 보고는 한글로 작성합니다.
- OpenAI ExecPlan 문서는 원문을 보존한 참조 파일로 추가합니다.
- 작업은 Codex 기본 Plan mode에서 시작합니다.
- Unity 작업 검증에는 CoplayDev Unity MCP를 사용합니다.
- 작은 작업은 별도의 ExecPlan 없이 진행합니다.
- 복잡한 기능, 큰 리팩터링, 여러 세션에 걸친 작업이 필요할 때만 ExecPlan 원문 파일을 참조합니다.

## 실험 범위

초기 범위는 Tiny Garden Restore의 작은 Unity 2D playable loop입니다.

게임 자체는 복잡하지 않아야 합니다.  
중요한 것은 게임의 완성도가 아니라 Codex가 가벼운 하네스 안에서 Unity 작업을 계획하고, 구현하고, 검증할 수 있는지 확인하는 것입니다.

## 실험하지 않는 것

초기 단계에서는 다음을 검증하지 않습니다.

- 상용 수준 게임 구조
- 복잡한 Clean Architecture
- 긴 PRD / GDD workflow
- 여러 agent 협업
- 대규모 자동화
- 고급 테스트 파이프라인
- Superpowers / gstack / grill-me 기반 workflow

## 전체 마일스톤

```text
M0. 기준 문서 정리
M1. Unity MCP 연결 확인
M2. Tiny Garden 기본 Scene 구성
M3. Player 이동 구현
M4. 복구 대상 상호작용 구현
M5. 첫 playable loop 완성
M6. 경량 하네스 평가
M7. 선택 실험: Skill / Hooks 검토
```

---

# M0. 기준 문서 정리

## 목표

Codex가 읽을 최소 기준 파일을 준비합니다.

## 완료 기준

- `README.md`가 존재합니다.
- `AGENTS.md`가 존재합니다.
- `docs/project-goal.md`가 존재합니다.
- `.agent/PLANS.md`가 존재합니다.
- 프로젝트 목적이 “경량 하네스로 Tiny Garden Restore의 작은 Unity playable loop를 만든다”로 설명되어 있습니다.
- 불필요한 workflow 문서가 기본값으로 추가되지 않습니다.

## 예상 작업 흐름

1. README와 docs/project-goal을 작성합니다.
2. AGENTS.md를 준비합니다.
3. ExecPlan 원문 참조 파일을 추가합니다.
4. Unity 프로젝트 기본 상태를 확인합니다.

## 예상 프롬프트

```text
이 저장소를 Tiny Garden Restore 경량 Codex 하네스 실험용으로 정리해줘.
README.md, docs/project-goal.md, AGENTS.md, .agent/PLANS.md 기준으로 점검해줘.
변경 전 plan을 먼저 제시해줘.
```

---

# M1. Unity MCP 연결 확인

## 목표

Codex가 Unity MCP를 통해 Unity Editor 상태를 확인할 수 있는지 검증합니다.

## 완료 기준

- Unity 프로젝트가 열립니다.
- Unity MCP 연결 상태를 확인합니다.
- 현재 Scene 정보를 읽을 수 있습니다.
- Console error를 확인할 수 있습니다.
- Play Mode 실행 가능 여부를 확인합니다.

## 예상 작업 흐름

1. Unity 프로젝트를 엽니다.
2. Unity MCP 연결 상태를 확인합니다.
3. 현재 Scene 정보를 읽습니다.
4. Console 상태를 확인합니다.
5. Play Mode 실행 가능 여부를 확인합니다.

## 예상 프롬프트

```text
Unity MCP 연결 상태를 확인해줘.
현재 Scene, Console error, Play Mode 실행 가능 여부를 점검해줘.
수정하지 말고 확인 결과만 보고해줘.
```

---

# M2. Tiny Garden 기본 Scene 구성

## 목표

Tiny Garden Restore의 첫 playable loop를 위한 아주 작은 정원 Scene을 구성합니다.

## 완료 기준

- 작은 정원으로 보이는 기본 Scene이 준비됩니다.
- Player 역할의 오브젝트가 존재합니다.
- 복구 대상을 배치할 수 있는 공간이 있습니다.
- 오브젝트 이름이 명확합니다.
- Unity에서 변경 사항을 확인할 수 있습니다.

## 예상 작업 흐름

1. 현재 Scene을 확인합니다.
2. 작은 정원 영역을 표현할 기본 오브젝트를 배치합니다.
3. Player 오브젝트를 생성합니다.
4. 카메라가 정원 영역을 볼 수 있게 조정합니다.
5. Unity에서 변경 결과를 확인합니다.

## 예상 프롬프트

```text
Tiny Garden Restore의 기본 정원 Scene을 만들어줘.
Player와 작은 정원 영역만 가장 단순하게 배치해줘.
변경 후 Unity에서 확인한 내용을 보고해줘.
```

---

# M3. Player 이동 구현

## 목표

작은 정원 안에서 Player가 움직일 수 있게 합니다.

## 완료 기준

- Player 오브젝트가 존재합니다.
- Player에 이동 스크립트가 연결됩니다.
- 키보드 입력으로 이동할 수 있습니다.
- Play Mode에서 동작을 확인합니다.
- Console error가 없습니다.

## 예상 작업 흐름

1. Player 오브젝트 구조를 확인합니다.
2. 이동 스크립트를 작성합니다.
3. Player에 스크립트를 연결합니다.
4. Play Mode에서 이동을 확인합니다.
5. Console error를 확인합니다.

## 예상 프롬프트

```text
Player가 작은 정원 안에서 키보드 입력으로 움직이게 해줘.
가장 단순한 Unity 기본 방식으로 구현해줘.
Play Mode 검증 결과와 Console 상태를 보고해줘.
```

---

# M4. 복구 대상 상호작용 구현

## 목표

Player가 정원 안의 복구 대상과 상호작용할 수 있게 합니다.

복구 대상은 초기에는 가장 단순한 오브젝트로 표현합니다.  
예를 들어 방치된 풀, 시든 식물, 더러워진 타일, 망가진 장식물처럼 “복구 전 상태”를 나타내는 오브젝트가 될 수 있습니다.

구체 표현은 구현 과정에서 가장 단순한 방식으로 정합니다.

## 완료 기준

- 복구 대상 오브젝트가 존재합니다.
- Player가 복구 대상과 상호작용할 수 있습니다.
- 상호작용 후 복구 대상의 상태가 바뀝니다.
- 상태 변화가 Scene에서 확인됩니다.
- Play Mode에서 확인 가능합니다.
- Console error가 없습니다.

## 예상 작업 흐름

1. 복구 대상 오브젝트를 하나 생성합니다.
2. Player와 복구 대상의 충돌 또는 거리 조건을 구현합니다.
3. 상호작용 입력 또는 접촉 방식 중 가장 단순한 방식을 선택합니다.
4. 복구 전/후 상태 변화를 구현합니다.
5. Play Mode에서 동작을 확인합니다.
6. Console error를 확인합니다.

## 예상 프롬프트

```text
Player가 정원 안의 복구 대상과 상호작용하면 상태가 바뀌게 해줘.
가장 단순한 충돌 또는 입력 방식으로 구현해줘.
Play Mode에서 확인하고 결과를 보고해줘.
```

---

# M5. 첫 playable loop 완성

## 목표

Tiny Garden Restore의 아주 작은 게임 루프를 완성합니다.

예상 loop:

1. Player가 작은 정원에서 시작합니다.
2. Player가 이동합니다.
3. Player가 여러 복구 대상과 상호작용합니다.
4. 각 복구 대상의 상태가 복구됨으로 바뀝니다.
5. 모든 필수 복구 대상이 처리되면 완료 메시지가 표시됩니다.

## 완료 기준

- 시작 상태가 있습니다.
- 플레이어 행동이 있습니다.
- 복구 대상이 여러 개 있습니다.
- 복구 완료 조건이 있습니다.
- 완료 결과가 표시됩니다.
- Unity Play Mode에서 처음부터 끝까지 확인 가능합니다.
- Console error가 없습니다.

## 예상 작업 흐름

1. 복구 대상 오브젝트를 여러 개 배치합니다.
2. 복구 상태를 관리합니다.
3. 모든 필수 복구 대상이 처리되면 완료 상태를 표시합니다.
4. Play Mode에서 전체 루프를 확인합니다.
5. Console error를 확인합니다.

## 예상 프롬프트

```text
복구 대상 3개를 모두 처리하면 완료 메시지가 나오게 해줘.
Tiny Garden Restore의 작은 playable loop로 끝까지 동작하게 만들어줘.
Play Mode 검증 결과를 보고해줘.
```

---

# M6. 경량 하네스 평가

## 목표

M0~M5까지의 작업을 기준으로 경량 하네스가 충분했는지 평가합니다.

## 완료 기준

다음 항목을 각각 평가합니다.

- `AGENTS.md`
- Codex 기본 Plan mode
- ExecPlan 원문 참조
- Unity MCP
- 3줄 이하 작업 프롬프트
- 한글 문서/보고 규칙

## 평가 기준

각 항목에 대해 다음을 판단합니다.

- 실제로 사용했는가?
- 언제 도움이 되었는가?
- 오히려 복잡도를 늘렸는가?
- 다음 프로젝트에서도 유지할 것인가?
- 보강이 필요한가?

## 예상 작업 흐름

1. M0~M5 작업 결과를 검토합니다.
2. 막힌 지점을 정리합니다.
3. 현재 하네스가 충분했던 점을 정리합니다.
4. 부족했던 점을 정리합니다.
5. Skill / Hooks가 필요한지 판단합니다.

## 예상 프롬프트

```text
M0~M5 작업을 기준으로 경량 하네스가 충분했는지 평가해줘.
AGENTS.md, Plan mode, ExecPlan, Unity MCP 관점으로 나눠줘.
Skill과 Hooks가 지금 필요한지도 판단해줘.
```

---

# M7. 선택 실험: Skill / Hooks 검토

## 목표

1차 playable loop 완료 후, 필요성이 확인된 항목만 가볍게 실험합니다.

이 단계는 필수가 아닙니다.  
M6 평가 결과에 따라 진행 여부를 결정합니다.

## 선택 실험 후보

### Skill

반복되는 Unity 검증 작업이 생겼다면 작은 skill 하나로 분리합니다.

예상 용도:

- Console error 확인
- Player 이동 확인
- 복구 대상 상호작용 확인
- 완료 메시지 확인
- 검증하지 못한 항목 보고

예상 프롬프트:

```text
Tiny Garden Restore Play Mode 검증용 작은 skill을 하나 만들어줘.
Console, Player 이동, 복구 상호작용, 완료 메시지만 확인하게 해줘.
작성 후 실제 검증에 한 번 사용해줘.
```

### Hooks

C# 파일 변경 후 반복되는 기계적 검사를 자동화할 수 있는지 확인합니다.

예상 용도:

- 변경 파일 목록 확인
- C# formatting check
- lint 또는 analyzer warning 확인
- 테스트 명령 안내

주의:

- 처음부터 자동 수정하지 않습니다.
- warning을 자동 제거하지 않습니다.
- 먼저 보고만 하고, 수정은 별도 작업으로 진행합니다.

예상 프롬프트:

```text
C# 변경 후 format/lint 상태를 확인하는 작은 hook을 만들어줘.
처음에는 자동 수정하지 말고, 변경 파일과 검사 결과만 보고하게 해줘.
한 번 실행해서 결과를 알려줘.
```

## 완료 기준

- M6 평가에서 필요성이 확인된 항목만 진행합니다.
- 각 실험은 작게 진행합니다.
- 실험 결과가 다음 프로젝트 판단에 도움이 되어야 합니다.
- playable loop 개선보다 하네스 설정이 커지면 중단합니다.

---

# 작업 프롬프트 원칙

프롬프트는 짧게 작성합니다.

좋은 프롬프트의 기준:

- 3줄 이하
- 한 번에 하나의 목표
- 구현 전 plan 요청
- 검증 결과 보고 요청
- 불필요한 구조화 금지

## 기본 프롬프트 형식

```text
[작업 목표]를 해줘.
가장 단순한 방식으로 구현하고, 변경 전 plan을 먼저 제시해줘.
작업 후 변경 파일과 Unity 검증 결과를 보고해줘.
```

## 확인 작업 프롬프트 예시

```text
현재 Unity 프로젝트 상태를 점검해줘.
Scene, Console error, Play Mode 가능 여부만 확인해줘.
파일은 수정하지 말고 결과만 보고해줘.
```

## 구현 작업 프롬프트 예시

```text
Player 이동을 구현해줘.
가장 단순한 Unity 기본 방식으로 작성하고, 변경 전 plan을 먼저 제시해줘.
Play Mode 검증 결과와 Console 상태를 보고해줘.
```

## 검증 작업 프롬프트 예시

```text
현재 playable loop가 끝까지 동작하는지 확인해줘.
Player 이동, 복구 상호작용, 완료 메시지를 기준으로 봐줘.
Console error와 확인하지 못한 부분도 보고해줘.
```

## 평가 작업 프롬프트 예시

```text
이번 작업에서 하네스가 충분했는지 평가해줘.
AGENTS.md, Plan mode, Unity MCP 관점으로 나눠줘.
부족했던 점만 짧게 정리해줘.
```

---

# 실험 기록 방식

초기에는 별도의 무거운 진행 문서를 만들지 않습니다.

대신 각 작업이 끝날 때 Codex의 완료 보고에 다음 항목이 포함되도록 합니다.

- 변경한 파일
- 구현한 동작
- 검증한 내용
- 검증하지 못한 내용
- 다음 작업 제안

필요성이 확인되면 이후에만 별도의 진행 기록 문서를 추가합니다.

---

# 최종 판단 기준

M6까지 완료한 뒤 다음 질문에 답할 수 있으면 1차 실험은 성공입니다.

1. `AGENTS.md`는 저장소 기본 규칙으로 충분했는가?
2. Codex 기본 Plan mode는 작은 Unity 작업에 충분했는가?
3. Unity MCP는 실제 구현과 검증에 도움이 되었는가?
4. ExecPlan 없이도 Tiny Garden Restore의 작은 playable loop를 만들 수 있었는가?
5. 3줄 이하 프롬프트로도 작업 지시가 가능했는가?
6. Superpowers, gstack, grill-me 없이도 충분했는가?
7. Skill / Hooks는 지금 필요한가, 아니면 다음 프로젝트로 미뤄도 되는가?
8. 다음 프로젝트에서 어떤 하네스 구성을 유지해야 하는가?
