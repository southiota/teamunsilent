"""DJ 커버(assets/cover.css) 마크업. 홈 DJ 패널과 프레스킷 상단이 같이 쓴다."""
import html

COVERS = {
    "ktrl": dict(name="DR.KTRL", no="01", title="DR.KTRL"),
    "lify": dict(name="LiFY", no="02", title="LiFY"),
    "kali": dict(name="KALI", no="03", title="KALI"),
}


def cover(key: str, img_src: str, style: str = "", alt: str = "") -> str:
    c = COVERS[key]
    e = html.escape
    st = f' style="{style}"' if style else ""
    return (f'<div class="cv"{st}>'
            f'<p class="cv-title" aria-hidden="true" style="--n:{len(c["title"])}">{e(c["title"])}</p>'
            f'<img class="cv-cut" src="{img_src}" alt="{e(alt or c["name"] + " 프로필 사진")}" loading="lazy">'
            f'<span class="cv-cap" aria-hidden="true">TEAM UNSILENT · DJ {c["no"]}</span>'
            f'</div>')
