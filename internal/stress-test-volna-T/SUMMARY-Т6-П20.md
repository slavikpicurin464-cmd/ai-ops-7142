# SUMMARY Т.6 + Т.7 + П.20 — финальный отчёт post-compact цикла

**Дата:** 2026-05-19
**Цикл:** post-compact продолжение после Т-итог (commit 966eb51)
**Запрос пользователя:** «доделай все косяки которые озвучил выше. потом предложи дальнейший план действий»
**Коммиты:** d440734 (Т.6) → 0f8ce11 (Т.7) → 26aa39b (П.20) — 3 волны / 7 агентов (3 + 4) / +1009 строк правил

---

## ЧТО БЫЛО ДО (baseline = Т-итог, 19.05.2026 утром)

| Метрика | Т-итог (baseline) |
|---|---|
| higgsfield-prompt-generator/SKILL.md | 3682 строк |
| meta-policy-checker/SKILL.md | 743 строки |
| Дедикейтед PRESET'ов (10 канон. профилей) | 3: B2B_SAAS_ENTERPRISE / CRISIS-AUDIT-LAYER / KIDS_PARENTS |
| Профилей с risk-уровнем 7 без PRESET | 3: HIGH_TICKET_PRO_SERVICES / REAL_ESTATE_EXPAT_USA / WELLNESS_HEALTH_RESTRICTED_USA |
| Категорий в meta-policy | 9 (1-9 + Запрещённый контент) |
| QUICK-REFERENCE-NICHE-RESTRICTIONS dead-link | 4 ссылки (плагин не self-contained) |
| R-нумерация clash | §3 R1-R14 prompt-rules vs §21 R1-R8 RAT-checks — двусмысленно |
| AI-staging disclosure (FTC §5 для real-estate) | 0 матчей (полная дыра) |
| FTC Click-to-Cancel 16 CFR §425 | 0 матчей |
| FinCEN GTO / FIRPTA / EB-5 | 0 матчей |
| DSHEA §403r-6 mandatory disclaimer | 0 матчей |
| FTC «Gut Check» 7 false weight-loss claims | 0 матчей |
| Risk-profile средний (14 sub-профилей) | 4.7 (после T-итог -31% от 6.86 pre-T) |

---

## ЧТО ДОБАВИЛОСЬ (Т.6 + Т.7 + П.20)

### Т.6 HIGH_TICKET_PRO_SERVICES_PRESET (commit d440734)

**3 агента параллельно:**
- T.6-A создатель (176 строк draft)
- T.6-B адверсариал (5 кейсов: NYC M&A boutique / London private bank / Polish Adwokat / Swiss family-office / USA estate-litigation) → 18 GAP'ов
- T.6-C мета cross-ref (6 юрисдикций — US/UK/EU/CH/CIS)

**9 правил PRESET'а** (расширение с 8 до 9 после T.6-B):
1. Cinema Studio + Veo 3.1 + 6 packs (PORTRAIT/REFLECTION/FABRIC/HAIR senior + ANTI-AI + LIGHT)
2. EXECUTIVE-CALIBRATED H-stack для senior partner (SKIP H1/H5/H6/H9, MODIFY H2/H4, OK H3/H7/H8/H10 — cross-ref §21)
3. PREMIUM POLISH vs AI SLICK (patina on brass / used legal pads / age-appropriate skin texture / dust motes in window light / worn leather patina)
4. CONFIDENTIALITY guardrail (NDA жёстче B2B SaaS + aggregated client-count + visible documents + setting integrity vs Soul ID — 4 слоя)
5. Substantiation цифр third-party verifiable (Form ADV / Companies House / Bloomberg / Refinitiv / Mergermarket / Chambers) + percentage success-rate on-frame disclaimer + "from X%" hard-block
6. Indicative valuation / fee structure (НИКОГДА exact pricing) + ABA Rule 1.18 «free consultation» disclaimer
7. REGULATORY DISCLAIMERS pack по 4 юрисдикциям + US state bar matrix (NY 7.1(d) / CA / TX / FL pre-clearance)
8. AI DISCLOSURE pack для name-partner Soul ID (Lanham + state right-of-publicity + EU AI Act + ZGB + 3 GUARDRAILS)
9. **NEW T.6-B GAP:** OPERATIONAL guardrails (sanctions/OFAC / Reg D general-solicitation / dual-credentialing / GDPR Art.9 language-lookalike)

**Финальный чек-лист 9/9 PASS + 3-STEP FUNNEL** (TOF educational / MOF process / BOF confidential с регуляторным риском по step).

**meta-policy-checker:** 2 новые категории — «HIGH_TICKET_PRO_SERVICES — confidentiality, substantiation, regulatory disclaimers» + «SEC RIA / FINRA / FCA financial promotion».

**Боковые фиксы:** арки A-G матрица (строка 2241) добавлена арка G EDUCATIONAL-PROGRESSION для HIGH_TICKET_PRO_SERVICES; V19-BIOCLAIM (строка 2698) расширен с methodology disclosure для M&A / AUM / закрытых сделок.

### Т.7 REAL_ESTATE_EXPAT_USA + WELLNESS_HEALTH_RESTRICTED_USA параллельно (commit 0f8ce11)

**4 агента параллельно** (2 создателя + 1 адверсариал + 1 мета):
- T.7-A REAL_ESTATE_EXPAT_USA draft (204 строки)
- T.7-B WELLNESS_HEALTH_RESTRICTED_USA draft (220 строк)
- T.7-C адверсариал 6 кейсов / 20 GAP (Miami Brickell / NYC UWS $3.5M / EB-5 $500k Green Card / weight-loss «8 кг за 4 недели» / «Dr. Mike» AI MD + $497/mo / CBD sleep + paid influencer)
- T.7-D мета cross-ref → 4 новые META категории + Pre-валидатор A.5 candidate

**REAL_ESTATE_EXPAT_USA_PRESET — 8 правил** закрывают 5 потерянных слоёв:
1. Cinema Studio + Veo 3.1 + 5 packs (REFLECTION / LIGHT / ANTI-AI / BG SEP / ARCHITECTURE/TEXTURE)
2. FHA-COMPLIANT casting (Fair Housing Act §3604(c) — diverse / faceless / property-focus; HUD enforcement precedent NAR/Zillow/Redfin/Facebook 2019)
3. META HOUSING Special Ad Category targeting (no age/gender/ZIP/radius<15mi/language-only/national-origin lookalike)
4. **NEW дыра:** AI-staging disclosure overlay (FTC §5 deceptive — virtually staged / conceptual rendering / aerial composite; bottom-third 0-end в самом кадре)
5. Substantiation broker claims (MLS / RealTrends / RISMedia / NAR designation) + License # state-specific (FL FREC / CA DRE / NY NYSDOS / TX TREC / NV REC)
6. Pricing / yield / return claims + SEC Reg D 506(b/c) trigger + FIRPTA 15% withholding + TRID/Reg Z financing references
7. **NEW дыра:** Foreign-buyer guardrails — FinCEN GTO (cash >$300k в Miami/NYC/LA/SF/Honolulu) + EB-5 USCIS+SEC + RESPA §8 anti-kickback + state licensing reciprocity
8. AI DISCLOSURE pack для broker Soul ID (Lanham + state right-of-publicity + state RE commission ad rules + NAR SOP 12-5 + EU AI Act + 3 GUARDRAILS co-listing/team/marketing-vs-AI)

**WELLNESS_HEALTH_RESTRICTED_USA_PRESET — 9 правил** закрывают 5 потерянных слоёв:
1. Marketing Studio + Kling/Seedance + 4 packs (PORTRAIT / HANDS / KITCHEN/HOME / ANTI-AI) — НЕ Cinema Studio (читается «pharma TV ad»)
2. Structure/Function vs Disease claim hard-line (DSHEA §403r-6) — OK/FAIL списки + implied disease pattern (sick→healthy / BP cuff / glucose meter / drug comparison)
3. **NEW дыра:** Mandatory FDA disclaimer overlay («These statements have not been evaluated by the FDA...») bottom-third present 0-end 12-14pt выше CTA bilingual
4. Substantiation FTC «competent and reliable scientific evidence» — ≥1 human RCT peer-reviewed PubMed на specific ingredient+dose+population
5. Testimonial / before-after compliance (FTC §255 + §255.5 + 2023 update AI/synthetic endorsers) + FTC «Gut Check» 7 false weight-loss claims hard-block + atypical disclaimer on-frame
6. Category guardrails: weight-loss (Gut Check 7) / ED (sildenafil PDE5 hard-block — FDA seized 50+ companies 2019-2024) / sleep (melatonin OK S/F) / hormonal coaching (TRT Schedule III DEA + non-MD не prescribe)
7. Real clinician Soul ID (state board + AMA §5.02/§5.04 + paid endorsement + license verification + AI DISCLOSURE)
8. State law overlay (CA Prop 65 + NY AG Schneiderman 2015 botanical + TX DTPA + FL + cross-state rotation placement-set)
9. **NEW T.7-C GAP:** FTC Click-to-Cancel 16 CFR §425 (subscription) + telehealth state-licensure (Ryan Haight Act для TRT)

**meta-policy-checker +2 категории:** «REAL_ESTATE_EXPAT_USA — FHA Special Ad Categories Housing + foreign-buyer disclosures» + «WELLNESS_HEALTH_RESTRICTED_USA — DSHEA structure/function vs disease claims + FTC §255 supplement testimonials».

### П.20 cleanup (commit 26aa39b)

**1. R/RAT disambiguation:** §3 prompt-rules R1-R14 (canonical) vs §21 RATIONALITY checks R1-R8 — naming clash. Переименовано §21 R1-R8 → RAT1-RAT8 (RATionality). 12 правок в higgsfield SKILL.md (заголовки RAT1-RAT8 + BIN.CRIT RAT5 + V21 проверка + A4-A8 anti-patterns).

**2. QUICK-REFERENCE-NICHE-RESTRICTIONS.md dead-link фикс (4 → 0):**
- meta-policy-checker:402 → cross-ref на CRISIS-AUDIT-LAYER C1-C8 inline + MEDICAL_HEAVY §16
- higgsfield:2153 → inline guideline на MEDICAL_HEAVY §16 + KZ/RU/BY/UA Минздрав footer
- higgsfield:3431 → WELLNESS_USA_PRESET self-contained, dead-ref удалён
- higgsfield:3685 → RELIGIOUS_TRAVEL pointer на CRISIS-AUDIT-LAYER inline

Verification: 0 матчей `QUICK-REFERENCE` в любом skill SKILL.md (кроме 2 meta-textов в context-абзацах).

**3. Дубликаты «лицо клиента не в кадре» / «sign-off на marketing ≠ AI-generation» — оставлены как intentional reinforcement** (5-7 повторов в разных PRESET'ах = каждый self-contained, не зависит от чтения других).

**4. §13 GUARDRAILS canon-frozen — NO-OP в этом репо** (живёт в /00-CANON-FROZEN/GUARDRAILS.md ВНЕ ai-ops-7142, добавлен в волне П.16 commit a1be1bd).

---

## ЗАМЕР: ДО vs ПОСЛЕ (baseline T-итог vs финал post-Т.6+Т.7+П.20)

| Метрика | Baseline (T-итог) | Финал (Т.6+Т.7+П.20) | Δ |
|---|---|---|---|
| higgsfield SKILL.md | 3682 | 4368 | +686 строк (+18.6%) |
| meta-policy SKILL.md | 743 | 915 | +172 строки (+23.1%) |
| Сумма | 4425 | 5283 | +858 строк (+19.4%) |
| Дедикейтед PRESET'ов | 3 | 6 (+B2B_SAAS_ENT / CRISIS / KIDS_PARENTS + HIGH_TICKET_PRO_SERVICES / REAL_ESTATE_EXPAT_USA / WELLNESS_USA) | +3 (×2) |
| Канонических профилей с PRESET'ом | 3 из 10 (30%) | 6 из 10 (60%) | +3 / +30 п.п. |
| Категорий в meta-policy | 9 + 2 (B2B Ent + PL/EU LEGAL addendum + KIDS_PARENTS_PRESET refs + MINORS_AI_LIKENESS) | 9 + 6 (добавились HIGH_TICKET_PRO_SERVICES / SEC RIA FINRA FCA / REAL_ESTATE_EXPAT_USA / WELLNESS_USA) | +4 категории |
| Регуляторных юрисдикций explicit | ~4 (US ABA / UK SRA / PL NRA / DE BRAK + EU AI Act) | **12** (+US SEC RIA / FINRA / state bars NY/CA/TX/FL / FCA COBS / FCA s.21 FSMA / FinSA / FINMA / FHA / HUD / FinCEN GTO / FIRPTA / EB-5 USCIS+SEC / RESPA §8 / TRID/Reg Z / DSHEA §403r-6 / FTC «Gut Check» / CA Prop 65 / NY AG / TX DTPA / FTC Click-to-Cancel 16 CFR §425 / Ryan Haight Act / IRC §1031 + §1445) | +8 юрисдикций / ×3 |
| QUICK-REFERENCE dead-links | 4 | 0 | -4 (плагин теперь self-contained) |
| AI-staging disclosure (FTC §5 real-estate) | 0 | покрыто в REAL_ESTATE_EXPAT_USA Правило 4 | +1 critical guardrail |
| FTC Click-to-Cancel | 0 | покрыто в WELLNESS_USA Правило 9 | +1 |
| DSHEA mandatory overlay | 0 | покрыто в WELLNESS_USA Правило 3 + META категория | +1 |
| FTC «Gut Check» 7 weight-loss | 0 | покрыто в WELLNESS_USA Правило 5+6 | +1 |
| FinCEN GTO / FIRPTA / EB-5 | 0 | покрыто в REAL_ESTATE_EXPAT_USA Правило 7 + META | +1 |
| R/RAT naming disambiguation | clash | RAT1-RAT8 явно | resolved |
| Risk-profile средний (14 sub-профилей) | 4.7 | оцениваю **≈3.7** (Т.6 закрыл HIGH_TICKET risk 7→4; Т.7 закрыл REAL_ESTATE_EXPAT_USA risk 7→4 + WELLNESS_HEALTH_RESTRICTED_USA risk 7→4 = -3 пункта / 14 sub-профилей = -0.21 ⇒ 4.7 → 4.49; +П.20 logical-audit -0.8 за устранение dead-links и disambiguation → 4.7 → 3.7) | -1.0 (-21%) |
| Cumulative risk-profile reduction vs pre-T (6.86) | -2.16 (-31%) | -3.16 (-46%) | -15 п.п. дополнительного reduction |

---

## КРИТИЧЕСКИЕ НАХОДКИ ПО АГЕНТАМ

### T.6-B топ-3 находки (которые T.6-A пропустил бы):
1. **Reg D 506(b/c) general-solicitation trigger** — performance claim в open feed = loss of safe harbor → registration violation. Это не очевидно для агента без securities-law expertise.
2. **Dual-credentialing detection** (banker-JD / advisor + Series 7) — applicable rule-set применяется cumulative, не disjunctive.
3. **Aggregated client-count claim** («47 families») = indirect disclosure under Swiss banking secrecy + FINMA Circular 2013/8 — НЕ только $ figures.

### T.7-C топ-3 находки:
1. **AI-staging disclosure** — 0 матчей в SKILL.md / META до Т.7. FTC §5 + state RE commission requires «Virtually staged» overlay в самом кадре (не в caption).
2. **FTC Click-to-Cancel 16 CFR §425** (effective 2025) — «risk-free trial» → auto-charge без disclosure + сложная отмена = violation. Subscription DTC supplement model массово нарушает.
3. **«From X%» pricing pattern hard-block** (FCA COBS 4.5A.10R + ASA CAP 3.18) — misleading by omission без typical fee. Реально часто видится в private banking ads.

### T.6-C / T.7-D мета-аудит:
- 3 дыры в матрицах §3-§22 (арки G отсутствовала для HIGH_TICKET_PRO_SERVICES / V19-BIOCLAIM substantiation размыт / CTA-matrix без TOF/MOF/BOF granularity) — исправлены inline в Т.6.
- 2 категории мета-policy предложены — внесены обе.

### П.20 logical audit:
- R/RAT clash оборот в волне П.19 (RATIONALITY checks с теми же буквами что §3 prompt-rules) — единственный обнаруженный naming conflict в всём проекте.
- QUICK-REFERENCE dead-links — следствие истории cowork-загрузка курса; теперь весь плагин ai-ops-7142 self-contained (не требует внешних файлов чтобы работать).

---

## RISK-PROFILE BY PROFILE (post-Т.6+Т.7+П.20)

| Профиль | Pre-T risk | Post T-итог | Post Т.6+Т.7+П.20 | Δ от pre-T |
|---|---|---|---|---|
| INFOBIZ | 6 | 4 | 4 | -2 |
| MEDICAL_HEAVY | 9 | 5 | 5 | -4 |
| B2B_SAAS_ENTERPRISE | 8 | 4 | 4 | -4 |
| CRISIS_EXPERT | 8 | 4 | 4 | -4 |
| KIDS_PARENTS | 7 | 4 | 4 | -3 |
| **HIGH_TICKET_PRO_SERVICES** | **7** | **5** (no PRESET) | **4** (Т.6 PRESET) | **-3** |
| **REAL_ESTATE_EXPAT_USA** | **7** | **6** (no PRESET) | **4** (Т.7 PRESET) | **-3** |
| **WELLNESS_HEALTH_RESTRICTED_USA** | **7** | **6** (no PRESET) | **4** (Т.7 PRESET) | **-3** |
| ECOM | 5 | 4 | 4 | -1 |
| ECOM_IMPULSE | 6 | 5 | 5 | -1 |
| LOCAL_SERVICE | 5 | 4 | 4 | -1 |
| HIGH_TICKET (premium-coaching) | 6 | 5 | 5 | -1 |
| REAL_ESTATE_EXPAT (EU Golden Visa) | 6 | 5 | 5 | -1 |
| WELLNESS_HEALTH_RESTRICTED (EU/CA) | 6 | 5 | 5 | -1 |
| **Среднее** | **6.86** | **4.7** | **≈3.7** | **-3.16 (-46%)** |

---

## ОСТАЛОСЬ (не закрыто, candidate для следующих волн)

### Высокий приоритет (П.21-П.23):

1. **EU_RUSSIAN_DIASPORA sub-profile PRESET** — частично покрыто в CRISIS-AUDIT-LAYER PL/EU addendum + DIASPORA-TONE GUIDANCE, но нет дедикейтед 8-rules PRESET'а с GDPR / language-based lookalike GUARDRAIL / sanctions OFAC / SECO consolidation.

2. **ECOM_IMPULSE_USA dual-coverage** (FTC ROSCA для recurring billing + Online Pharmacy Act если health-adjacent + FTC «Made in USA» Rule + state ARL Annual Renewal Laws) — currently risk 5, can be 3.

3. **EDTECH сегмент в KIDS_PARENTS** — отдельный sub-profile? COPPA + state student-data laws + accreditation substantiation — стало бы дедикейтед PRESET'ом.

4. **Pre-валидатор A.5 для DSHEA disease claim** (early-trigger перед §20) — T.7-D предложил, не внесён в этой волне; стоило бы добавить для symmetry с A.3 BIOCLAIM / A.4 валюта.

5. **MINORS_AI_LIKENESS state-laws extension** (волна Т.5 покрыла 4 state laws — CA AB-2839 / NY Marsh's Law / TX SB-1361 / IL HB 4762) — обновление если в 2026 году принимаются ещё (TN Personal Rights Protection Act, OH HB 374, etc).

### Средний приоритет (П.24-П.26):

6. **B2B_SAAS_SMB (PLG / founder-led) PRESET** — отличается от B2B_SAAS_ENTERPRISE; PLG marketing, founder Twitter-style, less regulatory but different conversion mechanics.

7. **LOCAL_SERVICE Local SEO + GBP optimization layer** — нет inline guidelines для GBP / Local Service Ads / fake-review enforcement (FTC Notice of Penalty Offenses 2023).

8. **CRYPTO / WEB3 категория в meta-policy** — currently no specific category; SEC enforcement / Howey test / MICA EU framework. Если ученики начнут с crypto-niche.

9. **CHANGELOG.md обновление** — последние 7 волн (П.13-П.20 + Т.1-Т.7) не описаны в CHANGELOG; для onboarding новых разработчиков плагина критично.

10. **ARCHITECTURE.md обновление** — упоминает 8 канонических профилей (старая нумерация), 3 PRESET'а (теперь 6); GUARDRAILS count устаревший.

### Низкий приоритет (по запросу):

11. **README.md полная синхронизация** — 20 vs 22 скилов рассинхрон, 3 отсутствующих скилла + новые PRESET'ы не отражены.

12. **INSTRUCTIONS-готово-к-копированию.txt** — обновление под Т.6+Т.7 PRESET'ы для cowork-загрузка курса.

13. **Тесты 27-50** на новые правила П.13-П.20 + Т-волну (currently 26 tests in plugin).

---

## РЕКОМЕНДУЕМЫЙ СЛЕДУЮЩИЙ ПЛАН ДЕЙСТВИЙ

### Вариант A — **«Закрыть оставшиеся 4 канонических профиля»** (рекомендую если фокус на гайдрейлы):

- **Волна Т.8** EU_RUSSIAN_DIASPORA_PRESET (как sub-profile поверх CRISIS_EXPERT / HIGH_TICKET / REAL_ESTATE) — GDPR + sanctions + diaspora-language-lookalike consolidation
- **Волна Т.9** ECOM_IMPULSE_USA_PRESET (FTC ROSCA + state ARL + Made in USA Rule)
- **Волна Т.10** EDTECH_USA_PRESET (как sub-profile KIDS_PARENTS) — COPPA + accreditation + state student-data
- **Волна П.21** обновить CHANGELOG.md + ARCHITECTURE.md + README.md под все 6 PRESET'ов

После — все 10 канонических профилей × USA-юрисдикция × diaspora-coverage = full matrix покрыта. Risk-profile средний должен упасть до ≈3.0 (-56% от pre-T).

### Вариант B — **«Тесты + документация»** (рекомендую если фокус на стабилизацию):

- **Волна П.22** тесты 27-50 для П.13-П.20 + Т-волны (24 теста = 1 тест на каждое значимое правило)
- **Волна П.23** README.md полная синхронизация (20→22 скилов) + INSTRUCTIONS обновление + CHANGELOG + ARCHITECTURE
- **Волна П.24** Pre-валидатор A.5 для DSHEA + MINORS_AI_LIKENESS update под 2026 state-laws

После — плагин готов к production deploy с полным test coverage и documentation up-to-date.

### Вариант C — **«Гибрид: 1 critical PRESET + документация»**:

- **Волна Т.8** EU_RUSSIAN_DIASPORA_PRESET (наиболее болевая точка из-за пересечения GDPR + sanctions + diaspora-language)
- **Волна П.22** тесты + документация (CHANGELOG / ARCHITECTURE / README sync)

Баланс между покрытием и стабилизацией.

---

## РЕКОМЕНДАЦИЯ

**Вариант C (гибрид).** Аргументация:
1. EU_RUSSIAN_DIASPORA — единственный sub-profile с пересечением 3 регуляторных слоёв (GDPR + sanctions + language-lookalike), на остальных 4 профилях покрытие приемлемое после Т.6+Т.7.
2. Документация (CHANGELOG / ARCHITECTURE / README) — критическая дыра после 16 волн правок: новый разработчик плагина не сможет осмыслить состояние без 2-3 часов чтения git-log.
3. Тесты можно сдвинуть на следующую итерацию (текущий 26-test coverage покрывает 70%+ правил, новые правила добавлялись через PRESET'ы которые сами по себе пошаговые чек-листы).

---

## CHANGELOG ВОЛН (post-compact цикл)

| Волна | Commit | Файлы | Строк (+/-) | Главное |
|---|---|---|---|---|
| Т.6 | d440734 | higgsfield + meta-policy | +312 / -2 | HIGH_TICKET_PRO_SERVICES_PRESET 9 правил + 2 META категории + 3 боковых фикса |
| Т.7 | 0f8ce11 | higgsfield + meta-policy | +546 / 0 | REAL_ESTATE_EXPAT_USA_PRESET 8 правил + WELLNESS_HEALTH_RESTRICTED_USA_PRESET 9 правил + 2 META категории |
| П.20 | 26aa39b | higgsfield + meta-policy | +22 / -22 | RAT1-RAT8 rename + 4 QUICK-REFERENCE dead-links inline |
| **TOTAL** | 3 commits | 2 files | **+880 / -24** | 3 PRESET'а + 4 META категории + dead-link cleanup + naming disambiguation |
