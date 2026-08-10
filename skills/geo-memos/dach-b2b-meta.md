# Памятка по DACH B2B (Германия / Австрия / Швейцария) на Meta

Когда использовать. При работе с B2B клиентами в DACH регионе — SaaS, professional services, Mittelstand. Курс ТОЛЬКО про Meta — другие каналы вне scope.

## Основной канал

Meta (Facebook + Instagram + Audience Network) — единственный канал в курсе. Для DACH B2B Meta работает через 1P Custom Audience из CRM + retargeting site-visitors + lookalike 1% от paying customers. Без качественной 1P-базы Meta lookalike для узкого DACH-ICP даёт слабые результаты.

LinkedIn Ads / Google Ads / любые другие каналы — вне scope курса. Если клиенту критически нужен LinkedIn-канал — это отдельная экспертиза, не учим в курсе.

## Ориентиры Meta для DACH B2B

Цифры ниже - ориентир для прикидки, не бенчмарк. [ГИПОТЕЗА: диапазоны собраны по рынку, не по кабинету конкретного клиента]. В расчёт клиенту подставляй факт его кабинета, а не эти числа; если факта нет - помечай цифру как гипотезу прямо в расчёте.

— CPM B2B broad: 12-20 USD
— CPM узкий ICP через Custom Audience: 25-40 USD (выше за счёт малой аудитории)
— CTR Feed: 1.5-2.5%
— CPL B2B mid-market: 80-200 USD
— CPQM enterprise (через 1P CRM ABM): 250-500 USD
— Цикл сделки 60-180 дней — payback не виден до 3-4 месяцев

## Особенности Meta в DACH

— **Detailed Targeting** работает слабее чем в US (Mittelstand плохо размечен по интересам). Дефолт — 1P Custom Audience.
— **Custom Audience из CRM** — выгрузка email/phone hash принимающих решения (CEO / Head of X / department heads), импорт в Meta через Hashed Email / Phone matching.
— **Retargeting site-visitors** — обязательно через Meta Pixel + CAPI. Server-side трекинг критичен: часть событий с браузера не доезжает из-за отказов от трекинга на iOS и из-за GDPR-баннеров.
— **Lookalike 1%** строй от paying customers / closed-won deals, не от leads (leads-lookalike даёт слишком широкую аудиторию).
— **Advantage+ Audience** для ABM через 1P CRM лучше не расширять: алгоритм размывает узкую аудиторию. Но в части типов кампаний Мета включает расширение сама и переключателя не даёт - тогда не ищи его, а держи узость на стороне входа: чистая 1P-база, отдельная кампания под ABM, крео под конкретную роль.
— **Плейсменты:** Feed (Facebook + IG) приоритет, Stories вспомогательно. Audience Network — для retargeting. Reels — для top-of-funnel awareness под молодую часть DM.

## 5-роль buying committee для DACH enterprise

— **Initiator** — тот кто ищет решение (operational manager / IT specialist)
— **Influencer** — тех-лиды, аналитики, консультанты которые формируют мнение
— **Champion** — внутренний адвокат сделки, продаёт решение коллегам и руководству
— **User** — конечный пользователь после внедрения
— **Decision-maker** — подписант бюджета (CFO / CTO / VP)

Без Champion enterprise-сделка в DACH не закрывается. Маркер в цитатах — «я лично продавал это нашему Geschäftsführer», «я взял этот проект на себя».

В крео ролевая сегментация обязательна:
— UGC-screencast для Initiator (показывает «как это работает на практике»)
— CAROUSEL кейс для Champion (помогает ему продавать внутри компании)
— STATIC с цифрами ROI для Decision-maker

## Compliance — особо строго

— **GDPR + Datenschutzgrundverordnung (DE)** — enforcement крайне жёсткий. Datenschutzbeauftragter mandatory для компаний от 20 человек.
— **FADP (Швейцария, не GDPR)** — отдельный режим для CH-аудитории.
— **FINMA** для финансовых услуг — отдельная лицензия.
— **BaFin** для banking / investments.
— **Mitbestimmungsrecht (DE)** — Betriebsrat (workers' council) имеет право обсуждать любую систему мониторинга сотрудников. Реклама time-tracking как «контроль» в DE запрещена де-факто. Позиционируй как «команда сама фиксирует часы» / «прозрачность для команды».
— **Datenschutzgesetz (AT)** — австрийский режим, подход тот же, что в DE.
— **Double opt-in для email обязателен.**
— **Баннер согласия на лендинге** - сертифицированный CMP, не самописный скрипт. Согласие должно реально доезжать до Meta Pixel и CAPI: нет согласия - событие не отправляется. (Consent Mode v2 - механизм Google, он нужен клиенту только если тот параллельно ведёт Google Analytics или Google Ads; на метовскую сторону он не влияет.)
— **Meta CAPI с server-side трекингом** — критично для DACH: браузерных событий доезжает мало из-за отказов от трекинга и баннеров согласия.

Соседние рынки (Нидерланды, Бельгия, скандинавы) в эту памятку не входят - там свой регулятор и свой закон о данных, по аналогии не применять.

## Языковая стратегия

— **English** — для startups / scaleups / international companies (Berlin tech, Zurich fintech, Vienna SaaS)
— **German** — для Mittelstand (традиционный средний бизнес) обязательно. English-копи для Mittelstand заметно проседает по конверсии [ГИПОТЕЗА: порядок просадки - десятки процентов, точную цифру бери из своего сплит-теста языка].
— **Mix EN+DE landing pages** для cross-segment campaigns, A/B-тест языка лендинга на одной аудитории.

## Что вне scope курса

— LinkedIn Ads (Document Ads, Conversation Ads, Sponsored InMail) — отдельная экспертиза, не учим
— Google Ads (Search + Display) — отдельная экспертиза
— Любые другие каналы (Reddit Ads, X Ads, Pinterest Ads) — не учим
— ABM через 6sense / Demandbase / Terminus — другая категория инструментов

Если клиенту ученика нужен LinkedIn-канал — отправляй «канал LinkedIn вне scope курса. По Meta-конвейеру для DACH B2B — продолжаем».

---

См. также:
- См. секцию Reality-check в `reality-check-metrics` скиле плагина — для расчёта предельного CPL/CAC по экономике B2B_SAAS-клиента
- `meta-launch-checklist` SKILL — короткая проверка технической готовности перед стартом (событие доезжает, домен подтверждён, согласие на лендинге собирается и передаётся)
