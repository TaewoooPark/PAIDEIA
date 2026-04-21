---
name: vision-ocr
description: Use whenever a hand-written or scanned answer PDF needs transcription to markdown for /grade. Runs Qwen3-VL 8B locally via ollama to produce clean MD+LaTeX from hand-written Korean prose + math, with pytesseract fallback if the VLM is unavailable. Replaces the old pytesseract-only path in the answer-processing skill.
---

# Vision-OCR

## When to load

- `/grade` needs to convert `answers/*.pdf` → `answers/converted/*.md`
- Any hand-written / scanned document whose previous pytesseract pass was garbled
- `answer-processing` skill's step-2 conversion

## Pipeline (tiered)

```
answers/<name>.pdf
  ↓ pdf2image @ 300dpi
  ↓ resize to ≤1600px wide (VLMs dislike huge inputs)
  ↓ base64 JPEG per page
  ↓ [Tier 1] ollama qwen3-vl:8b
  ↓ (on timeout / ollama down)
  ↓ [Tier 2] pytesseract (eng+kor)
answers/converted/<name>.md
```

Tier header is written into the file so `/grade` knows the confidence level:

```markdown
<!-- SOURCE: ..., qwen3-vl:8b @ 300dpi, N pages -->
```
or (fallback)
```markdown
<!-- TIER: tesseract fallback -->
```

## Entrypoint

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/vision_ocr.py" <input.pdf> <output.md>
```

`${CLAUDE_PLUGIN_ROOT}/scripts/vision_ocr.py` is the single source of truth. It:
1. Warms up the VLM with a 1-token `/api/generate` so the first real page isn't stalled by model load.
2. Sends each page as a JPEG-encoded base64 image with a Korean-aware, LaTeX-first prompt.
3. Sets `keep_alive: "15m"` so the model stays in memory across pages within a session.
4. On any exception (timeout, connection refused) falls back to pytesseract and marks the file.

## Prompt contract (must preserve)

The prompt tells the VLM to:
- Keep Korean prose as Korean
- Emit math as `$...$` / `$$...$$`
- Preserve problem numbering (P1, (1), (a), ...)
- NOT grade or interpret — just transcribe
- Write `[?]` for ambiguous glyphs instead of guessing
- Skip crossed-out work
- Return markdown only, no `<think>`, no commentary

If you edit the prompt, keep these six clauses — they're what separates useful transcription from hallucination.

## Dependencies

Already installed on this machine:
- `ollama` CLI + model `qwen3-vl:8b` (6.1 GB, pulled via `ollama pull qwen3-vl:8b`)
- Python: `pdf2image`, `pytesseract`, `pillow` (stdlib covers the rest)

If ollama is missing: `brew install ollama && ollama serve &` then `ollama pull qwen3-vl:8b`.

## Performance notes

- Mac M-series: first page ~2–5 min (model load + decode); subsequent pages ~20–60 s.
- A 2-page hand-written answer typically takes 3–7 min total.
- 300dpi input is downscaled to 1600px before encoding — keeps the base64 payload under ~500 KB.

## Failure modes + fixes

| Symptom | Cause | Fix |
|---|---|---|
| `timed out` on page 1 | first-load stall on cold ollama | re-run; warmup + `keep_alive` should help on 2nd try |
| empty response / `<think>...` leaks | prompt contract violated | re-check prompt; add "Return ONLY markdown, no <think>" |
| base64 error / 413 | image too large | drop `MAX_IMG_WIDTH` from 1600 → 1200 |
| ollama 404 | `qwen3-vl:8b` not pulled | `ollama pull qwen3-vl:8b` |
| tesseract fallback kept firing | ollama server not running | `ollama serve &` |

## Anti-patterns

- ❌ Don't pass base64 via `curl -d <arg>` — ARG_MAX overflow. Use stdlib `urllib` with POST body.
- ❌ Don't send PNG — JPEG q=90 is 5–10× smaller with no impact on VLM accuracy.
- ❌ Don't ask the VLM to grade or solve. That's `/grade`'s job; OCR must stay pure transcription.
- ❌ Don't trust the fallback tier silently — the file comment tells `/grade` to caveat its verdict.

## Integration

- Called by `/grade` via `answer-processing` skill step 2
- Called by `/ingest` (future) for hand-written lecture notes, if any appear in `materials/`
- Writes to `answers/converted/` only; does not modify originals in `answers/`
