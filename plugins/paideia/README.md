# paideia (plugin)

Exam-formation plugin for math / physics / engineering courses. Local-first by construction — no SaaS, no cloud upload of your materials, no subscription.

See the repo root `README.md` for the full manifesto, install steps, and workflow walk-through.

## Quick reference

```
ingest ──▶ analyze ──▶ drill ──▶ grade ──▶ weakmap ──▶ cheatsheet
   ▲                                                        │
   └────────────────── feedback loop ───────────────────────┘
```

| Command | Purpose |
|---------|---------|
| `/paideia:init-course` | Bootstrap a fresh course folder (deps check, dir skeleton, metadata prompt, background `ollama pull`) |
| `/paideia:ingest` | PDFs → markdown (vision for math-heavy lectures, `pdfplumber` for prose, OCR for scans) |
| `/paideia:analyze` | Build `course-index/{summary,patterns,coverage}.md` |
| `/paideia:hwmap hot` | Surface 🔥🔥 Exam-primary sections ranked by HW density |
| `/paideia:pattern <§\|Pk\|keyword>` | Show pattern cards |
| `/paideia:derive <target>` | Clean reference derivation to `derivations/` |
| `/paideia:quiz <topic\|§\|weakmap> [N]` | N practice problems, answers hidden |
| `/paideia:blind <problem-id>` | Strategy-check on a known problem |
| `/paideia:twin <problem-id>` | Variant — same pattern, new surface |
| `/paideia:chain <N>` | Multi-pattern integration problem |
| `/paideia:mock <minutes>` | Full mock exam, HW-density weighted |
| `/paideia:grade [path]` | OCR answer PDF via local Qwen3-VL, strategy-grade |
| `/paideia:weakmap [concept]` | Priority-ranked weakness report |
| `/paideia:cheatsheet [--pdf]` | Error-driven one-pager |

## Dependencies

- `ollama` + `qwen3-vl:8b` (Tier-1 OCR — runs locally, ~6 GB model)
- `tesseract-ocr` + `poppler-utils` (Tier-2 OCR fallback)
- Python: `pypdf pdfplumber pytesseract pdf2image pillow reportlab`

All checked and offered for install by `/paideia:init-course`.
