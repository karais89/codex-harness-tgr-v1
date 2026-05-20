# Tiny Garden Restore 이미지 생성 프롬프트

## 목적

이 문서는 M1.5에서 사용할 컨셉 참고 이미지의 생성 기준을 기록합니다.

이미지는 M2 구현용 에셋이 아니라, Tiny Garden Restore의 분위기와 구도 기준을 맞추기 위한 컨셉보드입니다.

## 최종 프롬프트

```text
Use case: stylized-concept
Asset type: concept reference board for a small Unity 2D game
Primary request: Create one cozy top-down 2D concept board for Tiny Garden Restore, showing a small neglected garden with a small gardener character and three clear restore targets: weeds, a wilted flower, and a dirty stone tile.
Scene/backdrop: a compact spring garden seen from above, with part of the scene neglected and part restored in the same image.
Subject: a small gardener character standing near the restore targets.
Style/medium: cozy 2D game concept art, soft shapes, readable object silhouettes, gentle hand-painted feel.
Composition/framing: top-down view, one cohesive garden scene, enough spacing so the weeds, wilted flower, dirty stone tile, gardener, neglected area, and restored area are visually distinct.
Lighting/mood: calm, quiet restoration mood with soft daylight.
Color palette: soft spring garden palette with fresh greens, light soil browns, gentle flower colors, clean stone grays, and slightly muted colors for neglected areas.
Constraints: no text, no watermark, no UI labels, no speech bubbles, no logos, no inventory, no shop, no complex interface.
Avoid: photorealism, 3D render, isometric perspective, side view, dark fantasy mood, large buildings, combat elements, busy decoration, unreadable clutter.
```

## 피해야 할 요소

- 이미지 안 텍스트
- 워터마크
- UI 라벨
- 말풍선
- 로고
- 인벤토리나 상점처럼 보이는 UI
- 3D 렌더 느낌
- isometric 시점
- side view 시점
- 전투나 위협적인 분위기
- 작은 복구 대상이 묻히는 과한 장식

## 생성 결과 검수 기준

- top-down 정원으로 보입니다.
- 작은 정원사가 있습니다.
- 잡초, 시든 꽃, 더러운 타일이 구분됩니다.
- 한 장면 안에서 방치 상태와 복구 상태의 대비가 보입니다.
- 봄 정원 팔레트로 읽힙니다.
- 텍스트, 워터마크, UI 라벨이 없습니다.
- M2 구현용 직접 에셋이 아니라 컨셉 참고 자료로만 사용하기에 적절합니다.

## 저장 위치

생성한 최종 이미지는 다음 경로에 저장합니다.

```text
docs/art/images/tiny-garden-concept-board-01.png
```
