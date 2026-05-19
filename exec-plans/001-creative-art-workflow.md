# Creative/Art 워크플로우 도입

## 목적

이 ExecPlan은 `codex-harness-tgr-v1`에 creative, art, design, ExecPlan, implementation이 반복적으로 오갈 수 있는 문서 흐름을 도입한다.

완료 후에는 Codex가 기획 아이디어, 아트 방향, 이미지 프롬프트, 승인된 design 사양, 구현 계획을 한 폴더에 섞지 않고 구분해서 다룰 수 있어야 한다. 또한 요청이 creative/art/design/ExecPlan 중 어디에 속하는지 애매하면 파일을 수정하기 전에 사용자에게 먼저 질문하는 엄격 모드가 저장소 규칙으로 남아야 한다.

이 계획은 gameplay 구현 계획이 아니다. Unity 씬, C# gameplay 코드, player-facing gameplay 규칙, 실제 이미지 생성, 생성 이미지의 Unity 에셋 사용, MCP, custom skill, hook, subagent, 외부 패키지를 추가하지 않는다.

## 진행 상황

- 상태: 완료
- [x] 사용자와 creative/art/design 역할 분리를 논의했다.
- [x] 공유된 이해 검증을 완료했다.
- [x] ExecPlan 생성 승인을 받았다.
- [x] 구현 승인을 받았다.
- [x] `README.md`에 확장된 하네스 목표를 반영했다.
- [x] `AGENTS.md`에 엄격 모드 라우팅 규칙을 추가했다.
- [x] `docs/decisions.md`에 장기 결정 사항을 기록했다.
- [x] `docs/current-state.md`에 현재 단계와 활성 계획을 갱신했다.
- [x] `docs/creative/`의 README와 단계별 placeholder 문서를 추가했다.
- [x] `docs/art/`의 README, 단계별 placeholder 문서, 이미지 폴더 placeholder를 추가했다.
- [x] 검증을 완료했다.
- [x] 회고를 작성했다.

## 맥락

Repository: `codex-harness-tgr-v1`

Project name: `Tiny Garden Restore`

Current stage: `Bootstrap & Harness Reuse Check`

현재 저장소는 bootstrap 검증을 완료했고, `docs/design/core-beliefs.md`는 `상태: 작성 전`이다. 따라서 player-facing gameplay design, gameplay ExecPlan, gameplay 구현은 아직 시작할 수 없다.

사용자는 첫 번째 프로젝트에서 실제 게임 개발 협업처럼 기획, 아트, 개발 순서가 자연스럽게 이어지지 않았다고 판단했다. 이번 v1 하네스에서는 단순 구현 루프뿐 아니라 기획 논의, 아트 방향 탐색, 이미지 프롬프트와 생성 결과 기록, 승인된 design 기준, 구현 계획이 서로 구분되면서도 필요할 때 반복될 수 있는 흐름을 검증하려 한다.

합의된 문서 역할은 다음과 같다.

- `docs/creative/`: 아이디어 브레인스토밍, 후보 압축, 기획 초안 도출을 위한 작업장이다. 확정 구현 사양이 아니다.
- `docs/art/`: 아트 방향, 이미지 프롬프트, 생성 이미지 기록을 위한 공간이다. 생성 이미지는 곧바로 Unity 에셋 또는 gameplay 사양이 아니다.
- `docs/design/`: 기존처럼 구현 기준으로 삼을 수 있는 승인된 player-facing design 사양을 보관한다.
- `exec-plans/`: 승인된 design 또는 workflow 기준을 어떻게 구현하고 검증할지 설명한다.

`docs/project-goal.md`는 하네스 방향을 잡기 위해 임시로 둔 참고 문서이며, 이번 변경의 정식 운영 기준 문서로 갱신하지 않는다.

## 계획

1. `README.md`를 갱신한다.
   - TGR v1의 목표가 단순 Unity 구현이 아니라 creative/art/design/implementation 루프까지 포함한 Unity/Codex 하네스 검증임을 짧게 반영한다.
   - 아직 player-facing gameplay가 승인되지 않았다는 경계는 유지한다.

2. `AGENTS.md`를 갱신한다.
   - 모든 요청을 먼저 creative, art, design, ExecPlan, 단순 구현/문서 작업 중 하나로 분류하도록 규칙을 추가한다.
   - 분류나 영향 범위가 애매하면 파일을 수정하지 않고 사용자에게 질문하는 엄격 모드를 추가한다.
   - 기획 브레인스토밍이나 concept brief 작업 시 `docs/creative/README.md`를 먼저 읽도록 한다.
   - 아트 방향, 이미지 프롬프트, 생성 이미지 기록 작업 시 `docs/art/README.md`를 먼저 읽도록 한다.
   - creative/art 결과가 player-facing 규칙, 목표, 조작, 피드백, 화면 상태, 구현 기준을 바꾸면 `docs/design` 갱신 절차로 넘어가야 한다고 명시한다.

3. `docs/decisions.md`를 갱신한다.
   - creative/art/design 역할 분리 결정을 기록한다.
   - 엄격 모드 도입 결정을 기록한다.
   - 생성 이미지는 채택 또는 검토 가치가 있는 것만 저장하고, 실제 Unity 에셋 사용은 별도 design/ExecPlan 승인 대상이라는 결정을 기록한다.

4. `docs/creative/`를 추가한다.
   - `docs/creative/README.md`: creative 단계 규칙, 산출물 역할, design으로 넘어가는 조건을 설명한다.
   - `docs/creative/01-brainstorming.md`: 아이디어 발산 placeholder로 만든다.
   - `docs/creative/02-concept-candidates.md`: 후보 압축과 선택/보류/폐기 이유 placeholder로 만든다.
   - `docs/creative/03-concept-brief.md`: 현재 채택한 기획 초안 placeholder로 만든다.
   - 단계별 placeholder는 `상태: 작성 전`으로 시작한다.

5. `docs/art/`를 추가한다.
   - `docs/art/README.md`: art 단계 규칙, 이미지 프롬프트와 생성 결과 기록 규칙, Unity 에셋 사용 전 승인 조건을 설명한다.
   - `docs/art/01-art-direction.md`: 아트 방향 placeholder로 만든다.
   - `docs/art/02-image-prompts.md`: 이미지 생성 프롬프트 placeholder로 만든다.
   - `docs/art/03-generated-results.md`: 생성 결과, 파일명, 프롬프트, 채택/보류/폐기 이유 기록 placeholder로 만든다.
   - `docs/art/images/.gitkeep`: 이미지 폴더를 추적하기 위한 placeholder로 만든다.
   - 단계별 placeholder는 `상태: 작성 전`으로 시작한다.

6. `docs/current-state.md`를 갱신한다.
   - 활성 계획을 이 ExecPlan으로 바꾼다.
   - 다음 단계가 구현 승인 후 creative/art 워크플로우 문서 적용임을 적는다.
   - gameplay 구현과 이미지 생성은 아직 하지 않았다고 유지한다.

7. 문서 간 표현을 점검한다.
   - `docs/project-goal.md`를 정식 운영 기준으로 참조하지 않는지 확인한다.
   - creative/art 문서가 확정 design 기준처럼 쓰이지 않도록 표현을 점검한다.
   - `docs/design`의 기존 역할과 충돌하지 않도록 확인한다.

8. 검증 결과와 회고를 이 ExecPlan에 기록한다.

## 구현 결과

다음 문서를 갱신했다.

- `README.md`: TGR v1이 creative/art/design/ExecPlan/implementation 루프를 검증한다는 목표를 추가했다.
- `AGENTS.md`: creative/art 작업 시 읽을 문서와 엄격 모드 라우팅 규칙을 추가했다.
- `docs/decisions.md`: creative/art/design 역할 분리, 엄격 모드, 생성 이미지 저장 및 Unity 에셋 사용 승인 기준을 장기 결정으로 기록했다.
- `docs/current-state.md`: 현재 단계를 Creative/Art Workflow Setup으로 갱신하고 다음 단계를 정리했다.

다음 문서를 추가했다.

- `docs/creative/README.md`
- `docs/creative/01-brainstorming.md`
- `docs/creative/02-concept-candidates.md`
- `docs/creative/03-concept-brief.md`
- `docs/art/README.md`
- `docs/art/01-art-direction.md`
- `docs/art/02-image-prompts.md`
- `docs/art/03-generated-results.md`
- `docs/art/images/.gitkeep`

Unity 씬, C# gameplay 코드, 실제 이미지 생성, 생성 이미지의 Unity 에셋 사용, MCP, custom skill, hook, subagent, 외부 패키지는 추가하지 않았다.

## 검증

터미널에서 다음을 확인한다.

```bash
test -f README.md
test -f AGENTS.md
test -f docs/current-state.md
test -f docs/decisions.md
test -f docs/creative/README.md
test -f docs/creative/01-brainstorming.md
test -f docs/creative/02-concept-candidates.md
test -f docs/creative/03-concept-brief.md
test -f docs/art/README.md
test -f docs/art/01-art-direction.md
test -f docs/art/02-image-prompts.md
test -f docs/art/03-generated-results.md
test -f docs/art/images/.gitkeep
rg -n "엄격 모드|creative|art|docs/creative|docs/art" README.md AGENTS.md docs/current-state.md docs/decisions.md docs/creative docs/art
rg -n "상태: 작성 전" docs/creative docs/art
git status --short
```

수동으로 다음을 확인한다.

1. `README.md`는 프로젝트 목표를 과하게 확장하지 않고 creative/art/design/implementation 루프 검증만 추가로 설명한다.
2. `AGENTS.md`는 애매한 creative/art/design/ExecPlan 영향을 사용자에게 질문하도록 지시한다.
3. `docs/creative/README.md`는 creative 산출물이 확정 구현 사양이 아니라고 설명한다.
4. `docs/art/README.md`는 이미지 프롬프트와 생성 결과 기록 규칙을 설명하고, 생성 이미지가 곧바로 Unity 에셋이 아니라고 설명한다.
5. `docs/design/README.md`의 기존 design 기준 역할과 새 creative/art 문서 역할이 충돌하지 않는다.
6. `docs/project-goal.md`는 이번 변경의 정식 운영 기준으로 취급되지 않는다.

이 계획은 다음이 모두 참일 때 완료한다.

- 요청한 문서와 폴더가 존재한다.
- 엄격 모드 라우팅 규칙이 `AGENTS.md`에 기록되어 있다.
- creative/art/design 역할 분리가 `docs/decisions.md`와 각 README에 기록되어 있다.
- `docs/current-state.md`가 활성 계획과 다음 단계를 정확히 설명한다.
- 검증 절차와 결과가 이 ExecPlan에 기록되어 있다.
- commit 후 `git status`가 clean이다.

현재 검증 결과:

- 날짜: 2026-05-19
- `find docs/creative docs/art -maxdepth 3 -type f -print | sort`로 creative/art README, 단계별 placeholder 6개, `docs/art/images/.gitkeep` 존재를 확인했다.
- `rg -n "엄격 모드|creative|art|docs/creative|docs/art" README.md AGENTS.md docs/current-state.md docs/decisions.md docs/creative docs/art`로 목표, 라우팅 규칙, 결정 기록, 폴더 규칙 문구가 존재함을 확인했다.
- `rg -n "상태: 작성 전" docs/creative docs/art`로 creative/art 단계별 placeholder가 작성 전 상태임을 확인했다.
- `git diff --check`는 출력 없이 통과했다.
- `rg -n "project-goal" README.md AGENTS.md docs/current-state.md docs/decisions.md docs/creative docs/art`는 결과가 없어 `docs/project-goal.md`가 새 정식 운영 기준으로 참조되지 않음을 확인했다.
- `git status --short`는 커밋 전 예상 변경만 표시했다.

## 결정 기록

- 결정:
  `docs/project-goal.md`는 정식 운영 문서로 갱신하지 않는다.
- 근거:
  사용자가 이 파일은 하네스 방향을 잡기 위한 임시 문서라고 명시했다. 정식 기준은 `README.md`, `AGENTS.md`, `docs/current-state.md`, `docs/decisions.md`, 각 폴더 README에 나누는 편이 기준 문서 중복을 줄인다.
- 날짜:
  2026-05-19

- 결정:
  `docs/creative`는 단계별 문서로 구성한다.
- 근거:
  아이디어 발산, 후보 압축, 기획 초안을 한 문서에 섞으면 현재 채택된 방향과 폐기/보류 아이디어가 혼동될 수 있다.
- 날짜:
  2026-05-19

- 결정:
  `docs/art`는 아트 방향, 이미지 프롬프트, 생성 결과, 이미지 폴더를 분리한다.
- 근거:
  프롬프트와 생성 결과와 실제 이미지 파일을 분리해야 나중에 어떤 이미지가 왜 남았는지 추적할 수 있다.
- 날짜:
  2026-05-19

- 결정:
  creative/art/design/ExecPlan 영향이 애매하면 엄격 모드로 멈추고 질문한다.
- 근거:
  이 프로젝트의 목적은 빠른 구현보다 Codex가 기획, 아트, design, 개발 경계를 흐리지 않고 협업 흐름을 유지할 수 있는지 검증하는 것이다.
- 날짜:
  2026-05-19

## 예상 밖 발견

- 없음.

## 회고

완료한 것:

- creative/art/design 문서 역할을 분리했다.
- 엄격 모드 라우팅 규칙을 `AGENTS.md`에 추가했다.
- creative와 art 단계별 placeholder 문서를 추가했다.
- 생성 이미지는 검토 가치가 있는 것만 저장하고, Unity 에셋 사용은 별도 승인 대상으로 둔다는 기준을 기록했다.

완료하지 않은 것:

- gameplay 설계, gameplay ExecPlan, Unity 씬 변경, C# gameplay 구현은 하지 않았다.
- 실제 이미지를 생성하거나 `docs/art/images/`에 이미지 파일을 추가하지 않았다.
- `docs/design/core-beliefs.md`는 여전히 `상태: 작성 전`이다.

배운 것:

- 이 프로젝트의 pre-production 흐름은 선형 `기획 -> 아트 -> 개발`보다 요청별 라우팅과 영향도 판정이 핵심이다.
- creative/art 결과를 design 기준으로 넘기는 순간을 엄격하게 묻는 규칙이 있어야 Codex가 아이디어와 구현 사양을 섞지 않는다.

다음에 해야 할 것:

- 다음 세션에서 `docs/creative/README.md`를 읽고 `docs/creative/01-brainstorming.md`를 기준으로 creative 브레인스토밍을 시작할 수 있다.

다음 계획을 시작할 준비:

- 준비됨.
