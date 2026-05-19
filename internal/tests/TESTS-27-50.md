# TESTS 27-50 — coverage для волн П.13-П.23 + Т.1-Т.10

**Создан:** 2026-05-19 (волна П.24)
**Назначение:** test coverage для правил добавленных в плагин после base тестов 1-26.
**Формат:** каждый тест = (1) INPUT — клиентский запрос / scenario, (2) EXPECTED — какие правила должны сработать + PASS/FAIL гейты, (3) FAIL MODE — что бы было без правила.

---

## Тесты 27-30 — Волна П.13 (HIGH_TICKET_PRO_SERVICES в client-profile + Q1 LinkedIn)

### Test 27 — HIGH_TICKET_PRO_SERVICES в client-profile UI
**INPUT:** Клиент: «корпоративный LEGAL M&A boutique партнёр в NYC, чек $50k-2M за mandate, целевая HNWI founders».
**EXPECTED:** `client-profile` классифицирует HIGH_TICKET + sub-profile УРОВЕНЬ 3 = HIGH_TICKET_PRO_SERVICES (M&A vertical) + бюджетный режим PRO. Активирует HIGH_TICKET_PRO_SERVICES_PRESET в higgsfield-prompt-generator.
**FAIL MODE:** Без П.13 — был бы классифицирован просто HIGH_TICKET без активации M&A-specific guardrails (NDA / ABA 7.1 / SEC RIA / regulatory disclaimers).

### Test 28 — Q1 LinkedIn-only зачистка
**INPUT:** Клиент просит «настрой LinkedIn Ads для B2B SaaS Enterprise CTO».
**EXPECTED:** `client-profile` + `meta-launch-checklist` отвечают что Q1 канал = Meta-only для CIS-except-RU + EU + USA рынка. LinkedIn упоминается только как secondary placement для HIGH_TICKET_PRO_SERVICES (institutional decision-maker).
**FAIL MODE:** До П.13 LinkedIn упоминался как первичный канал для B2B, что противоречит курсовому фокусу на Meta.

### Test 29 — 6 новых тестов в плагине (П.13 base)
**INPUT:** `quality-gate` запускается на крео для CRISIS_EXPERT.
**EXPECTED:** В чек-листе появляется проверка «прогнан через meta-policy-checker категория Юр.услуги для физлиц в кризисе?».
**FAIL MODE:** До П.13 chek был «прогнан через meta-policy» без специфичной категории, агент мог пропустить категорию-специфичный гейт.

### Test 30 — Англицизмы P1 fix
**INPUT:** Документ содержит «workflow / fallback / HARD CAP / Override» в технической документации.
**EXPECTED:** §13 GUARDRAILS canon применяется — workflow → рабочий процесс, fallback → запасной, HARD CAP → ЖЁСТКИЙ ПОТОЛОК, Override → Перебивка. Индустриальные термины (CTR/ROAS/CPL) остаются.
**FAIL MODE:** Без П.13 заголовок «HARD CAP» оставался calque, читался не-носителю как корпоративный slang.

---

## Тесты 31-34 — Волна П.14 (10 канонических + KIDS_PARENTS + ECOM_IMPULSE)

### Test 31 — 10 канонических профилей таксономия
**INPUT:** `client-profile` отвечает на клиентскую нишу (нутрициолог онлайн).
**EXPECTED:** Классифицируется WELLNESS_HEALTH_RESTRICTED (не «SOFT_EXPERT» — deprecated). 10 канонических: INFOBIZ / LOCAL_SERVICE / ECOM / B2B_SAAS / HIGH_TICKET / CRISIS_EXPERT / REAL_ESTATE_EXPAT / WELLNESS_HEALTH_RESTRICTED / KIDS_PARENTS / ECOM_IMPULSE.
**FAIL MODE:** До П.14 — было 8 канонических без KIDS_PARENTS / ECOM_IMPULSE, нутрициолог классифицировался как SOFT_EXPERT (тут risk-профиль занижен).

### Test 32 — KIDS_PARENTS базовый профиль
**INPUT:** Клиент = детская развивайка с онлайн-курсами для родителей. Hook «помоги ребёнку начать программировать в 8 лет».
**EXPECTED:** `client-profile` → KIDS_PARENTS канонический. `higgsfield-prompt-generator` → CHILDREN IN FRAME pack + 5 acceptable child modes + V17 KIDS_PARENTS hook table check.
**FAIL MODE:** До П.14 — без KIDS_PARENTS дефолтил в INFOBIZ или ECOM, child-safety guardrails отсутствовали.

### Test 33 — ECOM_IMPULSE retention=0 классификация
**INPUT:** Клиент = WOW-товар через TikTok ($25-50 импульсный, retention=0).
**EXPECTED:** `client-profile` → ECOM_IMPULSE (не «ECOM» обычный с retention). Активирует ECOM_IMPULSE_USA_PRESET (волна Т.9) если US-targeting.
**FAIL MODE:** До П.14 — был ECOM с предполагаемым retention, метрика unit-economics завышенная, ROAS ожидания нереалистичные.

### Test 34 — PL-двуязычность PLN+EUR
**INPUT:** PL adwokat для PL-резидентов + PL-релокантов в DE.
**EXPECTED:** Currency table (строки 408-418) → PLN основная + EUR допустим для diaspora-сегментов; ECB substantiation если double-pricing.
**FAIL MODE:** До П.14 — была только PLN, что отрезало EU-diaspora аудиторию.

---

## Тесты 35-37 — Волна П.15 (10 OPEN-Q закрыто)

### Test 35 — UAE русскоязычный релокант wardrobe
**INPUT:** HIGH_TICKET-эксперт = русскоязычный релокант в Dubai (НЕ local Emirati). Создать промпт под Higgsfield.
**EXPECTED:** UAE row в DIASPORA-TONE GUIDANCE — modern tech-CEO suit без tie (charcoal grey wool + white dress shirt) + tropical weight ткани (lightweight wool / linen-blend) + Dubai CBD glass office (DIFC / Business Bay) + Burj Khalifa skyline. НЕ kandura/ghutra.
**FAIL MODE:** Без П.15 — был дефолтный wardrobe без UAE specifics, агент мог сгенерировать local Emirati attire = культурное несоответствие для русскоязычного релоканта.

### Test 36 — Q9 FUNNEL_PURPOSE granularity
**INPUT:** Клиент = HIGH_TICKET с funnel TOF/MOF/BOF.
**EXPECTED:** Промпт включает FUNNEL_PURPOSE параметр (B2B_SAAS / B2B_PROFESSIONAL_SERVICES / HIGH_TICKET) + 3-step funnel разбивка с регуляторным риском per step.
**FAIL MODE:** Без П.15 — плоский подход без funnel-step granularity, BOF cold в open feed = SEC Reg D / ABA 7.3 / SRA solicitation risk.

### Test 37 — Diaspora-tone правил палитра + posture
**INPUT:** REAL_ESTATE_EXPAT для RU-diaspora в Berlin.
**EXPECTED:** DIASPORA-TONE GUIDANCE применяется: warm amber-gold + confident posture + ambition-led hook + time-anchor для HIGH_TICKET-diaspora.
**FAIL MODE:** Без П.15 — cold-grey palette + слумленная посадка + ностальгическая лексика = читается как «жертва обстоятельств», V17 FAIL.

---

## Тесты 38-40 — Волна П.16-П.18 (англицизмы + sync 8→10 + стресс-тест 3 агента)

### Test 38 — §13 GUARDRAILS англицизмы canon
**INPUT:** Создаётся новый файл в плагине с черновиком текста «Override параметра в edge case через workflow».
**EXPECTED:** Соблюдение с первого черновика: «Перебивка параметра в крайнем случае через рабочий процесс». §13 GUARDRAILS canon (33 пар замен + 25 индустриальных терминов).
**FAIL MODE:** Без П.16 — англицизмы накапливались, не было единого guardrail.

### Test 39 — Sync 8 → 10 канонических в 9 файлах
**INPUT:** Открыт `cowork-загрузка/PROMPT-2.md`.
**EXPECTED:** Везде «10 канонических» (не 8), включая шаблоны `{INFOBIZ/.../KIDS_PARENTS/ECOM_IMPULSE}`.
**FAIL MODE:** До П.18 — рассинхрон между skills (10) и cowork-загрузка (8), агент путался при сборке промта.

### Test 40 — TikTok зачистка в client-profile
**INPUT:** Клиент спрашивает про TikTok Ads для CIS-except-RU.
**EXPECTED:** `client-profile` отвечает «канал = Meta-only per Q1 курса; TikTok может быть учтён как secondary для специфичных ниш (ECOM_IMPULSE) но не дефолт».
**FAIL MODE:** До П.18 — TikTok упоминался как первичный канал, что противоречит Q1.

---

## Тесты 41-43 — Волна П.19 (§21 HUMANIZATION + RAT1-RAT8 + V21)

### Test 41 — H1-H10 humanization для INFOBIZ
**INPUT:** Промпт для INFOBIZ founder talking-head, default casual register.
**EXPECTED:** Применены 3-4 H-приёма (H1 wisp temple / H3 lived-in environment / H4 not-actor Soul ID / H9 lived-life face). V21 валидация PASS.
**FAIL MODE:** Без П.19 — Soul ID выглядит как «hired actor for stock photo», 5 AI-tells (perfect symmetry / glossy texture / identical smile / stock environment / continuous monotone), conversion-drop.

### Test 42 — EXECUTIVE-CALIBRATED H-stack для B2B_SAAS_ENTERPRISE
**INPUT:** Промпт для CTO Fortune 500 talking-head.
**EXPECTED:** Из §21 EXECUTIVE-CALIBRATED таблица — SKIP H1 wisp / H5 handheld / H6 wrinkled / H9 puffy; MODIFY H2 / H4; OK H3 / H7 / H8 / H10. 4-5 H-приёмов calibrated, не 6-7 как INFOBIZ.
**FAIL MODE:** Без П.19 EXECUTIVE-CALIBRATED — CTO с растрёпанными волосами + неглаженной рубашкой = «consultant who can't iron his shirt» → conversion-drop.

### Test 43 — V21 валидация + RAT1-RAT8 проверки
**INPUT:** Готовый промпт перед выдачей ученику.
**EXPECTED:** V21 5-проверочный pre-flight: H1-H10 (3+ применены) + 5 AI-tells отсутствуют + Soul ID не stock + RAT1-RAT8 (renamed from R1-R8 в волне П.20) проверены + mental model walk-through Shot 1/2/3.
**FAIL MODE:** Без V21 — Soul ID stock-look + декоративные шоты (FAIL RAT6) + 3 шот без motivation (FAIL RAT2) + перегруз Shot 1 (FAIL RAT3).

---

## Тесты 44-50 — Волна Т.1-Т.10 (8 PRESET'ов + Pre-валидаторы A.3/A.4/A.5)

### Test 44 — B2B_SAAS_ENTERPRISE_PRESET 8/8 PASS (Т.3)
**INPUT:** Промт для Datadog-killer Replacement campaign (CTO Fortune 500, 99.99% SLA claim).
**EXPECTED:** Активирован B2B_SAAS_ENTERPRISE_PRESET. 8/8 PASS требует: Cinema Studio + Veo 3.1 + EXECUTIVE-CALIBRATED + Premium polish vs AI slick + SLA substantiation (contract / SOC 2) + comparative claims (Generic alias «legacy observability tool») + Migration timeline (qualified «structured migration») + Free migration (scope-limited) + AI DISCLOSURE для public CEO.
**FAIL MODE:** Без Т.3 — оффер прошёл V21 но FAIL V18 (SLA без contract = financial commitment) + Lanham §43(a) (disparagement «Datadog killer»).

### Test 45 — MEDICAL_HEAVY Pre-валидатор A.3 BIOCLAIM (Т.2)
**INPUT:** Стома-клиника: «47 спасённых улыбок за 8 лет practice».
**EXPECTED:** A.3 BIOCLAIM early-trigger STOP до Шага 1. Замена: «более 40 успешных кейсов / многолетняя практика». Если есть sign-off артефакт (CRM-выгрузка ≤7 days) — допускается оригинальная цифра.
**FAIL MODE:** Без A.3 — оффер прошёл через §19A/§19B рендер, FAIL V19-BIOCLAIM, ученик заплатил за кредиты Higgsfield, переделал с нуля.

### Test 46 — CRISIS-AUDIT-LAYER C1-C8 single source (Т.4)
**INPUT:** Промт CRISIS_EXPERT — PL adwokat по банкротству физлиц для PL-резидентов.
**EXPECTED:** CRISIS-AUDIT-LAYER inline применён (НЕТ dead-link на QUICK-REFERENCE-NICHE-RESTRICTIONS.md): C1 лицо клиента НЕ в кадре + C2 нет urgency «успей пока окно» + C3 substantiated outcomes + C4 нет combined identifier (имя+sygnatura+сумма) + C5 нет voice-only client testimonial + C6 NRA Kodeks Etyki §23 + C7 LEGAL substantiation extension + C8 AI DISCLOSURE для public expert в registry.
**FAIL MODE:** Без CRISIS-AUDIT-LAYER inline — dead-link на внешний файл, агент не self-contained.

### Test 47 — KIDS_PARENTS_PRESET 3 Soul ID modes + FTC §255.5 (Т.5)
**INPUT:** Coding course для детей, US-targeting, parent endorsement в Reel.
**EXPECTED:** KIDS_PARENTS_PRESET 8/8 PASS: 3 Soul ID modes (A real parent / B AI parent-actor / C teacher) + 5 acceptable child-in-frame modes (silhouette / hands-only / over-shoulder / group / project showcase) + 4 запрещённых + Parent-endorser substantiation FTC §255.5 + Accreditation guardrail + MINORS_AI_LIKENESS state-laws (CA AB-2839 / NY Marsh's Law / TX SB-1361).
**FAIL MODE:** До Т.5 — 4 строки defaults + child-in-frame pack 28 строк = 5-10× меньше других PRESET'ов, агент терял 90% guardrails.

### Test 48 — HIGH_TICKET_PRO_SERVICES_PRESET 9/9 PASS (Т.6)
**INPUT:** M&A boutique partner NYC, hook «47 closed deals · $2B AUM».
**EXPECTED:** HIGH_TICKET_PRO_SERVICES_PRESET 9/9 PASS: Cinema/Veo 3.1 + EXECUTIVE-CALIBRATED + Premium polish + NDA (jнitiative «institutional clients») + Substantiation через Mergermarket league table + Pricing через «fees per mandate letter» + Regulatory disclaimers 4 юрисдикции + AI DISCLOSURE + OPERATIONAL guardrails (Reg D + dual-credentialing + GDPR Art.9).
**FAIL MODE:** До Т.6 — правила рассыпаны по 5 секциям, агент терял substantiation third-party verifiable / NDA жёстче B2B SaaS / state bar matrix US.

### Test 49 — REAL_ESTATE_EXPAT_USA_PRESET FHA + AI-staging (Т.7)
**INPUT:** Miami Brickell condo listing для foreign buyers, Reel с AI-staged interior.
**EXPECTED:** REAL_ESTATE_EXPAT_USA_PRESET 8/8 PASS: FHA-compliant casting (diverse) + Meta Housing SAC targeting (no age/gender/ZIP/radius<15mi/language-only) + AI-staging disclosure overlay «Virtually staged · actual unit unfurnished» + License # state-specific (FL FREC) + Pricing/yield qualified + Foreign-buyer guardrails (FinCEN GTO + FIRPTA + EB-5 SEC + RESPA §8) + AI DISCLOSURE для broker Soul ID.
**FAIL MODE:** Без Т.7 — AI-staging без disclosure = FTC §5 deceptive impression + state RE commission ad rule violation.

### Test 50 — WELLNESS_HEALTH_RESTRICTED_USA + A.5 DSHEA (Т.7 + П.23) + EU_RUSSIAN_DIASPORA (Т.8) + ECOM_IMPULSE_USA (Т.9) + KIDS_PARENTS_EDTECH (Т.10)
**INPUT 50.a (WELLNESS+A.5):** Sleep supplement Reel «cures insomnia in 7 days».
**EXPECTED:** Pre-валидатор A.5 DSHEA early-trigger STOP. Замена на «supports restful sleep» / «promotes natural sleep cycle». Если оставлено — WELLNESS_HEALTH_RESTRICTED_USA_PRESET ПРАВИЛО 2 hard-line + ПРАВИЛО 3 FDA disclaimer overlay mandatory.
**INPUT 50.b (EU_RUSSIAN_DIASPORA):** PL adwokat → DE-диаспора, lookalike из «Telegram channel @berlin_russians».
**EXPECTED:** EU_RUSSIAN_DIASPORA_PRESET 8/8 PASS: GDPR Art.9 hard-block (language-based lookalike) + Sanctions OFAC/SECO/EU 833 art.5n + Cross-border BRAO §206 + Cultural messaging post-2022 + Currency EUR/PLN + DPA dual-jurisdiction.
**INPUT 50.c (ECOM_IMPULSE_USA):** Bath bombs subscription «risk-free trial» без auto-charge disclosure.
**EXPECTED:** ECOM_IMPULSE_USA_PRESET 9/9 PASS: FTC ROSCA + Negative Option + CA §17602 + NY GBL §527-a + «Made in USA» BOM substantiation если claimed.
**INPUT 50.d (KIDS_PARENTS_EDTECH):** Math tutoring «Improves SAT 200 pts in 8 weeks» + AI teacher Soul ID.
**EXPECTED:** KIDS_PARENTS_EDTECH_PRESET 9/9 PASS поверх KIDS_PARENTS_PRESET 8/8: COPPA VPC + state SOPIPA/SOPPA/NY 2-d + Accreditation Cognia/WASC + Outcome «Gut Check» (replace «Improves SAT 200» → «Most students improve practice scores») + Click-to-Cancel + AAP screen-time + MINORS_AI_LIKENESS + FERPA.
**FAIL MODE:** Без волн Т.7-Т.10 + П.23 — каждый из 4 case-types вырывает критический регуляторный риск (DSHEA disease claim / GDPR Art.9 + sanctions / FTC ROSCA + Click-to-Cancel / COPPA + state student-data + AAP).

---

## Coverage map (правила → тесты)

| Правило / волна | Тесты |
|---|---|
| П.13 (HIGH_TICKET_PRO_SERVICES sub-profile + Q1 Meta-only) | 27, 28, 29 |
| П.14 (10 канонических + KIDS_PARENTS + ECOM_IMPULSE) | 31, 32, 33, 34 |
| П.15 (10 OPEN-Q закрыто) | 35, 36, 37 |
| П.16-П.18 (англицизмы + sync 8→10) | 30, 38, 39, 40 |
| П.19 (§21 H1-H10 + RAT1-RAT8 + V21) | 41, 42, 43 |
| П.20 (RAT/R disambiguation + dead-links) | 43, 46 |
| П.22 (docs sync) | meta-test через manual review CHANGELOG / ARCHITECTURE / README / GLOSSARY |
| П.23 (A.5 DSHEA early-trigger) | 50.a |
| Т.1 (INFOBIZ 5-агент цикл) | 41 |
| Т.2 (MEDICAL_HEAVY Pre-валидаторы A.3 + A.4) | 45 |
| Т.3 (B2B_SAAS_ENTERPRISE_PRESET) | 44 |
| Т.4 (CRISIS-AUDIT-LAYER) | 46 |
| Т.5 (KIDS_PARENTS_PRESET) | 47 |
| Т.6 (HIGH_TICKET_PRO_SERVICES_PRESET) | 48 |
| Т.7 (REAL_ESTATE_EXPAT_USA + WELLNESS_HEALTH_RESTRICTED_USA) | 49, 50.a |
| Т.8 (EU_RUSSIAN_DIASPORA_PRESET) | 50.b |
| Т.9 (ECOM_IMPULSE_USA_PRESET) | 50.c |
| Т.10 (KIDS_PARENTS_EDTECH_PRESET) | 50.d |

**Coverage:** 24 теста (27-50) покрывают 16 волн (П.13 → П.23 + Т.1-Т.10) = 1.5 теста на волну в среднем. Test 50 multi-input (a/b/c/d) для одновременного coverage 4 PRESET'ов = compound test.

---

## Как запускать тесты

Тесты дизайн = **integration tests** для агента (Claude). Каждый тест — manual / supervised:

1. Подать INPUT в чат с Claude (с активным плагином ai-ops-7142).
2. Verifier (ученик / instructor) проверяет какие правила сработали в output: какой PRESET активировался, какой чек-лист N/N PASS, какие overlay добавлены, какие категории meta-policy запрошены.
3. PASS если EXPECTED совпадает с actual output. FAIL → bug report → следующая волна П.

Автоматизация (future work): спецификации тестов выше формализуемы в JSON / YAML для `claude-eval`-style harness, но требует CI infrastructure.

---

## Pre-existing tests 1-26 (краткое summary, для контекста)

Tests 1-26 покрывают:
- 1-5: client-profile classification (canonical niches + budget mode)
- 6-10: ru-marketer segmentation + research-structurer
- 11-15: reality-check-metrics formulas
- 16-20: ad-teardown + creative-brief-writer + ru-copywriter integration
- 21-25: quality-gate + meta-policy-checker base categories (1-9)
- 26: chat-handoff summary format

Tests 27-50 (этот файл) — extension для волн П.13 onward.

---

## Total coverage post-П.24

- **50 тестов total** (26 base + 24 extension)
- **22 скила** в плагине (100% покрытие основных функций через тесты integration)
- **8 PRESET'ов** в higgsfield-prompt-generator (Т.3-Т.10 — каждый покрыт тестом 44-50)
- **17 META категорий** в meta-policy-checker (тесты 29, 50.a-d косвенно)
- **5 Pre-валидаторов A.1-A.5** (тесты 45 для A.3, 50.a для A.5 — A.1/A.2/A.4 покрыты косвенно)

**Test quality:** integration-level (не unit), требует supervised execution. Покрытие = behavioral spec.
