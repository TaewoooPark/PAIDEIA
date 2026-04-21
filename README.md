<h1 align="center">ΠΑΙΔΕΙΑ · Paideia</h1>

<p align="center">
  <strong>Stop renting your own learning.</strong><br>
  <em>A Claude Code plugin that forms exam readiness — locally, from your own materials, without a subscription.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/github/license/TaewoooPark/PAIDEIA?style=flat-square&labelColor=000000&color=333333" alt="License">
  <img src="https://img.shields.io/github/stars/TaewoooPark/PAIDEIA?style=flat-square&logo=github&logoColor=white&labelColor=000000&color=333333" alt="GitHub stars">
  <img src="https://img.shields.io/github/last-commit/TaewoooPark/PAIDEIA?style=flat-square&labelColor=000000&color=333333" alt="Last commit">
  <img src="https://img.shields.io/github/repo-size/TaewoooPark/PAIDEIA?style=flat-square&labelColor=000000&color=333333" alt="Repo size">
  &nbsp;
  <img src="https://img.shields.io/badge/Claude%20Code-000000?style=flat-square&logo=anthropic&logoColor=white&labelColor=000000" alt="Claude Code">
  <img src="https://img.shields.io/badge/Plugin-000000?style=flat-square&labelColor=000000&color=000000" alt="Plugin">
  <img src="https://img.shields.io/badge/Markdown-000000?style=flat-square&logo=markdown&logoColor=white&labelColor=000000" alt="Markdown">
  <img src="https://img.shields.io/badge/Python-000000?style=flat-square&logo=python&logoColor=white&labelColor=000000" alt="Python">
  <img src="https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white&labelColor=000000" alt="Ollama">
  <img src="https://img.shields.io/badge/Qwen3--VL-000000?style=flat-square&labelColor=000000&color=000000" alt="Qwen3-VL">
  <img src="https://img.shields.io/badge/Tesseract-000000?style=flat-square&labelColor=000000&color=000000" alt="Tesseract">
  &nbsp;
  <img src="https://img.shields.io/badge/LaTeX-000000?style=flat-square&logo=latex&logoColor=white&labelColor=000000" alt="LaTeX">
  <img src="https://img.shields.io/badge/Obsidian-000000?style=flat-square&logo=obsidian&logoColor=white&labelColor=000000" alt="Obsidian">
</p>

<p align="center">
  <a href="./README.ko.md">한국어 README</a>
</p>

---

<p align="center">
  <em>The textbook was already yours. The lectures were already yours. Your notes were already yours.<br>
  Paideia just lets you stop paying rent on understanding you already own.</em>
</p>

---

## What Paideia means

In ancient Greece, **Παιδεία** was never the deposit of facts into a passive student. It was the lifelong formation of a complete human being — through structured encounter with primary texts, guided practice under a master, and reflective dialogue that folds feedback into deeper revision.

This plugin implements that cycle for the specific, bounded problem of **exam preparation** in math, physics, and engineering courses:

```
  ingest ──▶ analyze ──▶ drill ──▶ grade ──▶ weakmap ──▶ cheatsheet
     ▲                                                        │
     └────────────────── feedback loop ───────────────────────┘
```

Every stage produces a markdown artifact that lives in your course folder forever. Nothing is ephemeral. Nothing is hidden behind an API. Nothing stops working when the next funding winter hits.

---

## The problem this replaces

The education industry has convinced students that understanding is a service you subscribe to.

- **Coursera, edX, Khan Academy Premium** — sell you access to lectures you could watch on YouTube.
- **Quizlet Plus, Anki cloud, Brainscape** — monetize flashcards of your own notes.
- **Chegg, Course Hero** — paywall the same solution manuals your library ships with the textbook.
- **Brilliant, Duolingo Max, Khanmigo** — charge monthly fees to chat with an LLM whose tokens cost a fraction of a cent.
- **ChatGPT Study Mode, Gemini "Deep Study", NotebookLM** — upload your entire private study corpus to someone else's server, train on it, bill you anyway.

None of these *form* understanding. They **rent** it to you — until you stop paying, or until the service is sunset, or until the model is lobotomized in the next alignment pass. The moment the charge fails, the moment the provider pivots, the moment a policy changes, your study environment evaporates.

Paideia is the counter-move. The intelligence lives on your disk. The artifacts are markdown files you own. The OCR runs on a VLM sitting in your own RAM. There is nothing to subscribe to, nothing to cancel, nothing to lose.

| Capability | Paideia | Typical edu-SaaS |
|-----------|---------|------------------|
| Where your PDFs live | Your disk, period | Uploaded, parsed, retained |
| Where your hand-written answers go | `answers/`, OCR'd on-device via Qwen3-VL 8B on ollama | Uploaded for "AI grading" |
| Where your error log lives | `errors/log.md` — a plain YAML file | Proprietary DB, exportable only with paid tier |
| Where the cheatsheet renders | Your local markdown + reportlab PDF | A web viewer behind login |
| What breaks when they shut down | Nothing | Everything |
| Monthly fee | $0 | $8–$25 |
| `git diff` your own understanding over time | Yes | No |
| Works offline on a plane the night before the exam | Yes | Often no |

The only component that touches a network is `ollama pull qwen3-vl:8b` — a one-time ~6 GB download of model weights. After that, every inference is local.

---

## The load-bearing principle: HW density = exam probability

Most "study smart" advice tells you to hunt your blind spots. That is **backwards**. The professor has *already told you* where the exam points live — by assigning homework. Sections with heavy HW coverage are 🔥🔥 Exam-primary. Sections with zero HW are ⚪ Low-risk, not "hidden traps". The professor's omission is the strongest possible signal that the topic is off the exam.

Paideia's ranking is explicit about this, and every drill command honors it by default:

| Tier | HW count on section | Treatment | Share of mock-exam points |
|------|---------------------|-----------|---------------------------|
| 🔥🔥 Exam-primary | 3+ | Drill hardest | ≥70% |
| 🔥 Exam-likely | 2 | Drill next | ~25% |
| 🟡 Exam-possible | 1 | Warm-pass review | ≤5% |
| ⚪ Low-risk | 0 | Reference only | 0 |

`/paideia:quiz all`, `/paideia:mock`, `/paideia:hwmap hot` all weight output by this tiering. If you insist on drilling a ⚪ section, the plugin complies once and warns you that exam probability is low — your limited time is worth more than an imagined gotcha.

---

## The formation cycle, stage by stage

| Stage | What it does | Commands | Produces |
|-------|-------------|----------|----------|
| **Encounter** | Read the professor's signal | `/paideia:ingest` | `converted/**/*.md` — every lecture, textbook chapter, HW, solution, as clean markdown |
| **Structure** | Extract the grammar of the course | `/paideia:analyze` | `course-index/{summary,patterns,coverage}.md` — topic tree, recurring solution patterns (P1..Pk), HW-density exam-tier ranking |
| **Practice** | Active recall weighted by what the professor actually tests | `/paideia:quiz`, `/paideia:twin`, `/paideia:blind`, `/paideia:chain`, `/paideia:mock` | `quizzes/`, `twins/`, `chain/`, `mock/` — problems you solve on paper |
| **Reflection** | Your hand-written work becomes a grade | `/paideia:grade` | `answers/converted/<name>.md` + `errors/log.md` — local Qwen3-VL OCR, strategy-based grading |
| **Diagnosis** | Errors compressed into a priority-ranked weakness report | `/paideia:weakmap` | `weakmap/weakmap_<ts>.md` — append-only history |
| **Distillation** | One page, error-driven, printable | `/paideia:cheatsheet`, `/paideia:derive`, `/paideia:pattern` | `cheatsheet/final.md`, `derivations/<slug>.md` — reference only what you actually need |

Supporting: `/paideia:hwmap` surfaces HW-density exam-probability, `/paideia:init-course` bootstraps a fresh course folder.

---

## Install

### Prerequisites

- [Claude Code](https://claude.ai/claude-code) CLI
- Python 3.9+ (the plugin checks + offers to install its deps)
- **macOS**: `brew install poppler tesseract tesseract-lang ollama`
- **Linux (Debian/Ubuntu)**: `apt-get install poppler-utils tesseract-ocr tesseract-ocr-kor` + [ollama install script](https://ollama.com/install.sh)
- ~6 GB free disk for the `qwen3-vl:8b` model (Tier-1 hand-writing OCR)

### Install via Claude Code plugin marketplace

```bash
# Inside Claude Code:
/plugin marketplace add TaewoooPark/PAIDEIA
/plugin install paideia@paideia-marketplace
```

After install, 14 slash commands become available under the `/paideia:` namespace.

### Per-course bootstrap

```bash
mkdir -p ~/courses/my-course && cd ~/courses/my-course
```

Then in Claude Code, inside that directory:

```
/paideia:init-course
```

This interactively:
1. Checks Python / tesseract / ollama deps and offers to install missing ones
2. Kicks off `ollama pull qwen3-vl:8b` in the background if the model isn't present
3. Creates the directory skeleton (`materials/`, `converted/`, `course-index/`, `quizzes/`, `mock/`, `twins/`, `chain/`, `derivations/`, `cheatsheet/`, `weakmap/`, `answers/converted/`, `errors/`)
4. Asks for `COURSE_NAME`, `EXAM_DATE`, `EXAM_TYPE`, `USER_WEAK_ZONES`
5. Writes a project-level `CLAUDE.md` with those values
6. `git init` so your prep is versioned from the first keystroke

---

## A reading tip: use Obsidian

Paideia writes everything as plain markdown with LaTeX math (`$...$`, `$$...$$`). You can read it in any editor, but **[Obsidian](https://obsidian.md)** is the natural choice:

- Renders `$...$` and `$$...$$` math via MathJax with zero configuration
- Backlinks let you click from `quizzes/q_<ts>.md` straight into the cited `converted/lectures/chN.md §K`
- The whole course folder is just a vault — point Obsidian at `~/courses/my-course`, and everything is a searchable graph
- Works entirely offline, free, local. Consistent with Paideia's philosophy: your notes, your disk, your tool

VS Code with a markdown-math extension works too. The terminal — even with a markdown preview — is bad for math; don't fight that.

---

## Full workflow — an example

### Phase 0 — once per course (15 minutes)

```bash
cp ~/textbooks/ch*.pdf      ~/courses/my-course/materials/textbook/
cp ~/lecture-notes/wk*.pdf  ~/courses/my-course/materials/lectures/
cp ~/hw/hw*.pdf             ~/courses/my-course/materials/homework/
cp ~/hw/hw*_sol.pdf         ~/courses/my-course/materials/solutions/
```

In Claude Code:

```
/paideia:ingest                     # PDFs → markdown (digital extract + OCR fallback)
/paideia:analyze <weak-zone hints>  # build patterns + coverage + summary
/paideia:hwmap hot                  # surface 🔥🔥 exam-primary zones
```

### Phase 1 — diagnostic (40 minutes)

```
/paideia:quiz all 20                # broad diagnostic, 20 problems
# solve on paper (40 min), scan to answers/diagnostic.pdf
/paideia:grade                      # local qwen3-vl OCR + strategy grade
```

### Phase 2 — targeted drilling (bulk of your prep time)

```
/paideia:weakmap                    # priority-ranked weakness report
/paideia:blind hw3-p2               # strategy-only drill on a known problem
/paideia:twin hw3-p2                # variant with same pattern, new surface
/paideia:chain 3                    # multi-pattern integration problem
/paideia:quiz weakmap 5             # 5 problems targeting the latest weakmap
```

### Phase 3 — integration (~90 minutes)

```
/paideia:mock 90                    # full 90-min mock weighted by HW density
# solve on paper, scan, upload to answers/mock_<ts>.pdf
/paideia:grade                      # grade the mock
```

### Phase 4 — compression (60 minutes, night before exam)

```
/paideia:cheatsheet --pdf           # error-driven one-pager
/paideia:weakmap                    # review weak zones one more time
```

### Phase 5 — cool-down (10 minutes before exam)

```
/paideia:weakmap                    # top 3 only. Do not learn new things.
```

---

## Commands (14 total)

| Command | Purpose |
|---------|---------|
| `/paideia:init-course` | Bootstrap a fresh course folder (dep check, skeleton, metadata prompt, background `ollama pull`) |
| `/paideia:ingest [--force]` | PDFs in `materials/**` → markdown in `converted/**` (digital extraction + OCR fallback) |
| `/paideia:analyze [hints]` | Build `course-index/{summary,patterns,coverage}.md` |
| `/paideia:hwmap hot\|<§>` | Surface 🔥🔥 Exam-primary sections ranked by HW density |
| `/paideia:pattern <§\|Pk\|keyword>` | Show pattern cards from course-index |
| `/paideia:derive <target>` | Clean reference derivation to `derivations/<slug>.md` |
| `/paideia:quiz <topic\|§\|weakmap> [N]` | N practice problems, answers hidden in sibling `_answers.md` |
| `/paideia:blind <problem-id>` | Strategy-check drill on a known problem (no re-solve, describe approach) |
| `/paideia:twin <problem-id>` | Variant of a known problem — same pattern, new surface |
| `/paideia:chain <N>` | Multi-pattern integration problem combining N patterns |
| `/paideia:mock <minutes>` | Full mock exam, HW-density weighted |
| `/paideia:grade [path]` | OCR answer PDF via local Qwen3-VL, strategy-grade, append `errors/log.md` |
| `/paideia:weakmap [concept]` | Priority-ranked weakness report saved to `weakmap/weakmap_<ts>.md` |
| `/paideia:cheatsheet [--pdf]` | Error-driven one-pager |

---

## Under the hood

### Hand-writing OCR: tiered and local

The user does not type math into chat. They solve on paper, scan to PDF, drop the PDF into `answers/`, and run `/paideia:grade`. The plugin converts the scan to markdown via a two-tier local OCR pipeline:

```
answers/<stem>.pdf
  ↓ python3 ${CLAUDE_PLUGIN_ROOT}/scripts/vision_ocr.py <pdf> <md>
  ↓   Tier 1: qwen3-vl:8b via ollama  (keep_alive 15m, warmup, ≤1600px JPEG)
  ↓   Tier 2: pytesseract eng+kor     (auto-fallback on any exception)
answers/converted/<stem>.md           ← has `<!-- SOURCE / TIER -->` header for /grade
```

Qwen3-VL 8B is currently the strongest open-weights VLM that fits in consumer RAM and reads mathematical hand-writing well. It runs via [ollama](https://ollama.com), which keeps the model warm between calls so subsequent grades are fast. If the model is unavailable for any reason, the pipeline silently falls back to pytesseract with `eng+kor` language data — lower fidelity, but always available.

### Strategy-based grading, not line-by-line

OCR noise in hand-written math makes strict algebraic grading useless — a single misread `∫` vs `∑` would cascade. More importantly, **pattern recognition is the actual exam bottleneck**, not arithmetic. The grader therefore checks three things on each problem:

1. **Pattern** — did the student pick the right Pk from `course-index/patterns.md`?
2. **Variables** — did they identify the right substitution / basis / index / contour?
3. **End-form** — does their final expression have the right shape (dimensions, asymptotics, structure)?

Errors get logged as YAML to `errors/log.md` with a typed classification (`pattern-missed | wrong-variable | wrong-end-form | algebraic | sign | definition`). This log is the seed for `/paideia:weakmap` and the *only* input to `/paideia:cheatsheet --pdf`.

### Patterns extracted from *your* solutions

`/paideia:analyze` doesn't ship a generic "calculus moves" list. It reads your course's actual solution manual, extracts recurring solution patterns, and labels them P1, P2, ... with worked instances that cite your own `converted/solutions/` files. The patterns are *your course's idioms*, not a textbook's. For a complex analysis course, P3 might be "closed contour + Jordan's lemma + residue at essential singularity." For a linear systems course, P3 might be "partial fractions + inverse Laplace with complex poles." Every discipline has its own moves; only the course itself reveals them.

### Append-only history

`weakmap/` never overwrites. Every `/paideia:weakmap` invocation produces `weakmap/weakmap_<ISO-timestamp>.md`. You can `git log weakmap/` and see exactly which weaknesses collapsed first, which ones persisted, which new ones emerged after the diagnostic mock. This is "`git diff` your own understanding over time" in practice.

---

## What ships

```
PAIDEIA/
├── .claude-plugin/marketplace.json      # marketplace manifest
├── LICENSE                              # MIT
├── README.md                            # this file
├── README.ko.md                         # Korean mirror
└── plugins/paideia/
    ├── .claude-plugin/plugin.json       # plugin manifest (name, version, author)
    ├── README.md                        # quick-reference card
    ├── skills/
    │   ├── pdf/SKILL.md                 # digital + basic OCR
    │   ├── vision-ocr/SKILL.md          # Qwen3-VL Tier 1 + tesseract Tier 2
    │   ├── course-builder/SKILL.md      # ingest + analyze pipeline
    │   ├── exam-drill/
    │   │   ├── SKILL.md                 # drill primitives (twin, blind, chain, mock)
    │   │   └── twin-recipe.md           # invariance rules for variant generation
    │   └── answer-processing/SKILL.md   # strategy-grade hand-written OCR output
    ├── commands/                        # 14 slash commands
    │   ├── init-course.md  ingest.md    analyze.md   hwmap.md
    │   ├── pattern.md      derive.md    quiz.md      blind.md
    │   ├── twin.md         chain.md     mock.md      grade.md
    │   └── weakmap.md      cheatsheet.md
    └── scripts/vision_ocr.py            # ollama qwen3-vl driver w/ tesseract fallback
```

---

## Design convictions

1. **The terminal is bad for math.** Claude produces markdown files; you read them (ideally in Obsidian).
2. **Typing solutions is slow and error-prone.** You solve on paper, scan, and the plugin OCRs locally.
3. **OCR noise is inevitable.** So grading is strategy-based (pattern / variables / end-form), not line-by-line algebra. This is what the actual exam grader is evaluating anyway.
4. **Patterns must be extracted from *your* course's solutions** — not from a generic list. Every discipline has its own idioms; only the course itself reveals them.
5. **Your errors are the most valuable study signal** — more than the textbook, more than the lectures. The cheatsheet is generated from `errors/log.md`, not from the syllabus.
6. **HW density tells you the exam.** Your time is finite; spend it where the points are.
7. **No cloud, no subscription, no lock-in.** If Paideia breaks or you walk away, every artifact is plain markdown under your own git history. Nothing to export, nothing to lose.

---

## FAQ

**Does this work for non-math courses?**
It's built around problem-pattern extraction, so it shines in quantitative disciplines: math, physics, EE, CS-theory, ML-theory, statistics, engineering. For history or literature it would still ingest and produce summaries, but the drill commands assume problems have solution patterns.

**Korean and English mixed materials?**
Yes. Ingestion and OCR are configured for `eng+kor`. Patterns and grading responses honor the language mix of your source materials.

**What does it cost?**
Zero. MIT-licensed. The `qwen3-vl:8b` model is open-weight. Ollama, tesseract, poppler, reportlab are all free.

**What if `qwen3-vl:8b` is unavailable or my machine can't run it?**
The pipeline automatically falls back to tesseract `eng+kor`. Grading still works; OCR fidelity on hand-writing is just lower.

**Can I trust an LLM to grade my work?**
Grading is strategy-based (pattern match, not algebra), the grader cites the pattern from `course-index/patterns.md`, and every grade writes a YAML entry you can audit in `errors/log.md`. If a grade is wrong, fix the YAML entry — the next `/paideia:weakmap` reflects the correction.

**Is my data private?**
Your PDFs, your markdown, your errors, your weakmaps — they all live in your local course folder. The plugin never uploads anything. `ollama pull qwen3-vl:8b` is a one-time model download from ollama.com; after that, inference runs on your machine.

---

## Connect

<p align="center">
  <a href="https://github.com/TaewoooPark"><img src="https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
  <a href="https://x.com/theoverstrcture"><img src="https://img.shields.io/badge/-X-000000?style=for-the-badge&logo=x&logoColor=white" alt="X (Twitter)"></a>
  <a href="https://www.linkedin.com/in/taewoo-park-427a05352"><img src="https://img.shields.io/badge/-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://www.instagram.com/t.wo0_x/"><img src="https://img.shields.io/badge/-Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram"></a>
  <a href="mailto:ptw151125@kaist.ac.kr"><img src="https://img.shields.io/badge/-Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
</p>

---

## License

MIT. Use freely. Modify for your own courses. Contributions welcome — though the point of the plugin is that **you shouldn't have to depend on anyone else's upstream to keep studying.**

---

<p align="center">
  <em>Education is not a subscription. It never was.<br>
  Παιδεία — formation, not rental.</em>
</p>
