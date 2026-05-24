# CHANGELOG — ai-ops-7142

История доработок плагина по волнам (П — production polishing, Т — таргетированный стресс-тест ниш).

Формат записи: **волна** / **commit** / **главное** / **затронутые файлы**.

---

## ⚠️ ВАЖНО: ТЕКУЩЕЕ СОСТОЯНИЕ (2026-05-19, после cleanup'а c23aed5 + f96d116)

**Плагин = 25 скилов** (НЕ 22 как в исторических волнах ниже).

После полной разведки 5 чатов 14-19 мая был проведён cleanup. Удалено из плагина следующее как нарушающее «out-of-scope gate» курса (см. `internal/CLEANUP-REPORT-2026-05-19.md`):

| Удалено | Из чего | В какой волне ниже было добавлено |
|---|---|---|
| EU AI Act art.50 production process + RUNBOOK | higgsfield-prompt-generator + internal/runbooks/ | Волны П.25 + П.26 |
| test-harness-schema.json + test-harness-example.json + ci/ + .github/workflows | internal/tests/ + .github/ | Волны П.25 + П.26 |
| LATAM_PRESET (BR/MX/AR/CL/CO/PE) | higgsfield-prompt-generator | Волна Т.14 |
| APAC_PRESET (JP/KR/SG/AU) | higgsfield-prompt-generator | Волна Т.15 |
| CRYPTO_WEB3_PRESET full + CRYPTO/WEB3 META категория | higgsfield + meta-policy-checker | Волны Т.16 + Т.13 |
| PET_SUPPLIES_USA_LAYER + OTC_PHARMA_USA_LAYER | higgsfield-prompt-generator | Волна Т.17 |

**Восстановлены 3 скила** которых не было в волнах Т-итог из-за бага: `offer-generator` (426 строк) + `winner-variations` (313) + `iterative-refiner` (134). Без них Чат 4 в PROMPT-5.md был сломан с 16 мая.

**Таксономия:** 10 канонических профилей (+KIDS_PARENTS, +ECOM_IMPULSE Волной П.14), не 8 как в исторических волнах ниже.

**Канон-резерв:** `internal/CANON-DO-NOT-CHANGE-2026-05-19.md` — stop-list для будущих ботов.

**Призма «не перебор ли это»:** любая новая правка проходит 3 вопроса (нужно 99% или 0.0001% таргетологов? покрывает scope CIS-EU-USA? курс/скилы зависят?). Нарушение призмы = регрессия.

---

## Hormozi-формат: маршрут оффер→крео (2026-05-24, commit 39ec4ee)

**Главное:** Hormozi-оффер в крео идёт через воронку (хук + карусель / VSL / рилсы), НЕ в холодную статику. Корень бага «крео = бред»: роутер формата выбирал формат без учёта типа оффера → Hormozi-стек тёк в default-статику = простыня. Развилка по типу оффера реализована в роутере PROMPT-4 (канон курса, отдельный репо); здесь — зеркальная пометка в offer-generator. ECOM_IMPULSE-исключение (короткий товарный стек → статика) сохранено. Класс Hormozi-офферов НЕ удалён — меняется только маршрут в крео. Протестировано на 3 нишах (инфобиз / стоматология / ECOM_IMPULSE) — PASS.

**Затронутые файлы:** `skills/offer-generator/SKILL.md` (+2 строки, обобщение принципа «холодное крео = слой-1»).

Дальше идут исторические записи волн **в состоянии на момент написания**. Многие из них откачены в cleanup'е — см. таблицу выше.

---

## v3.Т — Ночная автономка 2026-05-19 → 2026-05-20

**Триггер:** автономный прогон 50+ агентов на Opus 4.7 за ночь — расширение системы.

**Артефакт 1 (новый Cowork-проект):** `analytics-проект/` (4 файла, 1537 строк) — отдельный проект «Аналитика», главный принцип «месячная модель ROI» (выручка по месяцу подписки, не покупки).

**Артефакт 2 (новый скил):** `skills/analytics-deep-dive/SKILL.md` (1702 строк после 24 фиксов) — 26-й скил плагина. 10 сценариев: cohort, юнитка, корреляции, скармливание ИИ, выгрузка из Meta/TG/organic.

**ФАЗА 1 — Подготовка плагина:**
- Снос артефактов internal/stress-test-volna-T/* + TESTS-27-50.md (-1607 строк)
- EU_RUSSIAN_DIASPORA перенесён из плагина в KONVEYER (+91 строка)
- Прогон 25 скилов 5 параллельными агентами — 5 жёлтых починены
- CHANGELOG плагина — шапка про cleanup для будущих ботов

**ФАЗА 2 — analytics-deep-dive создание:**
- Изучение таблицы «Для курса.xlsx» + структуры NDA-таблицы «Коля статистика 26» + 2 уроков traficpro2
- Создан скил (890 строк) + методичка АНАЛИТИКА-LOGIKA.md (718) + PROMPT-АНАЛИТИК (247) + INSTRUCTIONS (95) + ПРИМЕР (477)

**ФАЗА 2.1 — Стресс-тест analytics-deep-dive (3 волны × 5 учеников):**
- Волна 1: 46 багов → 13 фиксов (адаптация под junior, mode «первая помощь», запрет выдумывать бенчмарки, не-Meta каналы TG Ads/Insta organic/TikTok, крипто+Notion, лимит exec summary, малая выборка n<100, client-comms триггер, payback разовые, subscription vs разовая, контексты ниш, обратная арифметика)
- Волна 2: 14 багов → 11 фиксов (client-comms жёстко, маржа всегда [ГИПОТЕЗА], HIGH_TICKET long-cycle, ECOM_IMPULSE явно, терминология ≤100 слов, UTM-структура, iOS-корректировка, trial→paid B2B SaaS, Notion Relations ловушка, валютная единица, обратная sanity-check)
- Волна 3: 0 регрессий

**ФАЗА 3 — Стресс-тест полного курса (3 волны × 15 разных ниш):**
- Волна 1: 80+ багов → 14 фиксов К1-К14 (Junior-mode + meta-policy на офферах + шпаргалка + маркеры промптов + KIDS_PARENTS + ECOM_IMPULSE + STANDARD multi-гео + EU ECOM `[ОТКАЧЕНО 2026-05-20]` + meta-launch-checklist в начало + force-trigger бана + schwartz нотация + CRISIS бесплатно + LEGAL US `[ОТКАЧЕНО 2026-05-20 — LEGAL_BANKRUPTCY_US свёрнут до 1 строки]` + Hormozi WELLNESS)
- Волна 2: 40+ багов → 13 фиксов К15-К27 (REAL_ESTATE_EXPAT EU programmes + EU_PRESET + income claims автотриггер + бюджетные диапазоны + analytics switch B2B_SAAS/B2B_PROF_SERVICES + GDPR cookie + опросник CRM + Junior-mode мгновенный + проактивная шпаргалка + Hormozi ECOM_IMPULSE + UGC противоречие + Special Ad Housing + AI DISCLOSURE)
- Волна 3: 13 фиксов К28-К38 (Pre-flight gate vape + TG Ads бенчмарки `[ОТКАЧЕНО 2026-05-20 — Yandex Direct ₽-бенчмарки удалены, TG Ads ограничен явным запросом]` + TG Ads архитектурное правило для GREY + schwartz GREY + creative-brief TG Ads + analytics GREY switch + B2B_SAAS_SMB + Stripe-CAPI + USDT × LEGAL DE AML `[ОТКАЧЕНО 2026-05-20 — свёрнут до 1 строки]` + Беженцы FAIL + Информационный запрос vs Жертва)

**Файлы курса изменены:** INSTRUCTIONS-готово-к-копированию.txt / KONVEYER-LOGIKA.md / PROMPT-2-5.md / BRIEFING-PACK.md / QUICK-REFERENCE-NICHE-RESTRICTIONS.md

**Файлы плагина изменены:** client-profile + meta-launch-checklist + meta-policy-checker + reality-check-metrics + schwartz-podhody + creative-brief-writer + analytics-deep-dive + offer-generator + ru-marketer + quality-gate + geo-memos/* + README + ARCHITECTURE

**Sync 4 клиентских копий:** md5-идентичны (Аи проект / Стоматология / MINOR / Дизайн)

**Коммиты:** 48b7b6f → 6a94641 → d43277c → e977dff → 3990456 → c888aa8 → e82f0f2 + финальный

### Post-audit чистка scope-creep (2026-05-20, коммит 100d341)
После прогона всех фиксов через призму «не перебор ли это» вычищено ~20% scope-creep который агенты протащили:
- TikTok Ads + Yandex Direct как каналы (вне Meta-only) → удалены
- iOS-регионы APAC (Singapore/Japan/Australia) + IL/UAE → урезаны до USA/Canada/EU
- LEGAL_BANKRUPTCY_US (~120 строк) + USDT×LEGAL DE AML (39 строк) → по 1 строке (0.0001%, аналог Pet/OTC/LATAM)
- MEDICAL_HEAVY + микро-ниши HIGH_TICKET → свёрнуты в канон
- EU_PRESET / EU ECOM / HIGH_TICKET long-cycle / Notion → урезаны
Детали и stop-list — `internal/CANON-DO-NOT-CHANGE-2026-05-19.md` §3.5. Нетто −253 строки лишнего.
ВАЖНО: записи волн Т.2 / Т.6 / Т.13 (и пр.) ниже про LEGAL_BANKRUPTCY_US, MEDICAL_HEAVY, USDT×LEGAL DE AML, TikTok, Yandex как «достижения» — УСТАРЕЛИ, эти штуки вычищены. Помечены инлайн `[ОТКАЧЕНО 2026-05-20]`.

---

## Волна П.25 — EU AI Act art.50 production execute process + test harness JSON schema (v2.1 release) [⚠️ ОТКАЧЕНО Cleanup 2026-05-19]

**Commit:** предстоящий (2026-05-19 финальный)

**Главное:**
- **EU AI Act art.50 production execute process** (~130 строк новой секции в higgsfield SKILL.md перед ДОПОЛНИТЕЛЬНЫЕ ПРЕСЕТЫ): 5-шаговый process для production-ready compliance с August 2026 effective date. Шаги: (1) AI-content inventory, (2) Real-person likeness identification, (3) Dual sign-off collection (marketing ≠ AI-generation) + шаблон AI-likeness release form, (4) Disclosure overlay design per PRESET, (5) Final audit 10-пунктовый checklist pre-launch. Penalties: €15M или 3% global turnover для AI provider / €7.5M или 1.5% для deployer.
- **test-harness-schema.json** (NEW, ~286 строк) — формальная JSON Schema для перехода от supervised manual execution к claude-eval-style CI. Описывает структуру integration test: id / wave / skill / input + context / expected (preset / validation rules / pre-validators / humanization / rationality / anti-patterns / meta-policy categories / regulatory overlays) / fail_mode / automation_notes.
- **test-harness-example.json** (NEW, ~269 строк) — 5 показательных тестов из TESTS-27-50.md формализованы в JSON (TEST-44 B2B Enterprise / TEST-46 CRISIS-AUDIT-LAYER / TEST-49 REAL_ESTATE_EXPAT_USA / TEST-50.b EU_RUSSIAN_DIASPORA / TEST-50.d KIDS_PARENTS_EDTECH). Полный набор 50 тестов конвертируется при готовности CI infrastructure.
- INSTRUCTIONS-готово-к-копированию.txt — NO-OP в этом репо (живёт в cowork-загрузка курса вне ai-ops-7142, недоступно для update из плагина).

**Файлы:** `skills/higgsfield-prompt-generator/SKILL.md` (5481 → 5597, +116 строк), `internal/tests/test-harness-schema.json` (NEW), `internal/tests/test-harness-example.json` (NEW).

**Plugin v2.1 = production-ready.**

---

## Волна Т.13 — CRYPTO/WEB3 META категория (SEC Howey + MICA + FCA crypto promotions)

**Commit:** `3ddebe9` (объединён с Т.11 + Т.12)

**Главное:** Standalone категория meta-policy «CRYPTO / WEB3 / Digital Assets» (~45 строк) — без полного PRESET (crypto не в 10 канонических ниш курса). 7 триггеров / 11 red flags (SEC Howey-test / Reg D unregistered / MICA non-compliance / FCA s.21 / state MTL / AI deepfake celebrity / SEC Kim Kardashian \$1.26M precedent) / 7 substantiation (SEC Form D / Reg A+ / Reg CF / MICA CASP / FCA registration / state MTL / CertiK audit) / 5 rewrite suggestions.

**Файл:** `skills/meta-policy-checker/SKILL.md` (+45 строк).

---

## Волна Т.12 — LOCAL_SERVICE_LOCAL_SEO_GBP_LAYER (extension layer поверх LOCAL_SERVICE)

**Commit:** `3ddebe9` (объединён с Т.11 + Т.13)

**3 агента параллельно** (T.12-A + T.12-B 12 GAP / 5 кейсов + T.12-C мета). Extension layer (7 правил, не полный PRESET) — поверх LOCAL_SERVICE базовых правил.

**Главное:**
- **Fake reviews enforcement** — FTC Notice of Penalty Offenses 2023 (\$53k/violation) + FTC «Consumer Reviewers and Testimonials» Final Rule 2024 (broader: запрет AI reviews + insider + suppression + gating) + state CA SB 567 / NY GBL §349 / TX DTPA.
- **Google Business Profile (GBP) optimization:** photo/video/post compliance, owner-uploaded vs AI-generated rules, Google 2026 tech limits (≤30s, ≤100MB, ≤1080p).
- **Local Service Ads (LSA) Google Guaranteed badge** — background check + insurance + licensing substantiation.
- **Local SEO NAP consistency + schema.org LocalBusiness + multi-location.**
- **Customer testimonial** — written consent + state right of publicity (CA §3344 / NY §50-51 / TX §26.001 / FL §540.08 / TN PRPA) + atypicality disclaimer + AI-generated FAIL FTC §255 2023.
- **Geo-fence / radius targeting disambiguation** — LOCAL_SERVICE OK для Meta vs FHA blocked для housing.
- Финальный 7/7 PASS.

**meta-policy-checker:** новая категория «LOCAL_SERVICE_LOCAL_SEO_GBP_USA — fake reviews + customer testimonial + Google Guaranteed badge».

**Файлы:** `skills/higgsfield-prompt-generator/SKILL.md` (+242 строки extension layer), `skills/meta-policy-checker/SKILL.md` (+60 строк).

---

## Волна Т.11 — B2B_SAAS_SMB_PRESET (PLG / founder-led)

**Commit:** `3ddebe9` (объединён с Т.12 + Т.13)

**3 агента параллельно** (T.11-A + T.11-B 15 GAP / 5 кейсов + T.11-C мета). Отдельный PRESET для PLG / founder-led SMB SaaS (mutually-exclusive с B2B_SAAS_ENTERPRISE по триггеру: чек $19-299/seat → SMB vs $300+/seat → Enterprise).

**8 правил PRESET'а — ключевые отличия от Enterprise:**
1. Marketing Studio + Kling 3.0 (vs Cinema Studio + Veo 3.1 Enterprise) + HANDHELD pack + DESK ENVIRONMENT (home-office, 3-5 used markers vs 1-2 Enterprise).
2. **HUMANIZATION FULL** (vs EXECUTIVE-CALIBRATED Enterprise) — ВСЕ H1-H10 enabled (founder в hoodie, wisp temple OK, room tone, late-night puffy face, built-in-public aesthetic).
3. Pricing direct OK («$19/mo», «Free forever», «14-day trial») + Click-to-Cancel + ROSCA + state ARL (reuse ECOM_IMPULSE Правило 4).
4. Substantiation PLG-sources (G2 / Capterra / TrustRadius / Product Hunt / GitHub stars / YC batch / Indie Hackers / Crunchbase / Stripe Atlas open-startup).
5. Comparative claims named competitor OK в Dialogue (vs hard-block Enterprise) с G2 substantiation, generic alias в overlay.
6. Migration story minutes OK для self-serve PLG (vs 24h FAIL Enterprise, нет SLA contract).
7. Founder Soul ID + AI DISCLOSURE (Twitter / YC / Indie Hackers public domain).
8. SMB-specific guardrails: LTD AppSumo non-refund + acquisition framing (TechCrunch/Crunchbase) + **AI-washing FTC Operation AI Comply 2024** (must demonstrate actual AI use, не marketing).

**meta-policy-checker:** новая категория «B2B_SAAS_SMB — PLG / founder-led / free-trial-to-paid + AI-influencer endorsement».

**Файлы:** `skills/higgsfield-prompt-generator/SKILL.md` (+186 строк PRESET), `skills/meta-policy-checker/SKILL.md` (+107 строк).

---

## Волна Т.10 + Т.9 + П.23 — ECOM_IMPULSE_USA + KIDS_PARENTS_EDTECH + Pre-валидатор A.5 DSHEA

**Commit:** `204b3a8` (2026-05-19)

[оригинальный entry уже описан в SUMMARY-Т9-П24.md — кратко: 2 PRESET + Pre-валидатор A.5 + 2 META категории]

---

## Волна П.24 — Tests 27-50 + SUMMARY-Т9-П24

**Commit:** `3d91b38`

24 теста integration-level (extension для волн П.13-П.23 + Т.1-Т.10), полный отчёт второго полного производственного цикла, 50 тестов total post-П.24.

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
- **QUICK-REFERENCE-NICHE-RESTRICTIONS.md dead-link фикс (4 → 0):** все 4 ссылки заменены на inline cross-ref на CRISIS-AUDIT-LAYER C1-C8 / MEDICAL_HEAVY §16 `[ОТКАЧЕНО 2026-05-20 — MEDICAL_HEAVY свёрнут в LOCAL_SERVICE HIGH_TICKET (медицина)]` / WELLNESS_USA_PRESET. Плагин теперь self-contained.
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

## Волна Т.2 — MEDICAL_HEAVY stress-test (5 агентов) + 3 фикса `[ОТКАЧЕНО 2026-05-20 — MEDICAL_HEAVY как отдельный профиль свёрнут в подпрофиль LOCAL_SERVICE HIGH_TICKET (медицина), см. чистку scope-creep в шапке v3.Т]`

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
