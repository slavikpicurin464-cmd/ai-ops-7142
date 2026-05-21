# ai-ops-7142

Набор из **25 скилов** для перформанс-таргетолога CIS-except-RU + EU + USA. Срабатывают в Claude автоматически по русским / английским фразам — не нужно ничего вызывать руками. Помогают пройти весь маршрут с клиентом — разобрать нишу, собрать ресерч, придумать офферы, написать крео, **сгенерировать промпт под видео в Higgsfield**, проверить кабинет перед запуском, продиагностировать стату, написать отчёт.

Это плагин для учеников курса «AI-операционка таргетолога».

## Установка

В Cowork (десктоп-приложение Claude) или Claude Code (терминал) — две команды по очереди.

```
/plugin marketplace add OWNER/ai-ops-7142
```

```
/plugin install ai-ops-7142@ai-ops-7142
```

`OWNER` — замени на имя владельца репозитория на GitHub (то что стоит до `/ai-ops-7142` в адресе репо).

Подробная инструкция со скринами шагов — в файле [INSTALL.md](./INSTALL.md).

## Что внутри

25 скилов разбиты по этапам работы таргетолога с клиентом — от первой встречи до отчёта по итогам месяца.

### Подготовка проекта (этапы 1-4)

| Скил | Что делает |
|---|---|
| `client-profile` | Определяет клиента за один проход — 10 канонических ниш + 6 sub-profile УРОВЕНЬ 3 + бюджетный режим |
| `brand-extractor` | Разбирает сайт, инст и крео клиента, собирает brand kit |
| `style-guide-extractor` | Из 3-10 референсов вытаскивает текстовое описание визуального стиля |
| `research-structurer` | Берёт сырьё (транскрипт, отзывы, чат) и раскладывает по таблице — сегменты, боли, цитаты, jobs |
| `ru-marketer` | Перформанс-маркетолог в чате — сегментация, ресерч, стратегия, разбор ниши |

### Стратегия и креативная разработка (этапы 5-7)

| Скил | Что делает |
|---|---|
| `schwartz-podhody` | Под каждый сегмент собирает 4 рекламных подхода исходя из уровня осознанности по Шварцу |
| `offer-generator` | Генерация офферов для Чата 4 / PROMPT-5 — дерево офферов под продукт по сегментам и ресерчу |
| `reality-check-metrics` | Считает предельный CPL по экономике клиента и сверяет с планом — реалистичен или нет |
| `ad-teardown` | Разбирает чужую рекламу из Ads Library и AdHeart, вытаскивает приёмы которые можно повторить |
| `ru-copywriter` | Пишет хуки, заголовки, скрипты UGC, посты, карусели на русском |
| `creative-brief-writer` | Собирает инженерное ТЗ для дизайнера, копирайтера или продакшна — 14 блоков |
| **`higgsfield-prompt-generator`** | **Промпты под видео-нейросети Higgsfield (Cinema/Marketing Studio + Veo 3.1 / Kling 3.0 / Seedance 2.0 / Soul ID / Nano Banana 2). 22 секции / 22 валидации / 7 дедикейтед PRESET'ов под рисковые ниши (B2B SaaS Enterprise / CRISIS / KIDS / HIGH_TICKET PRO SERVICES / REAL_ESTATE_EXPAT USA / WELLNESS_HEALTH_RESTRICTED USA / EU_RUSSIAN_DIASPORA)** |
| `text-humanizer` | Когда готовый текст звучит «как AI» (обтекаемо, без конкретики) — переписывает на живую речь |

### Запуск, проверка, диагностика (этапы 7-9)

| Скил | Что делает |
|---|---|
| `meta-policy-checker` | Проверяет крео и текст на риск бана в Мете до загрузки. **27 категорий** (после всех Т-волн и К-фиксов ночной автономки 2026-05-20) |
| `meta-launch-checklist` | **8-блочный** чек-лист готовности кабинета перед запуском — Pixel, CAPI, домен, iOS, UTM + EU compliance + Stripe-CAPI (после К20 + К35) |
| `campaign-diagnoser` | Диагностирует почему кампания плохо качает — проходит по 7 узлам отказа |
| `winner-variations` | 3 варианта на победителя — масштабирование выигравшего крео через вариации |
| `weekly-report-writer` | Пишет недельный или месячный отчёт клиенту — не свалка цифр, а история и план |
| `analytics-deep-dive` | Глубокая аналитика кампаний (cohort, юнитка, корреляции, месячная модель ROI). Используется в отдельном Cowork-проекте `analytics-проект/` |
| `client-comms` | Отвечает на возражения клиента и собирает файл передачи проекта другому таргетологу |

### Качество и память

| Скил | Что делает |
|---|---|
| `quality-gate` | Жёсткая проверка артефакта перед отправкой клиенту по 10 пунктам |
| `iterative-refiner` | Итеративная доводка содержательной задачи — делает, критикует, переделывает, пока не «хорошо» |
| `memory-updater` | После недельной итерации обновляет файл памяти по клиенту — чтобы не повторять отбракованные гипотезы |

### Утилиты сессии

| Скил | Что делает |
|---|---|
| `chat-handoff` | Когда чат становится длинным — выдаёт компактный summary для копирования в первое сообщение нового чата |
| `geo-memos` | Гео-специфичные памятки по регуляторике (KZ / EU / USA / UK) |
| `terminal-instructions` | Когда выдаёшь команды для bash / git / npm — явно помечает интерактивные запросы (пароли, Y/N) |

## Как запускать

Скилы сами подхватываются по русским фразам в обычном чате с Claude. Примеры:

- «Напиши 5 хуков для крео про английский для мам» — подхватит `ru-copywriter`
- «Сделай промпт под Higgsfield для B2B SaaS Enterprise CTO» — подхватит `higgsfield-prompt-generator` с автоматической активацией `B2B_SAAS_ENTERPRISE_PRESET` (9 правил + 9/9 PASS чек-лист)
- «Промпт для real-estate Miami foreign buyers» — подхватит `higgsfield-prompt-generator` с `REAL_ESTATE_EXPAT_USA_PRESET` (FHA + FinCEN GTO + EB-5 SEC + AI-staging FTC §5)
- «Промпт под supplement Reel для US weight-loss» — подхватит `higgsfield-prompt-generator` с `WELLNESS_HEALTH_RESTRICTED_USA_PRESET` (DSHEA + FTC «Gut Check» + Click-to-Cancel)
- «Промпт для PL adwokat на DE-диаспору» — `higgsfield-prompt-generator` с `EU_RUSSIAN_DIASPORA_PRESET` (sanctions + GDPR Art.9 + cross-border BRAO §206)
- «Разбери эту рекламу» (и ссылка или скрин) — подхватит `ad-teardown`
- «Прогон офферов через светофор» — подхватит `quality-gate`
- «Реалистичен ли CPL 3 USD для онлайн-курса по бухучёту» — подхватит `reality-check-metrics`
- «Чек-лист запуска Меты, готов ли кабинет» — подхватит `meta-launch-checklist`
- «Что не так с кампанией, CPL вырос вдвое за 3 дня» — подхватит `campaign-diagnoser`
- «Напиши недельный отчёт по клиенту X» — подхватит `weekly-report-writer`
- «Этот текст звучит как AI, оживи» — подхватит `text-humanizer`
- «Подведи черту, пора в новый чат» — подхватит `chat-handoff`

Триггеры внутри каждого скила прописаны заранее — можно говорить своими словами, не зубрить команды.

## Что нового в актуальной версии (волны П.1-П.20 + Т.1-Т.8)

Подробный список — в [CHANGELOG.md](./CHANGELOG.md). Архитектурный обзор — в [ARCHITECTURE.md](./ARCHITECTURE.md). Словарь имён — в [GLOSSARY.md](./GLOSSARY.md).

**Ключевые приросты:**

- **10 канонических ниш** + **6 sub-profile УРОВЕНЬ 3** (`B2B_SAAS_ENTERPRISE` / `HIGH_TICKET_PRO_SERVICES` / `EU_RUSSIAN_DIASPORA` / `REAL_ESTATE_EXPAT_USA` / `WELLNESS_HEALTH_RESTRICTED_USA` / `KIDS_PARENTS_EDTECH`).
- **10 PRESET'ов** в `higgsfield-prompt-generator` (B2B_SAAS_ENTERPRISE + B2B_SAAS_SMB + REAL_ESTATE_EXPAT_USA + REAL_ESTATE_EXPAT_EU + WELLNESS_HEALTH_RESTRICTED_USA + EU_RUSSIAN_DIASPORA + ECOM_IMPULSE_USA + HIGH_TICKET_PRO_SERVICES + KIDS_PARENTS + KIDS_PARENTS_EDTECH + CRISIS-AUDIT-LAYER) — каждый с финальным чек-листом 8/8 или 9/9 PASS перед выдачей промта.
- **22 валидации V1-V22** (включая V17 hook против Жертвы / V18 anchor pricing / V19-BIOCLAIM / V20 offer↔story / V21 humanization + rationality / V22 length-gate — лимит длины промта под поле Higgsfield).
- **4 Pre-валидатора A.1-A.4** (absolute promise / real brand / BIOCLAIM / non-USD currency conversion).
- **22 запрещённых AI-маркера** для humanization (cinematic / 8k / vibrant / perfect / flawless / etc).
- **8 anti-patterns A1-A8** + **10 RAT1-RAT10 проверок рациональности сценария** (переименовано из R1-R10 в волне П.20 для disambiguation от §3 prompt-rules R1-R14).
- **EXECUTIVE-CALIBRATED + MEDICAL-CALIBRATED humanization tables** (SKIP H1/H5/H6/H9 для CTO Fortune 500 + врача).
- **13 регуляторных категорий** в `meta-policy-checker` (12 юрисдикций: US ABA+SEC+FINRA+state bars / UK SRA+BSB+FCA / EU NRA+BRAK+MiFID / CH FinSA + FHA/HUD/FinCEN GTO/FIRPTA/EB-5 SEC+USCIS/RESPA / DSHEA/FTC Gut Check/CA Prop 65/NY AG/Click-to-Cancel/Ryan Haight + GDPR Art.9 + EU sanctions 269/833/2014 art.5n + UK OFSI + Swiss SECO).
- **Risk-profile средний** упал с **6.86** (pre-T baseline) до **≈3.3** (post-Т.8) = **-52%** благодаря 8-волновому стресс-тесту.

## Зачем нужен файл-конвейер курса

10 скилов из 25 ссылаются на «Лист 1-10» рабочей таблицы курса (`client-profile`, `reality-check-metrics`, `schwartz-podhody`, `creative-brief-writer`, `higgsfield-prompt-generator`, `meta-launch-checklist`, `campaign-diagnoser`, `weekly-report-writer`, `client-comms`, `memory-updater`). Это значит они знают порядок этапов — где какой лист должен быть закрыт до перехода дальше.

Чтобы они работали на полную — загрузи файл `KONVEYER-LOGIKA.md` (его дают на курсе) в Claude Project. Тогда скил видит полный контекст конвейера и точно понимает на каком этапе ты сейчас.

Без этого файла остальные 15 скилов работают независимо и без потерь — `ru-copywriter` напишет хук, `ad-teardown` разберёт рекламу, `brand-extractor` соберёт brand kit. Никаких обязательных зависимостей нет.
