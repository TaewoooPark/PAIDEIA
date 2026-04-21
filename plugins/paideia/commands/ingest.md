---
description: Convert all PDF course materials (lectures, textbook, homework, solutions) to markdown via the pdf skill. Idempotent — skips already-converted files.
argument-hint: [--force to reconvert everything]
---

Load `skills/pdf/SKILL.md` and `skills/course-builder/SKILL.md`.

Arguments: $ARGUMENTS

Follow the course-builder Phase 1 ingest pipeline:

1. Scan `materials/` recursively for `.pdf` and `.md` files.
2. Classify by subfolder: lectures, textbook, homework, solutions.
3. For any `.pdf`, convert to markdown following the pdf skill rules:
   - Try digital text extraction first (pdfplumber).
   - Fall back to OCR (pytesseract + pdf2image, `lang="eng+kor"`) if text is sparse.
   - Write to `converted/<category>/<stem>.md`.
   - Add provenance comment at top.
4. For any `.md` in `materials/`, copy to the mirror path in `converted/` (with provenance).
5. Skip files where `converted/X.md` is newer than `materials/X.pdf` unless `--force` is in arguments.
6. Normalize filenames if inconsistent — ask user if ambiguous (e.g., `hw_2.pdf` vs `HW2.pdf` → suggest `hw2.pdf`).

After conversion, print the ingest summary table:

| Category | Converted | Skipped (already done) | OCR'd |
|---|---|---|---|
| lectures | N | M | K |
| textbook | ... | ... | ... |
| homework | ... | ... | ... |
| solutions | ... | ... | ... |

End with:
"다음 단계: `/analyze`로 patterns.md, coverage.md, summary.md를 생성."

If any file failed to convert (encryption, corrupted, OCR unsupported language), list them at the end with the specific failure reason and a suggested workaround.
