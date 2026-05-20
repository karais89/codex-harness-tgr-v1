# Tiny Garden Restore 이미지 생성 프롬프트

## 목적

이 문서는 M1.5에서 사용할 컨셉 참고 이미지의 생성 기준을 기록합니다.

이미지는 M2 구현용 에셋이 아니라, Tiny Garden Restore의 분위기와 구도 기준을 맞추기 위한 컨셉보드입니다.

## 최종 프롬프트

```text
Draw one cozy top-down 2D concept board for Tiny Garden Restore, a small Unity game about quietly restoring a neglected spring garden.

Show one cohesive compact garden scene from above with a small gardener character and exactly three clear restoration targets: weeds, a wilted flower, and a dirty stone tile.

Make the neglected area and restored area visible in the same image, with enough spacing so the gardener, weeds, wilted flower, dirty stone tile, neglected soil, clean stone, and restored flowers are visually distinct.

Use cozy 2D game concept art with soft shapes, readable object silhouettes, gentle hand-painted texture, calm daylight, fresh greens, light soil browns, gentle flower colors, clean stone grays, and slightly muted colors for neglected areas.

Do not include text, watermark, UI labels, speech bubbles, logos, inventory, shop UI, complex interface, photorealism, 3D render, isometric perspective, side view, dark survival mood, combat, weapons, monsters, large buildings, busy decoration, or unreadable clutter.
```

## 도구 기준

OpenAI 공식 이미지 생성 문서 기준으로 다음 중 하나를 사용합니다.

- Responses API: `gpt-5.5` 같은 mainline model에서 `image_generation` tool을 호출합니다.
- Image API: `gpt-image-2`를 직접 지정해 단일 이미지 생성을 요청합니다.

이 프로젝트에서는 컨셉 참고 이미지 1장이 목적이므로 Image API의 `gpt-image-2` 또는 Responses API의 `image_generation` tool 중 더 단순한 쪽을 선택합니다.

## 생성 결과 기록

- 생성 도구:
- 모델:
- 저장 경로: `docs/art/images/tiny-garden-concept-board-01.png`
- 원본 프롬프트:
- `revised_prompt`: API 응답에서 제공된 경우 여기에 기록합니다.
- 시각 검수 결과:

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
