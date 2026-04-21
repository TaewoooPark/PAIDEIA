<p align="center">
  <strong>ΠΑΙΔΕΙΑ</strong>
</p>

<h1 align="center">Paideia</h1>

<p align="center">
  <em>Stop renting your own learning.</em><br>
  <em>A Claude Code plugin that forms exam readiness — locally, from your own materials, without a subscription.</em>
</p>

<p align="center">
  <a href="https://github.com/TaewoooPark/paideia">companion: paideia (formation cycle)</a>
</p>

---

## The problem this replaces

The education industry has convinced students that understanding is a service you subscribe to.

- **Coursera, edX, Khan Academy Premium** — sell you access to lectures you could watch on YouTube.
- **Quizlet Plus, Anki cloud, Brainscape** — monetize flashcards of your own notes.
- **Chegg, Course Hero** — paywall the same solution manuals your library ships with the textbook.
- **Brilliant, Duolingo Max, Khanmigo** — charge monthly fees to chat with an LLM whose tokens cost a fraction of a cent.
- **ChatGPT Study Mode, Gemini "Deep Study"** — upload your entire private study corpus to someone else's server, train on it, bill you anyway.

None of these form understanding. They **rent** it to you — until you stop paying, or until the service is sunset, or until the model is lobotomized in the next alignment pass.

Paideia is the counter-move. The intelligence lives on your disk. The artifacts are markdown files you own. The OCR runs on a VLM sitting in your own RAM. There is nothing to subscribe to, nothing to cancel, nothing to lose when the next funding winter hits your preferred app.

## What Paideia means

In ancient Greece, **Παιδεία** was never the deposit of facts into a passive student. It was the lifelong formation of a complete human being — through structured encounter with primary texts, guided practice under a master, and reflective dialogue that folds feedback into deeper revision.

This plugin implements that cycle for the specific problem of exam preparation:

```
  ingest ──▶ analyze ──▶ drill ──▶ grade ──▶ weakmap ──▶ cheatsheet
     ▲                                                        │
     └────────────────── feedback loop ───────────────────────┘
```

Every stage produces a markdown artifact that lives in your course folder forever. Nothing is ephemeral. Nothing is hidden behind an API.

| Stage | Commands | What it produces |
|-------|----------|------------------|
| **Encounter** — read the professor's signal | `/paideia:ingest` | `converted/**/*.md` — every lecture, textbook chapter, HW, solution, as clean markdown |
| **Structure** — extract the grammar of the course | `/paideia:analyze` | `course-index/{summary,patterns,coverage}.md` — topic tree, recurring solution patterns (P1..Pk), HW-density exam-tier ranking |
| **Practice** — active recall weighted by what the professor actually tests | `/paideia:quiz`, `/paideia:twin`, `/paideia:blind`, `/paideia:chain`, `/paideia:mock` | `quizzes/`, `twins/`, `chain/`, `mock/` — problems you solve on paper |
| **Reflection** — your hand-written work becomes a grade | `/paideia:grade` | `answers/converted/<name>.md` + `errors/log.md` — local Qwen3-VL OCR, strategy-based grading |
| **Diagnosis** — errors compressed into a priority-ranked weakness report | `/paideia:weakmap` | `weakmap/weakmap_<ts>.md` — append-only history |
| **Distillation** — one page, error-driven | `/paideia:cheatsheet`, `/paideia:derive`, `/paideia:pattern` | `cheatsheet/final.md`, `derivations/<slug>.md` — reference only what you actually need |

Supporting: `/paideia:hwmap` surfaces HW-density exam-probability, `/paideia:init-course` bootstraps a fresh course folder.

## The load-bearing principle: HW density = exam probability

Most "study smart" advice tells you to hunt your blind spots. That is backwards. The professor has **already told you** where the exam points live — by assigning homework. Sections with heavy HW coverage are 🔥🔥 Exam-primary. Sections with zero HW are ⚪ Low-risk, not "hidden traps." The professor's omission is the strongest possible signal that the topic is off the exam.

Paideia's ranking is explicit about this:

| Tier | HW count | Treatment |
|------|---------|-----------|
| 🔥🔥 Exam-primary | 3+ | Drill hardest. ≥70% of mock-exam points. |
| 🔥 Exam-likely | 2 | Drill next. ~25% of mock-exam points. |
| 🟡 Exam-possible | 1 | Warm-pass review. ≤5% of mock-exam points. |
| ⚪ Low-risk | 0 | Reference only. Do not spend drill time. |

Every drill command — `/paideia:quiz all`, `/paideia:mock`, `/paideia:hwmap hot` — honors this weighting by default.

## Local-first, by construction

| Capability | Paideia | Typical edu-SaaS |
|-----------|---------|------------------|
| Where your PDFs live | Your disk, period | Uploaded, parsed, retained |
| Where your hand-written answers go | `answers/`, OCR'd on-device via Qwen3-VL 8B on ollama | Uploaded for "AI grading" |
| Where your error log lives | `errors/log.md` — a plain YAML file | Proprietary DB, exportable only with paid tier |
| Where the cheatsheet renders | Your local markdown + reportlab | A web viewer behind login |
| What breaks when they shut down | Nothing | Everything |
| Monthly fee | $0 | $8–$25 |
| Ability to `git diff` your own understanding over time | Yes | No |

The only component that touches a network is `ollama pull qwen3-vl:8b` — a one-time 6 GB download of model weights. After that, every inference happens on your machine. You can disconnect and prep for the exam on a plane.

## Install

### Prerequisites

- [Claude Code](https://claude.ai/claude-code) CLI
- Python 3.9+ (the plugin checks + offers to install its deps)
- **macOS**: `brew install poppler tesseract tesseract-lang ollama`
- **Linux**: `apt-get install poppler-utils tesseract-ocr tesseract-ocr-kor` + [ollama install script](https://ollama.com/install.sh)
- ~6 GB free disk for the `qwen3-vl:8b` model (Tier-1 hand-writing OCR)

### Install from this marketplace

```
# Inside Claude Code:
/plugin marketplace add TaewoooPark/paideia-plugin
/plugin install paideia@paideia-marketplace
```

### Per-course bootstrap

```bash
mkdir -p ~/courses/complex-analysis && cd ~/courses/complex-analysis
```

Then in Claude Code, inside that directory:

```
/paideia:init-course
```

This interactively:
1. Checks Python / tesseract / ollama deps
2. Kicks off `ollama pull qwen3-vl:8b` in the background if the model isn't present
3. Creates the directory skeleton (`materials/`, `converted/`, `course-index/`, `quizzes/`, `mock/`, `twins/`, `chain/`, `derivations/`, `cheatsheet/`, `weakmap/`, `answers/converted/`, `errors/`)
4. Asks for `COURSE_NAME`, `EXAM_DATE`, `EXAM_TYPE`, `USER_WEAK_ZONES`
5. Writes a project-level `CLAUDE.md` with those values
6. `git init` so your prep is versioned from the first keystroke

## Workflow — an example

```bash
# Phase 0 — once per course
cp ~/textbooks/ch*.pdf       ~/courses/complex-analysis/materials/textbook/
cp ~/lecture-notes/wk*.pdf   ~/courses/complex-analysis/materials/lectures/
cp ~/hw/hw*.pdf              ~/courses/complex-analysis/materials/homework/
cp ~/hw/hw*_sol.pdf          ~/courses/complex-analysis/materials/solutions/
```

In Claude Code:

```
/paideia:ingest                        # PDFs → MDs
/paideia:analyze 적분변환, 복소해석     # build patterns + coverage + summary
/paideia:hwmap hot                     # surface 🔥🔥 exam-primary zones
```

```
/paideia:quiz all 20                   # broad diagnostic
# solve on paper (40 min), scan to answers/all_<ts>.pdf
/paideia:grade                         # local qwen3-vl OCR + strategy grade
```

```
/paideia:weakmap                       # priority-ranked weakness report
/paideia:blind hw3-p2                  # strategy-only drill on a known problem
/paideia:twin hw3-p2                   # variant with same pattern, new surface
/paideia:chain 3                       # multi-pattern integration problem
/paideia:mock 90                       # full 90-min mock weighted by HW density
```

```
/paideia:cheatsheet --pdf              # error-driven one-pager, 30 min before exam
/paideia:weakmap                       # top 3 weaknesses, 10 min before exam
```

## What ships

```
plugins/paideia/
├── .claude-plugin/plugin.json
├── skills/
│   ├── pdf/SKILL.md                   # digital + basic OCR
│   ├── vision-ocr/SKILL.md            # Qwen3-VL Tier 1 + tesseract Tier 2
│   ├── course-builder/SKILL.md        # ingest + analyze pipeline
│   ├── exam-drill/
│   │   ├── SKILL.md                   # drill primitives
│   │   └── twin-recipe.md             # invariance rules for variants
│   └── answer-processing/SKILL.md     # strategy-grade hand-written OCR output
├── commands/                          # 14 slash commands
│   ├── init-course.md
│   ├── ingest.md      analyze.md      hwmap.md     pattern.md
│   ├── derive.md      quiz.md         blind.md     twin.md
│   ├── chain.md       mock.md         grade.md     weakmap.md
│   └── cheatsheet.md
└── scripts/vision_ocr.py              # ollama qwen3-vl driver w/ tesseract fallback
```

## Design convictions

1. **The terminal is bad for math.** Claude produces markdown files; you read them.
2. **Typing solutions is slow.** You solve on paper, scan, and the plugin OCRs locally.
3. **OCR noise is inevitable.** So grading is strategy-based (pattern / variables / end-form), not line-by-line algebra. This is what the actual exam grader is evaluating anyway.
4. **Patterns must be extracted from *your* course's solutions** — not from a generic "calculus moves" list. Every discipline has its own idioms; only the course itself reveals them.
5. **Your errors are the most valuable study signal** — more than the textbook, more than the lectures. The cheatsheet is generated from `errors/log.md`, not from the syllabus.
6. **HW density tells you the exam.** Your time is finite; spend it where the points are.

## License

MIT. Use freely. Modify for your own courses. Contributions welcome — though the point of the plugin is that you shouldn't need to depend on anyone else's upstream to keep studying.

---

<p align="center">
  <em>The textbook was already yours. The lectures were already yours. Your notes were already yours.<br>
  Paideia just lets you stop paying rent on understanding you already own.</em>
</p>
