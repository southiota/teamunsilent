"""팀 언사일런트 사진 톤 보정 (톤 레시피 v1, 기준: brand/design.md "사진 톤").

원본은 건드리지 않고 out 폴더에 .jpg + .webp 로 저장한다. EXIF(촬영 위치 등)는 지운다.

    .venv/bin/python tools/grade.py <입력 파일 또는 폴더...> -o img/graded [--long 2000] [--strength 1.0]
"""
from __future__ import annotations

import argparse
import pathlib

import numpy as np
from PIL import Image, ImageOps

# brand/design.md 컬러 토큰
INK = np.array([0x1A, 0x28, 0x28]) / 255    # 그림자가 향하는 색
PAPER = np.array([0xF4, 0xF7, 0xEF]) / 255  # 하이라이트 상한
LIME = np.array([0xC2, 0xEA, 0x8C]) / 255   # 하이라이트에 아주 약하게

# 톤 레시피 v1 — 값을 바꾸면 design.md 표도 같이 바꾼다
SATURATION = 0.82      # 채도
CONTRAST = 0.32        # S커브 세기
SHADOW_TINT = 0.45     # 그림자를 ink 쪽으로 끌어오는 정도
HIGHLIGHT_TINT = 0.05  # 하이라이트에 lime을 섞는 정도
BLACK_LIFT = 0.5       # 0이면 순흑, 1이면 가장 어두운 곳이 ink

# 자동 맞춤 — 사진마다 다른 노출·색온도를 레시피 전에 고르게 한다
WB_AMOUNT = 0.5             # 중간톤 회색 기준 화이트밸런스, 절반만
WB_GAIN = (0.88, 1.12)      # 채널 배율 한도
TARGET_MID = 0.32           # 중간 밝기 목표 (야간 공연 기준)
GAMMA_RANGE = (0.8, 1.25)   # 노출 보정 한도
LEVELS = (0.5, 99.9)        # 자동 레벨 퍼센타일

EXTS = {".jpg", ".jpeg", ".png", ".webp"}
Y = np.array([0.2126, 0.7152, 0.0722])


def normalize(src: np.ndarray, mask: np.ndarray | None = None) -> np.ndarray:
    if mask is None:
        mask = np.ones(src.shape[:2], bool)  # 누끼는 인물 영역만 보고 맞춘다
    lo, hi = np.percentile((src @ Y)[mask], LEVELS)
    x = np.clip((src - lo) / max(hi - lo, 1e-3), 0, 1) * 0.5 + src * 0.5

    l = x @ Y
    mid = (l > 0.15) & (l < 0.85) & mask
    if mid.sum() > 1000:
        mean = x[mid].mean(axis=0)
        gain = np.clip(mean.mean() / np.maximum(mean, 1e-3), *WB_GAIN)
        x = np.clip(x * (1 + (gain - 1) * WB_AMOUNT), 0, 1)

    l = x @ Y
    gamma = np.clip(np.log(TARGET_MID) / np.log(np.clip(np.median(l[mask]), 0.02, 0.98)), *GAMMA_RANGE)
    if (l[mask] > 0.85).mean() > 0.04:  # 조명·하늘이 넓으면 밝게 올리지 않는다
        gamma = max(gamma, 1.0)
    return x ** gamma


def grade(img: Image.Image, strength: float) -> Image.Image:
    src = np.asarray(img.convert("RGB"), dtype=np.float32) / 255
    mask = np.asarray(img.convert("RGBA").getchannel("A")) > 128 if "A" in img.getbands() else None
    base = normalize(src, mask)
    luma = (base @ Y)[..., None]

    x = luma + (base - luma) * SATURATION
    x = x + CONTRAST * (x - 0.5) * (1 - np.abs(2 * x - 1))  # 중간톤만 미는 S커브
    l = (x @ np.array([0.2126, 0.7152, 0.0722]))[..., None]

    shadow = (1 - l) ** 3  # 중간톤(피부)은 거의 건드리지 않는다
    x = x + (INK - x) * SHADOW_TINT * shadow
    x = x + (LIME - x) * HIGHLIGHT_TINT * l ** 2
    x = INK * BLACK_LIFT + x * (PAPER - INK * BLACK_LIFT)  # 검정은 ink로, 흰색은 paper로

    out = src + (np.clip(x, 0, 1) - src) * strength
    return Image.fromarray((out * 255 + 0.5).astype(np.uint8))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", nargs="+")
    ap.add_argument("-o", "--out", required=True)
    ap.add_argument("--long", type=int, default=2000, help="긴 변 px")
    ap.add_argument("--strength", type=float, default=1.0, help="0~1, 원본과 섞는 비율")
    a = ap.parse_args()

    files = []
    for p in map(pathlib.Path, a.inputs):
        files += sorted(f for f in p.rglob("*") if f.suffix.lower() in EXTS) if p.is_dir() else [p]
    out = pathlib.Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    for f in files:
        img = ImageOps.exif_transpose(Image.open(f))
        img.thumbnail((a.long, a.long), Image.LANCZOS)
        g = grade(img, a.strength)
        if "A" in img.getbands():
            # 누끼: 알파는 그대로 두고 색만 보정한다
            g.putalpha(img.convert("RGBA").getchannel("A"))
            g.save(out / f"{f.stem}.png", optimize=True)
            g.save(out / f"{f.stem}.webp", quality=82, method=6)
            print(f"{f} -> {out / f.stem}.png/.webp (alpha)")
            continue
        g.save(out / f"{f.stem}.jpg", quality=82, optimize=True, progressive=True)
        g.save(out / f"{f.stem}.webp", quality=80, method=6)
        print(f"{f} -> {out / f.stem}.jpg/.webp")


if __name__ == "__main__":
    main()
