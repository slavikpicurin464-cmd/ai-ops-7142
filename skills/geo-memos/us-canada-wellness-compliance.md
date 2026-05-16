# Памятка по US / Canada Wellness Compliance

Когда использовать. При работе с wellness / health / fitness / nutrition клиентами в США и Канаде.

## US (Federal Trade Commission + iOS ATT)

FTC Wellness Rules:
— Запрещены medical claims без научной базы (RCT preferred)
— «May support» / «associated with» / «in some users» допустимы
— «Cure» / «treat» / «heal» / «fix» / «reverse» - запрещены, Meta + FTC блокируют
— Testimonials с disclaimer «results not typical»
— Income claims (для coaches) - под FTC Endorsement Guides

iOS 14+ ATT:
— 75% iPhone users opt-out из tracking
— Нужен CAPI (Conversions API) + Offline Conversions + Aggregated Event Measurement
— Web Pixel без ATT даёт 25-30% реальных данных
— Server-side tracking via Stape / Anyflow / Segment рекомендуется

HIPAA-adjacency:
— Wellness coaches НЕ medical providers - HIPAA не применяется напрямую
— Intake forms с health info - храни в HIPAA-compliant storage (Practice Better, Healthie)
— Никогда не публикуй client health data даже с consent (FTC может оспорить)

## Canada (Health Canada + CASL + PIPEDA)

Health Canada:
— Блокирует ~40% типовых hooks конкурентов
— Запрещены therapeutic claims без license (только Health Canada-registered NHPs)
— Functional claims разрешены если backed by Health Canada NHP monograph
— Hormones / thyroid / chronic disease claims - почти всегда блокируются

CASL (Canadian Anti-Spam Law):
— Stricter than US CAN-SPAM
— Explicit consent для email обязателен
— Implicit consent ограничен 24 месяцами
— Penalties до CAD $10M per violation

PIPEDA:
— Federal privacy law
— Provincial laws могут быть стricter (Quebec Bill 64)
— Cookie consent + opt-in для tracking

## Платформы

US wellness:
— Meta 60% + TikTok 25% + reserve 15% оптимальный split
— TikTok сильнее для wellness women 25-40
— Pinterest хорош для weight loss / nutrition top-funnel

Canada wellness:
— Meta 70% + TikTok 20% + Google 10%
— Toronto/Vancouver English-speaking, Quebec - French требуется
— Naturopath community сильна — гео-партнёрства

## Чек для бота

Перед запуском wellness кампаний в US/Canada:
— Прогон через FTC Wellness Rules (US) или Health Canada (CA)
— Все testimonials с disclaimers
— CAPI настроен (US iOS 14+)
— Intake forms HIPAA-compliant (US)
— CASL explicit consent flow (Canada)
