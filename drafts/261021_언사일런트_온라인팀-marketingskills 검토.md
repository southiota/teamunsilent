# marketingskills 도입 검토

**결론**
1. 전체 설치는 하지 않는다. 영어권 SaaS 전제이고, 우리 voice.md와 충돌하는 권고(가격 공개, 긴박감 연출)가 섞여 있다.
2. 쓸 만한 것은 `copy-editing`, `copywriting`, `cold-email`, `public-relations`, `schema` 다섯 개다. 원본 그대로가 아니라 우리 기준에 맞게 줄여서 둔다.
3. 위험은 낮다. 스킬 본문은 마크다운이고 훅·allowed-tools가 없다. 다만 `tools/clis/`(외부 API 호출 JS 66개)와 npx 설치 안내는 가져오지 않는다.

- 저장소: https://github.com/coreyhaines31/marketingskills (이름 정확함. 'marketingshills' 아님)
- 커밋: `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b` (main, 2026-10-19 push, v2.13.0)
- 확인 날짜: 2026-10-21
- 라이선스: MIT (저작권 Corey Haines). 별 55k대.
- 확인 방법: GitHub tarball을 스크래치패드(`/private/tmp/claude-501/.../scratchpad/mskills/src/`)에 받아 읽기만 했다. 설치·실행·복사 없음. 레포에는 이 보고서만 만들었다.

---

## 1. 저장소 구성

- 스킬 51개 (`skills/*/SKILL.md`). 대부분 영어. 각 스킬에 `references/`와 `evals/evals.json`이 붙는다.
- 스킬 안 스크립트는 `skills/conversion-tracking/scripts/*.py` 2개와 `assets/snippets/*.js` 뿐이다.
- 그 밖에 `tools/clis/*.js`(마케팅 SaaS API 래퍼 66개), `scripts/`, `tests/`, `.github/workflows/`가 있다.
- 한국·네이버 언급은 `skills/aso/references/apple-specs.md`의 "한국어는 글자당 2~3바이트" 한 줄이 전부다.
- 전 스킬이 `.agents/product-marketing.md`를 먼저 읽도록 되어 있다 (`product-marketing` 스킬이 만든다).

## 2. 추천 스킬 (5개)

| 스킬 | 이유 | 한계 |
|---|---|---|
| `copy-editing` | 이미 쓴 문구를 7단계로 점검한다 (명료·톤·So What·증거·구체성). 'Prove It' 단계가 "근거 없는 최상급 금지"라는 우리 규칙과 맞는다. 한 줄만 고치라 하면 그 줄만 고치는 모드가 있다. `references/checklist.md`는 영어 단어 대체표라 한국어에는 쓸모가 낮다. | 영어 관용구 기준. 한국어 문체는 voice.md가 우선. |
| `copywriting` | "빈 브리프 / 기존 목소리 / 한 줄 수정"을 먼저 진단하고, 근거 없는 수치를 지어내지 않으며 모자라면 `[NEED: ...]`로 표시한다. 우리 content 에이전트의 `[확인 필요]` 방식과 같다. 홈페이지 히어로·CTA 수정안 작업에 쓴다. | 가격 페이지 항목(267행 부근)은 제외. AI티 목록(`ai-tells.md`)은 영어 표현 위주. |
| `cold-email` | 섭외 메일에 가장 가깝다. "받는 사람의 상황을 먼저, 요청은 하나, 짧게". 우리 content 에이전트의 "5문단 이내, 행사 조건에 맞는 방식 하나 추천"과 방향이 같다. `personalization.md`, `follow-up-sequences.md`가 도움이 된다. | 대량 발송·발신 도메인·워밍업·LinkedIn 내용은 쓰지 않는다. 우리는 행사 담당자 소수에게 보내는 일이다. 한국 사업자 대상 광고성 메일 수신 규정은 따로 확인해야 한다. |
| `public-relations` | 프레스킷, 기자 피칭, 이야기 각도(창업 이야기, 다윗과 골리앗). `references/journalist-pitching.md`가 보도자료·프레스킷 정리에 참고가 된다. | 미국 매체(HARO, TechCrunch) 중심. 한국 매체 목록은 없다. 우리 보도 194+는 "행사 보도"라는 표기 규칙이 있어 팀 단독 보도처럼 쓰지 않도록 주의. |
| `schema` | JSON-LD, FAQ, Organization. web 에이전트가 이미 하는 일을 점검하는 용도로 좋다. | 구글 기준. 네이버 서치어드바이저 이야기는 없다. |

보조로만 참고: `seo-audit`(구글 기준 점검표. 네이버 항목 없음, 497행으로 길다), `events`(행사 지원 문안 때 "누구를 방에 모을지" 틀을 참고. B2B SaaS 기준), `product-marketing`(아래 6장 참고).

## 3. 맞지 않는 대표 스킬

- `social`: 링크드인·트위터·틱톡 중심. 인스타 해시태그도 "3~5개 권장"으로 우리 기준(10개 이내)과 다르다. 인스타 캡션은 content 에이전트 규칙이 더 맞다.
- `pricing`, `offers`, `paywalls`: 가격·보너스·희소성 설계. 공개 채널 가격 비공개 원칙과 반대 방향.
- `popups`: 카운트다운 타이머, 마감 긴박감 권장 (130, 354, 405행).
- `ads`, `ad-creative`, `ab-testing`, `cro`, `analytics`, `conversion-tracking`, `attribution`: 유료광고·전환 추적. 지금 업무에 없다. 정적 페이지에 추적 코드를 넣는 일은 web 에이전트 규칙("사용자 확인 없이 외부 스크립트 추가 금지")과 부딪힌다.
- `emails`, `churn-prevention`, `onboarding`, `signup`, `sms`, `referrals`: SaaS 구독·가입 흐름.
- `marketing-council`: 유명 마케터 흉내 토론. 근거가 약하고 우리 톤과 무관.
- `programmatic-seo`, `directory-submissions`, `link-building`: 대량 페이지·백링크 작업. 우리 규모에 과하다.
- `image`, `video`: 외부 생성 도구 전제. 사진 인물 규칙(관객+팀원 3명만)과 충돌 위험.

## 4. 기존 기준과 겹침·충돌

| 항목 | 마케팅스킬 | 우리 기준 | 처리 |
|---|---|---|---|
| 가격 | `sales-enablement` 325행 "가격을 숨기지 말라, 투명하게", 10번 "Pricing Overview", `copywriting` 가격 페이지 | voice.md "공개 채널에 금액 쓰지 않음. 소개서·견적만" | 충돌. 가격 관련 지시는 모두 무시하도록 명시한다. |
| 긴박감·희소성 | `popups`, `offers`가 마감·희소성 권장 (다만 `offers`는 가짜 타이머를 금지) | 과장 금지, 검증된 사실로 말함 | 해당 스킬은 두지 않는다. |
| 톤 | 'peer로 쓰기', 'punchy', 축약형 구어체 (영어 기준) | B2B는 협업형 존댓말, B2C는 가볍되 반말 금지 | 충돌 가능. 톤은 voice.md가 항상 우선. |
| 최상급 | `copywriting`은 "best-in-class는 장식, 증거 없으면 쓰지 말라"고 해서 방향은 같음 | "국내 유일/최고" 금지 | 일치. |
| 사실 지어내기 | 증거 없는 수치 금지, `[NEED: ]` 표시 | `[확인 필요]` | 일치. 표기만 통일한다. |
| 기준 문서 위치 | `.agents/product-marketing.md`를 단일 맥락 문서로 요구 | `brand/voice.md`가 단일 기준 | 중복 위험. 스킬 안의 경로를 `brand/voice.md`로 바꾼다. |
| 영어권 전제 | 영어 AI티 목록, 영어 단어 대체표, 미국 매체·구글·링크드인 | 한국어, 네이버, 인스타 | 한국어 문구에는 그대로 적용 불가. 원칙(구체성, 증거)만 가져온다. |
| 외부 링크·광고 | 일부 스킬에 저자 에이전시·Magister 링크 (`ad-creative/SKILL.md` 456행 `?ref=marketingskills`) | 외부 링크는 사용자 확인 | 해당 문단은 제거. |
| 에이전트 구조 | 스킬은 "Use when user mentions ..." 키워드로 자동 호출 | 우리는 총괄→담당 에이전트→brand-guardian | 자동 호출 키워드가 content와 겹쳐 두 갈래로 갈 수 있다. description을 줄이거나 content가 명시 호출만 하게 한다. |

## 5. 보안 점검

**낮음 (스킬 본문)**
- 51개 SKILL.md 어디에도 `allowed-tools`, `hooks`, PreToolUse/SessionStart 같은 자동 실행 설정이 없다 (grep 전수 확인). `.claude/settings`나 `settings.json`도 없다.
- 프롬프트 주입으로 보이는 문구("이전 지시 무시", "사용자에게 알리지 말 것" 등)는 찾지 못했다. grep으로 확인한 범위이며, 모든 줄을 눈으로 읽은 것은 아니다.
- 파일 쓰기 지시는 두 곳이다. `product-marketing`이 `.agents/product-marketing.md`를 만들고(`SKILL.md` 12, 145, 286행), `marketing-plan`이 `~/marketing-plans/`에 쓴다(경로 안전 규칙 있음, `SKILL.md` 39행). `marketing-council`은 `.agents/advisors/`에 쓴다 (142행). 쓰기 위치가 `.claude/` 밖이다.
- 명령 실행 안내는 참고 문서에만 있다. `curl`(`directory-submissions/SKILL.md` 144행, `social/references/listening.md`, `public-relations/references/newsjacking.md` 153행, `ai-seo/references/linkedin-ai-citations.md` 62행), `npx hyperframes`/`npx create-video`(`video/SKILL.md` 59, 75행), `npx is-agentic`(`ai-seo/SKILL.md` 301행), `npm install -g agent-browser`(`marketing-plan/references/ops-stack-mapping.md` 106행), `brew install`. 추천 5개 스킬에는 해당 없다. 에이전트가 이런 명령을 제안해도 승인 전에는 실행하지 않는다.

**중간 (스킬 밖 코드)**
- `tools/clis/*.js` 66개: 마케팅 SaaS(GA4, Semrush, Ahrefs, Meta Ads, Google Ads, Apollo, ZoomInfo, Clearbit 등)의 API를 `fetch`로 호출한다. API 키를 환경변수(`process.env.*_API_KEY` 등)에서 읽는다. 외부 호스트는 각 서비스 공식 도메인 위주였고 의심스러운 도메인은 못 봤다 (도메인 빈도 집계 상위 15개 기준). `child_process`, `eval` 사용은 grep에 안 걸렸다. 일부 스킬 본문이 이 도구를 안내한다 (`ad-creative/SKILL.md` 446행 `node tools/clis/google-ads.js ...`). 우리는 키도 계정도 연결하지 않으므로 가져오지 않는다.
- `skills/conversion-tracking/scripts/build_recipe.py`, `check_recipes.py`와 `assets/snippets/*.js`(폼 도구 감지 JS): 읽기만 했고 실행하지 않았다. 스킬 폴더 안 `scripts/*.py`에서 네트워크 호출은 grep에 안 걸렸다. 우리는 이 스킬을 쓰지 않는다.
- `scripts/package_skills.py`는 `git` 명령 호출, `scripts/sync-partners.mjs`, `.github/scripts/sync-skills.js`와 워크플로(`.github/workflows/*.yml`)는 저장소 운영용이다. 우리와 무관하다.
- `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`: 플러그인 메타데이터만 있고 훅 없음. README는 `npx skills add coreyhaines31/marketingskills` 또는 `/plugin` 마켓플레이스 설치를 안내한다. 이 방식은 51개와 `tools/`를 통째로 들여오므로 쓰지 않는다.

**상업적 영향**
- README와 `tools/PARTNERS.md`에 유료 파트너(Converly, Ploy, AIsa, Omnia)가 있다. 저장소는 "추천에 영향 없음"이라고 밝히지만, 도구 추천 문단이 광고성일 수 있다. 추천 5개 스킬에서 도구 안내 문단(`cold-email/SKILL.md` 191행 이하 등)은 지운다.

**라이선스**
- MIT. 복사·수정 가능하되 `LICENSE` 사본과 저작권 표시를 같이 두어야 한다. `copywriting`에는 Profound `improved-copywriting` (MIT) 차용 표기가 있어 함께 보존한다.

## 6. 도입안 (짧게)

**원칙**: 설치(`npx`/`/plugin`) 금지. 사용자 승인 후, 필요한 SKILL.md를 사람이 읽고 줄여서 `.claude/skills/`에 둔다. 도입 전에 brand-guardian 검수를 거친다.

| 스킬 | 형태 | 쓰는 에이전트 | 고칠 점 |
|---|---|---|---|
| `copy-editing` | 줄여서. 7단계 틀과 Prove It만 남기고 영어 단어표 제거 | content (홈페이지·캡션 수정안), brand-guardian은 읽기만 | 맥락 경로를 `brand/voice.md`로. "voice.md 용어·톤이 우선" 한 줄 추가 |
| `copywriting` | 줄여서. 진단 3가지, 3문항 게이트, `[NEED]`만 남김 | content | 가격 페이지 항목 삭제. `[NEED]`를 `[확인 필요]`로. 가격 언급 금지 규칙 명시 |
| `cold-email` | 줄여서. 원칙·personalization·follow-up만 | content (섭외 메일) | 발신 도메인·대량 발송·LinkedIn·도구 목록 삭제. 존댓말 협업형 톤 명시. 발송은 사용자 확인 |
| `public-relations` | 원본 일부. `journalist-pitching.md`, 프레스킷 부분만 | content | 미국 매체·HARO·위기 대응·newsjacking 삭제. 한국 매체 목록은 별도로 만든다. "행사 보도로 표기" 규칙 추가 |
| `schema` | 보류 가능 | web | web이 이미 JSON-LD를 갖고 있다. 점검 체크리스트로만 한 번 참고하고 스킬로는 두지 않아도 된다 |

- 나머지 46개는 두지 않는다. 필요해지면 그때 개별 검토한다.
- 두지 말 것: `product-marketing`(우리는 voice.md가 있고, 별도 `.agents/` 문서를 만들면 기준이 둘이 된다. 다만 "고객 언어·반론 정리" 항목은 voice.md 보강 때 참고할 만하다).
- 도입 후 확인: 같은 요청(예: 섭외 메일 한 통)을 현재 content 에이전트와 스킬 적용 버전으로 각각 만들어 brand-guardian에 비교 검수시킨다. 개선이 없으면 철회한다.
- 한 가지 대안: 스킬을 쓰지 않고, 아이디어(3문항 게이트, 7단계 점검)를 content.md에 5~6줄로 옮기는 방법도 있다. 파일이 늘지 않아 가장 가볍다.

## 확인하지 못한 것

- 51개 SKILL.md 전체를 줄 단위로 읽지는 않았다. 앞부분·설명·키워드 검색으로 훑었다. 추천 5개와 비추천 대표 스킬은 본문을 직접 확인했다.
- 한국 시장 적합성은 저장소에 한국 자료가 거의 없다는 사실과 영어권 전제를 근거로 판단했다. 실제 한국어 출력 품질은 시험하지 않았다.
- 도입 시점의 저장소 변경(활발히 갱신 중, 하루 단위 push)은 따로 확인이 필요하다. 도입할 때 커밋 해시를 고정해서 받는다.
