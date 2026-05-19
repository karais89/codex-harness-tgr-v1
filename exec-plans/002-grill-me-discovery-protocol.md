# Grill-Me Discovery Protocol 도입

## 목적

이 ExecPlan은 `codex-harness-tgr-v1`의 creative, art, design, ExecPlan 작업에 공통으로 적용할 `grill-me` 기반 인터뷰 프로토콜을 도입한다.

완료 후에는 Codex가 아이디어 발산, 아트 방향, player-facing design, 구현 계획을 바로 문서화하거나 구현하지 않고, 먼저 사용자와 decision tree를 끝까지 파고들어 공유된 이해를 만든 뒤 산출물로 넘길 수 있어야 한다.

이 계획은 custom skill을 추가하지 않는다. `mattpocock/skills`의 `grill-me` 원문 철학을 repo-local workflow 문서로 들여오고, 이 저장소의 creative/art/design/ExecPlan 문서가 그 공통 프로토콜을 참조하도록 연결한다.

이 계획은 gameplay 구현 계획이 아니다. Unity 씬, C# gameplay 코드, player-facing gameplay 규칙 확정, 실제 이미지 생성, 생성 이미지의 Unity 에셋 사용, MCP, custom skill, hook, subagent, 외부 패키지를 추가하지 않는다.

## 진행 상황

- 상태: 완료
- [x] 문제를 확인했다: creative/art 문서는 산출물 경계는 강하지만, 아이디어를 캐묻는 인터뷰 절차가 약하다.
- [x] 사용자와 `deep-interview` 대신 `grill-me`를 기준으로 삼는 방향을 합의했다.
- [x] 사용자에게 ExecPlan 생성 승인을 받았다.
- [x] 구현 승인을 받았다.
- [x] `docs/workflows/grill-me.md`를 추가했다.
- [x] `AGENTS.md`에 공통 프로토콜 필수 참조 규칙을 추가했다.
- [x] `PLANS.md`의 ExecPlan 전 인터뷰 규칙을 공통 프로토콜 참조로 정리했다.
- [x] `docs/creative/README.md`에 creative 작업의 `grill-me` 적용 규칙을 추가했다.
- [x] `docs/art/README.md`에 art 작업의 `grill-me` 적용 규칙을 추가했다.
- [x] `docs/design/README.md`에 design 작업의 `grill-me` 적용 규칙을 연결했다.
- [x] `docs/decisions.md`에 장기 결정 사항을 기록했다.
- [x] `docs/current-state.md`에 활성 계획과 다음 단계를 갱신했다.
- [x] 검증을 완료했다.
- [x] 회고를 작성했다.

## 맥락

Repository: `codex-harness-tgr-v1`

Project name: `Tiny Garden Restore`

Current stage: `Creative/Art Workflow Setup`

현재 저장소는 `docs/creative/`와 `docs/art/`의 기본 문서 구조를 갖고 있다. `exec-plans/001-creative-art-workflow.md`는 완료 상태다.

현재 `docs/creative/README.md`와 `docs/art/README.md`는 creative/art 산출물이 곧바로 design 기준이나 Unity 구현 기준이 되지 않는다고 잘 설명한다. 하지만 브레인스토밍, concept 후보 압축, art direction 탐색을 시작할 때 Codex가 반드시 사용자를 집요하게 인터뷰해야 한다는 강제력이 약하다.

현재 `docs/design/README.md`, `PLANS.md`, `AGENTS.md`에는 이미 인터뷰와 공유된 이해 검증 규칙이 일부 있다. 그러나 creative/art/design/ExecPlan마다 인터뷰 규칙을 복사해 적으면 문서 간 표현이 어긋날 수 있다. 따라서 공통 workflow 문서를 만들고 각 영역 문서가 이를 참조하는 구조가 필요하다.

기준으로 삼을 외부 자료는 다음이다.

- `mattpocock/skills`의 `grill-me` skill: https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md
- `mattpocock/skills` 라이선스: https://raw.githubusercontent.com/mattpocock/skills/main/LICENSE
- 비교 검토한 `deep-interview` skill: https://github.com/devbrother2024/skills/blob/main/deep-interview/SKILL.md

사용자와의 합의는 다음이다.

- `grill-me`를 기준으로 가져온다.
- `deep-interview`와 섞지 않는다.
- 질문이 많아져도 공유된 이해가 닫힐 때까지 묻는 방향이 이 프로젝트 목적에 맞다.
- 아직 custom skill은 추가하지 않고 repo-local 공통 프로토콜 문서로 둔다.

## 계획

1. `docs/workflows/grill-me.md`를 추가한다.
   - 이 문서는 custom skill이 아니라 repo-local workflow protocol임을 명시한다.
   - `grill-me` 원문 출처와 MIT 라이선스 고지를 적는다.
   - 원문 철학을 기준으로 다음 원칙을 문서화한다.
     - 계획이나 design에 대해 공유된 이해에 도달할 때까지 집요하게 인터뷰한다.
     - decision tree의 각 분기를 하나씩 해결한다.
     - 각 질문에는 Codex의 추천 답안을 포함한다.
     - 질문은 한 번에 하나만 한다.
     - 저장소 문서나 코드에서 답할 수 있는 질문은 사용자에게 묻지 않고 직접 확인한다.
   - 이 저장소의 적용 대상이 `creative`, `art`, `design`, `ExecPlan`임을 적는다.
   - 종료 조건은 Codex가 임의로 정하지 않는다. 중요한 decision branch가 남아 있으면 계속 묻고, 사용자의 명시 중단이나 공유된 이해 검증 후 다음 승인 질문으로 넘어간다.

2. `AGENTS.md`를 갱신한다.
   - `먼저 읽기`에 `docs/workflows/grill-me.md`를 추가한다.
   - creative, art, design, ExecPlan 작업은 해당 영역 README와 함께 공통 `grill-me` 프로토콜을 읽도록 한다.
   - 분석/검토 요청은 여전히 파일 변경 없이 처리한다는 기존 규칙을 유지한다.
   - custom skill을 추가하지 않는다는 기존 제한을 유지한다.

3. `PLANS.md`를 갱신한다.
   - ExecPlan 전 인터뷰와 생성 게이트가 `docs/workflows/grill-me.md`를 기준으로 한다고 연결한다.
   - ExecPlan 생성 전 인터뷰는 효율적으로 조기 종료하는 절차가 아니라, decision tree가 닫힐 때까지 공유 이해를 만드는 절차임을 명확히 한다.
   - 기존 ExecPlan 생성 승인과 구현 승인 분리는 유지한다.

4. `docs/creative/README.md`를 갱신한다.
   - creative 작업은 단순 기록 요청이 아닌 한 `grill-me` 인터뷰로 시작한다고 명시한다.
   - 브레인스토밍 전에 프로젝트 정체성, 플레이어 감정, 하지 않을 것, 후보 선택 기준 같은 decision branch를 질문으로 캐내도록 한다.
   - `01-brainstorming.md`, `02-concept-candidates.md`, `03-concept-brief.md`로 넘어가는 조건을 공통 프로토콜과 연결한다.
   - creative 결과가 design 기준이 되려면 별도 design 절차가 필요하다는 기존 경계를 유지한다.

5. `docs/art/README.md`를 갱신한다.
   - art 작업은 단순 이미지 기록 요청이 아닌 한 `grill-me` 인터뷰로 시작한다고 명시한다.
   - 분위기, 색감, 형태 언어, 피할 방향, 이미지 저장 여부, Unity 에셋 사용 여부를 decision branch로 분리한다.
   - 생성 이미지나 프롬프트가 곧바로 Unity 에셋 승인이나 gameplay 기준이 되지 않는다는 기존 경계를 유지한다.

6. `docs/design/README.md`를 갱신한다.
   - Core Beliefs와 조건부 design 문서 작성 전 인터뷰가 공통 `grill-me` 프로토콜을 따른다고 연결한다.
   - `상태: 작성 전`, `상태: 초안`, `상태: 승인됨` 게이트는 변경하지 않는다.
   - design 문서가 player-facing 기준이므로 creative/art보다 더 엄격하게 공유된 이해 검증을 거친다고 명시한다.

7. `docs/decisions.md`를 갱신한다.
   - `grill-me`를 공통 discovery protocol 기준으로 채택한다는 장기 결정을 기록한다.
   - `deep-interview`는 이번 프로토콜의 기준으로 채택하지 않는다고 기록한다.
   - custom skill이 아니라 repo-local workflow 문서로 먼저 검증한다는 결정을 기록한다.

8. `docs/current-state.md`를 갱신한다.
   - 활성 계획을 이 ExecPlan으로 바꾼다.
   - 현재 상태가 `Grill-Me Discovery Protocol Setup`임을 기록한다.
   - 다음 단계가 구현 승인 후 공통 프로토콜 문서와 참조 연결 적용임을 적는다.
   - gameplay design 승인, gameplay 구현, 이미지 생성, custom skill 추가는 아직 하지 않았다고 유지한다.

9. 문서 간 표현을 점검한다.
   - `grill-me` 프로토콜이 `deep-interview`식 절제된 요구사항 정리로 바뀌지 않았는지 확인한다.
   - creative/art/design/ExecPlan 문서가 서로 다른 인터뷰 규칙을 따로 발명하지 않는지 확인한다.
   - custom skill을 실제로 추가하지 않았는지 확인한다.
   - `docs/design/core-beliefs.md` 상태를 변경하지 않았는지 확인한다.

10. 검증 결과와 회고를 이 ExecPlan에 기록한다.

## 구현 결과

다음 문서를 추가했다.

- `docs/workflows/grill-me.md`: `mattpocock/skills`의 `grill-me`를 기준으로 삼는 repo-local discovery protocol이다. custom skill이 아니며, 출처와 MIT 라이선스 고지를 포함한다.

다음 문서를 갱신했다.

- `AGENTS.md`: creative, art, design, ExecPlan 작업 시 `docs/workflows/grill-me.md`를 먼저 읽고, 단순 기록 요청이 아닌 한 공통 protocol을 따르도록 연결했다.
- `PLANS.md`: ExecPlan 전 인터뷰가 `docs/workflows/grill-me.md`를 기준으로 하며, decision tree가 닫힐 때까지 공유 이해를 만드는 절차라고 명시했다.
- `docs/creative/README.md`: creative 작업을 passive 기록이 아니라 `grill-me` 기반 discovery로 시작하도록 했다.
- `docs/art/README.md`: art 작업을 이미지 생성이나 프롬프트 확정보다 먼저 `grill-me` 기반 방향 탐색으로 시작하도록 했다.
- `docs/design/README.md`: Core Beliefs와 조건부 design 문서 작성 전 인터뷰가 공통 protocol을 따르도록 연결했다.
- `docs/decisions.md`: `grill-me` 채택, `deep-interview` 비채택, custom skill 대신 workflow 문서로 먼저 검증한다는 결정을 기록했다.
- `docs/current-state.md`: 활성 계획과 다음 단계를 `exec-plans/002-grill-me-discovery-protocol.md` 기준으로 갱신했다.

Unity 씬, C# gameplay 코드, 실제 이미지 생성, 생성 이미지의 Unity 에셋 사용, MCP, custom skill, hook, subagent, 외부 패키지는 추가하지 않았다.

## 검증

터미널에서 다음을 확인한다.

```bash
test -f docs/workflows/grill-me.md
rg -n "grill-me|Grill-Me|docs/workflows/grill-me.md" AGENTS.md PLANS.md docs/current-state.md docs/decisions.md docs/creative/README.md docs/art/README.md docs/design/README.md docs/workflows/grill-me.md
rg -n "deep-interview" docs/workflows/grill-me.md docs/decisions.md
rg -n "custom skill|사용자 정의 skill" AGENTS.md docs/current-state.md docs/decisions.md docs/workflows/grill-me.md
rg -n "상태: 작성 전" docs/design/core-beliefs.md
find . -path "./.git" -prune -o -path "./.agents/skills/*" -print
git diff --check
git status --short
```

수동으로 다음을 확인한다.

1. `docs/workflows/grill-me.md`는 custom skill 설치 문서가 아니라 repo-local workflow protocol이다.
2. `docs/workflows/grill-me.md`는 `mattpocock/skills`의 `grill-me`를 기준으로 삼고 출처와 MIT 라이선스를 기록한다.
3. `docs/workflows/grill-me.md`는 `deep-interview`와 섞지 않는다.
4. `docs/creative/README.md`는 creative 작업을 passive 기록이 아니라 인터뷰 기반 discovery로 다룬다.
5. `docs/art/README.md`는 art 작업을 이미지 생성 요청 처리보다 먼저 인터뷰 기반 방향 탐색으로 다룬다.
6. `docs/design/README.md`와 `PLANS.md`의 기존 승인 게이트가 약해지지 않는다.
7. 실제 custom skill, hook, MCP, subagent, external package가 추가되지 않았다.
8. Unity 씬, C# gameplay 코드, 이미지 파일이 변경되지 않았다.

이 계획은 다음이 모두 참일 때 완료한다.

- 공통 `grill-me` protocol 문서가 존재한다.
- creative/art/design/ExecPlan 문서가 공통 protocol을 참조한다.
- `grill-me` 원문 출처와 MIT 라이선스 고지가 기록되어 있다.
- `deep-interview`는 이번 기준으로 채택하지 않았다는 결정이 기록되어 있다.
- custom skill은 추가하지 않았다.
- design baseline 상태는 변경하지 않았다.
- 검증 절차와 결과가 이 ExecPlan에 기록되어 있다.
- commit 후 `git status`가 clean이다.

현재 검증 결과:

- 날짜: 2026-05-19
- `test -f docs/workflows/grill-me.md`로 공통 protocol 문서 존재를 확인했다.
- `rg -n "grill-me|Grill-Me|docs/workflows/grill-me.md" AGENTS.md PLANS.md docs/current-state.md docs/decisions.md docs/creative/README.md docs/art/README.md docs/design/README.md docs/workflows/grill-me.md`로 각 문서의 참조 연결을 확인했다.
- `rg -n "deep-interview" docs/workflows/grill-me.md docs/decisions.md`로 `deep-interview`가 기준으로 채택되지 않았다는 기록만 존재함을 확인했다.
- `rg -n "custom skill|사용자 정의 skill" AGENTS.md docs/current-state.md docs/decisions.md docs/workflows/grill-me.md`로 custom skill 보류와 미추가 방침을 확인했다.
- `rg -n "상태: 작성 전" docs/design/core-beliefs.md`로 design baseline이 승인 상태로 바뀌지 않았음을 확인했다.
- `find . -path "./.git" -prune -o -path "./.agents/skills/*" -print`는 출력이 없어 custom skill 파일이 추가되지 않았음을 확인했다.
- `git diff --check`는 출력 없이 통과했다.
- `git status --short`는 커밋 전 예상 문서 변경만 표시했다.

## 결정 기록

- 결정:
  `grill-me`를 공통 discovery protocol의 기준으로 삼는다.
- 근거:
  이 프로젝트의 목적은 빠르게 요구사항을 정리하는 것이 아니라, creative/art/design/ExecPlan 과정에서 암묵적 결정과 판단 기준을 끝까지 캐내 공유된 이해를 만드는 것이다.
- 날짜:
  2026-05-19

- 결정:
  `deep-interview`는 이번 프로토콜의 기준으로 채택하지 않는다.
- 근거:
  `deep-interview`의 절제된 요구사항 정리 방식은 일반 작업에는 유용하지만, 이번 하네스의 pre-production discovery 목적에는 질문을 조기 종료할 위험이 있다.
- 날짜:
  2026-05-19

- 결정:
  이번 단계에서는 custom skill을 추가하지 않고 repo-local workflow 문서로 검증한다.
- 근거:
  현재 저장소 결정은 MCP, custom skill, hook, subagent를 보류하는 것이다. 실제 반복 사용으로 공통 프로토콜이 안정된 뒤 skill 승격을 검토하는 편이 기존 제약과 맞다.
- 날짜:
  2026-05-19

## 예상 밖 발견

- 없음.

## 회고

완료한 것:

- `grill-me`를 creative/art/design/ExecPlan 공통 discovery protocol로 연결했다.
- `deep-interview`와 섞지 않는다는 결정을 문서화했다.
- custom skill 추가 없이 repo-local workflow 문서로 먼저 검증하는 경로를 만들었다.
- creative와 art 작업이 단순 placeholder 작성이 아니라 질문 기반 discovery로 시작하도록 보강했다.

완료하지 않은 것:

- 실제 custom skill을 만들지 않았다.
- gameplay 설계, gameplay ExecPlan, Unity 씬 변경, C# gameplay 구현은 하지 않았다.
- 실제 이미지를 생성하거나 `docs/art/images/`에 이미지 파일을 추가하지 않았다.
- `docs/design/core-beliefs.md`는 여전히 `상태: 작성 전`이다.

배운 것:

- creative/art/design/ExecPlan 각각에 인터뷰 규칙을 복사하는 방식은 장기적으로 드리프트 위험이 크다.
- 이 저장소의 discovery 목적에는 절제된 요구사항 정리보다 `grill-me`식 decision tree 탐색이 더 적합하다.

다음에 해야 할 것:

- 다음 creative 세션에서 `docs/workflows/grill-me.md`와 `docs/creative/README.md`를 읽고, 한 번에 하나씩 질문하며 브레인스토밍을 시작한다.

다음 계획을 시작할 준비:

- 준비됨.
