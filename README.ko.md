<h1 align="center">ΠΑΙΔΕΙΑ · Paideia</h1>

<p align="center">
  <strong>당신의 배움을 구독하지 마라.</strong><br>
  <em>당신의 자료로, 당신의 컴퓨터 위에서, 구독료 없이 시험 대비 상태를 형성해 주는 Claude Code 플러그인.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/github/license/TaewoooPark/PAIDEIA?style=flat-square&labelColor=000000&color=333333" alt="라이선스">
  <img src="https://img.shields.io/github/stars/TaewoooPark/PAIDEIA?style=flat-square&logo=github&logoColor=white&labelColor=000000&color=333333" alt="GitHub 스타 수">
  <img src="https://img.shields.io/github/last-commit/TaewoooPark/PAIDEIA?style=flat-square&labelColor=000000&color=333333" alt="최근 커밋">
  <img src="https://img.shields.io/github/repo-size/TaewoooPark/PAIDEIA?style=flat-square&labelColor=000000&color=333333" alt="저장소 크기">
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
  <strong>태그:</strong> <code>시험대비</code> · <code>학습</code> · <code>수학</code> · <code>물리</code> · <code>공학</code> · <code>claude-code-plugin</code> · <code>local-first</code> · <code>OCR</code> · <code>qwen3-vl</code> · <code>ollama</code> · <code>필기인식</code> · <code>마크다운</code> · <code>obsidian</code>
</p>

<p align="center">
  <a href="./README.md">English README</a>
</p>

---

<p align="center">
  <em>교과서는 원래 당신 것이었다. 강의는 원래 당신 것이었다. 필기는 원래 당신 것이었다.<br>
  Paideia는 단지, 당신이 이미 소유한 이해에 매달 월세를 내는 것을 멈추게 해 줄 뿐이다.</em>
</p>

---

## Paideia의 뜻

고대 그리스에서 **Παιδεία(파이데이아)**는 수동적인 학생에게 사실을 예치하는 일이 결코 아니었다. 그것은 원전과의 구조화된 만남, 스승 아래에서의 연습, 피드백을 더 깊은 수정에 되먹이는 성찰적 대화를 통한 — 완전한 인간의 평생에 걸친 형성이었다.

본 플러그인은 이 순환을 **수학, 물리, 공학 과목의 시험 대비**라는 한정된 문제에 적용한다.

```
  ingest ──▶ analyze ──▶ drill ──▶ grade ──▶ weakmap ──▶ cheatsheet
     ▲                                                        │
     └────────────────── feedback loop ───────────────────────┘
```

모든 단계는 당신의 코스 폴더에 영원히 남는 마크다운 아티팩트를 생성한다. 아무것도 휘발되지 않는다. 아무것도 API 뒤에 숨어 있지 않다. 다음 자금 겨울이 와도 아무것도 멈추지 않는다.

---

## 이 플러그인이 대체하는 것

교육 산업은 이해가 구독하는 서비스라고 학생들을 설득해 왔다.

- **Coursera, edX, Khan Academy Premium** — 유튜브에서 볼 수 있는 강의의 접근권을 판매한다.
- **Quizlet Plus, Anki cloud, Brainscape** — 당신 자신의 필기로 만든 플래시카드를 수익화한다.
- **Chegg, Course Hero** — 도서관이 교과서와 함께 제공하는 것과 동일한 해답지를 유료화한다.
- **Brilliant, Duolingo Max, Khanmigo** — 토큰 비용이 1센트의 몇 분의 일에 불과한 LLM과의 대화에 월 구독료를 매긴다.
- **ChatGPT Study Mode, Gemini "Deep Study", NotebookLM** — 당신의 사적 학습 자료 전체를 타인의 서버에 업로드시키고, 그것으로 학습시키고, 그러면서도 요금을 청구한다.

이 중 어느 것도 이해를 *형성*하지 않는다. 그들은 이해를 **임대**한다 — 당신이 결제를 멈추는 순간까지, 서비스가 종료되는 순간까지, 다음 정렬(alignment) 패스에서 모델이 로보토미를 당하는 순간까지. 결제가 실패하는 순간, 공급자가 피벗하는 순간, 정책이 바뀌는 순간 — 당신의 학습 환경은 증발한다.

Paideia는 그것의 반격이다. 지능은 당신의 디스크 위에 거주한다. 아티팩트는 당신이 소유하는 마크다운 파일이다. OCR은 당신의 RAM에서 돌아가는 VLM 위에서 수행된다. 구독할 것도, 취소할 것도, 잃을 것도 없다.

| 역량 | Paideia | 일반 교육 SaaS |
|-----|---------|----------------|
| PDF가 존재하는 장소 | 당신의 디스크, 끝 | 업로드됨, 파싱됨, 보관됨 |
| 필기한 답안의 행방 | `answers/`, 로컬 ollama 위 Qwen3-VL 8B로 OCR | "AI 채점"을 위해 업로드됨 |
| 오류 로그의 위치 | `errors/log.md` — 평범한 YAML 파일 | 독점 DB, 유료 티어에서만 내보내기 가능 |
| 치트시트 렌더링 장소 | 로컬 마크다운 + reportlab PDF | 로그인 뒤의 웹 뷰어 |
| 서비스 종료 시 잃는 것 | 없음 | 전부 |
| 월 사용료 | $0 | $8–$25 |
| 시간에 따른 자신의 이해를 `git diff` | 가능 | 불가능 |
| 시험 전날 비행기에서 오프라인으로 작동 | 가능 | 대개 불가능 |

네트워크를 건드리는 유일한 구성요소는 `ollama pull qwen3-vl:8b` — 약 6 GB의 모델 가중치 일회성 다운로드다. 그 뒤로 모든 추론은 로컬이다.

---

## 핵심 원리: HW 밀도 = 시험 출제 확률

대부분의 "똑똑하게 공부하기" 조언은 사각지대를 사냥하라고 말한다. 그것은 **거꾸로** 된 조언이다. 교수는 이미 숙제 배정을 통해 시험 포인트가 어디 있는지 *말해 주었다*. 숙제가 몰린 절은 🔥🔥 Exam-primary. 숙제가 전혀 없는 절은 ⚪ Low-risk — "숨은 함정"이 아니다. 교수의 누락은 해당 주제가 시험 바깥이라는 가장 강력한 신호다.

Paideia의 순위는 이 원리를 명시적으로 반영한다. 모든 드릴 명령이 기본적으로 이 티어링을 따른다.

| 티어 | 해당 절의 HW 수 | 처리 방식 | 모의고사 점수 비중 |
|------|-----------------|-----------|--------------------|
| 🔥🔥 Exam-primary | 3+ | 가장 먼저, 가장 많이 드릴 | ≥70% |
| 🔥 Exam-likely | 2 | 다음 드릴 | ~25% |
| 🟡 Exam-possible | 1 | 워밍업 복습 | ≤5% |
| ⚪ Low-risk | 0 | 참조/독서만 | 0 |

`/paideia:quiz all`, `/paideia:mock`, `/paideia:hwmap hot`은 모두 이 가중치를 따른다. ⚪ 절을 고집해서 드릴하겠다고 하면, 플러그인은 한 번은 따라 주지만 출제 확률이 낮음을 경고한다. 당신의 제한된 시간은 상상 속 함정보다 가치 있다.

---

## 형성 사이클, 단계별

| 단계 | 무엇을 하는가 | 명령 | 산출물 |
|------|---------------|------|--------|
| **대면 (Encounter)** | 교수의 신호를 읽는다 | `/paideia:ingest` | `converted/**/*.md` — 모든 강의 노트, 교재 챕터, 숙제, 풀이를 깨끗한 마크다운으로 |
| **구조화 (Structure)** | 과목의 문법을 추출한다 | `/paideia:analyze` | `course-index/{summary,patterns,coverage}.md` — 주제 트리, 반복되는 풀이 패턴 (P1..Pk), HW 밀도 기반 출제 티어 |
| **연습 (Practice)** | 교수가 실제로 시험하는 것에 가중된 능동 회상 | `/paideia:quiz`, `/paideia:twin`, `/paideia:blind`, `/paideia:chain`, `/paideia:mock` | `quizzes/`, `twins/`, `chain/`, `mock/` — 종이로 푸는 문제들 |
| **성찰 (Reflection)** | 당신의 필기가 채점된 점수로 | `/paideia:grade` | `answers/converted/<name>.md` + `errors/log.md` — 로컬 Qwen3-VL OCR, 전략 기반 채점 |
| **진단 (Diagnosis)** | 오류를 우선순위화된 약점 리포트로 압축 | `/paideia:weakmap` | `weakmap/weakmap_<ts>.md` — append-only 이력 |
| **증류 (Distillation)** | 한 장, 오류 주도, 인쇄 가능 | `/paideia:cheatsheet`, `/paideia:derive`, `/paideia:pattern` | `cheatsheet/final.md`, `derivations/<slug>.md` — 정말로 필요한 것만 참조 |

보조: `/paideia:hwmap`은 HW-density 기반 출제 확률을 띄운다. `/paideia:init-course`는 새 코스 폴더를 부트스트랩한다.

---

## 설치

### 사전 조건

- [Claude Code](https://claude.ai/claude-code) CLI
- Python 3.9+ (플러그인이 의존성을 확인하고 설치를 제안함)
- **macOS**: `brew install poppler tesseract tesseract-lang ollama`
- **Linux (Debian/Ubuntu)**: `apt-get install poppler-utils tesseract-ocr tesseract-ocr-kor` + [ollama 설치 스크립트](https://ollama.com/install.sh)
- `qwen3-vl:8b` 모델용 여유 디스크 ~6 GB (Tier-1 필기 OCR)

### Claude Code 플러그인 마켓플레이스로 설치

```bash
# Claude Code 안에서:
/plugin marketplace add TaewoooPark/PAIDEIA
/plugin install paideia@paideia-marketplace
```

설치 후 14개의 슬래시 명령이 `/paideia:` 네임스페이스로 사용 가능해진다.

### 코스별 부트스트랩

```bash
mkdir -p ~/courses/my-course && cd ~/courses/my-course
```

해당 디렉토리에서 Claude Code를 연 뒤:

```
/paideia:init-course
```

대화식으로 다음을 수행한다.
1. Python / tesseract / ollama 의존성 확인, 누락된 것은 설치 제안
2. 모델이 없으면 백그라운드에서 `ollama pull qwen3-vl:8b` 시작
3. 디렉토리 골격 생성 (`materials/`, `converted/`, `course-index/`, `quizzes/`, `mock/`, `twins/`, `chain/`, `derivations/`, `cheatsheet/`, `weakmap/`, `answers/converted/`, `errors/`)
4. `COURSE_NAME`, `EXAM_DATE`, `EXAM_TYPE`, `USER_WEAK_ZONES` 입력
5. 프로젝트 수준 `CLAUDE.md`를 해당 값으로 작성
6. `git init` — 첫 키 입력부터 당신의 대비 이력이 버전 관리된다

---

## 읽기 팁: Obsidian을 쓰세요

Paideia는 모든 것을 LaTeX 수식(`$...$`, `$$...$$`)이 들어간 평범한 마크다운으로 쓴다. 어떤 에디터로도 읽을 수 있지만, **[Obsidian](https://obsidian.md)**이 자연스러운 선택이다.

- 설정 없이 MathJax로 `$...$`, `$$...$$` 수식을 렌더링한다
- 백링크로 `quizzes/q_<ts>.md`에서 인용된 `converted/lectures/chN.md §K`로 한 번의 클릭에 점프할 수 있다
- 코스 폴더 전체가 볼트(vault)다 — Obsidian을 `~/courses/my-course`에 겨누기만 하면, 모든 것이 검색 가능한 그래프가 된다
- 완전 오프라인, 무료, 로컬. Paideia의 철학과 일치한다: 당신의 필기, 당신의 디스크, 당신의 도구

마크다운-수식 확장을 단 VS Code도 가능하다. 터미널은 — 마크다운 프리뷰를 얹어도 — 수학을 읽기에 나쁘다. 그것과 싸우지 말자.

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
# 종이로 풀이 (40분), answers/diagnostic.pdf로 스캔
/paideia:grade                      # 로컬 qwen3-vl OCR + 전략 채점
```

### Phase 2 — 타겟 드릴링 (대비 시간의 대부분)

```
/paideia:weakmap                    # 우선순위 약점 리포트
/paideia:blind hw3-p2               # 기지(既知) 문제에 대한 전략만 점검
/paideia:twin hw3-p2                # 같은 패턴, 새 표면의 변형 문제
/paideia:chain 3                    # 3개 패턴 통합 문제
/paideia:quiz weakmap 5             # 최신 weakmap을 겨냥한 5문항
```

### Phase 3 — 통합 (약 90분)

```
/paideia:mock 90                    # HW 밀도로 가중된 90분 모의고사
# 종이로 풀이, answers/mock_<ts>.pdf로 스캔
/paideia:grade                      # 모의고사 채점
```

### Phase 4 — 압축 (60분, 시험 전날 밤)

```
/paideia:cheatsheet --pdf           # 오류 주도 한 장짜리 치트시트
/paideia:weakmap                    # 약점 구역 한 번 더 훑기
```

### Phase 5 — 쿨다운 (시험 10분 전)

```
/paideia:weakmap                    # 상위 3개만. 새로운 것을 배우지 말 것.
```

---

## 명령어 (총 14개)

| 명령 | 용도 |
|------|------|
| `/paideia:init-course` | 새 코스 폴더 부트스트랩 (의존성 확인, 골격, 메타데이터 입력, 백그라운드 `ollama pull`) |
| `/paideia:ingest [--force]` | `materials/**`의 PDF → `converted/**`의 마크다운 (디지털 추출 + OCR 폴백) |
| `/paideia:analyze [힌트]` | `course-index/{summary,patterns,coverage}.md` 구축 |
| `/paideia:hwmap hot\|<§>` | HW 밀도 순으로 🔥🔥 Exam-primary 절 띄우기 |
| `/paideia:pattern <§\|Pk\|키워드>` | course-index의 패턴 카드 표시 |
| `/paideia:derive <타겟>` | `derivations/<slug>.md`로 정돈된 참조 유도 저장 |
| `/paideia:quiz <주제\|§\|weakmap> [N]` | N개 연습 문항, 답은 형제 `_answers.md`에 숨김 |
| `/paideia:blind <problem-id>` | 기지 문제에 대한 전략 확인 드릴 (풀이 아님, 접근 기술) |
| `/paideia:twin <problem-id>` | 기지 문제의 변형 — 같은 패턴, 새 표면 |
| `/paideia:chain <N>` | N개 패턴이 결합된 통합 문제 |
| `/paideia:mock <분>` | HW 밀도 가중 모의고사 전체 |
| `/paideia:grade [경로]` | 로컬 Qwen3-VL OCR + 전략 채점, `errors/log.md`에 누적 |
| `/paideia:weakmap [개념]` | `weakmap/weakmap_<ts>.md`에 저장되는 우선순위 약점 리포트 |
| `/paideia:cheatsheet [--pdf]` | 오류 주도 한 장짜리 치트시트 |

---

## 내부 구조

### 필기 OCR: 계층적, 로컬

사용자는 채팅에 수식을 타이핑하지 않는다. 종이로 풀고, PDF로 스캔하고, PDF를 `answers/`에 떨어뜨리고, `/paideia:grade`를 실행한다. 플러그인은 2단계 로컬 OCR 파이프라인으로 스캔을 마크다운으로 변환한다.

```
answers/<stem>.pdf
  ↓ python3 ${CLAUDE_PLUGIN_ROOT}/scripts/vision_ocr.py <pdf> <md>
  ↓   Tier 1: qwen3-vl:8b via ollama  (keep_alive 15m, warmup, ≤1600px JPEG)
  ↓   Tier 2: pytesseract eng+kor     (예외 시 자동 폴백)
answers/converted/<stem>.md           ← /grade가 읽는 `<!-- SOURCE / TIER -->` 헤더 포함
```

Qwen3-VL 8B는 현재 소비자용 RAM에 올라가면서 수학 필기를 잘 읽는 최강 오픈 웨이트 VLM이다. [ollama](https://ollama.com)로 실행되며, 호출 사이에 모델을 웜 상태로 유지해 후속 채점이 빠르다. 어떤 이유로든 모델이 불가용하면 파이프라인은 조용히 pytesseract `eng+kor`로 폴백한다 — 정확도는 낮지만 늘 사용 가능하다.

### 라인 단위가 아닌, 전략 기반 채점

필기 수식의 OCR 잡음은 엄격한 대수식 채점을 쓸모없게 만든다 — 한 글자 `∫` ↔ `∑` 오독이 전체를 무너뜨린다. 더 중요한 것: **시험의 실제 병목은 패턴 인식이지, 산수가 아니다.** 따라서 채점기는 문항마다 세 가지를 본다.

1. **패턴 (Pattern)** — `course-index/patterns.md`의 올바른 Pk를 골랐는가?
2. **변수 (Variables)** — 올바른 치환 / 기저 / 인덱스 / 경로를 식별했는가?
3. **최종 형태 (End-form)** — 최종 표현의 모양(차원, 점근, 구조)이 맞는가?

오류는 타입이 지정된 분류(`pattern-missed | wrong-variable | wrong-end-form | algebraic | sign | definition`)와 함께 YAML로 `errors/log.md`에 기록된다. 이 로그가 `/paideia:weakmap`의 씨앗이자 `/paideia:cheatsheet --pdf`의 *유일한* 입력이다.

### *당신의* 풀이에서 추출된 패턴

`/paideia:analyze`는 일반적인 "미적분 기법" 목록을 배포하지 않는다. 당신의 실제 해답지를 읽고, 반복되는 풀이 패턴을 추출해 P1, P2, … 로 라벨링하며, 당신 자신의 `converted/solutions/` 파일을 인용하는 worked instance를 붙인다. 패턴은 *당신 과목의 관용구*이지 교과서의 것이 아니다. 복소해석 과목에서 P3는 "닫힌 경로 + Jordan's lemma + 본질 특이점에서의 residue"일 수 있다. 선형 시스템 과목에서 P3는 "부분분수 + 복소극점을 갖는 역Laplace"일 수 있다. 모든 분야는 자신만의 동작을 가진다; 과목 자신만이 그것을 드러낸다.

### Append-only 이력

`weakmap/`은 결코 덮어쓰지 않는다. `/paideia:weakmap` 호출마다 `weakmap/weakmap_<ISO-timestamp>.md`가 생성된다. `git log weakmap/`로 어떤 약점이 가장 먼저 무너졌는지, 어떤 것이 끈질겼는지, 진단 모의고사 후 어떤 새 약점이 나타났는지를 정확히 볼 수 있다. "시간에 따른 자신의 이해를 `git diff`한다"의 실천이다.

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
    │   ├── vision-ocr/SKILL.md          # Qwen3-VL Tier 1 + tesseract Tier 2
    │   ├── course-builder/SKILL.md      # ingest + analyze 파이프라인
    │   ├── exam-drill/
    │   │   ├── SKILL.md                 # 드릴 기본 단위 (twin, blind, chain, mock)
    │   │   └── twin-recipe.md           # 변형 생성 불변식 규칙
    │   └── answer-processing/SKILL.md   # 필기 OCR 산출물의 전략 채점
    ├── commands/                        # 14개 슬래시 명령
    │   ├── init-course.md  ingest.md    analyze.md   hwmap.md
    │   ├── pattern.md      derive.md    quiz.md      blind.md
    │   ├── twin.md         chain.md     mock.md      grade.md
    │   └── weakmap.md      cheatsheet.md
    └── scripts/vision_ocr.py            # tesseract 폴백을 갖춘 ollama qwen3-vl 드라이버
```

---

## 설계 신념

1. **터미널은 수학에 나쁘다.** Claude는 마크다운 파일을 생산한다; 당신은 (가능하면 Obsidian으로) 그것을 읽는다.
2. **풀이를 타이핑하는 것은 느리고 오류에 취약하다.** 종이로 풀고, 스캔하고, 플러그인이 로컬에서 OCR한다.
3. **OCR 잡음은 불가피하다.** 그래서 채점은 전략 기반(패턴 / 변수 / 최종 형태)이지 라인별 대수가 아니다. 이는 실제 시험 채점자가 보는 것이기도 하다.
4. **패턴은 *당신 과목의* 풀이에서 추출되어야 한다** — 일반 목록에서가 아니다. 모든 분야는 자신의 관용구를 가진다.
5. **당신의 오류가 가장 가치 있는 학습 신호다** — 교과서보다, 강의보다. 치트시트는 `errors/log.md`에서 생성된다, 실러버스가 아니다.
6. **HW 밀도가 시험을 알려 준다.** 당신의 시간은 유한하다; 점수가 있는 곳에 쓰자.
7. **클라우드 없음, 구독 없음, 락인 없음.** Paideia가 망가지거나 당신이 떠나도, 모든 아티팩트는 당신의 git 이력 아래 있는 평범한 마크다운이다. 내보낼 것도 잃을 것도 없다.

---

## FAQ

**수학 외 과목에서도 되나요?**
문제-패턴 추출 중심으로 설계되어 있어, 정량 분야에서 빛을 발한다: 수학, 물리, 전자공학, 전산 이론, ML 이론, 통계, 공학. 역사나 문학에서도 인제스트와 요약은 되지만, 드릴 명령어는 문제에 풀이 패턴이 있다고 가정한다.

**한영 혼합 자료도 되나요?**
된다. 인제스트와 OCR이 `eng+kor`로 구성되어 있다. 패턴과 채점 응답도 원자료의 언어 믹스를 따른다.

**비용은?**
0원. MIT 라이선스. `qwen3-vl:8b`는 오픈 웨이트. ollama, tesseract, poppler, reportlab 모두 무료.

**`qwen3-vl:8b`가 불가용하거나 기기가 못 돌리면?**
파이프라인이 자동으로 tesseract `eng+kor`로 폴백한다. 채점은 여전히 동작한다; 필기 OCR 정확도만 낮아진다.

**LLM 채점을 신뢰할 수 있나요?**
채점은 전략 기반(대수가 아닌 패턴 매칭)이고, 채점기는 `course-index/patterns.md`의 패턴을 인용하며, 모든 채점은 `errors/log.md`에 감사 가능한 YAML 항목을 쓴다. 채점이 틀렸다면 YAML 항목을 고치면 된다 — 다음 `/paideia:weakmap`이 수정을 반영한다.

**내 데이터는 사적인가요?**
당신의 PDF, 마크다운, 오류, weakmap — 모두 당신 로컬 코스 폴더에 산다. 플러그인은 아무것도 업로드하지 않는다. `ollama pull qwen3-vl:8b`는 ollama.com에서의 일회성 모델 다운로드이며, 그 뒤 추론은 당신의 기기에서 돈다.

---

## 연락

<p align="center">
  <a href="https://github.com/TaewoooPark"><img src="https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
  <a href="https://x.com/theoverstrcture"><img src="https://img.shields.io/badge/-X-000000?style=for-the-badge&logo=x&logoColor=white" alt="X (Twitter)"></a>
  <a href="https://www.linkedin.com/in/taewoo-park-427a05352"><img src="https://img.shields.io/badge/-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://www.instagram.com/t.wo0_x/"><img src="https://img.shields.io/badge/-Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram"></a>
  <a href="mailto:ptw151125@kaist.ac.kr"><img src="https://img.shields.io/badge/-Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
</p>

---

## 라이선스

MIT. 자유롭게 사용하라. 자신의 과목용으로 수정하라. 기여도 환영한다 — 다만 플러그인의 핵심은 **공부를 이어가기 위해 누군가의 upstream에 기대지 않아도 되게 만드는 것**이라는 점을 기억하자.

---

<p align="center">
  <em>교육은 구독이 아니다. 원래 그런 적이 없다.<br>
  Παιδεία — 임대가 아닌, 형성.</em>
</p>
