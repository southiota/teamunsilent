---
name: agy-chores
description: 반복·대량·기계적인 잡일을 agy(Antigravity CLI)에 위임한다. 이미지 압축·리사이즈·크롭·포맷 변환, alt 텍스트 초안 일괄, 캡션/문구 변형 대량 생성, 템플릿에 문구 채우기, 수집 자료 표 정리, 오탈자 1차 점검, 파일 정리에 사용. 판단이 필요한 일(시안, 기준 결정, 최종 문구)은 맡기지 않는다.
---

# agy에 잡일 맡기기

팀 규칙: **판단은 Claude 에이전트, 반복은 agy.** 서브에이전트 보고의 "agy 위임 필요" 목록도 이 스킬로 처리한다.

## 호출 방법
레포 루트에서 Bash로 실행한다.

```bash
agy -p "<작업 지시>" --mode accept-edits --print-timeout 300s
```

- 파일을 읽기만 하는 작업(목록화, 점검, 요약)은 `--mode plan`.
- `--dangerously-skip-permissions`는 쓰지 않는다.
- 오래 걸리는 일괄 작업은 Bash `run_in_background`로 돌리고 완료 알림을 기다린다.

## 지시문 작성 규칙
agy는 이 대화의 맥락을 모른다. 지시문 하나로 끝나게 쓴다.
1. **대상**: 정확한 파일·폴더 경로
2. **작업**: 무엇을 어떻게 (크기, 포맷, 개수, 규칙)
3. **기준**: 문구 작업이면 "brand/voice.md를 먼저 읽고 용어·톤·금지 사항을 따를 것"
4. **출력 위치**: 원본은 덮어쓰지 말고 새 경로에 (`img/opt/`, `drafts/agy/` 등)
5. **보고**: "끝나면 만든 파일 목록과 건너뛴 항목만 답할 것"

예시:
```bash
agy -p "img/ 의 .jpg 파일을 긴 변 1920px, 품질 80으로 리사이즈해서 img/opt/ 에 같은 이름으로 저장해. 원본은 건드리지 마. 끝나면 파일별 원본/결과 용량 표만 답해." --mode accept-edits --print-timeout 300s
```
```bash
agy -p "brand/voice.md를 먼저 읽어. drafts/content/2026-10-20-insta-hangang.md 의 캡션을 기준으로 길이·훅이 다른 변형 5개를 만들어 drafts/agy/insta-hangang-variants.md 에 저장해. 용어와 금지 사항을 지켜." --mode accept-edits --print-timeout 300s
```

```bash
agy -p "다음 명령만 실행해: .venv/bin/python tools/grade.py '공연사진/2026/20260731_광화문_유승영' -o img/graded/20260731-gwanghwamun --strength 0.9 . 색 보정을 직접 만들지 말고 이 스크립트만 써. 원본 폴더는 건드리지 마. 끝나면 만든 파일 수만 답해." --mode accept-edits --print-timeout 600s
```
사진 톤 보정을 맡길 때는 위처럼 `tools/grade.py` 실행만 지시한다. agy가 필터나 색 값을 임의로 정하게 두지 않는다 (기준: brand/design.md "사진 톤").

사진에서 다른 공연자를 지울 때 (기준: brand/design.md "사진 속 인물"):
```bash
agy -p "이미지 drafts/photos/src/0731-03.jpg 에서 오른쪽 디제이 부스 뒤에 선 검은 모자 남성 1명을 지우고 배경을 자연스럽게 채워. 다른 사람, 특히 관객과 왼쪽 디제이는 그대로 둬. 원본은 덮어쓰지 말고 drafts/photos/edit/0731-03-edit.jpg 로 저장해. 지울 수 없으면 이유만 답해." --mode accept-edits --print-timeout 600s
```
- 한 번에 한 장씩, 지울 사람의 위치와 옷차림을 구체적으로 적는다.
- 인물 제거는 톤 보정 **전에** 한다. 순서는 원본 → 제거(`-edit`) → `tools/grade.py`.
- 결과는 Claude가 직접 열어 확인한다. 흔적이 남으면 그 컷은 버린다.

## 받은 뒤
- 결과 파일을 직접 열어 지시대로 됐는지 확인한다 (개수, 경로, 원본 보존).
- **밖으로 나갈 문구·이미지**가 포함되면 brand-guardian 검수를 거친다.
- agy가 실패하거나 권한 때문에 멈추면, 그 사실과 출력을 사용자에게 그대로 보고한다. 우회하지 않는다.
