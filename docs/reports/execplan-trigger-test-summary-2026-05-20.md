# ExecPlan Trigger 테스트 요약 (2026-05-20)

## 목적

이번 테스트의 목적은 복합 Unity 작업에서 ExecPlan이 실제 실행 절차와 검증 기록을 통제하는 데 도움이 되는지 확인하는 것이었다. 테스트는 의도적으로 M2부터 M5까지를 한 번에 묶어 실행했다. 범위는 Tiny Garden Restore의 첫 작은 playable loop였다.

최종 보존 대상은 구현물이 아니라 테스트 회고 보고서다. Unity Scene 변경, 런타임 스크립트, Editor 검증 스크립트, M2-M5 체크리스트 수정, 임시 ExecPlan은 모두 실험 산출물로 보고 main에는 남기지 않는다.

## 진행 요약

1. Preflight에서 작업 전 Git 상태가 clean임을 확인했다.
2. M1/M1.5 완료 상태를 문서로 재확인했다.
3. Unity Editor 6000.4.6f1 프로젝트 로드와 `localhost:8090` MCP WebSocket 서버 시작을 확인했다.
4. 임시 ExecPlan `exec-plans/001-m2-m5-first-playable-loop.md`를 작성했다.
5. `Assets/Scenes/SampleScene.unity`에 작은 top-down 정원, Player, `WeedTarget`, `WiltedFlowerTarget`, `DirtyTileTarget`, 완료 UI를 생성했다.
6. `PlayerMover2D`, `PlayerInteractor`, `RestorableTarget`, `GardenRestorationManager`를 추가해 이동, 상호작용, 복구 상태, 완료 조건을 구현했다.
7. Editor 메뉴 기반 builder와 Play Mode verifier를 추가해 Scene 구성과 playable loop를 자동 확인했다.
8. Game view에서 시각 출력 문제를 발견했다. Unity 내장 UI sprite가 placeholder 사각형처럼 보이지 않고 의미 없는 UI skin 이미지처럼 출력되어, `Assets/Generated/SolidSquare.png` 기반 SpriteRenderer와 짧은 라벨로 수정했다.
9. M2-M5 체크리스트에 완료 증거를 기록했지만, 이 체크리스트 변경은 실험 결과이므로 main에는 남기지 않기로 했다.

## 검증 결과

- Play Mode verifier token: `20260520T104338078Z`
- Unity Console error: `0개`
- 활성 Scene: `Assets/Scenes/SampleScene.unity`
- 주요 확인 흐름: Player 이동, 세 복구 대상 복구, `Garden Restored` 완료 텍스트 표시
- Game view 캡처: `/private/tmp/tgr-m2m5-game-view.png`

자동 검증은 실제 물리 키보드 이벤트를 주입하지 않았다. verifier는 런타임 입력이 호출하는 public method인 `PlayerMover2D.MoveBy`와 `PlayerInteractor.TryInteract`를 직접 호출해 같은 동작 경로의 핵심 로직을 확인했다. 따라서 결과는 playable loop 로직 검증으로는 유효하지만, 실제 조작감 검증으로 보기는 어렵다.

## 판단

ExecPlan은 절차와 증거 기록에는 유효했다. 진행 중 발견 사항, 결정 이유, 검증 token, Console 상태, 화면 캡처 위치가 한 문서에 남아 작업 추적이 쉬웠다. 특히 Unity MCP 연결, Play Mode 검증 실패 원인, 시각 출력 문제 같은 중간 발견을 누락하지 않는 데 도움이 됐다.

다만 M2-M5를 한 번에 묶으니 완료 판정이 로직 중심으로 기울었다. 자동 verifier가 통과한 뒤에야 Game view 판독성 문제가 드러났고, "게임처럼 보이는가", "사용자가 한 화면에서 즉시 이해할 수 있는가" 같은 기준은 늦게 확인됐다.

## 문제점

- 단계별 시각 검증이 늦었다. M2의 한 화면 정원 구성 단계에서 바로 screenshot 판독을 했어야 했다.
- Play Mode 자동 검증과 실제 사용자 조작 검증이 분리되어 있지 않았다.
- M2-M5 체크리스트를 한 번에 완료 처리하면서 각 milestone의 품질 기준이 약해졌다.
- 화면 출력 문제가 "구현 완료 후 수정"으로 밀려, 완료 판정의 신뢰도가 낮아질 수 있었다.

## 다음 프로젝트에 반영할 교훈

- 각 milestone gate마다 screenshot 또는 Game view 캡처를 남기고 사람이 판독한다.
- 완료 판정 전에 사용자 관점의 화면 리뷰를 별도 기준으로 둔다.
- 자동 verifier는 로직 검증으로 제한하고, 실제 입력/조작감 검증은 따로 기록한다.
- 여러 milestone을 한 ExecPlan에 묶더라도 완료 판정은 milestone별로 끊어야 한다.
- 첫 playable loop에서는 "동작한다"와 "게임처럼 읽힌다"를 다른 검증 항목으로 관리한다.

## 정리 방침

이 테스트의 구현 변경은 main에 병합하지 않는다. main에는 이 보고서만 남긴다. 로컬 `test/execplan-trigger` 브랜치는 보고서 커밋 후 삭제한다. 원격 test 브랜치는 확인되지 않았으므로 삭제하지 않는다.
