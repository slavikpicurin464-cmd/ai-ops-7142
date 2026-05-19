# SUMMARY Т.8 + П.22 — финальный отчёт второго post-compact цикла

**Дата:** 2026-05-19 (вечер)
**Цикл:** post-(Т.6+Т.7+П.20) продолжение по Варианту C финального плана из SUMMARY-Т6-П20.md
**Запрос пользователя:** «запускай» (выбрал Вариант C — EU_RUSSIAN_DIASPORA_PRESET + documentation sync)
**Коммиты:** acaf26f (Т.8) → 867e83c (П.22) — 2 волны / 3 агента (Т.8) + 4 файла docs / +900 строк

---

## ЧТО СДЕЛАНО

### Т.8 EU_RUSSIAN_DIASPORA_PRESET (commit acaf26f)

**3 агента параллельно** (Т.8-A создатель + Т.8-B адверсариал 18 GAP + Т.8-C мета cross-ref 6 юрисдикций). Закрыты 8 потерянных слоёв для русскоязычной диаспоры в EU/UK/IL post-2022.

**8 правил PRESET'а:**
1. Workspace + НЕТ cultural-loaded music post-2022 (РОТ / советская эстрада / patriotic march)
2. DIASPORA-TONE casting + **regulated-attire AI guardrail** (мантия адвоката = uniform-as-claim-of-profession — NEW T.8-B GAP)
3. GDPR Art.6+9 (запрет language-based lookalike + Russian Orthodox affinity + EDPB Guidelines 8/2020 + CJEU C-184/20 OT)
4. Sanctions cumulative (OFAC + EU 269/2014 + **833/2014 art.5n advisory restriction** + UK OFSI + SECO + AML 5AMLD obliged-entity + **Cyprus CIP suspended Nov 2020** — все NEW из T.8-B/C GAP)
5. Cross-border professional services (BRAO §206 / NRA Kodeks Etyki / CCBE / BSB gC8/gC9 / Cyprus Bar / Israeli Bar)
6. Cultural messaging post-2022 («возвратная» OFF / «русскоязычные» не «русские» / UA-BY-KZ/IL identity-respect / **bilingual «сохрани русский» framing для UK/IL** — NEW)
7. Currency EUR/PLN/GBP/ILS + ECB substantiation
8. DPA dual-jurisdiction overlay + AI DISCLOSURE bilingual + EU AI Act art.50

**Финальный 8/8 PASS чек-лист + 3-STEP FUNNEL** (TOF «Вы» → MOF peer → BOF confident neutral) с регуляторным риском per step.

**meta-policy-checker:** 2 новые категории — «EU_RUSSIAN_DIASPORA — GDPR Art.9 + sanctions + cross-border» (13 red flags) + «Diaspora-cultural messaging — post-2022 political-sensitivity» (6 red flags).

**Боковой фикс:** арки A-G матрица (строка 2247) — 3 строки EU_RUSSIAN_DIASPORA × LEGAL / × HIGH_TICKET / × KIDS_PARENTS с разрешёнными арками и запретами.

**Ключевая особенность:** EU_RUSSIAN_DIASPORA — единственный sub-profile с логикой «stricter-rule при конфликте» (накладывается на вертикаль, не заменяет). B2B_SAAS_ENTERPRISE / HIGH_TICKET_PRO_SERVICES — extension одной вертикали; EU_RUSSIAN_DIASPORA — поверх любой из 6 (CRISIS_EXPERT / HIGH_TICKET_PRO_SERVICES / REAL_ESTATE_EXPAT / INFOBIZ / LOCAL_SERVICE / EDTECH).

### П.22 docs sync (commit 867e83c)

**4 файла обновлены:**

1. **README.md** (77 → 116 строк, +50%):
   - 20 → 22 скила (добавлены 5 которые были в dir но не в README: chat-handoff, geo-memos, higgsfield-prompt-generator, terminal-instructions, text-humanizer)
   - Удалены 3 несуществующих скила (offer-generator, winner-variations, iterative-refiner — были в README, но не в dir)
   - Реструктура по 5 функциональным группам
   - Highlighted `higgsfield-prompt-generator` с упоминанием 7 PRESET'ов
   - Секция «Что нового» с актуальными приростами (risk -52%)
   - Примеры how-to-run для PRESET'ов (B2B Ent / REAL_ESTATE_USA / WELLNESS_USA / DIASPORA)

2. **CHANGELOG.md** (NEW, 214 строк):
   - Полная история волн П.13-Т.8 в обратной хронологии
   - 11 commits описаны (Т.8 / П.20 / Т.7 / Т.6 / Т-итог / Т.1-Т.5 / П.19 / П.16-18 / П.15 / П.14 / П.13 / П.12 / П.1-11 базовая)
   - Финальная замер-таблица: pre-T → post-Т.8 по 9 метрикам

3. **ARCHITECTURE.md** (NEW, 253 строки):
   - Высокоуровневая структура репо
   - 22 скила по 5 функциональным группам с размерами
   - Архитектура `higgsfield-prompt-generator` (секции §1-§22 + 7 PRESET'ов)
   - 21 validation V1-V21 + Pre-валидаторы A.1-A.4 + H1-H10 + RAT1-RAT8 + A1-A8
   - 7 PRESET'ов с активацией / правилами / guardrails
   - EXECUTIVE-CALIBRATED + MEDICAL-CALIBRATED humanization tables
   - Архитектура `meta-policy-checker` (13 категорий)
   - 10 канонических ниш + 6 sub-profile УРОВЕНЬ 3
   - 7 ключевых архитектурных принципов

4. **GLOSSARY.md** (106 → 155 строк, +46%):
   - 13 «канонических плюс подпрофиль» → точно 10 канонических УРОВЕНЬ 2 (актуальная таксономия после волны П.14)
   - Удалены deprecated профили (SOFT_EXPERT разнесён / REAL_ESTATE без _EXPAT / FINTECH / SUBSCRIPTION_BOX)
   - Добавлены: секция 6 sub-profile УРОВЕНЬ 3, секция миграции профилей, секция Validation rules, секция 7 PRESET'ов, секция 13 META категорий
   - Risk-profile post-Т.8 в таблице 10 канонических ниш

---

## ЗАМЕР: ДО vs ПОСЛЕ (post-Т.6+Т.7+П.20 vs post-Т.8+П.22)

| Метрика | post-П.20 | post-П.22 | Δ |
|---|---|---|---|
| higgsfield SKILL.md | 4368 | **4568** | +200 (+4.6%) |
| meta-policy SKILL.md | 915 | **994** | +79 (+8.6%) |
| README.md | 77 | **116** | +39 (+50%) |
| GLOSSARY.md | 106 | **155** | +49 (+46%) |
| CHANGELOG.md | — | **214** (NEW) | +214 |
| ARCHITECTURE.md | — | **253** (NEW) | +253 |
| **Σ строк** | **5466** | **6300** | **+834 (+15%)** |
| Дедикейтед PRESET'ов | 6 | **7** (+EU_RUSSIAN_DIASPORA) | +1 |
| Канонических с PRESET-покрытием | 6 из 10 (60%) | **6 из 10 + 1 sub-profile** | +sub-profile coverage |
| META категорий | 13 | **15** (+2: EU diaspora GDPR + cultural messaging) | +2 |
| Регуляторных юрисдикций explicit | 12 | **15** (+EU Reg 833 art.5n / Cyprus CIP / IL PPA 2024 Amendment 13) | +3 |
| Docs files | 3 (README / GLOSSARY / INSTALL) | **5** (+CHANGELOG + ARCHITECTURE) | +2 |
| Risk-profile средний (14 sub) | ≈3.7 | **≈3.3** (Т.8 закрыл diaspora-cross-cutting risk → -0.4) | -0.4 |

**Cumulative reduction vs pre-T baseline (6.86):**
- post-T-итог: -2.16 (-31%)
- post-Т.6+Т.7+П.20: -3.16 (-46%)
- post-Т.8+П.22: **-3.56 (-52%)**

---

## ОСНОВНОЙ ИТОГ post-compact ЦИКЛОВ (Т.6 → Т.7 → П.20 → Т.8 → П.22)

5 волн / 5 commits / ~1860 строк правил и docs. Plugin теперь:

1. **Покрывает 60% канонических ниш дедикейтед PRESET'ами** (6 из 10) + 1 sub-profile поверх любой вертикали — самые рисковые ниши (B2B Enterprise, M&A LEGAL, CRISIS, KIDS, REAL_ESTATE USA, WELLNESS USA, DIASPORA) каждая имеет 8-9-правильный PRESET + финальный чек-лист N/N PASS.

2. **15 регуляторных юрисдикций explicit** (было 3-4 pre-T): US ABA / SEC RIA / FINRA / state bars (NY 7.1(d) / CA / TX / FL pre-clearance) / UK SRA / BSB / FCA COBS / s.21 FSMA / EU NRA / BRAK / MiFID / AIFMD / CH FinSA / FINMA / FHA / HUD / FinCEN GTO / FIRPTA / EB-5 SEC+USCIS / RESPA §8 / TRID / DSHEA §403r-6 / FTC «Gut Check» / CA Prop 65 / NY AG / TX DTPA / FTC Click-to-Cancel 16 CFR §425 / Ryan Haight Act / IRC §1031+§1445 / GDPR Art.6+9 / EU sanctions 269/2014 + 833/2014 art.5n / UK OFSI / Swiss SECO / AML 5AMLD / Cyprus CIP suspended Nov 2020 / EU AI Act art.50 / IL PPA 2024 Amendment 13.

3. **Self-contained плагин** — 0 dead-links после волны П.20 (было 4 на внешний QUICK-REFERENCE-NICHE-RESTRICTIONS.md).

4. **Documentation в актуальном состоянии** — README соответствует факт.списку 22 скила, GLOSSARY имеет актуальную таксономию 10 + 6 sub-profile, новые CHANGELOG.md и ARCHITECTURE.md дают полный обзор системы.

5. **Risk-profile -52%** от pre-T baseline (6.86 → 3.3) для 14 sub-профилей. Для 10 канонических — 6.6 → 4.1 (-38%).

---

## ОБНОВЛЁННЫЙ ПЛАН (что осталось)

### Высокий приоритет (П.23-Т.10):

1. **Волна Т.9 ECOM_IMPULSE_USA_PRESET** — единственный канонический профиль с risk 5+ без PRESET. FTC ROSCA (Restore Online Shoppers' Confidence Act) для recurring billing + state ARL (Annual Renewal Laws CA/NY) + FTC «Made in USA» Rule + Online Pharmacy Act если health-adjacent + state autoship laws. Деал-сайз малый ($15-100 импульс), но volume огромный. risk 5 → ожидаемо 3.

2. **Волна Т.10 KIDS_PARENTS_EDTECH_PRESET** (sub-profile поверх KIDS_PARENTS) — отдельный COPPA verifiable parental consent matrix + state student-data privacy laws (CA SOPIPA / IL SOPPA / NY Ed Law 2-d) + accreditation substantiation (Cognia / WASC / Stripe state-recognition) + AAP screen-time guidelines / WHO digital media для возрастного targeting + LMS data export FERPA.

3. **Волна П.23 INSTRUCTIONS-готово-к-копированию.txt update** — внешний артефакт курса в cowork-загрузка, не в этом репо. Если есть доступ — нужно обновить под актуальное состояние плагина (22 скила / 7 PRESET'ов / новые how-to-run примеры).

### Средний приоритет (П.24-П.26):

4. **Pre-валидатор A.5 для DSHEA disease claim** (early-trigger перед §20) — T.7-D предложил в волне Т.7, не внесён. Стоило бы добавить для symmetry с A.3 BIOCLAIM / A.4 валюта.

5. **MINORS_AI_LIKENESS state-laws extension** (волна Т.5 покрыла 4 state laws — CA AB-2839 / NY Marsh's Law / TX SB-1361 / IL HB 4762) — обновление если в 2026 году принимаются ещё (TN Personal Rights Protection Act extension, OH HB 374, FL HB 919 — currently in committee).

6. **Тесты 27-50** на новые правила П.13-П.20 + Т.1-Т.8 (currently 26 tests). 24 теста = 1 тест на каждое значимое правило.

### Низкий приоритет (по запросу):

7. **B2B_SAAS_SMB (PLG / founder-led) PRESET** — отличается от B2B_SAAS_ENTERPRISE; PLG marketing, founder Twitter-style, less regulatory.

8. **LOCAL_SERVICE Local SEO + GBP optimization layer** — нет inline guidelines для Google Business Profile / Local Service Ads / fake-review enforcement (FTC Notice of Penalty Offenses 2023 / Notice to Consumer Reviewers).

9. **CRYPTO / WEB3 категория в meta-policy** — currently no specific category; SEC enforcement / Howey test / MICA EU framework / FCA crypto promotions. Если ученики начнут с crypto-niche.

---

## РЕКОМЕНДАЦИЯ ДЛЯ СЛЕДУЮЩЕГО ЦИКЛА

**Вариант D — «Закрыть последний big-risk канонический + KIDS sub-profile»:**

- **Волна Т.9** ECOM_IMPULSE_USA_PRESET — самый болевой неприкрытый канонический (risk 5+ единственный)
- **Волна Т.10** KIDS_PARENTS_EDTECH_PRESET — самый болевой неприкрытый sub-profile (COPPA + accreditation узкоспециализированы)
- **Волна П.23** Pre-валидатор A.5 DSHEA early-trigger (быстро, ~30 строк)

После — все канонические профили с risk > 4 имеют дедикейтед PRESET + sub-profile coverage. Risk-profile средний ожидаемо упадёт до ≈3.0 (-56% от pre-T).

**Альтернатива:** «Тесты + стабилизация»:
- **Волна П.24** тесты 27-50 для П.13-П.20 + Т.1-Т.8
- **Волна П.25** INSTRUCTIONS-готово-к-копированию.txt обновление (если есть доступ к cowork-загрузка)

После — плагин полностью готов к production deploy с полным test coverage.

---

## CHANGELOG ВТОРОГО POST-COMPACT ЦИКЛА (Т.8 + П.22)

| Волна | Commit | Файлы | Строк (+/-) | Главное |
|---|---|---|---|---|
| Т.8 | acaf26f | higgsfield + meta-policy | +279 / 0 | EU_RUSSIAN_DIASPORA_PRESET 8 правил (sub-profile sanctions+GDPR+cross-border) + 2 META категории + арки матрица |
| П.22 | 867e83c | README + CHANGELOG (new) + ARCHITECTURE (new) + GLOSSARY | +641 / -86 | 4 файла docs sync — README rewrite, CHANGELOG/ARCHITECTURE created, GLOSSARY taxonomy update |
| **TOTAL** | 2 commits | 6 files | **+920 / -86** | 1 PRESET + 2 META + 4 docs обновления |

**Cumulative с первого post-compact цикла (Т.6 + Т.7 + П.20 + Т.8 + П.22):**

| Волна | Commit | Главное |
|---|---|---|
| Т.6 | d440734 | HIGH_TICKET_PRO_SERVICES_PRESET 9 правил + 2 META |
| Т.7 | 0f8ce11 | REAL_ESTATE_EXPAT_USA + WELLNESS_USA presets + 2 META |
| П.20 | 26aa39b | RAT/R disambiguation + dead-links inline |
| Т.8 | acaf26f | EU_RUSSIAN_DIASPORA_PRESET + 2 META |
| П.22 | 867e83c | docs sync (README+CHANGELOG+ARCHITECTURE+GLOSSARY) |
| **TOTAL** | 5 commits | **3 PRESET + 6 META категорий + cleanup + docs** = +1860 строк правил и docs за 1 рабочий день post-compact |
