---
description: Convert all PDF course materials (lectures, textbook, homework, solutions) to markdown. Lecture slides go through the vision pipeline (parallel agents + LaTeX transcription); prose through pdfplumber; scanned through OCR. Idempotent — skips already-converted files.
argument-hint: [--force to reconvert everything]
---

Load `skills/pdf/SKILL.md`, `skills/pdf/VISION.md`, and `skills/course-builder/SKILL.md`.

Arguments: $ARGUMENTS

## Routing rule

For each source PDF, choose the extraction method by looking at the file's category and its digital-text behavior:

| Source | Method | Why |
|---|---|---|
| `materials/lectures/*.pdf` | **Vision pipeline** (default) | Lecture slides are math-heavy and multi-column. pdfplumber reliably word-salads equations. |
| `materials/textbook/*.pdf` | pdfplumber | Textbook chapters are prose-heavy single-column; pdfplumber handles them well. |
| `materials/homework/*.pdf`, `materials/solutions/*.pdf` | pdfplumber first; fall back to vision if output looks like word-salad | HW problem sets are usually prose + a few equations. Worth trying the cheap path first. |
| Any PDF with empty/garbage digital text | pytesseract + pdf2image (OCR) | Scanned printed material — no digital layer to extract. |
| Any `.md` in `materials/` | Copy-through | Already markdown; just mirror into `converted/` with a provenance comment. |

**Sanity-check pdfplumber output before accepting.** Spot-check one converted page: if equations read like `ℏ ∂ p2 ℏ 2 ∂ 2 p ̂` instead of coherent LaTeX, delete that output and re-run through the vision pipeline (Step 3 below).

## Procedure

### Step 1 — Discovery

Scan `materials/` recursively for `.pdf` and `.md`. Classify by subfolder: `lectures`, `textbook`, `homework`, `solutions`. Ambiguous files (PDFs sitting in `materials/` root) get one prompt to categorize.

Apply idempotence: if `converted/<cat>/<stem>.md` exists and is newer than the source, skip — unless `--force` is in `$ARGUMENTS`. Log skip count.

### Step 2 — Prose-heavy sources (textbook + most homework/solutions)

Run digital extraction via `pdfplumber`:

```python
import pdfplumber
with pdfplumber.open(src) as pdf:
    pages = [p.extract_text() or "" for p in pdf.pages]
text = "\n\n---\n\n".join(pages)
```

Write to `converted/<cat>/<stem>.md` with provenance header:

```
<!-- SOURCE: materials/<cat>/<stem>.pdf, extracted <YYYY-MM-DD>, method: pdfplumber -->
```

If the extracted text is empty or near-empty (<50 chars/page avg), the PDF is scanned — fall through to OCR (Step 4).

### Step 3 — Math-heavy lecture slides (vision pipeline)

This is the default path for `materials/lectures/*.pdf`, and the fallback path for any other PDF whose pdfplumber output was word-salad. Full details in `skills/pdf/VISION.md`; the three non-negotiable steps are:

**3a. Render all pages to PNG at dpi=160.**

```python
from pdf2image import convert_from_path
from pathlib import Path

for pdf_path in lecture_pdfs:
    stem = pdf_path.stem
    out = Path(f"converted/lectures/_pages/{stem}")
    out.mkdir(parents=True, exist_ok=True)
    for i, im in enumerate(convert_from_path(str(pdf_path), dpi=160), 1):
        im.save(out / f"p{i:02d}.png", "PNG", optimize=True)
```

**3b. Resize every PNG to ≤1800 px long edge BEFORE any agent starts.**

```python
from PIL import Image

MAX = 1800
for png in Path("converted/lectures/_pages").rglob("*.png"):
    im = Image.open(png); w, h = im.size
    if max(w, h) <= MAX:
        continue
    scale = MAX / max(w, h)
    im.resize((int(w*scale), int(h*scale)), Image.LANCZOS).save(png, "PNG", optimize=True)
```

This is **not optional.** Claude's many-image requests hard-reject images >2000 px on the long edge; 16:9 slides at dpi=160 produce ~4267×2400 PNGs that blow past that. Any agent that started reading before the resize ran will have already captured the oversized image into its context — its whole run wastes.

**3c. Spawn one `general-purpose` agent per PDF, in parallel, backgrounded.** Each agent touches only its own file's `_pages/<stem>/` directory so writes don't race.

Use this prompt template for each agent (fill in the bracketed values):

```
You are re-extracting a <domain> lecture PDF that pdfplumber mangled
(it split equations across lines and interleaved columns). Use vision
to read each rendered page and write clean markdown.

Input: page images at <abs_path>/_pages/<stem>/p01.png through pNN.png
       (NN pages). Images are ≤1800px on the long edge.
Output: overwrite <abs_path>/<stem>.md

Procedure:
1. Read each page image with the Read tool — one at a time, not in
   parallel batches, to stay under the per-request image-dimension budget.
   After reading and transcribing a page, move to the next.
2. Transcribe each page into markdown, preserving the slide's reading
   order (not raw column order).
3. Format math in LaTeX: inline $...$, display $$...$$. Render hats,
   hbars, partials, bras/kets, sums, vectors, operators faithfully.
   If a symbol is genuinely unreadable, write [?] — do not guess.
4. Use ## for slide titles. Prepend ### Page N anchors so downstream
   tools can cite pages.
5. Preserve bullet hierarchy, numbered postulates/theorems/definitions,
   labeled equations, tables.
6. Skip-mark truly empty pages as *[blank]*.
7. Do NOT summarize — faithfully transcribe only what's on the slide.
8. For heavy diagrams, write one italic line *Figure: [description]*.

Top of file must be:
<!-- SOURCE: materials/<cat>/<stem>.pdf, extracted <YYYY-MM-DD>, method: vision -->

# <Title>

Write the full file once at the end. Report: page count handled and
any [?] symbols you marked.
```

`<domain>` should be whatever the course is about (quantum mechanics, linear algebra, discrete math, E&M, etc.) — infer from the materials or ask the user once if unclear. Sequential Read inside the agent is non-negotiable; parallel batches of Read tool calls trip the many-image dimension limit again even though each individual PNG is under the ceiling.

Wait for all agents to report done. Then spot-check one or two output files (equations should read top-to-bottom as coherent LaTeX) before moving on.

### Step 4 — Scanned printed PDFs (OCR)

```python
import pytesseract
from pdf2image import convert_from_path

images = convert_from_path(src, dpi=200)
text = "\n\n".join(
    f"## Page {i+1}\n\n" + pytesseract.image_to_string(im, lang="eng+kor")
    for i, im in enumerate(images)
)
```

Write `converted/<cat>/<stem>.md` with provenance:

```
<!-- SOURCE: materials/<cat>/<stem>.pdf, extracted <YYYY-MM-DD>, method: ocr, accuracy may vary. Verify math expressions manually. -->
```

### Step 5 — Copy-through for `.md` sources

For each `.md` already in `materials/`: mirror to `converted/<cat>/<stem>.md` verbatim, adding:

```
<!-- SOURCE: materials/<cat>/<stem>.md, copied <YYYY-MM-DD>, method: passthrough -->
```

### Step 6 — Cleanup

After all vision agents finish and outputs look sane, delete the `_pages/` scratch directory:

```bash
rm -rf converted/*/_pages
```

These are ~5–25 MB per lecture and have no downstream use. Keep them only if you plan to re-run immediately.

## Summary output

After ingest completes, print:

| Category | Converted | Skipped (already done) | Vision | OCR'd |
|---|---|---|---|---|
| lectures | N | M | V | K |
| textbook | ... | ... | ... | ... |
| homework | ... | ... | ... | ... |
| solutions | ... | ... | ... | ... |

End with:
"다음 단계: `/paideia:analyze`로 patterns.md, coverage.md, summary.md를 생성하세요."

If any file failed (encryption, corrupted PDF, agent timeout), list at the end with the specific failure reason and suggested workaround (e.g., `qpdf --decrypt` for password-protected PDFs; re-run `/paideia:ingest --force` if a vision agent crashed mid-run).
