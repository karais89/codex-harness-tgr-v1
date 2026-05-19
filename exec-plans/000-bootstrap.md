# Bootstrap 단계 검증

## 목적

이 ExecPlan은 `codex-harness-tgr-v1`의 bootstrap 단계 상태를 검증한다.

bootstrap 단계의 목적은 Unity 프로젝트가 존재하고, GitHub remote가 연결되어 있으며, 최소 Codex 하네스 문서가 존재하고 사용할 수 있는지 확인하는 것이다.

최소 하네스는 다음 파일로 구성된다.

- `README.md`
- `AGENTS.md`
- `PLANS.md`
- `docs/current-state.md`
- `docs/decisions.md`
- `docs/design/README.md`
- `docs/design/core-beliefs.md`
- `exec-plans/000-bootstrap.md`

이 계획은 gameplay 구현 계획이 아니다. 이 계획은 Unity 씬, C# gameplay 코드, gameplay 규칙, 새 패키지, MCP, custom skill, hook, subagent, architecture 확장, game specification을 추가하지 않는다.

## 진행 상황

- 상태: 완료
- [x] Unity 프로젝트가 존재한다.
- [x] Unity 6000.4.6f1에서 프로젝트가 열린다.
- [x] Git 저장소가 존재한다.
- [x] GitHub `origin` remote가 `https://github.com/karais89/codex-harness-tgr-v1.git`를 가리킨다.
- [x] `README.md`가 존재하고 저장소 목적, 현재 단계, 제외 범위를 설명한다.
- [x] `AGENTS.md`가 존재하고 Codex 작업 규칙, 읽기 순서, 문서 갱신 규칙, 완료 기준을 설명한다.
- [x] `PLANS.md`가 존재하고 ExecPlan 규칙, 필수 섹션, living document 기대치, 검증 규칙을 설명한다.
- [x] `docs/current-state.md`가 존재하고 현재 단계, 활성 계획, 다음 단계를 설명한다.
- [x] `docs/decisions.md`가 존재하고 오래 유지할 프로젝트 결정을 기록한다.
- [x] `docs/design/README.md`가 존재한다.
- [x] `docs/design/core-beliefs.md`가 `상태: 작성 전` placeholder로 존재한다.
- [x] `exec-plans/000-bootstrap.md`가 표준 bootstrap 단계 검증 계획으로 존재한다.
- [x] `git status`가 clean이거나 남은 변경이 명확히 기록되어 있다.
- [x] bootstrap 중 gameplay 구현, Unity 씬 변경, 새 패키지, MCP, custom skill, hook, subagent를 추가하지 않았다.

## 맥락

Repository: `codex-harness-tgr-v1`

Project name: `Tiny Garden Restore`

Unity version: `6000.4.6f1`

GitHub remote: `https://github.com/karais89/codex-harness-tgr-v1.git`

Current stage: `Bootstrap & Harness Reuse Check`

이 저장소는 최소 Codex 하네스를 새 Unity 프로젝트에 적용하는 단계다. Bootstrap 검증이 끝나기 전에는 gameplay 구현을 시작하지 않는다.

## 계획

1. 필수 문서가 존재하는지 확인한다.
2. `docs/current-state.md`가 현재 단계와 활성 계획을 정확히 가리키는지 확인한다.
3. `docs/decisions.md`에 장기 하네스 결정이 기록되어 있는지 확인한다.
4. `docs/design/core-beliefs.md`가 `상태: 작성 전` placeholder인지 확인한다.
5. Unity 프로젝트가 열리는지 확인한다.
6. GitHub `origin` remote와 worktree 상태를 확인한다.
7. bootstrap 범위에서 벗어난 변경이 없는지 확인한다.
8. 검증 결과에 따라 `진행 상황`, `예상 밖 발견`, `회고`를 갱신한다.
9. 프로젝트 상태가 바뀌면 `docs/current-state.md`를 갱신한다.

## 검증

터미널에서 다음을 확인한다.

```bash
git remote -v
git status --short
test -f README.md
test -f AGENTS.md
test -f PLANS.md
test -f docs/current-state.md
test -f docs/decisions.md
test -f docs/design/README.md
test -f docs/design/core-beliefs.md
test -f exec-plans/000-bootstrap.md
```

Unity Editor에서 다음을 확인한다.

1. Unity 6000.4.6f1에서 저장소 루트 폴더를 연다.
2. `Assets/Scenes/SampleScene.unity`가 열린다.
3. Console에 project-load 또는 compile error가 없다.
4. 검증 중 gameplay 구현, 씬 수정, 패키지 추가를 하지 않는다.

bootstrap 단계 검증은 다음이 모두 참일 때 통과한다.

- Unity 프로젝트가 정상적으로 열린다.
- GitHub remote가 연결되어 있다.
- 최소 하네스 문서가 모두 존재한다.
- `docs/design/core-beliefs.md`는 `상태: 작성 전`으로 남아 있다.
- `git status`가 clean이거나 남은 변경이 명확히 기록되어 있다.
- bootstrap 중 gameplay 구현이나 하네스 확장을 하지 않았다.

현재 터미널 검증 결과:

- 날짜: 2026-05-19
- 필수 하네스 파일 8개와 `.gitignore`가 프로젝트 루트에 존재한다.
- 루트 하네스 문서에 template placeholder가 남아 있지 않다.
- 루트 하네스 문서에 원본 프로젝트 전용 문구가 남아 있지 않다.
- `docs/design/core-beliefs.md`는 `상태: 작성 전`이다.
- GitHub `origin` remote는 `https://github.com/karais89/codex-harness-tgr-v1.git`이다.
- `Assets/`, `Packages/`, `ProjectSettings/`에는 변경이 없다.
- 현재 남은 하네스 변경은 루트 하네스 문서 추가, `docs/design/` 추가, `exec-plans/` 추가, `.gitignore` 갱신이다.
- 별도 untracked 파일 `docs/project-goal.html`이 존재한다. 이 파일은 template 적용 필수 파일이 아니며, 커밋 범위에 포함할지 별도로 결정해야 한다.
- Unity batchmode project-load 검증은 같은 프로젝트가 이미 Unity Editor에서 열려 있어 중단됐다.
- `/Users/kaya/Library/Logs/Unity/Editor.log`에는 `codex-harness-tgr-v1` 프로젝트 로드, package listing, `Mono: successfully reloaded assembly`, `CompileScripts` 기록이 있다.
- 같은 `Editor.log`에 초기 ShaderGraph `error CS0246` 두 줄이 있으나, 직후 API Updater가 PackageCache 파일을 갱신했고 이후 assembly reload가 성공했다. 현재 bootstrap 하네스 문서 적용과 직접 관련된 오류로 보지는 않는다.
- `Editor.log`에는 Unity cloud host DNS 실패 로그가 반복되지만, 네트워크/Unity 서비스 연결 로그이며 로컬 하네스 문서 적용 실패로 보지는 않는다.
- 사용자가 Unity Editor에서 프로젝트가 열리는 것을 수동으로 확인했다.
- 별도 untracked 폴더 `output/`이 존재한다. 이 폴더는 template 적용 필수 파일이 아니며, 커밋 범위에 포함할지 별도로 결정해야 한다.

## 결정 기록

- 결정:
  `exec-plans/000-bootstrap.md`를 표준 bootstrap 단계 검증 계획으로 사용한다.
- 근거:
  첫 gameplay 작업 전에 Unity 프로젝트, GitHub 연결, 최소 문서 하네스, design placeholder, worktree 상태를 확인할 안정적인 기준 계획이 필요하다.
- 날짜:
  2026-05-19

- 결정:
  이 계획은 bootstrap 검증만 다루고 gameplay 구현을 포함하지 않는다.
- 근거:
  첫 gameplay 작업은 bootstrap 검증과 승인된 design 기준이 생긴 뒤 별도 ExecPlan에서 다뤄야 한다.
- 날짜:
  2026-05-19

## 예상 밖 발견

- Unity batchmode는 프로젝트가 이미 다른 Unity 인스턴스에서 열려 있어 독립 검증을 완료하지 못했다.
- `docs/project-goal.html`이 별도 untracked 파일로 존재한다. 이 파일은 template 적용 필수 파일이 아니다.
- `output/`이 별도 untracked 폴더로 존재한다. 이 폴더는 template 적용 필수 파일이 아니다.

## 회고

완료한 것:

- 최소 Codex 하네스 문서를 프로젝트 루트에 적용했다.
- TGR placeholder 값을 실제 프로젝트 값으로 치환했다.
- Unity 프로젝트, Git 저장소, GitHub remote, 필수 하네스 파일, design placeholder 상태를 확인했다.
- 사용자의 수동 확인으로 Unity Editor project-load 검증을 완료했다.
- bootstrap 중 gameplay 구현, Unity 씬 변경, 새 패키지, MCP, custom skill, hook, subagent를 추가하지 않았다.

완료하지 못한 것:

- 같은 프로젝트가 이미 Unity Editor에서 열려 있어 독립 Unity batchmode 검증은 완료하지 못했다.
- `docs/project-goal.html`과 `output/`을 커밋 범위에 포함할지는 아직 결정하지 않았다.

배운 것:

- `exec-plans/000-bootstrap.md`는 실행 파일이 아니라 bootstrap 검증 계획과 결과 기록이다.
- Unity 실행 검증은 생성물과 Editor 상태에 영향을 줄 수 있으므로 사용자 명시 승인 없이 batchmode로 대체하지 않는다.

다음에 해야 할 것:

- 커밋 범위를 정한다.
- bootstrap 변경을 커밋한 뒤 `docs/design/core-beliefs.md` 작성을 위한 사용자 인터뷰를 시작한다.

다음 계획을 시작할 준비:

- 커밋 범위가 정리되면 Core Beliefs 인터뷰를 시작할 준비가 되어 있다.
