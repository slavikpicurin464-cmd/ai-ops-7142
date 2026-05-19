# ARCHITECTURE — ai-ops-7142

Архитектурный обзор плагина по состоянию на 2026-05-19 (post-Т.8).

---

## Высокоуровневая структура

```
ai-ops-7142/
├── README.md           — обзор + 22 скила + how-to-run
├── INSTALL.md          — установка через /plugin marketplace
├── CHANGELOG.md        — история волн П.1-П.20 + Т.1-Т.8
├── ARCHITECTURE.md     — этот файл
├── GLOSSARY.md         — единый словарь имён (профили / бюджеты / артефакты)
├── skills/             — 22 скила (см. ниже)
└── internal/
    └── stress-test-volna-T/
        ├── SUMMARY-Т1-Т5.md    — отчёт T-итог
        └── SUMMARY-Т6-П20.md   — отчёт post-compact
```

---

## 22 скила по функциональным группам

### 1. Подготовка проекта (этапы 1-4 конвейера)

| Скил | Размер | Главная функция |
|---|---|---|
| `client-profile` | small | 10 канонических ниш + 6 sub-profile УРОВЕНЬ 3 + 3 бюджетных режима |
| `brand-extractor` | small | Сайт/инст/крео → brand kit |
| `style-guide-extractor` | small | 3-10 референсов → текстовый стайл-гайд |
| `research-structurer` | medium | Сырьё (транскрипт/отзывы) → ABCDX-таблица |
| `ru-marketer` | medium | Чат-маркетолог: сегментация, ресерч, стратегия |

### 2. Стратегия и креативная разработка (этапы 5-7)

| Скил | Размер | Главная функция |
|---|---|---|
| `schwartz-podhody` | small | 4 подхода по Шварцу под каждый сегмент |
| `reality-check-metrics` | medium | Предельный CPL по экономике + reality-check |
| `ad-teardown` | medium | Разбор чужой рекламы из Ads Library / AdHeart |
| `ru-copywriter` | medium | Хуки / заголовки / UGC-скрипты / посты / карусели |
| `creative-brief-writer` | medium | 14-блочное ТЗ дизайнеру / копирайтеру / продакшну |
| **`higgsfield-prompt-generator`** | **XL (4568 строк)** | **Промпты под видео-нейросети + 7 дедикейтед PRESET'ов + 21 валидация (см. ниже)** |
| `text-humanizer` | small | Переписывание AI-текста на живую речь |

### 3. Запуск, проверка, диагностика (этапы 7-9)

| Скил | Размер | Главная функция |
|---|---|---|
| `meta-policy-checker` | **L (994 строк)** | 13 категорий регуляторного контроля Meta + цепочка ниш с pre-launch гейтом |
| `meta-launch-checklist` | medium | Pixel/CAPI/домен/iOS/UTM чек-лист |
| `campaign-diagnoser` | medium | Диагностика 7 узлов отказа кампании |
| `weekly-report-writer` | medium | Недельный/месячный отчёт клиенту |
| `client-comms` | medium | Возражения клиента + передача проекта другому таргетологу |

### 4. Качество и память

| Скил | Размер | Главная функция |
|---|---|---|
| `quality-gate` | medium | 10-пунктовая проверка артефакта pre-delivery |
| `memory-updater` | small | Файл памяти клиента post-итерация |

### 5. Утилиты сессии

| Скил | Размер | Главная функция |
|---|---|---|
| `chat-handoff` | small | Compact summary для нового чата |
| `geo-memos` | small | Гео-специфичные памятки (KZ/EU/USA/UK) |
| `terminal-instructions` | small | Маркировка интерактивных shell-команд |

---

## Архитектура `higgsfield-prompt-generator` (4568 строк, главный скил)

### Секции (по верхнему уровню)

```
§1.  CANON-FROZEN intro                  (строки ~1-50)
§2.  R1-R14 — 14 prompt-engineering rules (строки ~210-244)
§3.  Vocabulary anchors                  (строки ~250-400)
§4.  Currency conversion + ECB rates     (строки ~400-440)
§5.  Workspace selection matrix          (строки ~450-650)
§6.  Model picker (Veo/Kling/Seedance)   (строки ~650-820)
§7.  GUARDRAILS общая                    (строки ~820-980)
§8.  INFOGRAPHIC packs (§19A+19B inline) (строки ~980-1180)
§9.  P1-P10 reference prompts            (строки ~1180-1700)
§10. Quick Diagnosis Index               (строки ~1680-1740)
§11. Soul ID guardrails                  (строки ~1740-1820)
§12-§14. Pack composition / Veo specifics (строки ~1820-1980)
§15. NEVER list (23 rules)               (строки ~1980-2200)
§16. MEDICAL_HEAVY rules                 (строки ~1980-2160)
§17. Pre-валидаторы A.1-A.4              (строки ~2180-2200)
§18A. SPLIT-SCREEN                       (строки ~1880-1900)
§19A. UI MOCKUP PIPELINE                 (строки ~1980-2070)
§19B. INFOGRAPHIC-CHART PIPELINE         (строки ~2120-2200)
§20. OFFER → STORY MAPPING (арки A-G)    (строки ~2200-2470)
§21. HUMANIZATION + SCRIPT RATIONALITY   (строки ~2470-2650)
   - H1-H10 humanization
   - RAT1-RAT8 rationality (renamed from R1-R8 in П.20)
   - V21 validation
   - A1-A8 anti-patterns
   - EXECUTIVE-CALIBRATED + MEDICAL-CALIBRATED tables
§22. Связь с другими скилами             (строки ~2700-2880)

— 7 PRESET'ов sub-vertical —

B2B_SAAS_ENTERPRISE_PRESET               (строки ~2880-3020) — 8 правил
CRISIS_EXPERT short defaults             (строки ~3020-3030)
CRISIS-AUDIT-LAYER                       (строки ~3030-3170) — C1-C8 + 3-step funnel + DIASPORA-TONE TUNING
KIDS_PARENTS short defaults              (строки ~3240-3260)
KIDS_PARENTS_PRESET                      (строки ~3260-3410) — 8 правил + 3 Soul ID modes + MINORS_AI_LIKENESS
HIGH_TICKET_PRO_SERVICES_PRESET          (строки ~3415-3650) — 9 правил + 6 юрисдикций
REAL_ESTATE_EXPAT_USA_PRESET             (строки ~3220-3450 в порядке reading) — 8 правил + FHA/FinCEN/EB-5/RESPA
WELLNESS_HEALTH_RESTRICTED_USA_PRESET    (строки ~3460-3680) — 9 правил + DSHEA/FTC/state-laws
EU_RUSSIAN_DIASPORA_PRESET               (строки ~3670-3920) — 8 правил sub-profile sanctions+GDPR+cross-border

RELIGIOUS_TRAVEL preset                  (строки ~3920+)
... другие профили
```

### Validation rules V1-V21 + Pre-валидаторы A.1-A.4

| ID | Что проверяет |
|---|---|
| V1-V16 | Базовые pre-launch проверки (workspace / pack / format / Soul ID / hook / dialogue / etc) |
| **V17** | Hook против Жертвы (нет «жертвенного» framing в первые 1.5s) |
| **V18** | Anchor pricing / substantiation цифр |
| **V19** | Persona claims («основатель с 2015 / 47 закрытых сделок») |
| **V19-BIOCLAIM** | Biographical claim с числом (substantiation чек-лист) |
| **V20** | Offer ↔ story coherence (арка соответствует офферу) |
| **V21** | Humanization (H1-H10) + Rationality (RAT1-RAT8) финальный pre-flight |
| **A.1** | Absolute promise («гарантия» / «100%») early-trigger |
| **A.2** | Real brand mention check |
| **A.3** | BIOCLAIM early-trigger (волна Т.2) |
| **A.4** | Non-USD currency conversion (волна Т.2) |

### 7 PRESET'ов sub-vertical

| PRESET | Правил | Активируется когда | Главные guardrails |
|---|---|---|---|
| `B2B_SAAS_ENTERPRISE_PRESET` | 8 | B2B_SAAS + чек 300+ USD/seat OR CTO Fortune 500 target | SLA substantiation / disparagement / migration timeline / AI DISCLOSURE public CEO |
| `CRISIS-AUDIT-LAYER` | C1-C8 | CRISIS_EXPERT (юр / банкротство / развод / addiction) | Лицо клиента не в кадре / combined identifier / urgency forbidden / voice-only testimonial запрет |
| `KIDS_PARENTS_PRESET` | 8 | KIDS_PARENTS + детский продукт / family-content | 3 Soul ID modes / 5 acceptable child-in-frame modes / MINORS_AI_LIKENESS state-laws / FTC §255.5 parent-endorser |
| `HIGH_TICKET_PRO_SERVICES_PRESET` | 9 | M&A / corporate LEGAL / private banking / family-office (100k-50M+ USD deals) | EXECUTIVE-CALIBRATED H-stack / NDA жёстче B2B / regulatory disclaimers 4 юрисдикции / Reg D general-solicitation / dual-credentialing |
| `REAL_ESTATE_EXPAT_USA_PRESET` | 8 | REAL_ESTATE + US-гео / foreign-buyer / EB-5 | FHA §3604(c) casting / Meta Housing SAC / AI-staging FTC §5 / FinCEN GTO / FIRPTA / EB-5 SEC+USCIS / RESPA §8 |
| `WELLNESS_HEALTH_RESTRICTED_USA_PRESET` | 9 | WELLNESS + US-гео (supplement / TRT / weight-loss / ED / sleep) | DSHEA structure/function / FDA disclaimer overlay / FTC «Gut Check» 7 / CA Prop 65 / NY AG / Click-to-Cancel / Ryan Haight Act |
| `EU_RUSSIAN_DIASPORA_PRESET` | 8 | Любая вертикаль + русскоязычная диаспора EU/UK/IL | **Sub-profile** (накладывается, не заменяет — stricter rule при конфликте): GDPR Art.9 language-targeting / sanctions OFAC+SECO+EU 833 art.5n / cross-border BRAO/NRA/BSB / cultural messaging post-2022 / Cyprus CIP suspended |

### EXECUTIVE-CALIBRATED + MEDICAL-CALIBRATED humanization tables

Раздел внутри §21. SKIP/MODIFY/OK таблица для H1-H10 по register:

| Register | SKIP | MODIFY | OK |
|---|---|---|---|
| INFOBIZ founder (casual) | — | — | All H1-H10 |
| Executive (CTO/partner) | H1 wisp / H5 handheld / H6 wrinkled / H9 lived-life | H2 cadence / H4 not-actor | H3 lived-in (1-2 markers max) / H7 / H8 / H10 |
| Medical clinic | H1 wisp / H6 wrinkled coat / H9 lived-life face | H2 / H4 | H3 lived-in clinic / H7 / H8 / H10 |

---

## Архитектура `meta-policy-checker` (994 строки)

### 13 категорий

| # | Категория | Когда применяется |
|---|---|---|
| 1 | Запрещённый контент (полный стоп) | Скам / контрафакт / шпионаж / оружие / etc |
| 2 | Финансовые продукты (лицензированные брокеры / банки) | FINTECH / FINANCE с гарантиями доходности |
| 3 | Тяжёлая медицина (IVF / онкология / пластика / инвазивная) | MEDICAL_HEAVY US/EU/UK |
| 4 | Здоровье и медицина (БАДы / похудение / mental health) | WELLNESS_HEALTH_RESTRICTED (общая) |
| 5 | Targeting и discrimination | Housing / employment / credit (FHA / ADEA / GDPR Art.9) |
| 6 | Юридические услуги для физлиц в кризисе | CRISIS_EXPERT юр / банкротство / развод |
| 7 | Юр.услуги PL/EU-юрисдикция addendum | EU_RUSSIAN_DIASPORA × CRISIS × LEGAL |
| 8 | B2B SaaS — обещания бизнес-результата | B2B_SAAS general |
| 9 | B2B SaaS Enterprise — comparative claims | B2B_SAAS_ENTERPRISE (волна Т.3) |
| 10 | HIGH_TICKET_PRO_SERVICES — confidentiality + regulatory | M&A / LEGAL / private banking (волна Т.6) |
| 11 | SEC RIA / FINRA / FCA financial promotion | Private banking / investment advisory (волна Т.6) |
| 12 | REAL_ESTATE_EXPAT_USA — FHA + FinCEN + EB-5 | US real-estate + foreign-buyer (волна Т.7) |
| 13 | WELLNESS_HEALTH_RESTRICTED_USA — DSHEA + FTC §255 | US supplements + testimonials (волна Т.7) |
| 14 | EU_RUSSIAN_DIASPORA — GDPR Art.9 + sanctions + cross-border | EU diaspora flights (волна Т.8) |
| 15 | Diaspora-cultural messaging — post-2022 political-sensitivity | Все diaspora flights с возвратной лексикой / national-identity (волна Т.8) |

### Дополнительные блоки

- **MINORS_DATA COPPA** — US KIDS_PARENTS
- **MINORS_AI_LIKENESS state-laws** — CA AB-2839 / NY Marsh's Law / TX SB-1361 / IL HB 4762 + EU AI Act art.50 (волна Т.5)
- **FTC §255.5 PARENT-ENDORSER BLOCK** (волна Т.5)
- **AI DISCLOSURE generalization** (P9 → ВСЕ public professional в regulatory registry)

---

## 10 канонических ниш (УРОВЕНЬ 2)

Полная таксономия в `GLOSSARY.md`. Здесь — обзор по risk-profile (post-Т.8):

| # | Профиль | Risk pre-T | Risk post-Т.8 | Есть PRESET |
|---|---|---|---|---|
| 1 | INFOBIZ | 6 | 4 | — (волна Т.1 фиксы в основном тексте) |
| 2 | LOCAL_SERVICE | 5 | 4 | — |
| 3 | ECOM | 5 | 4 | — |
| 4 | B2B_SAAS | 8 | 4 | ✅ B2B_SAAS_ENTERPRISE_PRESET |
| 5 | HIGH_TICKET | 7 | 4 | ✅ HIGH_TICKET_PRO_SERVICES_PRESET |
| 6 | CRISIS_EXPERT | 8 | 4 | ✅ CRISIS-AUDIT-LAYER |
| 7 | REAL_ESTATE_EXPAT | 7 | 4 | ✅ REAL_ESTATE_EXPAT_USA_PRESET |
| 8 | WELLNESS_HEALTH_RESTRICTED | 7 | 4 | ✅ WELLNESS_HEALTH_RESTRICTED_USA_PRESET |
| 9 | KIDS_PARENTS | 7 | 4 | ✅ KIDS_PARENTS_PRESET |
| 10 | ECOM_IMPULSE | 6 | 5 | — (candidate для Т.9) |

**Среднее:** 6.6 → 4.1 (-38%, для 10 канонических). С учётом sub-profile 14 sub: 6.86 → 3.3 (-52%).

---

## 6 sub-profile УРОВЕНЬ 3

| Sub-profile | Поверх | Чем отличается |
|---|---|---|
| `B2B_SAAS_ENTERPRISE` | B2B_SAAS | CTO Fortune 500 / Replacement campaigns / SLA / 300+ USD/seat |
| `HIGH_TICKET_PRO_SERVICES` | HIGH_TICKET | M&A / LEGAL / private banking / family-office (100k-50M+ deals) |
| `EU_RUSSIAN_DIASPORA` | Любая вертикаль | Русскоязычная аудитория в EU/UK/IL post-2022 — sanctions + GDPR Art.9 + cross-border + cultural |
| `REAL_ESTATE_EXPAT_USA` | REAL_ESTATE_EXPAT | US-гео — FHA / FinCEN GTO / FIRPTA / EB-5 |
| `WELLNESS_HEALTH_RESTRICTED_USA` | WELLNESS_HEALTH_RESTRICTED | US-гео — DSHEA / FTC «Gut Check» / state laws |
| `KIDS_PARENTS_EDTECH` (candidate Т.10) | KIDS_PARENTS | EDTECH-specific COPPA + accreditation + state student-data |

---

## 3 бюджетных режима

| Режим | Граница | Особенности |
|---|---|---|
| LITE (МАЛЫЙ) | до 500 USD/мес | Лимит на крео-продакшн, фокус на ручной UGC |
| STANDARD (СРЕДНИЙ) | 500-1500 USD/мес | Базовая структура 1-3-1, Higgsfield Marketing Studio |
| PRO (БОЛЬШОЙ) | 1500+ USD/мес | Cinema Studio Veo 3.1 + полный pack-стек |

---

## Конвейер (10 этапов) ↔ скилы matrix

См. `GLOSSARY.md` секция «Этапы конвейера». Главный документ — `KONVEYER-LOGIKA.md` (загружается отдельно в Claude Project на курсе).

---

## Ключевые архитектурные принципы

1. **Self-contained плагин** — после волны П.20 не зависит от внешних файлов (QUICK-REFERENCE-NICHE-RESTRICTIONS.md inline в CRISIS-AUDIT-LAYER + MEDICAL_HEAVY §16 + WELLNESS_USA_PRESET).
2. **PRESET pattern** — каждый PRESET = единая точка истины для рисковой ниши, с 8-9 правил + финальным чек-листом N/N PASS перед выдачей промта.
3. **Sub-profile накладывается на вертикаль** — EU_RUSSIAN_DIASPORA_PRESET = stricter-rule при конфликте с базовой вертикалью (CRISIS-AUDIT-LAYER / HIGH_TICKET_PRO_SERVICES_PRESET / etc).
4. **Validation cascade V1-V21 + Pre-валидаторы A.1-A.4** — multi-level gate с early-triggers и финальным pre-flight.
5. **Cross-references explicit** — каждый PRESET ссылается на смежные секции / другие PRESET'ы / META категории; нет hidden dependencies.
6. **Naming disambiguation:** §3 prompt-rules R1-R14 (canonical) vs §21 RAT1-RAT8 rationality (волна П.20 rename).
7. **Англицизмы как guardrail** — §13 GUARDRAILS canon (внешний файл) + 33 пар замен + 25 индустриальных терминов разрешены (волна П.16).
