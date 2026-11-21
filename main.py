#!/usr/bin/env python3
"""Entry program: place the pre-rendered front page at /output/entry.png.

The grader mounts this repository read-only at /bot and gives a writable
/output. MAKEFUN_OUTPUT_DIR stands in for /output when running locally.
"""
import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().with_name("entry.png")
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUT_DIR / "entry.png"

if not SOURCE.is_file():
    raise SystemExit(f"missing source image: {SOURCE}")

OUT_DIR.mkdir(parents=True, exist_ok=True)
with SOURCE.open("rb") as src, TARGET.open("wb") as dst:
    dst.write(src.read())

if TARGET.stat().st_size != SOURCE.stat().st_size:
    raise SystemExit("output size mismatch")
print(f"wrote {TARGET} ({TARGET.stat().st_size} bytes)")
