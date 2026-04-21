---
description: Grade user's answer PDF (hand-written, scanned) against reference solution. Auto-converts PDF → MD via vision-ocr (Qwen3-VL local) with tesseract fallback, then strategy-based grade.
argument-hint: [optional: path to answer file; default = most recent in answers/]
---

Load `skills/vision-ocr/SKILL.md`, `skills/pdf/SKILL.md`, and `skills/answer-processing/SKILL.md`.

Target answer file: $ARGUMENTS

If no argument, find the most recently modified file in `answers/` (not `answers/converted/`).

Follow the answer-processing skill pipeline:

1. **Identify.** Is target a `.pdf` or `.md`?
   - `.pdf` → proceed to step 2
   - `.md` → skip step 2, go to 3

2. **Convert PDF → MD (Vision-OCR preferred).** Run:
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/scripts/vision_ocr.py" answers/<stem>.pdf answers/converted/<stem>.md
   ```
   This uses `qwen3-vl:8b` via ollama (Tier 1) — produces clean Korean+LaTeX markdown. Falls back to `pytesseract` (Tier 2) automatically if ollama is down. Tier is recorded in the file header via a `<!-- TIER: ... -->` or `<!-- SOURCE: ..., qwen3-vl:8b ... -->` comment. See `skills/vision-ocr/SKILL.md` for details.

   The old `pdf` skill path (`pdf2image` + `pytesseract`) is now only the Tier-2 fallback; do not invoke it directly.

3. **Identify reference solution.** Based on the answer filename stem:
   - `hw3.pdf` → `converted/solutions/hw3_sol.md` (or `converted/solutions/hw3.md`)
   - `diagnostic.pdf` → `quizzes/diagnostic_answers.md`
   - `<topic>_<ts>.pdf` → `quizzes/<topic>_<ts>_answers.md`
   - `twin_<id>_<ts>.pdf` → `twins/<id>_<ts>_sol.md`
   - `chain_<ts>.pdf` → `chain/<ts>_sol.md`
   If cannot resolve, ask the user to specify.

4. **Strategy-based grading per problem:**
   - Pattern match (did the user invoke the right pattern from `course-index/patterns.md`?)
   - Variable choice (did they hold the right things fixed?)
   - End form (does their final expression structure match?)
   - Completeness (where did they stop?)

5. **Render compact grade table** (≤ 15 lines in chat):
   ```
   | P# | Pattern | Vars | End form | Overall |
   |---|---|---|---|---|
   ```
   Plus one closing line: "우세한 실수: <type>. 다음 드릴: /<command> <target>."

6. **Log errors.** Append each non-✅ entry to `errors/log.md` in the YAML format from answer-processing SKILL.md.

7. **Do NOT** print the full reference solution. The user can open it themselves if they want to study.

## OCR quality escape hatch

Inspect the `<!-- TIER: ... -->` / `<!-- SOURCE: ... -->` header comment in `answers/converted/<stem>.md` first.

- **Tier 1 (`qwen3-vl:8b`) succeeded:** grade normally. Quality is usually good enough for strategy matching even on messy handwriting.
- **Tier 2 fallback (`tesseract`) was used**, OR the MD is <100 chars, OR mostly garbled:
  ```
  OCR 결과 품질이 낮음 (채점 신뢰도 떨어짐).
  옵션:
    (a) `ollama serve &` 후 `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/vision_ocr.py" <pdf> <md>` 재실행
    (b) 더 밝게/크게 재스캔 후 다시 /grade
    (c) 답안을 직접 .md로 타이핑해서 `answers/converted/<stem>.md`에 저장 후 다시 /grade
    (d) 채점 대신 /blind <problem-id>로 전략만 말로 체크
  ```

## When both .pdf and .md exist

If `answers/<stem>.pdf` AND `answers/converted/<stem>.md` both exist and the `.md` is recent (edited within 1 hour), use the `.md` directly (user likely manually cleaned OCR output).
