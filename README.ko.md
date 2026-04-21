<h1 align="center">ΠΑΙΔΕΙΑ · Paideia</h1>

<p align="center">
  <strong>더 이상 당신의 배움을 구독에 맡기지 마세요.</strong><br>
  <em>당신의 자료에서 출발해 당신의 컴퓨터 안에서, 구독료 없이 시험 준비 상태를 형성해 주는 Claude Code 플러그인입니다.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/github/license/TaewoooPark/PAIDEIA?style=flat-square&labelColor=000000&color=333333&cacheSeconds=3600" alt="라이선스">
  <img src="https://img.shields.io/github/stars/TaewoooPark/PAIDEIA?style=flat-square&logo=github&logoColor=white&labelColor=000000&color=333333&cacheSeconds=3600" alt="GitHub 스타 수">
  <img src="https://img.shields.io/github/last-commit/TaewoooPark/PAIDEIA?style=flat-square&labelColor=000000&color=333333&cacheSeconds=3600" alt="최근 커밋">
  <img src="https://img.shields.io/github/languages/top/TaewoooPark/PAIDEIA?style=flat-square&labelColor=000000&color=333333&cacheSeconds=3600" alt="주요 언어">
  &nbsp;
  <img src="https://img.shields.io/badge/Claude%20Code-000000?style=flat-square&logo=anthropic&logoColor=white&labelColor=000000&cacheSeconds=3600" alt="Claude Code">
  <img src="https://img.shields.io/badge/Plugin-000000?style=flat-square&labelColor=000000&color=000000&cacheSeconds=3600" alt="Plugin">
  <img src="https://img.shields.io/badge/Markdown-000000?style=flat-square&logo=markdown&logoColor=white&labelColor=000000&cacheSeconds=3600" alt="Markdown">
  <img src="https://img.shields.io/badge/Python-000000?style=flat-square&logo=python&logoColor=white&labelColor=000000&cacheSeconds=3600" alt="Python">
  <img src="https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white&labelColor=000000&cacheSeconds=3600" alt="Ollama">
  <img src="https://img.shields.io/badge/Qwen3--VL-000000?style=flat-square&labelColor=000000&color=000000&cacheSeconds=3600" alt="Qwen3-VL">
  <img src="https://img.shields.io/badge/Tesseract-000000?style=flat-square&labelColor=000000&color=000000&cacheSeconds=3600" alt="Tesseract">
  &nbsp;
  <img src="https://img.shields.io/badge/LaTeX-000000?style=flat-square&logo=latex&logoColor=white&labelColor=000000&cacheSeconds=3600" alt="LaTeX">
  <img src="https://img.shields.io/badge/Obsidian-000000?style=flat-square&logo=obsidian&logoColor=white&labelColor=000000&cacheSeconds=3600" alt="Obsidian">
</p>

<p align="center">
  <a href="./README.md">English README</a>
</p>

---

<p align="center">
  <em>교과서는 원래 당신의 것이었습니다. 강의도 원래 당신의 것이었습니다. 필기 역시 원래 당신의 것이었습니다.<br>
  Paideia는 이미 당신이 가진 이해에 월세를 내는 일을 멈추게 해 줄 뿐입니다.</em>
</p>

---

## Paideia라는 이름에 대하여

고대 그리스에서 **Παιδεία(파이데이아)**는 수동적인 학생에게 사실을 주입하는 일이 아니었습니다. 그것은 원전과의 구조화된 만남, 스승 아래에서의 연습, 그리고 피드백을 더 깊은 수정으로 되돌려 보내는 성찰적 대화를 통한 — 한 인간을 평생에 걸쳐 형성해 가는 일이었습니다.

이 플러그인은 그 순환을 **수학·물리·공학 과목의 시험 준비**라는 구체적이고 한정된 문제에 맞추어 구현합니다.

```
  ingest ──▶ analyze ──▶ drill ──▶ grade ──▶ weakmap ──▶ cheatsheet
     ▲                                                        │
     └────────────────── feedback loop ───────────────────────┘
```

각 단계는 당신의 코스 폴더에 영원히 남는 마크다운 파일 하나씩을 남깁니다. 휘발되는 것은 없고, API 뒤에 숨는 것도 없습니다. 다음 자금 한파가 닥쳐도 멈추는 것이 없습니다.

---

## 이 플러그인이 대체하는 것

교육 산업은 지난 몇 년 동안 학생들에게 "이해란 구독해야 하는 서비스"라는 감각을 심어 왔습니다.

- **Coursera, edX, Khan Academy Premium** — 유튜브에 이미 올라와 있는 강의의 접근권을 팝니다.
- **Quizlet Plus, Anki cloud, Brainscape** — 당신 스스로 만든 플래시카드에 월 요금을 붙입니다.
- **Chegg, Course Hero** — 교재에 이미 포함된 해답지와 동일한 풀이에 결제 벽을 세웁니다.
- **Brilliant, Duolingo Max, Khanmigo** — 토큰 원가가 1센트의 몇 분의 일에 불과한 LLM과의 대화에 매달 구독료를 매깁니다.
- **ChatGPT Study Mode, Gemini "Deep Study", NotebookLM** — 당신의 사적인 학습 자료를 통째로 남의 서버에 올려 학습에 쓰게 한 뒤, 그 위에서 다시 비용을 청구합니다.

이들 중 어느 것도 이해를 *형성*하지 않습니다. 이들은 이해를 **임대**할 뿐입니다 — 당신이 결제를 멈추는 그 순간까지, 서비스가 종료되는 그 순간까지, 다음 정렬(alignment) 패스에서 모델이 무뎌지는 그 순간까지만요. 카드 결제가 실패하면, 공급자가 방향을 틀면, 정책이 바뀌면 — 당신이 쌓아 둔 학습 환경은 순식간에 증발합니다.

Paideia는 이에 대한 정반대의 해답입니다. 지능은 당신의 디스크 위에 머뭅니다. 산출물은 당신이 소유하는 마크다운 파일입니다. OCR은 당신의 RAM 위에서 돌아가는 VLM이 처리합니다. 구독할 것도, 취소할 것도, 잃을 것도 없습니다.

| 항목 | Paideia | 일반적인 교육 SaaS |
|------|---------|--------------------|
| PDF가 저장되는 곳 | 당신의 디스크, 그게 전부 | 업로드되어 파싱·보관됨 |
| 손으로 쓴 답안이 가는 곳 | `answers/` 폴더. 기본은 이미 쓰고 계신 Claude Code 세션 안에서 OCR — 페이지 이미지조차 Anthropic 서버에 남기고 싶지 않다면 로컬 ollama의 Qwen3-VL 8B로 완전 오프라인 OCR | "AI 채점"을 위해 업로드 |
| 오류 로그가 있는 곳 | `errors/log.md` — 평범한 YAML 파일 | 독점 DB, 유료 티어에서만 내보내기 가능 |
| 치트시트가 렌더링되는 곳 | 로컬 마크다운 + reportlab PDF | 로그인 뒤의 웹 뷰어 |
| 서비스가 종료되면 잃는 것 | 없음 | 전부 |
| 월 사용료 | $0 | $8–$25 |
| 자신의 이해를 `git diff`로 추적 | 가능 | 불가능 |
| 시험 전날 비행기 안에서도 동작 | 가능 | 대부분 불가능 |

기본 설정에서 OCR은 이미 사용 중이신 Claude Code 세션 안에서 동작합니다 — 별도의 서비스도, 별도의 계정도, Claude Code 외의 구독도 필요하지 않습니다. 필기 PDF를 기기 밖으로 내보내고 싶지 않으시다면, `ollama pull qwen3-vl:8b`로 약 6 GB 모델 가중치를 한 번 내려받으면 그 뒤 모든 OCR은 로컬 Qwen3-VL 추론으로 전환됩니다. 어느 쪽을 고르시든 이후의 산출물(패턴, 커버리지, weakmap, 치트시트, 오류 로그)은 전부 당신 디스크 위의 평범한 마크다운입니다.

---

## 핵심 원리: 숙제 밀도가 곧 출제 확률입니다

대부분의 "똑똑하게 공부하는 법"은 사각지대부터 공략하라고 말합니다. 그러나 이 조언은 **방향이 반대입니다**. 교수님은 이미 숙제를 배정하는 것으로 시험 포인트의 위치를 알려 주셨습니다. 숙제가 몰린 절은 🔥🔥 Exam-primary이고, 숙제가 전혀 없는 절은 ⚪ Low-risk일 뿐 "숨겨진 함정"이 아닙니다. 교수님의 침묵은 그 주제가 시험 범위 바깥이라는 가장 강력한 신호입니다.

Paideia의 우선순위는 이 원리를 명시적으로 반영합니다. 모든 드릴 명령이 기본값으로 이 티어링을 따릅니다.

| 티어 | 해당 절의 숙제 수 | 처리 방식 | 모의고사 점수 비중 |
|------|---------------------|-----------|--------------------|
| 🔥🔥 Exam-primary | 3+ | 가장 먼저, 가장 강도 높게 드릴 | ≥70% |
| 🔥 Exam-likely | 2 | 그 다음 드릴 | ~25% |
| 🟡 Exam-possible | 1 | 가볍게 복습 | ≤5% |
| ⚪ Low-risk | 0 | 참조·독서 용도만 | 0 |

`/paideia:quiz all`, `/paideia:mock`, `/paideia:hwmap hot` 모두 이 가중치를 존중합니다. 만약 사용자가 ⚪ 절을 굳이 드릴하겠다고 요청하면, 플러그인은 한 번은 따라 주지만 출제 확률이 낮다는 경고를 덧붙입니다. 제한된 시간은 상상 속 함정보다 훨씬 가치 있기 때문입니다.

---

## 형성 사이클, 단계별 해설

| 단계 | 하는 일 | 명령 | 산출물 |
|------|---------------|------|--------|
| **대면 (Encounter)** | 교수님이 보낸 신호를 읽습니다 | `/paideia:ingest` | `converted/**/*.md` — 모든 강의노트·교재 챕터·숙제·풀이를 깨끗한 마크다운으로 |
| **구조화 (Structure)** | 과목 고유의 문법을 추출합니다 | `/paideia:analyze` | `course-index/{summary,patterns,coverage}.md` — 주제 트리, 반복되는 풀이 패턴 (P1..Pk), 숙제 밀도 기반 출제 티어 |
| **연습 (Practice)** | 교수님이 실제로 시험하는 것에 가중치를 두어 능동 회상을 수행합니다 | `/paideia:quiz`, `/paideia:twin`, `/paideia:blind`, `/paideia:chain`, `/paideia:mock` | `quizzes/`, `twins/`, `chain/`, `mock/` — 종이에 풀 문제들 |
| **성찰 (Reflection)** | 손으로 쓴 답안이 채점 결과로 바뀝니다 | `/paideia:grade` | `answers/converted/<name>.md` + `errors/log.md` — Claude 비전(기본) / Ollama Qwen3-VL / Tesseract 중 선택한 엔진으로 OCR, 전략 기반 채점 |
| **진단 (Diagnosis)** | 오류를 우선순위가 매겨진 약점 리포트로 압축합니다 | `/paideia:weakmap` | `weakmap/weakmap_<ts>.md` — append-only 이력 |
| **증류 (Distillation)** | 오류에서 출발한 한 장짜리 인쇄물을 만듭니다 | `/paideia:cheatsheet`, `/paideia:derive`, `/paideia:pattern` | `cheatsheet/final.md`, `derivations/<slug>.md` — 실제로 필요한 것만 참조 |

보조 명령: `/paideia:hwmap`은 숙제 밀도 기반 출제 확률을 띄워 줍니다. `/paideia:init-course`는 새 코스 폴더를 부트스트랩합니다.

---

## 설치

### 사전 요구사항

**필수**

- [Claude Code](https://claude.ai/claude-code) CLI
- Python 3.9+ (플러그인이 의존성을 확인하고 설치를 제안합니다)
- **macOS**: `brew install poppler tesseract tesseract-lang`
- **Linux (Debian/Ubuntu)**: `apt-get install poppler-utils tesseract-ocr tesseract-ocr-kor`

**선택 — `--ocr=ollama` 모드를 쓰고 싶을 때만 (페이지 이미지가 기기 밖으로 전혀 나가지 않습니다)**

- `ollama` + `qwen3-vl:8b` 모델 (~6 GB). macOS: `brew install ollama`. Linux: [ollama 설치 스크립트](https://ollama.com/install.sh). 이후 `ollama pull qwen3-vl:8b`.

Ollama를 설치하지 않으셔도 괜찮습니다. 기본 OCR 엔진은 Claude 자체의 비전 기능이라, 별도로 설치할 것도 Claude Code 외에 추가로 구독할 서비스도 없습니다.

### Claude Code 플러그인 마켓플레이스로 설치

Claude Code 안에서 **각 줄을 한 번에 하나씩** 실행해 주세요.

```
/plugin marketplace add https://github.com/TaewoooPark/PAIDEIA.git
```

```
/plugin install paideia@paideia-marketplace
```

> URL을 전부 적는 이유가 있습니다 — `owner/repo` 짧은 형태를 쓰면 CLI가 SSH를 먼저 시도하기 때문에, GitHub에 SSH 키가 등록돼 있지 않은 환경에서는 실패합니다. HTTPS URL을 쓰면 언제나 동작합니다.

설치가 끝나면 14개의 슬래시 명령이 `/paideia:` 네임스페이스로 제공됩니다.

### 코스별 부트스트랩

해당 코스용으로 쓰실 폴더 안에서 Claude Code를 여신 뒤 다음을 실행해 주세요.

```
/paideia:init-course
```

이 명령은 대화식으로 다음을 수행합니다.
1. Python / poppler / tesseract 의존성을 확인하고, 누락된 항목은 설치를 제안합니다 (ollama는 아래 3단계에서 `ollama` 엔진을 선택하신 경우에만 점검합니다)
2. `COURSE_NAME`, `EXAM_DATE`, `EXAM_TYPE`, `USER_WEAK_ZONES` 값을 입력받습니다
3. 기본 OCR 엔진을 고릅니다 — `claude` (네이티브 비전, 추가 설치 없음) / `ollama` (로컬 Qwen3-VL, 약 6 GB 모델을 백그라운드에서 받음) / `tesseract` (가장 가볍고 빠름, 필기 정확도는 낮음)
4. 디렉토리 골격을 생성합니다 (`materials/`, `converted/`, `course-index/`, `quizzes/`, `mock/`, `twins/`, `chain/`, `derivations/`, `cheatsheet/`, `weakmap/`, `answers/converted/`, `errors/`)
5. `.course-meta`(`OCR_ENGINE`을 담고 있으며 `/paideia:grade`가 이 값을 읽습니다)와 프로젝트 수준 `CLAUDE.md`를 작성합니다
6. `git init`을 수행해 첫 키 입력부터 준비 과정이 버전 관리되도록 합니다

개별 채점 호출에서는 엔진을 그때그때 덮어쓰실 수 있습니다. 예: `/paideia:grade --ocr=claude path/to/answer.pdf`.

---

## 읽기 팁: Obsidian을 쓰세요

Paideia는 모든 것을 LaTeX 수식(`$...$`, `$$...$$`)이 포함된 평범한 마크다운으로 씁니다. 어떤 에디터로도 읽을 수 있지만, **[Obsidian](https://obsidian.md)**이 가장 자연스러운 선택입니다.

- 별도 설정 없이 MathJax로 `$...$`, `$$...$$` 수식을 렌더링합니다
- 백링크를 통해 `quizzes/q_<ts>.md`에서 인용된 `converted/lectures/chN.md §K`로 클릭 한 번에 이동할 수 있습니다
- 코스 폴더 전체가 그 자체로 볼트(vault)입니다 — Obsidian을 `~/courses/my-course`로 향하게 하면, 모든 파일이 검색 가능한 그래프가 됩니다
- 완전히 오프라인, 무료, 로컬에서 동작합니다. Paideia의 철학과 정확히 맞닿아 있습니다 — 당신의 필기, 당신의 디스크, 당신의 도구

마크다운 수식 확장을 설치한 VS Code도 가능합니다. 다만 터미널은 — 마크다운 프리뷰를 얹더라도 — 수식을 읽기에 적합하지 않으니 억지로 맞추지 마세요.

---

## 전체 워크플로우 — 예시

### Phase 0 — 코스당 한 번 (15분)

```bash
cp ~/textbooks/ch*.pdf      ~/courses/my-course/materials/textbook/
cp ~/lecture-notes/wk*.pdf  ~/courses/my-course/materials/lectures/
cp ~/hw/hw*.pdf             ~/courses/my-course/materials/homework/
cp ~/hw/hw*_sol.pdf         ~/courses/my-course/materials/solutions/
```

Claude Code에서:

```
/paideia:ingest                     # PDF → 마크다운 (디지털 추출 + OCR 폴백)
/paideia:analyze <약점 힌트>        # 패턴 + 커버리지 + 요약 생성
/paideia:hwmap hot                  # 🔥🔥 exam-primary 영역 띄우기
```

### Phase 1 — 진단 (40분)

```
/paideia:quiz all 20                # 광범위 진단, 20문항
# 종이에 풀고 (40분), answers/diagnostic.pdf로 스캔
/paideia:grade                      # 로컬 qwen3-vl OCR + 전략 채점
```

### Phase 2 — 타겟 드릴링 (준비 시간의 대부분)

```
/paideia:weakmap                    # 우선순위 약점 리포트
/paideia:blind hw3-p2               # 이미 풀어 본 문제의 전략만 점검
/paideia:twin hw3-p2                # 같은 패턴, 새로운 표면의 변형 문제
/paideia:chain 3                    # 3개 패턴이 결합된 통합 문제
/paideia:quiz weakmap 5             # 최신 weakmap을 겨냥한 5문항
```

### Phase 3 — 통합 (약 90분)

```
/paideia:mock 90                    # 숙제 밀도로 가중된 90분 모의고사
# 종이에 풀고 answers/mock_<ts>.pdf로 스캔
/paideia:grade                      # 모의고사 채점
```

### Phase 4 — 압축 (60분, 시험 전날 밤)

```
/paideia:cheatsheet --pdf           # 오류에서 출발한 한 장짜리 치트시트
/paideia:weakmap                    # 약점 구역을 한 번 더 훑기
```

### Phase 5 — 쿨다운 (시험 10분 전)

```
/paideia:weakmap                    # 상위 3개만. 새로운 것을 배우지는 마세요.
```

---

## 명령어 (총 14개)

| 명령 | 용도 |
|------|------|
| `/paideia:init-course` | 새 코스 폴더 부트스트랩 (의존성 확인, 골격, 메타데이터 입력, 백그라운드 `ollama pull`) |
| `/paideia:ingest [--force]` | `materials/**`의 PDF를 `converted/**`의 마크다운으로 변환 (디지털 추출 + OCR 폴백) |
| `/paideia:analyze [힌트]` | `course-index/{summary,patterns,coverage}.md` 구축 |
| `/paideia:hwmap hot\|<§>` | 숙제 밀도 순으로 🔥🔥 Exam-primary 절 띄우기 |
| `/paideia:pattern <§\|Pk\|키워드>` | course-index에 있는 패턴 카드 표시 |
| `/paideia:derive <타겟>` | `derivations/<slug>.md`에 정돈된 참조 유도 저장 |
| `/paideia:quiz <주제\|§\|weakmap> [N]` | N개 연습 문항 생성, 답은 형제 `_answers.md`에 숨김 |
| `/paideia:blind <problem-id>` | 이미 본 문제의 전략만 확인하는 드릴 (재풀이 아님, 접근 기술) |
| `/paideia:twin <problem-id>` | 같은 패턴, 새 표면의 변형 문제 |
| `/paideia:chain <N>` | N개 패턴을 묶은 통합 문제 |
| `/paideia:mock <분>` | 숙제 밀도 가중 모의고사 전체 |
| `/paideia:grade [--ocr=<engine>] [경로]` | `.course-meta`의 엔진 선택(Claude 비전 / Ollama / Tesseract)으로 OCR 후 전략 채점, `errors/log.md`에 누적 기록 |
| `/paideia:weakmap [개념]` | `weakmap/weakmap_<ts>.md`에 저장되는 우선순위 약점 리포트 |
| `/paideia:cheatsheet [--pdf]` | 오류 주도 한 장짜리 치트시트 |

---

## 내부 구조

### 필기 OCR: 세 가지 엔진 중에서 직접 고르실 수 있습니다

사용자는 채팅에 수식을 타이핑하지 않습니다. 종이에 풀고, PDF로 스캔하고, 그 PDF를 `answers/`에 떨어뜨리신 뒤 `/paideia:grade`를 실행하시면 됩니다. 플러그인은 세 엔진 중 선택하신 엔진으로 스캔본을 마크다운으로 바꿉니다. 기본 엔진은 코스별 `.course-meta`의 `OCR_ENGINE`으로 지정하며, 개별 호출에서는 `/paideia:grade --ocr=<engine>`로 덮어쓰실 수 있습니다.

| 엔진 | 기본값? | 동작 방식 | 이럴 때 고르세요 |
|---|---|---|---|
| `claude` | **예** | `pdftoppm`으로 페이지별 PNG 렌더링 → Claude가 각 PNG를 직접 읽어 한 번에 마크다운으로 합성. 별도 모델도, 서브프로세스도, 설치도 필요하지 않습니다. | 가장 마찰이 적은 기본 경로. 한국어·LaTeX 모두 강하고 모델 로딩 지연도 없습니다. |
| `ollama` | 선택 | `vision_ocr.py --engine=ollama` — 로컬 Qwen3-VL 8B, 실패 시 자동으로 tesseract로 폴백합니다. | 페이지 이미지조차 Anthropic 서버에 보내고 싶지 않으실 때. 최초 `ollama pull qwen3-vl:8b` (~6 GB)가 필요합니다. |
| `tesseract` | 선택 | `vision_ocr.py --engine=tesseract` — pytesseract `eng+kor`만 사용합니다. | 가장 빠르고 가볍습니다. 타이핑된 스캔엔 괜찮고, 필기엔 정확도가 낮습니다. |

세 엔진 모두 `answers/converted/<stem>.md`에 `<!-- SOURCE: ... -->` / `<!-- TIER: ... -->` 헤더 코멘트를 남기므로, `/paideia:grade`가 OCR 신뢰도가 낮을 때 그에 맞게 태도를 바꿀 수 있습니다.

기본 엔진(`claude`)은 의도적으로 가장 마찰이 적은 선택으로 잡았습니다 — Claude Code에 이미 포함된 것만으로 충분합니다. `ollama` 엔진은 페이지 이미지 자체에 대해 단단한 프라이버시 경계를 원하실 때를 위해, `tesseract` 엔진은 다른 엔진을 쓸 수 없을 때의 안정적인 하한선으로 남겨져 있습니다.

### 라인 단위가 아닌, 전략 기반 채점

손으로 쓴 수식의 OCR 잡음은 엄격한 대수식 채점을 사실상 쓸모없게 만듭니다 — 한 글자 `∫` ↔ `∑` 오독이 전체를 무너뜨리기 때문입니다. 더 중요한 사실은, **시험의 실제 병목은 패턴 인식이지 산수가 아니라는 점**입니다. 그래서 채점기는 문항마다 세 가지를 확인합니다.

1. **패턴 (Pattern)** — `course-index/patterns.md`에서 올바른 Pk를 골랐는지
2. **변수 (Variables)** — 올바른 치환 / 기저 / 인덱스 / 경로를 식별했는지
3. **최종 형태 (End-form)** — 최종 표현의 모양(차원, 점근, 구조)이 맞는지

오류는 타입이 지정된 분류(`pattern-missed | wrong-variable | wrong-end-form | algebraic | sign | definition`)와 함께 YAML 형태로 `errors/log.md`에 기록됩니다. 이 로그가 `/paideia:weakmap`의 씨앗이자, `/paideia:cheatsheet --pdf`의 *유일한* 입력이 됩니다.

### *당신의* 풀이에서 추출된 패턴

`/paideia:analyze`는 일반적인 "미적분 기법" 목록을 배포하는 도구가 아닙니다. 당신 과목의 실제 해답지를 읽어 반복되는 풀이 패턴을 추출하고, P1, P2, … 로 라벨을 붙인 뒤, 당신 자신의 `converted/solutions/` 파일을 인용하는 worked instance를 함께 제공합니다. 패턴은 *당신 과목 고유의 관용구*이지 어떤 교과서의 것도 아닙니다. 복소해석 수업에서 P3는 "닫힌 경로 + Jordan's lemma + 본질 특이점에서의 residue"일 수 있고, 선형 시스템 수업에서 P3는 "부분분수 + 복소극점을 갖는 역Laplace"일 수 있습니다. 각 분야는 자신만의 손놀림을 가지고 있고, 그것은 과목 자신을 통해서만 드러납니다.

### Append-only 이력

`weakmap/` 디렉토리는 절대 덮어쓰지 않습니다. `/paideia:weakmap`을 호출할 때마다 `weakmap/weakmap_<ISO-timestamp>.md`가 새로 생성됩니다. `git log weakmap/`를 통해 어떤 약점이 가장 먼저 무너졌는지, 어떤 약점이 끈질기게 남아 있었는지, 진단 모의고사 이후 어떤 새로운 약점이 등장했는지 정확히 확인할 수 있습니다. "자신의 이해를 시간 축 위에서 `git diff`한다"는 발상이 실제로 구현된 지점이 이곳입니다.

---

## 배포물

```
PAIDEIA/
├── .claude-plugin/marketplace.json      # 마켓플레이스 매니페스트
├── LICENSE                              # MIT
├── README.md                            # 영문
├── README.ko.md                         # 본 파일
└── plugins/paideia/
    ├── .claude-plugin/plugin.json       # 플러그인 매니페스트
    ├── README.md                        # 빠른 참조 카드
    ├── skills/
    │   ├── pdf/SKILL.md                 # 디지털 + 기본 OCR
    │   ├── vision-ocr/SKILL.md          # Claude 비전(기본) + Ollama Qwen3-VL + tesseract
    │   ├── course-builder/SKILL.md      # ingest + analyze 파이프라인
    │   ├── exam-drill/
    │   │   ├── SKILL.md                 # 드릴 기본 단위 (twin, blind, chain, mock)
    │   │   └── twin-recipe.md           # 변형 생성 불변식 규칙
    │   └── answer-processing/SKILL.md   # 필기 OCR 결과의 전략 채점
    ├── commands/                        # 14개 슬래시 명령
    │   ├── init-course.md  ingest.md    analyze.md   hwmap.md
    │   ├── pattern.md      derive.md    quiz.md      blind.md
    │   ├── twin.md         chain.md     mock.md      grade.md
    │   └── weakmap.md      cheatsheet.md
    └── scripts/vision_ocr.py            # 선택적 사용: --ocr=ollama|tesseract 경로에서 쓰는 ollama qwen3-vl + tesseract 드라이버
```

---

## 설계 원칙

1. **터미널은 수식 읽기에 나쁩니다.** Claude는 마크다운 파일을 만들고, 당신은 그것을 (가능하면 Obsidian에서) 읽습니다.
2. **풀이를 타이핑하는 일은 느리고 오류에 취약합니다.** 종이에 풀고 스캔하면, 플러그인이 로컬에서 OCR을 처리합니다.
3. **OCR 잡음은 피할 수 없습니다.** 그래서 채점은 전략 기반(패턴 / 변수 / 최종 형태)으로 이뤄집니다 — 라인별 대수 검증이 아니라요. 실제 시험 채점자가 보는 것과 동일한 관점이기도 합니다.
4. **패턴은 *당신 과목의* 풀이에서 추출되어야 합니다** — 범용 목록에서가 아니라요. 각 분야는 고유한 관용구를 가지며, 그 관용구는 해당 과목 자신을 통해서만 드러납니다.
5. **당신의 오류는 가장 가치 있는 학습 신호입니다** — 교과서보다, 강의보다 더요. 치트시트는 실러버스가 아니라 `errors/log.md`에서 생성됩니다.
6. **숙제 밀도가 시험을 알려 줍니다.** 당신의 시간은 유한하니, 점수가 있는 곳에 쓰세요.
7. **클라우드도, 구독도, 락인도 없습니다.** Paideia가 망가지거나 당신이 떠나더라도, 모든 산출물은 당신의 git 이력 아래 있는 평범한 마크다운입니다. 내보내야 할 것도, 잃을 것도 없습니다.

---

## FAQ

**수학 과목이 아닌 경우에도 쓸 수 있나요?**
문제-패턴 추출을 중심으로 설계되어 있어, 정량 분야에서 강점을 가장 잘 드러냅니다: 수학, 물리, 전자공학, 전산 이론, 머신러닝 이론, 통계, 공학 등입니다. 역사나 문학 같은 과목에서도 인제스트와 요약은 동작하지만, 드릴 명령은 "문제에 풀이 패턴이 존재한다"는 전제를 두고 있습니다.

**한국어·영어가 섞인 자료도 되나요?**
됩니다. 인제스트와 OCR이 `eng+kor`로 설정되어 있고, 패턴과 채점 응답도 원자료의 언어 구성을 그대로 따라갑니다.

**비용은 얼마인가요?**
0원입니다. MIT 라이선스입니다. `qwen3-vl:8b`는 오픈 웨이트 모델이고, ollama·tesseract·poppler·reportlab 모두 무료입니다.

**Ollama / Qwen3-VL이 꼭 필요한가요?**
아니요. 기본 OCR 엔진은 Claude 자체의 비전 기능입니다 — 이미 사용 중이신 Claude Code 세션 안에서 동작하고, 추가로 설치할 것이 없습니다. Ollama + `qwen3-vl:8b`는 페이지 이미지까지 기기 안에 붙잡아 두고 싶으실 때(= Anthropic 서버에도 보내지 않고 싶으실 때)를 위한 선택 경로입니다. `tesseract`는 설치를 최소로 하고 싶거나 타이핑된 스캔만 다루실 때를 위한 세 번째 옵션입니다.

**`qwen3-vl:8b`를 선택했는데 제 기기가 감당하지 못하면요?**
`vision_ocr.py` 드라이버가 Ollama 실패 시 자동으로 tesseract `eng+kor`로 폴백합니다. 또는 `.course-meta`의 `OCR_ENGINE`을 `claude`로 바꾸시거나 `--ocr=claude`를 붙이시면 Ollama를 완전히 우회할 수 있습니다.

**LLM이 매긴 채점 결과를 믿어도 되나요?**
채점은 전략 기반(대수식 검증이 아니라 패턴 매칭)이며, 채점기는 `course-index/patterns.md`의 패턴을 인용하고, 모든 채점은 `errors/log.md`에 감사 가능한 YAML 항목으로 남습니다. 혹시 채점이 잘못되었다면 해당 YAML 항목만 수정하시면 됩니다 — 다음 `/paideia:weakmap`이 수정 사항을 반영합니다.

**제 데이터는 외부로 나가지 않나요?**
PDF·마크다운·오류 로그·weakmap은 모두 로컬 코스 폴더 안에만 머물며, 어떤 제3자 서비스로도 업로드되지 않습니다. 플러그인이 일으키는 네트워크 트래픽은 선택하신 OCR 엔진에 따라 달라집니다. `claude`(기본)를 고르시면 페이지 이미지는 이미 쓰고 계신 Claude Code 세션을 따라 흐릅니다(= 평소 Claude Code 대화에서 이미 일어나는 경로와 동일, 새로운 무언가가 추가되지는 않습니다). `ollama`를 고르시면 최초 모델 다운로드 이후에는 어떠한 데이터도 기기 밖으로 나가지 않습니다. `tesseract`는 아무 때도 네트워크를 타지 않습니다.

---

## 연락

<p align="center">
  <a href="https://github.com/TaewoooPark"><img src="https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github&logoColor=white&cacheSeconds=3600" alt="GitHub"></a>
  <a href="https://x.com/theoverstrcture"><img src="https://img.shields.io/badge/-X-000000?style=for-the-badge&logo=x&logoColor=white&cacheSeconds=3600" alt="X (Twitter)"></a>
  <a href="https://www.linkedin.com/in/taewoo-park-427a05352"><img src="https://img.shields.io/badge/-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&cacheSeconds=3600" alt="LinkedIn"></a>
  <a href="https://www.instagram.com/t.wo0_x/"><img src="https://img.shields.io/badge/-Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white&cacheSeconds=3600" alt="Instagram"></a>
  <a href="mailto:ptw151125@kaist.ac.kr"><img src="https://img.shields.io/badge/-Email-D14836?style=for-the-badge&logo=gmail&logoColor=white&cacheSeconds=3600" alt="Email"></a>
</p>

---

## 라이선스

MIT. 자유롭게 쓰시고, 본인 과목에 맞춰 수정하셔도 됩니다. 기여도 환영합니다 — 다만 이 플러그인의 핵심은 **공부를 이어가기 위해 누군가의 upstream에 기대지 않아도 된다는 것**임을 잊지 말아 주세요.

---

<p align="center">
  <em>교육은 구독이 아닙니다. 원래부터 그랬던 적이 없습니다.<br>
  Παιδεία — 임대가 아닌, 형성.</em>
</p>
