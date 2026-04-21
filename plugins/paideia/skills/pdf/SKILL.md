---
name: pdf
description: Use whenever the user works with PDF files — reading/extracting text from PDFs (lecture notes, textbook chapters, HW problems, HW solutions, hand-written answers), converting PDFs to markdown for downstream analysis, merging/splitting PDFs, or creating PDFs. For scanned or hand-written PDFs, OCR is required (pytesseract + pdf2image). Based on Anthropic's official PDF skill (github.com/anthropics/skills/tree/main/skills/pdf).
license: Proprietary (Anthropic). Condensed excerpt; see LICENSE in anthropics/skills.
---

# PDF Processing Guide

## When to use this skill

Load this skill whenever the workflow involves PDF input or output. In the paideia context specifically:
- Converting `materials/**/*.pdf` to markdown in `converted/**/*.md` (via `/ingest`)
- Converting hand-written answer PDFs in `answers/*.pdf` to markdown in `answers/converted/*.md` (via `/grade`)
- OCR for scanned lecture notes, textbook chapters, or hand-written work

## Quick decision tree

```
What kind of PDF?
├─ Course material (materials/**/*.pdf)  → VISION pipeline (see VISION.md)
│                                          pdfplumber is unreliable on course
│                                          content — even "prose-heavy"
│                                          textbook pages mix in equations,
│                                          figures, and multi-column layouts
│                                          that break digital extraction
│                                          silently. We route everything
│                                          through vision instead of
│                                          maintaining a per-category heuristic.
├─ Hand-written answer PDF              → vision-ocr skill (see vision-ocr/)
└─ Arbitrary outside-the-plugin PDF     → pdfplumber / pypdf / pytesseract
                                          per the sections below, case-by-case
```

Within this plugin, `/paideia:ingest` routes **all** `materials/**/*.pdf` through the vision pipeline. The `pdfplumber` / `pypdf` / `pytesseract` blocks below remain for reference and for ad-hoc PDF work outside the ingest flow (e.g., quick text dumps, PDF merge/split, producing the cheatsheet PDF).

## Core operations

### Text extraction (digital PDF)

```python
import pdfplumber

with pdfplumber.open("input.pdf") as pdf:
    text_by_page = []
    for page in pdf.pages:
        text_by_page.append(page.extract_text() or "")
full_text = "\n\n---\n\n".join(text_by_page)
```

Simpler alternative using pypdf:
```python
from pypdf import PdfReader
reader = PdfReader("input.pdf")
full_text = "\n\n".join(p.extract_text() or "" for p in reader.pages)
```

### OCR (scanned or hand-written PDF)

Install deps once:
```bash
pip install --break-system-packages pytesseract pdf2image
# Also needs system tesseract: apt-get install tesseract-ocr poppler-utils
```

```python
import pytesseract
from pdf2image import convert_from_path

images = convert_from_path("scanned.pdf", dpi=200)
text = ""
for i, image in enumerate(images):
    text += f"\n\n## Page {i+1}\n\n"
    text += pytesseract.image_to_string(image, lang="eng+kor")  # multi-lang
```

For best OCR quality on math/physics hand-writing, use `dpi=300` and consider preprocessing (deskew, binarize) with opencv before OCR.

### Command-line text extraction (fast path)

```bash
# Requires: apt-get install poppler-utils
pdftotext -layout input.pdf output.txt
```

### Merge / split

```python
from pypdf import PdfReader, PdfWriter

# Merge
writer = PdfWriter()
for f in ["chap1.pdf", "chap2.pdf"]:
    for page in PdfReader(f).pages:
        writer.add_page(page)
with open("merged.pdf", "wb") as out:
    writer.write(out)

# Split single page
reader = PdfReader("input.pdf")
for i, page in enumerate(reader.pages):
    w = PdfWriter()
    w.add_page(page)
    with open(f"page_{i+1}.pdf", "wb") as out:
        w.write(out)
```

### PDF creation (for producing clean cheatsheets)

```python
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("output.pdf", pagesize=letter)
styles = getSampleStyleSheet()
story = [Paragraph("Title", styles['Title']), Spacer(1, 12)]
# Use <sub> and <super> tags, NEVER Unicode subscripts (they render as black boxes)
story.append(Paragraph("H<sub>2</sub>O and E = mc<super>2</super>", styles['Normal']))
doc.build(story)
```

## Course-cram specific conventions

When converting PDF materials to markdown for this project:

1. **Preserve structure.** Section headers (`##`), numbered lists, tables. Do NOT reflow paragraphs — keep line breaks roughly aligned with source for verifiability.

2. **Math formatting.** Convert inline math to `$...$`, display math to `$$...$$`. If extraction produces garbled LaTeX, mark with `[?]` and move on — don't guess.

3. **Name convention.** `materials/lectures/chapter03.pdf` → `converted/lectures/chapter03.md`. Preserve subfolder structure.

4. **Provenance markers.** Prepend the output file with a source comment tagging the extraction method:
   ```
   <!-- SOURCE: materials/<cat>/<stem>.pdf, extracted <YYYY-MM-DD>, method: pdfplumber|vision|ocr -->
   ```
   For OCR specifically, append: `accuracy may vary. Verify math expressions manually.`

5. **Idempotence.** If `converted/X.md` already exists and is newer than `materials/X.pdf`, skip (unless user passes `--force`).

6. **Default route for all `materials/**/*.pdf`** is the vision pipeline (see `VISION.md`). `pdfplumber` was tried as a fast path for prose-heavy material and proved unreliable in practice — even textbook pages silently word-salad when they mix equations, multi-column layouts, or figure captions. Uniform vision routing is simpler and more reliable than per-category heuristics with fallbacks.

7. **Hand-written answer PDFs.** Output to `answers/converted/<name>.md`. Expect garbled math; the grading step handles ambiguity via strategy-matching, not exact algebra.

## Error patterns to watch for

- **Empty extracted text** (`page.extract_text()` returns `""`) → it's scanned. Fall through to OCR.
- **Unicode subscript/superscript in reportlab** → renders as solid black boxes. Use `<sub>`/`<super>` XML tags instead.
- **Protected PDFs** → `qpdf --password=... --decrypt in.pdf out.pdf` first.
- **Multi-column academic PDFs** → pdfplumber's default extraction interleaves columns. Use `page.extract_text(layout=True)` or crop bboxes per column.
- **Image-heavy scans** → `convert_from_path` uses a lot of memory. Set `dpi=150` for first pass, re-run at 300 only if OCR quality is poor.

## Dependencies

Standard install for paideia use:
```bash
pip install --break-system-packages pypdf pdfplumber pytesseract pdf2image reportlab
apt-get install -y poppler-utils tesseract-ocr tesseract-ocr-kor
```

The Korean language pack (`tesseract-ocr-kor`) is needed if the user writes solutions in Korean/Hangul.

## Reference

Full skill at https://github.com/anthropics/skills/tree/main/skills/pdf with REFERENCE.md covering pypdfium2, JavaScript libraries, and FORMS.md covering PDF form filling.
