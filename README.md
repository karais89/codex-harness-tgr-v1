# Tiny Garden Restore

Tiny Garden Restore는 Codex Harness v1을 검증하기 위한 작은 Unity 2D 복구 게임 실험입니다.

이 저장소의 중심 산출물은 큰 게임이나 완성 콘텐츠가 아니라, Codex가 문서 읽기, 사용자 인터뷰, ExecPlan 작성, 구현 승인, Unity 구현, 수동/자동 검증, 다음 세션 인수인계를 반복 가능한 흐름으로 수행할 수 있는지 확인하는 기록입니다.

## 현재 상태

현재 단계: Bootstrap & Harness Reuse Check

현재 이 저장소는 Unity 프로젝트와 Git 저장소를 기준으로 최소 Codex 하네스를 초기화한 단계입니다. Gameplay 구현은 아직 시작하지 않았습니다.

## 실행 방법

1. Unity 6000.4.6f1에서 저장소 루트 폴더를 엽니다.
2. `Assets/Scenes/SampleScene.unity`를 엽니다.
3. Unity Editor Console에 project-load 또는 compile error가 없는지 확인합니다.

아직 player-facing gameplay는 승인되지 않았으므로 Play Mode 조작 방법은 별도 design 문서와 ExecPlan이 승인된 뒤에 작성합니다.

## 문서 구조

- `AGENTS.md`: Codex가 이 저장소에서 따라야 하는 작업 규칙입니다.
- `PLANS.md`: ExecPlan 작성, 승인, 검증, 완료 기준입니다.
- `docs/current-state.md`: 현재 프로젝트 상태와 활성 계획입니다.
- `docs/decisions.md`: 오래 유지할 프로젝트 결정입니다.
- `docs/design/`: 승인된 player-facing design 기준과 작성 규약입니다.
- `exec-plans/`: 각 사소하지 않은 작업의 자기완결적 실행 계획과 결과입니다.

## 초기 성공 기준

- Unity 프로젝트가 정상적으로 열립니다.
- GitHub remote가 연결되어 있습니다.
- 최소 Codex 하네스 문서가 존재합니다.
- `docs/design/core-beliefs.md`는 `상태: 작성 전`으로 시작합니다.
- Codex가 사용자 인터뷰와 승인 없이 gameplay 규칙이나 구현을 시작하지 않습니다.

## 아직 포함하지 않는 것

- 새 gameplay 기능
- Unity 씬 변경
- C# gameplay 코드
- 승인되지 않은 player-facing design 문서
- Unity MCP
- custom skills
- hooks
- subagents
- external packages 추가
- 플레이 영상 또는 GIF
