# GLOSSARY — словарь плагина ai-ops-7143

Единый словарь имён, на который ссылаются все скилы. Если в скиле встречаешь имя из левой колонки — оно значит то же, что в правой.

Версия плагина — 1.2.2. Проверить свою: `/plugin list`.

## Профили ниши — 10 канонических (УРОВЕНЬ 2)

Канонический список — **10 профилей**. Русское имя и англ. код — одна сущность. Точка истины по списку: `skills/client-profile/SKILL.md`.

| # | Русское | Англ. код | Кратко |
|---|---|---|---|
| 1 | ИНФОБИЗ | `INFOBIZ` | онлайн-курсы, школы, наставничество, инфопродукты |
| 2 | ЛОКАЛЬНЫЙ-СЕРВИС | `LOCAL_SERVICE` | стома, бьюти, барбер, ремонт, фитнес-студии |
| 3 | ИНТЕРНЕТ-МАГАЗИН | `ECOM` | одежда, косметика, гаджеты, товарка с каталогом |
| 4 | B2B-СЕРВИС | `B2B_SAAS` | SaaS, агентства, корпоративный консалтинг |
| 5 | ПРЕМИУМ | `HIGH_TICKET` | премиум-наставничество, luxury-услуги, медтуризм, светский премиум-туризм |
| 6 | КРИЗИС-ЭКСПЕРТ | `CRISIS_EXPERT` | юристы в кризисе (банкротство, развод, уголовка), ритуальные услуги, врачи острых состояний, addiction-эксперты |
| 7 | НЕДВИЖИМОСТЬ-EXPAT | `REAL_ESTATE_EXPAT` | Golden Visa / D7 / Beckham / EB-5 / зарубежная недвижимость для релокантов |
| 8 | WELLNESS-ОГРАНИЧЕННЫЙ | `WELLNESS_HEALTH_RESTRICTED` | БАДы, hormonal coaching, supplements, sleep aids, ED, weight-loss |
| 9 | ДЕТСКИЕ-РОДИТЕЛИ | `KIDS_PARENTS` | детские школы, развивашки, детский спорт / медицина / лагеря, parent-targeting |
| 10 | ИМПУЛЬС-ECOM | `ECOM_IMPULSE` | WOW-товары через Reels / TikTok-style, retention=0, единичная покупка |

## Sub-profile УРОВЕНЬ 3 (накладываются на канонический профиль)

7 sub-profile с дедикейтед PRESET'ом в `higgsfield-prompt-generator`.

| Имя | Поверх | Чем специфичен |
|---|---|---|
| `B2B_SAAS_ENTERPRISE` | `B2B_SAAS` | CTO/CISO Fortune 500 target, чек ≥300 USD/seat OR deal-size ≥50k USD/год, Replacement / Datadog-killer / 99.X% SLA campaigns |
| `B2B_SAAS_SMB` | `B2B_SAAS` | малый и средний бизнес, короткий цикл сделки, решение принимает сам собственник или один руководитель |
| `HIGH_TICKET_PRO_SERVICES` | `HIGH_TICKET` | M&A / corporate LEGAL / private banking / family-office advisory, deal-size 100k-50M+ USD, HNWI / UHNWI / GC аудитория |
| `EU_RUSSIAN_DIASPORA` | Любая вертикаль | Русскоязычная аудитория в EU (DE/PL/CZ/AT/CY/IT/ES/NL/FR/SE/FI) / UK / IL post-2022 — sub-profile, накладывается stricter-rule при конфликте |
| `REAL_ESTATE_EXPAT_USA` | `REAL_ESTATE_EXPAT` | US-гео — FHA §3604(c) + Meta Housing SAC + FinCEN GTO + FIRPTA + EB-5 SEC+USCIS + RESPA §8 |
| `WELLNESS_HEALTH_RESTRICTED_USA` | `WELLNESS_HEALTH_RESTRICTED` | US-гео — DSHEA §403r-6 + FTC «Gut Check» 7 false weight-loss + FDA disclaimer + state laws (CA Prop 65 / NY AG / TX DTPA) |
| `KIDS_PARENTS_EDTECH` | `KIDS_PARENTS` | EDTECH-specific — COPPA combined-identifier + accreditation substantiation + state student-data laws. Свой PRESET есть: 9 проверок дополнительно к 8 проверкам базового `KIDS_PARENTS_PRESET` |

## Бюджетные режимы

| Канон (имя режима) | Русский синоним | Граница |
|---|---|---|
| `LITE` | МАЛЫЙ | до 500 USD/мес |
| `STANDARD` | СРЕДНИЙ | 500-3000 USD/мес |
| `PRO` | БОЛЬШОЙ | 3000+ USD/мес |

Канонические имена режимов — `LITE` / `STANDARD` / `PRO` (их используют все скилы плагина). Русские МАЛЫЙ / СРЕДНИЙ / БОЛЬШОЙ — допустимые синонимы для общения с учеником. Точка истины: `skills/client-profile/SKILL.md`.

## Удалённые / переименованные / реструктурированные профили

| Старое имя | Новое имя | Причина |
|---|---|---|
| `SOFT_EXPERT` (старая зонтик-категория) | разнесён на `CRISIS_EXPERT` (как канонический) + `WELLNESS_HEALTH_RESTRICTED` (нутрициологи / БАДы) + `MEDICAL_HEAVY` (врачи) | Слишком широкий зонтик, разные риск-профили |
| `REAL_ESTATE` (без `_EXPAT`) | `REAL_ESTATE_EXPAT` (канонический) — domestic real-estate отдельно (не покрыт PRESET'ом) | Главный pain-point именно expat-сегмент |
| `FINTECH` | не используется как канонический — лицензированный финтех в `meta-policy-checker`, категория 2 | Слишком узкая ниша, нет в 10 канонических |
| `SUBSCRIPTION_BOX` | не используется как канонический — recurring revenue логика в `ECOM` + `WELLNESS_HEALTH_RESTRICTED_USA_PRESET` ПРАВИЛО 9 (Click-to-Cancel) | — |
| `MEDICAL_HEAVY` | используется как **дополнительный профиль** (не канонический; правила лежат внутри профильных пресетов §10 в `higgsfield-prompt-generator`) | Сохранено для США/EU — IVF / онкология / пластика / инвазивная косметология |
| `RELIGIOUS_TRAVEL` | используется как **дополнительный профиль** (паломнические туры) | Сохранено |

## Файлы-артефакты

Имена одинаковы во всех скилах. Работаешь без файлов — используй свою таблицу с тем же содержанием.

| Файл | Что внутри | Где создаётся |
|---|---|---|
| `00-profile.md` | профиль клиента, бюджетный режим, вводные, реальность-чек | `client-profile`, `reality-check-metrics` |
| `01-research-raw.md` | сырьё ресерча: цитаты аудитории с источниками | ручной сбор + `research-structurer` |
| `02-segments-map.md` | сегменты и карта смыслов | `research-structurer` |
| `03-offers.md` | офферы, прошедшие проверку | `ru-marketer`, `offer-generator`, `quality-gate` |
| `04-creatives.md` | подходы, гипотезы крео, тексты и промты | `schwartz-podhody`, `creative-brief-writer`, `ru-copywriter`, `higgsfield-prompt-generator`, `text-humanizer`, `meta-policy-checker` |
| `05-analytics.md` | аналитика итерации и решения KILL/HOLD/SCALE | `campaign-diagnoser`, `weekly-report-writer` |
| `PROJECT-MEMORY.md` | память по клиенту между итерациями | `memory-updater` |

## Порядок работы

Этапы называются по делу, а не по номерам: разбор клиента и экономики → сбор сырья → сегменты и карта смыслов → офферы → подходы → производство крео → запуск → аналитика → решения и следующая итерация.

Номеров у этапов нет намеренно: раньше нумерация этапов, нумерация листов и нумерация промтов расходились между собой, и ученик подставлял не тот файл. Названия расходиться не могут.

Запуск ведёт `meta-launch-checklist`, передачу проекта — `client-comms`, масштабирование победителя — `winner-variations`.

## Структуры кампаний (нейминг)

- **1-1-1** — одна кампания / один адсет / один креатив. Минимальная структура для теста одной гипотезы.
- **1-3-1** — одна кампания / три адсета / по одному креативу в каждом. Тест трёх аудиторий или трёх сегментов на одном крео.
- **1-1-3** — одна кампания / один адсет / три креатива. Тест трёх крео на одной аудитории.
- **N-M-K** — в общем виде. В команде / клиенте договаривайтесь заранее, какой смысл вкладываете в цифры, иначе путаница.

## Формулы и метрики

- **Предельный CAC** = Средний чек × Маржа%. Максимум, что можно потратить на привлечение клиента.
- **Предельный CPL** = (Чек × Маржа × CR лид→продажа) / Целевой ROAS.
- **Предельная цена шага воронки** = предельная цена клиента × произведение CR всех ступеней между этим шагом и покупкой (обратный пересчёт от продажи к верху воронки). Разобранный пример — в `reality-check-metrics`. Считать «до этого шага» — распространённая ошибка: она завышает потолки цен в разы.
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
| V22 | Length-gate — лимит длины промта под поле генератора |
| A.1 | Absolute promise («гарантия» / «100%») early-trigger |
| A.2 | Real brand mention check |
| A.3 | BIOCLAIM early-trigger (биография с числом) |
| A.4 | Non-USD currency conversion |
| H1-H10 | Humanization приёмы (wisp / cadence / lived-in / not-actor / handheld / wrinkled / ambient / eye-contact / lived-life / used-props) |
| RAT1-RAT8 | Rationality проверки (beat logic / continuity / attention progression / mental model / stake / cohesion / why-now / what-if-miss). Именно RAT, а не R: `R1-R14` в том же скиле — это другое, правила промта в §3. |
| A1-A8 | Anti-patterns (AI-actor look / Stock environment / Театральная подача / Декоративные шоты / Привлекательный закат / 3 шот без motivation / Hook+Reveal+Resonance в одном шоте / Локация-телепорт без prop continuity) |

## PRESET'ы в `higgsfield-prompt-generator` — 9, плюс 2 слоя правил

Полные правила каждого — внутри самого скила, в `REFERENCE.md`.

| PRESET | Активируется когда | Финальный чек-лист |
|---|---|---|
| `B2B_SAAS_ENTERPRISE_PRESET` | B2B_SAAS + Enterprise триггеры | 8/8 PASS |
| `B2B_SAAS_SMB_PRESET` | B2B_SAAS + малый и средний бизнес | 8/8 PASS |
| `KIDS_PARENTS_PRESET` | KIDS_PARENTS + детский / family-content | 8/8 PASS |
| `KIDS_PARENTS_EDTECH_PRESET` | KIDS_PARENTS + EDTECH (языки, STEM, программирование) | 9/9 PASS дополнительно к 8/8 базового |
| `HIGH_TICKET_PRO_SERVICES_PRESET` | M&A / LEGAL / private banking | 9/9 PASS |
| `REAL_ESTATE_EXPAT_USA_PRESET` | REAL_ESTATE + US-гео | 8/8 PASS |
| `WELLNESS_HEALTH_RESTRICTED_USA_PRESET` | WELLNESS + US-гео | 9/9 PASS |
| `EU_RUSSIAN_DIASPORA_PRESET` | Любая вертикаль + русскоязычная диаспора EU/UK/IL | 8/8 PASS |
| `ECOM_IMPULSE_USA_PRESET` | ECOM_IMPULSE + US-гео | 9/9 PASS |

Слои правил поверх базового профиля (не PRESET'ы, применяются вместе с ними):

| Слой | Когда | Чек-лист |
|---|---|---|
| `CRISIS-AUDIT-LAYER` | CRISIS_EXPERT — банкротство, развод, уголовная защита, addiction, ритуальные услуги | 8/8 PASS |
| `LOCAL_SERVICE_LOCAL_SEO_GBP_LAYER` | LOCAL_SERVICE с локальным поиском и карточкой на картах | 7/7 PASS |

Отдельного PRESET'а под `REAL_ESTATE_EXPAT_EU` нет — для EU-гео работает базовый профиль плюс `EU_RUSSIAN_DIASPORA_PRESET`, если аудитория русскоязычная.

## Категории риска в `meta-policy-checker`

**10 пронумерованных категорий** (1-10) — базовый список: запрещённый контент, финансовые продукты, тяжёлая медицина, wellness и БАДы, таргетинг и дискриминация, юруслуги в кризисе, юруслуги PL/EU, B2B SaaS, B2B SaaS Enterprise, HIGH_TICKET профессиональные услуги.

**17 именованных категорий** без номера — нишевые расширения: SEC/RIA/FINRA/FCA, REAL_ESTATE_EXPAT USA и EU, WELLNESS_HEALTH_RESTRICTED USA, EU_RUSSIAN_DIASPORA, культурные сообщения на диаспору, ECOM_IMPULSE USA, KIDS_PARENTS EDTECH, B2B_SAAS_SMB, LOCAL_SERVICE локальный поиск и другие.

Плюс сквозные блоки: данные несовершеннолетних (COPPA), использование внешности несовершеннолетних, требования к отзывам родителей, раскрытие ИИ-контента для публичных профессий из регулируемых реестров.

Точный состав и формулировки — в самом скиле. Здесь только карта, чтобы понимать, что искать.
