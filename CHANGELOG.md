# CHANGELOG — ai-ops-7142

История доработок плагина по волнам (П — production polishing, Т — таргетированный стресс-тест ниш).

Формат записи: **волна** / **commit** / **главное** / **затронутые файлы**.

---

## Волна Т.8 — EU_RUSSIAN_DIASPORA_PRESET (sub-profile sanctions+GDPR+cross-border)

**Commit:** `acaf26f` (2026-05-19)

**3 агента параллельно** (T.8-A создатель + T.8-B адверсариал 18 GAP + T.8-C мета cross-ref 6 юрисдикций). Закрыты 8 потерянных слоёв для русскоязычной диаспоры в EU/UK/IL post-2022.

**Главное:**
- `EU_RUSSIAN_DIASPORA_PRESET` — sub-profile (накладывается на вертикаль, не заменяет) — 8 правил + 8/8 PASS чек-лист + 3-STEP FUNNEL: (1) Workspace + НЕТ cultural-loaded music post-2022, (2) DIASPORA-TONE casting + regulated-attire AI guardrail (мантия адвоката = uniform-as-claim-of-profession), (3) GDPR Art.6+9 (запрет language-based lookalike + Russian Orthodox affinity + EDPB Guidelines 8/2020 + CJEU C-184/20), (4) Sanctions cumulative (OFAC + EU 269/2014 + 833/2014 art.5n advisory restriction + UK OFSI + SECO + AML 5AMLD + Cyprus CIP suspended Nov 2020), (5) Cross-border (BRAO §206 / NRA Kodeks Etyki / CCBE / BSB gC8/gC9 / Cyprus Bar / Israeli Bar), (6) Cultural messaging post-2022 («возвратная» OFF / «русскоязычные» не «русские» / UA-BY-KZ-IL identity-respect / bilingual «сохрани русский» framing / latin URL), (7) Currency EUR/PLN/GBP/ILS + ECB substantiation, (8) DPA dual-jurisdiction + AI DISCLOSURE bilingual + EU AI Act art.50.
- 2 новые META категории: «EU_RUSSIAN_DIASPORA — GDPR Art.9 + sanctions + cross-border» и «Diaspora-cultural messaging — post-2022 political-sensitivity».
- Арки A-G матрица (строка 2247) — 3 строки EU_RUSSIAN_DIASPORA × LEGAL / × HIGH_TICKET / × KIDS_PARENTS.

**Файлы:** `skills/higgsfield-prompt-generator/SKILL.md` (+250 строк), `skills/meta-policy-checker/SKILL.md` (+110 строк).

---

## Волна П.20 — Logical cleanup (RAT/R disambiguation + dead-links inline)

**Commit:** `26aa39b` (2026-05-19)

**Главное:**
- **R/RAT disambiguation:** §3 prompt-engineering rules R1-R14 (canonical) vs §21 RATIONALITY checks R1-R8 — naming clash. Переименовано §21 R1-R8 → **RAT1-RAT8** (12 правок в SKILL.md).
- **QUICK-REFERENCE-NICHE-RESTRICTIONS.md dead-link фикс (4 → 0):** все 4 ссылки заменены на inline cross-ref на CRISIS-AUDIT-LAYER C1-C8 / MEDICAL_HEAVY §16 / WELLNESS_USA_PRESET. Плагин теперь self-contained.
- §13 GUARDRAILS канон — NO-OP в репо (живёт в внешнем /00-CANON-FROZEN/).

**Файлы:** `skills/higgsfield-prompt-generator/SKILL.md` + `skills/meta-policy-checker/SKILL.md` (+22 / -22 строки).

---

## Волна Т.7 — REAL_ESTATE_EXPAT_USA + WELLNESS_HEALTH_RESTRICTED_USA parallel

**Commit:** `0f8ce11` (2026-05-19)

**4 агента параллельно** (T.7-A REAL_ESTATE + T.7-B WELLNESS + T.7-C адверсариал 6 кейсов / 20 GAP + T.7-D мета cross-ref).

**REAL_ESTATE_EXPAT_USA_PRESET — 8 правил** закрывает 5 слоёв: FHA §3604(c) + Meta Housing SAC + AI-staging FTC §5 + substantiation broker (MLS/RealTrends/NAR) + License # state-specific (FL/CA/NY/TX/NV) + SEC Reg D 506(b/c) + FIRPTA + TRID + FinCEN GTO + EB-5 USCIS+SEC + RESPA §8 + AI DISCLOSURE broker.

**WELLNESS_HEALTH_RESTRICTED_USA_PRESET — 9 правил** закрывает 5 слоёв: DSHEA §403r-6 structure/function vs disease + FDA mandatory overlay + FTC «competent and reliable scientific evidence» + FTC §255 + §255.5 testimonials + FTC «Gut Check» 7 false weight-loss claims + category guardrails (ED PDE5 / sleep melatonin / TRT Schedule III) + real clinician Soul ID (state board + AMA §5.04) + state law (CA Prop 65 / NY AG / TX DTPA) + FTC Click-to-Cancel 16 CFR §425 + telehealth state-licensure Ryan Haight Act.

**2 новые META категории:** «REAL_ESTATE_EXPAT_USA — FHA Special Ad Categories Housing + foreign-buyer disclosures» + «WELLNESS_HEALTH_RESTRICTED_USA — DSHEA + FTC §255 supplement testimonials».

**Файлы:** `skills/higgsfield-prompt-generator/SKILL.md` (+451 строк), `skills/meta-policy-checker/SKILL.md` (+150 строк).

---

## Волна Т.6 — HIGH_TICKET_PRO_SERVICES_PRESET (M&A / LEGAL / private banking)

**Commit:** `d440734` (2026-05-19)

**3 агента параллельно** (T.6-A создатель + T.6-B адверсариал 5 кейсов / 18 GAP + T.6-C мета cross-ref 6 юрисдикций).

**Главное:**
- `HIGH_TICKET_PRO_SERVICES_PRESET` — 9 правил + 9/9 PASS + 3-STEP FUNNEL: Cinema/Veo 3.1 + EXECUTIVE-CALIBRATED H-stack + Premium polish vs AI slick + NDA жёстче B2B SaaS (4 слоя: aggregated client-count + visible documents + setting integrity) + Substantiation third-party verifiable (Form ADV / Bloomberg / Mergermarket / Chambers) + Percentage success-rate on-frame disclaimer + "from X%" hard-block + ABA Rule 1.18 free consultation + Regulatory disclaimers 4 юрисдикции + US state bar matrix (NY 7.1(d) / CA / TX / FL pre-clearance) + AI DISCLOSURE name-partner + OPERATIONAL guardrails (sanctions/Reg D/dual-credentialing/GDPR Art.9).
- 2 новые META категории: «HIGH_TICKET_PRO_SERVICES» + «SEC RIA / FINRA / FCA financial promotion».
- Боковые фиксы: арка G EDUCATIONAL-PROGRESSION для HIGH_TICKET_PRO_SERVICES (строка 2241); V19-BIOCLAIM (строка 2698) расширен с methodology disclosure.

**Файлы:** `skills/higgsfield-prompt-generator/SKILL.md` (+235 строк), `skills/meta-policy-checker/SKILL.md` (+77 строк).

---

## Волна Т-итог — финальный замер baseline vs final + SUMMARY-Т1-Т5

**Commit:** `966eb51` (2026-05-19 ранее)

**Главное:**
- `internal/stress-test-volna-T/SUMMARY-Т1-Т5.md` (170 строк) — финальный отчёт по 5 T-волнам, 20 метрик baseline vs final, risk-profile by 14 sub-профилей, top wins / risks, recommended next 3 actions, logical audit.
- Risk-profile средний: **6.86 → 4.7** (-31% после T-итог).

---

## Волна Т.5 — KIDS_PARENTS stress-test (3 агента) + 3 фикса

**Commit:** `1fafb69` (2026-05-19)

**Главное:**
- `KIDS_PARENTS_PRESET` (~210 строк) — 8 правил + 8/8 PASS: 3 Soul ID modes (A real parent / B AI parent-actor / C teacher) + 5 acceptable child-in-frame modes + 4 запрещённых + Parent-endorser substantiation + Accreditation guardrail + MINORS_AI_LIKENESS state-laws + 3-step funnel + V17 KIDS_PARENTS hook table.
- `MINORS_AI_LIKENESS CHECK` (~40 строк в meta-policy) — state laws CA AB-2839 / NY Marsh's Law / TX SB-1361 / IL HB 4762 + EU AI Act art.50 + усиленный overlay.
- `FTC §255.5 PARENT-ENDORSER BLOCK` (~25 строк в meta-policy) — Parent voice claim / Teacher endorsement / Child peer-endorsement table.

**Файлы:** `skills/higgsfield-prompt-generator/SKILL.md` (+210 строк), `skills/meta-policy-checker/SKILL.md` (+65 строк).

---

## Волна Т.4 — CRISIS_EXPERT stress-test (3 агента) + 3 фикса

**Commit:** `15a7032` (2026-05-19)

**Главное:**
- `CRISIS-AUDIT-LAYER` (~200 строк inline) — single source of truth с 8 проверок C1-C8 + 3-step funnel granularity for CRISIS_EXPERT + DIASPORA-TONE TUNING + LEGAL substantiation extension.
- Категория «Юридические услуги для физлиц в кризисе — PL/EU-юрисдикция addendum» (~85 строк) — NRA Kodeks Etyki §23 / BRAK BORA / UODO/GDPR / Prawo Upadłościowe + GUARDRAIL для EU_RUSSIAN_DIASPORA + AI DISCLOSURE для public professional в regulatory registry.

**Файлы:** `skills/higgsfield-prompt-generator/SKILL.md` (+200 строк), `skills/meta-policy-checker/SKILL.md` (+85 строк).

---

## Волна Т.3 — B2B_SAAS_ENTERPRISE stress-test (3 агента) + 3 фикса

**Commit:** `38612a2` (2026-05-19)

**Главное:**
- `B2B_SAAS_ENTERPRISE_PRESET` (~130 строк) — 8 правил + 8/8 PASS: Workspace+model / EXECUTIVE-CALIBRATED H-stack / Premium polish vs AI slick / SLA substantiation / Comparative claims / Migration timeline / Free migration / AI DISCLOSURE для public CEO.
- Категория «B2B SaaS Enterprise — comparative claims and brand-association» (~30 строк) — disparagement + Lanham Act §43(a) + named competitor + comparative without benchmark + absolute SLA + free migration + 24h migration.
- V18 fail→pass table расширен 4 B2B Enterprise rows (SLA / 10x faster / #1 alternative / Free migration).

**Файлы:** `skills/higgsfield-prompt-generator/SKILL.md` (+130 строк), `skills/meta-policy-checker/SKILL.md` (+30 строк).

---

## Волна Т.2 — MEDICAL_HEAVY stress-test (5 агентов) + 3 фикса

**Commit:** `87bb7c0` (2026-05-19)

**Главное:**
- **Pre-валидатор A.3 BIOCLAIM** — early-trigger перед §20 для biographical claim с числом («психолог, 47 спасённых браков»).
- **Pre-валидатор A.4 currency conversion** — non-USD ($ → ₽/₸/RUB/KZT/UAH) проверка с substantiation.
- **MEDICAL-CALIBRATED humanization table** — SKIP H1 wisp / H6 wrinkled coat (читается как «не клинический») / H9 puffy. OK H3 lived-in clinic / H7 ambient / H8 eye contact / H10 props.
- **Medical brand names exception** — Botox / Juvederm / Restylane разрешены при licensed clinic context.

**Файлы:** `skills/higgsfield-prompt-generator/SKILL.md` (+170 строк), `skills/meta-policy-checker/SKILL.md` (+40 строк).

---

## Волна Т.1 — INFOBIZ stress-test (5 агентов цикл создатель→критик→переписыватель→аудитор→мета) + 5 фиксов

**Commit:** `221b26e` (2026-05-19)

**Главное:** 5-агентский цикл (creator → critic → rewriter → auditor → meta) на INFOBIZ профиле для отработки методологии. 5 фиксов в SKILL.md под INFOBIZ-specific issues (founder talking-head specifics / over-polish / generic stock pose).

**Файлы:** `skills/higgsfield-prompt-generator/SKILL.md` (~100 строк).

---

## Волна П.19 — §21 HUMANIZATION + SCRIPT RATIONALITY + V21 валидация

**Commit:** `13dfed7` (2026-05-19)

**Главное:**
- §21 новый раздел (~400 строк): 10 H-приёмов humanization (H1 wisp temple / H2 natural cadence / H3 lived-in env / H4 not-actor / H5 handheld micro-drift / H6 wrinkled wardrobe / H7 ambient audio / H8 eye contact 70/30 / H9 lived-life face / H10 props used) + EXECUTIVE-CALIBRATED + PREMIUM POLISH vs AI SLICK + 22 запрещённых AI-markers.
- ЧАСТЬ 2: 8 проверок R1-R8 (переименованы в RAT1-RAT8 в волне П.20) + бинарный criterion для R5 stake-маркера + 8 anti-patterns A1-A8 + V21 валидация.
- Шаблон арки A в §20 обновлён с humanization-маркерами.

**Файлы:** `skills/higgsfield-prompt-generator/SKILL.md` (+400 строк).

---

## Волна П.16+П.17+П.18 — Англицизмы как guardrail + стресс-тест 3 агента + sync 8→10 канонических

**Commit:** `a1be1bd` (2026-05-19)

**Главное:**
- §13 GUARDRAILS canon (в /00-CANON-FROZEN/ вне репо) — раздел 13 «Язык: русский приоритет, англицизмы только индустриальные» + таблица 33 пар замен + список 25 индустриальных терминов.
- Глобальная замена «8 канонических» → «10 канонических» в 9 файлах.
- Удалён бэкап-файл SKILL.md.bak-volna-P4-2140.

**Файлы:** 9 файлов (PROMPT-2/3/4/5, KONVEYER, INSTRUCTIONS, BRIEFING-PACK + client-profile + higgsfield + creative-brief-writer).

---

## Волна П.15 — Закрыто 10 OPEN-Q (Q9/Q20/Q21/Q25/Q30/Q50/Q57/Q58/Q59/Q62/Q63)

**Commit:** `daa9814`

10 запросов закрыто: FUNNEL_PURPOSE granularity / UAE русскоязычный релокант wardrobe / диаспора-сегменты гайдлайн / etc.

---

## Волна П.14 — Топ-5 OPEN-QUESTIONS закрыто (Q48/Q49/Q51-Q55/Q60-Q61/Q56)

**Commit:** `db24771`

10 канонических профилей таксономия / out-of-scope gate / KIDS_PARENTS / ECOM_IMPULSE / PL-двуязычность.

---

## Волна П.13 — 6 новых тестов + P1 англицизмы + HIGH_TICKET_PRO_SERVICES в client-profile + Q1 LinkedIn зачистка

**Commit:** `f6812d5`

---

## Волна П.12 — §20 OFFER → STORY MAPPING + медицинская точность инфографики + V20 валидация

**Commit:** `c939606`

§20 раздел: 7 арок A-G офер → история + 14 правил mapping + V20 валидация.

---

## Волны П.1-П.11 (более ранние)

Базовая разработка плагина — 22 скила, 10 канонических профилей, 4 budget modes, §1-§19 секции higgsfield-prompt-generator, базовые V1-V16 валидации, 9 категорий meta-policy.

---

## Замер цикла П.13-Т.8 (16 волн / ~6 месяцев работы / 11 коммитов post-baseline)

| Метрика | Pre-T (baseline) | Post-Т.8 (актуально) | Δ |
|---|---|---|---|
| higgsfield-prompt-generator/SKILL.md | ~3200 строк | **4568** строк | **+1368 (+43%)** |
| meta-policy-checker/SKILL.md | ~600 строк | **994** строки | **+394 (+66%)** |
| Дедикейтед PRESET'ов | 0 | **7** | +7 |
| Канонических ниш / sub-profile с PRESET | 0% / 0% | **60% / 6 sub-profile** | большой sweep |
| Регуляторных юрисдикций explicit | ~3 (RU/KZ/общая EU) | **12** | ×4 |
| META категорий | 9 | **13** | +4 |
| Validation rules V1-V21 + Pre-валидаторы A.1-A.4 | V1-V16 | **V1-V21 + 4 Pre** | +5+4 |
| AI-маркеров запрет | 5 | **22** | ×4.4 |
| Risk-profile средний (14 sub-профилей) | **6.86** | **≈3.3** | **-52%** |
