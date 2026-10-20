"""사이트 문구 추출기 — 텍스트 수정 보드(아티팩트)에 넣을 목록을 만든다.

index.html과 dj/*.html에서 화면에 보이는 문구, 이미지 설명(alt), 입력 안내(placeholder),
검색·공유 문구(meta)를 섹션별로 뽑아 JSON으로 낸다. 같은 문구가 여러 곳에 있으면 하나로 묶는다.

    python3 tools/copy_extract.py > copy.json
"""
from __future__ import annotations

import hashlib
import json
import re
import pathlib
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent

# 이 태그 안의 글은 한 덩어리로 본다 (em·br 등 인라인은 부모에 붙인다)
SEG = {"title", "h1", "h2", "h3", "p", "li", "b", "small", "span", "dt", "dd", "th", "td",
       "figcaption", "button", "a", "label", "option", "time", "strong", "div"}
SKIP = {"script", "style", "svg", "canvas"}
VOID = {"br", "img", "input", "meta", "link", "source", "hr"}

INDEX_SEC = {"top": "히어로", "night": "그날 밤", "why": "소개", "vol": "공연 방식", "djs": "DJ",
             "live": "현장 영상", "rec": "실적·언론", "setup": "구성", "contact": "진행·섭외 문의"}
KIND = {"title": "탭 제목", "h1": "큰 제목", "h2": "제목", "h3": "소제목", "p": "문단", "li": "목록",
        "b": "굵은 글", "small": "작은 글", "span": "글", "dt": "항목명", "dd": "항목 내용", "th": "표 머리",
        "td": "표 칸", "figcaption": "사진 설명", "button": "버튼", "a": "링크", "label": "입력 이름",
        "option": "선택지", "time": "시각", "strong": "굵은 글", "div": "글"}


class Extract(HTMLParser):
    def __init__(self, page: str, sec_map: dict[str, str] | None, default_sec: str):
        super().__init__(convert_charrefs=True)
        self.page, self.sec_map, self.sec = page, sec_map, default_sec
        self.stack: list[str] = []          # 열린 태그
        self.skip = 0
        self.buf: list[str] = []            # 현재 덩어리
        self.buf_tag = ""
        self.out: list[dict] = []

    def flush(self):
        text = "".join(self.buf).strip()
        text = "\n".join(" ".join(line.split()) for line in text.split("\n")).strip()
        if text:
            self.add(text, KIND.get(self.buf_tag, "글"))
        self.buf, self.buf_tag = [], ""

    def add(self, text: str, kind: str):
        self.out.append({"page": self.page, "sec": self.sec, "kind": kind, "text": text})

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in SKIP:
            self.skip += 1
        if self.skip:
            if tag not in VOID:
                self.stack.append(tag)
            return
        if self.sec_map is not None and tag in ("section", "header", "footer", "article"):
            if a.get("id") in self.sec_map:
                self.sec = self.sec_map[a["id"]]
            elif tag == "footer":
                self.sec = "푸터"
            elif tag == "header" and ("nav" in (a.get("class") or "") or "top" in (a.get("class") or "")):
                self.sec = "상단 메뉴"
        if tag == "meta" and a.get("content") and (a.get("name") == "description" or a.get("property", "").startswith("og:")):
            if a.get("property") not in ("og:image", "og:type", "og:locale"):
                self.out.append({"page": self.page, "sec": "검색·공유 문구", "kind": a.get("name") or a.get("property"), "text": a["content"]})
            return
        if tag == "br":
            self.buf.append("\n")
            return
        if tag in SEG:
            self.flush()
            self.buf_tag = tag
        for k, kind in (("alt", "이미지 설명"), ("placeholder", "입력 안내"), ("data-cap", "사진 설명")):
            if a.get(k):
                self.add(a[k], kind)
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        while self.stack:
            t = self.stack.pop()
            if t in SKIP:
                self.skip -= 1
            if t == tag:
                break
        if self.skip:
            return
        if tag in SEG:
            self.flush()
            # 바깥 덩어리로 돌아간다
            for t in reversed(self.stack):
                if t in SEG:
                    self.buf_tag = t
                    break

    def handle_data(self, data):
        if self.skip:
            return
        if not self.buf_tag:
            for t in reversed(self.stack):
                if t in SEG:
                    self.buf_tag = t
                    break
        self.buf.append(data)


def run() -> list[dict]:
    rows: list[dict] = []
    p = Extract("홈", INDEX_SEC, "검색·공유 문구")
    p.feed((ROOT / "index.html").read_text(encoding="utf-8")); p.flush()
    rows += p.out
    for f, name in (("dr-ktrl", "DR.KTRL"), ("lify", "LiFY"), ("kali", "KALI")):
        p = Extract(f"{name} 프레스킷", None, f"{name} 프레스킷")
        p.feed((ROOT / "dj" / f"{f}.html").read_text(encoding="utf-8")); p.flush()
        rows += p.out
    # 같은 문구는 하나로, 나온 곳을 모두 적는다
    items: dict[str, dict] = {}
    for r in rows:
        # 시계 숫자처럼 화면에서 바뀌는 조각은 뺀다
        if r["text"] in {"↗", "→", "●", "*", ":"} or re.fullmatch(r"\d{1,2}", r["text"]):
            continue
        k = hashlib.sha1(r["text"].encode()).hexdigest()[:10]
        it = items.setdefault(k, {"id": k, "text": r["text"], "sec": r["page"] if r["page"] != "홈" else r["sec"], "kind": r["kind"], "n": 0})
        it["n"] += 1
    return list(items.values())


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=0))
