# Стресс-тест полного курса — Волна 2, Student #2

## Клиент: PixelOps (B2B_SAAS_PROFESSIONAL_SERVICES)

**Тип ученика:** middle-таргетолог
**Ниша:** White-label dev agency для русскоязычных стартапов EU
**Бюджет:** $1,800/мес → STANDARD
**Гео:** EU (DE/PL/CZ/PT по вводным; после фильтра К7 → топ-1 PL)
**Pricing:** 7 tiers $500-$25,000/проект
**Сделки:** 30-90 дней
**Buying committee:** CEO + CTO + Procurement (5 ролей по KONVEYER)
**Trial→paid:** 10-25% (но для агентства = BANT-pass rate, не trial)

**Дата теста:** 2026-05-20

---

## Резюме прохождения 7 этапов

| Этап | Скил | Статус | Время | Качество |
|---|---|---|---|---|
| 1. Опросник + Reality-check | client-profile + reality-check-metrics | PASS | ~10 мин эквив. | Сильно. Корректно определён B2B_PROFESSIONAL_SERVICES подпрофиль. Pipeline metrics присутствуют. |
| 1.5. Meta-launch-checklist | meta-launch-checklist | PASS с замечаниями | ~5 мин | Скил отработал, но дефолтные значения требуют профильного switch (см. баги) |
| 2. Ресерч | PROMPT-2 v3 + research-structurer | PASS симулированно | ~15 мин | Корректно определены источники для B2B EU. Слабая выборка по DE/CZ/PT |
| 3. Большой проход (5 блоков) | PROMPT-3 v3.М + schwartz-podhody | PASS | ~25 мин | 3 параллельных сегмента. Запрет Жертвы соблюдён. ROLE-теги работают. |
| 4. Офферы | offer-generator + meta-policy-checker | PASS с WARN | ~15 мин | 48 офферов (10+6 × 3). Pre-flight выявил 3 риск-точки. |
| 5. Креативный бриф | creative-brief-writer | PASS | ~20 мин | 14 блоков. 12 крео. Long-cycle 30/40/30 раскладка. |
| 6. Quality-gate | quality-gate | WARN (3 проблемы) | ~5 мин | 5 substantiation-цифр требуют подтверждения. 8 pre-launch hard-gate пунктов открыты. |
| 7. Аналитика | campaign-diagnoser | PASS | ~10 мин | 3 узла отказа диагностированы. Тест-план составлен с прогнозом. |

**Общий вердикт:** Курс **пригоден** для B2B_SAAS_PROFESSIONAL_SERVICES агентства в EU на middle-уровне. Обнаружено **6 багов разной критичности** + **3 рекомендации улучшения** (см. ниже).

---

## Регрессионная проверка фиксов из ТЗ

### ✅ К1 — middle-mode работает

**Проверка:** На всех 7 этапах ответы были на уровне middle (100-300 слов, термины без скобок, decision-points с trade-offs).

**Сигналы middle, наблюдённые в моих ответах:**
- Не объяснял термины (CPQM, MQL, Champion, BANT, payback) в скобках при первом упоминании
- Не выдавал «одно действие на сегодня + одно на неделю»
- Выдавал полные расчёты с альтернативами (3 сценария TCO / 3 теста крео / 3 варианта решения CPF-блокинга)
- Decision-points оставлял ученику с предупреждением о рисках (например cash-runway warning)
- Использовал длинные ответы только для промптов/брифов

**Что было бы junior-режим:** упрощённый ответ типа «у тебя B2B_SAAS, бюджет STANDARD, начни с PL. Делай 3 крео для FOUNDER сегмента в первую неделю» (50-100 слов, одно действие).

**Вердикт фикса К1:** ✅ работает корректно

### ✅ К7 — STANDARD $1800 + 1 гео EU = правильно

**Проверка:** На вводных 4 страны EU (DE/PL/CZ/PT) + STANDARD-бюджет $1,800:
- Скил `client-profile` корректно применил KONVEYER §126 правило 12 multi-гео
- Расчёт: 4 гео × $450/мес = распыление (ниже статзначимости)
- Предложение: топ-1 PL → после положительной итерации → расширение
- Альтернатива: либо поднять бюджет до PRO ($3,000+), либо клиент берёт риск (фиксируется как «осознанный риск»)

**Вердикт фикса К7:** ✅ работает корректно. Это критичный фикс — junior сделал бы 4 страны одновременно.

### ✅ К8 — EU compliance (GDPR, sanctions) присутствует

**Проверка:** На этапах 1.5 (Meta-launch-checklist), 3 (брифа GAPS), 4 (meta-policy pre-flight) — все упоминания EU compliance корректны:

| Compliance | Где проверено | Корректность |
|---|---|---|
| GDPR Art. 6 + 9 | Этап 1.5 Блок 7, Этап 3 GAPS, Этап 4 meta-policy | ✅ CMP cookie consent обязательно, ethnic-proxy запрет |
| Sanctions OFAC + EU 269/2014 + UK OFSI | Этап 1.5, Этап 3 GAPS | ✅ Hard-exclude RU/BY/IR/KP, billing entity EU only |
| EU AI Act Art. 50 (с авг 2026) | Этап 1.5, Этап 3, Этап 4 | ✅ Transparency overlay для AI-likeness, реальные Loom приоритет |
| EU representative Art. 27 GDPR | Этап 1.5 Блок 7 | ✅ Упомянуто |
| Mitbestimmungsrecht DE | Этап 4 meta-policy | ⚠️ Упомянуто (employee monitoring claim не наш случай, но в roadmap проверять) |
| Cyprus CIP suspended | Этап 3 GAPS, Этап 5 запреты | ✅ Запрещено к упоминанию |

**Вердикт фикса К8:** ✅ работает корректно

### ✅ Pipeline metrics в Reality-check

**Проверка:** На этапе 1 (reality-check-metrics) для B2B_SAAS использовалась:
- ✅ B2B-воронка: MQL → SQL → Demo Booked → Held → Proposal → Closed Won
- ✅ Бенчмарки CR на каждом шаге (KONVEYER §624 + analytics-deep-dive §775)
- ✅ CPL по каждому шагу + payback период
- ✅ Multi-touch attribution (W-shaped / U-shaped) — упомянута как baseline для long-cycle

**Вердикт:** ✅ Pipeline metrics присутствуют в Reality-check корректно

### ⚠️ Trial→paid в чек-листе — частичный PASS с багом

**Проверка:** В analytics-deep-dive SKILL.md §678 для B2B_SAAS прописано «Trial → paid conversion = первая метрика для оптимизации».

**Проблема:** Для **B2B_SAAS_PROFESSIONAL_SERVICES** (агентство-услуги) trial→paid **не применим**. Главная метрика — **BANT-pass rate** + Discovery call → Proposal CR. Скил это не различает.

**Что я сделал как ученик:** На этапе 1 + 7 явно переопределил замену: вместо trial→paid использовал MQL→SQL→Demo→Proposal→Closed Won. Junior бы тупо использовал trial→paid метрику и получил бы кашу.

**Вердикт:** ⚠️ Skill требует доработки (см. Баги).

---

## Найденные баги (6 + 3 рекомендации)

### 🔴 Баг 1 (критический) — analytics-deep-dive: нет switch B2B_SAAS vs B2B_PROFESSIONAL_SERVICES

**Где:** `analytics-deep-dive/SKILL.md` §678 — раздел для профиля B2B_SAAS

**Проблема:**
> «Trial → paid conversion = первая метрика для оптимизации: типичный диапазон 10-25% для SMB и 2-8% для self-serve без demo»

Это применимо ТОЛЬКО к classic SaaS-продукту с trial-flow (Notion / Linear / HubSpot). Для **агентств-услуг** (white-label dev / consulting / marketing agency / outsource teams) trial→paid отсутствует — есть **discovery call → proposal → closed-won**.

**Impact:** junior-таргетолог попытается измерять trial→paid у агентства и получит N/A, паника, потеря времени.

**Fix:** Добавить явный switch в §678:
```
B2B_SAAS (SaaS-продукт с trial): trial→paid 10-25% SMB / 2-8% self-serve без demo
B2B_SAAS_PROFESSIONAL_SERVICES (агентство-услуги): NO trial→paid.
   Главная метрика — BANT-pass rate (50-65%) +
   Discovery call → Proposal CR (40-60%) +
   Proposal → Closed Won (25-40%)
```

### 🔴 Баг 2 (критический) — meta-launch-checklist: рассинхрон с KONVEYER каноном бюджетов

**Где:** `meta-launch-checklist/SKILL.md` Шаг 3 (Структура аккаунта по бюджетному режиму)

**Проблема:**
> «LITE (бюджет <3000 USD/мес)»
> «STANDARD (3000-10000 USD/мес)»
> «PRO (10000+ USD/мес)»

Но KONVEYER §125 канон:
- LITE: до 500 USD
- STANDARD: 500-3000 USD
- PRO: 3000+ USD

**Impact:** Skill даёт ученику STANDARD-структуру (1-2 кампании, 4-6 адсетов) на бюджет $3000+, хотя по KONVEYER этот бюджет уже PRO (2-3 кампании, до 8 адсетов, CBO + Advantage+). Internal inconsistency между скилом и Knowledge base курса.

**Fix:** Переписать Шаг 3 скила в соответствии с каноном KONVEYER §125:
```
- LITE (до 500 USD/мес) - 1 кампания, 3-4 адсета, 3 крео в адсете
- STANDARD (500-3000 USD/мес) - 1-2 кампании, 4-6 адсетов, 3-4 крео
- PRO (3000+ USD/мес) - 2-3 кампании, до 8 адсетов, до 5 крео + Advantage+ Audience
```

### 🟡 Баг 3 — meta-launch-checklist: нет switch attribution window по профилю

**Где:** `meta-launch-checklist/SKILL.md` Блок 4 (iOS 14+)

**Проблема:**
> «Window - 1 day click / 7 day click согласно цели»

Для **B2B_SAAS / HIGH_TICKET / REAL_ESTATE_EXPAT / M&A** с циклом 30-90+ дней **обязателен 28-day click + 1-day view**. На 7-day click большая часть сделок не доезжает (см. KONVEYER §312 analytics для B2B).

**Impact:** junior настроит дефолтный 7-day click → потеряет 50%+ сделок при cycle 30-90 дней → решит что «реклама не работает» → закроет канал.

**Fix:** Добавить switch в Блок 4:
```
Window — по профилю:
- INFOBIZ / ECOM / LOCAL_SERVICE / ECOM_IMPULSE → 7-day click (дефолт)
- B2B_SAAS / B2B_PROFESSIONAL_SERVICES / HIGH_TICKET / REAL_ESTATE_EXPAT / M&A / KIDS_PARENTS годовой → 28-day click + 1-day view
- CRISIS_EXPERT (длинная воронка bcs + cycle) → 28-day click
```

### 🟡 Баг 4 — meta-launch-checklist: нет EU compliance Блока по умолчанию

**Где:** `meta-launch-checklist/SKILL.md` 6 базовых блоков

**Проблема:** Не упомянуты GDPR / CMP / EU representative / EU AI Act / billing entity / sanctions sweep. На этапе работы я (как ученик) вспомнил их из KONVEYER §874-879 + §425, junior забудет.

**Impact:** junior запустит без CMP cookie consent → GDPR-жалоба → штраф €20M по worst case. Запустит с RU/BY billing entity → hard-block Meta, не запустится вообще.

**Fix:** Добавить условный Блок 7 «EU compliance sweep» автоматически активируемый при гео = EU:
```
Блок 7 (только для EU гео).
- [ ] CMP cookie consent на лендинге (Cookiebot/OneTrust/Cookieyes)
- [ ] Privacy Policy на 2 языках (RU + state language)
- [ ] EU representative по Art. 27 GDPR если controller не в EU
- [ ] Billing entity ТОЛЬКО EU/UK/CH/IL (не RU/BY)
- [ ] Hard-exclude targeting RU/BY/IR/KP/Crimea/DPR/LPR
- [ ] EU AI Act Art. 50: transparency overlay для AI-likeness реального эксперта
- [ ] Sanctions sweep по таргетингу (без ethnic-proxy interest)
```

### 🟡 Баг 5 — reality-check-metrics: бенчмарки SWITCH ПО ГЕО для EU B2B не полные

**Где:** `reality-check-metrics/SKILL.md` §187-191 (множители гео)

**Проблема:** Множители даны для общих гео-зон (СНГ × 0.7-1.0, EU × 1.0-1.5, USA × 1.5-2.5). Но для **B2B_SAAS EU** в KONVEYER §384 указаны конкретные CPM-зоны:
- DACH (DE/AT/CH) — Meta CPM B2B 12-20 USD
- UK — 10-18 USD
- PL — 5-10 USD
- NL — 9-15 USD
- Nordics — 11-18 USD
- France — 8-14 USD (требует локальный французский)

Скил не различает страны внутри EU — даёт один множитель × 1.0-1.5. Для PL B2B это занижено в 1.5-2 раза от реалистичного.

**Impact:** Reality-check для PL B2B даёт CPQM по EU-усреднению, а реальный PL B2B дешевле на 30-50%. Меньшая проблема (oversize budget) но юнит-экономика искажена.

**Fix:** Добавить sub-switch по странам внутри EU для B2B_SAAS / HIGH_TICKET профилей:
```
EU CPM множители (для B2B_SAAS / HIGH_TICKET):
- PL — × 0.8-1.0 (CPM $5-10)
- France / Italy / Spain — × 1.0-1.3 (CPM $8-14)
- UK / NL — × 1.2-1.5 (CPM $10-15)
- DACH (DE/AT/CH) — × 1.5-2.0 (CPM $12-20)
- Nordics — × 1.3-1.7 (CPM $11-18)
```

### 🟢 Баг 6 (минорный) — schwartz-podhody: Most-aware дефолтные углы не учитывают B2B specifics

**Где:** `schwartz-podhody/SKILL.md` правило выбора углов для Most-aware

**Проблема:**
> «Most-aware → срочность + соцдоказ + статус + выгода»

Для **B2B_SAAS Most-aware (бывшие пользователи конкурента)** — «срочность» искусственная не работает, «статус» воспринимается как corporate-hype. Что реально работает: **guarantee + speed + risk reversal + соцдоказ**. То есть для B2B Most-aware углы должны быть смещены от «срочность + статус» к «выгода + risk reversal».

**Impact:** Я сделал это вручную в Сегменте 3 SWITCH (вместо «статус» использовал «выгода через гарантии»), но junior пошёл бы по дефолту и сделал бы «статус-style replacement-grade agency для Series A+» — что я сам пометил как corporate, не на языке switcher'а.

**Fix:** Добавить sub-правило для B2B_SAAS Most-aware:
```
Для B2B_SAAS / HIGH_TICKET Most-aware (switchers, replacement-seekers):
- НЕ использовать «срочность» искусственную (читается как hype)
- НЕ использовать «статус» в corporate-tone (читается как marketing-spin)
- Заменить на: соцдоказ (named/anonymous switchers) + risk reversal (guarantees) + speed (KT 7-day) + выгода (TCO)
```

---

## Рекомендации улучшения курса (не баги, а enhancement)

### 💡 Реко 1 — KONVEYER §385+: добавить раздел про offline conversions для long-cycle B2B

KONVEYER хорошо описывает long-cycle 30/40/30 раскладку, но **не упоминает offline conversions API** который критичен для атрибуции closed-won сделок через 30-90 дней обратно к крео. Без offline conversions Meta никогда не свяжет MVP crew #1 с deal закрытым на 60-й день.

**Где добавить:** §400-411 (cash-runway warning) — рядом параграф про техническую необходимость offline conversions webhook из CRM в Meta CAPI с lookback 90 дней.

### 💡 Реко 2 — BRIEFING-PACK: добавить «pre-launch hard-gate» секцию для long-cycle profiles

Сейчас Бриф 3 содержит Раздел 5 (GAPS) и Раздел 6 (Стадии воронки), но не упоминает **отдельный hard-gate чек-лист до запуска** который для long-cycle B2B критичен. На моём Quality-gate я нашёл 8 пунктов hard-gate (substantiation цифр / permission to disclose / Calendly URL / TCO Calculator URL / лендинг substantiation pages / CMP / billing entity / CRM выбор). Без этого чек-листа junior забудет и запустит со сломанной инфраструктурой.

**Где добавить:** В Бриф 3 — новый Раздел 7 «Pre-launch hard-gate (для long-cycle профилей)» с 8-10 чекбоксами обязательных к закрытию ДО запуска кампаний.

### 💡 Реко 3 — INSTRUCTIONS-готово-к-копированию.txt: добавить force-trigger на B2B_SAAS = autocall analytics-deep-dive с long-cycle модулем

Сейчас INSTRUCTIONS force-trigger вызывает скилы по триггерам, но для B2B_SAAS не упоминает явно вызов `analytics-deep-dive` с long-cycle модулем (cohort + pipeline value + multi-touch + payback). На моём этапе 7 я (как ученик) сам определил что нужен этот скил, но в текущей версии INSTRUCTIONS триггер только «при жалобе на плохую кампанию → campaign-diagnoser». Для B2B_SAAS планомерная аналитика на 14/28/42-й день должна быть встроена явно.

**Где добавить:** В INSTRUCTIONS §477+ FORCE-TRIGGER раздел:
```
— При работе с B2B_SAAS / HIGH_TICKET / REAL_ESTATE_EXPAT профилем на этапе 7 (аналитика) — ОБЯЗАТЕЛЬНО:
  1. analytics-deep-dive с pipeline-value-фокусом (не CPL focus)
  2. Cohort анализ MQL→SQL→Demo→Proposal с CR на каждом шаге
  3. Multi-touch attribution W-shaped / U-shaped baseline
  4. Reality-check метрик на 28-й + 56-й день (long-cycle двойной check)
```

---

## Что хорошо работало

**Сильные стороны курса на B2B_SAAS_PROFESSIONAL_SERVICES:**

1. **client-profile корректно угадал подпрофиль B2B_PROFESSIONAL_SERVICES** — KONVEYER §115 определение для law firms / consulting / wealth management применилось к dev agency без проблем.

2. **reality-check-metrics для B2B_SAAS использовал CPT/CPQM/payback** — не пытался натянуть CPL × CR формулу. Switch ПО ПРОФИЛЮ работает.

3. **schwartz-podhody корректно различил Solution-aware-light vs Solution-aware-deep** — это был ключевой нюанс для B2B где разница между «founder ищет первый шаг» и «CTO активно сравнивает решения» определяет всю стратегию лид-магнитов.

4. **PROMPT-3 v3.М блок D.0 (суб-боли / измеримые желания)** — для B2B это работает блестяще, конкретные инструменты (TCO Calculator / Champion-pack / KT-playbook) ложатся в эту структуру без боли.

5. **Long-cycle перебивка 30/40/30** — корректно применилась для long-cycle B2B (30 acq / 40 nurture / 30 retarget вместо классической 50/30/20). Это критично для B2B где nurture-этап доминирует.

6. **meta-policy-checker на pre-flight для офферов (фикс К2)** — поймал 3 риск-точки (EU AI Act / financial-claim risk / guarantee substantiation) до запуска. Это saved real campaign.

7. **quality-gate жёстко прокатил 5 substantiation-цифр** — поймал hallucinated metrics («12 MVP», «$500K seed», «3 switchers») и потребовал подтверждения. Без этого ученик запустил бы кампании с цифрами не подтверждёнными клиентом → риск иска / Meta-restriction.

8. **EU_RUSSIAN_DIASPORA cross-cutting overlay** — корректно активировался, привнёс GDPR Art. 9 ethnic-proxy запреты, Cyprus CIP запрет, валютные правила, языковые токсичности.

---

## Что вызвало трения (требует внимания)

1. **Бриф 3 в табличном формате очень длинный** для PM PixelOps впервые работающего с brief'ами курса. В реальной практике PM может застрять на Разделе 3 (Карта крео-заходов) — нужен facilitated walkthrough.

2. **Распределение spend по сегментам** — Advantage+ Audience ON в Acquisition broad даёт перекос в сторону cheap-CPL сегментов (FOUNDER_MVP) хотя более ценный pipeline у CTO_SCALE. Нужно либо инструкция «начать с manual budget split», либо явный warning «через 7 дней пересмотри split по pipeline value, не по cost».

3. **TCO Calculator как lead-magnet — высокая acquisition, низкая BANT-pass rate** — это типичная B2B-проблема где «curious browsers» fillup ваши leads без intent. Нужно warning в offer-generator + creative-brief-writer о «calculator-trap» и предложение перенести calculator из top-of-funnel в nurture-stage.

---

## Финальный вердикт стресс-теста

**Курс прошёл стресс-тест на B2B_SAAS_PROFESSIONAL_SERVICES EU/PL** с условиями:

- ✅ Все 7 этапов проходимы
- ✅ Все 5 проверяемых фиксов (К1, К7, К8, Pipeline metrics, Trial→paid) работают **с оговорками**
- ⚠️ 6 багов обнаружено (2 критических, 3 средних, 1 минорный)
- ⚠️ 3 рекомендации улучшения (offline conversions, pre-launch hard-gate, force-trigger для B2B аналитики)

**Главный учебный вывод:** Курс **разрабатывался с фокусом на INFOBIZ / ECOM / LOCAL_SERVICE** (это видно по дефолтам скилов). **Под B2B_SAAS_PROFESSIONAL_SERVICES агентства работает, но требует ручной адаптации в нескольких точках** — middle-таргетолог справится, **junior может потерять качество** без багфиксов 1-4.

**Приоритетные фиксы к доработке:**
1. 🔴 analytics-deep-dive: switch B2B_SAAS vs B2B_PROFESSIONAL_SERVICES (Баг 1)
2. 🔴 meta-launch-checklist: каноничные бюджетные диапазоны (Баг 2)
3. 🟡 meta-launch-checklist: attribution window switch по профилю (Баг 3)
4. 🟡 meta-launch-checklist: автоматический EU compliance Блок 7 (Баг 4)

После этих 4 фиксов курс будет работать на B2B_SAAS_PROFESSIONAL_SERVICES агентства EU **без ручных доработок** для middle и **с меньшим риском провала** для junior.
