"""DJ 프레스킷 페이지(dj/*.html) 생성기.

내용은 아래 DJS 데이터만 고친다. 출처: 리소스/ 프레스킷(DR.KTRL pptx, KALI pdf, LiFY pdf)과 소개서 V0.5.
실명·개인 연락처는 넣지 않는다 (brand/voice.md).

    python3 tools/build_dj.py
"""
from __future__ import annotations

import html
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from cover import cover  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent

DJS = [
    {
        "slug": "dr-ktrl", "name": "DR.KTRL", "img": "ktrl", "ow": "KTRL",
        "aka": "이전 활동명 BORNGI · 봉기",
        "tags": ["K-POP", "POP", "떼창", "EDM", "HARDSTYLE", "HARDCORE"],
        "job": "15년 연구개발사업 기획",
        "quote": "공연도 사전 준비가 8할입니다.",
        "intro": [
            "떼창의 민족 아닙니까. 한강에서 검증된 200곡 이상의 떼창곡으로 나이 불문, 간주까지 함께 부르게 만듭니다.",
            "그리고 오늘 3키로 빼고 가야지? 하드스타일·하드코어로 누구나 뛸 수 있는 유산소 무대를 만듭니다. 즐거움은 전염됩니다.",
        ],
        "stats": [("200곡+", "한강 행사로 검증된 떼창곡"), ("2023~", "한강 사일런트 디스코"), ("38건+", "송도 맥주 축제·서리풀 페스티벌 외")],
        "styles": [
            ("PLAY STYLE Ⅰ", "“떼창의 민족 아닙니까”", "#K-pop #Pop #떼창 #EDM · 24년 한강 행사로 검증된 노래 200곡 이상 · #나이불문 #간주로종결"),
            ("PLAY STYLE Ⅱ", "“오늘 3키로 빼고 가야지?”", "#Hardstyle #Hardcore #유산소 #체지방 · 누구나 뛸 수 있는 음악을 찾는 시간"),
            ("ENERGY VIRUS", "즐거움은 전염된다", "떼창 + 유산소 = ENERGY · ENJOY · ENDORPHIN"),
        ],
        "history": [
            ("2023~", ["한강 사일런트 디스코 메인 DJ"]),
            ("2024", ["카즈미 원더 캠프", "시흥 신언니의 낭만적인 하루", "화성 루나빛 축제", "강북 수유 청춘마켓", "수원화성 미디어아트 페스티벌", "안양시민축제 (안양춤축제)", "서리풀 페스티벌", "강남 문화 한마당 축제 (코엑스)", "강진 하맥축제", "태능시장 어울림 한마당 축제", "부산 유라리 건맥축제", "하남·안성·고양 아쿠아필드 사일런트 디스코", "덜위치칼리지 국제학교 공연", "오산 주간보호센터 (어르신 클럽)", "춘천마임 불의도시 축제", "경주 EDM 페스티벌", "단국대 EDM 축제", "안산대학교 축제", "남원 정월대보름 축제", "홍대 템플 HARD&BASS 파티"]),
            ("2023", ["홍대 무소음 투어 MUTE.K", "남양주 현대프리미엄아울렛 스페이스원 야외 공연", "한미 EDM 연합 페스티벌", "롯데타워 아쿠아슬론 층간 응원 음원 녹음", "광주 달빛 플리마켓 오프닝·클로징", "Double Attack 파티", "하이텐션 x 클럽엔트리 파티", "홍대 도킹어라운드 라운지 파티", "대림 클럽 Spade A"]),
            ("2022", ["부평 Center18 라운지 객원 DJ (2022~2024)", "홍대 클럽 Entry 카운트다운", "홍대 클럽 Temple 추석 행사", "HardTrip 파티", "제2회 WMF 페스티벌 파티"]),
        ],
        "gallery": ["live2/kt27", "live2/kt15", "live/k32", "live2/kt26", "live2/kt19", "live2/kt12", "live/k02", "live2/c014", "live/e_gwang_ktrl"],
        "videos": [("ktrl-mapo", "한강 마포대교"), ("ktrl-seori", "서초 서리풀 페스티벌"), ("ktrl-jamsu2", "한강 잠수교"), ("ktrl-stage", "무대 공연"), ("ktrl-stage2", "무대 공연"), ("ktrl-incheon", "인천 FESTA")],
        "links": [("INSTAGRAM", "@dr.ktrl", "https://www.instagram.com/dr.ktrl/")],
    },
    {
        "slug": "lify", "name": "LiFY", "img": "lify", "ow": "LiFY",
        "aka": "",
        "tags": ["ALL GENRE", "EDM", "HARD BASS", "LOUNGE"],
        "job": "마케터",
        "quote": "찍고 싶은 순간을 만듭니다.",
        "intro": [
            "클럽과 호텔 라운지, 브랜드 파티와 한강 사일런트 디스코까지. 장르를 가리지 않는 올장르 DJ입니다.",
            "디제잉 대회 우승과 차트 기록으로 다진 기본기에, 마케터의 감각으로 관객이 남기고 싶은 장면을 설계합니다.",
        ],
        "stats": [("1st", "2019 상상 디제잉 대회 우승"), ("5th", "Mixcloud Trending Chart (2019.09)"), ("2023~", "한강 사일런트 디스코 메인 DJ")],
        "styles": [
            ("AWARD", "2019 Sangsang DJing Competition 1st", "2020 Vava DJ Competition Finalist · 2020 IISFestival Final Stage"),
            ("CHART", "Mixcloud Trending Chart 5th", "2019.09"),
            ("ORGANIZER", "2019 KOREAN HARD BASS", "Organizer & DJ · Korean Hard Bass Vol.1&2"),
        ],
        "history": [
            ("기업·브랜드", ["롯데백화점 루프탑 와인 파티", "롯데백화점 The Wave 팝업스토어", "한강 페스티벌 (사일런트 디스코)", "FNB People 3주년 요트 파티", "광주 국립아시아문화전당 ACC City Run"]),
            ("호텔·라운지", ["비스타 워커힐 서울 Re:Bar", "반얀트리 클럽 앤 스파 루프탑", "Billions Seoul (강남)", "Janus Lounge 레지던트 (청담)", "Getallright Seoul 레지던트 (청담)", "Whitebar 7주년 파티 (청담)", "Fisherman Busan 1주년 파티 (부산)", "Glam Lounge (미국 애틀랜타)"]),
            ("파티·클럽", ["한강 무소음 DJ 파티 메인 DJ (2023~)", "Rhythm of the Night Vol.9·11·15", "Korean Hard Bass Vol.1&2", "Itaewon Connect 1st Party", "Nevermind 런칭 파티", "PLG EDM 네트워킹 파티"]),
        ],
        "gallery": ["live3/lify_cheonan1", "live2/c050", "live3/lify_seori_booth", "live2/kt34", "live3/lify_banpo_night", "live/lify02",
                    "live2/c077", "live3/lify_cheonan2", "live2/c428", "live3/lify_mapo_point", "live/lify03", "live3/lify_seori_armup"],
        "videos": [("lify-calling", "한강 반포"), ("lify-seori", "서초 서리풀 페스티벌"), ("lify-banpo", "한강 반포"),
                   ("lify-usa", "미국 클럽 공연"), ("lify-ailee", "한강"), ("lify-seori2", "서초 서리풀 페스티벌")],
        "links": [
            ("INSTAGRAM", "@dj_lify", "https://www.instagram.com/dj_lify/"),
            ("YOUTUBE", "DJ LiFY", "https://www.youtube.com/channel/UCKuwjx_NIb-UbznpO4YL9Eg"),
        ],
    },
    {
        "slug": "kali", "name": "KALI", "img": "kali", "ow": "KALI",
        "aka": "",
        "tags": ["OPEN FORMAT", "MELBOURNE BOUNCE", "BIGROOM HOUSE"],
        "job": "의약품 영업",
        "quote": "쭈뼛대는 관객, 제가 설득합니다.",
        "intro": [
            "어린아이부터 중장년층까지 모두를 아우르는 음악을 들려주는 DJ KALI. 익숙한 추억의 노래부터 모두가 따라 추는 메가히트곡까지, 폭넓은 스펙트럼으로 관객이 함께 뛰어놀 수 있는 즐거움을 선사합니다.",
            "클럽과 대·소규모 파티, 학교·기업·단체 행사 경험을 바탕으로 행사 취지에 맞는 센스 있는 선곡과 에너지 넘치는 호응 유도로 현장의 몰입도를 끌어올립니다.",
        ],
        "stats": [("2013~", "DJ 경력"), ("2023~", "사일런트 디스코 파트너 DJ"), ("39건+", "예술의전당 두둠칫·광안리 무소음 콘서트 외")],
        "styles": [
            ("MOTTO", "매순간 즐거움을 위해!", "모두가 함께 뛰어놀 수 있는 순간을 만듭니다."),
            ("MIXCLOUD", "Melbourne Bounce 3rd · 6th", "Mixcloud Trending Chart"),
            ("MIXCLOUD", "Bigroom House 5th · 7th", "Mixcloud Trending Chart"),
        ],
        "history": [
            ("2026", ["사일런트 디스코 마포대교·잠수교 메인 DJ", "그루브 인 관악 무소음 파티", "성수 MIXMIX TV UNSILENT DISCO", "서울바캉스페스티벌 in 신촌", "용인 워터스플래쉬 : 스위치ON", "예술의전당 두둠칫 사일런트 디스코", "을지로 페이퍼크레인", "한강 유람선 BLEND STAGE : TECHNO", "광안리 수영구 특화프로그램 : 무소음 DJ 콘서트", "성남시청 사일런트 디스코"]),
            ("2025", ["사일런트 디스코 마포대교·잠수교 메인 DJ", "하남 스타필드 아쿠아필드 파티", "부산 벡스코 대학생 연합 CO-SHOW", "단양 다리안 캠핑 페스티벌"]),
            ("2024", ["사일런트 디스코 마포대교·잠수교·뚝섬 메인 DJ", "코엑스 문화축제", "서초 서리풀 페스티벌", "한양대학교 국제 동계 WELCOME GLOW 파티", "수원화성 미디어아트", "동탄 호수공원 루나 라이트 페스티벌", "시흥 ROMANTIC NOISELESS DJ 파티", "부산 광안리 비치 파티", "대구 슈마커 오픈 파티"]),
            ("2023", ["사일런트 디스코 마포대교·잠수교·뚝섬 메인 DJ", "코엑스 COFFEE FAIR", "야누스 라운지", "부산 피셔맨 라운지 레지던트", "부산 DENGUE FEVER PUB 게스트"]),
            ("2019~2022", ["KOREAN HARD BASS 오거나이저 & DJ (2019·2022)", "부산 PRIZM LOUNGE (2021)", "부산 BASS OPEN DECK 오거나이저 & DJ", "부산 PKNU CLASS PARTY w/ SIUL PARTY", "디지털 스타디움 워터파크", "부산 CLUB VIBE·CLUB MAHA 게스트", "부산 PNU BASEMENT·NOBODY·POCHAMONSTER·SPACE WHALE 라운지"]),
        ],
        "gallery": ["live3/team_cheonan", "live3/kali_sac_face", "live3/kali_mapo_booth", "live3/kali_sac_crowd", "live2/c112", "live2/c077", "live3/kali_sac_play", "live/s_k1", "live2/c123"],
        "videos": [("kali-mapo", "한강 마포대교"), ("kali-apt2", "한강 마포대교"), ("kali-jamsu", "한강 잠수교"),
                   ("kali-love", "한강 마포대교"), ("kali-mapo2", "한강 마포대교"), ("kali-apt", "한강 마포대교")],
        "links": [("INSTAGRAM", "@djkali92", "https://www.instagram.com/djkali92/")],
    },
]

PAGE = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{name} 프레스킷 — 팀 언사일런트</title>
<meta name="description" content="팀 언사일런트 DJ {name} 프레스킷. {quote}">
<link rel="canonical" href="https://southiota.github.io/teamunsilent/dj/{slug}.html">
<meta property="og:title" content="{name} — 팀 언사일런트">
<meta property="og:description" content="{quote}">
<meta property="og:image" content="https://southiota.github.io/teamunsilent/img/dj/{img}.jpg">
<meta name="theme-color" content="#1A2828">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%231A2828'/%3E%3Ccircle cx='16' cy='16' r='6' fill='%23C2EA8C'/%3E%3C/svg%3E">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,600..900&family=JetBrains+Mono:wght@500;700&display=swap">
<link rel="stylesheet" href="../assets/site.css">
<link rel="stylesheet" href="../assets/dj.css">
<link rel="stylesheet" href="../assets/cover.css">
</head>
<body>
<a class="skip" href="#main">본문으로 건너뛰기</a>
<header class="nav" data-solid="1"><div class="wrap">
  <a class="logo" href="../"><i aria-hidden="true"></i>팀 언사일런트</a>
  <nav aria-label="DJ 프레스킷">{tabs}</nav>
  <a class="cta" href="../#contact">섭외 문의</a>
</div></header>

<main id="main">
<section class="pk-hero">
  {cover}
  <div class="wrap pk-copy">
    <p class="eyebrow">TEAM UNSILENT · PRESS KIT</p>
    <h1>{name}</h1>
    {aka}
    <p class="pk-q">“{quote}”</p>
    <p class="pk-job">본업 모먼트 · {job}</p>
    <ul class="pk-tags">{tags}</ul>
  </div>
</section>

<div class="wave tall"><div class="wrap">
  <span class="lab"><i></i>{name} · CH.1 · CH.2 · CH.3</span>
  <canvas data-wave="channels" data-bpm="128" aria-hidden="true"></canvas>
  <span class="lab">HEADSET MIX</span>
</div></div>

<section class="sec">
  <div class="wrap pk-intro">
    <div><div class="eyebrow rv">ARTIST PROFILE</div>{intro}</div>
    <dl class="pk-stats rv d1">{stats}</dl>
  </div>
  <div class="wrap pk-styles">{styles}</div>
</section>

<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="eyebrow rv">SELECTED PERFORMANCES</div>
    <h2 class="h2 rv">공연 이력</h2>
    <div class="pk-hist">{history}</div>
  </div>
</section>

<section class="sec" style="padding-top:0" aria-label="공연 사진">
  <div class="wrap">
    <div class="eyebrow rv">LIVE</div>
    <div class="pk-gal">{gallery}</div>
  </div>
</section>

{videos}

<section class="sec pk-end">
  <div class="wrap">
    <div class="pk-links">{links}</div>
    <div class="pk-cta rv">
      <h2 class="h2">{name} 섭외,<br>행사 정보만 알려주세요.</h2>
      <div class="pk-ask"><a class="cta" href="../#contact">섭외 문의 →</a><p><a href="tel:0507-1494-4029">0507-1494-4029</a> · <a href="mailto:support@fextai.com">support@fextai.com</a></p></div>
    </div>
    <nav class="pk-next" aria-label="다른 DJ">{others}</nav>
  </div>
</section>
</main>

<footer class="foot"><div class="wrap">
  <div class="big" aria-hidden="true">UNSILENT</div>
  <p>© 팀 언사일런트 · 4년간 한강에서 검증된 포터블 무소음 디제잉<br>섭외 문의 <a href="tel:0507-1494-4029">0507-1494-4029</a> · <a href="mailto:support@fextai.com">support@fextai.com</a></p>
  <nav aria-label="온라인 채널"><a href="https://www.instagram.com/dr.ktrl/" target="_blank" rel="noopener">Instagram · DR.KTRL</a><a href="https://www.instagram.com/djkali92/" target="_blank" rel="noopener">KALI</a><a href="https://www.instagram.com/dj_lify/" target="_blank" rel="noopener">LiFY</a><a href="https://blog.naver.com/night_share" target="_blank" rel="noopener">Blog</a></nav>
</div></footer>
<script src="../assets/wave.js" defer></script>
<script src="../assets/site.js" defer></script>
<script src="../assets/pk.js" defer></script>
</body>
</html>
"""


def e(s: str) -> str:
    return html.escape(s, quote=True)


def render(dj: dict) -> str:
    cur = ' aria-current="page"'
    tabs = "".join(f'<a href="{o["slug"]}.html"{cur if o is dj else ""}>{e(o["name"])}</a>' for o in DJS)
    intro = "".join(f'<p class="pk-p rv">{e(p)}</p>' for p in dj["intro"])
    stats = "".join(f"<div><dt>{e(v)}</dt><dd>{e(k)}</dd></div>" for v, k in dj["stats"])
    styles = "".join(
        f'<article class="rv d{i}"><small>{e(k)}</small><h3>{e(t)}</h3><p>{e(d)}</p></article>'
        for i, (k, t, d) in enumerate(dj["styles"]))
    txt = ' class="txt"'  # 연도가 아닌 묶음 이름은 아웃라인 대신 글자로
    history = "".join(
        f'<div class="rv"><h3{"" if y[0].isdigit() else txt}>{e(y)}</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></div>'
        for y, items in dj["history"])
    wide = len(dj["gallery"]) % 3 == 0  # 큰 칸(2x2)을 쓰면 3의 배수일 때만 빈칸 없이 맞는다
    gallery = "".join(
        f'<figure class="rv{" wide" if wide and i == 0 else ""}"><img src="../img/{g}.webp" alt="{e(dj["name"])} 공연 현장" loading="lazy"></figure>'
        for i, g in enumerate(dj["gallery"]))
    videos = "".join(
        f'<figure class="pk-vid rv"><video data-src="../vid/clips/{v}.mp4" poster="../vid/clips/{v}.jpg" muted loop playsinline preload="none" aria-label="{e(dj["name"])} {e(c)} 현장 영상"></video><figcaption>{e(c)}</figcaption></figure>'
        for v, c in dj["videos"])
    videos_sec = (f'<section class="sec" style="padding-top:0" aria-label="공연 영상"><div class="wrap"><div class="eyebrow rv">VIDEO</div><div class="pk-vids">{videos}</div></div></section>'
                  if videos else "")
    links = "".join(
        f'<a href="{u}" target="_blank" rel="noopener"><small>{e(k)}</small><b>{e(t)} ↗</b></a>' for k, t, u in dj["links"])
    others = "".join(
        f'<a href="{o["slug"]}.html"><small>NEXT DJ</small><b>{e(o["name"])} →</b></a>' for o in DJS if o is not dj)
    return PAGE.format(
        name=e(dj["name"]), slug=dj["slug"], img=dj["img"], ow=e(dj["ow"]), quote=e(dj["quote"]), job=e(dj["job"]),
        aka=f'<p class="pk-aka">{e(dj["aka"])}</p>' if dj["aka"] else "",
        tags="".join(f"<li>{e(t)}</li>" for t in dj["tags"]),
        cover=cover(dj["img"], f'../img/dj/{dj["img"]}-cut.webp', "right:max(56px,calc(50% - 620px))"),
        tabs=tabs, intro=intro, stats=stats, styles=styles, history=history, gallery=gallery, videos=videos_sec, links=links, others=others)


def main() -> None:
    out = ROOT / "dj"
    out.mkdir(exist_ok=True)
    for dj in DJS:
        (out / f'{dj["slug"]}.html').write_text(render(dj), encoding="utf-8")
        print(f'dj/{dj["slug"]}.html')


if __name__ == "__main__":
    main()
