"""
Vision-OCR pipeline for hand-written math answer PDFs.

Tier 1: local Qwen3-VL 8B via ollama (fast, free, Mac-friendly).
Tier 2: fallback to pytesseract + pdf2image (existing pipeline).

Usage:
    python scripts/vision_ocr.py <input.pdf> <output.md>
    python scripts/vision_ocr.py answers/foo.pdf answers/converted/foo.md
"""

import base64
import io
import json
import sys
import urllib.request
from pathlib import Path

from pdf2image import convert_from_path

OLLAMA_MODEL = "qwen3-vl:8b"
DPI = 300
MAX_IMG_WIDTH = 1200
PER_PAGE_TIMEOUT = 1800
MAX_TOKENS = 6000

PROMPT = """You are transcribing a hand-written student answer for a Discrete Mathematics exam.

Rules:
- Korean prose stays as Korean prose.
- Math expressions must become LaTeX: $...$ inline, $$...$$ display.
- Preserve problem numbering (P1, P2, (1), (2), (a), (b), etc.).
- Do NOT interpret or grade. Just transcribe what is written.
- If a symbol is ambiguous, write [?] instead of guessing.
- If a page has crossed-out work, ignore the strikethrough content.
- Return ONLY markdown, no commentary, no <think>.
"""


def image_to_b64(img) -> str:
    if img.width > MAX_IMG_WIDTH:
        ratio = MAX_IMG_WIDTH / img.width
        img = img.resize((MAX_IMG_WIDTH, int(img.height * ratio)))
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=90)
    return base64.b64encode(buf.getvalue()).decode()


def warmup_ollama() -> None:
    """Load the model into memory with a tiny request so the first real page isn't stalled."""
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": "ping",
        "stream": False,
        "keep_alive": "15m",
        "options": {"num_predict": 1},
    }
    req = urllib.request.Request(
        "http://localhost:11434/api/generate",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=PER_PAGE_TIMEOUT) as resp:
        resp.read()


def call_ollama_vision(img_b64: str) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": PROMPT,
        "images": [img_b64],
        "stream": False,
        "think": False,
        "keep_alive": "15m",
        "options": {
            "temperature": 0.1,
            "num_ctx": 4096,
            "num_predict": MAX_TOKENS,
            "repeat_penalty": 1.3,
            "repeat_last_n": 256,
        },
    }
    req = urllib.request.Request(
        "http://localhost:11434/api/generate",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=PER_PAGE_TIMEOUT) as resp:
        body = resp.read().decode()
    response = json.loads(body)
    # Qwen3-VL routes raw output to `thinking` when its internal reasoning mode
    # never closes. Fall back to that field so we don't lose the transcription.
    text = response.get("response", "") or response.get("thinking", "")
    text = text.replace("<think>", "").replace("</think>", "").strip()
    return dedupe_loops(text)


def dedupe_loops(text: str) -> str:
    """Qwen3 thinking mode loops on 'Wait, the image shows: ... <same block>'.
    Split into sentences, drop near-duplicates and self-doubt sentences."""
    import re
    sentences = re.split(r'(?<=[.?!])\s+', text)
    kept: list[str] = []
    seen: set[str] = set()
    for s in sentences:
        s = s.strip()
        if not s:
            continue
        lower = s.lower()
        if lower.startswith(("wait,", "wait.", "hmm,", "actually,", "but the hand-written", "the image shows", "the image has", "got it", "let's check", "let's look")):
            continue
        key = re.sub(r'\s+', ' ', s[:100])
        if key in seen:
            continue
        seen.add(key)
        kept.append(s)
    return " ".join(kept)


def tesseract_fallback(images) -> str:
    import pytesseract
    out = ""
    for i, img in enumerate(images):
        text = pytesseract.image_to_string(img, lang="eng+kor")
        out += f"## Page {i+1}\n\n{text}\n\n"
    return out


def ocr_pdf(pdf_path: Path, out_path: Path) -> None:
    images = convert_from_path(str(pdf_path), dpi=DPI)
    header = (
        f"# Vision-OCR transcription\n\n"
        f"<!-- SOURCE: {pdf_path.name}, "
        f"{OLLAMA_MODEL} @ {DPI}dpi, {len(images)} pages -->\n\n"
    )

    try:
        sys.stderr.write(f"[vision-ocr] warming up {OLLAMA_MODEL} ...\n")
        warmup_ollama()
        pages_md = []
        for i, img in enumerate(images):
            sys.stderr.write(f"[vision-ocr] page {i+1}/{len(images)} ...\n")
            sys.stderr.flush()
            b64 = image_to_b64(img)
            md = call_ollama_vision(b64)
            pages_md.append(f"## Page {i+1}\n\n{md}\n")
        body = "\n".join(pages_md)
    except Exception as e:
        sys.stderr.write(f"[vision-ocr] vision tier failed: {e}\n")
        sys.stderr.write("[vision-ocr] falling back to tesseract...\n")
        body = "<!-- TIER: tesseract fallback -->\n\n" + tesseract_fallback(images)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(header + body)
    sys.stderr.write(f"[vision-ocr] wrote {out_path} ({len(header+body)} chars)\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python scripts/vision_ocr.py <input.pdf> <output.md>", file=sys.stderr)
        sys.exit(2)
    ocr_pdf(Path(sys.argv[1]), Path(sys.argv[2]))
