---
description: Bootstrap a fresh course folder — create directory skeleton, check deps (Python, tesseract, ollama), kick off qwen3-vl:8b pull in the background, prompt for course metadata, and write CLAUDE.md + .course-meta. Run once per course in the course folder's CWD.
argument-hint: (no args; fully interactive)
---

You are bootstrapping the user's current working directory into a fresh paideia workspace. Everything you create lives in the **user's CWD**, not in the plugin. The plugin itself (skills, commands, `vision_ocr.py`) is auto-loaded — your job is the per-course state.

## Execution plan

Run these steps sequentially. Use the Bash tool. Keep chat output compact — the user is watching progress.

### Step 1 — Python deps

Check + offer to install `pypdf pdfplumber pytesseract pdf2image pillow reportlab`:

```bash
python3 -c "import pypdf, pdfplumber, pytesseract, pdf2image, PIL, reportlab" 2>&1 || \
  echo "MISSING_PYTHON_DEPS"
```

If missing: offer `python3 -m pip install --break-system-packages --user pypdf pdfplumber pytesseract pdf2image pillow reportlab`. Run only with user's OK.

### Step 2 — System binaries

```bash
command -v pdftoppm   >/dev/null 2>&1 && echo "poppler: ok"    || echo "poppler: MISSING"
command -v tesseract  >/dev/null 2>&1 && echo "tesseract: ok"  || echo "tesseract: MISSING"
command -v ollama     >/dev/null 2>&1 && echo "ollama: ok"     || echo "ollama: MISSING"
tesseract --list-langs 2>&1 | grep -q '^kor$' && echo "tesseract-kor: ok" || echo "tesseract-kor: MISSING"
```

For missing items, print the install command (don't auto-run — these often need sudo/brew):
- macOS: `brew install poppler tesseract tesseract-lang ollama`
- Ubuntu: `sudo apt-get install poppler-utils tesseract-ocr tesseract-ocr-kor` and see `https://ollama.com/install.sh` for ollama.

### Step 3 — Ollama daemon + qwen3-vl:8b pull (background)

Only if `ollama` binary is present:

```bash
# Daemon check
curl -fsS --max-time 2 http://localhost:11434/api/tags >/dev/null 2>&1 \
  && echo "daemon: up" || echo "daemon: down — run 'ollama serve &' in a separate shell"
```

If daemon is up AND model missing, kick off pull in background so it overlaps with the metadata prompts (Step 5):

```bash
if ! ollama list 2>/dev/null | awk '{print $1}' | grep -qx "qwen3-vl:8b"; then
  LOG=$(mktemp -t paideia-ollama-pull.XXXXXX.log)
  ( ollama pull qwen3-vl:8b > "$LOG" 2>&1 ) &
  echo "BACKGROUND_PULL_PID=$!"
  echo "LOG=$LOG"
fi
```

Remember the PID and LOG path. Report: "ollama 모델 백그라운드 pull 시작 (PID, ~6 GB, 메타데이터 입력과 병렬 진행)."

### Step 4 — Directory skeleton

Create these directories in the user's CWD (idempotent):

```bash
mkdir -p materials/{lectures,textbook,homework,solutions} \
         converted/{lectures,textbook,homework,solutions} \
         course-index quizzes mock twins chain derivations cheatsheet weakmap \
         answers/converted errors

# Seed errors/log.md if missing (append-only log; /grade and /weakmap depend on it)
[ -f errors/log.md ] || cat > errors/log.md <<'EOF'
# Error log

<!-- Append-only YAML entries. Schema:
- problem_id: <id>
  pattern: <Pk>
  error_type: pattern-missed | wrong-variable | wrong-end-form | algebraic | sign | definition
  summary: "<1 line>"
  date: <ISO8601>
-->
EOF
```

### Step 5 — Course metadata (ask the user)

Ask four short questions, in Korean:
1. `COURSE_NAME` (예: Complex Analysis MATH 405)
2. `EXAM_DATE` (YYYY-MM-DD)
3. `EXAM_TYPE` (midterm/final/qualifier)
4. `USER_WEAK_ZONES` (comma-separated topics, or `unknown`)

Wait for responses before continuing. Then write:

```bash
cat > .course-meta <<EOF
COURSE_NAME: <answer1>
EXAM_DATE: <answer2>
EXAM_TYPE: <answer3>
USER_WEAK_ZONES: <answer4>
EOF
```

### Step 6 — CLAUDE.md (project-level rules)

If `CLAUDE.md` doesn't exist in CWD, write the paideia template (see `CLAUDE.md.template` below). If it exists, **do not overwrite** — ask the user if they want to append the paideia section instead.

Substitute the 4 metadata values into the template's metadata block before writing.

### Step 7 — git init

If `.git` doesn't exist:

```bash
git init -q
cat > .gitignore <<'EOF'
.claude/cache/
answers/*.pdf
answers/converted/*.md
errors/log.md
quizzes/*_answers.md
mock/*_sol.md
twins/*_sol.md
chain/*_sol.md
cheatsheet/final.pdf
.DS_Store
*.pyc
__pycache__/
EOF
git add -A
git commit -q -m "paideia: initial setup" 2>/dev/null || true
```

### Step 8 — Wait for background pull (if any)

If Step 3 spawned a background pull:

```bash
wait <PID>
```

Report pull status (success or point to `$LOG`).

### Step 9 — Print next steps

```
✅ <COURSE_NAME> 준비 완료.

다음 단계:
  1. materials/{lectures,textbook,homework,solutions}/ 에 PDF/MD 드롭
  2. /paideia:ingest        ← PDFs → MDs
  3. /paideia:analyze       ← patterns, coverage 생성
  4. /paideia:hwmap hot     ← 🔥🔥 시험 핫존 확인
```

## CLAUDE.md.template

Below is the template to write at Step 6. Substitute `$COURSE_NAME`, `$EXAM_DATE`, `$EXAM_TYPE`, `$WEAK_ZONES` verbatim.

```markdown
# Course Cram — Project Context

## Purpose

This project is a general-purpose exam preparation workspace for any math or physics course.
Given raw course materials (lecture notes, textbook chapters, HW problems, HW solutions — in
PDF or markdown), it builds a structured knowledge base and provides drilling tools for exam prep.

## Course metadata

```
COURSE_NAME: $COURSE_NAME
EXAM_DATE: $EXAM_DATE
EXAM_TYPE: $EXAM_TYPE
USER_WEAK_ZONES: $WEAK_ZONES
```

## Directory map

materials/ converted/ course-index/ quizzes/ mock/ twins/ chain/ derivations/ cheatsheet/
weakmap/ answers/ errors/ — see the paideia plugin README for full semantics.

## Workflow philosophy

1. **User does not type math in the CLI.** Claude produces MD files. User reads.
2. **User produces PDF scans** of hand-written work in `answers/`.
3. **Claude OCRs via Qwen3-VL** (Tier 1, via the vision-ocr skill) and **strategy-grades**.
4. **HW density = exam probability.** Drill `🔥🔥` (3+ HW) sections first; `⚪` (no HW) = reference only.

## Slash commands

All commands are namespaced `/paideia:<name>`. See the plugin's README for the full list.

## Conventions

- Citations: every explanation cites `converted/<file>.md` §.
- Pattern IDs: reference by `Pk` from `course-index/patterns.md`.
- Never reveal solutions before the user attempts.
- Korean prose, LaTeX math (`$...$` inline, `$$...$$` display).
- Errors logged in `errors/log.md` on every failed attempt (YAML schema).
- Keep drill output ≤ 40 lines, grade reports ≤ 15 lines.
```
