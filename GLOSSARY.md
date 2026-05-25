# GLOSSARY — словарь плагина ai-ops-7143

Единый словарь имён, на который ссылаются все скилы. Если в скиле встречаешь имя из левой колонки — оно значит то же, что в правой.

Обновлён 2026-05-19 post-Т.8 (актуальная таксономия с учётом 16 волн доработок).

## Профили ниши — 10 канонических (УРОВЕНЬ 2)

Канонический список — **10 профилей** (не 8, не 11 — точно 10 после волны П.14). Русское имя и англ. код — одна сущность.

| # | Русское | Англ. код | Кратко | Risk-profile post-Т.8 |
|---|---|---|---|---|
| 1 | ИНФОБИЗ | `INFOBIZ` | онлайн-курсы, школы, наставничество, инфопродукты | 4 |
| 2 | ЛОКАЛЬНЫЙ-СЕРВИС | `LOCAL_SERVICE` | стома, бьюти, барбер, ремонт, фитнес-студии | 4 |
| 3 | ИНТЕРНЕТ-МАГАЗИН | `ECOM` | одежда, косметика, гаджеты, товарка с каталогом | 4 |
| 4 | B2B-СЕРВИС | `B2B_SAAS` | SaaS, агентства, корпоративный консалтинг | 4 |
| 5 | ПРЕМИУМ | `HIGH_TICKET` | премиум-наставничество, luxury-услуги, медтуризм, светский премиум-туризм | 4 |
| 6 | КРИЗИС-ЭКСПЕРТ | `CRISIS_EXPERT` | юристы в кризисе (банкротство, развод, уголовка), ритуальные услуги, врачи острых состояний, addiction-эксперты | 4 |
| 7 | НЕДВИЖИМОСТЬ-EXPAT | `REAL_ESTATE_EXPAT` | Golden Visa / D7 / Beckham / EB-5 / зарубежная недвижимость для релокантов | 4 |
| 8 | WELLNESS-ОГРАНИЧЕННЫЙ | `WELLNESS_HEALTH_RESTRICTED` | БАДы, hormonal coaching, supplements, sleep aids, ED, weight-loss | 4 |
| 9 | ДЕТСКИЕ-РОДИТЕЛИ | `KIDS_PARENTS` | детские школы, развивашки, детский спорт / медицина / лагеря, parent-targeting | 4 |
| 10 | ИМПУЛЬС-ECOM | `ECOM_IMPULSE` | WOW-товары через Reels / TikTok-style, retention=0, единичная покупка | 5 |

**Среднее risk-profile:** 4.1 (-38% от pre-T baseline 6.6).

## Sub-profile УРОВЕНЬ 3 (накладываются на канонический профиль)

6 sub-profile с дедикейтед PRESET'ом в `higgsfield-prompt-generator`.

| Имя | Поверх | Чем специфичен |
|---|---|---|
| `B2B_SAAS_ENTERPRISE` | `B2B_SAAS` | CTO/CISO Fortune 500 target, чек ≥300 USD/seat OR deal-size ≥50k USD/год, Replacement / Datadog-killer / 99.X% SLA campaigns |
| `HIGH_TICKET_PRO_SERVICES` | `HIGH_TICKET` | M&A / corporate LEGAL / private banking / family-office advisory, deal-size 100k-50M+ USD, HNWI / UHNWI / GC аудитория |
| `EU_RUSSIAN_DIASPORA` | Любая вертикаль | Русскоязычная аудитория в EU (DE/PL/CZ/AT/CY/IT/ES/NL/FR/SE/FI) / UK / IL post-2022 — sub-profile, накладывается stricter-rule при конфликте |
| `REAL_ESTATE_EXPAT_USA` | `REAL_ESTATE_EXPAT` | US-гео — FHA §3604(c) + Meta Housing SAC + FinCEN GTO + FIRPTA + EB-5 SEC+USCIS + RESPA §8 |
| `WELLNESS_HEALTH_RESTRICTED_USA` | `WELLNESS_HEALTH_RESTRICTED` | US-гео — DSHEA §403r-6 + FTC «Gut Check» 7 false weight-loss + FDA disclaimer + state laws (CA Prop 65 / NY AG / TX DTPA) |
| `KIDS_PARENTS_EDTECH` (candidate Т.10, ещё не PRESET) | `KIDS_PARENTS` | EDTECH-specific — COPPA combined-identifier + accreditation substantiation + state student-data laws |

## Бюджетные режимы

| Имя | Старое имя (deprecated) | Граница |
|---|---|---|
| МАЛЫЙ | `LITE` | до 500 USD/мес |
| СРЕДНИЙ | `STANDARD` | 500-3000 USD/мес |
| БОЛЬШОЙ | `PRO` | 3000+ USD/мес |

Старые имена `LITE` / `STANDARD` / `PRO` в новом коде не использовать. Точка истины: `skills/client-profile/SKILL.md`.

## Удалённые / переименованные / реструктурированные профили

| Старое имя | Новое имя | Причина |
|---|---|---|
| `SOFT_EXPERT` (старая зонтик-категория) | разнесён на `CRISIS_EXPERT` (как канонический) + `WELLNESS_HEALTH_RESTRICTED` (нутрициологи / БАДы) + `MEDICAL_HEAVY` (врачи) | Волна П.14 — слишком широкий зонтик, разные риск-профили |
| `REAL_ESTATE` (без `_EXPAT`) | `REAL_ESTATE_EXPAT` (канонический) — domestic real-estate отдельно (не покрыт PRESET'ом) | Волна П.14 — главный pain-point именно expat-сегмент |
| `FINTECH` | не используется как канонический — лицензированный финтех в `meta-policy-checker` категория 2 | Волна П.14 — слишком узкая ниша, нет в 10 канонических |
| `SUBSCRIPTION_BOX` | не используется как канонический — recurring revenue логика в `ECOM` + `WELLNESS_HEALTH_RESTRICTED_USA_PRESET` ПРАВИЛО 9 (Click-to-Cancel) | Волна П.14 |
| `MEDICAL_HEAVY` | используется как **дополнительный профиль** (не канонический, но имеет дедикейтед §16 правила в `higgsfield-prompt-generator`) | Сохранено для США/EU — IVF / онкология / пластика / инвазивная косметология |
| `RELIGIOUS_TRAVEL` | используется как **дополнительный профиль** (паломнические туры) | Сохранено |

## Артефакты конвейера (Листы)

| Имя в скиле | Имя в конвейере | Где создаётся |
|---|---|---|
| Профиль + Режим | Лист 1 | `client-profile` |
| Цитаты ЦА | Лист 2 | ручной сбор / `research-structurer` |
| Сегментация (ABCDX, Customer Avatar) | Лист 3 | `research-structurer` |
| Table of Meanings / Карта смыслов | Лист 4 | `research-structurer` |
| Офферы (с пометкой пройденных светофор) | Лист 5 | ручной / `ru-marketer` |
| Матрица 4 подходов | Лист 6 | `schwartz-podhody` |
| 12 гипотез крео | Лист 7 | `creative-brief-writer` + `higgsfield-prompt-generator` |
| Календарь и бюджет | Лист 8 | ручной |
| Аналитика недели/итерации | Лист 9 | ручной + `weekly-report-writer` |
| Итог итерации (KILL/HOLD/SCALE) | Лист 10 | ручной + `memory-updater` |

Для учеников без курсовой структуры — «Лист N» = любая таблица того же содержания. См. `client-comms`.

## Этапы конвейера

| Этап | Что | Главные скилы |
|---|---|---|
| 1 | Профиль + Режим + Реальность-чек | `client-profile`, `reality-check-metrics` |
| 2 | Сбор цитат | `ru-marketer` |
| 3 | Сегментация | `research-structurer` |
| 4 | Карта смыслов | `research-structurer` |
| 5 | Офферы + светофор | `ru-marketer`, `quality-gate` |
| 6 | Матрица 4 подходов | `schwartz-podhody` |
| 7 | Производство крео | `creative-brief-writer`, `ru-copywriter`, `style-guide-extractor`, **`higgsfield-prompt-generator`** (для AI-видео), `meta-policy-checker` (gate), `text-humanizer` |
| 8 | Запуск | `meta-launch-checklist` |
| 9 | Аналитика | `campaign-diagnoser`, `weekly-report-writer` |
| 10 | Итерация | `memory-updater`, `client-comms` |

## Структуры кампаний (нейминг)

- **1-1-1** — одна кампания / один адсет / один креатив. Минимальная структура для теста одной гипотезы.
- **1-3-1** — одна кампания / три адсета / по одному креативу в каждом. Тест трёх аудиторий или трёх сегментов на одном крео.
- **1-1-3** — одна кампания / один адсет / три креатива. Тест трёх крео на одной аудитории.
- **N-M-K** — в общем виде. В команде / клиенте договаривайтесь заранее, какой смысл вкладываете в цифры, иначе путаница.

## Формулы и метрики

- **Предельный CAC** = Средний чек × Маржа%. Максимум, что можно потратить на привлечение клиента.
- **Предельный CPL** = (Чек × Маржа × CR лид→продажа) / Целевой ROAS.
- **Предельная цена шага воронки** = Предельная цена клиента × произведение CR ступеней до этого шага. Подробная таблица — в `reality-check-metrics`.
- **LTV подписки (для recurring revenue, e.g. WELLNESS_HEALTH_RESTRICTED_USA subscription)** = `LTV_N мес = чек × Σ(1-churn)^k для k=0..N-1`. Сумма выплат когорты по убывающей за N месяцев. Worked example в `reality-check-metrics`.
- **Допустимый CAC для подписки** = `LTV × маржа × (1 - safety margin)`. Safety margin 20% по умолчанию. Считать по LTV_6мес, не по чеку tripwire.
- **Средневзвешенный LTV для серии (MEDICAL_HEAVY)** = `LTV = чек_прог1 + P(прог2) × чек_прог2 + P(прог3) × чек_прог3 + P(сопут) × чек_сопут`. Маржа в медицине 25-40% после операционки, не 70% как в инфобизе.
- **CAC payback (B2B SaaS)** = `CAC / (месячный чек × маржа на подписку)`. Норма для SMB 6-12 мес, для mid-market 12-18 мес, для **B2B_SAAS_ENTERPRISE** 18-24 мес. Дольше — сигнал что CAC завышен или чек занижен.
- **ERR (Engagement Rate by Reach)** = (лайки + сохранения + комменты + репосты) / охват × 100%.
- **LTV** — суммарный доход с одного клиента за весь период (включая повторные покупки и подписки).
- **ROAS** = Выручка / Расход на рекламу. **ROMI** = (Выручка − Расход) / Расход × 100%. Считаем когортно по месяцам, не по дням.
- **CPM (cost per mille)** — стоимость 1000 показов. Высокий CPM не означает плохую кампанию (см. `campaign-diagnoser` про две стратегии FB).

## Принцип CTR

CTR — производная метрика, не критерий KILL/SCALE. Решение по деньгам: cost per result + ROAS. Низкий CTR ≠ плохой крео — FB может намеренно крутить дорогому ядру ЦА. Старые «CTR 1-3% норма» — устарели.

## Validation rules (внутри `higgsfield-prompt-generator`)

| ID | Что проверяет |
|---|---|
| V1-V16 | Базовые pre-launch проверки (workspace / pack / format / Soul ID / hook / dialogue / etc) |
| V17 | Hook против Жертвы (нет «жертвенного» framing в первые 1.5s) |
| V18 | Anchor pricing / substantiation цифр |
| V19 / V19-BIOCLAIM | Persona claims + biographical claim substantiation |
| V20 | Offer ↔ story coherence |
| V21 | Humanization (H1-H10) + Rationality (RAT1-RAT8) финальный pre-flight |
| A.1 | Absolute promise («гарантия» / «100%») early-trigger |
| A.2 | Real brand mention check |
| A.3 | BIOCLAIM early-trigger (биография с числом) |
| A.4 | Non-USD currency conversion |
| H1-H10 | Humanization приёмы (wisp / cadence / lived-in / not-actor / handheld / wrinkled / ambient / eye-contact / lived-life / used-props) |
| RAT1-RAT8 | Rationality проверки (beat logic / continuity / attention progression / mental model / stake / cohesion / why-now / what-if-miss). **Переименовано из R1-R8 в волне П.20** для disambiguation от §3 prompt-rules R1-R14. |
| A1-A8 | Anti-patterns (AI-actor look / Stock environment / Театральная подача / Декоративные шоты / Привлекательный закат / 3 шот без motivation / Hook+Reveal+Resonance в одном шоте / Локация-телепорт без prop continuity) |

## PRESET'ы sub-vertical (в `higgsfield-prompt-generator`) — 10, полный список в `ARCHITECTURE.md`

| PRESET | Активируется когда | Финальный чек-лист |
|---|---|---|
| `B2B_SAAS_ENTERPRISE_PRESET` | B2B_SAAS + Enterprise триггеры | 8/8 PASS |
| `CRISIS-AUDIT-LAYER` | CRISIS_EXPERT (юр / банкротство / addiction) | C1-C8 PASS |
| `KIDS_PARENTS_PRESET` | KIDS_PARENTS + детский / family-content | 8/8 PASS |
| `HIGH_TICKET_PRO_SERVICES_PRESET` | M&A / LEGAL / private banking | 9/9 PASS |
| `REAL_ESTATE_EXPAT_USA_PRESET` | REAL_ESTATE + US-гео | 8/8 PASS |
| `WELLNESS_HEALTH_RESTRICTED_USA_PRESET` | WELLNESS + US-гео | 9/9 PASS |
| `EU_RUSSIAN_DIASPORA_PRESET` (sub-profile) | Любая вертикаль + русскоязычная диаспора EU/UK/IL | 8/8 PASS |

## 13 категорий в `meta-policy-checker`

Полный список в `ARCHITECTURE.md`. Кратко:

1-9 — базовые (запрещённый контент / FINTECH / MEDICAL_HEAVY / WELLNESS / targeting+discrimination / CRISIS LEGAL / CRISIS PL-EU / B2B SaaS / B2B Enterprise).
10-13 — добавлены в волнах Т.6-Т.7 (HIGH_TICKET_PRO_SERVICES / SEC RIA FINRA FCA / REAL_ESTATE_EXPAT_USA / WELLNESS_HEALTH_RESTRICTED_USA).
14-15 — добавлены в волне Т.8 (EU_RUSSIAN_DIASPORA + Diaspora-cultural messaging).

Плюс **MINORS_DATA COPPA** + **MINORS_AI_LIKENESS state-laws** (Т.5) + **FTC §255.5 PARENT-ENDORSER BLOCK** (Т.5) + **AI DISCLOSURE generalization** (П.9 → ВСЕ public professional в regulatory registry).
