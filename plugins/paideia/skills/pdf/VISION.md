# Vision-based PDF extraction (for math-heavy slides)

Supplemental to `SKILL.md`. Use this method when `pdfplumber` mangles the source — typically lecture slide decks with multi-column layout, heavy equations, and inline math where tokens end up split across lines or interleaved across columns.

This pipeline is what `/paideia:ingest` uses for `materials/lectures/*.pdf` by default, and what it falls back to for any other PDF whose digital extraction produced word-salad.

## When to use

Symptoms that `pdfplumber` has failed:
- Equations fragmented: operators on one line, operands on the next
- Variables and subscripts on separate lines
- Two-column slide content interleaved into alternating rows
- Greek letters preserved but structure (fractions, integrals, bras/kets, sums, vectors) lost
- Markdown looks like bag-of-tokens despite the PDF being "digital"

If the output reads like English prose with a few formula hiccups, stay with `pdfplumber`. If the output reads like a bag-of-tokens dump, switch to vision.

## Pipeline

```
materials/<cat>/X.pdf
    ├─(pdf2image, dpi=160)→  converted/<cat>/_pages/X/p01..pNN.png
    ├─(PIL resize, ≤1800px)→ (in-place)
    └─(parallel Agent per file, vision Read of PNGs)→ converted/<cat>/X.md
```

One agent per PDF, spawned in parallel. Each agent handles only its own file's page images — no cross-file writes — so they don't step on each other. For a 13-lecture course this gives ~4–7 min wall time instead of hours of serial work.

## Step 1 — Render pages to PNG

```python
from pdf2image import convert_from_path
from pathlib import Path

imgs = convert_from_path("materials/lectures/Lecture1.pdf", dpi=160)
out = Path("converted/lectures/_pages/Lecture1"); out.mkdir(parents=True, exist_ok=True)
for i, im in enumerate(imgs, 1):
    im.save(out / f"p{i:02d}.png", "PNG", optimize=True)
```

`dpi=160` is the sweet spot: readable math, reasonable file size. Lower and sub/superscripts blur; higher just burns disk.

## Step 2 — Enforce the 2000px ceiling

**Critical constraint.** Claude's many-image requests reject any image whose long edge exceeds ~2000 px with:

> An image in the conversation exceeds the dimension limit for many-image requests (2000px). Run /compact to remove old images from context, or start a new session.

Slide decks at `dpi=160` rendered from 16:9 PDFs routinely produce 4267×2400 PNGs, which blows past that. Downscale **before** any vision agent starts reading, to max 1800 px long edge (safety margin under 2000):

```python
from PIL import Image
from pathlib import Path

MAX = 1800
for png in Path("converted/lectures/_pages").rglob("*.png"):
    im = Image.open(png); w, h = im.size
    if max(w, h) <= MAX:
        continue
    scale = MAX / max(w, h)
    im.resize((int(w*scale), int(h*scale)), Image.LANCZOS).save(png, "PNG", optimize=True)
```

If an agent started before the resize ran, it will have already captured the oversized image into its context and the request dies on the way to the model — the whole agent-run wastes. **Resize first, agents second.**

## Step 3 — Parallel agents, one per file

Spawn a separate `general-purpose` agent per PDF, in parallel, backgrounded. Each agent handles only its own file's page images — no cross-file work — so they don't race on writes.

### Prompt template

```
You are re-extracting a <domain> lecture PDF that pdfplumber mangled
(it split equations across lines and interleaved columns). Use vision
to read each rendered page and write clean markdown.

Input: page images at <abs_path>/_pages/<stem>/p01.png through pNN.png
       (NN pages). Images are ≤1800px on the long edge.
Output: overwrite <abs_path>/<stem>.md

Procedure:
1. Read each page image with the Read tool — **one at a time**, not in
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
8. For heavy diagrams, write one italic line *Figure: [description]*
   rather than pixel-wise transcription.

Top of file must be:
<!-- SOURCE: materials/<cat>/<stem>.pdf, extracted <YYYY-MM-DD>, method: vision -->

# <Title>

Write the full file once at the end. Report: page count handled and
any [?] symbols you marked.
```

**Sequential read is non-negotiable.** Even though individual images are under the per-image ceiling, reading many in parallel batches the agent's request and trips the many-image dimension limit again. Instruct the agent explicitly to read → transcribe → next.

## Step 4 — Cleanup

After all agents report done and you've spot-checked the markdown, delete the `_pages/` scratch dir. These are ~5–25 MB per lecture; they have no downstream use.

```bash
rm -rf converted/lectures/_pages
```

Leave `_pages/` around only while a re-run is possible — once the markdown is verified, the PNGs are waste.

## Quality notes (from a real course run)

Validated on a 13-lecture Quantum Mechanics course, ~208 pages re-extracted:

- **0 `[?]` markers needed.** At `dpi=160` every equation, subscript, bra-ket, partial derivative, operator hat, and Greek letter was legible.
- Two of the initial agents failed on the oversized-image error because they started reading before the resize pass ran. Resizing preemptively avoided this for every subsequent run — hence Step 2 comes before Step 3.
- Output quality vs `pdfplumber`: equations render as `$$\hat H = -\frac{\hbar^2}{2m}\partial_x^2 + V(x)$$` instead of `ℏ ∂ p2 ℏ 2 ∂ 2 p ̂ =  H  = + V ( x )  Ĥ = − + V ( x )`. Night and day.
- Blank final pages are common (title separators, thank-you slides). Agents correctly mark them `*[blank]*`.

Equivalent wins are expected in any math/physics slide deck: linear algebra (matrices, tensor products), E&M (vector calculus, Maxwell's equations), statistical mechanics (partition functions, integrals), discrete math (summations, recurrences, binomial identities). The pipeline is domain-general — the prompt's `<domain>` placeholder is the only thing that changes.

## When NOT to use vision

- **Full textbook chapters** (hundreds of pages of single-column prose). `pdfplumber` handles prose fine, and vision at that scale is wasteful — both in wall time and in agent-context budget.
- **PDFs that are already scanned images** — use OCR (`pytesseract`) rather than vision; cheaper, and the text is printed so OCR is accurate.
- **Hand-written answer PDFs** — use the `vision-ocr` skill instead; it's tuned for that specifically (noisy ink, variable layouts, error-tolerant downstream grading).

## TL;DR

Math-heavy slide decks → render at `dpi=160` → resize all PNGs to ≤1800 px **before** any agent starts → one agent per deck in parallel → each agent reads images **sequentially** → clean LaTeX markdown out → `rm -rf _pages`.
