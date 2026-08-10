# Памятка по US / Canada Wellness Compliance

Когда использовать. При работе с wellness / health / fitness / nutrition клиентами в США и Канаде.

## US (Federal Trade Commission + iOS ATT)

FTC Wellness Rules:
— Запрещены medical claims без научной базы (RCT preferred)
— «May support» / «associated with» / «in some users» допустимы
— «Cure» / «treat» / «heal» / «fix» / «reverse» - запрещены, Meta + FTC блокируют
— Testimonials с disclaimer «results not typical»
— Income claims (для coaches) - под FTC Endorsement Guides

Трекинг на iOS:
— Большая часть пользователей iPhone отказывается от трекинга [ГИПОТЕЗА: доля отказов высокая, конкретный процент по рынку не сверялся - точную цифру не называй клиенту]
— Нужен CAPI (Conversions API) + Offline Conversions
— Браузерный Pixel в одиночку показывает заметно меньше реальных конверсий, чем есть [ГИПОТЕЗА: масштаб потерь считай по разнице с CRM клиента, а не по чужой цифре]
— Server-side трекинг рекомендуется
— Порядок работы с цифрами: сначала CAPI, потом сверка с CRM клиента, и только если и того и другого нет - прикидочный множитель, помеченный как гипотеза

HIPAA-adjacency:
— Wellness coaches НЕ medical providers - HIPAA не применяется напрямую
— Intake forms с health info - храни в HIPAA-compliant storage (Practice Better, Healthie)
— Никогда не публикуй client health data даже с consent (FTC может оспорить)

## Canada (Health Canada + CASL + PIPEDA)

Health Canada:
— Режет заметную часть типовых хуков ниши - те, что построены на лечебном обещании [ГИПОТЕЗА: доля по рынку не сверялась, цифру клиенту не называй]
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
— Провинциальные законы бывают жёстче федерального. Квебек - Law 25 (внесён как Bill 64), режим приватности строже PIPEDA; название и статус сверяй перед тем, как ссылаться на него в переписке с клиентом
— Cookie consent + opt-in для tracking

## Как устроен рынок

Кампании ведём только в Meta. Остальное ниже - контекст ниши, чтобы понимать, откуда у аудитории насмотренность; бюджет по другим каналам не распределяем и вести их не учим.

US wellness:
— Заметная часть ниши живёт в коротком вертикальном видео, аудитория пришла в Meta с той же насмотренностью - под неё и снимаем
— Женская аудитория 25-40 - ядро ниши

Canada wellness:
— Торонто и Ванкувер - английский, Квебек - нужен французский, отдельная связка крео и лендинга
— Сильное сообщество натуропатов - источник доверия и возражений одновременно

## Чек перед запуском

Перед запуском wellness кампаний в US/Canada:
— Прогон через FTC Wellness Rules (US) или Health Canada (CA)
— Все testimonials с disclaimers
— CAPI настроен и событие реально доезжает
— Intake forms HIPAA-compliant (US)
— CASL explicit consent flow (Canada)
