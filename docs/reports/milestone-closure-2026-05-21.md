# 마일스톤 종료 선언 - 2026-05-21

## 종료 선언

Tiny Garden Restore v1 경량 Codex 하네스 실험의 1차 마일스톤을 종료합니다.

## 종료 판정

- 판정: 종료
- 범위: `M0`부터 `M7`까지의 1차 마일스톤
- 기준 문서: `docs/project-goal.md`
- 체크리스트 경로: `docs/milestones/`

## 판정 근거

- `M0` 기준 문서 정리: 완료
- `M1` Unity MCP 연결 확인: 완료
- `M1.5` Tiny Garden 기획/아트 기준 정리: 완료
- `M2` Tiny Garden 기본 Scene 구성: 완료
- `M3` Player 이동 구현: 완료
- `M4` 복구 대상 상호작용 구현: 완료
- `M5` 첫 playable loop 완성: 완료
- `M6` 경량 하네스 평가: 완료
- `M7` 선택 실험: Skill 실험 완료, Hooks 보류

`M7`의 Hooks 보류는 미완료가 아니라, `M6` 평가에 따라 현재 반복 불편이 작고 하네스 복잡도를 키울 가능성이 있어 진행하지 않기로 한 종료 판단입니다.

## 남은 단서

- 마지막 대화 시점의 저장소 기준으로 작업 트리는 깨끗했고, `main`은 `origin/main`보다 앞서 있었습니다.
- 현재 세션에서 Unity MCP `get_scene_info` 재확인은 timeout으로 완료하지 못했습니다.
- 따라서 이 종료 선언은 저장소의 체크리스트, 구현 파일, Scene 파일, 이전 Unity 검증 기록을 근거로 합니다.
- 최종 릴리즈 태그를 만들기 전에는 Unity Editor에서 `Tools/Codex/M1/Run Play Mode Smoke Test`를 한 번 더 실행하는 것이 좋습니다.

## 후속 범위

이후 작업은 v1 마일스톤 연장이 아니라 별도 후속 범위로 다룹니다.

- v2 기획 또는 playable loop 개선
- Game view 시각 검수 보강
- 반복 검증이 커질 때 Hooks 재검토
- 다음 Unity 프로젝트에서 `tiny-garden-playmode-check` skill 재사용 여부 판단
