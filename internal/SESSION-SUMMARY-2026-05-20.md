# SESSION SUMMARY 2026-05-20 — полное саммари со всеми нюансами + stop-list

**Сессия:** доводка после cleanup c23aed5 → ночная автономка → откат scope-creep.
**Git:** `c23aed5 → d15d38b` (12 коммитов), origin/main синхрон.
**Назначение файла:** handoff для следующего чата/бота. Перед любой правкой — свериться с разделами 2 и 3.

---

## 1. СИСТЕМА

Курс AI-таргетолог + плагин ai-ops-7142 = единая система.
- **Курс** = методика (hub-and-spoke, 4 чата в Cowork). Целевая аудитория: русскоязычные таргетологи CIS-кроме-РФ + EU + USA.
- **Плагин** = 26 автоматических скилов (GitHub: slavikpicurin464-cmd/ai-ops-7142).

**2 проекта для коворка:**
1. Основной курс — `final-v3/cowork-загрузка/` (10 файлов)
2. Аналитика (отдельный, новый) — `final-v3/analytics-проект/` (4 файла)

**4 чата:** ЧАТ 1 Оркестратор (INSTRUCTIONS) → ЧАТ 2 Ресерч (PROMPT-2) → ЧАТ 3 Копирайт+Higgsfield (PROMPT-3 + PROMPT-4) → ЧАТ 4 Аналитика (PROMPT-5). + опц. Чат 5 Визуал (НАБОР-ДЛЯ-AI-КРЕАТОРСТВА = PROMPT-6).

---

## 2. КАНОН — ЧТО НЕЛЬЗЯ МЕНЯТЬ

### 2.1 Архитектура
- Hub-and-spoke 4 чата — НЕ возвращаться к «один умный плагин на всё».
- Курс + плагин = единая система, не альтернативы.

### 2.2 Таксономия — 10 канонических профилей (имена + порядок NO TOUCH)
INFOBIZ / LOCAL_SERVICE / ECOM / B2B_SAAS / HIGH_TICKET / CRISIS_EXPERT / REAL_ESTATE_EXPAT / WELLNESS_HEALTH_RESTRICTED / KIDS_PARENTS / ECOM_IMPULSE
+ GREY_NICHE (надстройка, НЕ профиль) + подпрофили через «BASE + специфика».

### 2.3 Канал — Meta-only
Facebook + Instagram + Audience Network (плейсменты Feed/Reels/Stories).
- TG Ads — ТОЛЬКО по явному запросу ученика (НЕ авто-fallback, дефолт = Meta).
- TikTok / Yandex / Google / LinkedIn / Pinterest / VK — вне scope как каналы рекламы.

### 2.4 Контентные правила (hard-gate, НЕ откатывать)
- Запрет сегмента Жертвы («разочарованная», «уже сливала», «снова страшно», «мы понимаем») — тест 3 вопросов.
- УТП в крео запрещено (5 исключений: брендовая на Most-aware / LOCAL_SERVICE с очевидным преимуществом / B2B SaaS Most-aware / новая категория / ретаргет тёплого).
- Дисклеймеры и AI-штампы в крео запрещены.
- «Бесплатно» для CRISIS_EXPERT — жёсткий блок → «диагностика-аудит / первичная оценка».
- Hormozi-urgency «закрытие набора» в WELLNESS = risk-flag → «следующий поток через X недель».
- Named-конкуренты в крео запрещены.
- Слабые CTA («узнай больше / жми / переходи / подробнее») запрещены. Исключение: «узнать больше» для CRISIS_EXPERT.
- Минимум 2-3 параллельных сегмента в STANDARD, 3-5 в PRO.
- meta-policy-checker pre-flight на этапе ОФФЕРОВ (не только крео) для risk-ниш.

### 2.5 Бюджетные режимы
LITE $0-500 (1 гео) / STANDARD $500-3000 (1-2 гео) / PRO $3000+ (3-5 гео при ≥$500/гео).

### 2.6 Принципы Игоря (PRINCIPLES-USER §1-32)
27 базовых (на «ты», серые ниши OK, без морализаторства, Reality-check не блокирует, УТП после ресерча и т.д.) + §28-32 из Волны Т (junior-mode, проактивная шпаргалка, meta-policy pre-flight, TG Ads по запросу, бесплатно-блок CRISIS).

### 2.7 GitHub
НЕ удалять repo. НЕ force-push. Ветку `backup-before-cleanup-2026-05-19` НЕ удалять. Merge conflicts → спросить Игоря.

---

## 3. STOP-LIST — ЧТО НЕЛЬЗЯ ДОБАВЛЯТЬ / ВОЗВРАЩАТЬ

### 3.1 Удалено в cleanup c23aed5 (2026-05-19)
- ❌ LATAM_PRESET (BR/MX/AR/CL/CO/PE)
- ❌ APAC_PRESET (JP/KR/SG/AU)
- ❌ CRYPTO_WEB3_PRESET full + CRYPTO/WEB3 META категория
- ❌ PET_SUPPLIES_USA_LAYER + OTC_PHARMA_USA_LAYER
- ❌ EU AI Act art.50 production process + backend runbook (DocuSign/DB)
- ❌ CI infrastructure (Docker / GitHub Actions / test-harness JSON)

### 3.2 Вычищено в чистке scope-creep 2026-05-20 (коммит 100d341)
Агенты ночной автономки протащили под видом фиксов. НЕ ВОЗВРАЩАТЬ:
- ❌ **TikTok Ads** как канал рекламы (подсекции с метриками)
- ❌ **Yandex Direct** как канал (₽-бенчмарки, РСЯ, ОРД/erid) — вне scope + РФ
- ❌ **iOS-регионы Singapore / Japan / Australia** (это APAC) + **Israel / UAE** (вне CIS-EU-USA)
- ❌ **LEGAL_BANKRUPTCY_US** полная регуляторика (State Bar/NACBA/§528) — 0.0001%
- ❌ **USDT × LEGAL DE AML** (5AMLD/6AMLD/BaFin/GwG/Anderkonto) — 0.0001%
- ❌ **MEDICAL_HEAVY / HEALTHCARE_COMPLIANCE_HEAVY** как отдельный профиль
- ❌ **M&A_ADVISORY / FAMILY_OFFICE / PRIVATE_BANKING** как отдельные профили

### 3.3 Призма-гейт (мета-правило)
Перед ДОБАВЛЕНИЕМ канала/профиля/региона/регуляторики — 3 вопроса:
1. Нужно 99% таргетологов или 0.0001%?
2. Покрывает scope (CIS-EU-USA, Meta-only)?
3. Курс/скилы зависят от этого?
Если хоть один «нет» → OPEN-QUESTIONS, ждать Игоря. НЕ применять автономно, даже если закрывает реальный gap.

---

## 4. ВАЖНЫЕ НЮАНСЫ И ИСКЛЮЧЕНИЯ (легко перепутать)

### 4.1 TikTok — что РАЗРЕШЕНО (не удалять)
- **TikTok Creative Center / TikTok-комменты** = research-источники (насмотренность, сбор болей). Канон Q1 их прямо разрешает.
- **«TikTok-style»** = стиль вертикального динамичного крео для **Meta Reels**, не реклама в TikTok.
- **«клиент хочет уйти на TikTok»** = возражение, которое скил `client-comms` отрабатывает (удерживает в Meta).
Запрещён только TikTok как **канал рекламы клиента** с метриками/чек-листами.

### 4.2 iOS-механизм — что ОСТАЛОСЬ
Корректировка атрибуции ×1.35-1.50 для **USA / Canada / EU-high-iOS** — РАЗРЕШЕНА и нужна. Убраны только регионы Singapore/Japan/Australia/IL/UAE из списка.

### 4.3 Крипто-платежи — что ОСТАЛОСЬ
Учёт USDT/USDC как способа оплаты в аналитике (комиссии биржи, конвертация в USD для ROAS) — РАЗРЕШЕНО, это про учёт платежей, НЕ про CRYPTO_WEB3_PRESET. Удалена только USDT×LEGAL DE AML регуляторика (юридический overengineering).

### 4.4 Медицина — что ОСТАЛОСЬ
Медицинская регуляторика (лицензия МЗ, «есть противопоказания», запрет AI-лиц пациентов, FDA disclosure) СОХРАНЕНА под именем подпрофиля **`LOCAL_SERVICE HIGH_TICKET (медицина)`**. Удалено только самовольное имя профиля MEDICAL_HEAVY. (Примечание: alias `HEALTHCARE_COMPLIANCE_HEAVY` мог остаться в client-profile как cross-ref для higgsfield — это ОК, не трогать без проверки ссылок.)

### 4.5 LEGAL_BANKRUPTCY_US — что ОСТАЛОСЬ
1 строка в CRISIS_EXPERT: «клиент-эксперт сам отвечает за State Bar compliance, таргетолог — только Meta-policy + Attorney Advertising disclaimer». Удалена только глубокая US-юр-регуляторика (~120 строк).

### 4.6 Что из ночной автономки ОСТАВЛЕНО (по делу, не трогать)
- B2B_SAAS_SMB подпрофиль (флаг, чек $19-299, mutually-exclusive с ENTERPRISE по $300+)
- GREY_NICHE Schwartz-матрица (Solution/Most-aware, skip Unaware)
- «Беженцы»/refugee/asylum в explicit FAIL для EU_RUSSIAN_DIASPORA (8 строк, по делу)
- Stripe-CAPI sub-check для subscription
- Pre-flight gate в meta-launch-checklist (vape/casino/adult → СТОП до запуска)
- REAL_ESTATE_EXPAT — вечнозелёные правила (Special Ad Housing, без конкретных сумм/дат Golden Visa)

### 4.7 TG Ads — точная формулировка
Пресеты TG Ads ОСТАЛИСЬ в скилах (creative-brief-writer, reality-check-metrics, analytics-deep-dive) с пометкой ⚠️ «не дефолт, только по запросу». Дефолт когда GREY_NICHE не проходит Meta: бот предлагает 3 варианта (Meta с authorization / ниша вне scope / TG Ads по явному запросу). НЕ переключается автоматически.

---

## 5. ЧТО СДЕЛАНО В СЕССИИ (хронология)

1. **Аудит после cleanup** — 4 агента, 13 групп багов исправлено (8→10 везде, битые ссылки, README 22→25, §29→§1-27, OPEN-QUESTIONS баг, DO-NOT-CHANGE Reels→Audience Network).

2. **Ночная автономка** (~50 агентов Opus, 4 фазы):
   - Создан analytics-deep-dive (скил) + проект Аналитика (4 файла). Принцип — месячная модель ROI.
   - EU_RUSSIAN_DIASPORA перенесён в KONVEYER.
   - Junior-mode + проактивная шпаргалка 32 терминов.
   - Стресс-тест 30 учеников (с «казахами-junior») → 51 фикс (К1-К38 курс + 24 аналитика).

3. **Откат scope-creep** (по наводке Игоря про TG Ads) — см. раздел 3.2.

4. **Строгая фиксация stop-list** — DO-NOT-CHANGE §3.5/§6.5 + CHANGELOG + SUMMARY с пометками [ОТКАЧЕНО 2026-05-20].

---

## 6. ИЗВЕСТНЫЕ ХВОСТЫ (на ревью)

1. **Пилот не проведён** — все 30 тестов это симуляции. На живом ученике может вылезти UX-косяк → Волна 4 фиксов по реальному feedback.
2. **REAL_ESTATE_EXPAT Golden Visa** — правила оставлены вечнозелёными (без конкретных сумм/дат), т.к. программы меняются ежеквартально.
3. **TG Ads / не-Meta** — курс под них не отлажен, честно говорит «вне курса».
4. **Backup'ы 2026-05-19** ещё лежат (final-v3_backup + 4 client backup + git branch) — удалить после успешного пилота.
5. **Системный урок** — призма должна быть гейтом в ТЗ каждого фикс-агента ПЕРЕД добавлением, а не аудитом постфактум. В этой автономке мандат агентов был слишком широк → ~20% scope-creep.

---

## 7. GIT

```
d15d38b Строгая фиксация чистки scope-creep в каноне (stop-list)
100d341 Чистка scope-creep — призма «не перебор ли это»
17738f6 Откат TG Ads до «по явному запросу»
1c2eaeb ФАЗА 4 финал: финальный аудит + 30+ остаточных фиксов
e82f0f2 ФАЗА 4: Финальный SUMMARY
c888aa8 ФАЗА 3 Волна 3 курса
3990456 ФАЗА 3 Волна 2 курса
e977dff ФАЗА 3 Волна 1 курса
d43277c ФАЗА 2.1 Стресс-тест аналитики
6a94641 ФАЗА 2 analytics-deep-dive
48b7b6f ФАЗА 1 подготовка
f96d116 Post-cleanup audit fixes
(база: c23aed5 cleanup + 07a27e8 DO-NOT-CHANGE — вчера)
```

**Статус:** production-ready, готово к пилоту на живом ученике.
