# REFERENCE — справочник higgsfield-prompt-generator (подгружается по требованию из SKILL.md)

## 1. PHOTOREAL ZONES (ЗОНА 1-8 — текстуры по зонам)

═══════════════════════════════════════════════════
PHOTOREAL ZONES (текстуры по зонам)
═══════════════════════════════════════════════════

ПРАВИЛО: пиши текстуры позитивными существительными, не отрицаниями. «visible skin pores» работает сильнее чем «no plastic skin». Подключай нужные зоны под кадр — не все 8 сразу, иначе промпт распухнет.

ЗОНА 1 — SKIN

Base: visible skin pores, subsurface scattering, micro-texture detail, natural skin oils on T-zone, peach fuzz on cheeks and jawline, slight redness on cheeks/nose/ears, uneven skin tone, visible capillaries near temples, small blemishes and moles, fine lines around eyes and mouth.

По возрасту:
— young → less wrinkles, more peach fuzz, smoother but textured
— mature → defined nasolabial folds, crow's feet, age spots, neck lines
— child → softer subsurface, rounder cheeks, no visible pores

Lighting on skin: soft falloff on cheekbones, key light reveals pore structure, rim light catches peach fuzz, shadow side retains skin detail.

Под ECU обязательно: visible individual pores, peach fuzz catching rim light, micro-blemishes, sebaceous detail, fine vellus hair.

ЗОНА 2 — EYES

Base: defined iris pattern with radial striations, limbal ring visible, catchlight from key light source (укажи позицию), wet film on eyeball, lower eyelid moisture line, visible eyelash count and direction, eyebrow hair direction, faint vein in sclera, slight asymmetry between eyes.

Gaze:
— direct → "eyes locked on lens, pupils centered, no off-axis drift"
— averted → "eyes look [direction], iris partially hidden by upper lid, no crossed eyes"

Эмоция через глаза:
— squint → "outer corners narrow, lower lid raised, crow's feet activate"
— wide → "upper lid lifted, sclera visible above iris, pupil dilated"

Под ECU/CU: reflection in eye matches key light position and shape, pupil reflects scene elements (window/light fixture), capillary detail in sclera near tear duct.

ЗОНА 3 — LIPS

Base: visible lip texture and vertical micro-lines, natural lip color graduation (darker at edges), cupid's bow defined, philtrum shadow, slight moisture sheen but not glossy, upper and lower lip asymmetry.

States:
— speaking → "mouth slightly parted, teeth visible, lip muscles engaged"
— closed → "lips touching naturally, soft compression line"
— smiling → "corners pulled up and back, cheek muscles raised, upper teeth visible (not all), lower lip stretched"

ECU: fine vertical lip lines, moisture beads, slight chapping, natural color variation, no glossy uniform surface.

ЗАПРЕЩЕНО: "perfect lips", "glossy lips", "uniform red" — даёт пластик.

ЗОНА 4 — TEETH (расширенная для медицинских иллюстраций)

Базовая (для talking-head где зубы видны случайно):
natural enamel translucency, slight yellow tint, individual tooth definition, gum line visible, no glow, no uniform whiteness, typical 8 visible upper / 8 lower in wide smile.

Расширенная M-зона (для 3D-моделей челюсти, схем имплантов, медицинской иллюстрации, образовательной графики, до/после на моделях):

Individual tooth anatomy: incisors (front 4) with flat edges, canines (corner 2) with pointed cusps, premolars (5,6 from center) with two cusps, molars (7,8 from center) with four-cusp grinding surfaces. Each tooth geometrically distinct, no merged or duplicated teeth.

Gum tissue (gingiva): pink-red color graduation darker at root level, lighter at margin, papilla (triangular gum between teeth) visible, stippled texture (orange-peel-like), no glow, no uniform plastic look, natural moisture sheen.

Occlusion: upper and lower teeth meet at natural contact points, slight overbite normal (1-2mm), molars interdigitate, no floating tooth, no gap between upper and lower when closed.

Brackets (если в кадре): metal or ceramic, attached flush to tooth surface, archwire passes through bracket slot, ligature ties visible, no floating brackets.

Implant (если в кадре): titanium screw threads (Ti grade-4 brushed finish) embedded in 3D bone-model, abutment connector visible at gum level, ceramic crown on top (separately, indicate material).

X-ray / radiograph (educational visual): grayscale tones, bone density gradient, tooth roots visible, periodontal space as thin dark line, NO photoreal — render as medical illustration (Nano Banana 2 static).

ЗАПРЕЩЕНО: «shiny white teeth», «perfect smile», «glowing teeth», «uniform white» — даёт glow effect. Описание реального рта пациента словами — запрещено (FDA-class). Расширенная зона применяется ТОЛЬКО когда зубы/челюсть — главный объект кадра (3D-модель, схема, медицинская иллюстрация), не на talking-head с улыбкой врача.

ЗОНА 5 — HAIR

Base: individual strand definition, baby hairs and flyaways at hairline, natural hair direction following growth pattern, visible scalp through hair (укажи density), hair catches rim light along outer edges, root color slightly darker, texture matches hair type (straight/wavy/coily).

В движении: motion shows hair shed and bounce, no rigid helmet, individual strands separate during turns, flyaways respond to wind/motion.

ЗАПРЕЩЕНО: "perfect hair", "shiny smooth hair" — CGI-look.

ЗОНА 6 — HANDS & FINGERS (главная боль AI)

ОБЯЗАТЕЛЬНО если руки в кадре:
five fingers per hand with correct proportions, visible knuckle creases, tendon detail on back of hand, nail beds defined, natural skin texture continues to hands, hand pose anatomically correct, fingers do not merge or duplicate.

Под gesture: describe exact finger positions — "thumb extended, index pointing, middle/ring/pinky curled".

ЗАПРЕЩЕНО: "elegant hands", "perfect hands" — выйдут 6 пальцев.

ЗОНА 7 — BODY / FABRIC

Body: natural body proportions matching age/gender, shoulders/hips/limbs in correct ratio, joints (elbows/knees/wrists) anatomically placed, no morphing limbs, weight distribution follows pose physics.

Fabric: visible fabric weave (укажи type: cotton/denim/silk/wool/leather), natural fabric drape following gravity, wrinkle pattern matches body pose and movement, stitching detail at seams, button/zipper accurate, fabric interacts with skin (no floating clothing), pattern follows surface curvature.

Под движение: fabric ripples and folds respond to motion with inertia, hem swings naturally, sleeves bunch at joints.

ЗОНА 8 — BACKGROUND

Base: consistent depth layering (FG/MG/BG separation), bokeh follows specified aperture (f/1.4 = heavy, f/8 = minimal), background lighting consistent with foreground key, shadows on subject match background light direction, no morphing background objects across frames (в видео), background detail decreases naturally with distance, atmospheric perspective on far elements (haze/desaturation).

Reflections: reflections show correct mirror geometry, reflected elements match scene contents, no ghost objects in reflection.

Shadows: shadow direction matches key light source position, shadow softness matches light size (point=hard, area=soft), contact shadows where subject touches surface, ambient occlusion in corners and crevices.


## 2. ZONE MATRIX + ГОТОВЫЕ PACKS

═══════════════════════════════════════════════════
ZONE MATRIX + ГОТОВЫЕ PACKS
═══════════════════════════════════════════════════

Какой pack под какой кадр:

| Тип кадра                     | Подключай                                              |
|-------------------------------|--------------------------------------------------------|
| Wide / establishing           | SKIN base + BACKGROUND + LIGHT CONSISTENCY             |
| MS / talking head             | SKIN + EYES + LIPS + HAIR (ОБЯЗАТЕЛЬНО, иначе T12)     |
| CU portrait                   | + детальные EYES/LIPS + HAIR (ОБЯЗАТЕЛЬНО) + HANDS если в кадре |
| ECU face                      | ECU FACE pack + EYES detailed                          |
| ECU hands                     | HANDS IN FRAME + SKIN                                  |
| Product                       | FABRIC + REFLECTION + BACKGROUND                       |
| Liquid pour / slow-mo / steam / foam | LIQUID DYNAMICS + REFLECTION + ANTI-AI-LOOK     |
| Medical transparent object    | TRANSPARENCY pack · medical sub-scope (Invisalign / mirror / vial) |
| Commercial transparent object | TRANSPARENCY pack · commercial sub-scope (frosted-amber bottle / parfum / crystal) |
| Medical illustration / X-ray  | MEDICAL_ILLUSTRATION (static-only, Nano Banana 2)      |
| Cultural / niche-specific     | + CULTURAL ACCURACY (≥1 cultural маркер)               |
| Multi-shot video              | + LIGHT CONSISTENCY всегда                             |
| Photoreal (любой)             | + ANTI-AI-LOOK PACK                                    |
| AI Soul ID на реального человека в WELLNESS_USA / WELLNESS / FINTECH / GREY paid | + AI DISCLOSURE pack (bottom-third overlay) |
| Infographic 2×2 style preview grid (лид-магнит «N промптов в M стилях») | STYLE-SWATCHES-GRID + §19B PIPELINE (Nano Banana 2) |
| Infographic 3-tier price/tariff/product comparison cards (с региональными флагами) | COMPARISON-CARDS + §19B PIPELINE (Nano Banana 2) |
| Infographic anatomical / technical progression (6мес/1год/3года, Step 1/2/3) | EDUCATIONAL-PROGRESSION + §19B PIPELINE (Nano Banana 2) |
| Infographic bar/donut/funnel/metric chart | INFOGRAPHIC-CHART + §19B PIPELINE (Nano Banana 2, V18 substantiation) |
| Infographic flowchart / process diagram with highlighted nodes | ANIMATED-DIAGRAM + §19B PIPELINE (Nano Banana 2 → Veo 3.1 для soft node-by-node reveal) |

ГОТОВЫЕ PACKS (копируй в промпт):

PORTRAIT CU:
```
visible skin pores, subsurface scattering, peach fuzz catching rim light, defined iris pattern with catchlight from {position}, wet film on eyeball, visible lip texture with vertical micro-lines, individual eyebrow hairs, natural skin tone variation, slight asymmetry
```

ECU FACE:
```
extreme close-up pore-level detail, individual peach fuzz hairs, micro-blemishes, sebaceous highlights on nose bridge, capillary detail near temples, eyelash count visible, moisture line on lower lid
```

HANDS IN FRAME:
```
five fingers per hand with correct anatomical proportions, visible knuckle creases and tendons, nail beds defined, hand skin texture matches face, no merged or extra digits
```

HAIR (ОБЯЗАТЕЛЕН для всего что MS/CU/ECU talking head — без него T12 helmet effect, известный артефакт Kling/Seedance/Veo на portraits):
```
individual strand definition, baby hairs and flyaways at hairline,
visible scalp through hair, hair catches rim light along outer edges,
root color slightly darker than tips. In motion: hair shows shed and
bounce, individual strands separate during head turns, no rigid helmet,
flyaways respond to head movement.
```

HAIR — short executive crop вариант (мужская короткая стрижка, B2B executive, юристы, врачи):
```
short professional crop, visible individual strand definition at temples
and crown, slight texture variation, faint hairline edge defined, slight
movement on micro-nod and head turn, no rigid helmet, no painted-on look.
```

LIQUID DYNAMICS (жидкости, slow-mo разливы, пенки, пар):
```
liquid follows realistic physics, surface tension visible at meniscus,
falling droplets form spheres mid-air with motion blur trailing,
viscous pour creates rope-like fold pattern, splash spreads radially,
slow-motion shutter 1/240s makes individual droplets readable,
refractive caustics on bottom of container, no floating liquid blobs,
gravity-driven flow with realistic acceleration, no levitating drops,
motion blur only on liquid stream, static elements remain sharp
```
Автоподключается ТОЛЬКО если в промпте есть liquid noun (water, coffee, milk, wine, oil, foam, steam, beer, juice, shampoo, perfume, ink). НЕ дублирует REFLECTION (геометрия отражения) и FABRIC (ткань).

TRANSPARENCY / REFRACTIVE OBJECT pack (универсальный — алиас: MEDICAL_TRANSPARENCY):

Покрывает ЛЮБОЙ полу-прозрачный объект где зрителю важна refraction physics. Scope расширен — два подраздела:

**Medical sub-scope** (Invisalign трей, зубные зеркала, контактные линзы, стеклянные ампулы, очки врача, капы — medical-grade vocab):
```
Invisalign clear aligner with realistic refractive index, thin polymer
transparency (medical-grade PETG), U-shaped thermoplastic dental tray with
14 tooth-shaped cavities visible, matte semi-transparent finish, subtle
highlights on edges, edges show natural plastic refraction of background
beige tone, fits to teeth contour, no flat shapes, no opaque overlay, no
glossy uniform surface.

Dental mirror with metal frame and reflective surface, brushed stainless
steel handle, mirror surface angled away from camera or angled to reflect
only soft overhead light, accurate inverse reflection geometry, no warping,
contact shadows where mirror touches tray surface, no human face reflected,
no mouth reflected, no ghost objects.

Glass ampule / vial: clear borosilicate glass, visible liquid meniscus,
thin wall refraction, label area solid (no readable text unless Nano Banana
2 EXACT STRING), light passes through liquid with subtle caustic on surface
below.
```

**Commercial sub-scope** (frosted-amber cosmetic bottle, perfume flacon, jewelry-display glass, crystal, любой translucent material — БЕЗ medical-grade vocab):
```
Frosted / amber / clear glass bottle with realistic refractive index, thin
wall refraction visible, visible liquid meniscus inside (если есть жидкость),
edges show natural glass refraction of background tone, soft highlights on
shoulder and base, subtle caustic shadow on surface below, label area solid
(no readable text unless Nano Banana 2 EXACT STRING), contact shadow where
bottle touches surface, no flat painted look, no opaque overlay, no glossy
uniform plastic surface.

Crystal / faceted glass object: angled facets refract light into subtle
prism caustics, reflections on each facet match scene angle, no rainbow
glow halo, no AI sheen, internal volume visible through clear sections.
```

Применение:
— ЗАМЕНЯЕТ REFLECTION SURFACES когда объект полу-прозрачный (medical OR commercial).
— Medical sub-scope использует «medical-grade PETG», «sterile», «borosilicate» — НЕ применяй для cosmetic/parfum (это путает парсер и при модерации Meta может прочитаться как implicit medical claim).
— Commercial sub-scope использует обычный glass / polymer vocab — НЕ применяй для зубных аппаратов / шприцов (потеряешь точность refraction для медицинских предметов).
— НЕ применять для непрозрачных инструментов (Cavitron handpiece, periodontal probe, металлический корпус) — для них хватает базового REFLECTION.
— Physics-блок (refraction, meniscus, caustic) универсален и работает в обоих sub-scopes.

**SUB-SCOPE ВЫБОР — явный decision tree (применяй ДО написания промта):**

Шаг 1 — категория объекта:
— Medical sub-scope ТОЛЬКО для: Invisalign трей, dental mirror, syringe / needle / vial, glass ampule с препаратом, контактные линзы, очки врача, элайнер, mouthguard.
— Commercial sub-scope для всего остального translucent material: ECOM bottles (frosted-amber supplement, perfume), WELLNESS supplements bottles, GREY vape glass cartridge / e-liquid bottle, jewelry display glass, crystal, любая бутылка / флакон / стекло без medical-procedural use-case.

Шаг 2 — если в нише есть risk implicit medical claim:
— Это **WELLNESS supplements** (БАДы, vitamins) — да, риск implicit drug claim → используй **commercial** (не medical), даже если визуально похоже на pharma-bottle.
— Это **GREY translucent product** (vape cartridge, CBD oil bottle, kratom) — да, риск implicit medical → используй **commercial**.
— Это **косметика / парфюмерия / jewelry** — нет medical risk → **commercial** дефолт.
— Это **реальный medical product** (Invisalign / dental mirror / syringe в клинике) — да, нужна точность → **medical**.

Шаг 3 — проверка по meta-policy-checker triggers:
— Medical vocab («medical-grade PETG», «sterile», «borosilicate», «pharmaceutical-grade») в supplement / vape / CBD сцене → активирует Meta «implicit drug claim» парсер → FAIL модерации.
— Commercial vocab в supplement / vape сцене → нейтрально → PASS модерации.
— Правило: если сомневаешься между sub-scopes — используй commercial. Medical только при явной medical-procedural use.

AI DISCLOSURE pack (обязательный overlay при использовании AI-likeness в коммерческой рекламе):

Когда подключать (триггеры):
— Профиль WELLNESS_HEALTH_RESTRICTED (USA gating) — supplements, hormonal coaching, sleep, ED, weight-loss.
— Профиль WELLNESS / MEDICAL_HEAVY где в кадре Soul ID реального founder / врача / эксперта.
— Профиль FINANCE с founder POV (crypto educator, fintech consultant, wealth coach).
— Профиль GREY_NICHE когда крео с AI-generated visual идёт в платный плейсмент Meta / Google / TikTok. По умолчанию даже vape гонится через Meta-paid с meta-policy-checker гейтом. Не-Meta каналы (Google / TikTok / др.) — только по явному запросу ученика.
— Любая ниша где Soul ID на реального человека генерирует talking-head / first-person endorsement в кадре.

Готовый блок для Nano Banana 2 EXACT STRING (bottom-third overlay, рендерится отдельным проходом, композитится в CapCut):

```
Bottom-third overlay band, lower 15% of frame, faint dark
translucent strip (40% opacity #1A1A1A), centered EXACT STRING text,
Inter Regular 38pt or equivalent ≤40pt, white #FFFFFF with soft
1px drop-shadow for contrast on variable backgrounds.

EXACT STRING text options (выбирай по контексту, не превышай 30-44 chars):
— "AI-assisted visual" (18 chars — минималистичный fallback)
— "AI-generated content" (20 chars — для не-founder сцены)
— "AI-assisted visual · {FounderName} (founder)" (≤44 chars — для talking-head с sign-off, используй когда хочешь явно атрибутировать)
— "AI-assisted visual · sign-off on file" (37 chars — компромисс между атрибуцией и privacy)
```

Соответствие регуляторике:
— CA AB 2655 (California, AI in political/commercial ads disclosure).
— IL HB 4762 (Illinois AI Generative Content disclosure).
— TX HB analogues и других US states.
— EU AI Act extraterritorial — применяется к рекламе видимой в EU, даже если рекламодатель в USA.
— FTC AI Disclosure Guidelines (2025-Q3 update).

Copy-safe правила в комбинации с AI DISCLOSURE pack:
— **WELLNESS_USA / WELLNESS / FINTECH / GREY с AI-visual → bottom 25% copy-safe** (вместо стандартных 20%) — место под AI disclosure overlay + CTA + brand-pointer одновременно.
— Top 15% copy-safe сохраняется как обычно (для caption sticker / autocaption).
— AI disclosure overlay не считается hook-overlay — он present от 0 до конца, не активирует V18.

Когда НЕ нужен AI DISCLOSURE:
— Product-only static без человека (Nano Banana 2 packshot бутылки, коробки, объекта).
— B-roll без человеческих лиц (cityscape, interior, object close-up).
— Mascot / illustrated character (не реальный человек) — **(не для minor-likeness, вкл. cartoon — см. meta-policy:291)**: маскот/мульт-персонаж с детской внешностью не освобождает от minor-likeness проверки.
— UGC-видео от реального актёра / founder снятое на телефон без AI-генерации (Higgsfield в этом случае не использовался) — **exemption только от AI-disclosure pack; живой actor как customer/patient всё равно требует FTC #ad / Actor portrayal-дисклеймер + не обходит Sensitive-Health (см. meta-policy:400)**.

Fallback при глитче EXACT STRING:
— 2-3 ретрая Nano Banana 2 → если текст всё ещё глитчит → text overlay в CapCut поверх готового видео (Inter Regular 38pt, bottom-third).
— CapCut overlay юридически эквивалентен Nano Banana 2 render (важен сам факт overlay, не модель).

Кросс-проверка в meta-policy-checker: с момента интеграции CANON-FROZEN OPEN-QUESTIONS Q26+Q27 этот pack явно проверяется и в скиле `meta-policy-checker` (раздел «AI-DISCLOSURE CHECK (EU AI Act + USA state laws)») и в финальном гейте PROMPT-4 (пункт 18). Раньше правило жило только здесь — теперь оно явный гейт на финальной выдаче. Если ученик сгенерировал AI-визуал без overlay и гео USA/EU — `meta-policy-checker` вернёт FAIL и крео не пройдёт в продакшн.

MEDICAL_ILLUSTRATION (Nano Banana 2 / GPT Image 2, T2I статика — образовательная медицинская графика, рентген, схема импланта в кости, диаграмма движения зуба, инфографика процесса):
```
Medical textbook illustration style, flat 2D vector or anatomical cross-
section, muted palette (warm cream background + dark navy lines + accent
red/blue for highlighted structures), clean line weight, labelled regions
with small numbered callouts (text via Nano Banana 2 EXACT STRING in
Cyrillic), no photoreal skin / no photoreal tissue, no shading attempt at
realism, no 3D render glow.

Для X-ray / radiograph: grayscale only, bone density gradient (cortical
bone bright white, medullary bone dim grey, soft tissue darkest), tooth
roots visible as elongated triangles, periodontal ligament as thin dark
line, NO color, NO photoreal mouth opening, NO patient face.

Для импланта в кости: cross-section view, jaw bone as cancellous lattice,
implant screw threads engaging bone, abutment + crown stacked above,
labels — текст через Nano Banana 2 (например «Имплант Ti-grade 4»,
«Циркониевый абатмент», «Керамическая коронка»).
```
ЗАПРЕЩЕНО: попытка photoreal через эту zone — выйдет страшная челюсть. Если нужна 3D-модель — отдельный кадр через Flux/Soul с MEDICAL_TRANSPARENCY pack и явным «3D dental model on tabletop, isolated, not human mouth». Только статика, только Nano Banana 2 / GPT Image 2. Не Soul, не Flux в этой зоне.

CULTURAL ACCURACY (нишевые костюмы, региональная архитектура, аутентичные артефакты, диаспоральный type face):

Подключай если в кадре ≥1 элемент cultural-specific. Шаблон для каждого элемента:

— Традиционная одежда: explicit garment name + region + era + 2-3 визуальных маркера + явный negative для частых путаниц.
  Пример: «Svan kabalakhi felt cap — cone-shaped grey wool hat with rounded peak, sits on the crown of the head, not a fez, not a papakha, not a wider Cossack hat».

— Архитектура: explicit landmark name + region + era + geometric markers + negative для частых glitch-замен.
  Пример: «Svaneti medieval defensive tower — square stone base, tapered top with crenellation, not generic European castle, not minaret, not Georgian church».

— Артефакты: explicit object name + material + use-context.
  Пример: «kvevri large clay amphora half-buried in Kakhetian wine cellar floor, not Greek amphora style, not Roman amphora».

— Local type face: явное «weathered local Caucasian features» / «East Asian features» / «Sub-Saharan African features» + конкретные морфологические дескрипторы (nasolabial folds depth, skin tone variation, eye shape). NB: «Caucasian» в английском = белый европеец, для жителей Кавказа писать «Caucasus region» или прямо «Georgian / Armenian / Svan local features».

— Безопасный fallback: «if unsure on detail, default to solid color and visible fabric weave texture rather than invented pattern / ornament / signage».

REGIONAL SUB-PACKS (специфические markers для конкретного гео — применяй когда в кадре ≥1 элемент из соответствующего региона):

**MENA (Middle East / North Africa):**
— Архитектура мечетей: 4 минарета для султанских / 2-1 для квартальных (число — статусный маркер, не путать); османская архитектура (центральный купол + полудомы, pencil-thin минареты с балконами); ablaq masonry (red-and-white voussoir alternation); İznik tile (cobalt blue / turquoise / oxblood / white, geometric / arabesque only).
— Орнамент: ИСКЛЮЧИТЕЛЬНО geometric / arabesque / каллиграфический (Куфическая / Насх / Сулюс). НИКАКИХ figurative human / animal forms.
— Hammam: мраморный göbektaşı (центральный камень), купол с göz penceresi (стеклянные «глаза» для света). НЕ western SPA (массажные столы / халаты / свечи / lavender oil).
— Hijab: modest headscarf полностью покрывает волосы и шею под подбородком, цвет нейтральный (бордо / тёмно-синий / кремовый), silk satin weave visible, no fashion-style loose wrap, no loose strands at forehead.
— Modest dress: длинный рукав, длина ниже колена / макси, обувь снимается при входе в мечеть.
— Skyscrapers Dubai: Burj Khalifa (needle-tipped spire рисующая Y-tiered tower, не Shanghai Tower / Petronas / minaret); Cayan Tower (helical 90-degree twist по всей высоте, не curved facade); Palm Jumeirah (palm-tree shape с центральным trunk + 17 fronds + crescent breakwater, не World Islands / Yas Island).
— Type face: Lebanese-Emirati / Khaleeji / Levantine / Maghrebi — конкретно по subnation. Generic Western executive face = FAIL для MENA-аудитории.

**Caucasian (Caucasus region):**
— Национальная одежда: Georgian chokha (узкая талия, газыри на груди), Svan kabalakhi (cone-shaped grey felt cap, не fez / не papakha), Armenian taraz.
— Архитектура: Svaneti defensive towers (square stone base + tapered top + crenellation, не castle / minaret); Armenian churches (cone-shaped roof, khachkar stone crosses); Georgian basilicas.
— Артефакты: kvevri (clay amphora half-buried, не Greek / Roman amphora style).
— Type face: «Caucasus region local features» — не «Caucasian» (в EN = белый европеец, ошибка). Прямо: Georgian / Armenian / Svan / Ossetian / Chechen.

**Slavic:**
— Cyrillic typography ОТЛИЧАТЬ по языку: русский (нет ї, є, ў, ё иногда), украинский (ї, є, і, ґ), польский (латиница с ą, ę, ł, ó, ś, ż, ź), белорусский (ў, і).
— Архитектура: Russian Orthodox (onion domes, kokoshniks); Ukrainian baroque; Polish Gothic / wood architecture; Belarusian baroque.
— Type face: восточно-славянский / западно-славянский — конкретно. «Russian features» / «Ukrainian features» — fine; generic «Slavic» = stereotypical мусор.

**Byzantine / Greek Orthodox / Mount Athos sub-pack (волна П.15, закрытие Q62) — для православных паломнических туров на Афон / Святую Землю:**
— Архитектура: Byzantine cross-domed basilica (Греция / Mount Athos), catholicon-style monastery (центральный храм монастыря), pendentive domes, Byzantine mosaic patterns gold-on-blue, narthex с фресками, peninsular landscape Mount Athos (узкий полуостров, лесистые склоны).
— Иконография: явно «Byzantine icon style, gold leaf background, formal frontal posture, halos» (НЕ Russian iconography с onion domes). Различай: Russian Orthodox = onion domes / kokoshniks; Greek Orthodox = cross-dome / Byzantine basilica.
— Type face: «Greek monk» / «Byzantine-era figure» / «Athonite monastic» — конкретно, не generic «Orthodox».
— Respectful framing обязателен: иконы и святые мощи как фон, не близкий план как «продукт в продаже». См. RELIGIOUS_TRAVEL preset + NEVER #23.

**East Asian:**
— Иероглифы по language: Mandarin (simplified vs traditional — разные регионы), Japanese (kanji + hiragana + katakana mix), Korean (hangul block syllables). НЕ путать.
— Архитектура: Japanese pagoda (multi-tier with curved eaves); Chinese temple (red+gold with dragon ornament); Korean hanok (low tiled roof + wood structure).
— Type face: Japanese / Korean / Han Chinese / Vietnamese — конкретно. «Asian» = размытый stereotype.

**SCOPE NOTE (волна П.8):** этот East Asian sub-pack покрывает **historical / touristic context** (храмы, традиционная архитектура, иероглифы). Для **modern corporate Asian** (Tokyo Marunouchi tower / Seoul Gangnam glass office / Singapore CBD / HK Central) — отдельный sub-pack ОТСУТСТВУЕТ (см. OPEN-QUESTION Q51). Если ученик заказывает B2B SaaS / FinTech / professional services для Asia Tier-1 банков — НЕ применяй pagoda / hanok / temple дескрипторы (читается как «иностранный sales rep, не свой»), запрашивай у Игоря расширение scope или используй generic modern office без специфики гео.

**South Asian (India / Pakistan / Bangladesh):**
— Одежда: sari drape по региону (Nivi / Bengali / Gujarati), sherwani men's formal, salwar kameez.
— Орнамент: paisley (Kashmiri), mehndi pattern, Mughal arches.
— Type face: North Indian / South Indian / Sikh / Bengali — конкретно.

**European traditional:**
— Architecture: explicit period (Romanesque / Gothic / Renaissance / Baroque / Belle Époque) с маркерами.
— Костюмы: explicit country + region + era (Bavarian Tracht ≠ Tyrolean ≠ Alpine generic).

Для каждого региона: explicit textual descriptors + явные negatives для частых glitch-замен + REFERENCE IMAGES обязательно (@image1) при ≥3 cultural маркерах в одном кадре.

Pack НЕ заменяет @image1 reference. Для ≥3 cultural маркеров в кадре @image1 ОБЯЗАТЕЛЕН (см. блок «@image1 workflow»).

WARDROBE CONSISTENCY (cross-shot и cross-creative):

ВАЖНО: Soul ID фиксирует ЛИЦО (черты, пропорции, асимметрию), но НЕ одежду. Через 3 крео в одном flight (P1 → P2 → P3) одежда героя поплывёт даже при правильно собранном Soul ID на 12 ракурсов, если не закрепить wardrobe явно.

Способы держать identical wardrobe через 3+ крео:

1. ОБЯЗАТЕЛЬНО — повторить FABRIC pack дословно в КАЖДОМ промте:
   — Полное описание ткани (charcoal grey wool / white cotton / weave pattern)
   — Цвет конкретный (charcoal grey, не просто grey)
   — Детали (no tie / top button open / lapel width / stitching colour)
   — Контактные сжатия (compression at collar / shoulder line)
   — Это не дубль — это анкер, без которого Veo / Kling начинают «творить».

2. ДОПОЛНИТЕЛЬНО — @image1 ref на готовый кадр P1 или статичное фото героя в нужном wardrobe:
   — В P2 / P3 описать «wardrobe matches @image1 (reference frame from P1)» или «Reference wardrobe: @image1. Anna in same outfit as @image1 across all shots.»
   — Работает с Seedance / Cinema Studio / Recast.
   — С Kling 3.0 — частично работает, через @image1 в motion-слое.
   — Veo 3.1 — @-refs НЕ поддерживаются. Wardrobe consistency только через Soul ID + жёсткое текстовое описание + готовиться к ретраям.
   — ВАЖНО: один @ref = одна роль. Если у тебя уже Soul ID на лицо — @image1 идёт ТОЛЬКО на wardrobe (T37 @-ref конфликт).

3. SEED-LOCKING НЕ работает для видео в Higgsfield на 2026 год (см. SEED-LOCKING matrix). Не обещай ученику «сессия одним прогоном с fixed seed» для видео.

GUARDRAILS:
— Никогда не полагайся ТОЛЬКО на Soul ID для одежды. Always copy FABRIC pack.
— Никогда не обещай ученику «съёмка одной сессией с fixed seed» если речь про видео — это галлюцинация фичи.

FABRIC / WARDROBE:
```
natural fabric weave visible, drape follows body contour, contact compression at touch points, gravity-driven folds, stitching detail at seams, no floating cloth
```

BACKGROUND SEPARATION:
```
subject separated from background via rim light, shallow DOF (f/1.8), color contrast between FG/BG, atmospheric perspective on distant elements, no morphing background
```

LIGHT CONSISTENCY (для multi-shot видео):
```
key light from {position}, {color temp K}, consistent across all shots, shadow direction matches throughout, no color temp drift
```

ВАЖНО — LIGHT DIRECTION CONSISTENCY ≠ LIGHT TEMPERATURE CONSISTENCY. Это два отдельных вектора, и в split-screen / before-after часто требуются разные:

**LIGHT DIRECTION CONSISTENCY** — одинаковое направление key light, position, shadow side между шотами. Применяй ВСЕГДА когда сцена выглядит как «один и тот же момент / локация».

**COLOR TEMP CONSISTENCY** — одинаковый Kelvin между всеми шотами. Применяй когда сторителлинг требует «единого освещения» (cinema look, единая локация). НЕ применяй когда контраст между шотами осознанный — например split-screen chaos→clarity, before→after, cold-office→warm-home.

Если намеренный contrast температур (4200K fluorescent chaos vs 5200K daylight clarity) — обозначь явно:
```
LIGHT DIRECTION consistency across shots (key from camera-left both halves),
COLOR TEMP intentionally differentiated for narrative — Shot A 4200K fluorescent,
Shot B 5200K daylight. Skin tone matches temperature of each shot but identity
remains consistent.
```

Это снимает риск T31/T32 («съехала температура») когда на самом деле это твой осознанный выбор. Иначе ученик / другой агент прочитает «LIGHT CONSISTENCY pack применён» = ожидает одинаковую температуру и не поймёт почему она разная.

REFLECTION SURFACES (зеркала/стекло/вода):
```
reflection shows correct mirror geometry, reflected elements match visible scene, no ghost objects
```

REFLECTION pack — transport sub-scope (для премиум-авто / motorbike / yacht / aviation):
```
— Car paint reflection (glossy metallic / matte / satin) — specular highlights match curve geometry
— Chrome / polished trim — distorted environment reflection matching scene angle
— Headlight optics (LED matrix / DRL) — clear polycarbonate with internal lens elements visible, realistic refractive geometry
— Glass / windshield — transparent + reflective layered, thin-wall refraction at edges
— Wheel rims — metallic specular, accurate inverse reflection
— Cool grade для technical / operating-room aesthetic, warm grade для luxury-cinematic
— Без HDR halo, без AI sheen, без painted-flat look на стекле
```

CHILDREN IN FRAME pack (для KIDS_PARENTS / SUBSCRIPTION_BOX / educational ниш):

Два-слойный guardrail почему AI-лица детей запрещены:
(а) Meta image-of-minor policy риск + риск жалобы родителя «использовали лицо моего ребёнка» даже если AI-generation, а не real photo.
(б) AI face-drift на детях жёстче — детские лица имеют меньше anchor-маркеров (мягче subsurface, нет pores / wrinkles), Soul ID и текстовое описание держат хуже взрослого. Каждый ретрай = +30% риск «странного» детского лица.

Разрешённые способы показать ребёнка в кадре:
— PoV сверху (parent perspective) — кадр от лица родителя на ребёнка
— Силуэт сзади — back-of-head only, no skin of face, no facial features
— ECU child hands / feet only — knee-down / shoulder-down framing (frame cuts above knee / below shoulder)
— Реальное фото статикой в CapCut поверх motion (с письменного согласия родителей) — это второй заход дизайнера, НЕ AI-generation

Запрет:
— БЕЗ AI-сгенерированных детей на фоне действия
— БЕЗ AI-рендера face/skin ребёнка ни при каких условиях

**DIASPORA-VARIANT для CHILDREN IN FRAME (волна П.15, закрытие Q63) — для KIDS_PARENTS-diaspora (RU-diaspora / Spanish-speaking-diaspora / другие):**
— Сцена в diaspora-контексте: US suburb kitchen / Berlin apartment balcony / Warsaw playground / Brooklyn brownstone interior. НЕ generic «русский дом» (это сигнал «не diaspora»).
— Multi-ethnic ребёнок: если мама second-gen RU-diaspora, ребёнок third-gen может быть mixed-race (отец местный). AI-генератор по умолчанию даст «Russian-looking» лицо — это НЕ отражает реальность diaspora-семей. Явно прописывай «mixed-race child» / «European-Latina mixed features» / «European-Asian mixed features» в зависимости от типичного состава семей диаспоры.
— Mix-language scene: ребёнок отвечает на EN / Spanish / German, мама переключает на RU. Это типичный bilingual-сценарий, показывает аутентичность diaspora-experience.
— Запрет «русские маркеры» в кадре которые читаются как стереотип (матрёшка на полке, шапка-ушанка, балалайка) — это отталкивает diaspora-маму как «понаехавшие». Используй cultural-relevant artifacts (фото бабушки и дедушки на холодильнике / русские книги на полке среди английских / borscht на плите рядом с pasta).
— Остальные правила CHILDREN IN FRAME (PoV / силуэт / hands-feet only / no AI face) применяются как обычно.
— БЕЗ «дорисовки» лица ребёнка при ретраях — если модель начинает дорисовывать, переписать описание жёстче: «child rendered as dark silhouette only, no skin tone visible, no facial features, back-of-head only, face fully obscured by motion blur or shadow»

Adults в кадре с children:
— Adult identity OK через Soul ID
— Child только PoV / silhouette / parts (knee-down / shoulder-down)
— Adult hand + child foot ECU — нормальный кейс (педагогический контекст). Adult hand явно больше child foot — clear scale relationship anchor для anti-merge.
— Ручной скан перед запуском: adult-child interaction в нейтральном педагогическом / спортивном контексте без двусмысленностей.

ANTI-AI-LOOK PACK:
```
visible skin pores and subsurface scattering, peach fuzz, natural asymmetry, micro-blemishes, no plastic skin, no oversaturation, no HDR halo, no glossy uniform surfaces, no AI sheen, natural highlight rolloff
```

───────────────────────────────────────────────────
INFOGRAPHIC / EDUCATIONAL / COMPARISON PACKS
───────────────────────────────────────────────────

Это НЕ photoreal паки. Это иллюстрации, схемы, карточки, диаграммы — то что Higgsfield генерит через Nano Banana 2 (статика) → опционально подгружается в Veo 3.1 / Kling 3.0 для мягкой анимации. См. §19B INFOGRAPHIC PIPELINE — там полный workflow.

Принцип: эти паки решают НЕ кинематографичные сцены, а **статичные образовательные / сравнительные / инфографические форматы**. Это 30-50% креативов для INFOBIZ / MEDICAL / LOCAL_SERVICE прайсовых / ECOM каталога / B2B SaaS funnel-explainer.

Все 5 паков ОБЯЗАТЕЛЬНО включают text-rendering правила §19A (EXACT STRING ≤5 строк, real-looking numbers, generic brand alias). Pipeline всегда: Nano Banana 2 (рендер базы) → опционально @image1 → Veo 3.1 / Kling 3.0 (мягкая анимация: подсветка, появление цифр, мини-зум, дыхание).

STYLE-SWATCHES-GRID PACK (4 превью стилей в одном кадре — для INFOBIZ карусели / лид-магнита «10 промптов в 4 стилях»):
```
2×2 grid layout, four equal-size square preview cards with subtle inner shadow, 8px rounded corners, label tag bottom-left of each card in lowercase sans-serif (Inter Regular 12px), generous white padding between cards (40-60px gap), single accent color for label tags and CTA only, dominant background white or pale neutral (#F8F8F6), no decorative borders, no gradients on cards themselves except where the style itself is "gradient", consistent lighting across all four previews (no mixed light temperatures), thumbnail-like crop (each preview shows ONE clear style sample, not collage), no text inside the preview thumbnails themselves
```
Когда применять: лид-магнит-крео «N промптов в M стилях», карусель-связка по визуальным стилям, образец стилевого набора для дизайнера. **EXACT STRING cap (волна П.6 уточнение):** header (1) + subline (1) + CTA (1) = **3 текстовых слота из обычного cap 5**. Style-labels (4 коротких ≤15 chars каждый, типа «продуктовый», «градиент») считаются ОТДЕЛЬНЫМ slot — итого **7 EXACT STRING ВСЕГО** для этого пака (исключение из cap 5). Pre-flight: каждый style-label ≤15 chars. Длинные обоснования стилей — в CapCut overlay post-prod, не в исходном кадре.
Когда НЕ применять: если в кадре нужны люди / motion / sequential narrative — это другие зоны.

COMPARISON-CARDS PACK (3-tier цена / тариф / продукт с региональными флагами — для LOCAL_SERVICE прайса / ECOM каталога / B2B SaaS pricing):
```
three vertical cards side-by-side with equal width and 16-24px gap between them, each card has a header label in uppercase sans-serif (Inter Bold 14-16px) centered top, a single hero icon or line illustration mid-card (40-60% of card height, 1.5-2px stroke line-art style, single color, no fills), price or core metric below icon as the largest type element (Inter Bold 28-36px), optional currency flag emoji or 16×12px flag illustration bottom-center, 1.5px outer border each card with subtle accent color for the middle "recommended" tier, clean white card backgrounds on neutral page background, NO drop shadows beyond 4-8% opacity, NO promotional badges or starbursts, ONE accent color total for the whole composition
```
Когда применять: «3 системы имплантов», «3 тарифа подписки», «3 пакета услуг», «3 уровня товара». EXACT STRING cap: 3 header labels + 3 prices + 3 optional sublines + optional flag = ≤12 строк ВСЕГО, но каждая микро-надпись считается. Reality-check: если >12 строк — режь sublines, оставь только header + price + flag.
Когда НЕ применять: 4+ тарифа (Nano Banana 2 ломает layout на 4+ vertical cards — переразбивай на 2 ряда или 2 креатива).
Generic brand rule: реальные имена тарифов клиента — generic alias («Базовая / Стандарт / Премиум», не «Vault Lite / Vault Pro / Vault Enterprise»).

**ВИЗУАЛЬНАЯ КОНСИСТЕНТНОСТЬ ИКОНОК — критично для медицины (волна П.12 после реального бага).**

Если на одной из 3 карточек icon = «продукт + контекстный объект» (например, имплант + зуб) — то на ВСЕХ 3 карточках должна быть та же логика (имплант + зуб + имплант + зуб + имплант + зуб). НЕ ДЕЛАЙ так что на «БАЗОВОЙ» нарисован «имплант + зуб», а на «СТАНДАРТ» и «ПРЕМИУМ» — только имплант без зуба: это **визуально сравнивает разные вещи** (один тарифа = «винт + зуб», другой = «только винт») и читается как «в БАЗОВОЙ дают зуб бонусом, в дороже — без зуба». Реальный риск для медицинской ниши: врач / регулятор предъявят «вы вводите в заблуждение что в дешёвом тарифе зуб есть».

Правило: **одна логика icon-композиции для всех 3 карточек**. Либо везде «продукт изолирован», либо везде «продукт + один и тот же контекстный объект». Без смешения.

**АНАТОМИЧЕСКАЯ КОРРЕКТНОСТЬ МЕДИЦИНСКИХ ИКОНОК (для MEDICAL_HEAVY и связанных ниш — волна П.12):**

Если в icon — медицинский объект (имплант / винир / брекет / шприц / ампула / коронка / прибор), он должен быть **визуально отличим от соседних медицинских объектов**:
- **Винир** — тонкая лепесткоподобная накладка на переднюю поверхность зуба (НЕ объёмная коронка). В icon: «thin shell-like overlay on tooth front surface, translucent edges, lepestok shape» (а не «full crown covering tooth»).
- **Коронка** — полное покрытие зуба сверху и по бокам (НЕ просто винир). Чётко отличается от винира объёмом.
- **Имплант голый** — только винт + abutment (заглушка сверху, плоская). НЕ показывай сразу с коронкой если описание = «имплант» (это два разных продукта).
- **Имплант с коронкой** — винт + abutment + корона сверху. Описывай явно как «implant + crown unit», не как «имплант».
- **Брекет** — кронштейн закреплённый на зубе с дугой ПРОХОДЯЩЕЙ ЧЕРЕЗ паз (не лежащей сверху). Для сравнения «брекеты vs виниры» — показывай зубной ряд с несколькими брекетами и дугой через все, не один брекет с дугой отдельно (это outlier, читается странно).

В промпте к Nano Banana 2 для медицинских icon: явно указывай **анатомический тип объекта** + ссылку на медицинский референс если возможно. Если генератор выдаёт «странный» объект (брекет с дугой не в пазу / имплант сразу с короной / винир толщиной с коронку) — переделывай. Это не «эстетика», это **доверие врача и регулятора**.

**Кросс-checking для MEDICAL_HEAVY icon-композиции — pre-flight волны П.12:**
1. Иконки 3 карточек consistent по логике (везде «продукт» / везде «продукт + объект»)?
2. Каждый медицинский объект анатомически отличим от соседних (винир ≠ коронка)?
3. Если объект может быть «бoss» (имплант + протез vs голый имплант) — это явно отражено в подписи или icon показывает именно то что в подписи?
4. Для сравнения «один объект vs другой объект» (виниры vs брекеты) — оба показаны **в одинаковом контексте** (оба отдельно ИЛИ оба в зубном ряду), не смешение «отдельная штука vs зубной ряд».

EDUCATIONAL-PROGRESSION PACK (timeline-прогрессия с анатомическими / медицинскими / техническими иллюстрациями — для MEDICAL_HEAVY стом «3 года без зуба → что с костью», тех-explainer «как работает алгоритм 1→2→3 этап»):
```
horizontal three-stage progression layout, three equal panels left-to-right with consistent illustration style across all three (cross-section anatomical illustration OR isometric technical diagram OR side-profile schematic), thin connecting arrow between panels (1-2px stroke, single accent color), time-stamp label below each panel in sans-serif (Inter Medium 16-18px: "6 months" / "1 year" / "3 years" OR "Step 1" / "Step 2" / "Step 3"), source-of-change arrow or callout from outside the panel pointing to the changing element, consistent color palette across panels (do not switch palettes between stages — only the changing element drifts in color/intensity), neutral background page, single brand accent color for arrows and labels only, clinically clean illustration register (NO 3D rendering, NO photo-real, NO cartoon)
```
Когда применять: MEDICAL_HEAVY (стом — bone loss progression, ortho — alignment timeline, dermo — sun damage years), LEGAL/M&A (процесс сделки 1→2→3 этап), B2B SaaS funnel (lead → MQL → SQL → customer). EXACT STRING: 3 stage labels + optional 3 sublines + 1 header + 1 CTA = ≤8 строк.
Когда НЕ применять: photoreal медицинское фото пациента (riskует violation Meta policy + локальный закон). Только illustration / cross-section / schematic.
КРИТИЧНО для MEDICAL_HEAVY: метки времени должны быть **наблюдаемыми изменениями в типичном случае**, не «гарантированный исход для пациента X». Эта иллюстрация ≠ before/after конкретного пациента.

INFOGRAPHIC-CHART PACK (bar / donut / funnel / metric-card / before-after metric — для ECOM результатов, B2B SaaS conversion-funnel, INFOBIZ outcome-numbers):
```
single dominant chart element occupying 50-60% of frame (horizontal bar chart OR donut chart OR funnel diagram OR large metric card), data labels in sans-serif numerals (Inter Bold for primary metric, Inter Regular for axis labels), MAX 5 data points per chart (3-5 bars / 3 funnel stages / 1-3 metric callouts), single accent color for highlighted data point, neutral grey for baseline data, generous white space (40%+ of canvas), header at top in sans-serif (Inter Bold 18-22px), single-line subline OR source-attribution under chart (Inter Regular 11-13px), NO 3D effects, NO gradients on bars/segments, NO drop shadows beyond 4% opacity, NO decorative chart-junk
```
Когда применять: ECOM «выросли X% за месяц», B2B SaaS «trial-to-paid funnel», INFOBIZ outcomes-карусель, CRISIS_EXPERT «процент клиентов получивших результат» (с substantiation!).
КРИТИЧНО: цифры должны быть **substantiated** — реальные данные клиента, не «придуманные впечатляющие». V18 anchor pricing rule распространяется на все цифры в чартах. «Conversion 47%» без объяснения базы = V18 fail.

**SUBSTANTIATION для multi-point чартов (волна П.15, закрытие Q50) — гибрид-правило:**
- (а) **Внутренние метрики одного клиента** (один чарт с 3-5 data points из CRM / Analytics / SLA-report клиента) → **один named source на весь чарт** OK. Пример header subline: «Cortex Q3 2025 internal audit». Все 5 data points в чарте покрыты этим одним источником.
- (б) **Бенчмарки рынка / индустриальная статистика** (один чарт с 3-5 data points из разных public sources) → **per data point substantiation** обязательна. Каждая цифра — своя ссылка / footnote («US Bureau of Labor 2024», «McKinsey Report Q1 2025», «Property Monitor Q3 2025»).
- (в) **Смешанный кейс** (часть из клиента, часть из бенчмарков) → разделяй визуально (две группы data points с двумя sub-headers с источниками). НЕ смешивай в одну кашу.
- Если у клиента нет ни внутреннего источника, ни public бенчмарка для данной цифры — `[GAP-substantiation]` placeholder в кадре, оффер идёт в LATER до получения данных от клиента. НЕ выдумывай.
EXACT STRING: 1 header + 1 subline/source + 3-5 data labels = ≤8 строк.
Generic brand rule: бренды конкурентов в funnel/comparison chart — generic alias («Existing Platform», «Legacy CRM»).

ANIMATED-DIAGRAM PACK (illustrator-style схема алгоритма / процесса / архитектуры с подсветкой узлов — для B2B SaaS explainer-карусели «как работает наш AI», CRISIS_EXPERT «3 шага юр-аудита», INFOBIZ «структура курса»):
```
flat-vector flowchart layout with rounded-rectangle nodes (8-12px corner radius) connected by directional arrows (1.5-2px stroke), MAX 5 nodes per diagram (3-5 узла, не 7+), node labels in sans-serif (Inter Medium 14-16px) centered inside node, single accent color for arrows and active-node highlight, neutral colors for inactive nodes (light grey fill + dark grey text), node icons as line-art (1.5px stroke, single color, no fills), clear directional flow left-to-right OR top-to-bottom (no backwards arrows except for explicit feedback loop), generous gap between nodes (60-80px), no decorative background, neutral page background, NO 3D, NO isometric perspective, NO gradient fills
```
Когда применять: B2B SaaS «как работает наш AI» / explainer onboarding, EDTECH «структура курса», CRISIS_EXPERT «3 шага юр-аудита», HIGH_TICKET «процесс работы». EXACT STRING cap: 1 header + 3-5 node labels + 1 CTA = ≤7 строк.
Когда НЕ применять: 7+ узлов (Nano Banana 2 ломается на сложных flowchart — разбивай на 2 диаграммы). Heatmap / sankey / treemap — НЕ через этот pack (Nano Banana 2 не держит).
Анимация в Veo 3.1: «node-by-node highlight reveal, soft 200ms fade-in per node, accent-color pulse on active node, arrow draw-on animation 300ms between stages, no camera move» — мягкое появление узлов по очереди.

GUARDRAILS для всех 5 INFOGRAPHIC packs (см. §19B PIPELINE — там полные правила):
— EXACT STRING ≤5 (HARD CAP, не floor) — кроме случаев где явно прописан другой лимит. Если в драфте >cap → режь sublines, footer, disclaimer (выноси в CapCut overlay post-prod).
— Real-looking numbers: substantiated (не «99% conversion», а «1247 sign-ups out of 4380 visitors = 28.5%»). Цифры из чартов / cards / metric callouts проходят V18 anchor pricing.
— Generic brand alias для UI / competitor names в любом из 5 паков (см. §19A KNOWN BRAND UI rule).
— NO photoreal лица пациентов / клиентов в EDUCATIONAL-PROGRESSION или INFOGRAPHIC-CHART — только illustration / silhouette / generic icon.
— Шрифт указать явно: «Inter Medium» / «Inter Bold» / «SF Pro Display» — иначе Nano Banana 2 ломается на decorative шрифтах.

VO FALLBACK PACK (voice-over в CapCut вместо Dialogue: блока — для Kling 3.0 с не-английской речью):

Когда применять:
— Нужен Kling 3.0 (camera verbs / photoreal motion / I2V), но речь героя — русская / украинская / казахская / грузинская / армянская / белорусская.
— Kling 3.0 не имеет Dialogue: блока, и Veo 3.1 не подходит по другим причинам (например, нужны @-refs которые Veo не держит, или multi-shot single-block).
— Talking content где Dialogue critical для смысла, но lip-sync крупно нельзя рендерить (Kling + русский язык + рот в кадре = T11 в 80% случаев).

Правила съёмки кадра под VO (рот зрителю не виден или нечитаем):
— Back-of-head — герой со спины, видны плечи и голова сзади
— ECU рук — только руки/жест в кадре, лицо вне фрейма
— Wide shot — герой в LS/ELS, рот не различим на дистанции
— Side-profile — герой строго сбоку, движение губ маскируется ракурсом
— ¾-action — герой в действии (печатает, готовит, идёт), внимание на действии не на губах
— PoV — кадр от первого лица героя, его лица не видно

Workflow:
1. В Higgsfield Kling 3.0 промпте — НЕ вписывай Dialogue: блок и НЕ описывай произносимую речь словами. Герой ничего не «говорит» в промпте.
2. Запиши voice-over отдельно: голос актёра / TTS / клиента — в любом аудио-редакторе.
3. Импортируй в CapCut: видео из Kling + аудио VO + опционально субтитры через CapCut auto-captions.
4. Если нужны точные тайминги речи под action — раскладывай action в Kling по секундам, потом подгоняй VO по action в CapCut.

В промпте под Kling добавь явную пометку в Caveats: «Речь идёт voice-over в CapCut, в Kling-промпте Dialogue не вписан намеренно (R14 fallback для не-английской речи)». Это страхует от того что другой агент / ученик подумает что ты «забыл» Dialogue.

VO FALLBACK — расширение для Kling 3.0 / Seedance 2.0 с русской / казахской / украинской речью КРУПНО в кадре:

Если Dialogue: на русском (или другом не-английском) + герой в CU / MCU с ртом крупно + модель Kling 3.0 / Seedance 2.0 (которые не держат русский lip-sync крупно):
— **Опция 1:** Talking head ТОЛЬКО в Veo 3.1 с Dialogue: блоком (R14). Veo держит русскую речь native, lip-sync на RU работает на 80-90% (4-5 ретраев).
— **Опция 2:** Talking head БЕЗ речи в Kling / Seedance + voice-over в CapCut (классический VO FALLBACK PACK).
— **НЕ генерировать рот крупно в Kling / Seedance с русской фонетикой** — lip-sync mismatch очевиден зрителю, читается как «AI и плохо сделано», убивает trust.

Конкретные жанровые случаи:
— Veo 3.1 RU dialogue: PRO-бюджет + Cinema Studio + один hero — OK. Закладывай 4-5 ретраев.
— Kling 3.0 + RU + back-of-head / ECU hands / side-profile / wide LS + voice-over CapCut — OK дёшево.
— Seedance 2.0 + RU + ECU action (без лица) + voice-over CapCut — OK дёшево.
— Kling 3.0 + RU + рот крупно (CU/MCU) — НЕ ДЕЛАТЬ. Переключай на Veo 3.1 ИЛИ на back-of-head / ¾-action.


## 3. VALIDATION (V1-V22, внутренняя проверка)

═══════════════════════════════════════════════════
VALIDATION (V1-V22, внутренняя проверка)
═══════════════════════════════════════════════════

Прогон перед выдачей каждого промпта. Ученику показываешь только результат:
✓ validation passed — если все V1-V22 OK
✗ V{N} fail: {причина} — если хоть один FAIL → переписывай, не выдавай.

V1. Intake собран (все 8 полей известны или дефолтнуты).
V2. Workspace выбран и совместим с моделью.
V3. Слои не смешаны (image/identity/motion раздельно).
V4. Aspect одинаковый сквозь все стадии.
V5. Camera verbs только в motion-слое.
V6. Лицо словами не описано, если есть Soul ID/Cast/ref. **Soul-ID pre-flight gate: если промт ссылается на Soul ID → строка «создай ID `{имя}` в кабинете Higgsfield (5-15 фото) ДО запуска» ОБЯЗАТЕЛЬНА в выдаче. Без неё Soul ID на бумаге = рандомное лицо.**
V7. Multi-shot video: shot count + duration + aspect в первой строке.
V8. Конкретика из vocab anchors вместо «cinematic/beautiful».
V9. Negative prompts только в моделях из matrix.
V10. [VFX:] только в Seedance. Dialogue: только в Veo. @refs по matrix.
V11. ≥2 персонажа — есть anchor + position map.
V12. PURPOSE=ad — hook ≤2s, паттерн H1-H7 назван явно. **6s-cram gate: single shot ≤6-7s → макс 2 beat (0-2s hook + 2-6s payoff); если >2 beat запрошено в один шот → раскадровка (multi-shot), не утрамбовка в один.**
V13. ECU/CU портрет → подключён PORTRAIT CU или ECU FACE pack.
V14. Руки/жесты в кадре → подключён HANDS IN FRAME pack.
V15. Photoreal → подключён ANTI-AI-LOOK PACK.
V16. Multi-shot video → подключён LIGHT CONSISTENCY pack.

V17. Контент-флаги ad creative (Hook + overpromise):

17a. Hook не зашивает сегмент Жертвы. Прогон ТОЛЬКО первых 5-10 слов hook (Shot 1 0-2s диалог / overlay). FAIL если активирует хоть один паттерн:
   — Возрастной маркер БЕЗ амбиционной второй части в первые 2s: «47 / 30 / поздно / не успею» — без явного «вернусь сильной / еду забрать / готова». Сравни «47, не была 22 года» = тот же эмоциональный уровень что «поздно ли в 30».
   — Ностальгия без результата: «вернуться к тому что было», «как раньше», «то что потеряла» — без явного «забрать обратно сильной».
   — Сравнение с провалом конкурента: «не как массмаркет», «не как Skillbox», даже если фактически верно.
   — Утомление словами: «устала», «снова не получается», «опять страшно», «сложно одной».
   — Виктимизация в pose / palette / tone БЕЗ слов:
     * Pose — ссутуленные плечи, опущенный взгляд, статика без жеста.
     * Palette — cold-desaturated-grey, faded-blue, muted desaturated.
     * Tone — minor key motivated music, потухший свет, «focused neutral» в холодной палитре.
   — Подтекст «возможно я не справлюсь»: «попробую всё-таки», «может получится», «надеюсь».
   — Если контраст до/после — оба состояния АКТИВНЫЕ (focused vs engaged), не «потухший → ожившая».

   Hook PASSED V17 если первые 5-10 слов содержат явный результат / обещание / амбицию / число / факт-якорь без эмоционального самобичевания. Допустимы возрастные / временные числа только если они сопровождаются позитивным действием в первые 2s.

ШАБЛОН-ТАБЛИЦА ЗАМЕН ЖЕРТВА → АМБИЦИЯ (готовый словарь — снимает 80% работы V17 при ручной переписке):

| Жертва-маркер             | Амбиция-замена                                                  |
|---------------------------|------------------------------------------------------------------|
| устал / устала            | контролируешь / видишь / делаешь / держишь в руках              |
| один тащит / одна тащит   | (удалить полностью, не нужно — заменить на инструмент/команду)  |
| страшно / снова страшно   | у тебя есть план / у меня есть метод / проверенный метод / 14 проектов |
| разочарованная / -ный     | переключаешься / выбираешь по-другому                            |
| сложно одной / одному     | (удалить + добавить инструмент / шаблон / систему)              |
| надеюсь / возможно / может| решаю / делаю / знаю / вижу                                     |
| разберу с тобой           | вижу где / даю N решений / считаю по P&L                        |
| поздно ли в 30 / 40 / 47  | (удалить возрастной маркер — заменить факт-якорем «4 недели / следующая дата») |
| не успею / уже не успею   | следующая дата / 4 недели / понедельник / N мест из M           |
| ты не одна / ты не один   | команда / группа / поддержка / 14 пациентов / N выпускниц       |
| мы понимаем               | (удалить — заменить инструментом / процессом / методом)         |
| снова не получилось       | следующий шаг / следующая попытка по методу X                   |
| долг душит / задолженность давит / разваливаюсь под долгом | взял долг под контроль / план реструктуризации / по 152-ФЗ списать N% (волна П.9 — кризисные метафоры) |
| всё горит / горю / горит срок | вижу что приоритет / 3 шага до дедлайна / план на 14 дней (волна П.9) |
| тонет в задачах / захлёбываюсь / накрывает | расставил приоритеты / 5 задач из 30 = 80% результата / метод по Эйзенхауэру (волна П.9) |
| задыхаюсь / нечем дышать (метафорически) | дышу спокойно по плану / 14-дневный sprint и пауза (волна П.9) |
| на грани / на пределе     | держу темп / методика устойчивого темпа / 4 спринта по 21 день (волна П.9) |
| ребёнок забывает русский (KIDS_PARENTS-diaspora) | за 30 дней ребёнок говорит по-русски сам (волна П.10) |
| у меня не получается научить (parent-victim) | профи-педагог берёт на себя — ребёнок играет (волна П.10) |
| бабушка плачет что внук не понимает | внук рассказал бабушке сказку — по-русски (волна П.10) |
| дети не отвечают на русском | игры на русском, в которые ребёнок просит играть ещё (волна П.10) |
| спаси русский у ребёнка   | прокачай русский ребёнка — без занудства (волна П.10 — «спаси» = катастрофическая лексика, аналог religious «спаси душу» FAIL) |

Применение: ученик / агент перед V17 hook-check открывает таблицу → находит в драфте hook любой маркер из левой колонки → подставляет замену из правой. Не творчество — механическая замена. Если ни одна замена не подходит по контексту — значит сегмент не должен слышать этот hook вообще (возврат в `ru-copywriter` или `offer-generator`).

**Расширение таблицы Волной П.9** — добавлены 5 кризисных метафор (душить / гореть / тонуть / задыхаться / на грани). Типичны для CRISIS_EXPERT / FINANCE-кризис (банкротство / долговая яма) / WELLNESS acute mental health. Без явной таблицы менее опытный prompt-runner ловил их только через расширительное применение пунктов 17a — теперь механическая замена доступна напрямую.

ВАЖНО: таблица не исчерпывающая. Если в hook есть подозрительный паттерн которого нет в таблице — прогон по полному списку 17a выше. Таблица для самых частых случаев.

17b. Для MEDICAL_HEAVY / FINANCE / HIGH_TICKET — словесные claims в Dialogue: блоке или текст-overlay через Nano Banana 2 НЕ содержат absolute promises («за 1 визит», «без металла», «гарантия», «100%», «-30% без anchor», «доход X USD»). FAIL → отправить в `meta-policy-checker` до выдачи.

При FAIL V17 — НЕ выдавай промпт. Объясни ученику почему fail + дай пример переписанного hook с амбиции. Если hook прислан из `ru-copywriter` — возвращай туда, ответственность за Жертву на этапе текста крео. Если hook собирался внутри промта — переписывай самостоятельно.

V17 проверяет ТОЛЬКО hook (первые 5-10 слов Shot 1 0-2s). НЕ проверяет последующие шоты. Если в Shot 3 кадр умиления / возвращения с амбицией — это OK.

**V17 для §19B INFOGRAPHIC (волна П.7).** В инфографических креативах «Shot 1 0-2s» = функциональный эквивалент = **первая строка EXACT STRING** (header чарта / прогрессии / диаграммы / тарифа). Это то что зритель читает первым за 1-1.5 секунды. Проверяй header через таблицу 12 пар маркер→амбиция точно так же как hook видеошоры:
— STYLE-SWATCHES-GRID header: «10 промптов которые упростят рутину» (PASS) vs «10 промптов которые спасут тебя от пресной работы» (FAIL по «спасут»).
— COMPARISON-CARDS header: «3 системы имплантов в Алматы» (PASS) vs «За что переплачиваешь в 3 раза?» (WARN — «переплачиваешь» подсвечивает потерю, проходит по contrast-reveal hook H5, не по Жертве).
— EDUCATIONAL-PROGRESSION header: «Прогрессия костной ткани при потере зуба» (PASS) vs «Что остаётся от кости когда годы уходят» (FAIL по эмоциональному «годы уходят»).
— INFOGRAPHIC-CHART header: «AML точность 94% на 1247 кейсах» (PASS) vs «Почему 87% не справляются с AML» (FAIL по «не справляются» — маркер беспомощности).
— ANIMATED-DIAGRAM header: «Как работает наш compliance engine» (PASS) vs «Как разобраться в этом хаосе одному» (FAIL по «одному» + «хаос» — двойной маркер).
— Если первый узел flowchart содержит маркер Жертвы — тот же FAIL.

V18. Anchor pricing для MEDICAL_HEAVY / FINANCE / HIGH_TICKET:

Если в промте через Nano Banana 2 рендерится цифра скидки (-N%, «было X стало Y», «дешевле на N», «0% рассрочка») ИЛИ в Dialogue: блоке устно произносится такая цифра — требуется substantiation от клиента (зафиксированная в брифе цена 30+ дней до запуска + наименование партнёра-банка для рассрочки + расчёт базы для процента).

Без substantiation → FAIL, отправить в `meta-policy-checker` и `reality-check-metrics` ДО выдачи промпта.

V18 срабатывает на anchor-цифры во ВСЕХ носителях кадра (Meta speech-to-text парсит одинаково с overlay):
— EXACT STRING через Nano Banana 2 (text overlay).
— **Устные claims в Dialogue: блоке Veo 3.1** (голос героя считывается speech-to-text парсером Meta так же как написанный текст).
— Voice-over в CapCut поверх Kling/Veo видео (через TTS / актёра — тот же speech-to-text парсинг).
— Субтитры если генерятся в CapCut auto-captions (двойной trigger).

Триггеры V18 в любом носителе: %, USD, ₽, ₴, тг, zł, EUR, цифра со словом «скидка», «было / стало», «дешевле на N», «0% рассрочка», «гарантия», **+ срок-обещание** («за N дней», «за N визитов», «за N часов восстановления», «через N недель результат», «вышел в свет на N день»), **+ процент с числом** («у 9 из 10», «67% клиентов теряют», «N% бухгалтеров»).

НЕ срабатывает на нейтральные ценники типа «60 USD/визит» без сравнения, скидки или обещания результата за срок.

Применение к Dialogue: блоку Veo 3.1:
— Прогоняй текст Dialogue: через тот же фильтр что и EXACT STRING.
— Если найден триггер — требуй substantiation у клиента или переписывай реплику без anchor-цифры.
— Пример FAIL: `Dialogue: "67% бухгалтеров теряют на этом"` — устный anchor % без substantiation → FAIL.
— Пример FAIL: `Dialogue: "Реабілітація — 5-7 день при типовому відновленні"` — устный срок-обещание для MEDICAL_HEAVY → FAIL. Переписать: `Dialogue: "Реабілітація залежить від випадку — обговорюємо на консультації"`.
— Пример PASS: `Dialogue: "За нашою статистикою 2024 у пацієнток 30-40 років з типовим випадком piezo-ринопластики соціальна активність відновлюється на 5-7 день у 78% спостережень"` — substantiated, период, возрастная группа, тип процедуры → PASS.

**ШАБЛОН-ТАБЛИЦА V18 FAIL → PASS** (готовые замены для самых частых кейсов — снимает 80% работы при ручной переписке):

| FAIL anchor | PASS replacement | Что применено |
|---|---|---|
| «до конца марта» (бесконечный диапазон) | «до 31 марта» (конкретная дата) | Замена fake-anchor срока на чёткую дату |
| «20% скидка» без substantiation | удалить % + «цена комплекса фикс до DD месяца» | Удаление anchor + замена на fixed-price с датой |
| «-30% на пакет» без substantiation | «пакет по фиксированной цене X до DD месяца» | Anchor → fixed-price |
| «67% клиентов» без proof | удалить число + «многие клиенты» / «большинство клиентов» | Удаление числа + качественный quantifier |
| «у 9 из 10 пациенток» без substantiation | «у большинства пациенток» / удалить и переписать через метод | Удаление сравнения + качественный quantifier |
| «47% of US adults» без NSF citation | «Most US adults» / «Many US adults» | Удаление точного % + soft quantifier |
| «33% Americans» без CDC citation | «1 in 3 Americans» с citation в footnote ИЛИ «many Americans» без числа | Citation или замена на качественный |
| «Stanford PhD» без diploma sign-off | «founder with neuroscience background» / «PhD neuroscientist» | Удаление institutional bind + general credential |
| «14 лет в инъекционке» без verified bio | «опытный врач-косметолог» (без числа лет) | Удаление точного срока |
| «I take this every night» (FTC endorsement) без declaration | удалить first-person + «science-backed formula» | Удаление endorsement → product claim |
| «clinically-formulated» без trial-reference | «science-backed» / «formulated by neuroscientist» | Удаление grade-claim → authority claim |
| «гарантия результата за N дней» | «средний срок видимого результата — N-M дней при типовом случае» | Удаление absolute promise → qualified statement |
| «доход X USD/мес» без proof | удалить число + «выручка зависит от ниши и трафика» | Удаление income claim |
| «0% рассрочка» без bank-partner | удалить + «рассрочка через банк-партнёр» | Удаление 0% без partner |
| «дешевле на N% чем конкурент» | удалить + «фикс-цена комплекса» | Удаление comparative claim |
| «до конца месяца / весь март» (бесконечный) | «до DD числа» | Конкретная дата |
| «вышел в свет на 5 день» | «средняя длительность реабилитации обсуждается на консультации» | Удаление промиса срока |
| «гарантированно» | удалить + переформулировать через «обычно» / «как правило» | Удаление absolute |
| **B2B Enterprise: «99.99% SLA» / «X-nines SLA» без contract** | «designed for 99.99% availability, with service credits per signed SLA» | Absolute SLA-commitment → qualified target |
| **B2B Enterprise: «10x faster than Datadog» / «N-x faster than {competitor}»** | удалить число + «built for cloud-native observability» ИЛИ оставить число только если named benchmark source + год + same-workload context | Comparative claim без same-workload benchmark = FAIL |
| **B2B Enterprise: «#1 alternative to {competitor}»** | удалить + «modern alternative for cloud-native teams» | Superlative + named competitor (disparagement risk) |
| **B2B Enterprise: «Free migration + 24-hour cutover»** | «Migration assistance included in Enterprise plan, scope defined per SoW» | Free как financial promise + 24h unrealistic для Enterprise = двойной FAIL |

Применение: ученик / агент перед V18 re-check находит в драфте anchor-маркер из левой колонки → подставляет PASS-замену из правой. Не творчество — механическая замена.

Если ни одна замена не подходит → возврат в `meta-policy-checker` за substantiation от клиента (документы / прайс 30+ дней / лицензия / clinical trial reference). Без substantiation промт не выпускается.

Таблица не исчерпывающая. Если в драфте anchor которого нет в таблице — прогон по 6-пунктовому чек-листу V18 + `meta-policy-checker`.

**MITIGATION PATTERN для V18 FAIL — перенос claim'а из Dialogue / EXACT STRING крео в Meta Ad Manager primary text:**

Если substantiation у клиента ЕСТЬ (документы / расчёт / research source с годом) — anchor-цифру можно вернуть в кампанию НЕ через крео, а через primary text. Преимущество: text-поле Meta Ad Manager более «терпимое» к substantiated claims чем video-creative (нет speech-to-text парсера который реагирует на устные anchors).

Шаги mitigation:
1. **Перенести claim** из Dialogue / EXACT STRING крео → в Meta Ad Manager primary text.
2. **Добавить substantiation в primary text + citation** в формате: «Average gross rental yields on Dubai apartments range 5-8% (Property Monitor Q3 2025). Historical performance, not a guarantee of future returns.» — обязательно named research source + год + disclaimer.
3. **В крео оставить только нейтральное product / service description** — без числа. Dialogue: устно говорит «stable USD yields» (нейтрально), EXACT STRING показывает «CONFIDENTIAL VALUATION · FIXED TIMELINE» (без числа).
4. **PASS V18 только при условии что substantiation реально предоставлен** (документ 30+ дней / clinical trial / audit attestation / research source named + год). Без документа — даже text-поле не выпускается с цифрой.

Когда применять mitigation vs полное удаление:
— **Mitigation (text+disclaimer):** если substantiation у клиента ЕСТЬ и audience уже частично прогрета (warm / retargeting / lookalike).
— **Полное удаление (по таблице FAIL→PASS):** если substantiation НЕТ или audience полностью холодная (TOF) — text-поле читают <30% холодной аудитории, claim не работает; зато snowflake-эффект Meta scrutiny на «substantiated в тексте, но в крео тоже всплыло» = риск flag'а.

GUARDRAIL: НЕ переносишь claim в text если в крео он ВСЁ ЕЩЁ присутствует (visual claim + text claim = двойной trigger Meta). Mitigation работает только когда из крео claim полностью удалён.

V19. verify_with_client check для biographical / founder / endorsement claims:

Срабатывает когда в Dialogue: блоке Veo / voice-over в CapCut / EXACT STRING через Nano Banana 2 присутствуют ЛЮБЫЕ персональные утверждения о founder / expert / враче / эксперте:

— Академические credentials: «Stanford PhD», «Harvard MD», «14 лет в инъекционке», «выпускник Гарварда», «MBA INSEAD».
— Профессиональный опыт с конкретикой: «пересобирал 14 проектов», «провёл 200 операций», «обучил 1000 человек».
— Endorsement first-person: «I take this every night», «я сам пью этот БАД», «я лечусь у себя в клинике», «my morning ritual».
— Биография героя: «я переехал», «у меня было», «я сам прошёл через это», «my journey from X to Y».

Pre-flight требование ДО выдачи промта:
1. Sign-off от клиента / founder / эксперта в письменном виде на конкретную формулировку.
2. Supporting documents в зависимости от типа claim:
   — Academic credential → диплом / университетская страница / LinkedIn verified.
   — Endorsement first-person («I take this») → отдельная декларация founder + supplement-facts на упаковке + соответствие FTC Endorsement Guides.
   — Клиентский кейс «обучил 1000 человек» → customer list под NDA + методика подсчёта.
   — Medical-procedural опыт → лицензия + клиника + страховка.

Если sign-off + документы отсутствуют → промт НЕ выпускаешь. Возврат в `creative-brief-writer` или к клиенту за verification. В Caveats явно: «V19 trigger — требует verify_with_client до запуска».

Регуляторные требования (почему этот шаг обязателен):
— FTC Endorsement Guides (USA) — endorsement без honest experience = deceptive advertising violation.
— EU AI Act extraterritorial — AI-generated likeness конкретного человека требует явной декларации в кадре + sign-off.
— USA state laws (CA AB 2655, IL HB 4762, TX HB-аналоги) — AI likeness в commercial use требует консента.
— Закон РФ / РК / UA о рекламе медуслуг — credentials врача только при наличии лицензии.

Безопасный fallback при отсутствии sign-off:
— «Stanford PhD» → «founder with neuroscience background»
— «14 лет в инъекционке» → «опытный врач-косметолог» (без числа лет)
— «I take this every night» → удалить first-person, оставить «science-backed formula» / «evidence-based ingredients»
— «обучил 1000 человек» → «обучил сотни специалистов» (без точной цифры)

V19 РАСШИРЕННЫЕ ТРИГГЕРЫ — по носителю claim'а:

V19 срабатывает в любом носителе кадра, где претензия о реальном человеке появляется. Не только Dialogue: блок Veo 3.1 — все четыре носителя одинаково триггерят:

| Носитель | Что триггерит V19 | Что требуется до запуска |
|---|---|---|
| **Dialogue: блок (устная речь Veo 3.1)** | Любой first-person / biographical / endorsement claim в реплике героя | Sign-off на конкретную формулировку реплики + supporting document (диплом / лицензия / LinkedIn verified / clinic registration) |
| **EXACT STRING overlay (Nano Banana 2)** | Текстовый overlay с credentials / endorsement / years («ex-McKinsey · MBA INSEAD», «12 лет в Berlin», «8 years brokering in Dubai») | Sign-off + LinkedIn screenshot / Anwaltskammer Eintragungsbescheinigung / Higher Education diploma / professional license number |
| **Meta primary text (Ad Manager)** | Тот же claim перенесён в text для V18 mitigation — V19 проверка тоже применяется | Substantiation + sign-off на текст-вариант формулировки (она может отличаться от устной — отдельный sign-off) |
| **Visual claim (показ официального документа в кадре)** | Демонстрация диплома / лицензии / сертификата / премии в кадре | Официальный документ ОБЯЗАТЕЛЕН (не PSD-mockup) + sign-off на использование visual + проверка что номер лицензии не expired |

Если claim есть в ДВУХ носителях одновременно (Dialogue + overlay; Dialogue + Meta text) — sign-off на КАЖДУЮ формулировку ОТДЕЛЬНО. Формулировка устной речи ≠ формулировке overlay ≠ формулировке Meta text. Sign-off на одну не покрывает остальные.

Multi-creative flight (P1 + P2 + P3 одной кампании): V19 sign-off для КАЖДОГО крео отдельно. Sign-off P1 НЕ покрывает P2/P3 даже если использован тот же Soul ID — формулировки реплик разные.

V19 ≠ V18: V18 ловит anchor pricing / curative claims в копи. V19 ловит persona-claims о реальном человеке. Часто триггерятся одновременно — проверять оба.

V19 brand-association trigger (real brand name в attribution):

Если в Dialogue: или EXACT STRING упоминается real brand name в формулировке attribution founder («ex-Coinbase», «ex-McKinsey», «ex-Google», «former JPMorgan analyst») — это double trigger: V19 sign-off на формулировку + brand association risk check.

Meta speech-to-text парсит real brand name в Dialogue как brand association — даже если претензия «я работал ТАМ», Meta может прочитать как implicit endorsement / partnership с конкурентом и flag креатив.

Mitigation pattern:
— В крео (Dialogue + EXACT STRING + visual) — generic alias: «major US exchange» / «top-tier consulting firm» / «leading tech company» / «one of the largest banks in EU».
— Real brand name произносится ТОЛЬКО в Meta primary text (text-поле tolerance выше) + LinkedIn / лендинг bio. Там это OK как factual employment history с verified screenshot.
— Если клиент настаивает на real brand name в крео — требует письменное согласие brand (нереалистично) ИЛИ клиент письменно принимает риск flag.

Применимо к: FINTECH (ex-Coinbase / ex-Binance), консалтинг (ex-McKinsey / ex-BCG), tech (ex-Google / ex-Meta), банкинг (ex-JPMorgan / ex-Goldman), любые prestigious brand name в founder attribution.

ГЕО-СПЕЦИФИЧЕСКИЕ ДИСКЛЕЙМЕРЫ (для подвала лендинга, не в крео):

Сами по себе НЕ зашиваются в видео-крео (V18 / V19 покрывают то что в кадре). Но при выдаче пачки промтов клиенту — ОБЯЗАТЕЛЬНО напомни список в Caveats: «следующие дисклеймеры идут на лендинг (волна Н), не в крео — без них рискуете local-law violation».

Чек-лист по странам:
— **KZ медуслуги**: «Имеются противопоказания, проконсультируйтесь со специалистом» + номер лицензии Минздрава РК + ИИН клиники. Закон РК «О рекламе» ст. 21.
— **РК финансовые услуги**: лицензия АРРФР + warning о рисках инвестиций. Закон РК «О рынке ценных бумаг».
— **UA медуслуги / юр.услуги**: лицензія МОЗ / Anwaltskammer-аналог + предупреждение о противопоказаниях. Закон України «Про рекламу» ст. 21.
— **RU медуслуги**: лицензия Росздравнадзора + «имеются противопоказания». ФЗ «О рекламе» ст. 24.
— **RU финансовые услуги**: предупреждение о рисках + лицензия ЦБ РФ. ФЗ «О рекламе» ст. 28.
— **UAE financial advice**: SCA / DFSA / FSRA license + DIFC / ADGM jurisdiction указание + «advisory services subject to engagement terms».
— **UAE real estate**: RERA license + DLD broker registration + «historical performance, not guarantee» для yields claims.
— **EU AI Act extraterritorial**: AI-content disclosure в кадре или подвале при использовании AI-likeness реального человека. EU AI Act применяется ко всем рекламам показываемым EU-аудитории, даже если company не в EU.
— **EU professional services (DE / FR / IT)**: BRAO § 43b (Sachlichkeitsgebot) — никаких сравнений «лучший» / «единственный»; Erfolgshonorar запрещён в DE по § 49b BRAO; в FR Loi Murcef. Atomtenkammer / Notarkammer registry number в подвале.
— **USA supplements**: FDA disclaimer «These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.»
— **USA endorsements**: FTC Endorsement Guides disclosure «#ad» или «paid partnership» в подвале + #sponsored визуально различимое.
— **USA financial**: SEC / FINRA disclaimers (для investment advice); state-by-state для insurance / mortgage.
— **CA / IL / TX AI likeness**: state-level consent declarations (CA AB 2655, IL HB 4762, TX HB-аналоги) — отдельно от FTC.

GUARDRAIL: при выдаче промтов агент НЕ зашивает эти дисклеймеры в EXACT STRING крео (это перегрузит кадр и снизит CTR). Только напоминание в Caveats клиенту: «следующие дисклеймеры — на лендинг, проверь с юристом по гео».

V22. Гейт длины копи-блока (HARD FAIL — Higgsfield обрезает длинные промты, см. A3):

Перед выдачей замерь длину копи-блока (вместе с NEGATIVE PROMPT для статики):
— Статика (Nano Banana 2 / Soul / Flux): ≤~1500 символов.
— Видео (Seedance / Veo / Kling / WAN): ≤~2500 символов.

Превышен → НЕ выдавай как есть. Сначала компактируй: identity свернуть до якорей (волосы / брови / глаза / нос / губы / овал + 1 примета вместо абзаца) ИЛИ заменить словесное лицо на Soul ID / @image1. Если после компактирования всё ещё >лимита — режь сцену (меньше beat / разбивай на отдельные шоты) ДО выдачи. Выдаёшь ученику только версию, влезающую в лимит — НЕ заставляешь резать руками (A3).

Это HARD FAIL: длинный промт молча обрежется в Higgsfield и сгенерит мусор — ученик заплатит за кредиты и не поймёт почему. V22 ловит это до выдачи.


## 4. FAILURE CATALOG T1-T39 + QUICK DIAGNOSIS INDEX

═══════════════════════════════════════════════════
FAILURE CATALOG T1-T39 (диагностика)
═══════════════════════════════════════════════════

Активируется ТОЛЬКО по запросу ученика: «у меня сломалось», «6 пальцев», «лицо плывёт», «hook не зашёл», «шот 3 не вытянул». НЕ выдавай весь каталог стеной.

Логика (A2): найди T-номер в Quick Diagnosis Index → выдай T-диагноз ОДНОЙ строкой сверху → затем ПОЛНЫЙ готовый промт под копирку с уже вшитым фиксом (один код-блок по формату Output). НИКОГДА не проси ученика «заменить фрагмент / блок X на этот» или «остальное не трогай» — всегда цельный промт одним блоком.

ЛИЦО

T1. Лицо плывёт между кадрами.
   Diag: нет Soul ID/Cast, нет ref image, описание лица словами.
   Fix: создать Soul ID или дать @image1. Убрать описание лица.

T2. Лицо асимметрично сверх нормы.
   Diag: нет anchor или противоречивое описание.
   Fix: «natural facial symmetry with subtle asymmetry, eyes aligned horizontally».

T3. Кожа пластиковая / AI-look.
   Diag: нет позитивных текстурных дескрипторов из SKIN zone.
   Fix: добавить «visible skin pores, subsurface scattering, micro-texture, peach fuzz». Снять «perfect skin».

T4. Кожа слишком зернистая / шум.
   Diag: переборщил с film grain + ISO + texture.
   Fix: уменьшить film stock до Vision3 250D. Убрать «heavy grain».

ГЛАЗА

T5. Глаза смотрят в разные стороны / cross-eyed.
   Diag: gaze не прописан явно.
   Fix: «both pupils centered, gaze locked on [target], no eye drift».

T6. Глаза без catchlight, мёртвые.
   Diag: не прописан источник света для глаз.
   Fix: «catchlight from key light at [position], wet film on eyeball, defined iris pattern».

T7. Зрачки разного размера.
   Diag: AI random.
   Fix: «matched pupil dilation, symmetric iris size».

T8. Брови искажены или отсутствуют.
   Diag: occluded by hair или модель пропустила.
   Fix: «visible eyebrow hair with natural direction, brow ridge defined».

ГУБЫ / ЗУБЫ

T9. Губы пластиковые / uniform glossy.
   Diag: «glossy lips», «perfect lips» или нет текстуры.
   Fix: «visible lip texture, vertical micro-lines, natural color graduation, moisture sheen not glossy».

T10. Зубы glow / неестественно белые / extra teeth.
   Diag: «shiny white teeth», «perfect smile».
   Fix: «natural enamel translucency, slight yellow tint, 8 upper / 8 lower visible, gum line natural».

T11. Рот раскрыт во время речи неправильно.
   Diag: Veo + диалог не в Dialogue: блоке.
   Fix: вынести диалог в Dialogue: «...» блок.

ВОЛОСЫ

T12. Волосы как шлем / rigid helmet.
   Diag: «perfect hair», «shiny smooth hair».
   Fix: «individual strand definition, baby hairs at hairline, natural hair direction, flyaways, visible scalp».

T13. Волосы не двигаются в видео.
   Diag: motion-слой без описания вторичного движения.
   Fix: «hair responds to motion with secondary movement, strands separate during head turns, motion blur on fast moves».

РУКИ / ПАЛЬЦЫ (killer-категория)

T14. 6+ пальцев / сросшиеся пальцы / extra hand.
   Diag: руки в кадре + нет явного описания + длинный промпт.
   Fix: «five fingers per hand, correct anatomical proportions, no merged fingers, no extra appendages». В ECU — описать каждый палец по позиции.

T15. Кисть выглядит резиновой.
   Diag: нет vocab текстуры для рук.
   Fix: «visible knuckle creases, tendon detail, nail beds defined, skin texture matches face».

T16. Жест нечитаемый.
   Diag: «elegant hand gesture» без конкретики.
   Fix: описать пальцы — «thumb extended, index pointing, middle/ring/pinky curled, palm facing camera».

ТЕЛО

T17. Конечности удлинены / укорочены / искажены.
   Diag: сложные позы + нет anatomical anchor.
   Fix: «natural body proportions, joints anatomically placed, no morphing limbs». В сложных позах — давать ref image.

T18. Уши асимметричные или отсутствуют.
   Diag: occluded by hair + не упомянуты в промпте.
   Fix: «both ears visible (or symmetrically hidden by hair), natural ear shape and proportion».

ФОН

T19. Фон морфится между кадрами видео.
   Diag: не указана static background + длинный промпт.
   Fix: «background remains static across all frames, no element morphing, depth layers stable».

T20. Тени не совпадают с источником света.
   Diag: нет explicit light direction в image-слое.
   Fix: «shadows fall [direction] matching key light at [position]».

T21. Отражения в зеркале/стекле неверные.
   Diag: AI не считает геометрию.
   Fix: «reflection shows correct mirror geometry, reflected elements match scene». Если сложно — убери reflective surface.

T22. Объекты на фоне сливаются с передним планом.
   Diag: нет separation tools.
   Fix: «subject separated from background via rim light, shallow DOF (f/1.4-f/2.8), color contrast between FG and BG».

T23. Текст на знаках / одежде = глитч.
   Diag: модель не умеет рендерить текст (кроме Nano Banana 2).
   Fix: переключись на Nano Banana 2: «EXACT STRING» in {font}. Если не важен — «no readable text on signs, abstract graphics only».

   ПОДКЕЙС UI MOCKUP (экран дизайна / интерфейс / календарь / Figma / dashboard):
   «abstract block shapes» теряет смысл — зритель не поймёт что на экране.
   Правильно: «recognizable interface mockup via solid colored rectangles
   and thin border lines, no text glyphs, layout reads as [календарь /
   Figma / dashboard / portfolio] through block geometry alone».
   Для календаря: «calendar grid with darker filled time blocks indicating
   busy hours, no specific event text, recognizable as a weekly calendar».
   Для портфолио: «3 distinct UI thumbnails on project board, each with
   recognizable layout sections (header bar / grid / chart shape), no text».
   Для full dashboard / CRM / SaaS — см. §19A UI MOCKUP PIPELINE (2-шаговый Nano Banana 2 → @image1 → Veo).

   ПОДКЕЙС КИРИЛЛИЦА В ВИДЕО (этикетка / вывеска / текст на упаковке в видео-модели):
   Видео + кириллица на этикетке = глитч даже с @image1 (текст плывёт по кадрам — Nano Banana 2
   держит текст в одном статик-кадре, но видео-модели регенерят его каждый кадр и он морфится).
   Fix: рендери видео БЕЗ читаемого текста на товаре («no readable text on label, plain surface»)
   + накладывай текст/этикетку оверлеем в CapCut поверх готового видео. Либо — если текст ОБЯЗАН
   читаться в кадре — статик через Nano Banana 2 (не видео). @image1 один кириллицу в видео НЕ держит.

T24. Логотипы / бренды галлюцинируют.
   Diag: дефолт AI.
   Fix: «no logo hallucination, plain product surfaces». Или подай ref.

ТКАНЬ / ОДЕЖДА

T25. Ткань «плавает» над телом, не касается.
   Diag: нет описания контакта.
   Fix: «fabric drapes following body contour, contact points compress fabric, gravity-driven folds».

T26. Pattern на ткани ломается на изгибах.
   Diag: AI не следит за surface curvature.
   Fix: «pattern follows fabric curvature, no pattern warping at seams». Сложный pattern — выбрать solid color.

T27. Одежда меняется между шотами видео.
   Diag: identity-слой смешан с motion.
   Fix: закрепить wardrobe в identity-слое или через @image1. Не описывать одежду в motion-слое.

ФИЗИКА

T28. Motion blur где не должно быть / не там.
   Diag: глобальное «motion blur» без контекста.
   Fix: «motion blur only on fast-moving elements, static elements sharp, shutter speed equivalent 1/48s».

T29. Refraction (вода/стекло/очки) ломается.
   Diag: сложная оптика, модель не считает.
   Fix: «glasses lenses show natural refraction of background, frame visible». Критично — Soul с ref image, не motion.

T30. Гравитация нарушена (волосы/одежда не вниз).
   Diag: нет gravity anchor.
   Fix: «hair and fabric respond to gravity downward, natural weight on suspended elements».

СВЕТ

T31. Цветовая температура съезжает между шотами.
   Diag: light setup не закреплён.
   Fix: закрепить «color temperature {K}, key light from {position}, consistent across all shots».

T32. Skin tone shift (лицо то жёлтое, то синее).
   Diag: смешанный свет без явного описания.
   Fix: «neutral white balance on skin, key light {temp K}, no color shift across frames».

T33. HDR halo вокруг ярких объектов.
   Diag: модель добавляет artistic glow.
   Fix: «natural highlight rolloff, no HDR halo, soft clipping on bright areas».

IDENTITY DRIFT

T34. Персонаж в Shot 1 ≠ персонаж в Shot 5.
   Diag: motion-слой описывает лицо словами, нет Soul ID.
   Fix: Soul ID на героя. В motion только имя ID, без описаний.

T35. Multi-character перепутаны (A делает действия B).
   Diag: нет anchor + position map.
   Fix: применить Multi-Character Anchoring (anchor + position map + явные имена в каждом действии).

AD CREATIVE

T36. Hook не работает / scroll past.
   Diag: первый шот без H1-H7 паттерна.
   Fix: переписать Shot 1 под один из H1-H7. Удалить setup-кадры.

T37. @-ref конфликт.
   Diag: один @ref нагружен ≥2 ролями.
   Fix: один @ref = одна функция. Разделить на @image1/@image2.

T38. Infographic glitch — text wrap fail / layout drift / decorative-junk.
   Diag: в инфографическом креативе (один из 5 паков §19B) текст переносится не там / падают decorative шрифты вместо указанного / >5 EXACT STRING на креатив / chart-junk (тени, градиенты, 3D) который не запрашивался / data points >5 на чарт / узлы >5 на flowchart.
   Симптомы: «не читается за 1.5s», «много мусора», «цифры в разнобой», «строки не помещаются», «шрифт стал курсивным сам по себе».
   Fix: переключи на §19B PIPELINE (Nano Banana 2 only). EXACT STRING ≤5 (HARD CAP). Шрифт указать явно (Inter Medium 14px / Inter Bold 28px / SF Pro Display 18px). MAX 5 data points на чарт. MAX 5 узлов на flowchart. Если >5 — режь до 5 или разбивай на 2 креатива. Sublines / footer / disclaimer → CapCut overlay post-prod.

ПРОДУКТ

T39. Продукт не той формы / масштаба (бутылка раздута / тюбик стал банкой / товар занял весь кадр / пропорции «гулять»).
   Diag: продукт описан словами без @image1 product-ref ИЛИ @image1 есть, но без scale-anchor — модель не знает реальный размер и масштабирует произвольно (один @image1 сам по себе масштаб НЕ держит, форму держит частично).
   Fix: @image1 product-ref (Cinema Studio / Seedance / Marketing Studio с image ref) ОБЯЗАТЕЛЕН + scale-anchor в кадре: рука / монета / стандартный объект рядом ЛИБО явно «product occupies ~30% frame height» + «product matches reference proportions, no size exaggeration, true-to-life scale». Без scale-anchor @image1 фиксирует этикетку/форму, но не размер — товар всё равно «дышит» по кадру. Кириллицу на этикетке словами НЕ описываешь (T24); в видео текст на товаре не читаемый + оверлей CapCut (см. T23 подкейс кириллица-видео).

═══════════════════════════════════════════════════
QUICK DIAGNOSIS INDEX (один экран)
═══════════════════════════════════════════════════

Фраза ученика → T-номер. Дальше — Fix из каталога.

Лицо плывёт                    → T1
Лицо асимметрично              → T2
Кожа пластиковая               → T3 + ANTI-AI-LOOK PACK
Кожа зернистая                 → T4
Глаза косят                    → T5
Глаза мёртвые                  → T6
Зрачки разного размера         → T7
Брови потеряны                 → T8
Губы пластик                   → T9
Зубы glow                      → T10
Рот при речи кривой            → T11 (переключи на Veo + Dialogue:)
Волосы шлем                    → T12
Волосы не двигаются            → T13
6 пальцев / сросшиеся          → T14
Кисть резиновая                → T15
Жест нечитаемый                → T16
Конечности удлинены            → T17
Ушей нет                       → T18
Фон морфится                   → T19
Тени неправильно               → T20
Отражения врут                 → T21
Объекты слипаются с фоном      → T22
Текст на знаках глитч          → T23 (переключи на Nano Banana 2)
Логотип галлюц                 → T24
Одежда плавает                 → T25
Pattern ломается               → T26
Одежда меняется между шотами   → T27
Motion blur не там             → T28
Очки/стекло врёт               → T29
Гравитация нарушена            → T30
Свет съезжает между шотами     → T31
Skin tone скачет               → T32
HDR halo                       → T33
Identity drift                 → T34
Multi-char перепутаны          → T35
Hook не зашёл                  → T36
@-ref конфликт                 → T37
Продукт не той формы / масштаба / бутылка раздута / товар на весь кадр → T39 (@image1 + scale-anchor)
Hook звучит как Жертва         → V17 fail, пересобрать Shot 1 без маркеров
Anchor pricing без substantiation → V18 fail, в meta-policy-checker
UI mockup в видео-модели       → T23 → §19A UI MOCKUP PIPELINE
Инфографика «скучная» / схема не читается / chart-junk / >5 строк / >5 data points / decorative шрифт → T38 → §19B INFOGRAPHIC PIPELINE
Нужна 2×2 grid стилей / 3 тарифа / прогрессия / chart / flowchart → §19B PIPELINE (один из 5 паков)
Креатив красивый но «не продаёт оффер» / зритель не помнит WHAT → V20 fail → §20 OFFER → STORY MAPPING (5 шагов + 6 арок)
Один креатив пытается показать 3 концепта одновременно → V20 fail → разбивай на 3 креатива в пачке
Comparison-оффер (3 тарифа) показан как video с героем → V20 fail → §19B COMPARISON-CARDS static
Process-оффер (5 этапов) в single-shot без beats → V20 fail → multi-shot с Shot 2/3/4 на каждый этап ИЛИ §19B ANIMATED-DIAGRAM
Креатив выглядит «как реклама» / зритель скроллит за 1.5s / Soul ID slick / «AI-actor look» → V21 fail Humanization → §21 ЧАСТЬ 1 (H1-H10 приёмы, минимум 3-4 применить)
Сюжет красивый но шоты не двигают зрителя / beat без motivation / continuity рваная / декоративные шоты → V21 fail Rationality → §21 ЧАСТЬ 2 (RAT1-RAT8 проверки — переименованы из R1-R8 в волне П.20 для disambiguation от §3 R1-R14 prompt-engineering rules)
Stock environment / glass-partition glamour / идеальный desktop / театральная подача → V21 fail H1+H3+H4
Hook + Reveal + Resonance в одном Shot 1 / перегруз mental model → V21 fail R3+R7


## 5. §18A — SPLIT-SCREEN

═══════════════════════════════════════════════════
СПЕЦ-КЕЙС — SPLIT-SCREEN (алиас: §18A SPLIT-SCREEN)
═══════════════════════════════════════════════════

Ссылочный alias раздела: **§18A**. Другие агенты / промты могут ссылаться на эту секцию как «§18A SPLIT-SCREEN» или «§18A способ 1/2/3» — это валидная нотация, секция == §18A.

Триггер-фразы: «split-screen», «до/после в одном кадре», «два состояния одновременно», «вертикальный split», «контраст в кадре», «old CRM vs new CRM», «before vs after».

ВАЖНО: split-screen с одним героем в обеих половинах = де-факто Multi-Position case. Identity drift риск HIGH (~60-70%) даже с Soul ID — модель обрабатывает каждую половину как независимую композицию.

ТРИ способа собрать split-screen — выбор по приоритету:

1. РЕКОМЕНДУЕТСЯ — 2 отдельные генерации + manual composite в CapCut / Premiere:
   — Шаг A: левая (или верхняя) половина — отдельная генерация (Veo / Kling / Nano Banana 2).
   — Шаг B: правая (или нижняя) половина — отдельная генерация.
   — Шаг C: композит в CapCut (vertical split, центральный 2-4px divider).
   — Контроль: каждая половина рендерится независимо, identity / wardrobe / light можно подогнать ретраями без риска cross-half contamination.
   — Это надёжнее в 2-3 раза и единственный честный путь для STANDARD-режима.

2. Только статика — Nano Banana 2 split-frame:
   — Один промпт описывает обе половины + центральный divider.
   — Работает для статичных «before / after» постеров.
   — НЕ для видео — Nano Banana 2 only image.

3. ВНУТРИ Higgsfield single-shot video (Veo / Kling) — высокий риск:
   — Обязательно ОДНА color temperature для обеих половин (5600K + 5600K).
   — Обязательно ОДНО направление key light (key from camera-left для обеих).
   — LIGHT CONSISTENCY pack — применить inversed для обеих половин одновременно.
   — Risk T31 / T32 (skin tone clash, light shift between halves) — HIGH.
   — Сходимость 25-40% (5-10 ретраев).
   — Делать только если ученик настаивает на single-shot pipeline.

ПРАВИЛО ВЫБОРА ПО РЕЖИМУ:
— STANDARD режим → способ 1 (две отдельные single-shot + склейка). Это надёжнее в 2-3 раза.
— PRO режим → можно попробовать способ 3 (Veo 3.1 split-screen), но Soul ID + split-screen одновременно остаётся экспериментальной зоной. Закладывай 6-10 ретраев.
— LITE режим → split-screen архитектурно недопустим (бюджет не вытянет ретраи). Только способ 1 или 2.

**ЗАПРЕТ КОМБИНАЦИЙ (волна П.6 симметрия):**
— **§18A SPLIT-SCREEN × §19B INFOGRAPHIC** в одном креативе — НЕ КОМБИНИРОВАТЬ. Overload информации: половина экрана инфографика + половина talking head / lifestyle = ничего не читается. Если ученик просит «слева flowchart, справа founder» — разбивай на 2 креатива в пачке или композит в CapCut post-prod. Зеркало правила из §19B GUARDRAILS «не комбинируй §19B с §18A».
— **§18A SPLIT-SCREEN × Soul ID на ОБЕИХ половинах** — то же экспериментальная зона (см. способ 3 выше), не дефолт.

ЕСЛИ ВСЁ ЖЕ ОДНА ГЕНЕРАЦИЯ (способ 3):
```
Top half: anna_ds at position A wearing X doing Y, light setup L1.
Bottom half: anna_ds at position B wearing X doing Z, light setup L2.
Same anna_ds identity locked across both halves via Soul ID anchor.
```

Wardrobe и hair locked явно — повторять в описании обеих половин.
Split-line: «split-line clean and stable at frame midpoint, no morphing across the boundary».
Skin tone между половинами при разных color temp: «skin tone matches color temperature of each half but identity remains consistent» — снимает T32 риск.

Divider geometry:
— Vertical center line — стандарт для 9:16.
— 2-4px width, medium grey #888 — нейтральный.
— Можно опустить divider полностью (clean edge-to-edge) если контраст цветов сам разделяет половины.

Frame ownership per side (anti-drift):
— Левая (или верхняя) половина = «old / before / problem» — описать ОДНОЙ строкой.
— Правая (или нижняя) половина = «new / after / solution» — описать ОДНОЙ строкой.
— Никаких пересечений: персонаж НЕ ходит между половинами, объекты НЕ пересекают divider, light НЕ перетекает.

Hook H5 (contrast reveal) на split-screen работает СЛАБЕЕ чем монтажный cut «до/после» — за 2s зрителю надо успеть прочитать обе половины. Если выбрал split-screen для H5 — закладывай слабый CTR. Лучше: монтажный cut в CapCut.

КОГДА SPLIT vs МОНТАЖНЫЙ CUT — алгоритм выбора:

Прогоняй до начала генерации, не после. Если хоть один из критериев CUT-side активен — переключай на cut, не split.

| Условие                                                                  | SPLIT OK | CUT обязателен |
|--------------------------------------------------------------------------|----------|----------------|
| Сегмент Most-aware (H5 contrast reveal для evaluating-vendors)           | ✓        |                |
| Сегмент Cold / Problem-aware (top-of-funnel, новая аудитория)            |          | ✓              |
| LITE-режим (бюджет не вытянет 5-10 ретраев)                              |          | ✓              |
| STANDARD-режим + split с одним героем в обеих половинах (Soul ID)        |          | ✓ (drift риск 60-70%) |
| PRO-режим + два разных объекта в половинах (UI mockup + герой)           | ✓        |                |
| Жёсткая одновременность контраста требуется по смыслу (комп vs облако)   | ✓        |                |
| Нет жёсткой одновременности — это «трансформация во времени»             |          | ✓              |
| Watch-time сегмента >5s (B2B / HIGH_TICKET evaluating)                   | ✓        |                |
| Watch-time сегмента ≤3s (ECOM impulse / cold-traffic INFOBIZ)            |          | ✓              |
| Дизайнерское / эстетическое решение клиента «потому что прикольно»       |          | ✓ (cut даёт выше CTR) |

Если ученик выбирает split «потому что прикольно» / «в брифе так стоит» — переспроси: «split-screen с одним героем = identity drift 60-70% + H5 на 2s читается слабее cut. Cut даёт выше CTR. Уверен что split?» Перевыставление в cut снимает с тебя 5-10 ретраев на проект.

LITE — split архитектурно недопустим, только cut в CapCut.
Cold/Problem-aware (TOF) — split не использовать вообще. Только cut.
Most-aware + watch-time >5s — split рабочий вариант, но только способ 1 (две отдельные генерации + composite).

ШАБЛОН ОТВЕТА АГЕНТА при запросе split-screen:
```
Split-screen с одним героем — это известная боль AI-видео. Identity
дрейфует между половинами в 60-70% случаев. Рекомендую fallback:
1. Generate две отдельные single-shot (top + bottom) на Kling 3.0
2. Склейка вертикально в CapCut с одинаковым framing и color
3. Получишь стабильный результат за половину кредитов
Сделать так или всё же одну Veo-генерацию с риском ретраев?
```


## 6. §19A — UI / SCREEN MOCKUP PIPELINE

═══════════════════════════════════════════════════
§19A — UI / SCREEN MOCKUP PIPELINE
═══════════════════════════════════════════════════

Когда применять: ученику нужен screen mockup CRM / dashboard / app UI / web-app в кадре. Если профиль клиента = B2B_SAAS, FINTECH, EDTECH, HEALTHTECH — агент ОБЯЗАН предложить этот pipeline по умолчанию, не ждать запроса.

PIPELINE 2-шаговый (рекомендуемый):

Шаг 1 — Nano Banana 2 (статика UI):
— Workspace: Image Studio
— Модель: Nano Banana 2 (рендерит EXACT STRING лучше всех)
— Output: чистый PNG 9:16 / 1:1 / 16:9 — готовый к использованию как @image1

Шаг 2 — Veo 3.1 / Kling 3.0 (композитное видео):
— В motion-промпте: «Reference image: @image1 (the UI mockup from Step 1)»
— Камера смотрит на ноутбук / экран / планшет где этот @image1 «отображается»
— Push-in / static / arc — любая камера, главное чтобы экран был в кадре

АЛЬТЕРНАТИВА (fallback при провале композита 5+ ретраев):

Out-of-focus laptop screen:
— DOF f/1.4 — UI размытый до нечитаемости.
— Smartphone / hands / face в фокусе.
— Контраст композиции сохраняется, читаемость UI уходит — но крео работает на форме.

Real screenshot через Loom:
— Активируется ТОЛЬКО если ученик явно запросил screencast вне Meta-кампании (дефолт = Meta+IG, screencast не делаем).
— Заранее снять реальный UI в Loom / ScreenStudio.
— Импортировать как @video1 в Higgsfield (Veo 3.1 поддерживает video reference).
— Поверх AI добавляет camera move / talking head split.

REAL-LOOKING DATA PRINCIPLE (для шага 1):
— Цифры метрик должны выглядеть реалистично: CTR 1.7%, не 99%. MRR 24,300 USD, не 99999.
— Имена клиентов в UI: generic (Sarah J., Mike P.) или anonymized (Account #1247).
— Логотипы интеграций (MLS, Zillow, Stripe, HubSpot) — НЕ рендерить, оставить serif text-name или generic icon.
— Графики — простые bars / lines, не сложные heatmaps / sankey / treemap (Nano Banana 2 ломается на сложных визуализациях).

MITIGATION T23 (текст-глитч):
— EXACT STRING ≤50 символов на сегмент UI.
— Цифры лучше длинных слов («99 USD» рендерится чище чем «ninety-nine dollars»).
— Шрифт указать явно: «Inter Medium 13px» / «SF Pro Display SemiBold 18px» / «system UI sans-serif».
— **MAX 5 EXACT STRING на скрин (HARD CAP, не floor)**. Pre-flight FAIL если >5 строк — переделывай Шаг 1, не выпускай в Шаг 2. 6+ строк = 6-10 ретраев гарантировано на текстовый глитч. Не «у границы 5» — это **превышение лимита**, а не верхняя граница интерпретации.
  — Если в драфте 7 строк → дроп до 5 жёстко: оставь header + 2 metric + 1 status + 1 CTA. Subline / footer / disclaimer выноси в CapCut overlay post-prod.
  — Не объяснение «RISK: at the ceiling» в Caveats — это post-failure mitigation, а здесь нужен pre-flight cap.

GUARDRAILS §19A:
— Никогда не пытайся рендерить UI напрямую в Veo 3.1 / Kling 3.0 / Seedance — абракадабра гарантирована. Только через @image1 от Nano Banana 2 / GPT Image 2.
— Никогда не вставляй real логотипы (Stripe, Salesforce, HubSpot) в @image1 — это и юр-риск и triggers Meta brand violation. Только generic / serif text.

— **KNOWN BRAND UI generic mockup правило** (применяется когда в кадре нужен интерфейс узнаваемой third-party платформы):

Список узнаваемых SaaS / платформ-триггеров (НЕ исчерпывающий, расширяй при встрече):
TradingView · Bloomberg Terminal · MetaTrader · Salesforce · HubSpot · Pipedrive · Notion · Figma · Linear · Asana · Slack · Gmail · Google Calendar · Google Analytics · Looker · Tableau · Power BI · Stripe Dashboard · QuickBooks · Xero · Shopify Admin · WooCommerce · Klaviyo · Mailchimp · ClickUp · Monday · Zoom · MS Teams · Webflow · Squarespace · **AI-tools (волна П.6):** Midjourney · DALL-E · ChatGPT · Claude · Stable Diffusion · Runway · ElevenLabs · Suno · Pika · Higgsfield · Kling · Veo · Sora · Nano Banana · **Observability / APM / monitoring (волна П.8):** Datadog · Splunk · New Relic · Dynatrace · Grafana · Prometheus · PagerDuty · Sentry · AppDynamics · Elastic · Honeycomb · Lightstep.

Правило:
— ЕСЛИ у клиента нет официального partnership / referral агреемента с брендом → identifiable UI бренда в кадре **ЗАПРЕЩЁН**.
— Альтернатива: рендерим **generic mockup** через Nano Banana 2 с собственным стилем (минимальный sans-serif, нейтральная цветовая палитра, generic элементы — bars / lines / cards / sidebar).
— Generic alias для речи / overlay / hover-text:
   * TradingView → «Trading Platform» / «Chart Tool»
   * Bloomberg → «Market Terminal»
   * MetaTrader → «Trading Terminal»
   * Midjourney / DALL-E / Stable Diffusion → «Image Gen Tool» / «AI Image Model»
   * ChatGPT / Claude → «AI Assistant» / «LLM Tool»
   * Runway / Pika / Higgsfield / Kling / Veo / Sora → «AI Video Tool»
   * ElevenLabs / Suno → «AI Audio Tool»
   * Datadog / New Relic / Dynatrace / AppDynamics → «Observability Platform» / «APM Tool»
   * Splunk / Elastic → «SIEM Platform» / «Log Analytics Platform»
   * Grafana / Prometheus → «Monitoring Stack» / «Metrics Platform»
   * PagerDuty / Opsgenie → «Incident Response Tool»
   * Sentry / Honeycomb / Lightstep → «Error Tracking Tool» / «Distributed Tracing»
   * Salesforce / HubSpot / Pipedrive → «CRM Dashboard» / «Sales Console»
   * Notion / Linear / Asana → «Workspace App» / «Task Manager»
   * Figma → «Design Tool»
   * Google Analytics / Looker → «Analytics Dashboard»
   * Stripe Dashboard → «Payments Console»

Причины ограничения:
— Brand exposure risk: Meta brand-association check ловит реальное UI как «implicit endorsement» бренда без согласия.
— Юридический риск: trademark dilution + copyright (UI design protected как audiovisual work).
— Reputational risk: бренд может пожаловаться на использование своего UI в рекламе чужого продукта.

Pre-flight checklist для UI mockup:
1. Это реальный identifiable third-party brand? → Да → есть partnership? → Нет → generic mockup.
2. Если partnership есть → запросить у клиента письменное разрешение на использование UI в рекламе (sign-off).
3. Применить generic alias даже в Dialogue / voice-over если brand-name произносится крупно.
4. Workshop с клиентом до запуска если категория грейзоновая (например клиент торгует на TradingView → claim «как профессиональный трейдер на TradingView» без партнёрства = MISLEADING).

— **REAL product/brand name КЛИЕНТА в UI mockup → ВСЕГДА generic alias**. Не «Vault» (реальное имя продукта) — а «Compliance OS» / «Stack OS» / «Hub Console» (generic эквивалент). Причины: (а) визуальная связка «именно их UI» без screencast подтверждения = misleading-риск + Meta brand check; (б) при ребрендинге крео устаревает за день; (в) generic alias легче проходит модерацию.
  — В Dialogue: блоке Veo герой может произносить «Vault» — это статус mention. Но в UI экране generic.
  — Шаблон замены: «{Product} → {Category} OS» / «{Product} Dashboard» / «{Product} Console». Пример: «Vault → Compliance OS», «Recurly → Subscription OS», «Pipedrive → Sales Console».
— Не пытайся в одном @image1 совмещать full dashboard + sidebar + 3 modal окна — layout ломается. Один UI элемент = один @image1.

— **BRAND MARK HALLUCINATION rule** (для physical product категорий — авто / electronics / luxury goods / FMCG):

Если в кадре real product категории (BMW / Mercedes / Apple iPhone / Coca-Cola bottle / Rolex / Nike) БЕЗ partnership с brand:
— **Описывать как generic в IMAGE / motion слое:**
  * «German E-segment executive saloon» / «full-size luxury saloon» вместо BMW / Mercedes
  * «modern smartphone» / «slate-grey phone» вместо iPhone
  * «cola-style bottle» / «dark soda bottle» вместо Coca-Cola
  * «premium chronograph watch» вместо Rolex
  * «athletic running shoe» вместо Nike
— **В NEGATIVES — явный list для каждого brand:** «NO BMW roundel, NO BMW kidney grille badge, NO Mercedes-Benz three-pointed star, NO Porsche crest, NO Apple logo, NO Nike swoosh, NO brand badge, NO emblem, NO logo on body, NO manufacturer mark».
— **Brand name можно произносить в Dialogue** (это услуга / упоминание / статус mention, не visual exposure). «ТО вашего BMW G-серии» в речи Тимура — OK; visual BMW roundel в кадре — НЕ OK без partnership.
— **3-5 ретраев** на brand mark hallucination — Veo / Seedance / Kling часто дорисовывают узнаваемые badge даже при явных negatives (модели «знают» как выглядит BMW grille и подсовывают его).
— **Fallback при 5+ ретраях:** Nano Banana 2 генерит generic car статикой → подгружай как @image1 в Cinema Studio / Seedance → motion-промпт описывает только героя и движение, машина приходит из ref. Это снимает hallucination brand mark (Nano Banana 2 lower brand mark drift).
— **Generic silhouette:** для авто — намеренно generic E-segment full-size saloon без характерных hofmeister kink (BMW) / sloping coupe roof (Mercedes CLS / Audi A7) / signature grille pattern. Чтобы не считывалось как конкретная модель.

Регуляторный фон:
— Trademark dilution risk (использование real brand badge без партнёрства в чужой рекламе)
— Meta brand-association check может прочитать как implicit partnership / endorsement
— Если product категория критична (премиум-автосервис, ремонт техники) — brand упоминание в речи OK, но visual exposure brand mark = риск.

BUDGET TIERS для §19A (волна П.7 — симметрия с §19B):
— **LITE** = Шаг 1 only (Nano Banana 2 рендер UI как статика 9:16, без motion-композита). Если бюджет совсем не вытягивает — out-of-focus laptop screen fallback (см. ALTERNATIVA выше).
— **STANDARD** = Шаг 1 обязателен + Шаг 2 (Veo 3.1) для hero-крео (1 из 3-5). Остальные крео — статика @image1 без motion-композита.
— **PRO** = Шаг 1 + Шаг 2 (Veo 3.1) дефолт + **Magnific upscale финального кадра** (обязательно для PRO, симметрия с §19B PRO-логикой). Higgsfield Audio soft ambient опционально под кадр с UI.

GUARDRAILS §19A camera-move (волна П.7 уточнение):
— Push-in / static / arc — камера движется **ВОКРУГ физического экрана** где @image1 «отображается» (вокруг ноутбука / планшета / телефона). Это OK.
— **NO pan / orbit / dolly ON the UI surface itself** — камера НЕ двигается по самому UI (ВНУТРИ экрана). Это drift текста + нечитаемость UI elements. Если ученик просит «pan по dashboard» (внутри UI) → reject + предложить альтернативу:
   (а) §19B INFOGRAPHIC-CHART motion-логика (soft pulse / fade-in отдельных UI-элементов) — но тогда UI становится «инфографикой», упрощённый layout без фотореализма ноутбука.
   (б) Multi-shot композит — несколько отдельных @image1 (UI sequence) показанных через cut, не camera-move.


## 7. §19B — INFOGRAPHIC / EDUCATIONAL / COMPARISON PIPELINE

═══════════════════════════════════════════════════
§19B — INFOGRAPHIC / EDUCATIONAL / COMPARISON PIPELINE
═══════════════════════════════════════════════════

Ссылочный alias раздела: **§19B**. Другие агенты / промты могут ссылаться как «§19B INFOGRAPHIC PIPELINE» или «§19B SWATCHES / COMPARISON / PROGRESSION / CHART / DIAGRAM» — валидная нотация, секция == §19B.

Когда применять: ученику нужен формат который **не кинематографичный**, а инфографический / образовательный / сравнительный. Это 30-50% креативов для:
— **INFOBIZ** — карусели «N промптов в M стилях», структура курса, outcome-метрики
— **MEDICAL_HEAVY / LOCAL_SERVICE медицина** — анатомическая прогрессия («3 года без зуба → что с костью»), 3-tier сравнение имплантов / процедур
— **LOCAL_SERVICE прайсовые** — 3 пакета услуг с ценами, тарифы с региональными флагами
— **ECOM каталог** — сравнение продуктов, размерная сетка, до/после метрик
— **B2B SaaS** — explainer-диаграммы «как работает наш AI», conversion funnel, pricing tiers
— **CRISIS_EXPERT** — «3 шага юр-аудита» / «процесс работы», substantiated outcomes
— **HIGH_TICKET** — процесс работы 1→N этап, indicative-valuation framework visual

Если профиль = один из выше И ученик в Intake указал жанр «инфографика / схема / сравнение / прайс / explainer» — агент ОБЯЗАН предложить §19B по умолчанию, не ждать запроса.

PIPELINE 2-шаговый (рекомендуемый):

Шаг 1 — Nano Banana 2 (статика инфографики):
— Workspace: Image Studio
— Модель: Nano Banana 2 (рендерит EXACT STRING + flat-vector layouts лучше всех)
— Pack: один из 5 (STYLE-SWATCHES-GRID / COMPARISON-CARDS / EDUCATIONAL-PROGRESSION / INFOGRAPHIC-CHART / ANIMATED-DIAGRAM) — см. каталог паков
— Output: чистый PNG 9:16 / 1:1 / 16:9 / 4:5 — готовый к использованию как @image1 ИЛИ как самостоятельный статический креатив

Шаг 2 (опциональный) — Veo 3.1 / Kling 3.0 (мягкая анимация):
— В motion-промпте: «Reference image: @image1 (the infographic from Step 1)»
— Камера статика (no camera move / static frame / locked-off)
— Motion ТОЛЬКО на элементах: подсветка / появление цифр / мини-зум на одну деталь / soft fade-in узлов flowchart / pulse на active-card / draw-on arrow
— ЗАПРЕТ: pan / orbit / dolly-in на инфографику — текст становится нечитаемым во время движения, killер для conversion

LITE-логика для §19B (CRITICAL — это главное окно применения):
— Дефолт = ТОЛЬКО Шаг 1 (Nano Banana 2 статика). Без Veo / Kling.
— Статичный креатив = LITE-friendly: 1 генерация, 0 ретраев на motion, читается за 1.5s.
— 80% инфографики для INFOBIZ / LOCAL_SERVICE прайс / ECOM каталог должны быть статикой — мягкая анимация добавляет 20-30% к conversion, но стоит 5-10x по credits.

STANDARD-логика:
— Шаг 1 ОБЯЗАТЕЛЕН (статика). Шаг 2 — для hero-крео (1 из 3-5).
— Мягкая анимация через Veo 3.1: 200-300ms fade-in / soft pulse / draw-on. Camera ВСЕГДА static.

PRO-логика:
— Шаг 1 + Шаг 2 как дефолт. Plus Magnific upscale для финального крео.
— Higgsfield Audio — soft ambient one-note под мягкую анимацию (НЕ cinematic trailer mood).
— Допустимо: композитный 2-3 секционный креатив (3 progression panels с последовательным reveal каждой через ~1s).

REAL-LOOKING DATA PRINCIPLE (см. §19A для деталей):
— Цифры должны быть substantiated (см. V18): «1247 sign-ups из 4380 visitors = 28.5%», не «99% conversion».
— Имена / бренды клиента → generic alias («Базовый тариф» вместо «Vault Lite»; «existing CRM» вместо «Salesforce»).
— Региональные флаги (для COMPARISON-CARDS) — emoji или 16×12px line-art, без полной геральдики.
— Шрифт указать явно: Inter Medium / Inter Bold / SF Pro Display (Nano Banana 2 ломается на decorative шрифтах).

MITIGATION T38 (infographic glitch — text wrap fail / layout drift / decorative-junk):
— EXACT STRING ≤5 на креатив (HARD CAP, не floor). Pre-flight FAIL если >5 строк → переделывай Шаг 1, не выпускай в Шаг 2.
   — Если 7+ строк → режь до 5: оставь header + 3 data labels + 1 CTA. Sublines / footer / disclaimer → CapCut overlay post-prod.
   — Для COMPARISON-CARDS (3 cards × 3 строки) разрешённый cap ≤12 общих микро-надписей, но pre-flight: каждая card должна читаться независимо за 1 секунду.
— MAX 5 data points на чарт (3-5 bars / 3-5 funnel stages / 1-3 metric callouts). 7+ data points = chart-junk + читается как «много цифр, ничего не понятно».
— MAX 5 узлов на flowchart (ANIMATED-DIAGRAM). 7+ узлов → разбивай на 2 диаграммы (2 креатива).
— Шрифт явный (Inter Medium 14px / Inter Bold 28px) — иначе T38 drift в decorative шрифты на 3-5 ретраях.

GUARDRAILS §19B:
— Никогда не пытайся рендерить infographic напрямую в Veo 3.1 / Kling 3.0 / Seedance — абракадабра гарантирована. Только через @image1 от Nano Banana 2.
— **NO photoreal лица пациентов / клиентов** в EDUCATIONAL-PROGRESSION или INFOGRAPHIC-CHART — только illustration / silhouette / generic icon. Для MEDICAL_HEAVY это критично (Meta policy + локальный закон о персональных данных).
   — **Включая AI-сгенерированные лица (волна П.6).** Meta Sensitive Health не различает реальное vs AI-сгенерированное лицо в медицинском/прогрессионном контексте — оба = FAIL. Защита тройная: Meta policy + EU AI Act art.50 + ФЗ-152 РФ / GDPR EU / state-laws USA (CA AB-2602 + IL BIPA).
   — **Возражение «есть подписанное согласие пациента» НЕ снимает запрет** — стандартная клиническая согласка не покрывает (а) коммерческое использование в рекламе, (б) AI-likeness, (в) трансграничную передачу данных через Meta. Нужно отдельное opt-in под рекламную кампанию + проверка совместимости с локальной юрисдикцией. Для KZ/RU/BY/UA — закон о рекламе медуслуг ПРЯМО запрещает использование изображений конкретных пациентов в рекламе независимо от согласия. См. также `meta-policy-checker` категория «Тяжёлая медицина» строки 304-305.
— **V18 anchor pricing** применяется КО ВСЕМ цифрам в чартах / cards / metric callouts. «Conversion 47%» без объяснения базы / источника = V18 fail.
— **Generic brand alias** для UI / competitor / client product names в любом из 5 паков (см. §19A KNOWN BRAND UI rule).
— **Камера статика в Шаге 2** — pan / orbit / dolly-in на инфографику убивают читаемость. Motion ТОЛЬКО на элементах внутри кадра.
— **Не комбинируй §19B с §18A (SPLIT-SCREEN)** в одном креативе — overload информации. Если нужен «график + talking-head» — это 2 отдельных креатива в пачке или композит в CapCut post-prod.
— **Не комбинируй §19B с Soul ID на главного героя** — инфографика читается одна, без человека в кадре. Если нужен founder face — outro frame (3-5s после инфографики), separate композит.

ПРИВЯЗКА К ПРОФИЛЯМ (когда §19B обязателен для рассмотрения):

| Профиль | Pack | Когда |
|---|---|---|
| **INFOBIZ** | STYLE-SWATCHES-GRID + INFOGRAPHIC-CHART | Лид-магнит «N промптов в M стилях», outcome-метрики курса, структура курса (через ANIMATED-DIAGRAM) |
| **LOCAL_SERVICE медицина (MEDICAL_HEAVY)** | EDUCATIONAL-PROGRESSION + COMPARISON-CARDS | «3 года без зуба → что с костью», «3 системы имплантов с флагами», anatomy-explainer |
| **LOCAL_SERVICE прайсовые (бьюти, фитнес)** | COMPARISON-CARDS | 3 пакета услуг, тарифы, абонементы |
| **ECOM** | COMPARISON-CARDS + INFOGRAPHIC-CHART | Сравнение продуктов, размерная сетка, результаты «выросли X% за месяц» |
| **B2B_SAAS** | ANIMATED-DIAGRAM + INFOGRAPHIC-CHART | «Как работает наш AI», conversion funnel, pricing tiers — параллельно с §19A UI MOCKUP |
| **CRISIS_EXPERT** | ANIMATED-DIAGRAM + INFOGRAPHIC-CHART | «3 шага юр-аудита», substantiated outcomes (с обязательной substantiation per V18) |
| **HIGH_TICKET / M&A** | ANIMATED-DIAGRAM + INFOGRAPHIC-CHART | Процесс работы 1→N этап, indicative-valuation framework visual |
| **EDTECH / KIDS_PARENTS** | STYLE-SWATCHES-GRID + ANIMATED-DIAGRAM | Программа курса, структура занятий, тематические недели |

Pre-flight checklist для §19B креатива:
1. Жанр явный? (swatches / comparison / progression / chart / diagram) → если нет → переспроси у ученика.
2. EXACT STRING на драфте ≤5 (или ≤12 для COMPARISON-CARDS)? → если нет → дроп лишнего ДО Шага 1.
3. Все цифры substantiated (V18)? → если нет → запрашивай у ученика источник или generic alias.
4. Все имена клиента / brand → generic alias (§19A rule)? → если нет → заменяй.
5. MEDICAL_HEAVY: проверка — нет photoreal лиц пациентов (вкл. AI-сгенерированные — Meta Sensitive Health не различает реальное vs сгенерированное), нет direct medical claims, прогон через `meta-policy-checker`, проверка MEDICAL_HEAVY правил §16 + HIGH_TICKET_LOCAL_SERVICE медицина guardrails: лицензия Минздрава в footer для KZ/RU/BY/UA, generic icons / silhouettes / abstract figures вместо лиц пациентов, лицо клиента НЕ в кадре (cross-ref CRISIS-AUDIT-LAYER C2/C4 — single source of truth inline)?
6. Шрифт указан явно (Inter / SF Pro / system UI)? → если нет → добавь.
7. Шаг 2 нужен? → LITE: нет. STANDARD: только hero (1/3-5). PRO: дефолт.
8. Камера в Шаге 2 = static? → если pan/orbit/dolly → переделай (текст не читается).

**ВАЖНОЕ РАЗЛИЧИЕ §19A vs §19B по камере (волна П.6 уточнение):**
— §19A UI MOCKUP разрешает push-in / static / arc — камера двигается по физической сцене где экран находится (камера движется ВОКРУГ ноутбука с UI, не по UI).
— §19B INFOGRAPHIC только static — инфографика занимает 100% кадра, любое движение камеры = drift текста и нечитаемость.
— Не путать: визуально похоже (оба — статика-плюс-анимация), функционально разное.


## 8. §20 — OFFER → STORY MAPPING

═══════════════════════════════════════════════════
§20 — OFFER → STORY MAPPING (как оффер превращается в сюжет видео)
═══════════════════════════════════════════════════

Главная дыра до Волны П.12: оффер ученика лежит в PROMPT-4 (Чат 3), промпт под Higgsfield пишется в higgsfield-prompt-generator — но **между ними нет правила «как именно текст оффера превращается в визуальный сюжет 6-9 секунд»**. Без этого правила Cowork импровизирует — два креатива под один оффер получаются разные по структуре, новички получают «красивую картинку которая не продаёт оффер».

§20 закрывает эту дыру.

ПРИНЦИП «ONE OFFER = ONE STORY» (волна П.12):
— Один оффер = один сюжетный концепт = один креатив (не 2-3 в одном видео).
— Сюжет = носитель оффера. Если зритель посмотрел 6s видео и не понимает «какая выгода продаётся» — сюжет неправильный.
— Сюжет НЕ иллюстрирует оффер дословно («10 проектов за 3 недели» ≠ кадр с цифрой «10» на экране). Сюжет показывает **доказательство** того что оффер реален (герой собирает портфолио = доказательство).

ШАБЛОН СТЫКОВКИ ОФФЕРА К СЮЖЕТУ (5 шагов + 2 pre-валидатора, обязательно для каждого промпта):

**Pre-валидатор A (волна П.12 после стресс-теста §20). Profile-block / absolute promise check ДО Шага 1.**

Перед деконструкцией оффера — два жёстких теста:

A.1. **MEDICAL_HEAVY / FINANCE — absolute promise в оффере?** Если WHEN или WHAT содержат: «за 1 визит / за 1 час / гарантированно / 100% / без боли / без металла / на всю жизнь» — STOP, верни в meta-policy-checker, перепиши оффер ДО §20. Не запускай §20 на оффере который заблокируется на V17b после генерации (это лишний цикл, агент ничего не выдаёт ученику до переписи).

A.2. **Real brand names в оффере?** Если WHO / WHAT / PROOF / CTA содержат named brands (Datadog / Salesforce / Vault Compliance / etc) — **переписи через §19A KNOWN BRAND alias СЕЙЧАС**, ДО Шага 1. Пример: оффер «миграция с Datadog за 24 часа» → переписать в «миграция с existing APM за 24 часа» в EXACT STRING / overlay. Real brand name можно произнести в Dialogue Veo (статус-mention), но в визуальном слое — generic alias.

**ИСКЛЮЧЕНИЕ — medical brand names (волна Т.2 после Т.2-5 Мета).** Для MEDICAL_HEAVY медицинские системы (Straumann / Nobel Biocare / Osstem / MIS импланты, Invisalign ортодонтия, Restylane / Juvederm филлеры) — это **substantiated factual product names**, не маркетинговая жертва. Разрешены в визуальном слое + Dialogue. Условия: (а) система реально используется в клинике, (б) есть регистрационное удостоверение в стране (KZ Минздрав / RU Росздравнадзор / EU CE-mark), (в) лицензия клиники на работу с системой. Без условий — generic («премиальная швейцарская система»).

A.3. **Biographical claim с числом? (волна Т.2 после Т.2-5 Мета — ранний trigger V19-BIOCLAIM):**

Если WHAT / PROOF / CTA содержат **число рядом со словом** «операций / имплантаций / пациентов / лет практики / выпускников / клиентов / сделок закрыто / N% conversion / N лет на рынке» — **STOP**. Запросить артефакт sign-off (скриншот письма / Notion ≤ 7 дней / реестр пациентов / CRM-выгрузка) ДО Шага 1.

Это дубль V19-BIOCLAIM (см. §21 ДОПОЛНЕНИЕ) но **на раннем этапе**, до §19A/§19B рендера. Иначе ученик заплатит за Higgsfield-кредиты, дойдёт до V21 pre-flight, поймает FAIL и переделает с нуля.

Без артефакта — обязательная замена ДО Шага 1:
- «47 студентов» → «более 40 выпускников»
- «1247 имплантаций за 12 лет» → «более 1000 имплантаций / многолетняя практика»
- «98% успеха» → «высокий процент успеха согласно отраслевым стандартам»

A.4. **Non-USD валюта в оффере? (волна Т.2):**

Если WHAT / PROOF содержат цены в non-USD валюте (KZT / RUB / UAH / BYN / PLN / TRY / EUR / AED / GBP / CHF) — Cowork **обязан** выполнить conversion в USD по live-курсу ДО Шага 1 для:
- Сверки режима клиента (LITE до 500 USD / STANDARD 500-3000 / PRO 3000+)
- Reality-check экономики
- Корректного выбора арки (HIGH_TICKET_ECOM требует AOV >1000 USD, ECOM_PREMIUM = 200-1000)

Пример: «3 системы имплантов 250/450/800 тысяч тенге» → курс 470 KZT/USD = $530/$957/$1700. Средний чек $1062 — **HIGH_TICKET_LOCAL_SERVICE медицина** (не «STANDARD-имплант»). Reality-check + рекомендуемый формат меняются.

A.5. **DSHEA disease claim в оффере для WELLNESS_HEALTH_RESTRICTED USA-flight? (волна П.23 после Т.7-D предложения — early-trigger для WELLNESS_HEALTH_RESTRICTED_USA_PRESET ПРАВИЛО 2):**

Если профиль = WELLNESS_HEALTH_RESTRICTED + гео USA (даже частичное) и WHAT / PROOF / WHEN / CTA содержат **disease claim pattern** — **STOP**, верни в meta-policy-checker категорию «WELLNESS_HEALTH_RESTRICTED_USA — DSHEA», перепиши оффер ДО Шага 1.

Disease claim FAIL patterns (DSHEA §403r-6 — требует FDA drug approval NDA process, supplement не может claim):
— «Cures insomnia» / «treats insomnia» / «replaces prescription sleep meds»
— «Treats diabetes» / «reverses diabetes» / «lowers blood sugar in diabetics» / «lowers A1C»
— «Prevents cancer» / «reduces cancer risk» / «fights tumor growth» / «shrinks tumors»
— «Reverses ED» / «treats erectile dysfunction» / «cures impotence» / «like Viagra»
— «Treats depression» / «cures anxiety» / «manages bipolar» / «eliminates anxiety»
— «Lowers high blood pressure» / «treats hypertension» / «dissolves cholesterol plaques»
— «Treats COVID» / «prevents flu» / «kills viruses» / «boosts immunity to disease»
— «Reverses arthritis» / «cures joint pain» / «heals leaky gut»
— «Reverses menopause symptoms» / «treats menopause»
— «FDA-approved» (supplement = NOT FDA-approved, только pre-market notification — sam claim = misleading)

Implied disease claim FAIL patterns (более коварные — detection требует визуальный + контекстный анализ):
— Imagery sick person → healthy person transition в before/after (implied treatment claim)
— Before/after с medical visual cue (waist measurement, BP cuff, glucose meter, thermometer)
— Voice-over «my doctor said my numbers came back normal» (implied disease treatment)
— Targeting через condition («for diabetics» / «for cancer patients» / «for arthritis sufferers») = disease-claim by population
— «Like Ambien without prescription» / «like Viagra naturally» (drug comparison = implied drug-equivalence)

Без переписи — обязательная замена ДО Шага 1 (structure/function claim per 21 CFR 101.93):
— «Cures insomnia» → «supports restful sleep» / «promotes natural sleep cycle»
— «Treats diabetes» → «supports healthy blood sugar levels already within normal range»
— «Reverses ED» → «supports healthy circulation» / «supports male vitality»
— «Lose 30 lbs in 30 days» → «may support weight management as part of healthy diet and exercise»
— «Cures anxiety» → «supports stress response» / «promotes relaxation»

Это дубль WELLNESS_HEALTH_RESTRICTED_USA_PRESET ПРАВИЛО 2 (DSHEA §403r-6 hard-line) но **на раннем этапе**, до §19A/§19B рендера. Иначе ученик заплатит за Higgsfield-кредиты, дойдёт до 9/9 PASS чек-листа, поймает FAIL на ПРАВИЛО 2 + ПРАВИЛО 3 (FDA disclaimer overlay) и переделает с нуля.

Cross-ref: WELLNESS_HEALTH_RESTRICTED_USA_PRESET ПРАВИЛО 2 (полные OK/FAIL списки) + ПРАВИЛО 3 (mandatory FDA disclaimer overlay для structure/function claim) + meta-policy-checker категория «WELLNESS_HEALTH_RESTRICTED_USA — DSHEA structure/function vs disease claims».

**Шаг 1. Деконструкция оффера на 5 элементов:**
- **WHO** — кому (сегмент)
- **WHAT** — что получит (конкретный технический результат)
- **WHEN** — за какой срок
- **PROOF-ELEMENT** — что реально доказывает что результат достижим (метод / инструмент / кейс / число)
- **CTA-ACTION** — что нужно сделать (написать / записаться / купить)

Пример для оффера «Junior-дизайнер соберёт 10 проектов в портфолио за 3 недели — пиши КЕЙСЫ в директ»:
- WHO: junior-дизайнер с пустым портфолио
- WHAT: 10 проектов в портфолио
- WHEN: 3 недели
- PROOF-ELEMENT: методика учеников + Figma-шаблоны + ментор
- CTA-ACTION: написать КЕЙСЫ в Direct

**Шаг 2. Выбор сюжетной арки по типу оффера (6 канонических арок):**

| Тип оффера | Сюжетная арка | Когда применять | Профили |
|---|---|---|---|
| **A. РЕЗУЛЬТАТ-В-РУКАХ** | Shot 1 «герой держит/использует РЕЗУЛЬТАТ» → Shot 2 «процесс получения (compressed)» → Shot 3 «CTA + результат» | Конкретный материальный результат (портфолио, гайд, чек-лист, диплом, отчёт) | INFOBIZ / EDTECH / B2B SaaS lead-magnit |
| **B. ДО → ПОСЛЕ ПРОЦЕССА** | Shot 1 «исходная точка (без жертвы)» → Shot 2 «процесс/инструмент» → Shot 3 «новое состояние + CTA» | Трансформация workflow / выходов (ноль клиентов → поток, ручной труд → AI-pipeline) | INFOBIZ / B2B SaaS / WELLNESS lifestyle |
| **C. ЭКСПЕРТ ПОКАЗЫВАЕТ МЕТОД** | Shot 1 «эксперт прямой взгляд + цифра» → Shot 2 «эксперт указывает на инструмент / экран / схему» → Shot 3 «CTA» | Authority-driven офферы (методика / процесс / framework) | HIGH_TICKET / EXEC_COACHING / B2B_PROFESSIONAL_SERVICES / CRISIS_EXPERT |
| **D. ПРОДУКТ В ДЕЙСТВИИ** | Shot 1 «product reveal с macro detail» → Shot 2 «использование в life-style» → Shot 3 «CTA + price + flag» | ECOM / WELLNESS-product / LOCAL_SERVICE с физическим артефактом | ECOM / ECOM_IMPULSE / WELLNESS / LOCAL_SERVICE bauty/repair |
| **E. КАТАЛОГ ВАРИАНТОВ** | Shot 1 «3 варианта в кадре одновременно» → Shot 2 «крупный план на отличие» → Shot 3 «CTA + выбор» | COMPARISON-офферы (3 тарифа / 3 пакета / 3 процедуры) | LOCAL_SERVICE прайс / ECOM каталог / B2B SaaS pricing tiers |
| **F. ПРОЦЕСС ПО ШАГАМ** | Shot 1 «вход (текущая ситуация)» → Shot 2 «шаги 1-2-3 (compressed)» → Shot 3 «выход + CTA» | Process-офферы («3 шага юр-аудита», «5 этапов M&A», «4 фазы трансформации») | CRISIS_EXPERT / HIGH_TICKET / B2B_PROFESSIONAL_SERVICES / EDTECH |
| **G. TIMELINE-OBSERVATION** | Static §19B EDUCATIONAL-PROGRESSION: 3 панели «состояние через N времени» с консистентным визуальным стилем (cross-section / 3D / schematic) | Timeline-наблюдение пассивного изменения («3 года без зуба → что с костью», «6мес/1год/3года после процедуры») — НЕ process-действия | MEDICAL_HEAVY стом/ortho/dermo + EDTECH (структура курса по неделям) |

Дополнительно для статика (§19B INFOGRAPHIC) — арка та же логически, но **без motion**: header (хук) → визуальная схема (тело) → CTA (закрытие).

**КОМПАТИБИЛИТИ АРОК × ПРОФИЛИ (волна П.12 после S20-B):**

| Профиль | Разрешённые арки | ЗАПРЕТ |
|---|---|---|
| MEDICAL_HEAVY (premium-static-only) | C (talking-head врача tripod) / E (§19B COMPARISON-CARDS) / G (§19B EDUCATIONAL-PROGRESSION) / F через §19B ANIMATED-DIAGRAM static | **A** (требует лицо/тело пациента в кадре = AI-лицо запрет П.6), **B** (до/после = direct medical claim риск), **D** (lifestyle handheld нарушает premium-static-only) |
| HIGH_TICKET_PRO_SERVICES (M&A / LEGAL / private banking) | C (партнёр через Soul ID tripod) / E (§19B 3 service tiers) / F через §19B ANIMATED-DIAGRAM static / **G через §19B EDUCATIONAL-PROGRESSION** (process показ M&A 1→4 этап / 3-этапа due diligence / 4-фазы wealth-structuring — TOF educational без лиц, разрешено per HIGH_TICKET_PRO_SERVICES_PRESET 3-STEP FUNNEL) | **A** (NDA — нет лиц клиентов), **B** (NDA + риск конкретных сумм), **D** (нет физического продукта) |
| B2B_SAAS_ENTERPRISE | A (UI mockup как «результат») / C (executive Soul ID) / F (process миграции) | D (нет физического продукта) |
| INFOBIZ | A (портфолио/гайд) / B (workflow) / C (наставница) / F (программа в этапах) | E (есть только если 3 тарифа курса) |
| ECOM / ECOM_IMPULSE / ECOM_PROSTOY / ECOM_PREMIUM | D (продукт в действии) / E (каталог 3 вариантов) | C (нет эксперта-фронтмена обычно) |
| LOCAL_SERVICE (стом/бьюти/фитнес) | A (результат услуги) / C (врач/мастер) / E (3 пакета услуг) / G для MEDICAL_HEAVY | D handheld для премиум — снижает register |
| CRISIS_EXPERT | C (юрист tripod) / F через §19B ANIMATED-DIAGRAM static | A (нельзя «результат» = бывший клиент), B (нельзя before/after психо-состояний), D (нет продукта) |
| REAL_ESTATE_EXPAT | A (вилла как результат) / C (broker) / D (виллa как продукт) | F (процесс покупки слишком длинный для одного крео) |
| EU_RUSSIAN_DIASPORA × LEGAL (sub-profile поверх CRISIS_EXPERT) | C (эксперт-релокант Soul ID tripod) / F (3-этапа процедуры через §19B ANIMATED-DIAGRAM, BRAO/NRA scope-of-practice overlay) | B (FHA-аналог в EU = GDPR Art.9 ethnic preference signal), D (NDA + cross-border confidentiality) |
| EU_RUSSIAN_DIASPORA × HIGH_TICKET (sub-profile поверх HIGH_TICKET_PRO_SERVICES) | C (эксперт-релокант с adapted-to-EU wardrobe) / G через §19B EDUCATIONAL-PROGRESSION (Cyprus Non-Dom / Malta GRP / D7 process без identifiable people) | A (sanctions cash-friendly framing), B (aggregated client-count = AML indirect disclosure) |
| EU_RUSSIAN_DIASPORA × KIDS_PARENTS (sub-profile поверх KIDS_PARENTS) | C (parent-релокант Soul ID) / F (3-этапа bilingual EDTECH curriculum через §19B) с mixed-race casting | B (UK ICO AADC minor's data inference через lookalike), F (Russian-language interest = ethnic-proxy GDPR Art.9) |
| RELIGIOUS_TRAVEL | A (паломники у святыни) / C (гид-священник) — с CRISIS-audit-layer если в crisis-аудитории | B (катастрофическая лексика «исцеление»), D (нет продукта) |

**Шаг 3. Соответствие арке × подходу Schwartz (волна М):**

| Schwartz уровень | Арка-фокус | Что НЕ показывать |
|---|---|---|
| **Unaware** | A или B — открыть существование решения | Без прямого CTA «купи» — это закрытие. Сначала «вот что есть» |
| **Problem-aware** | B или F — показать процесс решения проблемы | Без давления на боль (V17 Жертва) — показать инструмент |
| **Solution-aware** | C или E — показать почему ИМЕННО ваш метод vs альтернативы | Без generic «купи у нас» — показать дифференциатор |
| **Most-aware** | C или E — Authority + срочность + конкретные числа | Без «открытия» (зритель уже знает) — сразу к CTA + цене |

**Шаг 4. Связка с подходом (волна М, 8 подходов):**
- Боль → арка B или F (показ процесса вытаскивания)
- Выгода → арка A или D (результат-в-руках / продукт в действии)
- Страх → арка B (до/после, БЕЗ Жертвы в Shot 1)
- Соцдоказ → арка C (эксперт + цифра достижений)
- Эмоция → арка A или D (момент удовольствия от результата)
- Статус → арка D или E (премиум-продукт / премиум-выбор)
- Простота → арка F (процесс в 3 простых шага)
- Срочность → арка C (эксперт + time-anchor)

**Шаг 5. Pre-flight стыковки оффер ↔ сюжет (5 проверок):**

1. **Сюжет показывает PROOF-ELEMENT оффера?** Если оффер «10 проектов за 3 недели через методику X» — в сюжете виден намёк на методику X (учебник / лекция / Figma-доска / ментор). Иначе зритель не верит что результат реальный.

2. **Сюжет НЕ дублирует текст оффера дословно?** Если оффер «10 проектов» — НЕ нужен Shot 2 с цифрой «10» на экране (это перегруз). Сюжет показывает action, текст оффера живёт в EXACT STRING overlay 1-2 раза.
   — **ИСКЛЮЧЕНИЕ (волна П.12 после S20-A):** time-anchor / deadline / гарантия Hormozi-офферов разрешено дублировать «речь + overlay» как намеренный приём срочности или risk-reversal. Примеры: «набор закрыт 20 октября» — в Dialogue + в overlay (срочность); «30-day money-back» — в Dialogue + в overlay (Hormozi гарантия). Это canonical приём, не violation п.2. Запрет п.2 действует на дублирование цифр **результата** оффера (10 проектов / 47 учеников / 99.99% SLA) — это разные категории.

3. **CTA-ACTION физически возможен после просмотра?** Если CTA «пиши КЕЙСЫ в Direct» — сюжет ведёт к моменту когда зритель потянется к телефону. Кадр должен заканчиваться на something pointing to action (рука на phone / IG icon / Direct interface). Если кадр заканчивается на герое идущем в закат — CTA не сработает.

4. **Сюжет не превышает 1 концепт.** Если в 6s показано «герой собирает портфолио + клиент пишет в Direct + новая работа + happy ending» — это 4 концепта, перегруз. Один концепт на креатив. Остальное — в следующих креативах пачки.

5. **Сюжет PASSED V17 (нет Жертвы) + V18 (substantiated) + V19 (sign-off если biographical) + V20 (это §20 — стыковка оффер↔сюжет, новая проверка волны П.12).**
   — **Для CRISIS_EXPERT профиля (волна П.12 после S20-C):** активируй CRISIS-audit-layer проверки независимо от того что оффер религиозный или нет. CRISIS-audit-layer (раньше формально только для RELIGIOUS_TRAVEL × crisis-аудитории, см. §20 RELIGIOUS preset) теперь применяется ко всем CRISIS_EXPERT-кейсам: нет «успей пока окно / последние места» — только реальный slot / реальная дата судебного процесса; нет before/after психо-состояний в визуале; нет давления страхом.
   — **Для INFOBIZ Authority-офферов с числом учеников (волна П.12 после S20-A):** «47 маркетологов вышли на 100к за 3 месяца» = biographical claim = **V19 sign-off ОБЯЗАТЕЛЕН** до запуска. Реальный список учеников с подтверждением + срок «за 3 месяца» substantiated по реальным cohort-результатам. Без sign-off — переписать в generic «больше 40 выпускников» или удалить.
   — **Для B2B_SAAS_ENTERPRISE SLA-claim (волна П.12 после S20-C):** «99.99% SLA на 50k хостов» = juridical commitment с financial penalty при breach. V18 substantiation требует подписанный SLA contract от клиента, не маркетинговый «target». Без contract — FAIL V18, переписать в «target 99.99%» или удалить из оффера.

ВАЛИДАЦИЯ V20 (волна П.12):
- FAIL V20: «красивая картинка которая не продаёт оффер» — зритель посмотрел и не помнит WHAT (что получит).
- FAIL V20: «оффер про методику X — сюжет про лайфстайл героя» (показано не то).
- FAIL V20: «оффер из §19B COMPARISON-CARDS / тарифы — сюжет видео-героя» (формат не совпадает с типом оффера; нужна арка E через §19B).
- FAIL V20: «1 оффер = 3 концепта в одном креативе» (перегруз).

При FAIL V20 — НЕ выдавай промпт. Переписывай сюжет через шаги 1-5 выше.

ШАБЛОНЫ-ЗАГОТОВКИ ПО АРКАМ (готовые скелеты — заполняются под конкретный оффер):

**Арка A — РЕЗУЛЬТАТ-В-РУКАХ (пример: «10 проектов в портфолио за 3 недели») — обновлено П.19 с humanization-маркерами:**
```
Shot 1 (0-2s): MS frame, slight handheld micro-drift (not perfectly locked). {hero} sitting at desk in lived-in home office — half-empty coffee mug visible left, sticky notes on monitor edge, slightly wrinkled rug below desk. MacBook open. Figma board on screen with 10 finished UI mockups in 2x5 grid (real projects, varied styles). {hero} wardrobe: smart-casual blazer + plain tee, slight wrinkles at collar (lived-in not freshly ironed). Hair has one wisp near temple, day-old subtle stubble (for male) / minimal natural makeup with smile lines visible (for female). Camera holds, no cuts. Natural daylight from left + warm desk lamp.
Shot 2 (2-4s): ECU push-in on Figma board, scrolling through 3 hero projects (e-comm landing / dashboard / mobile app). Quick beat — 0.5s per project. Cursor moves with natural hesitation, not robotic.
Shot 3 (4-6s): Pull back. {hero} turns to camera. Eye contact NOT continuous — 4-4.3s direct, 4.3-4.5s brief look down (as if recalling), 4.5-6s back to camera with slight head tilt. Says with natural delivery cadence (micro-pause before "10", voice softens at end): «{цитата подтверждающая срок}». EXACT STRING overlay (5.5s fade-in): «{CTA — пиши КЕЙСЫ в Direct}».
[AUDIO] Natural ambient — distant cafe murmur OR home traffic through window, occasional keyboard typing under voice, NO stock background music.
[HUMANIZATION applied: H1 wisp+stubble, H3 lived-in workspace, H4 non-actor eye-shifts, H6 lived-in wardrobe, H7 ambient audio, H8 eye contact 70/30].
```

**Арка B — ДО → ПОСЛЕ ПРОЦЕССА (пример: «Поток клиентов 60k за 2 месяца»):**
```
Shot 1 (0-2s): Wide MS. {hero} в обычном workspace, типичная сцена работы. БЕЗ маркеров Жертвы (нет «уставшего» взгляда, нет ноутбука одного).
Shot 2 (2-4s): Smash cut в новую сцену. {hero} в processе использования метода (Notion-доска с pipeline / shadow проекта в Figma / звонок клиенту). Beat 1-1.5s на каждое действие.
Shot 3 (4-6s): Final cut. {hero} с измеримым результатом в руках (платёжка / счёт / новый клиент). EXACT STRING overlay: «{цифра результата} за {срок} — {CTA}».
```

**Арка C — ЭКСПЕРТ ПОКАЗЫВАЕТ МЕТОД (пример: «Indicative valuation за 14 дней»):**
```
Shot 1 (0-2s): MS frame, tripod-locked. {expert Soul ID} прямой взгляд в линзу, в кадре подсвечен один объект (notebook / book / screen). Opens with: «{цифра + контекст}».
Shot 2 (2-5s): Slow push-in на объект (notebook / methodology page / valuation framework). {expert} pointing to specific element. NO cuts, continuous shot.
Shot 3 (5-7s): Pull back to MS. {expert}: «{CTA — оставь заявку на indicative valuation за 14 дней}». EXACT STRING overlay: «{name + credentials}».
```

**Арка D — ПРОДУКТ В ДЕЙСТВИИ (пример: «Smart-кружка с auto-heat за 89 USD»):**
```
Shot 1 (0-2s): ECU on product. Macro detail — material, button, screen-glow. Slow rotate 30°. Beautiful light.
Shot 2 (2-4s): MS. {hero} using product in real lifestyle (morning kitchen / office desk / outdoor). Subtle interaction (sip / glance at temp display).
Shot 3 (4-6s): Product back on surface. EXACT STRING overlay: «{product name} · {price} · {1 unique benefit}». Optional flag (страна origin).
```

**Арка E — КАТАЛОГ ВАРИАНТОВ (пример: «3 системы имплантов» через §19B COMPARISON-CARDS):**
```
Это §19B static — НЕ video. Используй COMPARISON-CARDS pack:
- 3 vertical cards side-by-side, equal width
- Icon-логика consistent через все 3 (см. волну П.12 правило: либо везде «продукт + объект», либо везде «продукт изолирован»)
- Anatomically correct medical objects (винир ≠ коронка, имплант голый ≠ имплант с протезом)
- Header + 3 prices + 3 sublines + optional flags
- Camera static, no motion
- Опционально Шаг 2: soft pulse на «recommended» middle tier
```

**Арка F — ПРОЦЕСС ПО ШАГАМ (пример: «3 шага юр-аудита банкротства»):**
```
Если video: Shot 1 (0-2s) — header overlay «3 шага». Shot 2 (2-4s) — beat 1: action кадр шага 1. Shot 3 (4-6s) — beat 2: action кадр шага 2. Shot 4 (6-8s) — beat 3: action кадр шага 3 + CTA.
Если static (§19B ANIMATED-DIAGRAM): 3-5 nodes connected by arrows, header top, CTA bottom. Camera static (если Шаг 2 — node-by-node soft fade-in 200ms).
```

ANTI-PATTERNS — что НЕ делать (волна П.12):

1. **«Красивый кадр без оффера»** — герой в кафе с латте на закате, без visible PROOF-ELEMENT. Зритель посмотрел = «красиво» но не помнит «что мне продали». FAIL.

2. **«Оффер дословно в кадре»** — оффер «10 проектов за 3 недели», в кадре цифра «10» + «3 недели» + «портфолио» одновременно. Перегруз EXACT STRING (>5). FAIL T38.

3. **«Сюжет про лайфстайл при техническом оффере»** — оффер «методика X дает 50% conversion», сюжет про утро героя с кофе. Несоответствие WHAT и сюжета. FAIL V20.

4. **«3 концепта в 1 креативе»** — «герой работает + клиент звонит + happy ending + получение оплаты». Перегруз. Один креатив = один концепт. FAIL V20.

5. **«COMPARISON-оффер показан как видео-история»** — оффер «3 тарифа», вместо §19B COMPARISON-CARDS — сделан video с героем который «листает 3 тарифа». Структура не работает за 6s. FAIL V20.

6. **«Process-оффер показан как single-shot»** — оффер «5 этапов M&A», один кадр с экспертом без visualization этапов. Process требует beats (Shot 2/3/4 на каждый этап). FAIL V20.


## 9. §21 — HUMANIZATION + SCRIPT RATIONALITY (H1-H10, RAT1-RAT8)

═══════════════════════════════════════════════════
§21 — HUMANIZATION + SCRIPT RATIONALITY (волна П.19)
═══════════════════════════════════════════════════

§20 решил **что показывать** (оффер → сюжетная арка). §21 решает **как показывать чтобы выглядело живым и работало логически**. Две проблемы которые ловит §21:

1. **AI-видео выглядит как AI-видео** — uncanny valley, slick, generic, «никто так не живёт». Это убивает trust зрителя за 1.5 секунды. Сюжет правильный, но «не верю».
2. **Сюжет красивый но не работает на оффер** — beat-структура не имеет внутренней логики, кадры не складываются в продвижение зрителя от boredom к action. Сюжет — арт, не продажа.

§21 — это две параллельные проверки + V21 валидация.

═══════════════════════════════════════════════════
ЧАСТЬ 1 — HUMANIZATION (как не выглядеть AI)
═══════════════════════════════════════════════════

5 ПРИЗНАКОВ AI-СГЕНЕРИРОВАННОГО ВИДЕО которые нужно избегать (если хоть один присутствует — зритель чувствует «не настоящее»):

1. **Perfect symmetry** — лицо/композиция слишком симметричные. Реальное лицо асимметрично (одна бровь чуть выше, одна сторона рта чуть длиннее). В промпте: «slight facial asymmetry, one eyebrow ~2-3mm higher than other, natural micro-imbalance».
2. **Glossy texture** — кожа/ткань без noise / blemishes / pores. В промпте: ANTI-AI-LOOK pack дословно + «visible skin pores, peach fuzz catching light, sebaceous highlights on nose bridge, micro-blemishes near temples».
3. **Identical actor smile** — улыбка на одной интенсивности через все шоты. Реальный человек улыбается по-разному (полу-улыбка / усмешка / широкая улыбка / задумчивая полу-улыбка). В промпте: «smile intensity varies across shots: Shot 1 неловкая полу-улыбка, Shot 2 концентрация без улыбки, Shot 3 широкая искренняя улыбка после результата».
4. **Stock environment** — кухня/кафе/офис слишком clean, ничего «жилого». Реальный home/office имеет беспорядок: посуда в раковине, бумаги на столе, кружка не в центре, кабели в углу. В промпте: «lived-in workspace: half-empty coffee mug, sticky notes on monitor edge, books leaning to one side, slightly wrinkled rug».
5. **Continuous monotone delivery** — голос без вариаций, каждое слово одинаковой энергии. Реальная речь имеет неровности: пауза перед важной фразой, ускорение на знакомой части, тише на конце предложения. В промпте Dialogue Veo: «natural delivery — slight pause before "47", faster on familiar phrase, voice drops slightly on final word».

10 ПРИЁМОВ HUMANIZATION (применяй минимум 3-4 на промпт):

**H1. Микро-несовершенства внешнего вида героя:**
- Волосы немного не на месте (одна прядь у виска / слегка растрёпаны утром)
- Рукав слегка задёрнут / воротник немного криво
- Тонкий блик пота на лбу под софитом (или ВАЛИДНОЕ отсутствие — natural matte skin)
- Чуть смазанная помада / тушь немного потекла (для женского Soul ID)
- Слегка щетинистый подбородок (для founder, через 1-2 дня без бритья — это аутентично, не неряшливо)
В промпте: «slight imperfections — one wisp of hair near temple, sleeve subtly rolled up unevenly, micro-shine on forehead, day-old stubble».

**H2. Естественные паузы в речи (для Dialogue/voice-over):**
- Не каждое слово одинаковой энергии
- Микро-пауза перед ключевой цифрой / именем
- Замедление на знакомых терминах
- Слегка тише в конце предложения
- Опционально: пауза-вдох на стыке мыслей
В промпте Veo Dialogue: «natural delivery cadence — micro-pause before "10", subtle slowdown on "методика", voice softens at sentence end, mini-breath between two thoughts».

**H3. Бытовая environment vs glamour:**
- Glass-partition executive office → ТОЛЬКО для PRO Enterprise. Для остального — modern co-working / cafe corner / home office (с признаками жизни).
- Зеркальная стерильная кухня → реальная кухня с posy на холодильнике, magnet collection, half-loaded dish rack
- Идеальный desktop → MacBook на столе с water stain, заметки на полях notebook, cup of coffee у клавиатуры
- Smooth gallery wall → шкаф с книгами разной высоты, рамка чуть кривовато, плакат с угла подклеен
В промпте: «not perfectly staged — water ring on desk surface near laptop, fridge with kid drawings + magnets, slightly cluttered shelf above MacBook».

**H4. "Not actor" Soul ID feel:**
- Direct eye contact в линзу — НЕ постоянный (не «продаёт»). Допустимы микро-сдвиги взгляда (вспомнил → посмотрел в сторону на 0.3s → вернулся в кадр).
- Не каждое движение «отрепетированное». Можно подправить волосы за ухо, потереть глаз, посмотреть на кружку.
- Микро-зевок / chuckle / momentary тишина — для INFOBIZ founder типичная фактура.
- Голос не как у TV-ведущего. Подходящие маркеры: «conversational, not theatrical», «slight hesitation as if thinking», «natural rhythm of internal monologue».
В промпте: «non-actor feel — micro eye shifts (looks left briefly as recalling), occasional self-touch (fixing hair, rubbing eye), conversational tone not theatrical broadcast voice».

**H5. Естественные движения камеры (для handheld):**
- Handheld micro-drift даже на «локк-офф» — реальная камера не идеально статична (хоть subtle движение от дыхания оператора).
- Slight focus pull miss (камера на 0.5s чуть не в фокусе → восстановление) — реальная съёмка.
- Не идеально cetered framing — герой в кадре чуть смещён.
В промпте: «subtle handheld micro-drift even when locked-off, occasional 0.5s soft-focus drift before settling, hero positioned slightly off-center (rule of thirds)».

**H6. Wardrobe не glossy:**
- Не свежевыглаженная футболка — реальная ношеная.
- Slight wrinkles на рукаве / воротнике
- Цвета не сверкающие (washed-out look ткани после нескольких стирок)
- Опционально: едва видимое пятнышко от кофе на манжете (для very casual founder)
В промпте FABRIC pack + добавка: «lived-in wardrobe — slight wrinkles at collar and sleeves, washed-out fabric not freshly ironed».

**H7. Audio ambient (если Higgsfield Audio):**
- Не stock-music
- Реальные шумы окружения: distant traffic / cafe murmur / kettle boiling / keyboard typing
- Опционально: soft instrumental UNDERNEATH ambient (не overlay поверх)
- Громкость: ambient -25 dB, голос -6 dB primary
В промпте: «audio: natural ambient — distant cafe murmur, occasional cup clink, no stock background music, soft piano very subtle under ambient at -25 dB».

**H8. Eye contact non-perfect:**
- НЕ каждые 2 секунды прямой взгляд (это уже «уверенный лектор», AI-template)
- Допустимы микро-сдвиги: подумал → посмотрел вбок 0.3s → вернулся
- В talking-head 6s: 70% eye contact + 30% небольшие отрывы (vs 100% которые читаются как AI)
В промпте: «eye contact rhythm — 0-2s direct, 2.0-2.3s brief look down (as if recalling), 2.3-6s back to camera with slight tilt».

**H9. Лицо со следами реальной жизни:**
- Лёгкая припухлость под глазами утром (для founder в кадре с утренним свеженьким взглядом — это «не выспался, но работает» = relatable)
- Make-up не идеально вечерний — для INFOBIZ-founder лучше «свежий минимальный»
- Микро-морщинки у глаз при улыбке (smile lines — это здоровый признак, не дефект)
В промпте: «realistic morning look — slight under-eye puffiness, minimal natural makeup, smile lines visible when smiling at end».

**H10. Несовершенный продукт в кадре:**
- Кружка не идеально центрирована
- Notebook раскрыт не на «правильной» странице (есть пометки, зачёркивания)
- Phone screen не в идеальном фокусе (немного отражение)
- Опционально: legal pad с реальными почерком набросками
В промпте: «props look used — notebook open to a page with handwritten margin notes, half-empty coffee cup, phone screen with realistic UI not staged perfection».

ПОЧЕМУ ЭТО РАБОТАЕТ: зритель за 1.5s интуитивно сканирует «фейк/реал». Один-два маркера «реал» (имперфекция, lived-in environment, не-actor feel) — переключает в trust. Без маркеров — даже идеально написанный hook читается как «реклама», скролл.

═══════════════════════════════════════════════════
EXECUTIVE-CALIBRATED HUMANIZATION (волна П.19 после S21-A — критическое уточнение)
═══════════════════════════════════════════════════

H1-H10 выше написаны под **INFOBIZ founder / casual register**. Для **B2B_SAAS_ENTERPRISE / HIGH_TICKET_PRO_SERVICES / FINANCE PRO-bracket** прямое применение части H-приёмов **разрушает trust executive-аудитории**. CTO Fortune 500 в кадре с растрёпанными волосами + неглаженной рубашкой = читается «не контролирует себя», не «relatable founder».

**CROSS-REFERENCE (волна Т.3):** для B2B_SAAS_ENTERPRISE этот calibration-блок — Правило 2 из 8 в полном `B2B_SAAS_ENTERPRISE_PRESET` (см. отдельный пресет после блока EXECUTIVE vs UGC). Если работаешь на Replacement / Datadog-killer / 99.99% SLA кейсе — открой пресет полностью (8 правил + финальный чек-лист 8/8 PASS), а не только эту таблицу. Без правил 4-7 (SLA / comparative claims / migration timeline / free migration) промт пройдёт V21 но провалит V18.

**Какие H-приёмы для executive:**

| H-приём | INFOBIZ founder | Executive (B2B Enterprise / M&A / FINANCE) |
|---|---|---|
| H1 wisp + сильно растрёпанные волосы | OK relatable | **SKIP wisp/messy.** Оставить только slight facial asymmetry + day-old stubble (для male) / minimal natural makeup без heavy editing (для female). Это даёт «человека» без потери «контроля». |
| H2 паузы / hesitation | OK conversational | **Modify:** calm authority cadence — micro-pause перед ключевой цифрой, voice softens at end. НЕ «hesitation as if thinking» (читается как неуверенность). |
| H3 lived-in workspace | OK home office | **Уменьшить:** 1-2 lived маркера допустимы (coffee ring на столе, slight cable visible) — не posy + sticky notes + wrinkled rug (это discord-vibe для CTO). |
| H4 non-actor feel | OK | **Modify:** eye shifts 0.3s max (vs 0.5-0.7s для founder). Conversational tone allowed только если аудитория = peer-CTO (founder-to-CIO sales). Для board / partner — restrained authority. |
| H5 handheld micro-drift | OK | **SKIP полностью.** Executive register = tripod stable. Max 0.3px drift через tripod weight, не больше. |
| H6 wrinkled wardrobe | OK | **SKIP.** Enterprise CTO в wrinkled blazer = unprofessional. Wardrobe pressed and clean, но **quality fabric texture видна** (см. ниже «premium polish ≠ AI slick»). |
| H7 ambient + no stock music | OK | **OK + extension:** soft instrumental piano/strings UNDERNEATH ambient at -32dB (allowed PRO Enterprise). Не overlay поверх. |
| H8 eye contact 70/30 | OK | **OK** — 70/30 ratio работает для всех. |
| H9 morning puffiness + minimal makeup | OK INFOBIZ-relatable | **SKIP puffiness.** Executive register требует «well-rested authoritative». Smile lines OK (smile lines = здоровый признак). Минимальный пigment-correction makeup OK. |
| H10 props look used | OK | **Modify:** props look used **but organized** — notebook open with notes (не handwritten cross-outs everywhere), phone screen real-looking (не staged), coffee cup placed deliberately (не «выпил-поставил-забыл»). |

**Total target для executive:** **4-5 H-приёмов с calibration** (vs 6-7 для INFOBIZ).

**MEDICAL-CALIBRATED HUMANIZATION (волна Т.2 после Т.2-5 Мета).** Для MEDICAL_HEAVY (стом / косметология / IVF / пластика / дерматология) врач-founder в халате — отдельная calibration:

| H-приём | INFOBIZ founder | MEDICAL врач-founder в халате |
|---|---|---|
| H1 wisp / messy | OK relatable | **SKIP wisp / messy полностью** — врач с растрёпанными волосами = «неаккуратный врач» = убивает trust. Оставить slight facial asymmetry + day-old grooming для male / minimal makeup для female. |
| H6 wrinkled wardrobe | OK lived-in | **SKIP wrinkled халат** — мятый медицинский халат = unprofessional. Халат чистый + slight wear at sleeve (естественная носка) OK. |
| H9 morning puffiness | OK INFOBIZ-relatable | **SKIP puffiness** — врач должен выглядеть «выспавшимся, контролирующим ситуацию», puffiness = «не спит, проблемы». Smile lines OK (здоровый признак). |
| H3 lived-in environment | OK home office | **Modify:** клинический кабинет, НЕ операционная. 1-2 lived-in маркера (анатомический атлас на полке, кружка чая на столе вне рабочей зоны), НЕ posy + sticky notes. |
| H2 / H4 / H7 / H8 | OK | **OK** — calm clinical cadence, eye shifts короткие 0.3s max, ambient клиники без музыки, eye contact 70/30. |
| H5 handheld micro-drift | OK conversational | **SKIP** — premium-static-only для MEDICAL_HEAVY. Только tripod-locked. |
| H10 props look used | OK | **Modify:** props look used **but organized** (анатомическая модель на полке аккуратно, не разбросано). |

**Total для MEDICAL_HEAVY врача-founder:** 4 H-приёма (H2 + H3 modified + H4 + H7 / H8). НЕ применяй H1 wisp / H6 wrinkled / H9 puffiness / H5 handheld — каждый ломает clinical trust.

Если ученик применит INFOBIZ-дефолтный stack (H1 + H6 + H9) к врачу-Айдару → крео читается «уставший непрофессиональный врач» → trust убит → CTR падает 40-50%. Это **самая частая ошибка middle-таргетолога** на MEDICAL_HEAVY (см. Т.2-5 Мета Ошибка #2).

**PREMIUM POLISH ≠ AI SLICK — критическое разграничение (волна П.19 после S21-A):**

| AI-slick (FAIL) | Premium polish (OK для executive) |
|---|---|
| Skin без pores / subsurface — **AI tell** | Skin с visible pores + subsurface scattering + sebaceous highlights — **realism** |
| Ткань без noise / blemishes — **AI tell** | Quality fabric texture (wool weave / linen weave visible) + restrained colour palette — **production-grade realism** |
| Smooth gallery wall фон — **AI tell** | Acid-etched glass partition с subtle depth + dim background lighting — **executive-grade depth** |
| Flat lighting one source — **AI tell** | 3-point lighting (key 45° + fill 30% + rim 15%) + REFLECTION pack на metal/glass — **cinematography** |
| Saturated «vibrant» colours — **AI tell** | Restrained colour palette (charcoal / cream / muted accent) — **premium register** |

Применяй **premium polish** через явные промпт-маркеры:
- «professional 3-point lighting setup, key light 45° camera-right, fill light 30% intensity, rim light 15%»
- «REFLECTION pack on watch face / glasses / metal trim — sharp specular not soft AI gloss»
- «quality wool blazer fabric texture, visible weave, slight natural drape»
- «restrained colour palette — charcoal grey + cream + single warm accent» (не «vibrant» / «saturated»)

**Скрытые AI-маркеры в промпте (волна П.19 + волна Т.1 расширение с 5 до 20 — после Т.1-5 Мета):**

ПОЛНЫЙ ЗАПРЕТНЫЙ СПИСОК (любой из этих 20 слов в промпте → V21 проверка 6 FAIL):

| Категория | Запретные слова |
|---|---|
| **Качество без конкретики** | `cinematic` (без указания 3-point lighting / 2.39:1 / DOF f/2.8) / `professional shot` / `professionally shot` / `high quality production` / `high production value` / `studio-grade lighting` / `studio lighting` |
| **Ультра-резкость** | `8k ultra detail` / `ultra-sharp` / `ultra-realistic` / `hyper-realistic` (парадокс: эти слова палят как AI) / `crystal clear` |
| **Перенасыщенность** | `vibrant colors` / `saturated colors` / `vivid colors` / `dramatic lighting` |
| **Идеальность** | `perfect lighting` / `perfect symmetry` / `flawless skin` / `pristine` / `immaculate` / `spotless` |
| **Превосходство** | `award-winning` / `award winning` / `masterpiece` / `masterful` / `epic` / `grand` / `majestic` |
| **Привлекательность без сути** | `picturesque` / `breathtaking` / `stunning` / `mesmerizing` / `captivating` / `atmospheric` / `moody atmosphere` / `smooth motion` / `fluid motion` |

**Замены на production-фразы:**
- `cinematic` → «3-point lighting setup, key light 45° camera-right, fill 30% intensity, rim 15%»
- `8k / ultra-sharp` → «natural sharpness with subtle film grain» + «ARRI ALEXA Mini LF on Kodak Vision3 250D film stock emulation»
- `vibrant / saturated` → «restrained natural colour balance» / «warm-amber palette + cream + single accent»
- `perfect lighting` → «natural daylight 5400K from window camera-left + warm 3200K desk lamp practical»
- `flawless skin` → ВСЕГДА ANTI-AI-LOOK pack + «visible skin pores, peach fuzz, micro-blemishes near temples»
- `professional shot` → конкретная модель камеры + lens + film emulation
- `award-winning / masterpiece` → УБРАТЬ, ничем не заменять (само по себе AI-trigger)

В V21 pre-flight проверка 6: «промпт НЕ содержит ни одного из 20 запретных AI-маркеров?» — конкретный список, falsifiable.

═══════════════════════════════════════════════════
ЧАСТЬ 2 — SCRIPT RATIONALITY (как сюжет логически работает)
═══════════════════════════════════════════════════

§20 даёт **арку** (структуру) и **PROOF-ELEMENT** (что показывается). §21 Rationality проверяет **внутреннюю логику** — почему именно этот beat после предыдущего, какой mental shift у зрителя через каждый шот, что persistent / changes.

8 ПРОВЕРОК RATIONALITY (применяй перед V20):

**RAT1. Beat logic — зачем именно этот Shot после предыдущего?** (переименовано из R1 в волне П.20 для disambiguation от §3 R1-R14)
- Каждый Shot должен ДВИГАТЬ зрителя — добавлять новую информацию / эмоцию / контекст. Если Shot 2 = «то же что Shot 1, но другим ракурсом» — это перегруз без прогрессии.
- Правильно: Shot 1 устанавливает «кто и где» → Shot 2 раскрывает «что делает / что есть» → Shot 3 закрывает «зачем зрителю это нужно» (CTA + result).
- Каждый переход = explicit smash-cut / continuous motion / push-in. НЕ «декоративный crossfade».

**RAT2. Continuity check — что persistent через шоты?**
- **Герой** — Soul ID consistency через все шоты (одно лицо, одна wardrobe, одна сцена логически).
- **Объект** — если в Shot 1 был notebook, он же в Shot 2-3 (или явный transition «отложил notebook → взял phone»).
- **Action** — линия действия не прерывается без motivation (герой сидел → встал → подошёл к окну — это chain. Герой сидел → стоит на улице — это разрыв без motivation).
- **Мотив** — зачем герой делает что делает в каждом шоте. Связь с оффером.

Если что-то меняется без motivation — зритель путается → отрыв.

**RAT3. Attention progression — как удерживается зритель через 6/9/15 секунд?**
- 0-1.5s: HOOK (V17 валиден, без Жертвы)
- 1.5-3.5s: REVEAL — раскрытие что именно даёт hook (PROOF-ELEMENT появляется в кадре)
- 3.5-5.5s: RESONANCE — зритель «узнаёт себя» / видит выгоду / понимает что это для него
- 5.5-6s: CTA — конкретное действие
Для 9s: добавь 6-9s SCALE / SOCIAL PROOF (число клиентов / результаты).
Для 15s: 9-12s OBJECTION_NEUTRALIZATION + 12-15s URGENCY/CTA.

Если в одном шоте смешано «hook + reveal + resonance» — перегруз, зритель не успевает мыслить.

**RAT4. Mental model — что зритель ДУМАЕТ в каждый момент?**
- Shot 1 «герой за компьютером» → зритель думает: «кто это / зачем смотрю?» — нужен ответ через 1.5s.
- Shot 2 «героиня показывает 10 готовых проектов» → зритель думает: «о, она это сделала. как?» — нужен PROOF-ELEMENT через 1.5s.
- Shot 3 «direct eye contact + CTA» → зритель думает: «ладно, что от меня нужно?» — нужен конкретный action.

Если в любой момент зритель думает «не понимаю / что это / зачем мне» — сценарий ломается на этом шоте.

**RAT5. Stake / consequence — есть ли что-то на кону для героя?**
- Без stake — это «иллюстрация» (как сток-фото). Со stake — это история.
- Stake может быть мини: «герой уже месяц без клиентов, наконец нашла метод» (stake = месяц без работы). Не нужен hollywood-stake, нужен relatable.
- Stake для зрителя: «если я не сделаю это (CTA) — буду продолжать [нерешённую проблему]».

**БИНАРНЫЙ CRITERION для RAT5 (волна П.19 после S21-B — защита от подгона; rename из R5 в волне П.20):**
В кадре должен быть **видимый маркер stake** (хотя бы один из 3):
- (а) **Предмет** который маркирует stake (calendar с дедлайном / empty CRM-pipeline / piling bills / etc)
- (б) **Выражение лица** в Shot 1 (concentration / mild concern / focused-not-relaxed — НЕ casual smile)
- (в) **Слово в реплике** (за N дней / последний quarter / next month deadline / before close of quarter)

Если ни одного из 3 в промпте — RAT5 FAIL. «Stake встроен в категорию ниши» (например «банкротство = stake очевиден») = legitimate exception ТОЛЬКО для CRISIS_EXPERT / MEDICAL_HEAVY / HIGH_TICKET_PRO_SERVICES (где категория сама по себе = stake-signal). Для INFOBIZ / ECOM / B2B_SAAS — нужен явный маркер.

В промпте: эксплицитный stake-маркер в Shot 1 / 2 / 3 как «эмоциональный якорь».

**RAT6. Cohesion с оффером per шот:**
- Каждый шот вносит вклад в один из: WHAT (что получит) / WHY-BELIEVE (почему верить) / PROOF (доказательство) / CTA (что делать).
- Если шот **не вносит вклад** ни в один из 4 элементов → вырезать. Только декорация.
- Пример FAIL: Shot 2 «герой смотрит в окно задумчиво на закат» — не вносит вклад. Если только это не PROOF «процесс работы», но даже тогда — есть способы показать процесс конкретнее.

**RAT7. "Why now?" — почему этот сюжет именно сейчас?** (волна П.19 — ОПЦИОНАЛЬНАЯ проверка после S21-B)
- Если оффер действительно urgent (deadline / scarcity / time-anchor) — это видно в кадре (calendar / countdown / event-context).
- Если оффер evergreen (нет time-anchor) — НЕ создавай fake urgency через scenery. Лучше: эксперт + социальное доказательство.
- Проверка: убери из кадра все time-маркеры — теряется ли смысл? Если нет — значит scenery был decorative, можно проще.
- **Опциональная проверка** — в 80% кейсов оффер evergreen и RAT7 проходит автоматически. Применяй только когда оффер действительно содержит time-anchor / urgency-element.

**RAT8. "What if I miss this?" — что зритель упускает?**
- Завершающий beat должен давать зрителю явное ощущение «я что-то упускаю если не сделаю CTA».
- Это НЕ страх / scarcity / манипуляция. Это **рациональная оценка** ценности: «если не запишусь — буду делать то же что делал, без этого инструмента».
- В промпте: эксплицитный «losing-out» frame в Shot 3 (e.g., founder говорит «или попробуй, или останься со старым подходом — твой выбор» — это neutral, не давление).

═══════════════════════════════════════════════════
V21 VALIDATION (Humanization + Rationality финальный pre-flight)
═══════════════════════════════════════════════════

Перед выдачей промпта — 5-проверочный pre-flight V21:

**Humanization (3 проверки):**
1. **Минимум 3-4 приёма H1-H10 применены?** Если только «direct eye contact + ANTI-AI-LOOK pack» — недостаточно для talking-head 6s. Нужны микро-несовершенства + lived-in environment + non-actor feel + естественная речь.
2. **5 признаков AI-видео отсутствуют?** Perfect symmetry / Glossy texture / Identical smile / Stock environment / Continuous monotone — все 5 явно сняты через промпт-маркеры.
3. **Soul ID не выглядит как «hired actor for stock photo»?** Если внешность героя в кадре «professional headshot polish» — добавь H1, H4, H9 явно.

**Rationality (2 проверки):**
4. **Прошёл RAT1-RAT8?** Каждый шот двигает зрителя, continuity сохранена, attention-progression выстроена, mental model понятна, есть stake, cohesion с оффером per шот.
5. **Mental model walk-through:** Опиши в одну фразу что зритель думает в Shot 1 / Shot 2 / Shot 3. Если в любом шоте «не понимаю что это / зачем» — переделай сюжет, не косметику.

При FAIL V21 — НЕ выдавай промпт. Переписывай через H/R-checks.

═══════════════════════════════════════════════════
ANTI-PATTERNS HUMANIZATION + RATIONALITY (волна П.19)
═══════════════════════════════════════════════════

**A1. «AI-actor look»** — Soul ID выглядит slick, лицо без следов жизни, причёска идеальная. Зритель чувствует «реклама», скролл за 1.5s. FAIL Humanization.

**A2. «Stock environment»** — переговорная с glass partition, идеальный desktop, ничего «жилого». Не убеждает founder-narrative. FAIL Humanization.

**A3. «Театральная подача»** — голос как TV-ведущего, каждое слово громко, нет пауз. Не conversational. FAIL Humanization H2.

**A4. «Декоративные шоты»** — Shot 2 = герой смотрит в окно задумчиво, без вклада в WHAT/PROOF/CTA. FAIL Rationality RAT6.

**A5. «Привлекательный закат без логики»** — последний beat = founder на крыше на закате. Красиво, но не закрывает CTA. FAIL RAT8 + RAT6.

**A6. «3 шот без motivation»** — герой за столом → герой на улице → герой держит CTA-табличку. Action-chain разорван, continuity сломана. FAIL RAT2.

**A7. «Hook + Reveal + Resonance в одном шоте»** — Shot 1 содержит всё: и кто, и что делает, и зачем зрителю. Перегруз, зритель не успевает мыслить. FAIL RAT3.

**A8. «Локация-телепорт без prop continuity»** (волна П.19 после S21-B) — герой за столом дома → герой на улице → герой в кафе за 6s без motivation-chain и без persistent prop. Зритель ловит «WAIT, где она теперь?» вместо story. FAIL RAT2 + RAT4. Fix: либо single location, либо multi-location с PROP CONTINUITY (один и тот же notebook / phone / папка проходит через все 3 локации = «один день в жизни», создаёт chain).

═══════════════════════════════════════════════════
ДОПОЛНЕНИЕ §21 (волна Т.1 после meta-анализа)
═══════════════════════════════════════════════════

**ВЕСА H-ПРИЁМОВ — какие даёт максимум authenticity (волна Т.1 после Т.1-5 Мета):**

H-приёмы НЕ равноценны. Если ученик применяет 3-4 из 10 (минимум по V21) — выбор должен быть осознанным. Приоритет:

| Вес | Приёмы | Эффект |
|---|---|---|
| **H-weight=5 (CRITICAL — без них AI-палево с первого кадра)** | H2 (micro-stutters / паузы в речи), H3 (lived-in environment с одним явным prop с признаком жизни), H4 (eye glance off-camera 1 раз минимум) | Дают 70% authenticity. Если ученик применяет ТОЛЬКО эти 3 — V21 PASS. |
| **H-weight=3 (IMPORTANT — +30% к authenticity)** | H1 (асимметрия + smile lines), H6 (lived-in wardrobe slight wrinkles), H7 (ambient audio без stock-music), H8 (eye contact 70/30) | Усиление trust для talking-head формата. Применяй если талкинг-хед основная сцена. |
| **H-weight=1 (POLISH — украшение)** | H5 (handheld micro-drift), H9 (morning puffiness), H10 (props look used — если H3 уже покрывает) | Без них работает. Применяй для PRO-режима если есть запас по бюджету. |

**ПРИОРИТЕТ ПРИМЕНЕНИЯ:** для middle-таргетолога — H2 + H3 + H4 минимум (3 critical). Для STANDARD — добавь H1 + H8 (5 приёмов). Для PRO talking-head hero — добавь H7 (6 приёмов).

---

**R9 — MESSENGER-PROP CHECK (волна Т.1 после Т.1-5 Мета):**

Если в кадре screenshot мессенджера / уведомление / chat UI — сверь с audience locale из Чата 1 / PROMPT-2:

| Гео / Audience | Default messenger | Альтернатива |
|---|---|---|
| **PL-LOCAL** (Польша местные) | WhatsApp 78% | Messenger 65% |
| **RU-DIASPORA в Польше** | Telegram 71% | WhatsApp 58% |
| **UA-DIASPORA в ЕС** | Telegram 80% | Viber 50% |
| **DE-LOCAL** (Германия местные) | WhatsApp 87% | Signal 40% |
| **US / UK** | iMessage 60% | WhatsApp 45% |
| **CZ / KZ / BY / RU-CIS** | Telegram default | WhatsApp вторично |

**FAIL R9** если messenger в кадре ≠ audience default без явного обоснования в брифе. Пример FAIL: PL-LOCAL аудитория + Telegram screenshot в кадре = PL-зритель подсознательно отфильтрует «это для русских, не для меня», CTR упадёт 30-40%.

---

**R10 — GDPR / NDA для PROOF-screenshot (волна Т.1 после Т.1-2 Критик + Т.1-5 Мета):**

Если PROOF-ELEMENT = screenshot с реальными именами / лицами клиентов:
- **Blur лица / имени** = AI-trigger (palится как fake). НЕ использовать.
- **Initials overlay** («M.K.» / «Анна K.») = GDPR-safe И не AI-trigger. Использовать всегда вместо blur.
- **Полные имена с письменным consent** = OK для крео (sign-off от каждого клиента + dated до запуска).
- **Аватарка/photo клиента** = только с signed release. Без — generic avatar placeholder.

В §21 V21 pre-flight добавить проверку 7: «Если PROOF содержит screenshot с реальными именами — используется initials overlay (а не blur) ИЛИ есть signed consent для каждого имени?»

---

**V19 BIOCLAIM — класс-правило (волна Т.1 после Т.1-5 Мета, расширение Q-INFOBIZ-V19):**

Раньше требование sign-off было локальным «для INFOBIZ-Authority с числом учеников». Расширение волны Т.1 — **класс-правило**:

**V19-BIOCLAIM срабатывает на ЛЮБОЙ biographical claim с количественным элементом** (число / год / процент / срок). Применяется ко ВСЕМ профилям:

| Профиль | Типичный biographical claim | V19-BIOCLAIM trigger |
|---|---|---|
| INFOBIZ | «47 студентов», «за 2 года 200 выпускников» | ДА |
| MEDICAL | «15 лет практики», «1200 операций», «98% успеха» | ДА |
| KIDS_PARENTS | «помогла 200 семьям», «10 лет работы с детьми» | ДА |
| B2B_SAAS | «работали с 5 банками», «клиенты в 12 странах», «47k MAU» | ДА |
| HIGH_TICKET / PRO_SERVICES | «47 closed M&A mandates 2020-2024 per Mergermarket league table (DACH mid-cap sub-cat)» / «$5M aggregated transaction volume per intake records, individual mandate values vary» / «Partner since 2015 per {State} Bar admission» / «$2B AUM per Form ADV Part 1 Item 5 (SEC.gov)» | ДА + methodology disclosure + period + scope + Bar/SEC/FINMA registration overlay (НЕ self-attested LinkedIn — cross-ref HIGH_TICKET_PRO_SERVICES_PRESET Правило 5) |
| CRISIS_EXPERT | «12 лет в адвокатуре», «47 банкротств защитил» | ДА |

**Артефакт sign-off обязателен:**
- Скриншот письма клиента с подтверждением цифры
- Запись звонка с timestamp
- Notion-запись с timestamp ≤ 7 дней до запуска
- Подписанный лист с реальными именами клиентов (для cohort-claims)

**Без артефакта V21 pre-flight FAIL.** Заменяй на generic формулировку («больше 40 выпускников» вместо «47»; «многолетняя практика» вместо «15 лет») ИЛИ удаляй число вообще.


## 10. ПРОФИЛЬНЫЕ ПРЕСЕТЫ + SUB-PACKS (профиль-матрица, все PRESET, GREY, бенчмарки, СНГ-адаптация)

═══════════════════════════════════════════════════
БЮДЖЕТНЫЕ РЕЖИМЫ
═══════════════════════════════════════════════════

Промпты адаптируются под бюджетный режим клиента (определяется через `client-profile`). Не лей PRO-стек на LITE-проект — большая часть Cinema Studio + Soul Cast не оправдается экономикой.

| Режим      | Workspaces                                              | Модели                              | Soul ID  | Раскадровка | Hook    |
|------------|---------------------------------------------------------|-------------------------------------|----------|-------------|---------|
| LITE       | Marketing Studio                                        | Nano Banana 2 + Kling 3.0           | нет      | макс 3      | H1, H4 (multi-shot) + H3, H7 (single-shot only) |
| STANDARD   | Marketing Studio + Cinema Studio (для hero-крео)        | Kling 3.0 / Seedance 2.0 default, Veo 3.1 premium | 1 герой  | 3-5         | H1-H7   |
| PRO        | Cinema Studio 3.5 + Marketing Studio + Higgsfield Audio | Veo 3.1 default, Seedance 2.0, Soul; Sora 2 (если API access) для hero UGC + диалоги + физика | Soul Cast (2-3 героя) | 5-7 | H1-H7 |

LITE-логика: быстрая генерация, простой image+motion, минимум packs (только ANTI-AI-LOOK + PORTRAIT CU где нужно).
LITE hook-расширение: H3 (dopamine — slow-mo, разлив, удар) и H7 (anomaly — странная деталь, аномальный свет, контраст ожидания) разрешены в LITE ТОЛЬКО для single-shot 5s или статики. Multi-shot H3/H7 в LITE запрещены — drift между шотами съест эффект. H4 (direct address) в LITE без Soul ID работает только через UGC-актёра или text-overlay прямого обращения.

STANDARD-логика: добавляешь LIGHT CONSISTENCY на раскадровку, Soul ID на главного героя, HANDS IN FRAME где руки в кадре.

ПРИМЕЧАНИЕ к STANDARD-режиму: Veo 3.1 в STANDARD оправдан только для hero-крео (1 промт из 3-5 в кампании, не как дефолт). Veo 3.1 + сложная сцена (split-screen / multi-shot 3+ / редкий wardrobe) → 6-10 ретраев, что съедает бюджет STANDARD-режима. Дефолт STANDARD = Kling 3.0 или Seedance 2.0. Veo 3.1 — premium опция для одного hero.

PRO-логика: полная палитра. Soul Cast, ECU FACE pack, REFLECTION pack, multi-character anchoring, audio через Higgsfield Audio, raster-style packs. Sora 2 — опция для hero-крео если у клиента есть прямой API access (UGC + диалоги + физика в 2026 лучше Kling 3.0). Web-доступ к Sora 2 закрыт OpenAI с апреля 2026 — через Higgsfield/Magnific UI недоступна.

Sora 2 для LITE и STANDARD по умолчанию недоступна (нет API access у большинства учеников). Дефолт стека остаётся Kling 3.0 / Veo 3.1 / Seedance 2.0.

═══════════════════════════════════════════════════
ПРИВЯЗКА К ПРОФИЛЯМ НИШ
═══════════════════════════════════════════════════

Краткие пресеты по 10 каноническим профилям из `client-profile` + дополнительные.

CTA MATRIX (canon-first + A/B backup) — для всех профилей ниже:

Канон сейчас — одна CTA per профиль (см. колонку «CTA #1 canon»). Это жёсткое правило для дефолтного крео. Колонки #2/#3 — backup-варианты для A/B-тестов в пачке (НЕ смешивать в одном крео — одна CTA на крео).

| Профиль | CTA #1 canon (default) | CTA #2 backup (A/B) | CTA #3 alternative |
|---|---|---|---|
| LOCAL_SERVICE медицина | Запишитесь на консультацию | Узнайте о методе | Получите расчёт |
| LOCAL_SERVICE прочее | Запишитесь / Закажите | Узнайте подробнее | Получите расчёт |
| INFOBIZ | Узнайте программу | Получите программу | Записаться в поток |
| ECOM | Закажите / Купите | Оформите подписку | Получите бесплатную доставку |
| ECOM_PROSTOY | Купить за {цена} | В корзину | Заказ за минуту |
| B2B_SAAS | 14-day trial, no credit card | Book a demo | See pricing |
| B2B_SAAS_ENTERPRISE | Book a demo | Talk to sales | Get a proposal |
| HIGH_TICKET | Запишитесь на консультацию | Получите indicative {valuation/расчёт} | Связаться с партнёром |
| HIGH_TICKET_PRO_SERVICES (M&A / LEGAL / private banking — переименовано в П.9) | Indicative valuation | Confidential intro call | Speak to partner |
| CRISIS_EXPERT | Запишитесь на 48-часовой аудит | Узнайте формат | Связаться сейчас |
| REAL_ESTATE_EXPAT | Получите подборку | Назначьте Zoom | Связаться с broker |
| WELLNESS_HEALTH_RESTRICTED | Узнайте о продукте | Free 30-day money-back | Pre-order |
| WELLNESS_HEALTH_RESTRICTED_USA | Learn more | 30-day money-back | First-order discount |
| GREY_NICHE (любой) | Узнайте больше | Получите программу | Записаться |
| SUBSCRIPTION_BOX | Оформите подписку | Подарите подписку | Первый месяц 99 {валюта} |
| KIDS_PARENTS | Запишитесь на пробное | Узнайте расписание | Связаться с тренером |
| RELIGIOUS_TRAVEL | Забронировать место | Узнать программу | Связаться с гидом |
| EXECUTIVE_COACHING | Запишись на discovery-call / стратегическую сессию | Узнайте программу | Get a proposal |

Правила:
— CTA #1 = default для одиночного крео и для hero в пачке.
— CTA #2 / CTA #3 = только для A/B-вариаций (одна CTA на крео, не смешивать в одном кадре).
— Для GREY_NICHE — см. отдельный расширенный блок «CTA matrix для GREY» ниже (после пресета GREY_NICHE) — там запрещённые формулировки и подкатегории.
— Для B2B_SAAS Replacement (миграция с конкурента) — CTA #1 может смещаться на «Мигрируйте за 24 часа» — см. MIGRATION-FRICTION блок в B2B_SAAS пресете.

INFOBIZ (онлайн-курсы, инфопродукты):
— Workspace: Marketing Studio
— Модель: Kling 3.0 / Seedance 2.0
— Packs: PORTRAIT CU + ANTI-AI-LOOK + HANDS IN FRAME (если показ экрана)
— Hook: H4 (direct address) или H2 (curiosity loop)
— Format: 9:16 + 6-7s
— Особенность: герой с прямым взглядом в линзу + конкретная цифра в первой фразе
— **§19B INFOGRAPHIC обязательно к рассмотрению** для лид-магнит-крео («N промптов в M стилях» — STYLE-SWATCHES-GRID), outcome-метрик курса (INFOGRAPHIC-CHART с substantiation), структуры курса (ANIMATED-DIAGRAM). 30-50% INFOBIZ-креативов = статика-инфографика, не Soul ID-видео. На LITE — Шаг 1 only (Nano Banana 2 статика, без Veo/Kling).

LOCAL_SERVICE (стоматология, бьюти, фитнес):
— Workspace: Marketing Studio
— Модель: Veo 3.1 / Kling 3.0
— Packs: PORTRAIT CU + BACKGROUND SEPARATION + ANTI-AI-LOOK
— Hook: H1 (pattern interrupt — врач в халате с инструментом)
— Format: 9:16 + 5-6s
— Особенность: гео-привязка в кадре (название улицы / района на табличке если рендерим — Nano Banana 2 для текста)
— **§19B INFOGRAPHIC обязательно к рассмотрению** для прайс-крео (COMPARISON-CARDS — 3 пакета услуг / абонементы / тарифы), MEDICAL_HEAVY explainer (EDUCATIONAL-PROGRESSION — анатомическая прогрессия типа «3 года без зуба → что с костью»). 30-50% LOCAL_SERVICE-креативов с прайсом = COMPARISON-CARDS статика. На LITE — Шаг 1 only.
— ВАЖНО: если подпрофиль = MEDICAL_HEAVY (стоматология, инвазивная косметология, дерматология, пластика) — переключайся на блок «premium-static-only → подсекция MEDICAL_HEAVY стоматология» (см. соответствующий раздел). Часть приёмов LOCAL_SERVICE недоступна. **MEDICAL_HEAVY EDUCATIONAL-PROGRESSION** — только illustration / cross-section / schematic, НЕ photoreal лица пациентов.

ECOM (D2C-каталог, физический товар):
— Workspace: Marketing Studio product showcase
— Модель: Seedance 2.0 (product spin) / Nano Banana 2 (статика с ценой)
— Packs: FABRIC + REFLECTION + BACKGROUND (для frosted-amber / parfum / crystal — TRANSPARENCY commercial sub-scope)
— Hook: H3 (dopamine — slow-mo распаковка)
— Format: 1:1 или 4:5 + 5s
— Особенность: продукт занимает 70% кадра, фон нейтральный, цена через Nano Banana 2 если нужна на картинке
— **§19B INFOGRAPHIC обязательно к рассмотрению** для каталог-крео (COMPARISON-CARDS — сравнение 3 продуктов / размерная сетка), outcome-метрик (INFOGRAPHIC-CHART — «выросли X% за месяц» с substantiation per V18). LITE — Шаг 1 only.
— **Soul ID опционален для ECOM_IMPULSE / ECOM_PROSTOY** — только в outro brand frame (founder reveal 3-5s, 1 крео из пачки), НЕ дефолт для product-showcase. Лицо мастера в handmade / craft / artisan = trust-якорь, оправдано на outro. Для outro-сцены достаточно 8-10 фото single-shot (по нижней границе single-shot static portrait). Multi-shot wardrobe для founder не нужен — outro один кадр.

B2B_SAAS (продажа софта бизнесу):
— Workspace: Cinema Studio
— Модель: Veo 3.1
— Packs: PORTRAIT CU + LIGHT CONSISTENCY + ANTI-AI-LOOK + HAIR (short executive crop)
— Hook: H2 (curiosity — кадр экрана с метрикой)
— Format: 9:16 (Meta — дефолт). 16:9 (LinkedIn) — опционально, по запросу ученика. Длительность 7-9s.
— Особенность: герой = LPR-инициатор (HR / ops). Кадр офиса, screen capture через DOP.
— UI mockup CRM / dashboard — ВСЕГДА через §19A UI MOCKUP PIPELINE (Nano Banana 2 → @image1 → Veo), не напрямую в Veo.
— **§19B INFOGRAPHIC обязательно к рассмотрению** для explainer-крео (ANIMATED-DIAGRAM — «как работает наш AI», onboarding flow), conversion funnel (INFOGRAPHIC-CHART — trial-to-paid metrics), pricing tiers (COMPARISON-CARDS — 3 plans с региональными флагами). Параллельно с §19A UI MOCKUP, не вместо.
— DEMO-SCREENCAST integration: активируется ТОЛЬКО если ученик явно запросил screencast вне Meta-кампании (дефолт = Meta+IG). Higgsfield НЕ генерирует реальные screencast интерфейса. Для middle-funnel (видевшие top-funnel но не заявившие demo) и trial-to-paid nurturing закажи DEMO-SCREENCAST через Loom / ScreenStudio / Tella параллельно. Это вне твоей выдачи, но критично для конверсии trial→paid. В пачку креативов: 2-3 Higgsfield (top-funnel) + 1 Loom screencast (middle-funnel) = cross-format.

DEMO-SCREENCAST integration по бюджетному режиму (активируется ТОЛЬКО если ученик явно запросил screencast вне Meta-кампании — дефолт = Meta+IG):
— LITE (до $500/мес) — Loom Free (5 min limit, 25 video cap). Достаточно для квалифицированной лиды.
— STANDARD ($500-$3000/мес) — Loom Pro ($15/мес) или Tella ($25/мес). Без лимитов, branding, analytics.
— PRO ($3000+/мес) — ScreenStudio (одноразово $129) для cinematic-screencast + Tella Team для продакшена. Подходит для hero-крео.
— Workflow: Higgsfield-крео + Loom/ScreenStudio screencast параллельно. В Meta пачкинг — отдельные креативы в пачке.
— Запрет: НЕ генерируем screencast через Higgsfield (модели не рендерят real UI). Только реальная съёмка экрана.

MIGRATION-FRICTION ZAHODY (для Replacement SaaS — переход с конкурента):
— Hook кандидат: «Мигрируйте с {generic competitor} за 24 часа без потери данных. Бесплатная миграция нашей командой.»
— Сегментация: Most-aware (уже использует другой SaaS, ищет лучше)
— Главное возражение: «миграция сложная» / «команда не хочет менять»
— Mitigation в крео: «migration assistance», «no downtime», «keep your data», «48-hour switch»
— Запрет: named конкурент в крео (Волна М) → переформулировать в «existing CRM» / «другая платформа»
— В Meta primary text: можно named конкурент если sales-pitch context (post-click)

EXECUTIVE vs UGC — ЖЁСТКОЕ ПРАВИЛО для B2B_SAAS / HIGH_TICKET / B2B_PROFESSIONAL_SERVICES / EXECUTIVE_COACHING:

Всегда executive cinematic, НИКОГДА UGC casual handheld как дефолт. Эти профили продают на 200+ USD/seat (SaaS) или 5000+ USD чек (coaching / services) — UGC-формат снижает воспринимаемую авторитетность и убивает конверсию даже при правильном таргетинге.

Wardrobe:
— OK: suit / dress shirt / blazer / smart casual «tech-CEO uniform» (charcoal grey wool suit + white dress shirt без галстука = универсал).
— Запрет: футболка / худи / casual everyday / «домашняя кофта».
— **SMB-tier** — это правило мягче, см. «EXECUTIVE wardrobe — SMB vs Enterprise разделение» (строка ~2962) + B2B_SAAS_SMB_PRESET §3118: для SMB худи / tee + smart-casual blazer OK, а suit + tie запрещён (читается как enterprise-overdress). Запрет «футболка / худи» выше относится к Enterprise / HIGH_TICKET, не к SMB-tier.

EXECUTIVE wardrobe matrix — suit с галстуком vs без vs smart-casual:

**SCOPE NOTE (волна П.8):** matrix покрывает **EU / USA контексты** (EU Vorstand / Silicon Valley tech / smart-casual coaching / academic). Для **Asia Tier-1 банк** (Tokyo / Seoul / Singapore / HK) — отдельные строки ОТСУТСТВУЮТ (после Q51 закрыта через out-of-scope gate в client-profile: Asia формально вне scope курса). Если ученик заказывает B2B для Asia — `client-profile` срабатывает на отказ.

**UAE row (волна П.15, закрытие Q59) — для русскоязычного релоканта-коуча / HIGH_TICKET-эксперта в Дубае (НЕ local Emirati):** (строки вынесены в таблицу ниже, под разделитель)

| Контекст / целевая аудитория | Wardrobe | Когда выбирать |
|---|---|---|
| **UAE русскоязычный релокант (HIGH_TICKET / EXEC_COACHING / B2B)** | Modern tech-CEO suit без tie (charcoal grey wool + white dress shirt, top button open) + tropical weight ткани (lightweight wool / linen-blend, не heavy worsted), металлический браслет часов | Background: modern Dubai CBD glass office (DIFC / Business Bay), Burj Khalifa skyline через окно, marble / stone interior. НЕ kandura/ghutra (это для local Emirati). Wardrobe consistency: один Soul ID flight = одна wardrobe-вариация |
| **UAE local Emirati / Saudi (вне scope курса по client-profile out-of-scope gate)** | kandura + ghutra (white + checkered red/white в зависимости от country), сandura starched, ghutra с iqal | Только если ученик явно нарушил scope-гейт и требует — flag WARN, redirect в out-of-scope (Asia/MENA local не покрыт курсом) |
| **Traditional B2B / EU Vorstand / банкинг / Big-4 consulting** | Suit + tie (классический темный или charcoal + галстук classic narrow) | EU traditional B2B, banking, Big-4 audit / consulting, legacy enterprise sales. Аудитория = consensus-driven board, ожидает «классический register». |
| **Modern tech / Silicon Valley / scale-up founder** | Suit БЕЗ галстука (charcoal grey wool + white dress shirt, top button open) | Tech, SaaS, modern professional services (consulting тип BCG modern / strategy boutiques), B2B SaaS founder-CEO. «Tech-CEO uniform», современный default. |
| **Smart-casual / wellness / R&D / academic** | Lab coat + collared shirt / casual blazer + plain tee / chinos + button-down | Wellness, healthcare R&D, academic, medical (talking-head врача в халате), educational coaches. |
| **HIGH_TICKET-diaspora / executive coaching** | Wardrobe matches register сегмента: traditional EU diaspora = with tie; tech-Cyprus / Almaty re-located = without tie | По segment-context: traditional → tie, modern → без. |
| **Без выбора / непонятно** | Suit БЕЗ галстука (modern bias) | Дефолт. Современный register более универсальный — даже в traditional B2B читается приемлемо, тогда как «traditional with tie» в tech-context выглядит outdated. |

GUARDRAIL: НЕ микшируй внутри одной flight (P1/P2/P3 одного клиента). Wardrobe consistency через flight — FABRIC pack дословный повтор + один и тот же variant (с галстуком ИЛИ без, не комбинируй).

EXECUTIVE wardrobe — SMB vs Enterprise разделение (важно — не лей enterprise-look на SMB-tier):

| Tier | Чек | Wardrobe | Setting |
|---|---|---|---|
| **Enterprise** (PRO, 50k+ USD deal / 300+ USD/seat SaaS) | Большой контракт | Traditional suit + tie ИЛИ modern tech-CEO suit без tie | Strict boardroom / glass partition executive office / formal interior |
| **SMB** (STANDARD, 30-300 USD/мес SaaS / 5-50k USD service) | Малый-средний | Smart-casual blazer + tee/smart shirt. БЕЗ tie | Modern co-working / cafe / open office / glass partition meeting room. НЕ strict boardroom (выглядит overdressed для SMB) |
| **Founder-tech** (SaaS / B2B tech) | Любой tier | Smart-casual blazer + plain tee | Tech-CEO uniform. НЕ suit + tie (читается overdressed) |
| **Founder-services** (юр, мед, finance) | Любой tier | Suit без tie modern OR suit с tie traditional (выбор по сегменту аудитории) | Office / clinic / boardroom — соответствует профессии |
| **Coaching** (executive / life / business) | Любой tier | Smart-casual ИЛИ soft executive (academic register — blazer + collared shirt) | Studio / library / minimalist studio interior |

GUARDRAIL: B2B_SAAS SMB-tier (39-299 USD/мес чек) — НЕ применяй strict boardroom + suit + tie (это enterprise-presentation). Делай smart-casual blazer + tee/smart shirt в modern co-working / glass partition. Иначе founder читается как «выдрессированный консультант», а не как «свой» для SMB owner.

Setting:
— OK: современный офис / конференц-зал / executive boardroom / loft с designer фурнитурой / glass partition / professional lighting.
— Запрет: кухня / гостиная / кафе / уличная локация «как у инфлюенсера».

Camera & workspace:
— OK: Cinema Studio + Veo 3.1 (или Kling 3.0 для статичного hero-shot). Tripod-shot / locked-off framing / controlled handheld dolly (с явной пометкой «intentional, controlled — not shaky»).
— Запрет: Marketing Studio handheld phone-shake / TikTok creator vibe / vlog-style.

Talking head:
— OK: Tripod-locked CU, 50-85mm, f/2.8-f/4, direct eye contact.
— Запрет: «телефон в руке» / arm extension shake / iPhone front-cam vibe.

Исключения (где UGC всё-таки можно):
— B2B_SAAS PLG self-serve (Notion-tier, 10-30 USD/seat) — UGC допустим.
— B2B_SAAS founder-led startups — handheld dolly с явной мотивацией.
— НИКОГДА: enterprise SaaS 300+ USD/seat, executive coaching 5k+ USD, high-ticket professional services (юристы, financial advisors, ip-агенты).

GUARDRAILS:
— Если ученик просит «handheld phone-shake» для этих профилей — переспроси: «уверен? для X USD/seat это снижает воспринимаемую авторитетность. Альтернатива — controlled handheld dolly в Cinema Studio. Подтверди если всё равно phone-shake.»
— Если в Intake PROFILE=B2B_SAAS_ENTERPRISE → дефолт workspace = Cinema Studio, агент НЕ предлагает Marketing Studio без явного запроса.

═══════════════════════════════════════════════════
B2B_SAAS_ENTERPRISE_PRESET — отдельный пресет (волна Т.3 после S-Т.3-5 мета-аудита)
═══════════════════════════════════════════════════

Контекст: B2B_SAAS_ENTERPRISE имеет систематически иной риск-профиль, чем B2B_SAAS SMB (PLG / founder-led). До волны Т.3 правила были рассыпаны по 5 разным секциям (§19A UI MOCKUP / §20 SLA-claim / §21 EXECUTIVE-CALIBRATED / MIGRATION-FRICTION / EXECUTIVE vs UGC). Агент при сборке промта для CTO Fortune 500 (Replacement / Datadog-killer / Snowflake-alternative тип кейса) терял часть guardrails — выходили промты с дискламерами вроде «Datadog killer» (disparagement) или «99.99% SLA на 50k хостов» (financial commitment без contract). Этот пресет — единая точка истины.

**КОГДА АКТИВИРУЕТСЯ B2B_SAAS_ENTERPRISE_PRESET:**

Профиль клиента = B2B_SAAS, и любой из триггеров:
— Чек 300+ USD/seat/мес ИЛИ deal-size 50k+ USD/год.
— Целевая аудитория = CTO / VP Engineering / CISO / Head of Platform Fortune 500 / enterprise mid-market.
— Hook содержит named competitor («лучше чем X», «X killer», «replacement for X», «N-x faster than X»).
— SLA-claim в Dialogue / EXACT STRING / overlay («99.X% uptime», «X-nines SLA», «zero downtime»).
— Replacement / migration кампания (переход с существующего vendor — Datadog / Snowflake / Splunk / New Relic / Salesforce / etc).
— Профиль клиента содержит флаг `tier=enterprise` или sub-profile `B2B_SAAS_ENTERPRISE`.

Если хотя бы один триггер — все 8 правил ниже **обязательны**. Не «опционально к рассмотрению».

**ПРАВИЛО 1 — Workspace + модель (дефолт жёсткий, не предложение):**
— Workspace = Cinema Studio (НЕ Marketing Studio, НЕ переспрашивай).
— Модель = Veo 3.1 (НЕ Kling — у Kling executive face uncanny на CU 50-85mm).
— Packs = PORTRAIT CU + LIGHT CONSISTENCY + ANTI-AI-LOOK + HAIR (short executive crop) + FABRIC (suit / dress shirt fibre detail).
— UI mockup CRM / dashboard в кадре = ВСЕГДА через §19A UI MOCKUP PIPELINE, не напрямую в Veo.
— Format = 16:9 + 9-12s (LinkedIn primary placement) / 9:16 + 9s (Meta secondary).

**ПРАВИЛО 2 — EXECUTIVE-CALIBRATED HUMANIZATION (SKIP-список):**

Запускается автоматически — не ждёт явного запроса. Из §21 H-стэка для Enterprise CTO:
— SKIP: H1 wisp temple (executive crisp), H5 handheld micro-drift (Cinema Studio = locked tripod), H6 wrinkled wardrobe (charcoal grey wool suit pressed, dress shirt crisp), H9 lived-life face (puffiness под глазами читается как «он не контролирует себя»).
— MODIFY: H2 natural speech cadence (без «эм» / «ну» — но natural pacing), H4 not-actor Soul ID (cast executive, не stock-CEO).
— OK: H3 lived-in workspace (glass partition office с реальными papers / coffee mug — НЕ AI-stock «cleanest desk in the world»), H7 ambient audio без stock-music, H8 eye contact 70/30, H10 props look used (notebook with edges worn, pen с brand-marking).

Без этой калибровки H-стэк INFOBIZ-уровня (wisp / wrinkled / handheld) разрушает trust executive-аудитории — CTO Fortune 500 читается как «consultant who can't even iron his shirt».

**ПРАВИЛО 3 — PREMIUM POLISH vs AI SLICK граница (для glass-partition office):**

Glass-partition executive office (типичный setting B2B Enterprise) — высокий риск AI-slick фейла:
— OK: REFLECTION pack для glass partition (реалистичные отражения с micro-imperfection — отпечатки пальцев на стекле, лёгкая пыль), LIGHT CONSISTENCY (один key-light + fill, не «award-winning cinematography»), фокус с micro-depth-of-field на лице (f/2.8-f/4).
— FAIL: «cleanest glass possible» (slick AI), «pristine reflection» (slick AI), «picturesque office» (slick AI), «award-winning lighting» (slick AI), идеально гладкая кожа без пор (AI tell).
— RULE: prompt-фраза «with natural micro-imperfections — light dust on glass partition, used notebook on desk, slight skin texture detail» включается в EVERY B2B Enterprise промт.

**ПРАВИЛО 4 — SLA-claim substantiation (cross-reference V18):**

Любой SLA-claim в Dialogue / EXACT STRING / overlay = juridical commitment с financial penalty при breach (service-level credits). Не маркетинговый «aspirational target».

Триггеры SLA-claim: «99.X% uptime», «X-nines SLA», «zero downtime guarantee», «sub-N-ms latency guarantee», «N-9s availability».

PASS условия:
1. У клиента есть подписанный SLA contract template с конкретным customer (не «target metric» из internal OKR).
2. Substantiation = SLA-document + service-credit policy + audit-attestation (SOC 2 Type II reference / ISO 27001).
3. Если substantiation НЕТ → ОБЯЗАТЕЛЬНАЯ переписка в «target 99.99%» / «designed for 99.99%» / удалить из оффера.

FAIL пример: `Dialogue: "We guarantee 99.99% SLA across your 50k hosts"` без contract → V18 FAIL + meta-policy-checker B2B Enterprise категория.

PASS пример: `Dialogue: "Our platform is designed for 99.99% availability, with service credits per signed SLA"` — qualified, нет absolute commitment.

**ПРАВИЛО 5 — Comparative claims / named competitor (cross-reference Волна М + meta-policy-checker B2B Enterprise категория):**

Триггеры: «X killer», «alternative to X», «replacement for X», «N-x faster than X», «#1 alternative to X», «better than X by N%», disparagement language («X is broken / X can't scale / X is legacy»).

PASS условия:
1. В крео — НИКОГДА не называть competitor exact string (даже если у клиента есть бенчмарки). Generic alias: «legacy observability tool», «existing CRM», «current vendor», «another platform».
2. В Meta Ad Manager primary text — competitor exact name DOPUSTIM только если sales-pitch context (post-click, warm/retargeting), не cold TOF.
3. Бенчмарк-число («N-x faster») — требует named benchmark source + год + same-workload-context. Без — FAIL V18.
4. Disparagement («X is broken») — ВСЕГДА FAIL независимо от substantiation (Meta CSR + risk of competitor counter-claim / lawsuit). Переписать в neutral comparison: «built for modern cloud-native workloads».

FAIL пример: `EXACT STRING: "Datadog killer · 10x faster · #1 alternative"` → 3 нарушения (named competitor + disparagement + N-x без benchmark).

PASS пример: `EXACT STRING: "Built for cloud-native observability"` + Dialogue про migration без названия конкурента.

**ПРАВИЛО 6 — MIGRATION-FRICTION timeline realistic для Enterprise:**

MIGRATION-FRICTION zahody block (выше) для SMB B2B_SAAS использует «24 часа миграция». Для Enterprise — «24 часа» = misleading (Enterprise миграция = 4-12 недель cutover plan с parallel-running, dual-write, gradual cutover, runbook).

PASS hooks для Enterprise migration:
— «Структурированная миграция с parallel-running и нашей командой» (без числа дней).
— «Дедикейтед migration engineer + runbook + parallel-running phase» (process, не deadline).
— «Migration phase зависит от scale инфраструктуры — обсуждается на discovery call» (qualified).

FAIL hook для Enterprise: `"Мигрируйте с {X} за 24 часа без потери данных"` → CTO читает как «not enterprise-ready, doesn't understand our scale» → conversion-drop + skepticism.

**ПРАВИЛО 7 — "Free migration" / "наша команда мигрирует" — financial promise → V18:**

«Бесплатная миграция нашей командой» = financial commitment (engineer-hours оцениваются в десятки тыс. USD для Enterprise scope). Не factual feature, а pricing-claim.

PASS условия:
1. У клиента есть программа «included migration» с конкретным scope-limit (например «up to 50k hosts included, beyond — quote»).
2. Substantiation = ссылка на pricing-page / Statement of Work template.
3. Без substantiation → переписать в «migration assistance» / «dedicated migration engineer» (service-feature, не free-money claim).

FAIL пример: `"Free migration + 24-hour cutover"` → 2 нарушения (free как financial promise + 24h timeline).

PASS пример: `"Migration assistance included in Enterprise plan, scope defined per SoW"`.

**ПРАВИЛО 8 — AI DISCLOSURE pack для public CEO Soul ID (right-of-publicity):**

Если в крео Soul ID = реальный public CEO / executive (на публичном LinkedIn / press / earnings calls) → AI DISCLOSURE pack ОБЯЗАТЕЛЕН независимо от гео (не только USA/EU):

Причина — public figures имеют усиленную right-of-publicity protection (US: Lanham Act + state right-of-publicity laws CA / NY / TX / TN; EU: GDPR art.6 + национальные защитные нормы; UK: Image Rights). AI-likeness public CEO без disclosure = риск litigation независимо от Meta-policy.

Overlay-формат: `«AI-assisted visual · {Alex Park}, CEO {Cortex}»` (bottom-third, present 0-end, не активирует V18, не считается hook-overlay).

GUARDRAIL: даже если ученик утверждает «у меня sign-off на use of likeness» — sign-off на marketing use ≠ sign-off на AI-generation use. Это **разные** rights. AI DISCLOSURE pack нужен дополнительно к sign-off, не вместо.

**B2B_SAAS_ENTERPRISE PRESET — финальный чек-лист (8 проверок перед выдачей промта):**

| # | Проверка | PASS если | FAIL → |
|---|---|---|---|
| 1 | Cinema Studio + Veo 3.1 + PORTRAIT CU pack | Да | Переключить workspace, ANTI-AI-LOOK pack добавить |
| 2 | EXECUTIVE-CALIBRATED H-stack (SKIP H1/H5/H6/H9, OK H3/H7/H8/H10) | Да | Убрать «wisp temple» / «wrinkled shirt» / «handheld» из промта |
| 3 | Premium polish prompt-фраза включена («natural micro-imperfections, light dust on glass, used notebook») | Да | Дописать |
| 4 | SLA-claim substantiated (contract / SOC 2 / ISO 27001) ИЛИ переписан в «designed for» / «target» | Да | Запросить у клиента / переписать |
| 5 | Competitor НЕ exact name в крео (только generic alias «legacy tool» / «existing vendor») | Да | Заменить named на generic |
| 6 | Disparagement отсутствует («X killer» / «X is broken» / «X can't scale») | Да | Убрать / переписать в neutral comparison |
| 7 | Migration timeline qualified (нет «24 hours», есть process-description) | Да | Переписать в «parallel-running» / «discovery call» |
| 8 | AI DISCLOSURE pack включён (если Soul ID = real public CEO) | Да | Добавить overlay «AI-assisted visual · {Name}, CEO {Co}» |

8/8 PASS → промт выпускается ученику.
≤7/8 PASS → return to editor, не выпускается. Конкретные FAIL-причины перечисляются в return-note.

═══════════════════════════════════════════════════

═══════════════════════════════════════════════════
B2B_SAAS_SMB_PRESET — отдельный пресет (волна Т.11 после Т.11-А создателя)
═══════════════════════════════════════════════════

Контекст: B2B_SAAS_SMB (PLG / founder-led startup SaaS — Notion-style / Cal.com / Plausible Analytics / Beehiiv / Tally / Vercel-style indie tools) имеет систематически иной риск-профиль и иную эстетику, чем B2B_SAAS_ENTERPRISE (см. волна Т.3). До волны Т.11 SMB-кампании сбивались на enterprise-rails: агент применял Cinema Studio + Veo 3.1 + EXECUTIVE-CALIBRATED H-stack к founder с чеком $19-49/seat, и founder читался «как выдрессированный консультант», а не «свой» для SMB owner / indie hacker. Параллельно терялись три критических SMB-only слоя: (1) FTC Click-to-Cancel 16 CFR §425 + state ARL matrix для free-trial-to-paid auto-renew (overlap с ECOM_IMPULSE_USA_PRESET Правило 4 — но в SaaS-контексте: seat subscription / freemium upgrade trigger), (2) PLG-specific substantiation source matrix (G2 / Capterra / TrustRadius / Product Hunt / GitHub stars / YC batch / Indie Hackers revenue / open-startup metrics — вместо SEC ADV / Bloomberg / SOC 2 Enterprise-привычных), (3) SMB-specific risks (LTD AppSumo non-refund disclosure / acquisition framing TechCrunch substantiation / «we're hiring» soft-trust signal pattern). Этот пресет — единая точка истины для PLG / founder-led SMB SaaS.

**КОГДА АКТИВИРУЕТСЯ B2B_SAAS_SMB_PRESET:**

Профиль клиента = B2B_SAAS, и любой из триггеров:
— Чек $19-299/seat/мес ИЛИ deal-size $500-50k/год (LITE-STANDARD-tier).
— Pricing model = self-serve / freemium / 14-day free trial БЕЗ sales-call (PLG signature).
— Целевая аудитория = SMB founder / startup CEO / индивидуальный предприниматель / freelancer / small-team lead (10-200 employees).
— Distribution = Twitter / X / LinkedIn (founder-led) / Product Hunt launch / Indie Hackers / Y Combinator forum / Hacker News.
— Founder в кадре (личность founder = brand — не agency-cast actor, не corporate CMO).
— Сравнение через G2 / Capterra / TrustRadius / Product Hunt badge / GitHub stars / YC batch.
— Pricing claim «$19/month» / «$49/seat» / «Free forever» / «14-day free trial» в крео.
— Профиль клиента содержит флаг `tier=smb` или sub-profile `B2B_SAAS_SMB`.

Если хотя бы один триггер — все 8 правил ниже **обязательны**. При конфликте с B2B_SAAS_ENTERPRISE_PRESET — применяется этот preset (mutual exclusion по чеку $300/seat и аудитории CTO Fortune 500).

**ПРАВИЛО 1 — Workspace + модель + packs (Marketing Studio + Kling 3.0 + HANDHELD + DESK ENVIRONMENT):**

— Workspace = **Marketing Studio** (НЕ Cinema Studio как Enterprise) — founder talking-head на phone-camera ИЛИ OBS-style desk-recorder с веб-камерой laptop. НЕ professional set с glass partition.
— Модель = **Kling 3.0 default** (НЕ Veo 3.1 — у Veo executive-polish читается overdressed для $19/seat tier). Kling 3.0 даёт phone-camera authenticity на CU 35-50mm — это match для PLG-founder aesthetic.
— Packs = **PORTRAIT CU + ANTI-AI-LOOK + HANDHELD pack** (handheld phone-shake OK для SMB — vs locked tripod Enterprise; controlled micro-drift ≤2-3deg, не vlog-shake) + **DESK ENVIRONMENT pack** (home-office desk с реальными items — coffee mug с patina, notebook с edges worn, plant in pot, mechanical keyboard, second monitor с реальным UI, NOT pristine glass-partition / NOT «cleanest desk in the world» AI-stock).
— UI mockup product / dashboard в кадре = через §19A UI MOCKUP PIPELINE (как в Enterprise), но product UI = real SaaS interface (Notion-style sidebar / Cal.com booking flow / Plausible chart), не corporate-CRM mock.
— Format = **9:16 + 7-9s** (Meta Reels / X Native Video primary) + **1:1 + 6s** (Twitter/X feed secondary) — НЕ 16:9 + 12s LinkedIn primary как Enterprise. LinkedIn 16:9 — опционально, если founder активно ведёт LinkedIn-распространение.

GUARDRAIL: если ученик просит Cinema Studio + Veo для SMB-проекта ($19-299/seat) — переспроси: «уверен? для PLG founder cinema-polish снижает trust, читается как agency-actor. Альтернатива — Marketing Studio + Kling 3.0 + DESK ENVIRONMENT pack. Подтверди если всё равно cinema.»

**ПРАВИЛО 2 — HUMANIZATION FULL (vs EXECUTIVE-CALIBRATED Enterprise) — все H1-H10 ENABLED:**

Запускается автоматически — built-in-public aesthetic для PLG founder. Из §21 H-стэка все 10 маркеров включены (в отличие от Enterprise SKIP H1/H5/H6/H9):

— **H1 wisp temple OK** — founder casual, не corporate-crisp.
— **H2 natural cadence с «эм / ну / так» / pause-fillers** — conversational, recorded-with-laptop-mic vibe, не teleprompter-read.
— **H3 lived-in desk 3-5 markers** (coffee stain on desk, used notebook с edges worn, plant in pot с реальной почвой, mechanical keyboard worn keycaps, post-it notes на monitor edge) — НЕ 1-2 marker как Enterprise. Более грубая «лайв» подача.
— **H4 not-actor Soul ID — real founder в кадре** (НЕ cast actor / stock-founder). Founder = brand для PLG, агент cast actor разрушает built-in-public trust. См. Правило 7.
— **H5 handheld micro-drift OK** — phone-camera authenticity (≤2-3deg drift, не vlog-shake). Локед tripod = enterprise-vibe, для SMB читается «overproduced».
— **H6 wrinkled wardrobe OK** — founder в hoodie / unironed t-shirt / startup-merch / plain cotton tee — built-in-public aesthetic. ЗАПРЕТ: suit + tie / blazer + dress shirt (читается как «agency hired this guy»).
— **H7 ambient audio room tone + keyboard click + occasional dog bark / kids-distant / coffee-machine hiss** — НЕ «studio quiet». Реальный home-office sound design.
— **H8 eye contact 70/30 с looks-away-to-think beats** — founder задумывается, не teleprompter-stare.
— **H9 lived-life face — puffiness OK** (late-night founder построил продукт ночью, реалистично). Зеркало enterprise SKIP правила.
— **H10 props look used** — laptop с stickers (Vercel / YC / GitHub Octocat), notebook с worn cover, pen-marks на desk.

Без HUMANIZATION FULL H-стэк EXECUTIVE-уровня (crisp suit / pristine desk / locked tripod) разрушает trust SMB-аудитории — indie hacker читается founder как «consultant нанятый агентством», вместо «такой же founder как я».

**ПРАВИЛО 3 — Pricing claims direct OK + Click-to-Cancel + state ARL для subscription / free trial / freemium (cross-ref ECOM_IMPULSE_USA_PRESET Правило 4):**

Direct pricing в крео для SMB SaaS — норма (vs Enterprise «fees per mandate letter / contract»):
— **«$19/month» / «$49/seat/mo» / «$199/year (save 17%)»** OK в overlay + EXACT STRING + Dialogue.
— **«Free forever» / «Free up to N users / N projects / N events»** OK при clear limits disclosure (что именно free vs paid — storage / seats / API calls / branding-watermark).
— **«14-day free trial» / «No credit card required»** OK как hook.

НО — auto-renew / subscription triggers federal + state laws (cross-ref ECOM_IMPULSE_USA_PRESET Правило 4 — те же 4 закона применяются к SaaS subscription, не только DTC physical product):
— **FTC Click-to-Cancel 16 CFR §425** (effective 2025) — cancellation должна быть в том же канале и количестве кликов как enrollment. Если sign-up online → cancel online в 1 клик, без «email support to cancel» flow.
— **FTC ROSCA 15 USC §8401-8405** — express informed consent для recurring billing.
— **FTC «Negative Option Marketing Rule»** (2024/2025) — pre-paid auto-renew terms disclosed clear-and-conspicuous.
— **State ARL matrix** — CA Civil Code §17602 / NY GBL §527-a annual notice / OR §646A.295 / VT 9 VSA §2454a (multi-state default = соблюдай CA + NY как strict baseline).

Требования в SMB SaaS крео:
— **«14-day free trial»** хук — overlay или caption: «After 14 days, $X/mo continues. Cancel online anytime via [domain.com/billing] before day 14.» Без — FTC ROSCA + Click-to-Cancel + state ARL violation.
— **«Free forever»** хук — qualifier «free up to N {events / users / projects} — paid plans start at $X/mo» (clear limits, не bait-and-switch).
— **«Cancel anytime»** в EXACT STRING — текстовый qualifier «Cancel online in 1 click at {domain}/account» обязателен.
— **Annual subscription («$199/year save 17%»)** — annual notice ≥15 days до renewal требуется per NY GBL §527-a (если subscription ≥12 months).

FAIL pattern в крео: «Try free for 14 days — risk-free!» без auto-charge disclosure → FTC ROSCA + Click-to-Cancel + CA §17602 + NY GBL violation одновременно (4 закона = тот же риск как DTC subscription box per ECOM_IMPULSE_USA_PRESET).

PASS pattern: «Try free for 14 days. After trial, $19/mo continues unless cancelled. Cancel online in 1 click at notion-like.com/billing.»

**ПРАВИЛО 4 — Substantiation через PLG sources (НЕ Enterprise SEC ADV / Bloomberg):**

SMB substantiation matrix — публично верифицируемые sources, привычные PLG-аудитории:

| Claim | Substantiation source (PLG-attached) | Overlay format |
|---|---|---|
| «100k+ users» / «50k+ signups» | Product Hunt launch badge + landing page counter (timestamped screenshot) | «100k+ users per [product-hunt.com/posts/X] · {date}» |
| «$5M ARR» / «$2M MRR» | Open-startup metrics page (Stripe / Lemonsqueezy public revenue page если open startup) ИЛИ Indie Hackers revenue page ИЛИ TechCrunch / Crunchbase published round | «$5M ARR per indiehackers.com/product/X · {date}» |
| «#1 alternative to {legacy tool}» | **G2 Crowd Grid leader** (category + year) ИЛИ Capterra category leader ИЛИ TrustRadius Top Rated | «#1 in G2 [Category] Spring 2025 Grid · g2.com/grid/X» |
| «Top 5 product of the day / week / month» | Product Hunt ranking (timestamped) | «#3 Product of the Day · Product Hunt · {date}» |
| «Y Combinator backed» / «YC W24» | YC public directory ycombinator.com/companies/X | «YC W24 · ycombinator.com/companies/X» |
| «10k+ GitHub stars» (для dev tools) | github.com/{org}/{repo} (publicly verifiable counter) | «12k stars · github.com/X/Y · {date}» |
| «Used by teams at {Google / Stripe / Shopify / Vercel}» | Public customer logo wall с прямым подтверждением (case study / public testimonial / customer logo permission) | «Trusted by teams at Stripe, Vercel, Linear» |

ЗАПРЕТ self-attested founder LinkedIn claim («I built this to $5M ARR») без public substantiation — это V18 FAIL (не verifiable, риск counter-claim).

**ПРАВИЛО 5 — Comparative claims / named competitor (PLG-context vs Enterprise hard-block):**

В B2B_SAAS_SMB named competitor допустим в Dialogue с G2 substantiation (vs Enterprise hard-block — там Lanham Act risk выше из-за крупных чеков и retaliation by named competitor). НО в overlay / EXACT STRING — generic alias.

PASS условия (PLG-context):
1. **В Dialogue** — named competitor («simpler than Notion» / «cheaper than Calendly» / «open-source alternative to Mixpanel») OK ЕСЛИ:
   — substantiation = G2 / Capterra / TrustRadius public comparison (с overlay badge year + category);
   — НЕТ disparagement language («X is broken / X can't scale / X is dead» — ВСЕГДА FAIL, как в Enterprise);
   — comparative claim factual («cheaper» = с реальным pricing-чартом; «simpler» = с UX comparison feature matrix), не subjective.
2. **В overlay / EXACT STRING** — generic alias: «legacy {category} tool» / «existing scheduling tool» / «current analytics platform» — НЕ named competitor exact string (overlay видна без context, риск screenshot-out-of-context litigation).
3. **«Better than X by N%»** — требует named benchmark source (G2 review-score comparison / public speed test / open-source benchmark repo) + год + same-workload context.

FAIL пример: `EXACT STRING: "Notion killer · 10x simpler · #1 alternative"` → 3 нарушения (named competitor в overlay + disparagement «killer» + N-x без benchmark).

PASS пример: `Dialogue: "I built this because Notion got too heavy for solo founders — simpler, $9/mo, no setup"` + `EXACT STRING: "The lightweight workspace for solo founders"` + G2 badge overlay «#2 in G2 Lightweight Note-Taking Spring 2025».

**ПРАВИЛО 6 — Migration story / free trial transitions (без 24h timeline FAIL как Enterprise):**

PLG SMB migration — самообслуживание без contract SLA, поэтому в отличие от Enterprise (где «24h cutover» = FAIL) — для SMB **«import your data in 5 minutes»** PASS, потому что:
— Нет contractual SLA commitment (нет signed contract → нет breach exposure).
— Self-serve migration tool в продукте (CSV import / API import / Zapier connector — factual feature).
— Audience expectation = «try product now», не «4-12 week parallel-running».

PASS hooks для SMB migration:
— «Import your Notion workspace in 2 minutes» — factual если import-tool реально работает за 2 минуты на typical workspace.
— «Migrate from Calendly in 5 minutes — connect Google Calendar, import event types» — factual feature.
— «Free CSV import — bring your data from {legacy tool}» — feature description, не commitment.

GUARDRAIL: число минут должно быть **реально достижимо на typical workspace** (если для 80-percentile user migration занимает 30 минут — «5 minutes» = misleading per FTC §5). Substantiation = product analytics typical-migration-duration (NOT marketing aspiration).

FAIL pattern: «Migrate everything in 30 seconds» если в реальности занимает 10+ минут на average workspace → FTC §5 deception risk + churn (user приходит, ожидает 30s, выходит).

**ПРАВИЛО 7 — Founder Soul ID + AI DISCLOSURE (real founder в public domain):**

Если в крео Soul ID = реальный founder (Twitter handle / LinkedIn / Y Combinator profile / Indie Hackers profile — public-domain identity) → AI DISCLOSURE pack ОБЯЗАТЕЛЕН (cross-ref B2B_SAAS_ENTERPRISE_PRESET Правило 8 — pattern совпадает).

Причина — founder = public figure для PLG-аудитории (Twitter-followers, YC alumni, Indie Hackers community). AI-likeness real founder без disclosure = риск:
— Twitter / X community call-out (PLG-аудитория очень чувствительна к authenticity — обнаружат AI-clone founder за часы);
— Right-of-publicity (US: Lanham Act + state right-of-publicity laws CA / NY / TX; EU: GDPR Art.6 + UK Image Rights);
— EU AI Act Art.50 extraterritorial transparency obligation (если контент видим в EU).

Overlay-формат: «AI-assisted visual · {Alex Park}, founder of {Notion-like}» (bottom-third, present 0-end, не активирует V18, не считается hook-overlay).

GUARDRAIL #1: даже если founder подписал sign-off на marketing — sign-off на marketing use ≠ sign-off на AI-generation use (это разные rights). AI DISCLOSURE pack нужен дополнительно к sign-off.

GUARDRAIL #2: если founder = co-founder pair (two founders в кадре, типичный PLG pattern) — sign-off + AI DISCLOSURE требуется на каждого отдельно.

**ПРАВИЛО 8 — SMB-specific guardrails (LTD AppSumo + acquisition framing + «we're hiring» soft signal):**

PLG-specific риски, не покрытые Enterprise preset:

**(a) Lifetime Deal (LTD) на AppSumo / similar platforms:**
— «$49 lifetime deal — 90% off» — OK pattern PLG, НО overlay должен содержать:
  — **Limited-time qualifier**: «AppSumo deal valid through {date}» (substantiated — реальная дата окончания deal).
  — **Non-refundable terms disclosure**: если LTD non-refundable (типичный AppSumo terms) — «non-refundable after 60-day window» (AppSumo terms 60 days).
  — **Scope of «lifetime»**: «lifetime = lifetime of {product} or {company}» — clear definition (не deceptive — если compa shuts down, lifetime ends).
— FAIL: «$49 forever — no risk» без non-refund disclosure → FTC §5 deception + AppSumo platform policy violation.

**(b) Acquisition / exit framing:**
— «We got acquired by {Stripe / Shopify / Vercel}» — substantiation TechCrunch / Crunchbase / official acquirer press release (public verifiable).
— «$XM acquisition» — exact figure требует public-disclosure source (Crunchbase deal page / TechCrunch coverage / SEC 8-K если public-acquirer).
— Если deal undisclosed (typical для small acquisitions) — «acquired by {brand} (terms undisclosed)» qualifier.
— ЗАПРЕТ «about to be acquired» / «next-acquired» — speculative, FTC §5 risk + insider-trading risk если acquirer public-traded.

**(c) «We're hiring» как soft trust signal:**
— OK pattern PLG founder («we're hiring engineer #5 — apply at careers.X.com»). Сигналит «growing company, real product» — повышает trust SMB-аудитории.
— GUARDRAIL: если «we're hiring» используется как proxy для «we're growing» substantiation — реальная careers-page с реальными open positions требуется (FTC §5 misleading if no actual openings).

**(d) «Built in public» / «open startup» framing:**
— «Public revenue: $50k MRR» — substantiation через open-startup page (Plausible-style public dashboard).
— «Built in 4 weeks» / «$0 funding» / «bootstrapped to $1M ARR» — substantiation Twitter thread timestamps + Crunchbase «no funding raised» + revenue page.
— Эти patterns = high-trust PLG signal, но требуют public proof — иначе FTC §5 risk + community call-out.

**B2B_SAAS_SMB_PRESET — финальный чек-лист (8 проверок перед выдачей промта):**

| # | Проверка | PASS если | FAIL → |
|---|---|---|---|
| 1 | Marketing Studio + Kling 3.0 + PORTRAIT CU + ANTI-AI-LOOK + HANDHELD pack + DESK ENVIRONMENT pack (НЕ Cinema Studio + Veo) | Да | Переключить workspace на Marketing Studio, заменить модель на Kling 3.0, добавить HANDHELD + DESK ENVIRONMENT packs |
| 2 | HUMANIZATION FULL — все H1-H10 ENABLED (built-in-public aesthetic: wisp temple OK, lived-in desk 3-5 markers, wrinkled wardrobe OK, ambient room tone, late-night founder face) | Да | Снять EXECUTIVE-CALIBRATED SKIPs, добавить hoodie / coffee stain / used notebook / room tone к промту |
| 3 | Pricing claims direct OK ($19/mo / Free forever / 14-day trial), НО subscription / free trial / freemium = Click-to-Cancel + ROSCA + state ARL disclosure (cross-ref ECOM_IMPULSE_USA_PRESET Правило 4) | Да | Добавить auto-charge disclosure overlay, clear limits для freemium, cancel-mechanism qualifier |
| 4 | Substantiation через PLG sources (G2 / Capterra / TrustRadius / Product Hunt / GitHub stars / YC batch / Indie Hackers / Crunchbase / TechCrunch / open-startup metrics — НЕ Enterprise SEC ADV / Bloomberg) | Да | Заменить source на PLG-verifiable, добавить overlay badge + date |
| 5 | Comparative claims: named competitor OK в Dialogue с G2 substantiation, НО в overlay / EXACT STRING — generic alias. Disparagement («killer / broken / dead») ВСЕГДА FAIL | Да | Заменить named на generic в overlay, убрать disparagement, добавить G2 badge для Dialogue named claim |
| 6 | Migration timeline factual (минуты OK для self-serve, нет contractual SLA как Enterprise). Число минут реально достижимо на typical workspace (substantiation = product analytics) | Да | Заменить aspirational «30 seconds» на realistic typical-duration, добавить «for typical workspace» qualifier |
| 7 | AI DISCLOSURE pack включён (если Soul ID = real founder в public domain — Twitter / LinkedIn / YC / Indie Hackers). Sign-off на marketing ≠ sign-off на AI-generation | Да | Добавить overlay «AI-assisted visual · {Name}, founder of {Co}», запросить отдельный AI-generation release |
| 8 | SMB-specific guardrails (LTD AppSumo non-refund + acquisition framing TechCrunch / Crunchbase substantiation + «we're hiring» real openings + built-in-public open-startup substantiation) | Да | Добавить non-refund disclosure для LTD, substantiate acquisition с public source, проверить реальные careers-openings, substantiate public-revenue claim |

8/8 PASS → промт выпускается ученику.
≤7/8 PASS → return to editor, не выпускается. Конкретные FAIL-причины перечисляются в return-note.

**3-STEP FUNNEL для B2B_SAAS_SMB (PLG cold → free trial):**

| Этап | Цель | Арка крео | EXACT STRING / CTA | Risk-layer |
|---|---|---|---|---|
| **TOF** | Awareness через founder twitter-style talking-head | C (founder в desk-environment, education-mode — «вот проблема which I built this to solve», 1 insight per 7-9s) | «Why I built {product}» / «The {category} I wish existed» / «Stop {pain}, start {benefit}» | Низкий — нет pricing-claims, нет comparative-claims, нет substantiation requirement за пределами founder Soul ID + AI DISCLOSURE |
| **MOF** | Product demo + social proof (G2 / Product Hunt / customer logo) | C+G (founder + UI walkthrough через §19A UI MOCKUP PIPELINE, badge overlays G2 / Product Hunt / GitHub stars) | «See how {founder name} uses {product}» / «{N}k+ teams trust {product}» / «#1 in G2 {category} {year}» | Средний — substantiation overlay обязательна, named competitor в overlay = generic alias, G2/PH badge должна быть current (timestamp) |
| **BOF** | Free trial signup с Click-to-Cancel disclosure | C (founder с CTA) + overlay disclosure block | «Try free for 14 days — cancel online anytime at {domain}/billing. After trial, $19/mo unless cancelled.» / «Get started — no credit card required» | Высокий — все 8 правил применимы + Click-to-Cancel + state ARL (CA §17602 / NY GBL §527-a) + freemium limits disclosure + AI DISCLOSURE для founder |

GUARDRAIL: BOF cold open feed для subscription auto-renew model = автоматический pre-launch compliance review (FTC ROSCA + Negative Option + state ARL — top FTC priority 2024-2026, applicable к SaaS subscriptions equally к DTC physical product). Default — soft TOF/MOF в cold с free-trial-signup-no-CC-required pattern, BOF auto-renew commitment только в retargeting warm-audience с prior trial-experience + clear cancel mechanism disclosure.

═══════════════════════════════════════════════════

═══════════════════════════════════════════════════

HIGH_TICKET (премиум-коучинг, недвижимость премиум):
— Workspace: Cinema Studio 3.5
— Модель: Veo 3.1 + Soul Cast
— Packs: ECU FACE + ANTI-AI-LOOK + LIGHT CONSISTENCY + REFLECTION
— Hook: H5 (contrast reveal — до/после life)
— Format: 9:16 + 9s (Meta — дефолт). 16:9 + 15s (YouTube) — опционально, по запросу ученика.
— Особенность: cinematic look, premium интерьер, Soul Cast 2 героев, dialogue в Veo
— **§19B INFOGRAPHIC обязательно к рассмотрению** для process-крео (ANIMATED-DIAGRAM — «процесс работы 1→N этап» / «4 фазы трансформации»), indicative-valuation framework visual (INFOGRAPHIC-CHART). Для M&A / HIGH_TICKET_PRO_SERVICES (M&A / LEGAL / private banking — переименовано в П.9) — все цифры substantiated per V18, имена клиентов generic alias.

**Для полного workflow HIGH_TICKET_PRO_SERVICES (M&A advisory / corporate LEGAL / private banking / family-office advisory / wealth advisory) используй HIGH_TICKET_PRO_SERVICES_PRESET ниже (волна Т.6 — 9 правил + финальный чек-лист 9/9 PASS). В нём собрана регуляторика 6 юрисдикций (US ABA/SEC/FINRA + state bars NY/CA/TX/FL / UK SRA/BSB/FCA / EU NRA/BRAK/MiFID/AIFMD / CH FinSA/FINMA), NDA/confidentiality жёстче B2B SaaS, substantiation third-party verifiable, AI DISCLOSURE для name-partner Soul ID.**

CRISIS_EXPERT (юр-кризис, банкротство, психотерапия острая):
— Workspace: Marketing Studio
— Модель: Kling 3.0 / Veo 3.1
— Packs: PORTRAIT CU + ANTI-AI-LOOK
— Hook: H4 (прямой взгляд юриста + цифра)
— Format: 9:16 + 6-8s
— Особенность: лицо клиента НЕ светим (используй PoV / back-of-head). Лицо эксперта на ID. Без срочности «успей пока не поздно» — только процессуальный срок.
— **§19B INFOGRAPHIC обязательно к рассмотрению** для process-крео (ANIMATED-DIAGRAM — «3 шага юр-аудита» / «процесс банкротства 1→4 этап»), substantiated outcomes (INFOGRAPHIC-CHART — обязательно с substantiation per V18, иначе FAIL). Лицо клиента НЕ в инфографике — generic icon / silhouette / abstract figure.

═══════════════════════════════════════════════════
CRISIS-AUDIT-LAYER (single source of truth — волна Т.4 после Т.4-5 Мета закрытие D9/D10/D14/D17/D20)
═══════════════════════════════════════════════════

Контекст: до волны Т.4 правила CRISIS_EXPERT были рассыпаны по 4 разным секциям (§20 п.5 + RELIGIOUS_TRAVEL CRISIS-AUDIT-LAYER + V17 таблица крис.метафор + meta-policy-checker категория «Юр.услуги»). Файл `QUICK-REFERENCE-NICHE-RESTRICTIONS.md` упомянут как «раздел 1 (CRISIS_EXPERT)» в 4+ местах, но не находится в ai-ops-7142 репо (живёт в cowork-загрузка курса) — это рабочая dependency, но не self-contained source. Эта секция — inline single source of truth.

Когда применять CRISIS-AUDIT-LAYER: профиль CRISIS_EXPERT (банкротство, развод-кризис, уголовная защита, кризисная психология/addiction, реанимация частной практики, ритуальные услуги, острые психо-состояния). Применяется ПОВЕРХ базовых V1-V22 проверок. Также применяется как audit-layer для RELIGIOUS_TRAVEL × crisis-аудитории (вдовцы / разведённые / в утрате / банкротстве — см. ниже).

**8 ПРОВЕРОК CRISIS-AUDIT-LAYER:**

**C1 — Нет «успей пока окно» / fake urgency.**

PASS только если:
— substantiated regulatory deadline (статья закона + дата вступления изменений + ссылка на public source: Dz.U. для PL / КонсультантПлюс РФ / Adilet КЗ / Rada.gov.ua для UA / Bundesgesetzblatt DE);
— реальный процессуальный срок конкретного дела клиента (30-дневный срок обжалования по ст. X / срок подачи заявления о банкротстве);
— реальный slot календаря (конкретный день/час, не «осталось 3 места до конца месяца»).

FAIL: «акция до конца месяца», «осталось 3 места», «скоро закроем приём», «успей пока окно открыто», «до конца марта пока действует».

**C2 — Нет before/after психо-состояний.**

Запрет:
— «потухший → ожившая» в визуале одного героя;
— палитра cold-grey → warm-amber transition для одного героя;
— minor-key audio → major-key audio внутри одного крео;
— любые impl эмоциональные before/after через wardrobe / posture / lighting.

Применяется к visual И voice-over (если voice-over описывает emotional state клиента до/после).

**C3 — Нет давления страхом без regulatory-grounding.**

Запрет: «потеряешь всё», «лишишься семьи», «дети без отца», «коллекторы заберут квартиру», «приставы постучатся завтра», «спаси свою семью».

Разрешено только substantiated regulatory facts: «по ст. X КоАП срок до N лет ограничения», «по ст. 446 ГПК взыскание невозможно на единственное жильё» (factual reference, не fear-mongering framing).

**C4 — Лицо клиента НЕ в кадре, НЕ в voice-over (даже generic alias).**

Запрет: фото реального клиента в кадре (даже с consent), full name overlay «Maria S.», generic alias уровня «Анна 35 Краков долг 1.5M» (combined identifier = identifiable person в малом community).

Разрешено:
— Soul ID эксперта (адвокат/психолог/специалист) с AI DISCLOSURE pack обязательно (см. C8);
— PoV / back-of-head клиента (без идентифицирующих признаков);
— Generic illustration / silhouette / abstract figure в §19B инфографике (без facial features / ethnicity / gender markers).

**C5 — Аудиоистория клиента запрещена (даже без лица).**

Voice-over от лица клиента («Я Александр, прошёл процедуру банкротства, не показываю лицо но это мой реальный опыт») = тот же риск что лицо клиента. Voice-print = personal data per GDPR Art.4. PL UODO / DE BfDI прямо применяет это правило.

Testimonials клиентов CRISIS_EXPERT — только письменный текст на лендинге с opt-in от клиента под рекламную кампанию (отдельный consent от стандартного клиентского соглашения), НЕ в крео.

**C6 — Substantiated outcome vs искусственная виктимизация (V17 vs V19 resolution).**

Когда V17 (Hook против Жертвы) конфликтует с V19 (substantiated outcome), приоритет такой:

PASS: «47 завершённых дел по упрощённой процедуре банкротства 2023-2024 (public records sygnatury XX/XX-XX/XX)» — substantiated outcome + neutral framing.

FAIL: «избавил тебя от приставов» / «спишем все долги» — promise исхода (не substantiated outcome).

FAIL: «коллекторы душат — освобожу» — substantiated outcome но fake-victim framing (читается виктимно: «ты жертва коллекторов»).

PASS resolution: если outcome substantiated AND no fake-victim framing → PASS V19 имеет приоритет над V17 «звучит как жертва». Переписать на neutral: «процедура банкротства = legal механизм защиты, 47 завершённых дел по моей практике».

**C7 — Regulatory-timeframe vs маркетинг-обещание (extension V18 для CRISIS LEGAL).**

Procedure duration claims («4 мес / 6-12 мес процедура»):

PASS если:
— source = official statistics (PL: Ministerstwo Sprawiedliwości RP raport; РФ: Минюст РФ; DE: Bundesamt für Justiz Insolvenzstatistik; CZ: Insolvenční rejstřík);
— period stated («среднее 2023 по упрощённой процедуре»);
— hedge: «в зависимости от загруженности суда» / «по типовому случаю».

FAIL: «у меня процедура за 4 мес» (как маркетинг-обещание исхода).
FAIL: «гарантированно за N месяцев» — absolute promise + срок = двойной триггер.

**C8 — AI DISCLOSURE для public expert в regulatory registry (generalize правила 8 B2B_SAAS_ENTERPRISE_PRESET).**

Soul ID = реальный public professional в national regulatory registry (адвокат в NRA / врач в реестре Минздрава / психолог в реестре PTP / нотариус в нотариальной палате / архитектор в IARP) → AI DISCLOSURE pack ОБЯЗАТЕЛЕН независимо от гео.

Причина — public professional в regulatory registry имеет усиленную защиту personal data + image rights:
- PL: Kodeks Cywilny art. 23-24 ochrona dóbr osobistych + UODO + Prawo o adwokaturze art.4 защита dignity zawodu;
- DE: KUG §22 Recht am eigenen Bild + BORA §43b;
- CZ: NOZ §84-90;
- UK: Image Rights;
- USA: Lanham Act + state right-of-publicity (CA / NY / TX / TN).

AI-likeness public professional без disclosure = риск:
1. Дисциплинарного procedure адвокатской/медицинской палаты (за «нарушение dignity zawodu»);
2. Гражданского иска (нарушение image rights).

Overlay-формат: `«AI-assisted visual · {Sergiusz Kovalchuk}, adwokat»` (bottom-third, present 0-end, ≤47 chars).

GUARDRAIL: sign-off на marketing use ≠ sign-off на AI-generation use. AI DISCLOSURE pack нужен дополнительно к sign-off, не вместо.

**CRISIS-AUDIT-LAYER финальный чек-лист (8/8 PASS перед выпуском промта для CRISIS_EXPERT):**

| # | Проверка | PASS если | FAIL → |
|---|---|---|---|
| C1 | Нет fake urgency (только substantiated regulatory deadline / реальный slot) | Да | Переписать CTA на нейтральную запись |
| C2 | Нет before/after психо-состояний (visual + voice-over) | Да | Удалить контрастные scenes / palette transition / music key change |
| C3 | Нет давления страхом без regulatory facts | Да | Заменить на factual reference со статьёй закона |
| C4 | Лицо клиента НЕ в кадре (только Soul ID эксперта + AI DISCLOSURE + PoV / silhouette) | Да | Заменить фото клиента на generic abstract figure |
| C5 | Voice-only client testimonial отсутствует | Да | Удалить voice-over от лица клиента |
| C6 | Outcome substantiated AND no fake-victim framing | Да | Переписать на neutral («legal механизм защиты») |
| C7 | Procedure duration claim substantiated official statistics | Да | Заменить на «в зависимости от случая» |
| C8 | AI DISCLOSURE pack для Soul ID public professional | Да | Добавить overlay «AI-assisted visual · {Name}, {profession}» |

8/8 PASS → выпускается ученику.
≤7/8 PASS → возврат на переписку с конкретными FAIL-причинами в return-note.

**3-STEP FUNNEL GRANULARITY для CRISIS_EXPERT (волна Т.4 закрытие D1/D2/D3):**

Если профиль клиента предполагает 3+ шага funnel (TOF awareness → MOF nurture → BOF close — типичный case для CRISIS_EXPERT с воронкой «заявка → 15-30-мин диагностика-аудит / первичная оценка → платная сессия / сопровождение»), пачка крео должна содержать минимум по 1 крео на step.

Таблица сюжетных арок × funnel-step для CRISIS_EXPERT:

| Step | Цель | Арка (§20) | EXACT STRING focus | CTA |
|------|------|------|------|------|
| TOF | Awareness — проблема существует, есть метод | F (3 шага процедуры) через §19B ANIMATED-DIAGRAM | «3 шага банкротства физлица в Польше» + substantiated process | «Узнайте подходит ли процедура» (soft) |
| MOF | Nurture — выбор эксперта (уже знает что метод есть) | C (эксперт показывает метод) через Soul ID tripod talking-head | «Adw. {N}, {registry number} · 47 завершённых дел» | «Запишитесь на 15-30-мин разбор бесплатно» |
| BOF | Close — конкретный action на платную | C (эксперт + кейс substantiated) через Soul ID tripod | «Платная сессия $1500 — детальный анализ + план процедуры» | «Запишитесь на платную сессию / Получите предложение» |

Правило пачки для CRISIS_EXPERT (расширение §«ЕСЛИ ПАЧКА»):
- LITE (3 крео): TOF + MOF + BOF — по одному каждого. **НЕ 3 TOF.**
- STANDARD (5 крео): 2 TOF (2 angle: hook процессуальный срок + hook substantiated outcome) + 2 MOF (process + authority) + 1 BOF.
- PRO (7 крео): 3 TOF + 3 MOF + 1 BOF.

GUARDRAIL: НЕ смешивай в одном крео hook TOF («у тебя 30 дней до пропуска срока — общий awareness») + CTA BOF («запишись на платную сессию $1500») — это разрыв воронки, аудитория не готова к BOF cold.

DIASPORA-TONE TUNING для CRISIS × EU_RUSSIAN_DIASPORA × LEGAL (закрытие D8/D18):
- TOF: спокойный авторитетный (на «вы») — холодная аудитория не готова к peer.
- MOF: empathic peer (на «ты») — уже знакомы с экспертом, разбор бесплатный, можно ближе.
- BOF: confident neutral («запишись на платную — это твоё решение») — без давления, но конкретно.
- Возвратные hooks («вернуться в РФ / вернуться в страну происхождения») — для PL диаспоры политически окрашенные. Требуется отдельная pre-проверка с ученика что hook нейтрален. Default — избегать «возвратной» лексики, заменять на «решить дело здесь, не выезжая».

**LEGAL substantiation extension для V19-BIOCLAIM (волна Т.4 закрытие D13):**

Для CRISIS_EXPERT × LEGAL standard V19-BIOCLAIM артефакты (CRM-выгрузка / Notion / письмо клиента ≤7 дней) — недостаточны. Требуется:

- Public court records (anonymized sygnatura list): «47 zakończonych spraw upadłości konsumenckiej 2023-2024 — sygnatury akt internal registry, доступны verification по запросу регулятора»;
- Verified membership в национальной адвокатской палате (NRA / BRAK / KRRP / ČAK / коллегия адвокатов РФ);
- Years of practice — подтверждённые karta pobytu / лицензия с датой выдачи (substantiates «3 года в Кракове» = 3+ years residency permit, не маркетинговое «годы практики»).

Voice-only client testimonials как substantiation — запрещены (per C5).

Aggregated financial outcome claims («помог списать 1.5M zł долгов на 47 клиентов»):
- Требует methodology disclosure: по какой статье считается «списано» (PL: art.491-491^21 Pr.Up.; DE: §286 InsO Restschuldbefreiung), period (Q1 2025 / 2023-2024), scope (упрощённая процедура / типовые случаи);
- Disclaimer: «Suma list dotyczy konkretnych spraw zakończonych w {period}; wynik zależy od okoliczności indywidualnej sprawy».

═══════════════════════════════════════════════════

REAL_ESTATE_EXPAT (Golden Visa, D7, Beckham):
— Workspace: Cinema Studio + Higgsfield Audio
— Модель: Veo 3.1 / Seedance 2.0
— Packs: BACKGROUND SEPARATION + REFLECTION + LIGHT CONSISTENCY + ANTI-AI-LOOK
— Hook: H1 (pattern — кадр виллы / квартиры в первые 2s) или H7 (anomaly — палм за окном офиса)
— Format: 9:16 + 9s (Reels Meta+IG — дефолт). 16:9 + 12-15s (YouTube / LinkedIn) — опционально, по запросу ученика.
— Особенность: cinematic exterior + interior, voice-over на английском через Higgsfield Audio, без targeting age/gender в самом крео (Meta Housing Special Category)

DIASPORA-TONE GUIDANCE (REAL_ESTATE_EXPAT и diaspora-сегменты в любом профиле — diaspora-INFOBIZ / diaspora-HIGH_TICKET / diaspora-LOCAL_SERVICE):

— Hook ОБЯЗАТЕЛЬНО начинается с РЕЗУЛЬТАТА / ОБЕЩАНИЯ / АМБИЦИИ. НЕ с грусти / ностальгии / возрастного маркера. Diaspora-аудитория уже носит ностальгию в фоне — не надо её активировать в hook.
— Палитра: тёплая warm-amber-gold / terracotta / oxblood. НЕ cold-desaturated-grey / faded-blue / minor-key visual.
— Звук (если Higgsfield Audio): major key, НЕ minor. Тёплый vocal-led ambient, НЕ cinematic-trailer mood.
— Visual posture героя: confident pose, eye contact, head up, active gesture. НЕ ссутуленный, НЕ опущенный взгляд, НЕ статика без жеста.
— Запрет фраз: «вернуться» БЕЗ явной амбиционной части («вернуться обогащённой / сильной / готовой к диалогу со своими»). Чистое «вернуться» = ностальгия-сожаление.
— Запрет фраз с возрастным маркером БЕЗ амбиции (см. V17). «47, не была 22 года» — FAIL. «47, еду забрать что моё, со своей группой» — PASS.
— Time-anchor в офере / overlay ОБЯЗАТЕЛЕН для HIGH_TICKET-diaspora: дата заезда / срок брони / количество мест («следующий заезд 12 октября, 3 места из 6»). Без time-anchor оффер «висит» — характерно для INFOBIZ, не для HIGH_TICKET tours / experience.

Diaspora-tone не отменяет проверку V17. Hook должен пройти и V17 (нет Жертвы), и diaspora-tone (амбиция + warm palette + confident pose).

**INDICATIVE VALUATION для real estate sell-side (волна П.8 — переиспользование M&A паттерна).** Для REAL_ESTATE_EXPAT residential sell-side комиссия 3-5% от чека 200-500k = 6-25k USD/сделка. Аналогично M&A indicative valuation (см. KONVEYER §703-707) — добавь паттерн «бесплатная индикативная оценка виллы за 3-5 дней» как Bonuses-трипваер в Hormozi-офферы:
— Содержание: AVM (automated valuation model) + comparables sales last 12 months + neighborhood trend report + maintenance/staging recommendations.
— **Free** (не fixed-fee 3-5k как M&A) — потому что в residential broker уже зарабатывает на комиссии при close, не на отдельной оценке.
— Lead-magnit: PDF-отчёт на 5-8 страниц с branded cover. Email-collection → CRM → 30-60-90 day nurture sequence.
— Solution-aware bucket (клиент знает что хочет продать, выбирает broker по доверию).

**META HOUSING SPECIAL CATEGORY — US HISPANIC addendum (волна П.8).** Если кампания на US-резидентов:
— Запрет targeting age / gender / ZIP code (Fair Housing Act + Meta Housing Policy).
— **Запрет targeting language preference** (Spanish-speaking only / Hispanic affinity audience) — это national origin proxy, FHA violation.
— Запрет «for Mexican-American families» / «cubans only» в копи — national origin discrimination.
— Допустимо: targeting broad US с copy на Spanish + ENGLISH; targeting по interests (Real Estate / International Travel / Property Investment) без attribute-restriction.
— GUARDRAIL для US-кампаний REAL_ESTATE: явная проверка через `meta-policy-checker` категория «Housing/Employment Special Ad Categories» до запуска.

**Для полного workflow REAL_ESTATE_EXPAT US-flight'ов (residential / investment property / EB-5 / foreign-buyer) используй REAL_ESTATE_EXPAT_USA_PRESET ниже (волна Т.7 — 8 правил + финальный чек-лист 8/8 PASS). В нём FHA §3604(c) casting compliance, Meta Housing Special Ad Category targeting, AI-staging disclosure FTC §5, substantiation broker claims через MLS/RealTrends/NAR, foreign-buyer guardrails (FinCEN GTO + FIRPTA + EB-5 SEC Reg D + RESPA §8 anti-kickback), state license # по штатам, AI DISCLOSURE для broker Soul ID.**

═══════════════════════════════════════════════════
REAL_ESTATE_EXPAT_USA_PRESET — отдельный пресет (волна Т.7 после Т.7-А создателя + Т.7-C адверсариала 6 кейсов / 20 GAP + Т.7-D мета cross-ref)
═══════════════════════════════════════════════════

Контекст: REAL_ESTATE_EXPAT_USA (residential / investment property для international buyers — Russian / Brazilian / Israeli / Chinese / EU diaspora покупающие в США + домашняя audience) имеет систематически иной риск-профиль, чем REAL_ESTATE_EXPAT EU-резидентский (Golden Visa / D7 / Beckham). До волны Т.7 секция REAL_ESTATE_EXPAT покрывала только базовый Meta Housing Special Category US HISPANIC addendum (строки 3201-3206), и для US-кампаний агент терял пять критических слоёв: (1) Fair Housing Act §3604(c) discriminatory-advertising запрет с HUD enforcement + private-lawsuit risk, (2) AI-generated property images / virtual staging FTC §5 misleading-impression risk + state real-estate commission ad rules, (3) substantiation broker claims через MLS / RealTrends / RISMedia (НЕ self-attested «top broker»), (4) foreign-buyer specific guardrails (FinCEN Geographic Targeting Orders для cash >$300k в Miami/NYC/LA/SF/Honolulu/San Antonio/Las Vegas + FIRPTA 15% withholding disclosure + EB-5 visa-investment SEC + USCIS regulations), (5) RESPA §8 anti-kickback при «free consultation» tied to specific lender / title company + TRID disclosures для financing references. Этот пресет — единая точка истины.

**КОГДА АКТИВИРУЕТСЯ REAL_ESTATE_EXPAT_USA_PRESET:**

Профиль клиента = REAL_ESTATE_EXPAT с US-гео триггером, и любой из триггеров:
— Listing property на территории США (single-family / condo / townhouse / multi-family / investment property).
— Целевая аудитория = foreign buyers (international purchasers — RU/BR/IL/CN/EU diaspora) + домашняя US audience (resident citizens / green-card holders / H-1B / L-1 / E-2 visa holders).
— Hook / Dialogue / EXACT STRING содержит ZIP-code mention, neighborhood-by-name (Miami Brickell / NYC Tribeca / LA Beverly Hills), price-point claim («from $850k»), rental-yield claim («6-8% annual yield»), investment-return claim.
— Soul ID = licensed real-estate broker / Realtor® (NAR member) / managing broker firm — state-licensed (FL / CA / NY / TX / WA / NV / IL / GA / AZ).
— Регуляторный гео-триггер: US Federal (FHA / HUD / FTC / FinCEN / SEC / IRS FIRPTA) + State real-estate commission (FREC / CalDRE / NYSDOS / TREC / WA DOL / NV REC) + Meta Housing Special Ad Category.
— Профиль клиента содержит флаг `vertical=us_residential|us_investment_property|us_commercial_re|eb5_marketing|firpta_seller`.
— Multi-investor / syndicated / crowdfunded deal detected (SEC Reg D 506(b/c) trigger) — rule-set расширяется автоматически.

Если хотя бы один триггер — все 8 правил ниже **обязательны**. Не «опционально к рассмотрению». EU REAL_ESTATE_EXPAT preset (строки 3175-3199) НЕ покрывает US-специфику — для US flight'ов запускать ИМЕННО этот preset.

**ПРАВИЛО 1 — Workspace + модель + packs (дефолт жёсткий, не предложение):**
— Workspace = Cinema Studio + Higgsfield Audio (НЕ Marketing Studio — exterior property + golden-hour interior + architectural cinematic motion ломаются в MS; Marketing Studio допустим ТОЛЬКО для broker talking-head pre-recorded segment).
— Модель = Veo 3.1 (НЕ Kling — у Kling architectural геометрия деформируется на slow camera-pull / parallax; wood-grain / stone-veining / glass-reflection рендерятся «plastic-like»). Seedance 2.0 допустим как fallback для establishing shots без архитектурного near-field detail.
— Packs = REFLECTION (window glass + pool surface + marble countertops + brass fixtures) + LIGHT CONSISTENCY (golden hour один key-light + practical fill, НЕ «award-winning real-estate cinematography») + ANTI-AI-LOOK + BACKGROUND SEPARATION (depth of field f/2.8-f/4 на property feature) + ARCHITECTURE / TEXTURE pack (wood-grain натуральный, stone-veining случайный, glass с micro-imperfection — без «AI-perfect» surface).
— UI / floor-plan / fee-schedule / map в кадре = ВСЕГДА через §19B INFOGRAPHIC-CHART / §19A UI MOCKUP PIPELINE, не напрямую в Veo (карты-схемы в Veo рендерятся с искажениями streets).
— Format = 9:16 + 9s (Meta + IG Reels — дефолт где сидит retail-buyer) / 16:9 + 12-15s (YouTube / LinkedIn — institutional / investor audience) / 1:1 + 7s (карусель листинг). Cross-ref §15 — формат-mix per placement-set обязателен для disclaimer rotation (см. ПРАВИЛО 7).

**ПРАВИЛО 2 — FHA-COMPLIANT CASTING (diverse / faceless / property-focus, НЕ только determined demographics):**

Fair Housing Act §3604(c) запрещает «discriminatory advertising indicating any preference, limitation, or discrimination based on race, color, religion, sex, handicap, familial status, or national origin». HUD enforcement + private lawsuit risk применяется ДАЖЕ к AI-generated images, если кадр signals preference. Industry settlements 2020-2024 (NAR / Zillow / Redfin / Facebook 2019 HUD complaint) задали precedent: показ ОДНОЙ ethnicity / family-type / age-group в семейном кадре листинга = FHA preference signal.

Триггеры FHA preference-signal:
— Семейный кадр с детьми только определённой ethnicity (white-only / Black-only / Hispanic-only / Asian-only family) при отсутствии diversity в других кадрах flight'а.
— Кадр только с молодыми покупателями (25-35) при listing семейного home → familial-status preference («for young couples») = FHA violation.
— Кадр только с пожилой парой (65+) при listing condo → age preference («for retirees») = ADEA + FHA familial-status.
— Религиозная символика в кадре (crucifix / mezuzah / Buddha statue на видном месте) при том что property нейтральная = religious preference signal.
— Wheelchair-accessibility отсутствует в кадре когда property advertised как «accessible» = handicap discrimination через omission.

PASS варианты для casting:
1. **Diverse cast** — 2-3 разных ethnicity / age / family-composition rotation через flight (4-6 крео в кампании, каждое со своим cast).
2. **Faceless / back-of-head** — фокус на property feature, лица не show (камера за плечом, ECU на key turning in lock, hand-on-railing).
3. **Property-only** — НЕТ human в кадре вообще (cinematic exterior + interior pan, golden-hour establishing shots, drone aerial).
4. **Generic AI faces** — НЕ recognizable real person; soft-focus background.

Cross-ref §11 (Soul ID guardrails) — broker Soul ID в кадре ЭТО OK (это professional, не FHA-protected class signal), но семейный кадр с одной ethnicity при отсутствии diversity в campaign = FAIL.

**ПРАВИЛО 3 — META HOUSING SPECIAL AD CATEGORY targeting compliance:**

Meta classifier auto-detects housing ads и принудительно применяет Special Ad Category restrictions. Если кампания идёт на US-резидентов И о housing → restrictions кумулятивные с FHA §3604.

Запреты (Meta enforcement + FHA):
— **Age / gender / ZIP code targeting** — hard-block. Допустимо: country = US, age 18-65+, all genders.
— **Radius targeting < 15 miles** (Meta минимум для housing = 15 miles, не default 1 mile) — hard-block при < 15.
— **Language-only targeting** (Spanish-only / Russian-only / Mandarin-only / Hebrew-only / Portuguese-only) = national-origin proxy under FHA §3604(c). Hard-block. Допустимо: bilingual (target-language + English) в copy + broad geo.
— **Copy с national-origin reference** — «for Russian families» / «cubans only» / «Chinese investors welcome» / «русскоязычная диаспора» / «服务华人社区» = hard-block.
— **Lookalike audiences based на demo / religion / family-status proxy** — нельзя seed lookalike из «members of Russian Orthodox church» / «Brazilian expats group» / «Jewish community center» / «Mandarin-speakers in Bay Area». PASS: lookalike на behavior («engaged with Real Estate / Property Investment / International Travel interest») без demographic-affinity seed.
— **Detailed targeting expansion** для housing — Meta auto-restricts; нельзя override toggle.

PASS условия:
1. Broad US geo + age 18-65+ + all genders + interest-based targeting (Real Estate / Property Investment / International Travel / Luxury Lifestyle / Relocation) — БЕЗ demographic-affinity.
2. Copy на target-language + ENGLISH bilingual (не single-language-only).
3. Lookalike — только behavior-based (engaged with property pages / saved listings / requested showings).
4. Radius targeting ≥ 15 miles от listing location (если geo-narrow нужен).
5. Pre-flight через `meta-policy-checker` категория «Housing Special Ad Category» — ОБЯЗАТЕЛЬНА (NEVER #23 блокер). Без галочки промт не считается выданным.

FAIL пример: `Targeting: Miami residents (radius 5mi from Brickell) · age 30-45 · Russian-speaking · interest "Russian Orthodox" lookalike` → 4 нарушения (radius <15 + age + language-only + religious-affinity lookalike).

PASS пример: `Targeting: US country-wide + interest "Property Investment, Luxury Real Estate, International Relocation" + lookalike (1%) seeded from past listing-engagement events · all ages 18+ · all genders · copy ENG+RUS bilingual`.

**ПРАВИЛО 4 — AI-staging disclosure (virtually staged overlay obligatory + FTC §5 misleading-impression):**

Industry adoption AI-virtual-staging (Roomvo / Virtual Staging AI / IKEA Place / generative interior fillers) выросла 2023-2026 в 10x. Без disclosure это создаёт misleading impression «actual property condition» — FTC Act §5 (deception) + state real-estate commission ad rules (FREC 61J2 / CalDRE Reg 2773 / NYSDOS 175.25 / TREC §535.155) + NAR Code of Ethics Standard of Practice 12-1.

Триггеры обязательного disclosure:
— Interior generated полностью AI (пустая комната + AI furniture overlay) → overlay «Virtually staged · actual property unfurnished».
— Exterior с AI-добавленной landscaping / pool / outdoor furniture которые НЕ существуют → overlay «Conceptual rendering · actual exterior may vary».
— Twilight / golden-hour version single-time-of-day photo upgraded AI → overlay «Time-of-day enhanced for marketing purposes».
— Drone aerial с AI-removed neighbors / construction sites / power lines → overlay «Aerial composite — actual surroundings may include {neighbor properties / utility infrastructure}» (FTC material-omission risk высокий).
— AI-generated «what could be» renovation visualization → overlay «Conceptual renovation — not current condition · subject to permits and HOA approval».

PASS overlay-формат: bottom-third, present 0-end, Inter Regular 14-16pt, white-90% на gradient-darken, ≤90 chars/line, две строки максимум. ТЕКСТ ОБЯЗАТЕЛЕН в самом кадре (не в caption / description Meta поста — FTC требует «clear and conspicuous» в creative, не вспомогательном поле).

FAIL пример: AI-generated luxury kitchen в empty condo без overlay → «materially misleading impression» under FTC §5 + state RE commission ad rule violation.

PASS пример: Тот же AI-generated kitchen + overlay «Virtually staged · actual unit is unfurnished · staging not included in sale» (present 0-end, bottom-third).

**ПРАВИЛО 5 — Substantiation для broker claims + License # state-specific в overlay:**

Любая числовая / qualitative claim в Dialogue / EXACT STRING / overlay = подпадает под V18 substantiation + state real-estate commission ad rules + NAR Code of Ethics Article 12 («true picture»).

Self-attested «top broker» / «#1 in Miami» / «sold $200M last year» = НЕ substantiation. Нужны third-party verifiable источники:
— **Sales volume («$200M closed last year»):** MLS production report + brokerage-firm validation OR RealTrends «The Thousand» / «America's Best» published ranking (annual, methodology disclosed) с годом + категорией.
— **Transaction count («147 sides closed»):** MLS-pulled report с datestamp + scope (buyer-side + seller-side disclosed? team-aggregated vs individual?).
— **Ranking («Top 1% nationally»):** RealTrends / RISMedia / Wall Street Journal RealTrends ranking + год + методология + категория (individual vs team vs brokerage).
— **Years experience («20 years in Miami luxury»):** license-issuance date через state real-estate commission public lookup (FREC / CalDRE / NYSDOS).
— **«Luxury specialist» / «International specialist»:** designation через NAR (CIPS — Certified International Property Specialist / CLHMS — Certified Luxury Home Marketing Specialist) — public NAR member directory; БЕЗ designation = ad violation.

License # обязательна в overlay (state real-estate commission ad rules):
— **FL (FREC 61J2-10.025):** «{Name}, Licensed Real Estate Broker · FL License #SL{NNNNNNN} · {Brokerage Name}, License #BK{NNNNNNN}».
— **CA (CalDRE Reg 2773):** «{Name}, DRE #{NNNNNNNN} · {Brokerage}, DRE #{NNNNNNNN}».
— **NY (NYSDOS 175.25):** «{Name}, Licensed Real Estate Salesperson/Broker · {Brokerage}, Licensed Real Estate Broker · Fair Housing Notice».
— **TX (TREC §535.155):** «{Name}, TREC License #{NNNNNN} · {Brokerage}, TREC #{NNNNNN}» + Consumer Protection Notice + Information About Brokerage Services form link.
— **NV (NV REC NAC 645.610):** «{Name}, NV RE License #B.{NNNNNN}.LLC · {Brokerage}».

«Realtor®» trademark — ONLY если broker действительно NAR member (verifiable через NAR membership directory). Misuse = trademark infringement + NAR enforcement.

FAIL пример: `EXACT STRING: "#1 Miami Luxury Broker · $300M closed · 20 years experience · Realtor®"` → 4 unsubstantiated claims (ranking + volume без MLS source + experience без license-date verification + Realtor® без NAR membership check).

PASS пример: `EXACT STRING: "Active in Miami luxury market · RealTrends 2025 The Thousand (FL sub-cat) · CIPS / CLHMS designations · FL Lic #SL3294857"`.

**ПРАВИЛО 6 — Pricing / rental-yield / investment-return claims + SEC Reg D + FIRPTA + TRID:**

Pricing и yield claims в US real-estate creо — высокий риск под FTC §5 + state RE ad rules + (для investment property) SEC Reg D 506(b/c) + (для financing references) TRID / Reg Z.

Запреты в крео:
— **«From $850k» pattern** — без typical price prominence = FTC «from-pricing» qualification rule + state RE «materially misleading» = violation. Замена: «typical 2-bed condo $1.2M, entry-level studio from $850k» с typical-price prominence equal.
— **«6-8% rental yield guaranteed»** — investment-return guarantee для residential rental → hard-block (FTC + SEC если syndicated). Замена: «historical rental yield in {neighborhood} 4-7% per Zillow/RentCafe 2024-2025 data, actual yields vary by unit / season / management cost — not guaranteed».
— **«Property values up 40% since 2020»** — past performance ≠ future results disclosure обязательна; источник (Case-Shiller / Zillow ZHVI / FHFA HPI) с датой обязателен.
— **«Tax-free if you hold 1031»** — IRC §1031 like-kind exchange имеет strict requirements (45-day identification / 180-day close / QI) — НЕ упрощать в крео. Замена: «1031 exchange may defer capital gains tax — eligibility per IRS rules, consult qualified intermediary».
— **«$0 down for foreign buyers»** — мортгидж claim → TRID / Reg Z disclosure pre-application + state mortgage broker ad rules. Если broker не licensed mortgage broker — referencing financing terms = unauthorized practice. Замена: «financing options available — terms per lender Loan Estimate disclosure».

SEC Reg D 506(b/c) trigger (NEW): Если deal syndicated / crowdfunded / multi-investor (любой структуре где investors pool capital, sponsor manages) — это **securities offering** под Securities Act 1933. Reg D 506(b) запрещает general solicitation → ЛЮБОЙ performance / fund-raising claim в open Meta/LinkedIn feed = loss of safe harbor → registration violation. Flag в intake: `client_offers_pooled_investment: y/n` → если yes, либо Reg D 506(c) с accredited-investor verification, либо удаление всех performance / yield / return claims из крео.

FIRPTA disclosure (для foreign sellers, NEW): Foreign Investment in Real Property Tax Act требует 15% withholding from gross sale proceeds when foreign person sells US real property (IRC §1445). Если креатив targeted foreign sellers («sell your US property») — добавь overlay «Sale by foreign person subject to FIRPTA 15% withholding — exemption certificate may apply per IRC §1445» либо избегай sale-side claims.

TRID (Truth in Lending) trigger: ANY mortgage / financing mention → Loan Estimate disclosure within 3 business days применяется ПОСЛЕ application. Pre-application creо НЕ может quote APR / payment / terms без Loan Estimate context. Замена: «financing options available — Loan Estimate provided within 3 business days of application per TRID».

PASS пример: `Dialogue: "Miami Brickell 2-bed condos — typical price $1.2M (entry-level from $850k for studios) · historical rental yield 4-7% per Zillow 2024-2025 data, actual yields vary · financing options per Loan Estimate disclosure"`.

FAIL пример: `Dialogue: "Miami condos from $850k · 6-8% guaranteed rental yield · $0 down for foreign buyers"` → 3 нарушения (from-pricing + guarantee + TRID financing claim).

**ПРАВИЛО 7 — Foreign-buyer specific guardrails (FinCEN GTO + EB-5 + RESPA §8):**

Foreign-buyer flight'ы имеют дополнительный слой regulatory triggers поверх FHA / Meta / FTC.

**(a) FinCEN Geographic Targeting Orders (GTOs):** Cash purchases >$300k by legal entity (LLC / corp / partnership) в GTO-covered counties (Miami-Dade / Broward / Palm Beach FL · Manhattan / Brooklyn / Queens / Bronx / Staten Island NY · Los Angeles / San Diego / San Francisco / San Mateo / Santa Clara CA · King County WA · Bexar TX · Honolulu HI · Clark NV · Cook IL · Suffolk MA · Fairfield CT · Maricopa AZ + extensions) → title insurance company обязана submit FinCEN Form 8300-equivalent within 30 days. Если creо advertised «cash-friendly · LLC-friendly · anonymous purchase» — это red flag для AML. Заменить на: «we work with international cash buyers per US AML compliance — title company handles FinCEN GTO reporting where applicable».

**(b) EB-5 visa investment marketing (USCIS + SEC):** Если property tied to EB-5 Regional Center program («invest $800k → US Green Card path») — двойное regulatory cover:
— USCIS Form I-526E filing requirements + targeted-employment-area (TEA) designation.
— SEC: EB-5 investment IS a security → Reg D 506(c) compliance + Regional Center registration + investor accreditation verification.
— Запрет в крео: «guaranteed Green Card» / «100% approval rate» / «$0 risk EB-5» → hard-block (USCIS approval НЕ guaranteed + SEC investment-return guarantee запрет).
— Замена: «EB-5 investment opportunity through {USCIS-designated Regional Center} · Green Card eligibility per USCIS approval · investment subject to risk · accredited investor verification required per Reg D 506(c)».

**(c) RESPA §8 anti-kickback (NEW):** «Free consultation» / «no-cost services» — если broker has referral arrangement с specific lender / title company / inspector / insurance provider И consultation tied к that referral → RESPA §8 violation (anti-kickback + unearned-fee prohibition). Treble damages + criminal penalty.
— Триггер: «Free pre-approval through our preferred lender» / «Complimentary title insurance quote from our partner» в крео.
— Замена: либо удалить partner-reference («free consultation — independent lender / title company of your choice»), либо disclose RESPA-compliant Affiliated Business Arrangement (AfBA) с overlay «Affiliated Business Arrangement disclosure — see [link]».

**(d) State broker licensing reciprocity:** Foreign-licensed broker / unlicensed referral partner cannot collect compensation на US property sale. Если creо featured «our Russian-speaking partner in Moscow» с implied compensation → state RE commission violation (unlicensed practice). Замена: «we work with international referral network — all US transactions handled by US-licensed brokers per {State} RE Commission rules».

**ПРАВИЛО 8 — AI DISCLOSURE pack для broker Soul ID:**

Если Soul ID = real licensed broker (firm website agent page / Zillow agent profile / Realtor.com profile / LinkedIn / NAR member directory) → AI DISCLOSURE pack ОБЯЗАТЕЛЕН независимо от гео и независимо от того есть ли direct regulatory mandate. Pattern совпадает с HIGH_TICKET_PRO_SERVICES senior partner — risk-of-misrepresentation такой же (fiduciary relationship + state-licensed professional).

Правовые слои:
— **US Federal:** Lanham Act §43(a) (false endorsement) + FTC §5 (deceptive practice) + NAR Code of Ethics Standard of Practice 12-5 (broker identification).
— **State right-of-publicity:** CA Civil Code §3344 / NY Civil Rights Law §50-51 / TX Property Code §26.001+ / FL Stat §540.08 / TN Personal Rights Protection Act — broker AI-likeness без disclosure = misappropriation + state RE commission misleading-advertising rule violation.
— **State real-estate commission ad rules:** FREC 61J2-10.025 / CalDRE Reg 2773 / NYSDOS 175.25 / TREC §535.155 — все требуют «true and accurate representation» of broker — AI-likeness без disclosure = misrepresentation.
— **NAR Code:** Article 12 + SOP 12-5 — broker identification «in a reasonable and readily apparent manner» — undisclosed AI generation нарушает «readily apparent».
— **EU AI Act art.50** (effective 2026): transparency obligation для AI-generated content depicting real person — extraterritorial если EU-diaspora targeted (US creо visible в EU).

Overlay-формат: `«AI-assisted visual · {Name}, {Title} · {State} Lic #{NNNNNNN} · {Brokerage}»` (bottom-third, present 0-end, ≤120 chars, Inter Regular 14pt, white-90% on gradient-darken). Объединяется с License # overlay из ПРАВИЛО 5 — единый disclaimer-block.

GUARDRAIL #1: даже если broker лично дал sign-off на marketing use of likeness — sign-off на marketing ≠ sign-off на AI-generation. Это **разные** rights. AI DISCLOSURE pack нужен дополнительно к sign-off, не вместо.

GUARDRAIL #2: для co-listing agents — если AI-rendered broker в кадре advertises listing where co-listing agent ALSO has compensation interest → co-listing disclosure required per state RE commission rules. Default — name BOTH brokers в overlay либо использовать faceless format.

GUARDRAIL #3: для team / brokerage account (multi-broker firm) — AI-rendered single broker без team context может mislead consumer о who-will-handle-transaction. Замена: «AI-assisted visual · {Name} & {Brokerage} team · Lic #{N}».

**REAL_ESTATE_EXPAT_USA_PRESET — финальный чек-лист (8 проверок перед выдачей промта):**

| # | Проверка | PASS если | FAIL → |
|---|---|---|---|
| 1 | Cinema Studio + Veo 3.1 + REFLECTION + LIGHT CONSISTENCY + ANTI-AI-LOOK + BACKGROUND SEPARATION + ARCHITECTURE/TEXTURE packs + Higgsfield Audio | Да | Переключить workspace, подключить недостающие packs |
| 2 | FHA-compliant casting (diverse / faceless / property-focus — НЕ только determined demographic) + НЕТ religious symbols / familial-status / age-group preference signals | Да | Заменить cast на diverse rotation либо переключить на faceless / property-only |
| 3 | Meta Housing Special Ad Category targeting: НЕТ age / gender / ZIP / radius <15mi / language-only / national-origin lookalike; copy bilingual; pre-flight через meta-policy-checker категория «Housing Special Ad Category» | Да | Расширить targeting на broad geo + behavior-based; убрать language-only seed; запустить meta-policy-checker |
| 4 | AI-staging disclosure overlay obligatory если interior / exterior / aerial AI-modified («Virtually staged · actual unit unfurnished» / «Conceptual rendering — actual exterior may vary»), bottom-third 0-end, в самом кадре не в caption | Да | Добавить overlay в кадр; если AI-generation не disclosed — переделать без AI-staging либо добавить disclaimer |
| 5 | Substantiation broker claims third-party verifiable (MLS production report / RealTrends ranking / RISMedia / NAR designation directory / state license public lookup) + License # overlay state-specific (FL FREC / CA DRE / NY NYSDOS / TX TREC / NV REC) + «Realtor®» только если NAR member | Да | Запросить source / переписать в qualified statement / добавить License # overlay |
| 6 | Pricing / yield / return: НЕТ «from $X» без typical-price prominence; НЕТ rental-yield guarantee; past performance disclosure если price-appreciation claim; SEC Reg D 506(b/c) flag если syndicated; FIRPTA disclosure если foreign-seller targeted; TRID для financing references | Да | Заменить on typical+minimum; убрать guarantee; добавить past-performance disclosure; flag SEC/FIRPTA/TRID на compliance |
| 7 | Foreign-buyer guardrails: FinCEN GTO acknowledged для cash >$300k в covered counties; EB-5 marketing без «guaranteed Green Card» + Reg D 506(c) accredited; RESPA §8 «free consultation» без tied-lender / AfBA disclosure; state licensing — only US-licensed broker collects compensation | Да | Удалить «cash-friendly anonymous» framing; добавить EB-5 disclaimers; разорвать tied-lender или добавить AfBA disclosure; rephrase referral arrangement |
| 8 | AI DISCLOSURE pack включён (overlay «AI-assisted visual · {Name}, {Title} · {State} Lic #{N} · {Brokerage}»), sign-off на marketing ≠ sign-off на AI-generation проверен отдельно; co-listing / team context disclosed | Да | Добавить overlay; запросить отдельный AI-generation sign-off; добавить team/co-listing context |

8/8 PASS → промт выпускается ученику.
≤7/8 PASS → return to editor, не выпускается. Конкретные FAIL-причины перечисляются в return-note.

**REAL_ESTATE_EXPAT_USA — 3-STEP FUNNEL GRANULARITY:**

Funnel-step разбивка обязательна (по аналогии с HIGH_TICKET_PRO_SERVICES 3-STEP FUNNEL):

| Step | Цель | Арка | CTA | Регуляторный риск |
|------|------|------|-----|---|
| TOF | Awareness — market intelligence / neighborhood guide / international-buyer education | Property-focus / faceless через §19B EDUCATIONAL-PROGRESSION (market data, neighborhood overview без identifiable people) | «Download Miami International Buyer Guide» / «Subscribe to monthly market report» / «Get FIRPTA cheat-sheet» | Низкий (educational, не listing-specific) |
| MOF | Nurture — listing portfolio + broker credibility + process | Broker Soul ID talking-head (с AI DISCLOSURE pack) + listing reel (с virtual-staging disclosure если AI) | «Browse current listings» / «Watch our buyer journey explainer» / «Get our process guide» | Средний (substantiation broker claims + FHA casting) |
| BOF | Close — specific listing showing / private tour / consultation | Listing cinematic + broker direct CTA | «Schedule private tour» / «Request listing package» / «Speak to broker» | Высокий (FinCEN GTO if cash-foreign; SEC Reg D if syndicated; RESPA §8 if consultation tied to lender) |

GUARDRAIL: Cold BOF CTA для investment property в open feed может trigger SEC Reg D 506(b) loss of safe harbor если deal syndicated. Default — soft TOF/MOF в cold-аудитории, BOF только в retargeting / warm после accredited-investor self-identification. Для FinCEN GTO geo (Miami / NYC / LA / SF / Honolulu) cash-purchase claims в open feed = AML compliance flag — escalate на title company / compliance до запуска.

CROSS-REFERENCES (не дублировать в этом пресете, использовать ссылками):
— DIASPORA-TONE GUIDANCE (строки 3183-3193) — применима поверх US preset для diaspora-аудитории (warm palette + confident pose + ambition-led hook + time-anchor).
— INDICATIVE VALUATION (строки 3195-3199) — pattern AVM + comparables actionable для US residential sell-side, но без «6-8x EBITDA»-style guarantee.
— META HOUSING SPECIAL CATEGORY US HISPANIC addendum (строки 3201-3206) — частный случай ПРАВИЛО 3 (Hispanic-affinity = national-origin proxy); этот preset расширяет на ВСЕ language groups.
— §11 Soul ID guardrails + §15 NEVER #23 meta-policy блокер + §19A UI MOCKUP + §19B INFOGRAPHIC-CHART + §21 EXECUTIVE-CALIBRATED HUMANIZATION (для broker Soul ID если senior).
— HIGH_TICKET_PRO_SERVICES_PRESET ПРАВИЛО 8 (AI DISCLOSURE) + ПРАВИЛО 9 (sanctions/OFAC / dual-credentialing / GDPR Art.9 language-lookalike) — sanctions screening применима для foreign-buyer flight'ов (RU/IR/KP/VE/BY exclusion).
— V17 (Жертва hook check) + V18 (substantiation) — universal guards, применимы поверх preset.

═══════════════════════════════════════════════════

WELLNESS_HEALTH_RESTRICTED (БАДы, hormonal coaching, US/Canada/EU):
— Workspace: Marketing Studio
— Модель: Kling 3.0 / Seedance 2.0
— Packs: PORTRAIT CU + ANTI-AI-LOOK + HANDS IN FRAME (если показ продукта)
— Hook: H4 с «may support» формулировкой, не «cure / heal»
— Format: 9:16 + 6s
— Особенность: НЕТ medical claims в визуале (не показывай «волшебное превращение»), герой в life-style ситуации (готовит завтрак, гуляет), сертификаты на стене кадра через Nano Banana 2

**Для полного workflow WELLNESS_HEALTH_RESTRICTED USA-flight'ов (supplements / hormonal coaching / weight-loss / sleep / ED / male enhancement) используй WELLNESS_HEALTH_RESTRICTED_USA_PRESET ниже (волна Т.7 — 9 правил + финальный чек-лист 9/9 PASS). В нём DSHEA §403r-6 structure/function vs disease claim hard-line, FDA mandatory disclaimer overlay, FTC «competent and reliable scientific evidence» substantiation, FTC §255 + §255.5 atypical results + material connection + AI-influencer disclosure, FTC «Gut Check» 7 false weight-loss claims hard-block, category-specific guardrails (ED PDE5 ban / sleep melatonin / hormonal TRT Schedule III), real clinician Soul ID + AMA §5.04 + AI DISCLOSURE, state law overlay (CA Prop 65 / NY AG botanical / TX DTPA), FTC Click-to-Cancel 16 CFR §425 для subscription DTC.**

═══════════════════════════════════════════════════
WELLNESS_HEALTH_RESTRICTED_USA_PRESET — отдельный пресет (волна Т.7 после Т.7-B создателя + Т.7-C адверсариала 6 кейсов / 20 GAP + Т.7-D мета cross-ref)
═══════════════════════════════════════════════════

Контекст: WELLNESS_HEALTH_RESTRICTED_USA (БАДы / dietary supplements / hormonal coaching / sleep / ED / weight-loss) имеет систематически иной риск-профиль, чем generic WELLNESS_HEALTH_RESTRICTED (см. 7-строчная секция выше). До волны Т.7 секция занимала 7 строк, и для US-кампаний агент терял пять критических слоёв: (1) FDA + DSHEA 1994 framework (structure/function vs disease claim hard-line + mandatory §403r-6 disclaimer), (2) FTC §255 (testimonials + material connection + substantiation = «competent and reliable scientific evidence»), (3) FTC «Gut Check» 7 false weight-loss claims (auto-violation pattern, multi-million consent decrees TINA.org enforcement), (4) state-law overlay (CA Prop 65 cancer/reproductive warnings + NY AG botanical supplements enforcement Schneiderman 2015 GNC/Walgreens/Walmart + TX DTPA), (5) hormonal/ED grey zones (TRT — Schedule III controlled substance требует MD prescription, ED supplements с PDE5 analogs — FDA seizure history). Этот пресет — единая точка истины для US-кампаний.

Cross-ссылки: V19-BIOCLAIM (3 категории claim «may support / proven / substantiated») в §V-серии, MEDICAL_HEAVY-сравнения в §16, Pre-валидатор A.3 BIOCLAIM (волна Т.2). Этот PRESET = single source of truth для US-Wellness/Supplements (заменяет ссылку на внешний `QUICK-REFERENCE-NICHE-RESTRICTIONS.md` — inline self-contained после волны П.20).

**КОГДА АКТИВИРУЕТСЯ WELLNESS_HEALTH_RESTRICTED_USA_PRESET:**

Профиль клиента = WELLNESS_HEALTH_RESTRICTED, и любой из триггеров:
— Геотаргетинг US (даже частично — US + CA mix трактуется по US-rules как stricter).
— Категория = dietary supplement / nutraceutical / botanical / vitamin / mineral / probiotic / amino acid / sports nutrition.
— Sub-vertical = hormonal coaching / testosterone optimization / DHEA / TRT-related (даже non-prescription positioning).
— Sub-vertical = weight-loss / fat-burner / appetite suppressant / metabolism booster.
— Sub-vertical = sleep aid / melatonin / herbal sleep / cortisol management.
— Sub-vertical = ED supplement / male enhancement / libido booster / «natural Viagra».
— Hook / Dialogue / EXACT STRING / overlay содержит claim на эффект («supports / promotes / boosts / restores»), цифровой outcome («-15 lbs in 30 days», «3x testosterone»), сравнение с drug («like Viagra without prescription», «better than Ambien»), testimonial с specific outcome.
— Soul ID = real MD / DO / RN / RD / DC / DPT / licensed nutritionist в endorsement-формате.
— Pricing model = subscription / auto-renew / «cancel anytime» (FTC Click-to-Cancel 16 CFR §425 trigger — NEW T.7-C GAP).
— Профиль клиента содержит флаг `vertical=supplement_dtc|hormonal_coaching|weight_loss|sleep_aid|ed_supplement|male_enhancement`.
— Платформа кампании = Meta / TikTok / Instagram / YouTube Shorts с US-targeting (FTC §255 influencer disclosure jurisdiction).

Если хотя бы один триггер — все 9 правил ниже **обязательны**. Не «опционально к рассмотрению».

**ПРАВИЛО 1 — Workspace + модель + packs (дефолт жёсткий, не предложение):**
— Workspace = Marketing Studio (talking-head wellness creator / customer-testimonial-стиль работает оптимально в MS; Cinema Studio overkill и читается «pharma TV ad», что увеличивает FDA scrutiny как drug-like marketing).
— Модель = Kling 3.0 (default для life-style talking-head) / Seedance 2.0 (если нужны smooth body-movement сцены: yoga / kitchen / morning routine — НЕ before/after weight-loss transformations, см. Правило 5).
— Packs = PORTRAIT CU + ANTI-AI-LOOK + HANDS IN FRAME (если показ продукта / pill / powder scoop / supplement bottle) + KITCHEN/HOME LIFESTYLE pack (готовит smoothie, наливает воду, утренний свет через окно — НЕ clinical setting, НЕ lab-coat, НЕ pharmacy).
— UI / supplement-facts panel / bottle label в кадре = ВСЕГДА через §19A UI MOCKUP PIPELINE или §19B INFOGRAPHIC-CHART, не напрямую в Kling (label-text иначе рендерится с галлюцинациями, FDA label compliance ломается).
— Format = 9:16 + 6-9s (Meta/TikTok primary, где сидит DTC supplement buyer) / 1:1 + 6s (Instagram feed retargeting).

**ПРАВИЛО 2 — Structure/Function vs Disease claim hard-line (DSHEA §403r-6):**

Граница, нарушение которой = FDA Warning Letter + product seizure + FTC consent decree:

**OK (structure/function — DSHEA permitted):**
— «Supports immune function»
— «Promotes restful sleep»
— «Helps maintain healthy cholesterol levels already within normal range»
— «Supports cognitive function»
— «Helps maintain healthy hormone balance»
— «Promotes muscle recovery»
— «Supports cardiovascular health»

**FAIL (disease claim — требует FDA drug approval NDA process):**
— «Cures insomnia» / «treats insomnia»
— «Treats diabetes» / «reverses diabetes» / «lowers blood sugar in diabetics»
— «Prevents cancer» / «reduces cancer risk» / «fights tumor growth»
— «Reverses ED» / «treats erectile dysfunction» / «cures impotence»
— «Treats depression» / «cures anxiety» / «manages bipolar»
— «Lowers high blood pressure» / «treats hypertension»
— «Treats COVID» / «prevents flu» / «kills viruses»
— «Reverses arthritis» / «cures joint pain»

**Implied disease claim FAIL pattern (более коварный):**
— Imagery sick person → healthy person transition = implied treatment claim.
— Before/after с medical visual cue (waist measurement, BP cuff, glucose meter) = implied disease claim даже без слов.
— Voice-over «my doctor said my numbers came back normal» = implied disease treatment.
— «Like Ambien without prescription» / «like Viagra naturally» = drug comparison = implied drug-equivalence claim = FDA red flag.

RULE: каждая claim в Dialogue / overlay / on-screen text прогоняется через структуру «supports/promotes/helps maintain [body function/system] [already within normal range]». Если конструкция не работает — переписать или удалить.

**ПРАВИЛО 3 — Mandatory FDA disclaimer overlay (DSHEA §403r-6):**

Не «опционально к рассмотрению». Overlay обязателен в bottom-third для любого крео с structure/function claim. Формат:

`«*These statements have not been evaluated by the Food and Drug Administration. This product is not intended to diagnose, treat, cure, or prevent any disease.»`

Спецификация:
— 12-14pt Inter Regular / Helvetica, white-90% на gradient-darken bottom-strip.
— Present 0-end (НЕ flash на последние 2s — FTC «clear and conspicuous» standard).
— Размещение: bottom-third, выше всех CTA / brand-logo overlay (чтобы не закрывалось).
— Языковая локализация для bilingual ads (ES + EN US-Hispanic market) — disclaimer на обоих языках одновременно.
— Если несколько claims в одном reel — один disclaimer покрывает все, но **обязан** появляться pre-claim или одновременно с первым claim, не post-claim.

GUARDRAIL: если product не зарегистрирован как dietary supplement (например, «functional food» / «medical food» / cosmetic с health claim) — disclaimer формулировка меняется. Flag в intake: `fda_product_category: dietary_supplement | functional_food | medical_food | cosmetic | otc_drug` — preset подбирает correct disclaimer.

**ПРАВИЛО 4 — Substantiation для structure/function claim (FTC «competent and reliable scientific evidence»):**

Любая claim о benefit / efficacy / outcome = подпадает под FTC substantiation standard (Health Products Compliance Guidance Dec 2022). Self-attested «our customers love it» / «our blend works» = НЕ substantiation. Требования:

— **Minimum standard:** 1 well-designed human RCT (randomized controlled trial), peer-reviewed, опубликованный в indexed journal (PubMed / Scopus / Web of Science), на том же ingredient + dose + population как в продукте.
— **НЕ substantiation:** in vitro study, animal study only (mice / rats), single-case anecdote, observational без control group, journal без peer review, study на different ingredient form (extract vs whole-plant) или different dose.
— **Reference на лендинге обязательна:** clickable citation list на product page (минимум author / journal / year / DOI), доступна до checkout.
— **Если ingredient = proprietary blend без published RCT** на сам blend — claim ограничена до characterization individual ingredients, не blend efficacy.
— **Если study sponsored by ingredient supplier** — disclosure conflict-of-interest в reference list (FTC §255.5 material connection).

PASS пример substantiation: «Magnesium glycinate 200mg supports sleep onset — based on Abbasi et al. 2012, J Res Med Sci, DOI:XX (n=46 RCT, elderly insomnia, 8-week)».

FAIL пример: «Our proprietary sleep blend is clinically proven» (без specific study, без dose, без population, без citation).

GUARDRAIL: «Clinically proven» / «scientifically proven» / «doctor-recommended» = elevated claim, требует ещё более robust substantiation (multiple RCT или meta-analysis). Если 1 RCT — заменить на «studied» / «researched» / «supported by clinical research».

**ПРАВИЛО 5 — Testimonial / before-after compliance (FTC §255 + §255.5 + Endorsement Guides 2023 update):**

**Testimonial с specific outcome («I lost 27 lbs in 6 weeks» / «my testosterone went from 280 to 650») = ATYPICAL результат:**
— On-frame disclaimer обязателен: «Results not typical. Average user experiences [X] under [conditions Y]» — на той же frame с testimonial, не bottom overlay.
— Substantiation typical results disclosure: компания обязана иметь data на «what typical user experiences» (не маркетинговая фикция).
— Sample-size + methodology: «Based on internal study, n=X users, 12-week period, with diet + exercise per protocol».

**Before/after photo testimonials (особо weight-loss / body transformation):**
— FTC red flag по умолчанию. Default — НЕ использовать в крео для US-targeting.
— Если используются — atypical disclaimer + «paid testimonial» disclosure (если compensated) + photo-manipulation disclosure (если retouched).
— FTC «Gut Check» 7 false weight-loss claims auto-violation: (1) lose 2+ lbs/week without diet/exercise, (2) lose substantial weight regardless of diet, (3) cause permanent weight loss, (4) block fat absorption to enable substantial weight loss, (5) cause substantial weight loss for all users, (6) cause substantial weight loss by wearing/applying to skin, (7) lose more than 3 lbs/week for over 4 weeks. Любая из 7 = automatic FTC violation, $5M+ TINA.org enforcement precedent.

**Material connection (FTC §255.5):**
— Paid endorser / influencer compensated в любой форме (cash, free product worth $X, commission affiliate link) = `#ad` / `#sponsored` / «Paid partnership» disclosure clear and conspicuous, начало caption + on-frame первые 3s.
— Employee endorser = «I work for [Brand]» disclosure.
— Family/friend endorser of business owner = «my partner owns this business» disclosure.

**AI-generated influencer testimonial (NEW grey zone):**
— FTC §255 + state right-of-publicity = AI-fabricated «testimonial» от persona, которая не существует / не использовала продукт = deceptive practice (Endorsement Guides 2023 update прямо addresses AI/synthetic endorsers).
— Required disclosure: «AI-generated character, not real customer testimonial».
— Если AI-likeness реального person (UGC creator подписал release) — material connection + AI disclosure both required.

PASS пример testimonial: `«I've been taking it 8 weeks, sleep feels deeper» [overlay: "Individual experience. Results vary. Paid endorsement."] [bottom: FDA disclaimer]`

FAIL пример: `«Lost 27 lbs in 30 days without changing my diet — this stuff is magic!»` → 4 нарушения (atypical без disclaimer + Gut Check #2 «without diet» + implied drug-equivalence «magic» + missing FDA disclaimer).

**ПРАВИЛО 6 — Category-specific guardrails (weight-loss / ED / sleep / hormonal):**

**Weight-loss (highest FTC enforcement priority):**
— Hard-block 7 «Gut Check» claims (см. Правило 5).
— «Lose X lbs in N days» pattern = FTC red flag. Replace: «may support weight management as part of healthy diet and exercise».
— «Without diet or exercise» / «while you sleep» / «melts fat» = automatic FAIL.
— Caloric deficit context required: «used alongside reduced-calorie diet and regular physical activity».

**ED supplements (FDA aggressive enforcement):**
— Hard-block: claims на sildenafil analogs / tadalafil analogs / PDE5 inhibitor mechanism (FDA seized 50+ companies 2019-2024 за undeclared sildenafil в «natural» male enhancement).
— Hard-block: «like Viagra» / «like Cialis» / «works in 30 minutes like a prescription» / «harder erections guaranteed» = drug claim + comparison = automatic FDA red flag.
— Grey zone (case-by-case с pre-clearance): «supports healthy circulation», «supports male vitality», «supports libido as part of healthy lifestyle» — допустимо если ingredient profile НЕ contains undeclared pharma.
— Intake flag `ingredient_panel_third_party_tested: y/n` — если no, escalate.

**Sleep supplements:**
— Melatonin OK как structure/function: «supports sleep cycle», «helps maintain natural sleep-wake rhythm».
— Magnesium glycinate / L-theanine / valerian / chamomile OK structure/function: «promotes relaxation», «supports sleep onset».
— FAIL: «cures insomnia», «treats sleep apnea», «replaces prescription sleep meds», «like Ambien but natural».

**Hormonal coaching:**
— Если коуч НЕ MD / DO — hard-block medical advice (state licensure violation, particularly CA / NY / TX / FL).
— Mandatory disclaimer overlay: «Not medical advice. Consult your physician before changing diet, exercise, or supplement regimen. Not a substitute for diagnosis or treatment.»
— TRT / testosterone replacement therapy = Schedule III controlled substance (DEA), требует MD prescription. «Hormonal optimization coaching» НЕ может ни prescribe, ни recommend specific TRT protocol. Replace: «education on lifestyle factors affecting hormone health».
— DHEA в US — sold as supplement OTC, но FDA grey zone (banned in sports). Если targeting athletes — additional WADA / NCAA disclosure.

**ПРАВИЛО 7 — Real clinician Soul ID (state board scrutiny + AMA Code §5.04 + FTC §255):**

Если Soul ID = real MD / DO / RN / RD / DC / DPT в endorsement формате («I'm Dr. Sarah Chen, board-certified endocrinologist, and I recommend this supplement to my patients») → multi-layer compliance:

— **State medical board advertising rules:** каждый state board (CA Medical Board / NY State Department of Health / TX Medical Board / FL Board of Medicine) имеет свои advertising rules. «Recommended by my doctor» в open feed без state-licensure context = potential scrutiny. Flag в intake: `clinician_state_license: {state list}` + `targeting_geo_match_license: y/n`.
— **AMA Code of Medical Ethics §5.02 + §5.04** (Communications to Public + Self-Promotion): запрет «testimonials of patient endorsement» в advertising без strict disclosure; запрет claim «superior service» без objective evidence; запрет «exclusive technique» без peer-reviewed evidence.
— **Paid endorsement disclosure (FTC §255):** real MD endorser получает compensation (cash, equity, free product, commission) → mandatory clear disclosure: «Paid medical advisor / Compensated endorsement / Equity stake holder». Disclosure в первые 3s + caption start.
— **Substantiation поверх «my clinical experience»:** «I see this work in my patients» = NOT substantiation. Required: published RCT references + sample-size of clinician's practice + period.
— **AI-likeness real MD без disclosure = misrepresentation under state board + FTC + Lanham Act:** AI-rendered Dr. X в кадре без AI disclosure → patients думают real Dr. X лично endorses = false endorsement. AI DISCLOSURE pack mandatory: overlay «AI-assisted visual · Dr. [Name], [Title]» в bottom-third 0-end.
— **License verification:** перед использованием real-clinician Soul ID — verify active license в state board public lookup, NPI registry check, board-certification verification (ABMS for MDs / AOA for DOs). Suspended / revoked license = hard-block.

Если clinician = coach без medical license (RD nutritionist, certified health coach, IFM-certified practitioner): Soul ID OK, НО:
— Title accuracy: «Certified Health Coach» НЕ «Doctor» / «Physician» / «Specialist» (medical title impersonation = state criminal statute в некоторых states).
— Disclaimer overlay: «Educational only. Not medical advice. Not a licensed physician.»

**ПРАВИЛО 8 — State law overlay (CA Prop 65 + NY AG + TX DTPA + targeting matrix):**

**CA Prop 65 (Safe Drinking Water and Toxic Enforcement Act 1986):**
— Если product содержит ingredient на Prop 65 list (lead, cadmium, certain botanicals, BPA в bottle) → warning label на product + on-frame warning в крео для CA-targeting: «WARNING: This product can expose you to chemicals including [chemical], which is known to the State of California to cause [cancer/birth defects/reproductive harm]. For more information go to www.P65Warnings.ca.gov.»
— Без warning + CA-targeting = private right of action ($2,500/day per violation + attorney fees) — major enforcement industry.
— Flag в intake: `prop65_applicable_ingredients: y/n + which`. Если yes + CA-targeting — overlay mandatory.

**NY AG enforcement (precedent: Schneiderman 2015 GNC / Walgreens / Walmart / Target DNA-testing case):**
— Botanical supplement DNA testing case — NY AG demanded each product contain stated botanical via DNA barcoding. Replication risk для любой botanical supplement claim в NY-targeting.
— Required для NY-targeting: third-party verification of ingredient identity + potency (USP / NSF / ConsumerLab / Eurofins certificate of analysis).
— Flag `nyc_targeting + botanical_product: y/n` → require third-party COA reference на лендинге.

**TX Deceptive Trade Practices Act (DTPA):**
— Broader than FTC — private right of action + treble damages + attorney fees.
— «Implied warranty» claims в Texas-targeting крео = elevated risk. Conservative formulation требуется.

**FL — Office of Attorney General + Florida Drug and Cosmetic Act:**
— Pre-market notification for certain «functional food» categories.
— Aggressive enforcement weight-loss claims.

**FTC §255 для Instagram / TikTok / YouTube US-targeting:**
— #ad / #sponsored / «Paid partnership» обязательны для влогера-endorser принимающего supplement on-camera.
— Disclosure visible WITHOUT clicking «more» button (caption start) AND on-frame первые 3s.
— TikTok Branded Content toggle ≠ FTC compliance alone — overlay disclosure ещё нужен (TikTok toggle = platform compliance, не FTC).
— AI-generated influencer testimonial (см. Правило 5) — отдельный FTC + state right-of-publicity layer.

**Cross-state кампания targeting:**
— Если кампания спан CA + NY + TX + FL одновременно — overlay rotation по placement-set (Prop 65 для CA placement, NY AG language для NY placement, etc.), НЕ один collapsed overlay со всеми states (нечитаемо + не соответствует ни одному state properly).
— Default: разделить кампанию на per-state placement-sets с per-state regulatory overlay.

GUARDRAIL: если product НЕ third-party tested (COA от ISO 17025 accredited lab) — escalate всю campaign на pre-launch compliance review независимо от state.

**ПРАВИЛО 9 — FTC Click-to-Cancel 16 CFR §425 + telehealth state-licensure (NEW T.7-C GAP):**

Subscription-based DTC supplement model (auto-renew / «cancel anytime» / monthly subscription) = триггер FTC Click-to-Cancel Rule 16 CFR §425 (effective 2025).

Требования:
— **Simple cancellation method:** cancellation должна быть в том же канале как enrollment (если sign-up онлайн — cancel должна быть онлайн в равном clicks). НЕТ «call to cancel» если sign-up был онлайн.
— **Material terms disclosure pre-enrollment:** auto-renew frequency + amount + how-to-cancel — clear-and-conspicuous ДО collection payment info. Reel CTA «Start your trial» должен link на лендинг с этими disclosures выше fold.
— **Express informed consent:** affirmative click на «I understand subscription will auto-renew at $X/month» отдельно от primary CTA. НЕТ pre-checked boxes.
— **Annual reminder для long subscriptions:** для ≥12 months — annual reminder за ≥30 days до renewal.
— **FAIL pattern в крео:** «Try risk-free 30 days» без disclosure что после 30 дней auto-charge $X/month → FTC §5 deception + Click-to-Cancel violation. Replace: «30-day satisfaction guarantee — cancel anytime via [link] before day 30 to avoid $X/month subscription».

**Telehealth state-licensure (для hormonal coaching + ED / TRT prescribing):**

Если creо advertises «MD-supervised TRT protocol» / «telehealth hormone optimization» / «get prescription online» → telehealth licensure compliance:
— MD должен быть licensed в КАЖДОМ state куда targeting (state-by-state licensure, не universal). Flag в intake: `telehealth_states_licensed: [list]` + `targeting_geo: [list]` → match check.
— Ryan Haight Act (controlled substances online) — TRT = Schedule III → не может быть prescribed only via online consult, требует initial in-person OR DEA Special Registration (limited).
— «Prescription delivered to your door» framing для controlled substances → DEA scrutiny.
— Replace: «Telehealth-supported lifestyle education in [licensed states] · Prescription decisions made by your state-licensed physician».

**WELLNESS_HEALTH_RESTRICTED_USA_PRESET — финальный чек-лист (9 проверок перед выдачей промта):**

| # | Проверка | PASS если | FAIL → |
|---|---|---|---|
| 1 | Marketing Studio + Kling 3.0 / Seedance 2.0 + PORTRAIT CU + ANTI-AI-LOOK + HANDS IN FRAME + KITCHEN/HOME LIFESTYLE packs; label / supplement-facts через §19A UI MOCKUP PIPELINE; format 9:16 + 6-9s | Да | Переключить workspace / модель, подключить недостающие packs, route label через pipeline |
| 2 | Все claims проходят structure/function test («supports/promotes/helps maintain [function] [within normal range]»), нет disease claims (cures/treats/prevents/reverses + disease name), нет implied disease claims (sick→healthy imagery, medical visual cue, drug comparison) | Да | Переписать в S/F конструкцию, удалить sick→healthy arc, заменить «like Viagra/Ambien» на S/F формулировку |
| 3 | FDA mandatory disclaimer overlay включён («These statements have not been evaluated by the FDA. This product is not intended to diagnose, treat, cure, or prevent any disease.»), bottom-third, present 0-end, 12-14pt, выше CTA / brand overlay; bilingual если ES+EN | Да | Добавить overlay, поднять выше CTA, проверить language coverage |
| 4 | Substantiation: structure/function claim = minimum 1 human RCT peer-reviewed (PubMed), на тот же ingredient + dose + population; reference на лендинге clickable; conflict-of-interest disclosure если sponsored study; «clinically proven» только если multiple RCT / meta-analysis | Да | Запросить study reference, переписать в qualified «studied/researched», убрать «clinically proven» если нет multiple RCT |
| 5 | Testimonial с specific outcome = atypical disclaimer on-frame + typical results data + material-connection disclosure (#ad / Paid partnership) clear-and-conspicuous; before/after weight-loss default OFF; «Gut Check» 7 claims hard-block; AI-generated testimonial = separate disclosure | Да | Добавить on-frame disclaimer, убрать «Gut Check» pattern, добавить material disclosure, удалить before/after или escalate |
| 6 | Category guardrails: weight-loss НЕ 7 Gut Check + caloric-deficit context; ED НЕ sildenafil/PDE5 claim + НЕ drug comparison; sleep — melatonin OK S/F не «cures insomnia»; hormonal coaching — «not medical advice» disclaimer + non-MD не prescribe TRT | Да | Удалить запрещённые claims, добавить «with diet and exercise» context, переписать ED claims в S/F, добавить «not medical advice» |
| 7 | Real clinician Soul ID — active state license verified + AMA §5.04 endorsement disclosure + FTC paid-endorsement disclosure + substantiation поверх «my clinical experience» + AI DISCLOSURE pack («AI-assisted visual · Dr. [Name], [Title]»); non-MD coach — title accuracy + «not licensed physician» disclaimer | Да | License lookup + добавить paid-endorsement disclosure + AI overlay + substantiation; для coach — fix title + добавить disclaimer |
| 8 | State law overlay: CA Prop 65 warning если applicable + CA targeting; NY botanical supplement — third-party COA reference; TX DTPA conservative formulation; FL pre-market если applicable; cross-state — rotation по placement-set; FTC §255 disclosure на Instagram/TikTok/YouTube (caption start + on-frame 3s) | Да | Добавить per-state overlay, разделить placement-sets, добавить COA reference, добавить #ad first-3s |
| 9 | FTC Click-to-Cancel 16 CFR §425 (если subscription model): simple cancellation = enrollment channel + material terms pre-enrollment + express informed consent + annual reminder; telehealth state-licensure match для MD-supervised hormonal/ED programs | Да | Переписать «risk-free trial» с auto-charge disclosure, переключить cancellation на онлайн, добавить affirmative consent, match licensure states |

9/9 PASS → промт выпускается ученику.
≤8/9 PASS → return to editor, не выпускается. Конкретные FAIL-причины перечисляются в return-note.

**WELLNESS_HEALTH_RESTRICTED_USA — 3-STEP FUNNEL GRANULARITY:**

В отличие от плоского preset выше, для US-supplements funnel-step разбивка обязательна (по аналогии с HIGH_TICKET_PRO_SERVICES 3-STEP FUNNEL):

| Step | Цель | Арка | CTA | Регуляторный риск |
|------|------|------|-----|---|
| TOF | Awareness — educational lifestyle / wellness habit content | G через §19B EDUCATIONAL-PROGRESSION (process, ingredient education, без specific product claim) | «Get our sleep guide» / «Download morning routine PDF» / «Subscribe to weekly wellness newsletter» | Низкий (educational, не product claim — FDA / FTC scrutiny минимальный) |
| MOF | Nurture — ingredient story + brand POV + quality differentiator (third-party testing / sourcing) | C (founder / clinician Soul ID) с overlay disclaimers + KITCHEN/HOME pack | «Watch our sourcing story» / «See our COA report» / «Read clinical references» | Средний (structure/function claims начинаются — Правила 2-4 обязательны) |
| BOF | Close — product offer с full disclaimer stack | C (talking-head endorser) или G (product UI / pricing) | «Shop now» / «Subscribe & save 20%» / «Try risk-free 60 days» | Высокий (все 9 правил applicable + testimonial compliance + state law overlay + Click-to-Cancel) |

GUARDRAIL: BOF в cold open feed для weight-loss / ED / hormonal — auto-escalation на pre-launch compliance review (FTC priority enforcement categories). Default — soft TOF/MOF в cold, BOF только в retargeting warm-audience с prior brand exposure.

═══════════════════════════════════════════════════
EU_RUSSIAN_DIASPORA_PRESET — отдельный пресет sub-profile (волна Т.8 после Т.8-А создателя + Т.8-B адверсариала 18 GAP + Т.8-C мета cross-ref 6 юрисдикций)
═══════════════════════════════════════════════════

Контекст: «русскоязычная диаспора в EU/UK/IL после 2022» — это **горизонтальный sub-profile**, который накладывается поверх вертикали (CRISIS_EXPERT / HIGH_TICKET_PRO_SERVICES / REAL_ESTATE_EXPAT / INFOBIZ / LOCAL_SERVICE / EDTECH), а не заменяет её. До волны Т.8 покрытие было фрагментарным: DIASPORA-TONE TUNING для CRISIS × EU × LEGAL (строки 3153-3158), DIASPORA-TONE GUIDANCE по визуалу/палитре/звуку (строки 3183-3193), упоминания OFAC / GDPR Art.9 / language-based lookalike в HIGH_TICKET_PRO_SERVICES_PRESET ПРАВИЛО 9 (строки 3877-3891) и currency-таблица (строки 404-418). Для post-2022 политической реальности агент терял восемь критических слоёв: (1) GDPR Art. 6 + Art. 9 language-based targeting = ethnicity proxy = special-category processing, (2) кумулятивные санкционные режимы OFAC / EU 269/2014+833/2014 + art.5n advisory services restriction / UK OFSI / Swiss SECO + AML 5AMLD / FinCEN GTO для финансов и недвижимости, (3) национальные DPA-наслоения (PL UODO / DE BfDI / UK ICO / Cyprus DPC / IL PPA 2024) при cross-border targeting, (4) cross-border professional services guardrails (PL adwokat → DE BRAO + RBerG / DE Rechtsanwalt → NRA Kodeks Etyki / UK barrister → BSB), (5) cultural messaging guardrails (политически окрашенная «возвратная» лексика / UA-BY-KZ identity-respect / «русскоязычные» НЕ «русские» / Cyprus CIP suspended Nov 2020), (6) currency localization EUR/PLN/GBP/ILS с ECB substantiation, (7) EU AI Act art.50 extraterritorial transparency obligation для AI-likeness, (8) визуальная аутентичность «adapted to EU» wardrobe vs stuck в pre-2022 RU-glamour aesthetic + regulated attire AI-avatar guardrail (мантия адвоката / халат врача = uniform-as-claim-of-profession check). Этот пресет — единая точка истины.

**КОГДА АКТИВИРУЕТСЯ EU_RUSSIAN_DIASPORA_PRESET:**

Профиль клиента = CRISIS_EXPERT / HIGH_TICKET_PRO_SERVICES / REAL_ESTATE_EXPAT / INFOBIZ / LOCAL_SERVICE / EDTECH, и любой из триггеров:
— Целевая аудитория = русскоязычные релоканты / диаспора в EU (DE / PL / CZ / AT / CY / IT / ES / NL / FR / SE / FI) / UK / IL.
— Hook / Dialogue / EXACT STRING / overlay на русском языке адресуется аудитории, физически проживающей в EU/UK.
— Soul ID = эксперт-релокант (адвокат / advisor / broker / coach), оказывающий услугу cross-border (PL adwokat → DE-диаспора; CY-резидент → UK-диаспора).
— Гео-mix: agency / эксперт находится в одной EU-стране, аудитория — в другой (PL → DE / CY → UK / DE → AT).
— Чек ≥ 500 EUR / 2 000 PLN / 400 GBP за услугу (HIGH_TICKET territory) ИЛИ subscription ≥ 80 EUR/мес.
— Sub-vertical = Cyprus Non-Dom / Malta GRP / Portuguese D7 / DE Aufenthaltstitel / PL karta pobytu / UK Skilled Worker / Israeli aliyah — любой immigration / tax / wealth-structuring slot для релокантов.
— Profile contains flag `vertical=eu_diaspora_legal|eu_diaspora_realestate|eu_diaspora_infobiz|eu_diaspora_local_service|eu_diaspora_edtech|eu_diaspora_high_ticket`.
— Платформа = Meta / TikTok / Telegram Ads / LinkedIn с гео-таргетом ≥ 1 EU-страна И копи на русском.

Если хотя бы один триггер — все 8 правил ниже **обязательны**. Этот sub-profile **накладывается** на правила базовой вертикали (CRISIS-AUDIT-LAYER / HIGH_TICKET_PRO_SERVICES_PRESET / REAL_ESTATE_EXPAT_USA_PRESET), не заменяет их. При конфликте применяется **stricter rule**.

**ПРАВИЛО 1 — Workspace + модель + packs (дефолт жёсткий):**
— Workspace = Cinema Studio + Higgsfield Audio для cinematic legal / HIGH_TICKET / REAL_ESTATE diaspora-flight'ов (Berlin Mitte café exterior / Limassol marina golden hour / Warsaw Old Town facade). Marketing Studio = ТОЛЬКО для talking-head expert (релокант-эксперт в кадре, peer-tone, MOF/BOF).
— Модель = Veo 3.1 (default для cinematic + любой архитектурной EU-локации — Wiener Ringstrasse / Prague Vinohrady / Berlin Kreuzberg ломаются на Kling). Seedance 2.0 = fallback для establishing shots без архитектурной геометрии в near-field.
— Packs = PORTRAIT CU + ANTI-AI-LOOK + LIGHT CONSISTENCY (warm amber/gold ключ per DIASPORA-TONE GUIDANCE строки 3186-3187) + REFLECTION (café glass / marina water / apartment window) + FABRIC / HAIR (если senior expert Soul ID + cross-ref §21 EXECUTIVE-CALIBRATED HUMANIZATION).
— Higgsfield Audio — major key, тёплый vocal-led, НЕ minor / cinematic-trailer mood (см. строка 3187). Локализация voice-over: русский с нейтральным акцентом, БЕЗ маркеров «московского радио-диктора» или «эмигрантского ностальгического»; нейтральная подача в диапазоне 25-55 лет. **NEW T.8-B GAP:** запрет cultural-loaded music post-2022 (РОТ / советская эстрада / patriotic march) — может trigger Meta classifier политический контент.
— UI / маршрутный лист / fee schedule / документ-overlay в кадре = ВСЕГДА через §19A UI MOCKUP PIPELINE или §19B INFOGRAPHIC-CHART, не напрямую в Veo (Cyrillic в Veo при near-field рендерится с галлюцинациями глифов).
— Format = 9:16 + 9s (Meta + IG Reels primary для diaspora retail) / 16:9 + 12-15s (YouTube + LinkedIn для HIGH_TICKET institutional) / 1:1 + 7s (карусель листинг). Cross-ref §15 — формат-mix per placement-set обязателен для disclaimer rotation (ПРАВИЛО 8).

**ПРАВИЛО 2 — DIASPORA-TONE casting calibration (warm + confident + adapted-to-EU wardrobe + regulated-attire AI guardrail):**

Базовая DIASPORA-TONE GUIDANCE (строки 3183-3193) обязательна. Дополнительно для post-2022 audience:

— **Wardrobe эксперта-релоканта** = adapted-to-EU professional: charcoal / navy / muted olive wool blazer, дискретный shirt без logo, минимальные accessories. НЕ pre-2022 RU show-business glamour (золотой массивный signet, велюровый пиджак, vibrant shirt). НЕ stereotype «European local» (no Loden jacket, no Hermès scarf — это carbon-copy local, не релокант).
— **Visual posture** — confident peer, eye contact, head up, открытая ладонь в gesture (см. строка 3188). НЕ ссутуленный «уставший беженец», НЕ overconfident «прорвался-добился» с агрессивным жестом.
— **Палитра** — warm amber / gold / terracotta / oxblood (строка 3186). НЕ cold-desaturated-grey (читается как «европейский корпоративный» = не свой), НЕ faded-blue minor-key (читается как ностальгия-сожаление, см. ПРАВИЛО 6). **Для LEGAL diaspora** — warm-but-professional (приглушённый amber + neutral grey balance, НЕ saturated terracotta).
— **Background hint локальности** — Berlin Mitte café с латунным окном / Vienna Innere Stadt кофейня / Limassol marina с яхтами / Warsaw Stare Miasto facade / Prague Vinohrady апартамент / Tel Aviv белая Bauhaus стена. **Запрет stereotype reduction**: Wiener Schnitzel в кадре / Brandenburger Tor лоб в лоб / красная площадь / матрёшка / шапка-ушанка / медведь / самовар. Деталь locality нужна, но без туристического штампа.
— **Soul ID identifiability проверка** — если эксперт идентифицируем (firm website / LinkedIn / Bar registry) → AI DISCLOSURE pack ПРАВИЛО 8 + sign-off на AI-generation отдельно от sign-off на marketing.
— **Regulated-attire AI-avatar GUARDRAIL (NEW T.8-B КЕЙС 1+3 GAP):** мантия адвоката (PL toga / DE Robe / UK barrister wig+gown) + халат врача / медицинский костюм = **uniform-as-claim-of-profession**. AI-generated Soul ID в regulated attire = implicit claim о professional capacity = state bar / medical board scrutiny даже если в кадре нет explicit claim о услугах. PASS условия: либо (а) реальный лицензированный профессионал с verified registry # + AI DISCLOSURE pack, либо (б) переключение на business-casual wardrobe (без uniform), либо (в) generic ad-actor с явным «actor portrayal» overlay.
— **Mixed-family кадры** (KIDS_PARENTS overlay) — если family-content, mixed-race casting per CHILDREN IN FRAME pack (строки 895-898), особенно для UA/BY/KZ-смешанных семей в EU.

**ПРАВИЛО 3 — GDPR Art. 6 + Art. 9 language-based targeting compliance:**

Targeting «русскоговорящие в DE» / «Russian-speakers in PL» через Meta lookalike / interest-affinity / custom audience = ethnicity proxy через язык = **special-category processing под GDPR Art. 9** без explicit consent (EDPB Guidelines 8/2020 + CJEU C-184/20 OT v. Vyriausioji tarnybinės etikos komisija precedent — special-category attributes through proxy data).

Запреты (GDPR + национальные DPA):
— **Meta Custom Audience** seeded из «русскоязычных групп» / «RU community pages» / Telegram-чатов диаспоры → seed = ethnic-affinity processing → hard-block без Art. 9(2)(a) explicit consent.
— **Lookalike audience** на base «Russian-speakers in {country}» / «PL Cyrillic-typing users» → Art. 9 violation. PASS: lookalike seeded из behavior-based pixel events (page view / form-fill на лендинге, где consent уже собран).
— **Detailed targeting** на «Russian (Russia)» / «Russian (language)» / «Russian Orthodox Church» / «Russian literature interest» → ethnic-proxy = Art. 9. Дополнительно — **Russian Orthodox Church membership** post-2024 может trigger sanctioned-organization proximity check (Кирилл / Patriarchate of Moscow на sanctions list ряда стран). PASS: broad geo + behavior-based interests («Immigration services» / «International tax» / «Cross-border banking») БЕЗ ethnic-affinity / religious-affinity seed.
— **Pixel sharing** с третьими сторонами без DPA → GDPR Art. 28 violation.

Cross-ref CRISIS-AUDIT-LAYER C4 (combined-identifier risk).

PASS условия:
1. **Explicit consent funnel** — TOF cold креатив ведёт на лендинг с двойным opt-in (Art. 6(1)(a) + Art. 9(2)(a) для language preference), retargeting только из consented pool.
2. **Behavior-based audience** — pixel событий «engaged with immigration / international tax / property abroad content» без ethnic-affinity seed.
3. **Broad geo + bilingual copy** — broad EU geo + копи на русском + английском в одном крео; classifier не имеет ethnic-targeting trigger.
4. **Pre-flight через `meta-policy-checker`** категория «EU_RUSSIAN_DIASPORA — GDPR Art.9 language-targeting» — обязательна (NEVER #23 блокер расширение для EU).

FAIL пример: `Targeting: Berlin radius 25km · interest "Russian language" · lookalike from "Telegram channel @berlin_russians" subscribers · age 30-55`.
PASS пример: `Targeting: DE country-wide + interest "Cross-border tax · Immigration services · Property abroad" + lookalike (1%) seeded from consented form-fill events on landing page · ages 18+ · copy RU+ENG bilingual`.

**ПРАВИЛО 4 — Sanctions OFAC / SECO / EU / UK OFSI geo-screening + AML 5AMLD / FinCEN GTO для HIGH_TICKET:**

Targeting «русскоязычные в EU» = high-scrutiny zone для AML / sanctions screening — кумулятивно для финансовых услуг / недвижимости / HIGH_TICKET с cash-component.

**(a) Sanctions geo-screening (обязателен whitelist):**
— **OFAC SDN** (US persons и US-touching transactions) + **EU Council Regulation 269/2014** (asset freeze designated persons) + **833/2014** (sectoral) + **UK OFSI** consolidated list + **Swiss SECO** (post-2022 alignment с EU).
— Whitelist гео EU-residents (DE / PL / CZ / AT / CY / IT / ES / NL / FR / SE / FI / IE / GR / PT / RO / HU / SK / SI / EE / LT / LV / LU / MT) + UK + IL.
— **Hard-exclude direct targeting RU / BY / IR / KP / VE / Crimea / DPR / LPR / Donetsk / Luhansk / Zaporizhzhia / Kherson** — sanctioned territories. Даже «русскоязычные in CY» НЕ trigger sanction, но если creо направлено / читается как promotion услуги для resident-в-RU → OFAC General License / SDN match risk.
— **NEW T.8-B GAP — EU Reg 833/2014 art.5n advisory services restriction:** **запрет** оказывать accounting / auditing / legal / tax / business / management consulting / PR / advertising / market research / opinion polling services to (i) Government of Russia, (ii) legal persons established in Russia. Применима к PL/DE/CY-licensed adwokat / advisor / агентствам. Even если crео не explicitly target RU-residents, scope-of-services overlay должна явно exclude services to Russian-based legal entities.
— Cross-ref HIGH_TICKET_PRO_SERVICES_PRESET ПРАВИЛО 9(a) — sanctions/OFAC/SECO/EU geo-screening.

**(b) AML / 5AMLD / FinCEN GTO (для HIGH_TICKET / REAL_ESTATE / PRIVATE_BANKING diaspora):**
— EU 5AMLD (Directive 2018/843) — Enhanced Due Diligence для PEP / high-risk третьих стран. «Русскоязычная HNWI клиентура из CIS» = PEP-screening trigger.
— Cyprus AML Law 188(I)/2007 (последние изменения 2024) — usual для Cyprus Non-Dom / yacht-registration / IBC структур. **Cyprus CIP scheme (Citizenship by Investment) suspended 17 November 2020 — реклама «Cypriot passport через инвестицию / €300k → Citizenship» = hard-block** (выдаёт misselling currently-suspended programme). Замена: «Cyprus Permanent Residency через Investment route per Regulation 6(2) of Aliens & Immigration Regulations — не citizenship».
— FinCEN GTO применима для US-properties (cross-ref REAL_ESTATE_EXPAT_USA_PRESET ПРАВИЛО 7(a)), но для EU-real-estate (DE / FR / IT / ES / PT) — local AML EDD + transactions >10k EUR cash reporting через Notar / Notaire / Notario.
— **Запрет в крео** для HIGH_TICKET diaspora: «cash-friendly · anonymous · LLC через Cyprus · нулевая декларация» — auto-flag для AML compliance officer + регулятора. Замена: «работаем по KYC / AML compliance · structuring per local notary requirements».

**(c) Cross-platform sanctions screening:**
— Meta + Google + LinkedIn автоматически блокируют ads с RU/BY billing accounts (post-2022). Если эксперт ранее имел RU LE / RU bank account → switch на EU entity до запуска. Flag в intake: `billing_entity_jurisdiction: eu_member|uk|ch|il|other` → если RU/BY → hard-block платформенный.

**(d) Obliged-entity pre-screen (NEW T.8-B GAP):** Real-estate broker / wealth advisor / legal firm являются **obliged entities** под 5AMLD Art. 2. Запуск programmatic ads без SDN-pre-screen / EDD на audience pool = AML supervisory risk (CySEC / BaFin / FCA / PNL). Flag в intake: `obliged_entity_status: y/n` + `sdn_prescreen_completed: y/n + date` обязательны для HIGH_TICKET diaspora launches.

**ПРАВИЛО 5 — Cross-border professional services guardrail:**

Эксперт-релокант, оказывающий услугу cross-border (страна лицензии ≠ страна аудитории), триггерит дополнительный compliance-слой национальной адвокатской / advisory регуляторики.

— **PL adwokat / radca prawny → DE-диаспора** = **BRAO §43b** (Berufsordnung) + **RBerG / RDG** (Rechtsdienstleistungsgesetz — German Legal Services Act). Без локального BRAO admission или EU lawyer registration под §206 BRAO (Niederlassung) → unauthorized practice of law. PASS: оверлей «Adw. {Name}, Izba Adwokacka {miasto}, wpis #{NRA-num} · usługi w zakresie prawa polskiego, kontakt z partnerem niemieckim per BRAO §206» либо ограничение услуги до «PL law consultation only».
— **DE Rechtsanwalt → PL-диаспора** = **NRA Kodeks Etyki Adwokackiej** + **§5 ust.1 Prawo o adwokaturze**. Cross-border требует либо CCBE-registration, либо ограничения до «DE Recht consultation only».
— **UK barrister → EU-диаспора** = **BSB Handbook gC8 / gC9** (international practice rules) + Bar Council Brexit guidance (post-2021 — UK lawyers не имеют автоматического права на EU representation). Дополнительно — **BSB запрет identifiable face в advertising без chambers approval** (cross-ref HIGH_TICKET_PRO_SERVICES_PRESET ПРАВИЛО 8 GUARDRAIL #2).
— **CY-licensed lawyer → UK-диаспора** = Cyprus Bar Council + UK SRA Article 25 LSA 2007 (reserved activities). Только consultation на CY-law без UK-law-claim.
— **IL advocate → EU-диаспора** = Israeli Bar Rules + EU host-country bar. Post-2024 Israeli Privacy Law update применима к Israeli-resident data subjects.

Substantiation overlay обязательна: имя + registry number + жетон лицензирующей коллегии + scope-of-practice disclaimer.

FAIL пример: `Dialogue: "Адвокат поможет с банкротством в Германии — звоните"` (PL adwokat без BRAO disclosure → unauthorized practice).
PASS пример: `Dialogue: "Adw. Marek Kowalski, NRA #12847 · сопровождаю банкротство physical person по польскому праву (art.491 Pr.Up.) · сотрудничаю с партнёром Rechtsanwalt {N} BRAK München по DE-юрисдикции"` + overlay «PL law consultation only · DE matters per partner Rechtsanwalt».

**ПРАВИЛО 6 — Cultural messaging guardrail (post-2022 политическая чувствительность):**

— **«Возвратная» лексика default OFF** — «вернуться в РФ» / «вернуться домой» / «увидеть Родину снова» = политически окрашено post-2022. Для одной части аудитории — positive, для другой (UA / BY / RU-opposition / IL aliyah) — trigger. Default — заменять на:
  • «решить дело здесь, не выезжая»
  • «остаться на привычной системе банкротства»
  • «открыть practice в новой стране»
  • «закрыть финансовый вопрос в стране проживания»
  • «легализоваться без поездок»
  Cross-ref DIASPORA-TONE TUNING CRISIS × EU × LEGAL строка 3157.
— **«Русскоязычные» НЕ «русские»** — национальность-нейтральная формулировка. «Русскоязычная аудитория в EU» включает UA-релокантов (особенно post-2022), BY-релокантов, KZ / KG / UZ / GE / AM-релокантов с русским как функциональным языком. «Русские» = ethnic claim = identity-смешивание + politically toxic.
— **UA / BY / KZ / IL identity-respect** — не используй «наши» / «свои» / «земляки» как зонтик. Если креатив ориентирован на UA-релокантов специально — отдельный flight на украинском или с явной UA-identity маркой (без RU-symbols). Если креатив ориентирован на BY — учёт post-2020 political context (нейтральная подача, без «братский народ»). Для IL aliyah / репатриации — отдельный context (Hebrew co-language + Israeli locality marker).
— **Политически нейтральный copy** — НЕ упоминать «спецоперация» / «война» / «мобилизация» / «военкомат» / «релокация по политическим причинам» в крео (toxic для классификатора Meta + риск аккаунт-бана). Замена: «переезд» / «новая страна» / «жизнь за границей» / «вне РФ».
— **«Сохрани русский язык у ребёнка» — UK/IL toxic check (NEW T.8-B GAP):** для UK / IL diaspora-EDTECH аудитории «сохранение языка» нейтрально на bare-content, но toxicity post-2022 = «national pride preservation» reading. Default — добавить inclusive framing «двуязычное развитие (RU + {state language})» / «cognitive benefit bilingual» / «семейная коммуникация bilingual».
— **Religious symbols guardrail** — для post-Soviet православной audience: не показывать crucifix / иконы / монастырь prominently — это narrowing (FHA-аналог в EU = GDPR Art. 9 religious processing + Meta narrowing rules). Если religious-context контента — отдельный pack с явным opt-in.
— **Cyrillic в URL / handle / domain** — может попасть под Meta language-flag auto-targeting (выдаёт ethnic affiliation). Default: latin URL + Cyrillic копи внутри лендинга (после opt-in).

GUARDRAIL: Перед выпуском проверить hook через V17 (нет Жертвы) + DIASPORA-TONE GUIDANCE (амбиция + warm palette) + ПРАВИЛО 6 (политически нейтрально + identity-нейтрально).

**ПРАВИЛО 7 — Currency / pricing localization (EUR / PLN / GBP / ILS per country):**

Валютная таблица (cross-ref строки 404-418):
— **DE / AT / NL / CY / IT / ES / FR / IE / PT / GR / FI / EE / LT / LV / LU / MT** → **EUR** основная.
— **PL** → **PLN** основная, EUR допустим для diaspora-сегментов.
— **UK** → **GBP** основная.
— **CZ** → **CZK** основная, EUR допустим для diaspora.
— **CH** → **CHF** основная, EUR допустим.
— **IL** → **ILS** основная, USD допустим для премиума.
— **USD в EU/UK diaspora креативе** — default OFF. Допустим ТОЛЬКО если эксперт оказывает US-связанную услугу (FIRPTA / EB-5 / US-tax / US-real-estate cross-ref REAL_ESTATE_EXPAT_USA_PRESET).

**Double-pricing rules:**
— «35 zł / 8 EUR» — допустим ТОЛЬКО для PL-сегмента смешанного с EU-residents (например, PL adwokat работает с PL-резидентами и PL-релокантами в DE/AT).
— Расхождение ±3% от ECB exchange rate → требует substantiation overlay «по курсу ECB на {дата}». Если расхождение >3% → fallback на одну валюту (см. строка 418).
— **НЕ дублировать в EU / UK** — «990 EUR / £850» в одном крео раздувает EXACT STRING + триггерит T23.

**ECB substantiation:**
— Source = ECB euro foreign exchange reference rates (https://www.ecb.europa.eu/stats/eurofxref/) — daily 16:00 CET fix.
— Если конвертация в крео — overlay «по курсу ECB {дата}» или ссылка на лендинг с актуальной таблицей.

**Pricing prominence:**
— typical price prominence equal с «entry» / «от» — иначе FTC-аналог в EU = UCPD Directive 2005/29/EC misleading omission. «От 990 EUR» БЕЗ typical → заменить на «typical mandate 2 500 EUR, entry-level consultation от 990 EUR».

**ПРАВИЛО 8 — Country-specific DPA overlay + AI DISCLOSURE pack + EU AI Act art.50:**

**(a) National DPA matrix (cross-border targeting = double-jurisdiction):**
— **DE** → BfDI (federal) + Landesdatenschutzbeauftragte (per Bundesland — особенно BayLDA Bavaria жёсткая).
— **PL** → UODO (Urząd Ochrony Danych Osobowych).
— **UK** → ICO (Information Commissioner's Office) — post-Brexit UK GDPR + Data Protection Act 2018.
— **CY** → Cyprus DPC (Commissioner for Personal Data Protection).
— **AT** → DSB (Datenschutzbehörde).
— **FR** → CNIL.
— **IL** → Privacy Protection Authority (PPA Amendment 13 2024 — special-category включает «communal-religious membership» — closer to GDPR).

Cross-border (PL agency → DE-диаспора) = double-jurisdiction. Default: privacy notice на лендинге с указанием **обеих** DPA + DPO contact в EU country аудитории (Art. 27 GDPR — EU representative обязателен если controller не в EU).

**(b) AI DISCLOSURE pack — обязательна для public diaspora-expert Soul ID:**
Если Soul ID = реальный лицензированный эксперт (Bar registry / Companies House / SEC ADV / NAR-аналог) → AI DISCLOSURE pack ОБЯЗАТЕЛЕН независимо от triggera. Pattern совпадает с HIGH_TICKET_PRO_SERVICES_PRESET ПРАВИЛО 8 + REAL_ESTATE_EXPAT_USA_PRESET ПРАВИЛО 8.

Overlay-формат: `«AI-assisted visual · {Имя}, {Title} · {Registry} #{N} · {Firm}»` (bottom-third, present 0-end, ≤120 chars, Inter Regular 14pt, white-90% на gradient-darken). Локализация — на языке аудитории (русский) + дублирующая строка на государственном языке страны аудитории (DE / PL / EN-UK) — ПРАВИЛО 8(a) DPA требование национального языка для compliance overlay.

**(c) EU AI Act art.50 (effective August 2026):**
Transparency obligation для AI-generated content depicting реального person. **Extraterritorial** — применима к любому AI-likeness креативу, **видимому в EU**, даже если producer не EU-резидент. Overlay в **(b)** покрывает art.50 требование. Sign-off на marketing ≠ sign-off на AI-generation — требуется отдельный AI-generation release (cross-ref HIGH_TICKET_PRO_SERVICES_PRESET ПРАВИЛО 8 GUARDRAIL #1).

**EU_RUSSIAN_DIASPORA_PRESET — финальный чек-лист (8 проверок перед выдачей промта):**

| # | Проверка | PASS если | FAIL → |
|---|---|---|---|
| 1 | Cinema Studio / Marketing Studio (per use-case) + Veo 3.1 + PORTRAIT CU + ANTI-AI-LOOK + LIGHT CONSISTENCY (warm amber/gold) + REFLECTION + Higgsfield Audio (major key vocal-led, БЕЗ cultural-loaded music); UI/документы через §19A/19B | Да | Переключить workspace, подключить недостающие packs, переключить Audio mode |
| 2 | DIASPORA-TONE casting: warm palette + confident posture + adapted-to-EU wardrobe (НЕ pre-2022 RU glamour, НЕ stereotype EU local); локация detail без штампа; regulated-attire AI guardrail (мантия / халат = verified registry + AI DISCLOSURE ИЛИ business-casual ИЛИ actor portrayal overlay); mixed-family cast если KIDS_PARENTS overlay | Да | Заменить wardrobe / посадку / локацию; удалить штамповый prop; добавить verification overlay для regulated-attire или переключить wardrobe |
| 3 | GDPR Art. 6 + Art. 9 compliance: НЕТ language-based lookalike / ethnic-affinity seed / Russian-language interest targeting / Russian Orthodox affinity; broad geo + behavior-based; explicit consent funnel для retargeting; pre-flight `meta-policy-checker` категория «EU_RUSSIAN_DIASPORA — GDPR Art.9 language-targeting» | Да | Расширить targeting на broad geo + behavior; отключить language-seed lookalike; перевести на consented audience; запустить meta-policy-checker |
| 4 | Sanctions OFAC / SECO / EU 269/2014 + 833/2014 (art.5n advisory restriction) / UK OFSI geo-whitelist (EU/UK/IL residents) + hard-exclude RU/BY/IR/KP/VE; AML 5AMLD / FinCEN GTO для HIGH_TICKET / REAL_ESTATE; obliged-entity SDN pre-screen completed; billing entity jurisdiction = EU/UK/CH/IL (НЕ RU/BY); Cyprus CIP НЕ упомянут как valid programme (suspended Nov 2020) | Да | Скорректировать geo-whitelist; escalate на AML compliance officer; сменить billing entity; удалить «cash-friendly / anonymous» framing; заменить «Cypriot passport» на «Cyprus Permanent Residency» |
| 5 | Cross-border professional services: PL adwokat → BRAO §206 / RBerG check; DE Rechtsanwalt → NRA Kodeks Etyki / CCBE; UK barrister → BSB gC8/gC9 + chambers approval для face; scope-of-practice disclaimer overlay (registry # + jurisdiction limit) | Да | Добавить registry # + scope disclaimer; ограничить услугу до single-jurisdiction; switch на partner-firm structure |
| 6 | Cultural messaging: «возвратная» лексика default OFF (замена на «решить здесь / не выезжая»); «русскоязычные» НЕ «русские»; UA/BY/KZ/IL identity-respect; политически нейтрально (нет «война / спецоперация / мобилизация»); «сохрани русский язык у ребёнка» → inclusive bilingual framing; religious symbols не prominently; latin URL + Cyrillic копи | Да | Переписать hook без «вернуться / Родина»; заменить «русские» → «русскоязычные»; удалить политически окрашенные термины; добавить bilingual framing; переключить URL на latin |
| 7 | Currency / pricing localization: EUR/PLN/GBP/ILS per country; double-pricing только для PL-mixed с ECB substantiation (±3%); typical price prominence equal с «от/from»; НЕТ USD в EU/UK diaspora креативе (кроме US-связанной услуги) | Да | Заменить валюту на основную per гео; добавить typical price; добавить ECB substantiation overlay или fallback на одну валюту |
| 8 | DPA overlay + AI DISCLOSURE pack: privacy notice ссылается на обе DPA при cross-border (PL UODO + DE BfDI); EU representative Art. 27 если controller не EU; AI DISCLOSURE overlay «AI-assisted visual · {Name}, {Registry} #{N}» bilingual (RU + state language); EU AI Act art.50 sign-off на AI-generation отдельно от marketing release | Да | Дописать privacy notice; назначить EU representative; добавить AI DISCLOSURE overlay; запросить отдельный AI-generation release |

8/8 PASS → промт выпускается ученику.
≤7/8 PASS → return to editor, не выпускается. Конкретные FAIL-причины перечисляются в return-note.

**EU_RUSSIAN_DIASPORA — 3-STEP FUNNEL GRANULARITY:**

| Step | Цель | Арка | EXACT STRING focus + Tone | CTA | Регуляторный риск |
|------|------|------|---|-----|---|
| TOF | Awareness — образовательный контент для cold diaspora-аудитории (общая проблема релоканта, не listing-specific) | F через §19B ANIMATED-DIAGRAM (3-этапа процедуры / market overview без identifiable people) | «Вы» — спокойный авторитетный · warm amber palette · нейтральный voice-over · НЕТ возвратной лексики | «Скачайте гайд по {topic}» / «Подпишитесь на чек-лист релокантов EU» / «Получите карту юрисдикций Cyprus Non-Dom» | Низкий (educational, не financial promotion / не listing-specific) |
| MOF | Nurture — авторитет эксперта-релоканта (методология + cross-border process + case без NDA) | C — эксперт Soul ID tripod talking-head + §19B EDUCATIONAL-PROGRESSION (1→4 этап процедуры) | «Вы» → «ты» (если peer-tone уместен per сегменту) · empathic peer · adapted-to-EU wardrobe | «Запишитесь на 15-30-мин разбор бесплатно» / «Получите methodology PDF» / «Anonymized case-study» | Средний (substantiation broker/lawyer claims + GDPR Art. 9 при retargeting + cross-border BRAO/NRA disclosure) |
| BOF | Close — confidential pre-qualified call, конкретный action на платную | C — эксперт Soul ID + signed engagement letter overlay | Confident neutral («запишитесь на платную — это ваше решение») · без давления · конкретно | «Запишитесь на платную сессию {EUR/PLN/GBP}» / «Получите engagement proposal» / «Speak to partner» | Высокий (ABA 7.3-аналог в EU = SRA / BRAO / NRA solicitation rules cold; FCA s.21 для UK financial promo; sanctions screening для HIGH_TICKET cash-component) |

GUARDRAIL: Cold BOF CTA в open feed для регулируемых услуг (LEGAL / financial / REAL_ESTATE diaspora) — высокий риск SRA / BRAO / FCA / NRA solicitation violation. Default — soft TOF/MOF в cold-аудитории; BOF — только в retargeting / warm после consent collection + identity verification (KYC pre-screen).

CROSS-REFERENCES (не дублировать в этом пресете, использовать ссылками):
— **DIASPORA-TONE GUIDANCE строки 3183-3193** — warm palette / confident posture / ambition-led hook / time-anchor / запрет возвратной лексики без амбиции / запрет возрастного маркера без амбиции — обязательны поверх ПРАВИЛО 2.
— **DIASPORA-TONE TUNING CRISIS × EU × LEGAL строки 3153-3158** — TOF/MOF/BOF tone-шкала и запрет возвратной лексики для PL-диаспоры — частный случай ПРАВИЛО 6, применим напрямую для CRISIS_EXPERT × EU diaspora.
— **CRISIS-AUDIT-LAYER** (раздел V19-BIOCLAIM для legal substantiation строки 3159-3172) — substantiation для LEGAL claim (sygnatura akt / NRA membership / years of practice через karta pobytu) применима для cross-border legal services из ПРАВИЛО 5. Combined-identifier C4 — cross-ref для GDPR Art. 9 risk из ПРАВИЛО 3.
— **HIGH_TICKET_PRO_SERVICES_PRESET ПРАВИЛО 9** (sanctions/OFAC + Reg D general-solicitation + dual-credentialing + GDPR Art. 9 language-based lookalike) — расширяется в этом preset на полную регуляторную матрицу sanctions (ПРАВИЛО 4) + GDPR (ПРАВИЛО 3) + cross-border (ПРАВИЛО 5).
— **HIGH_TICKET_PRO_SERVICES_PRESET ПРАВИЛО 8** (AI DISCLOSURE для senior partner Soul ID) + **REAL_ESTATE_EXPAT_USA_PRESET ПРАВИЛО 8** (broker AI DISCLOSURE) — pattern переиспользуется в ПРАВИЛО 8 этого preset для diaspora-эксперта (Bar registry overlay bilingual).
— **REAL_ESTATE_EXPAT_USA_PRESET ПРАВИЛО 6** (FIRPTA / SEC Reg D / TRID) — применима если EU-diaspora эксперт refer-ит на US-property; double-preset активация (US preset + EU diaspora sub-profile).
— **Currency-таблица строки 404-418** + **MULTI-CURRENCY FOOTER rule строки 420+** — расширение в ПРАВИЛО 7 для EU/UK diaspora-specific (double-pricing PL-mixed с ECB substantiation).
— **§11 Soul ID guardrails + §15 NEVER #23 meta-policy блокер + §19A UI MOCKUP + §19B INFOGRAPHIC-CHART + §21 EXECUTIVE-CALIBRATED HUMANIZATION** — универсальные guards, применимы поверх preset.
— **V17 (Жертва hook check) + V18 (substantiation) + V19-BIOCLAIM** — universal guards, проходятся поверх ПРАВИЛО 2 (визуал) + ПРАВИЛО 5 (cross-border claims) + ПРАВИЛО 6 (нейтральный hook).

═══════════════════════════════════════════════════

═══════════════════════════════════════════════════
ECOM_IMPULSE_USA_PRESET — отдельный пресет (волна Т.9 после Т.9-А создателя)
═══════════════════════════════════════════════════

Контекст: ECOM_IMPULSE_USA (DTC physical product $15-100 single purchase — bath bombs / coffee subscription / pet supplies monthly box / phone accessories / kitchen gadgets / small fitness equipment) — последняя из 10 канонических ниш с risk-profile 5, не имевшая дедикейтед PRESET до волны Т.9. До этой волны секция ECOM_IMPULSE покрывалась 3 точечными упоминаниями (строка 2244 — арка D «продукт в действии»; строка 2756 — CTA-matrix; строка 2799 — Soul ID опционален только в outro brand frame). Для US-кампаний агент терял шесть критических слоёв: (1) FTC «Negative Option Marketing Rule» 2024/2025 + FTC ROSCA (Restore Online Shoppers' Confidence Act) для express informed consent при auto-renew subscription DTC моделях (bath bombs monthly / coffee monthly / pet supplies box), (2) FTC «Made in USA» Rule 2021 final («all or virtually all» domestic + civil penalty до $50k/violation за misuse «Made in USA» / «Designed in USA» / «Assembled in USA»), (3) state Automatic Renewal Laws matrix (CA Civil Code §17602 + NY GBL §527-a annual notice + OR §646A.295 + VT 9 VSA §2454a), (4) FTC Mail Order Rule 16 CFR §435 (30-day shipment default + refund disclosure clear-and-conspicuous pre-purchase), (5) TikTok Shop / Instagram Shopping FTC §5 direct-purchase ads regulation + FTC §255 + §255.5 UGC creator / affiliate compensation disclosure + 2023 update AI-synthetic endorser, (6) supplement-adjacent escalation guardrail (если product = vitamin / weight-loss / muscle-builder / sleep — pre-flight escalation на WELLNESS_HEALTH_RESTRICTED_USA_PRESET). Этот пресет — единая точка истины для US-DTC impulse e-commerce.

**КОГДА АКТИВИРУЕТСЯ ECOM_IMPULSE_USA_PRESET:**

Профиль клиента = ECOM_IMPULSE / ECOM_PROSTOY с US-гео триггером, и любой из триггеров:
— Геотаргетинг US (даже частично — US + CA mix трактуется по US-rules как stricter; CA-only попадает под CA ARL + Prop 65 layer).
— Категория = physical consumable / accessory / gadget AOV $15-100, single purchase или recurring DTC subscription.
— Sub-vertical = bath bombs / soap / candles / home fragrance.
— Sub-vertical = coffee / tea / specialty food subscription.
— Sub-vertical = pet supplies / pet food / treat box.
— Sub-vertical = phone accessories / charging cables / cases / pop-sockets.
— Sub-vertical = kitchen gadgets / silicone tools / small appliances <$100.
— Sub-vertical = small fitness equipment (resistance bands / yoga mat / mini massage gun <$100).
— Hook / Dialogue / EXACT STRING / overlay содержит «50% off» / «from $X» / «free shipping» / «Made in USA» / «Designed in California» / «hand-poured small batch» / «risk-free trial» / «cancel anytime» / «#1 best-seller».
— Pricing model = one-time + subscription option / auto-renew / «cancel anytime» / monthly box / quarterly box (FTC ROSCA + Negative Option Rule + state ARL trigger).
— Платформа кампании = Meta / TikTok / Instagram / TikTok Shop / Instagram Shopping с US-targeting (FTC §255 + Section 230 + state UDAP jurisdiction).
— UGC creator / influencer endorsement в кадре (FTC §255 + §255.5 + 2023 update AI-synthetic disclosure trigger).
— Affiliate-driven creо (affiliate link в bio / promo code в caption — Material Connection trigger).
— Профиль клиента содержит флаг `vertical=ecom_impulse_us|ecom_subscription_box|ecom_dtc_consumable|ecom_tiktokshop|ecom_instashop`.

Если хотя бы один триггер — все 9 правил ниже **обязательны**. EU/UK ECOM (GDPR consent + UK CMA Digital Markets Act subscription) НЕ покрывается — для EU/UK flight'ов отдельный preset (волна Т.10+).

GUARDRAIL АВТО-ЭСКАЛАЦИИ: Если product = supplement / vitamin / weight-loss / muscle-builder / sleep aid / nootropic / hormonal / ED — **этот preset НЕ применяется**, автоматический switch на **WELLNESS_HEALTH_RESTRICTED_USA_PRESET** (9 правил, DSHEA + FDA + FTC §255 + Click-to-Cancel). См. ПРАВИЛО 8 ниже для disambiguation.

**ПРАВИЛО 1 — Workspace + модель + packs (дефолт жёсткий, не предложение):**
— Workspace = **Marketing Studio + Higgsfield Audio** (НЕ Cinema Studio — overproduced cinematic для $15-100 impulse читается «pharma-grade TV ad» / «luxury watch ad» и ломает price-perception; conversion падает + FTC scrutiny растёт потому что creо выглядит как high-stakes claim). Cinema Studio допустим **только** для outro brand frame founder-reveal (Soul ID опциональный по строке 2799 — 3-5s).
— Модель = **Kling 3.0 (default)** для product macro + UGC talking-head + hand-in-frame product reveal. **Seedance 2.0** = fallback для smooth lifestyle motion (применение продукта — bath bomb dissolving в воде, кофе наливается, pet eating). Veo 3.1 — только для outro brand frame Soul ID.
— Packs = **PRODUCT MACRO** (close-up texture / packaging / label детали) + **HANDS IN FRAME** (применение, разворачивание, scooping) + **LIFESTYLE pack** (kitchen / bathroom / desk / pet corner — НЕ studio whiteroom, НЕ professional set-design) + **ANTI-AI-LOOK** (без AI-perfect surface, micro-imperfection в packaging / texture) + **PORTRAIT CU** (если UGC creator в кадре).
— Label / packaging / supplement-facts / pricing UI в кадре = ВСЕГДА через **§19A UI MOCKUP PIPELINE** или **§19B INFOGRAPHIC-CHART**, не напрямую в Kling (label-text иначе рендерится с галлюцинациями глифов, FTC label compliance ломается, особенно «Made in USA» / «Net Wt» / «Best By» / supplement-facts panel).
— Format = **9:16 + 6-9s** (Meta Reels / TikTok / IG Reels primary — где сидит impulse buyer) / **1:1 + 6s** (Instagram feed retargeting) / **4:5 + 8s** (Meta in-feed scroll-stop). 16:9 НЕ default — YouTube для $15-100 impulse редко converts.

**ПРАВИЛО 2 — Product representation accuracy (FTC §5 deception — actual product vs creо):**

Любое визуальное представление продукта в крео = создаёт material impression actual product condition. FTC §5 deception trigger если creо product отличается от shipped product (color / size / packaging / contents / texture / functionality).

Триггеры обязательного disclosure / accuracy:
— **Product color enhancement** (saturation boost, brand-color shift) → если actual product менее vibrant → overlay «Color may vary from screen» либо color-correct в крео к actual SKU.
— **Product size misrepresentation** (forced perspective, hand-scale exaggeration — phone accessory выглядит крупнее чем actual) → размер reference (рука, монета US quarter) обязателен в одном кадре, либо overlay «Actual size: {dimensions}».
— **AI-generated product imagery** (полностью synthetic product без physical sample) → overlay «Conceptual rendering — actual product may vary» (bottom-third, present 0-end, FTC «clear and conspicuous»).
— **Composite shot** (один product в нескольких сценах через AI compositing — pet eating в кухне, спальне, gym) → если pet или environment AI-generated → AI disclosure overlay.
— **Functionality demo** (kitchen gadget «slices in 3 seconds», massage gun «1 hour battery») → substantiation per ПРАВИЛО 3 (substantiated claim) + on-frame qualifier если выходит за typical user experience.
— **«Glowing magical product»** треатмент (особенно для bath bombs / candles / cosmetics с supernatural glow) — hard-block. Replace: realistic product-in-action.

PASS overlay-формат для AI-rendered product: bottom-third, present 0-end, Inter Regular 12-14pt, white-90% на gradient-darken, ≤90 chars/line. ТЕКСТ ОБЯЗАТЕЛЕН в самом кадре (не в caption / description Meta поста).

FAIL пример: AI-generated «glowing bath bomb explosion с rainbow fizz» без overlay, actual product = standard pink bath bomb стандартного fizz → «materially misleading impression» FTC §5.

PASS пример: Real product через image-to-video Kling, hand reaches in, bath bomb drops into water, realistic fizz + color release; overlay «Color and effect may vary per batch» (present 0-end).

**ПРАВИЛО 3 — Pricing / discount / from-pricing / «#1 best-seller» substantiation:**

Любая pricing / discount / ranking claim = подпадает под FTC §5 deception + state UDAP («unfair or deceptive acts or practices» — каждый штат свой statute) + FTC «Made in USA» Rule (если origin claim).

Запреты в крео:
— **«50% off» pattern** без anchor reference price = FTC «former price» rule + state UDAP. Replace: «Originally $40 · today $20 (50% off)» с typical-price prominence equal или больше discount price. Anchor price должен быть **bona fide regular price** проданный по этой цене recently (not inflated «MSRP» fiction).
— **«From $15» pattern** без typical-price prominence = FTC «from-pricing» qualification rule. Replace: «Starter $15 · most popular $35 · best value $55» с typical-price prominence equal.
— **«#1 best-seller» / «America's favorite» / «top-rated»** = substantiation required. PASS sources: Amazon Best Seller Rank screenshot с datestamp + category + sub-category specified; Shopify category rank; published industry ranking. FAIL: self-attested «our customers say».
— **«5-star reviews» / «4.9 rating»** = substantiation required + sample size disclosure («Based on 1,247 verified reviews» — caption или on-frame, не bottom overlay font 6pt).
— **«Limited time offer» / «only X left»** = artificial scarcity — FTC §5 + state UDAP «dark pattern» enforcement (CA AB-211 + new FTC Click-to-Cancel rule extends to scarcity dark patterns). Replace: real-stock-based countdown OR remove urgency framing.
— **«Free shipping»** — если conditional (orders >$X) — condition overlay обязательна. Если international shipping excluded — «Free shipping within US contiguous 48 states» qualifier.
— **«Buy one get one free» (BOGO)** — actual price of paired SKU must not be inflated to absorb free unit — FTC enforcement precedent.

PASS пример: `EXACT STRING: "Bath bomb 6-pack · regular $36 · summer sale $24 (save $12) · free US shipping over $35"` (anchor price prominent, savings explicit, shipping condition clear).

FAIL пример: `EXACT STRING: "50% OFF · only 3 left · #1 best-seller · free shipping!"` → 4 unsubstantiated claims (no anchor + artificial scarcity + ranking без source + shipping без condition).

**ПРАВИЛО 4 — Subscription / auto-renew compliance (FTC Negative Option + ROSCA + Click-to-Cancel + state ARL matrix):**

DTC subscription / monthly box / «cancel anytime» = триггер четырёх federal + state laws одновременно.

**Federal layer:**
— **FTC «Negative Option Marketing Rule»** (effective 2024/2025) — covers pre-paid auto-renew DTC subscription boxes. Overlaps но БОЛЕЕ ШИРОКИЙ чем Click-to-Cancel.
— **FTC ROSCA (Restore Online Shoppers' Confidence Act) 15 USC §8401-8405** — express informed consent для recurring billing; ban negative-option «trial-to-paid» без clear disclosure; clear-and-conspicuous material terms.
— **FTC Click-to-Cancel 16 CFR §425** — cancellation должна быть в том же канале и количестве кликов как enrollment.
— **FTC Mail Order Rule 16 CFR §435** — 30-day shipment default (если не указан другой timeframe) + refund / cancellation rights.

**State ARL layer (наслаивается на federal):**
— **CA Civil Code §17602** — clear-and-conspicuous auto-renew disclosure pre-enrollment + acknowledge confirmation + cancel mechanism online (если sign-up онлайн). Private right of action + restitution.
— **NY GBL §527-a** — annual notice ≥15 days до renewal для contracts ≥1 year; clear cancellation instructions; AG enforcement + civil penalty.
— **OR §646A.295** — auto-renewal disclosure + cancel mechanism + annual notice.
— **VT 9 VSA §2454a** — automatic renewal restrictions, similar to CA / NY.
— **Дополнительно**: IL, NC, DC, HI, FL имеют related disclosure rules — для multi-state кампании default = соблюдай CA + NY (самые strict, покрывают остальные).

Требования в крео (overlay + landing) если subscription модель присутствует:
— **«Subscribe & save 15%» CTA**: link на лендинг с clear-and-conspicuous (above-the-fold) disclosure: frequency (monthly / quarterly), amount per shipment ($X), how-to-cancel (1-click online), free-trial-to-paid transition если applicable.
— **«Risk-free 30-day trial»** в крео — overlay в кадре или caption: «After 30 days, $X/month subscription continues. Cancel anytime online via [link] before day 30 to avoid charge.» Без этого — Click-to-Cancel + ROSCA + state ARL violation одновременно.
— **Express informed consent** — affirmative click на «I understand subscription will auto-renew at $X/{frequency}» отдельно от primary CTA. НЕТ pre-checked boxes (CA §17602 + ROSCA hard-block).
— **Annual reminder** для ≥12 month subscriptions — за ≥30 days до renewal (CA, NY GBL §527-a strict — 15 days minimum).
— **Cancel mechanism в кадре**: если creо advertises «cancel anytime» — текстовый qualifier «Cancel online in 1 click at [domain.com/account]» обязателен (демонстрация actual cancel-button screenshot — bonus, не required).

FAIL pattern в крео: «First box FREE — try risk-free!» без auto-charge disclosure → FTC ROSCA + Negative Option + CA §17602 + NY GBL violation (4 laws simultaneously). Civil penalty + restitution + class action precedent (multiple FTC consent decrees 2023-2025 — Vonage $100M, Adobe pending, Amazon Prime $134M settlement пендинг).

PASS pattern: «First box $9.95 (regular $34.95) — monthly subscription auto-renews at $34.95/month. Cancel anytime online in 1 click at brand.com/account. Annual reminder sent 30 days before each renewal.»

**ПРАВИЛО 5 — Returns / refunds / shipping policy (FTC Mail Order Rule + state cooling-off + clear-and-conspicuous):**

FTC Mail Order Rule 16 CFR §435 — default 30-day shipment requirement если не указан иной timeframe в creо / order page. Late shipment → buyer right to cancel + full refund.

— **Shipping timeframe в крео**: если promised «ships in 24 hours» / «delivers in 3 days» — actual fulfillment должен соответствовать. FAIL = FTC §5 + state UDAP. Default safe phrasing: «Orders ship within 2-5 business days · Delivery 5-10 business days within US contiguous 48 states».
— **Refund / return policy disclosure pre-purchase**: state UDAP (CA, NY, FL, MA) требуют clear-and-conspicuous refund policy ДО checkout. Creо advertising «satisfaction guaranteed» → return-window timeframe + condition (used / unused / shipping-cost responsibility) обязательны в caption или landing above-fold.
— **«30-day money-back guarantee»** в крео — qualifier: «Return unused product within 30 days for full refund. Original shipping cost non-refundable. Return shipping at buyer cost unless defective.» Без этого — implied unconditional refund = FTC deception.
— **FTC «Cooling-Off Rule» 16 CFR §429** — applies to door-to-door / off-premises sales $25+ (3-day cancellation). НЕ applies to online ecom by default, но если creо advertises «pop-up shop» / «trade show» / «home party» — trigger activates.
— **State cooling-off для subscriptions**: CA §17602 — implied 3-day cooling-off для automatic renewal contracts entered into via internet/phone (interpretation evolving 2024-2025).

PASS пример overlay: «Free 30-day returns · Ships in 2-5 business days · US contiguous 48 states» (bottom-third, present 5s-end после product reveal).

FAIL пример: «100% satisfaction guaranteed!» без timeframe + без condition + без shipping responsibility = FTC §5 deception + state UDAP.

**ПРАВИЛО 6 — Testimonial / UGC creator / influencer compliance (FTC §255 + §255.5 + 2023 AI-synthetic update):**

ECOM_IMPULSE на TikTok / Reels = UGC creator endorsement = dominant формат. FTC §255 + §255.5 + 2023 Endorsement Guides update + FTC §5 материal connection — кумулятивны.

— **Paid UGC creator** (cash, free product worth $X, commission affiliate link, gifted PR box) = material connection → `#ad` / `#sponsored` / «Paid partnership» disclosure clear-and-conspicuous. Disclosure в caption start (visible БЕЗ клика «more») + on-frame первые 3s.
— **TikTok Branded Content toggle ≠ FTC compliance alone** — overlay disclosure ВСЁ РАВНО нужен (TikTok toggle = platform compliance, не FTC §255).
— **Affiliate creator** (promo code в caption / Linktree / bio) = Material Connection → «Affiliate link · I earn commission on purchases» disclosure.
— **Customer testimonial с specific outcome** («I use it every morning, my skin looks 5 years younger») = atypical results если outside typical user experience → on-frame disclaimer + typical results data. Hardly «Gut Check» 7 weight-loss claims — если adjacent к weight-loss / muscle-builder → escalate на WELLNESS_HEALTH_RESTRICTED_USA_PRESET ПРАВИЛО 5 (см. cross-ref).
— **AI-generated UGC creator / synthetic endorser (FTC 2023 Endorsement Guides update)** — AI-fabricated «testimonial» от persona, которая не существует / не использовала продукт = deceptive practice. Required disclosure: «AI-generated character — not real customer testimonial» overlay (present 0-end, bottom-third).
— **AI-likeness real UGC creator** (creator подписал release на AI-recreation) — material connection + AI disclosure both required.
— **Review screenshots в кадре** (Amazon / Shopify reviews shown) — review должен быть real verifiable + sample size («Based on 1,247 reviews on Amazon US — see product page») + no cherry-picking (cannot show only 5-star если distribution mixed).
— **Before/after** для non-supplement физического продукта (kitchen organization, pet grooming, phone accessory aesthetic) — обычно OK if non-medical claim. НО: если adjacent к body transformation / weight-loss / muscle → hard-block + escalate на WELLNESS_HEALTH_RESTRICTED_USA_PRESET.

PASS пример: UGC creator opening box, talking-head, overlay first-3s: «#ad · gifted by @brand · my honest review»; caption start: «#ad / paid partnership with @brand».

FAIL пример: UGC creator demos product без disclosure, caption: «You guys NEED this! Link in bio for discount» → 2 нарушения (paid endorsement без disclosure + affiliate без material connection).

**ПРАВИЛО 7 — «Made in USA» / origin claims (FTC «Made in USA» Rule 2021 final + civil penalty $50k/violation):**

FTC «Made in USA» Labeling Rule (effective August 2021) — first time FTC has civil penalty authority for false «Made in USA» claims. Civil penalty up to **$50,120 per violation** (adjusted 2024).

«Made in USA» standard = «all or virtually all» made in USA:
— **All significant parts and processing must be of US origin.**
— **Final assembly OR processing in US.**
— **De minimis foreign content allowed** только если negligible AND clearly disclosed.

Запреты в крео:
— **«Made in USA» / «Made in America» / «Proudly American» / «100% American»** без full «all or virtually all» compliance → hard-block. FTC civil penalty.
— **US flag в кадре + product** без origin substantiation — implied «Made in USA» claim → triggers same standard.
— **«American-owned» / «Family business in USA»** — separate claim от «Made in USA» — ownership ≠ origin. PASS если truthful, но **не interchangeable** с origin.

PASS variations:
— **«Designed in California · Assembled in USA · components sourced globally»** — qualified origin claim. Acceptable если truthful.
— **«Made in USA from imported components»** — acceptable qualifier (specific to bath bombs / cosmetics — imported essential oils / ingredients).
— **«Made in USA from domestic and imported parts»** — qualifier acceptable for textiles / accessories.
— **«Hand-poured in {state}»** — local-craft signal, не triggers «Made in USA» standard if не explicit «Made in USA».

Substantiation: bill of materials (BOM) audit + supplier certificates + final assembly location verification. Flag в intake: `made_in_usa_substantiation: BOM_audit_complete | partial | none`. Если none → block «Made in USA» claim, use «Designed in {state}» / «Assembled in {state}» qualifier с component disclosure.

FAIL пример: `EXACT STRING: "Bath bombs handmade in California · 100% American" · US flag overlay` — если essential oils imported, fragrances imported, packaging from China → «all or virtually all» fails → $50k+ civil penalty.

PASS пример: `EXACT STRING: "Hand-poured in California · made with domestic and imported ingredients · small batch family business"`.

**ПРАВИЛО 8 — Category-specific guardrails (TikTok Shop / Instagram Shopping + affiliate + supplement-adjacent escalation):**

**TikTok Shop / Instagram Shopping direct-purchase ads (FTC §5 + Section 230 evolving):**
— Direct-purchase в-приложении (TikTok Shop video tag / Instagram Shopping tag) = ad + checkout = full retailer responsibility. Все правила выше (substantiation / refunds / origin / subscription) применяются + дополнительные platform-specific terms.
— **TikTok Shop Seller Center compliance** — product listing accuracy, restricted-product category check (supplements / weight-loss / CBD / sexual wellness — restricted/banned), price-matching with brand site.
— **Instagram Shopping FTC §5** — checkout-out experience должен match price + shipping в creо.

**Affiliate-driven creо (Amazon Associates / ShareASale / Impact / brand-direct):**
— Affiliate disclosure required в caption + overlay (FTC §255.5 material connection).
— Amazon Associates policy — «As an Amazon Associate I earn from qualifying purchases» обязательно в любом контенте с Amazon link.
— Promo code distribution в bio / caption — Material Connection regardless of commission rate.

**Supplement-adjacent escalation (HARD GUARDRAIL):**
— Если product содержит **vitamin / mineral / botanical / amino acid / herbal supplement / protein powder / pre-workout / nootropic / sleep aid / weight management** → **ECOM_IMPULSE_USA_PRESET НЕ применяется, switch на WELLNESS_HEALTH_RESTRICTED_USA_PRESET** (9 правил, DSHEA §403r-6 + FDA disclaimer + FTC «Gut Check» + state Prop 65 / NY AG / TX DTPA).
— Disambiguation: bath bomb с lavender essential oil = ECOM_IMPULSE (cosmetic, не ingestible, no health claim → OK). Bath bomb advertised «helps with sleep / muscle recovery» = implied health claim → WELLNESS escalation.
— Coffee subscription = ECOM_IMPULSE (food, no health claim). «Nootropic coffee blend» / «adaptogenic coffee» с health claim → WELLNESS escalation.
— Pet supplies = ECOM_IMPULSE. «CBD pet treats» / «joint supplement for dogs» = veterinary regulatory + FDA Center for Veterinary Medicine → escalation на separate pre-flight (no preset yet, T.10+).
— Kitchen gadget = ECOM_IMPULSE. «Detox blender» / «alkaline water bottle» с health claim → WELLNESS escalation.

**OTC pharma-adjacent (отдельный layer):**
— Если product = OTC drug / homeopathic remedy / topical analgesic с drug-claim (Bengay, Aspercreme, sunscreen с SPF claim) → FDA monograph compliance + Online Pharmacy Act check → escalate на pre-launch FDA compliance review (no preset yet).

**Cross-state campaign targeting:**
— Default split по placement-set: CA-only с Prop 65 overlay (если applicable ingredients) + ARL §17602 disclosure; NY-only с GBL §527-a annual notice language; remaining-US с federal-only stack.

GUARDRAIL: если product НЕ third-party-tested и не имеет US-based fulfillment center (dropshipping from China direct) — escalate на pre-launch compliance review независимо от state (FTC «origin» + customs declarations + Mail Order Rule 30-day risk).

**ПРАВИЛО 9 — AI-product imagery + Soul ID outro brand frame (FTC §5 для AI-product + Soul ID опционально outro):**

**AI-generated product imagery (повторяется в ПРАВИЛО 2, но здесь специфика для full-AI-rendered creо):**
— Если creо полностью AI-generated без physical product photo (image-to-video без real SKU image as seed) → overlay «Conceptual rendering — actual product may vary» mandatory.
— **Color accuracy** — AI tends to over-saturate; для cosmetic / candle / bath bomb / textile — обязателен реальный SKU как reference seed либо overlay color-vary disclaimer.
— **Packaging accuracy** — AI tends to «remix» logo / label / typography. Logo / label = ВСЕГДА через §19A UI MOCKUP PIPELINE с brand asset, не AI-generated freehand.
— **Material rendering** — AI rendering для glass / metal / fabric может «hallucinate» material properties. Для high-end packaging accuracy critical → physical photo + image-to-video preferred.

**Soul ID outro brand frame (опционально, по строке 2799):**
— Soul ID для ECOM_IMPULSE = НЕ дефолт для product-showcase. Применяется ТОЛЬКО в outro brand frame: founder reveal 3-5s в конце крео (1 крео из пачки 4-6).
— Use case: handmade / craft / artisan / family-business positioning (bath bombs «founded by sisters in Vermont», coffee «small-batch roaster in Portland»). Founder в кадре = trust-якорь, оправдан только в outro.
— Format: 8-10 фото single-shot static portrait для outro frame (по нижней границе single-shot static portrait). Multi-shot wardrobe для founder НЕ нужен — outro один кадр.
— Если Soul ID = real identifiable founder (firm website / LinkedIn / brand About page) → AI DISCLOSURE pack обязателен: overlay «AI-assisted visual · {Founder Name}, Founder» (bottom-third, present in outro frame, ≤90 chars, Inter Regular 12pt, white-90%).
— Если Soul ID = generic ad-actor / stock-likeness (не identifiable real person) — «Actor portrayal» overlay рекомендован для transparency, не mandatory.

FAIL пример: AI-rendered glowing bath bomb + AI-generated «founder» с подписью «Sarah, our founder» (когда real founder совсем другая person) → FTC §5 false endorsement + state right-of-publicity.

PASS пример: Real product image-to-video + outro frame с real founder photo + overlay «AI-assisted visual · Sarah Chen, Co-Founder · brand.com».

**ECOM_IMPULSE_USA_PRESET — финальный чек-лист (9 проверок перед выдачей промта):**

| # | Проверка | PASS если | FAIL → |
|---|---|---|---|
| 1 | Marketing Studio + Kling 3.0 / Seedance 2.0 + PRODUCT MACRO + HANDS IN FRAME + LIFESTYLE + ANTI-AI-LOOK + PORTRAIT CU (если UGC) packs; label / pricing через §19A UI MOCKUP PIPELINE; format 9:16 + 6-9s (Cinema Studio только outro brand frame) | Да | Переключить workspace на MS, подключить недостающие packs, route label через pipeline |
| 2 | Product representation accuracy: реальный product через image-to-video или AI-rendered с overlay «Conceptual rendering — actual product may vary»; нет «glowing magical product» если actual продукт обычный; нет size misrepresentation без scale reference; functionality claim substantiated | Да | Заменить на real product image-to-video, добавить overlay для AI-rendering, добавить scale reference, удалить magic-glow treatment |
| 3 | Pricing / discount: «50% off» с anchor reference price prominent; «from $X» с typical-price prominence equal; «#1 best-seller» с source (Amazon BSR + date + category); rating с sample size; «free shipping» с condition; нет artificial scarcity dark pattern | Да | Добавить anchor price, добавить typical-price prominence, запросить ranking source, добавить sample size, добавить shipping condition, убрать «only X left» если не real-stock |
| 4 | Subscription / auto-renew compliance (если applicable): FTC ROSCA express informed consent + FTC Negative Option + Click-to-Cancel 16 CFR §425 + CA §17602 + NY GBL §527-a annual notice; «risk-free trial» с auto-charge disclosure; cancel mechanism online в same channel as enrollment; no pre-checked boxes | Да | Переписать «risk-free» с auto-charge disclosure, добавить affirmative consent click, разделить cancel-mechanism сетап, добавить annual reminder spec |
| 5 | Returns / refunds / shipping disclosure: FTC Mail Order Rule 30-day shipment либо stated timeframe; refund window + condition + shipping-cost responsibility clear-and-conspicuous pre-purchase; «satisfaction guaranteed» с qualifier; cooling-off rule check если off-premises | Да | Добавить shipping timeframe, добавить refund window + condition, добавить shipping responsibility, удалить implied unconditional guarantee |
| 6 | Testimonial / UGC / influencer compliance: paid UGC = #ad / Paid partnership disclosure caption start + on-frame 3s; affiliate = material connection disclosure; TikTok Branded Content toggle + on-frame overlay (toggle alone insufficient); AI-synthetic endorser = «AI-generated character» disclosure; before/after escalation если adjacent body-transformation | Да | Добавить #ad disclosure, добавить affiliate disclosure, добавить on-frame overlay поверх TikTok toggle, добавить AI-synthetic disclosure, escalate на WELLNESS_USA если body-transformation |
| 7 | «Made in USA» / origin claims: «all or virtually all» substantiation through BOM audit + supplier certificates + final assembly verification; qualified claims («Designed in CA · Assembled in USA · components sourced globally») допустимы; US flag без origin substantiation = implied claim = same standard; civil penalty $50k/violation acknowledged | Да | Удалить unqualified «Made in USA» claim, заменить на qualified origin disclosure, удалить US flag без substantiation, запросить BOM audit |
| 8 | Category guardrails: TikTok Shop / Instagram Shopping price-match + restricted-category check; affiliate disclosure (Amazon Associates language если applicable); supplement-adjacent → ESCALATE на WELLNESS_HEALTH_RESTRICTED_USA_PRESET; OTC pharma-adjacent → escalate на FDA pre-launch review; cross-state placement-set rotation для Prop 65 / ARL | Да | Switch на WELLNESS_USA_PRESET если ingestible с health claim; добавить Amazon Associates disclosure; разделить placement-set для CA + NY; escalate OTC pharma |
| 9 | AI-product imagery accuracy + Soul ID outro (опционально): full-AI creо = «Conceptual rendering — actual product may vary» overlay; logo / label через §19A UI MOCKUP; Soul ID outro frame только 1 крео из пачки + AI DISCLOSURE pack если identifiable founder; «Actor portrayal» если generic likeness | Да | Добавить AI rendering disclaimer, route logo через UI MOCKUP, добавить AI DISCLOSURE overlay для founder outro, переключить на «Actor portrayal» если generic |

9/9 PASS → промт выпускается ученику.
≤8/9 PASS → return to editor, не выпускается. Конкретные FAIL-причины перечисляются в return-note.

**ECOM_IMPULSE_USA — 3-STEP FUNNEL GRANULARITY:**

| Step | Цель | Арка | CTA | Регуляторный риск |
|------|------|------|-----|---|
| TOF | Awareness — product discovery / category education / lifestyle integration | D (product в действии — Shot 1 product reveal macro → Shot 2 lifestyle use → Shot 3 brand frame); UGC creator first-impression без price/discount; «meet our product» tone | «Learn more» / «See how it works» / «Browse collection» (без direct-purchase) | Низкий (no pricing / no substantiation claims — FTC scrutiny minimal) |
| MOF | Nurture — social proof + ingredient story + quality differentiator (third-party testing / sourcing / craft story) | C (UGC creator with disclosure) или D (product macro + sourcing story); founder reveal в outro если applicable; review aggregation overlay с sample size | «Read reviews» / «See our story» / «Join the email list» (15% off first order opt-in OK) | Средний (substantiation для reviews / origin claims начинается — Правила 2, 3, 7 обязательны) |
| BOF | Close — direct-purchase + subscription offer + scarcity (real-stock-based only) | D или E (каталог 3 SKU вариантов с price-tier) + UGC testimonial с full disclosure stack | «Shop now» / «Subscribe & save 15%» / «Add to cart» / TikTok Shop / IG Shopping checkout | Высокий (все 9 правил applicable + subscription compliance + state ARL + TikTok Shop platform terms + UGC §255 disclosure) |

GUARDRAIL: BOF cold open feed для subscription model = автоматический pre-launch compliance review (FTC ROSCA + Negative Option + state ARL — top FTC priority enforcement 2024-2026). Default — soft TOF/MOF в cold с email-capture, BOF subscription только в retargeting warm-audience с prior brand exposure + clear cancel mechanism disclosure.

CROSS-REFERENCES (не дублировать в этом пресете, использовать ссылками):
— **Существующая ECOM_IMPULSE база** — арка D «продукт в действии» (строка 2229 / 2244); Soul ID опционален outro brand frame (строка 2799); CTA-matrix (строка 2756).
— **WELLNESS_HEALTH_RESTRICTED_USA_PRESET** — supplement-adjacent escalation (ПРАВИЛО 8 hard guardrail). Если product = vitamin / botanical / weight-loss / muscle / sleep / nootropic — НЕ применять этот preset, switch на WELLNESS preset (9 правил, DSHEA + FDA disclaimer + FTC «Gut Check» + state Prop 65 / NY AG / TX DTPA).
— **REAL_ESTATE_EXPAT_USA_PRESET** — pattern reuse для (а) AI DISCLOSURE pack overlay format (real founder Soul ID outro = same template как broker AI DISCLOSURE), (б) substantiation pattern для «#1 best-seller» (same third-party source standard как broker «Top 1%» substantiation через RealTrends), (в) FTC §5 deception standard для product representation (same как AI-staging disclosure).
— **§19A UI MOCKUP PIPELINE + §19B INFOGRAPHIC-CHART** — для label / pricing UI / supplement-facts / review screenshots в кадре.
— **§11 Soul ID guardrails** + **§15 NEVER #23 meta-policy блокер** + **§21 EXECUTIVE-CALIBRATED HUMANIZATION** (если founder Soul ID senior).
— **V17 (Жертва hook check)** + **V18 (substantiation)** — universal guards, применимы поверх preset.
— **EU_RUSSIAN_DIASPORA_PRESET** — НЕ применяется для US-only ECOM_IMPULSE, но pattern AI DISCLOSURE pack overlap.

═══════════════════════════════════════════════════

# LOCAL_SERVICE_LOCAL_SEO_GBP_LAYER — extension правил поверх LOCAL_SERVICE (волна Т.12 после Т.12-А создателя)

**Тип:** extension layer (НЕ канонический PRESET, 7 правил поверх базовых LOCAL_SERVICE)
**Применяется поверх:** LOCAL_SERVICE PRESET (стома / бьюти / барбер / ремонт / фитнес-студии / HVAC / сантехника)
**Версия:** Т.12-А draft 2026-05-19
**Risk after fixes:** target 4/10 (наследует от LOCAL_SERVICE базы)

---

## КОНТЕКСТ И ОБЛАСТЬ ПРИМЕНЕНИЯ

Этот layer покрывает специфику Local SEO и Google Business Profile (далее GBP) для бизнесов LOCAL_SERVICE профиля. Базовые правила LOCAL_SERVICE (лицензирование, before/after для бьюти/стома, медицинские claims, ценовое substantiation) остаются обязательными. Этот слой добавляет ИМЕННО онлайн-репутацию, GBP-листинг и Local Service Ads.

Триггеры подгрузки layer:
- крео упоминает «5-star reviews» / «top-rated on Google»
- крео показывает Google rating в кадре
- бизнес запускает Local Service Ads (LSA) с Google Guaranteed / Google Screened badge
- крео использует customer testimonial (видео/фото клиента)
- крео упоминает «serving X city» / radius targeting
- крео использует AI-generated photos для GBP / landing page

---

## ПРАВИЛО 1 — GBP photo / video / post compliance

**Что проверяем:** соответствие фото / видео / постов в GBP политике Google «Owner-uploaded content».

**Стандарт PASS:**
- Owner-uploaded фото = actual business / actual products / actual staff (не stock, не чужой Pinterest)
- Видео ≤30 сек, ≤100 MB, ≤1080p (текущие лимиты Google 2026)
- 360° tour — только через Google Trusted Photographer (сертификация подтверждена)
- AI-generated фото OK, ЕСЛИ представляет actual business (например AI-апскейл реального снимка / удаление мусора с реального фото)
- GBP posts (offers / events / updates) — character limit 1500 + media + CTA с реальной ссылкой на бизнес

**FAIL:**
- AI-сгенерированный «стоковый» интерьер салона который реально не существует
- Фото клиента без письменного согласия (см. ПРАВИЛО 6)
- Видео >100 MB или >30 сек (отклонится Google)
- Owner отвечает на свои же отзывы под другим аккаунтом (см. ПРАВИЛО 2)

**Пример FAIL:** dental clinic в Алматы загружает в GBP AI-сгенерированный «стоматологический кабинет с белой мебелью» — пациент приходит и видит совсем другой интерьер → Google policy violation + потенциальный consumer deception claim.

**Пример PASS:** barber shop загружает реальные фото мастеров + видео-обзор салона 25 сек снятый на iPhone + offer post «10% off first haircut» с ссылкой на booking.

---

## ПРАВИЛО 2 — Fake reviews enforcement (FTC NOPO 2023 + FTC Final Rule 2024 + state laws)

**База:** **FTC «Notice of Penalty Offenses Concerning Deceptive Endorsements» 2023** ($50,000 per violation для bad-faith деяний) + **FTC «Rule on the Use of Consumer Reviews and Testimonials» (Final Rule вступил в силу октябрь 2024)** — broader, чем NOPO, покрывает почти все формы fake-review manipulation.

**Что прямо запрещено:**
- покупка / соliciting fake reviews (плата за положительный отзыв без disclosure)
- AI-сгенерированные отзывы выдаваемые за человеческие
- insider reviews — отзывы от сотрудников / семьи / владельца без раскрытия связи
- suppression негативных отзывов (review gating — show 5★ публично, 1-3★ отправь только в личку)
- review hijacking — перенос отзывов с одного товара/услуги на другой
- threats / intimidation против reviewers за негативный отзыв

**State laws (US):**
- **CA SB 567 (2024)** — запрет false / misleading reviews + право AG штрафовать
- **NY GBL §349** — deceptive business practices (применяется к fake reviews)
- **TX DTPA** — Deceptive Trade Practices Act, civil penalties

**Google platform policy:**
- запрет review gating (нельзя screening positive vs negative pre-publication)
- «Verified Visit» badge присваивается Google автоматически на основе location signal — нельзя имитировать
- responses владельца разрешены, но не от лица клиента

**FAIL:**
- HVAC contractor предлагает $20 скидку «за 5-star Google review» без disclosure «paid review» — FTC §255.5 + Final Rule violation
- fitness studio просит сотрудников оставить отзывы под личными аккаунтами без disclosure — insider reviews FAIL
- plumber удаляет негативный отзыв через подачу fake DMCA / лживый flag — FTC Final Rule (suppression)
- крео клиента показывает «100+ five-star reviews on Google» когда их 42 — substantiation FAIL

**PASS:**
- «Leave us an honest review on Google» (без условий о звёздности) — OK
- ответ владельца на негативный отзыв с извинением + предложением resolve — OK и желательно

---

## ПРАВИЛО 3 — Reputation management в крео (звёзды / sample size / atypicality)

**Что проверяем:** показ Google rating и review counts в рекламном крео.

**Стандарт PASS:**
- Star rating в кадре fetched ≤30 дней назад и match текущий live GBP rating (screenshot с датой как substantiation)
- Sample size disclosure если ≤50 отзывов: «4.9★ based on 38 Google reviews»
- Atypicality disclaimer если testimonial показывает результат: «Individual results vary» (см. также ПРАВИЛО 6 + KIDS_PARENTS FTC §255.5 layer)
- Cherry-picking — допустим показ конкретного отзыва, НО общий rating не должен противоречить (показал 5★ отзыв при общем 3.2★ — misleading)

**FAIL:**
- крео показывает «4.9★ on Google» при текущем 4.1★ (rating вырос на скриншоте 2 года назад, но упал)
- «hundreds of five-star reviews» при 28 отзывах — substantiation FAIL
- скриншот positive отзывов без линка на источник = unverifiable

**Пример:** stoma-клиника в Tashkent делает Meta-крео со скриншотом Google rating «4.8★ — 156 reviews». На момент запуска rating уже 4.6★ — рекламу надо перерендерить. Решение: брать скриншот в день запуска кампании + refresh каждые 30 дней.

---

## ПРАВИЛО 4 — Local Service Ads (LSA) Google Guaranteed / Google Screened

**Что проверяем:** соответствие требованиям LSA для бизнесов с badge «Google Guaranteed» (home services) или «Google Screened» (professional services — lawyer / financial planner / real estate).

**Стандарт PASS:**
- **Google Guaranteed** (plumbing / HVAC / locksmith / electrician / cleaning / appliance repair / garage door / pest control / roofing / lawn care):
  - business-level background check passed
  - state-required licensing подтверждено (substantiation хранится 3 года)
  - general liability insurance verified ($) — лимит зависит от категории
  - workers comp если есть сотрудники
- **Google Screened** (lawyer / financial planner / real estate agent / tax specialist):
  - professional licensing verified (bar / FINRA / state real estate board / CPA / EA)
  - business owner + customer-facing employees проходят background check
  - state-specific compliance (например для lawyer — bar association in good standing)
- LSA review responses — допустимы от business owner, не должны содержать confidential client info (особенно для lawyer / medical)
- Service category accuracy — если LSA указывает «HVAC repair» а реально делает только installation → category misrepresentation FAIL

**FAIL:**
- крео упоминает «Google Guaranteed» когда badge revoked после insurance lapse
- LSA review response от lawyer раскрывает client case details → bar association ethics violation + LSA policy
- service category «plumbing» использует под маркетинг сантехнических товаров (e-commerce) — это не LSA-eligible

**Lead pricing / dispute:**
- LSA = pay-per-lead, не pay-per-click
- charged leads можно disputить через LSA dashboard (out-of-area / spam / wrong service) — окно 30 дней
- chronic disputes >15% от leads → Google может suspend listing

---

## ПРАВИЛО 5 — Local SEO NAP consistency + schema markup + multi-location

**Что проверяем:** консистентность NAP (Name / Address / Phone) и техническое SEO для local ranking.

**Стандарт PASS:**
- NAP идентичны across: GBP / website / Yelp / TripAdvisor / Yellowpages / Better Business Bureau / industry directories (Healthgrades для медицины, Avvo для lawyer, Houzz для home services)
- Schema.org LocalBusiness markup на website (type accurate — Dentist / BarberShop / HVACBusiness / etc)
- Phone format одинаковый везде (с/без +country code — но единообразно)
- Multi-location chains — отдельный GBP listing per location, отдельная NAP, отдельные отзывы (нельзя сливать ratings локаций в один)
- Service-area business без storefront — указывает service area (radius / cities), НЕ указывает виртуальный адрес как физический storefront (Google policy violation)

**FAIL:**
- сеть из 4 fitness-студий имеет один GBP listing с 4 адресами в описании → suspension
- HVAC contractor «обслуживаю весь Tashkent» использует virtual office address на Regus как storefront → suspension + потеря rankings
- website schema указывает «type: Restaurant» для barber shop (skill issue, но реальный) → confusing для Google

**Пример PASS:** dental network из 3 клиник в Алматы / Астане / Шымкенте имеет 3 отдельных GBP с уникальными NAP, 3 schema-marked страницы локаций на website, NAP идентичны в Yandex.Business / 2GIS / Flamp / Zoon.

---

## ПРАВИЛО 6 — Customer testimonial usage (consent + state laws + AI-generated)

**Что проверяем:** использование клиентских отзывов в крео и на сайте.

**Стандарт PASS:**
- **Written consent** от клиента на использование изображения / видео / голоса в рекламе (model release form подписана)
- **State right of publicity** соблюдён:
  - **California Civil Code §3344** — written consent + commercial use defined
  - **NY Civil Rights Law §50/51** — written consent обязателен для коммерческого использования
  - **TX Property Code §26.001** — descendible right of publicity
  - **TN Personal Rights Protection Act** — strong publicity rights
- **Atypicality disclaimer** если testimonial показывает результат: «Individual results vary. Typical outcome may differ.» (см. также **KIDS_PARENTS FTC §255.5 layer** для reuse)
- **Material connection disclosure** если клиент получил compensation / free service / discount за testimonial — clearly disclosed «Paid testimonial» / «Received free service»
- **AI-generated testimonial = FAIL** по FTC §255 (2023 update + Final Rule 2024) — выдача AI-голоса/лица за реального клиента запрещена даже с disclosure (с октября 2024 — abusive practice per Final Rule)

**FAIL:**
- barber shop использует фото клиента в Meta-крео без model release → CCPA / state right of publicity violation
- weight-loss fitness studio показывает «Lost 30 lbs in 60 days» без atypicality disclaimer → FTC §255.5 violation + medical claim issue (см. LOCAL_SERVICE базовое правило про health claims)
- AI-deepfake video якобы клиента «Я очень доволен» — даже с disclosure не PASS после Final Rule 2024
- влогер получил free dental whitening и снял «обзор» без disclosure «Received free service» → §255.5

**Reuse policy:**
- Atypicality + material connection disclosure механика берётся из **KIDS_PARENTS FTC §255.5 layer** (там детально расписана)
- Эта механика идентична kid-influencer endorsement disclosure, отличие только в субъекте

---

## ПРАВИЛО 7 — Geo-fence / radius / lookalike targeting

**Что проверяем:** настройки гео-таргетинга в Meta Ads / Google Ads для LOCAL_SERVICE.

**Стандарт PASS:**
- Radius targeting в Meta Ads для LOCAL_SERVICE — **РАЗРЕШЁН** (vs blocked для REAL_ESTATE / HOUSING категории по FHA — см. **REAL_ESTATE_EXPAT_USA layer** для disambig)
- Geo-fencing для in-store events / promotions OK
- Lookalike audiences на основе past customers — требуется CCPA-compliant consent (California) / GDPR consent (EU clients) на seed audience upload в Custom Audience
- Custom Audience seed file — hash emails / phones перед upload (Meta делает auto-hash, но best practice)
- Service area radius matches реальной зоне обслуживания (не «весь штат» если реально 15 mi радиус)

**FAIL:**
- LOCAL_SERVICE бизнес помечен как HOUSING / EMPLOYMENT / CREDIT в Meta Ads Special Ad Category → radius locked 15 mi minimum + age 18-65 + no gender targeting (так помечать НЕ нужно, кроме реально mortgage broker / property management)
- HVAC contractor загружает customer email list без CCPA notice → potential class action в Калифорнии
- fitness studio targeting «women 25-40» без проблем для LOCAL_SERVICE (это не HOUSING / EMPLOYMENT / CREDIT)

**Важная disambig:**
- LOCAL_SERVICE = НЕ housing → radius / age / gender targeting свободные
- REAL_ESTATE / property management / mortgage broker / apartment listing → Meta Special Ad Category «Housing» → restrictions (см. REAL_ESTATE_EXPAT_USA FHA layer)
- LOCAL_SERVICE с financial services (financial planner / tax specialist) → может попасть в Special Ad Category «Credit» — отдельная проверка

---

## ФИНАЛЬНЫЙ ЧЕК-ЛИСТ 7/7

- [x] ПРАВИЛО 1 — GBP photo/video/post compliance (owner-uploaded actual; AI OK if represents actual, FAIL if synthetic stock; ≤30s ≤100MB ≤1080p video)
- [x] ПРАВИЛО 2 — Fake reviews (FTC NOPO 2023 $50k/violation + FTC Final Rule 2024 + CA SB 567 / NY GBL §349 / TX DTPA + Google review gating ban)
- [x] ПРАВИЛО 3 — Reputation в крео (rating ≤30 дней + sample size disclosure + atypicality)
- [x] ПРАВИЛО 4 — LSA Google Guaranteed/Screened (background check + insurance + licensing substantiation; service category accuracy; dispute window 30d)
- [x] ПРАВИЛО 5 — NAP consistency + schema.org LocalBusiness + multi-location separate GBP + service-area business без virtual storefront
- [x] ПРАВИЛО 6 — Customer testimonial (written consent + CA §3344 / NY §50/51 / TX §26.001 / TN PRPA + atypicality + AI-generated FAIL по FTC §255 2024 update)
- [x] ПРАВИЛО 7 — Geo-fence / radius (LOCAL_SERVICE OK vs HOUSING blocked; CCPA/GDPR consent для Custom Audience seed)

**Status:** 7/7 PASS — draft готов для T.12-B (создатель) ревью.

---

## ЧТО ПОКРЫЛ

1. GBP-листинг: фото/видео/посты — лимиты + AI-policy
2. Online review enforcement — самый свежий регуляторный слой (FTC Final Rule 2024 = новизна, NOPO 2023 = деньги, state laws = teeth)
3. Звёздные рейтинги в крео — substantiation + freshness ≤30d
4. LSA badges — Google Guaranteed для home services / Google Screened для professionals
5. Local SEO технический слой — NAP + schema + multi-location
6. Customer testimonials — consent + state right of publicity + AI-generated ban
7. Гео-таргетинг — disambig LOCAL_SERVICE vs HOUSING/CREDIT Special Ad Categories

## CROSS-REFERENCES

- **LOCAL_SERVICE базовый PRESET** — лицензирование / before-after / медицинские claims / ценовое substantiation остаются обязательными, этот layer добавляется поверх
- **KIDS_PARENTS FTC §255.5 layer** — переиспользуется механика atypicality disclaimer + material connection disclosure (правило 3 + правило 6)
- **REAL_ESTATE_EXPAT_USA FHA layer** — disambig: для housing radius targeting blocked (Meta Special Ad Category Housing), для LOCAL_SERVICE — OK (правило 7)
- **(будущий) FINANCIAL_SERVICES layer** — если LOCAL_SERVICE бизнес = financial planner / tax specialist → правило 7 переключает на Special Ad Category «Credit» гайдлайны
- **(будущий) MEDICAL_SPA layer** — если LOCAL_SERVICE = aesthetics / med-spa → правило 6 atypicality усиливается медицинским FDA layer

## RISK ASSESSMENT

- Inherits LOCAL_SERVICE base risk = 4/10 после P.13 fixes
- Layer не повышает risk (правила консервативные, FAIL-критерии явные, substantiation механика чёткая)
- Высокий risk зона: ПРАВИЛО 2 (fake reviews) — самое регуляторно active поле 2023-2024, требует regular update по FTC enforcement actions
- Средний risk зона: ПРАВИЛО 6 (AI-generated testimonials) — policy ещё evolves, watch FTC sub-regulations 2026

## ОТКРЫТЫЕ ВОПРОСЫ ДЛЯ Т.12-B

1. Нужна ли отдельная подсекция для не-US юрисдикций (СНГ — Yandex.Business / 2GIS / Flamp consistency + российский ФЗ-38 о рекламе для отзывов)?
2. Где провести границу с MEDICAL_SPA / AESTHETICS будущим layer (стома + бьюти попадают и туда и сюда)?
3. Стоит ли добавить 8-е правило про Apple Business Connect / Apple Maps listing (рост значимости с iOS 17+) или это slim case?
HIGH_TICKET_PRO_SERVICES_PRESET — отдельный пресет (волна Т.6 после Т.6-А создателя + Т.6-B адверсариала 18 GAP + Т.6-C мета-cross-ref 6 юрисдикций)
═══════════════════════════════════════════════════

Контекст: HIGH_TICKET_PRO_SERVICES (M&A advisory / corporate LEGAL / private banking / family-office advisory / wealth advisory) имеет систематически иной риск-профиль, чем HIGH_TICKET premium-coaching и недвижимость. До волны Т.6 секция HIGH_TICKET занимала 7 строк (см. выше), и для M&A / private banking / law-firm кейсов агент терял три критических слоя: (1) profession-specific advertising rules (ABA / SRA / BSB / SEC Marketing Rule 206(4)-1 / FINRA Rule 2210 / FCA COBS / FinSA / Kodeks Etyki Adwokackiej + BRAK BORA + MiFID II + KIID + AIFMD/UCITS), (2) NDA / client confidentiality на уровне жёстче B2B SaaS (даже generic alias «sovereign wealth fund» recognizable в узком рынке 30-50 SWF / 200-300 family offices глобально), (3) substantiation цифр уровня «$2B AUM / $500M closed / 47 transactions» — для этого слоя self-attested LinkedIn bio не годится, нужны third-party verifiable источники (Form ADV / Companies House / Bloomberg / Refinitiv / Mergermarket / Pitchbook / Chambers / Legal 500). Этот пресет — единая точка истины.

**КОГДА АКТИВИРУЕТСЯ HIGH_TICKET_PRO_SERVICES_PRESET:**

Профиль клиента = HIGH_TICKET, и любой из триггеров:
— Деал-сайз 100k-50M+ USD (M&A success-fee, private-banking AUM threshold, retainer + hourly per engagement letter).
— Целевая аудитория = HNWI / UHNWI клиент / корпоративный CEO продающий бизнес / family-office trustee / founder перед exit / GC корпорации / institutional CIO.
— Hook / Dialogue / EXACT STRING содержит claim на AUM («$2B AUM»), closed-deals («$500M closed»), transaction count («47 cross-border M&A»), league-table ranking («top-5 boutique»), win-rate / success-rate в LEGAL.
— Soul ID = senior partner (50+, седина OK, gravitas), Suit mandatory (charcoal / navy / dark grey wool, no business-casual).
— Регуляторный гео-триггер: US (ABA / SEC RIA / FINRA / state bar NY/CA/TX/FL) / UK (SRA / BSB / FCA COBS / s.21 FSMA) / EU (PL Adwokatura NRA + KRRP / DE BRAK BORA / MiFID II / AIFMD / UCITS) / CH (FinSA / FIDLEG / FINMA).
— Профиль клиента содержит флаг `vertical=ma_advisory|legal_firm|private_banking|family_office|wealth_advisory`.
— Dual-credentialing detected (банкир, который тоже licensed attorney; advisor, который тоже broker-dealer registered) — rule-set расширяется автоматически.

Если хотя бы один триггер — все 9 правил ниже **обязательны**. Не «опционально к рассмотрению».

**ПРАВИЛО 1 — Workspace + модель + packs (дефолт жёсткий, не предложение):**
— Workspace = Cinema Studio (НЕ Marketing Studio, executive Soul ID + premium интерьер ломаются в MS).
— Модель = Veo 3.1 (НЕ Kling — у Kling executive face uncanny на CU 50-85mm для 50+ Soul ID, седина рендерится «парик-like»).
— Packs = PORTRAIT CU + LIGHT CONSISTENCY + REFLECTION (wood-panel + brass + leather) + FABRIC (wool suit weave + silk-tie sheen + dress-shirt cotton fibre) + ANTI-AI-LOOK + HAIR (senior executive crop — short, не «flowy AI hair»).
— UI / chart / fee-schedule в кадре = ВСЕГДА через §19B INFOGRAPHIC-CHART / §19A UI MOCKUP PIPELINE, не напрямую в Veo.
— Format = 16:9 + 9-12s (LinkedIn primary — где сидит decision-maker) / 9:16 + 9s (Meta secondary, ретаргет warm-аудитории).

**ПРАВИЛО 2 — EXECUTIVE-CALIBRATED H-stack для senior partner (SKIP-список + cross-ref §21):**

Запускается автоматически — не ждёт явного запроса. Cross-ссылка: см. §21 EXECUTIVE-CALIBRATED HUMANIZATION таблица (строки 2456-2475) — там полная таблица executive vs INFOBIZ register для всех 10 H. Применение для senior partner / managing director:
— SKIP: H1 wisp temple (senior partner crisp grooming — седина OK, но wisp = «не справляется с собой» = NDA-doubt сигнал), H5 handheld micro-drift (Cinema Studio = locked tripod на $50k Arri-rig look), H6 wrinkled wardrobe (charcoal/navy wool suit pressed, dress shirt crisp без crease — wrinkle = «junior associate с deal-floor», не partner), H9 lived-life face (puffiness под глазами читается как «hangover после client dinner», не gravitas).
— MODIFY: H2 natural speech cadence (без «эм» / «ну» — senior partner pacing медленнее, паузы 0.5-0.8s между ключевыми клозами), H4 not-actor Soul ID (cast senior partner — не stock-CEO «GQ cover»; реалистичная gravitas = morgan freeman / christopher walken тип, не chris hemsworth).
— OK: H3 lived-in workspace (wood-panel library с реальными bound treatises / financial journals / used legal pads — НЕ AI-stock «cleanest law library in the world»; **1-2 lived маркера максимум, не 3-4 как INFOBIZ**), H7 ambient audio без stock-music (только room tone + occasional pen-on-paper), H8 eye contact 70/30 (senior partners не «sales eye contact» 100% — есть looks-away-to-think beats), H10 props look used (Mont Blanc / Lamy 2000 с marking, legal pad с edges worn, leather portfolio с patina).

Target: 4-5 H-приёмов с calibration (не 6-7 как INFOBIZ founder). Без калибровки H-стэк INFOBIZ-уровня (wisp / wrinkled / handheld) → HNWI client читается как «consultant who couldn't make partner», UHNWI trustee — «not at our level» → conversion-drop у audience C-suite/HNWI.

**ПРАВИЛО 3 — PREMIUM POLISH vs AI SLICK граница (для wood-panel library / brass / leather / silk-tie):**

Corner-office library / Mayfair glass-partition / Park Avenue corner / Geneva quay (типичные settings HIGH_TICKET_PRO_SERVICES) — высокий риск AI-slick фейла на «luxury slick»:
— OK: REFLECTION pack для brass fixtures + glass partition (реалистичные отражения с micro-imperfection — patina на brass, лёгкие отпечатки на стекле, dust motes в light beam), LIGHT CONSISTENCY (один key-light через window-side + practical desk-lamp, не «award-winning cinematography»), фокус с micro-depth-of-field на лице (f/2.8-f/4), wool suit weave с natural micro-texture (не plastic-shiny suit), silk-tie с natural sheen (не «patent-leather» sheen).
— FAIL: «luxurious library», «pristine wood panelling», «picturesque corner office», «award-winning luxury cinematography», «opulent setting», «pristine brass», идеально гладкая кожа senior partner без пор / age spots / natural texture 50+ (AI tell для executive Soul ID).
— RULE: prompt-фраза «with natural micro-imperfections — patina on brass fixtures, used legal pads on desk, natural skin texture detail with age-appropriate features (fine lines, subtle age spots), slight dust motes in window light beam, worn leather chair patina» включается в EVERY HIGH_TICKET_PRO_SERVICES промт.

**ПРАВИЛО 4 — CONFIDENTIALITY guardrail (NDA + aggregated client-count + visible documents + setting integrity — жёстче B2B SaaS Enterprise):**

В B2B SaaS Enterprise generic alias = «legacy CRM» / «existing observability tool» (нейтральный класс tools). В HIGH_TICKET_PRO_SERVICES generic alias ДОЛЖЕН быть жёстче — даже «sovereign wealth fund client» / «$2B family office in Geneva» recognizable в узком рынке (где 30-50 SWF / 200-300 family offices глобально). NDA breach risk = personal liability senior partner + firm reputation + lawsuit. **Дополнительно — agregated client-count claim («47 families», «12 UHNWI clients») = indirect disclosure under Swiss banking secrecy (Art. 47 BankG) / FINMA Circular 2013/8 / Swiss attorney privilege (StGB Art. 321). FINMA enforcement 2019-2023 несколько case'ах flagged exactly такой формат.**

Триггеры NDA-breach + расширения:
— Exact client name («Saudi PIF», «Walton family office»).
— Exact deal («€3.2B Atos carve-out», «$890M cross-border tech M&A in DACH 2024»).
— Exact firm name conflict (бывший partner показывает прошлые сделки прошлого firm = возможный non-compete violation).
— **Aggregated client-count** («47 families», «12 UHNWI clients», «300+ corporate mandates») — treat как confidentiality risk даже без individual names.
— **Visible documents на background** (читаемые case files / deal docs / KYC pages / family-tree document с именами / signed engagement letters) — universal hard-block.
— **Setting integrity vs Soul ID** — location фона должен совпадать с registered office в bar/regulator registry. Если partner работает в Midtown без террасы, AI-сгенерированный «Park Avenue terrace» = false context (FINMA Circular 2013/8 + state bar misleading-impression rules).

PASS условия:
1. В крео — НИКОГДА не называть client / deal / counterparty exact string.
2. Generic alias ЖЁСТЧЕ B2B SaaS — НЕ «sovereign wealth fund» / «$2B family office» / «top-10 US bank», а: «institutional client», «UHNWI relationship», «multi-generational wealth structure», «mid-cap industrial transaction», «cross-border carve-out in regulated industry».
3. Geographic generalization: НЕ «Geneva-based family office», а «European wealth structure»; НЕ «DACH carve-out», а «Continental Europe transaction».
4. Year обобщение: НЕ «2024 deal», а «recent engagement» / «last reporting cycle».
5. Aggregated client-count: НЕ «47 families», а «multi-family relationship base» / «institutional mandate base» (без точного N).
6. Documents на background: blurred / generic abstract / removed entirely.
7. Setting: registered-office location ИЛИ нейтральная library/boardroom без identifying landmarks.

FAIL пример: `Dialogue: "We advised a $2B sovereign wealth fund out of Singapore on the Atos carve-out · across 47 family-office relationships"` → 4 нарушения (sector + geo + named target + aggregated count).

PASS пример: `Dialogue: "We advise institutional clients on cross-border carve-outs in regulated industries — engagement specifics per signed NDA"`.

**ПРАВИЛО 5 — Substantiation цифр + percentage success-rate disclaimer + "from X%" hard-block:**

Любая числовая claim в Dialogue / EXACT STRING / overlay = подпадает под V18 substantiation + profession-specific advertising rules (ABA 7.1 «false or misleading» / SRA Code 8.6 / SEC Marketing Rule «materially misleading»).

Self-attested LinkedIn bio / firm website «about us» = НЕ substantiation для V18. Нужны third-party verifiable источники:
— **AUM («$2B AUM»):** Form ADV Part 1 Item 5 (SEC filing, public) / Companies House annual return (UK) / FINMA registry (CH) / national regulator filing.
— **Closed-deals («$500M closed last year»):** Bloomberg / Refinitiv / Mergermarket / Pitchbook league-table reference + год + ranking-methodology.
— **Transaction count («47 cross-border M&A»):** Mergermarket counter с datestamp + scope-definition (cross-border = both legs disclosed? minority deals included?).
— **League-table («top-5 boutique»):** Refinitiv / Bloomberg / Mergermarket published ranking + год + sub-category (overall vs sub-vertical) + region.
— **Awards («Chambers Band 1»):** Chambers / Legal 500 / IFLR1000 directory link + год + practice area.

**Percentage success-rate в LEGAL (NEW — T.6-B КЕЙС 5):** «We win 89% of contested probate cases» / «97% success rate» — на reel физически не помещается полный disclaimer, поэтому hard-block без on-frame disclaimer в том же кадре. Audio disclaimer недостаточен (NY RPC 7.1(d) явно требует «на той же странице/в том же frame»). Sample-size + methodology disclosure обязательны: «X завершённых mandates по типу Y за период 2023-2024 (substantiation per intake records, individual outcomes vary)». Implied specialty claim («contested probate cases») = additional risk под ABA 7.4 + state bar specialization rules — требует board-certification если не сертифицирован, не reklamovat as specialist.

**"From X%" pricing pattern hard-block (NEW — T.6-B КЕЙС 2):** «Fees from 0.5% AUM» / «From £500 per case» = FCA COBS 4.5A.10R (price prominence) + ASA CAP Rule 3.18 (qualification of «from») = misleading by omission. Замена: «typical fee 1.2% AUM, minimum 0.5% AUM for {tier}», или удалить из крео и оставить «fees per Client Agreement».

PASS условия:
1. Substantiation source + дата ≤12 месяцев (для AUM ≤ last reporting cycle).
2. Methodology disclosure если ranking («Refinitiv 2024 cross-border M&A league table by deal value, mid-market sub-category»).
3. Percentage success-rate: sample-size N + period + scope + on-frame disclaimer «Prior results do not guarantee similar outcome» (одной frame с числом, не bottom-overlay).
4. "From X%" — заменить на «typical fee Y%, minimum X%» с typical fee prominence равной minimum.
5. Если substantiation отсутствует → переписать в qualified statement без числа («multi-billion AUM mandate base», «active in cross-border M&A», «recognized in directories»).

FAIL пример: `EXACT STRING: "$500M closed · 47 deals · 89% win rate · fees from 0.5%"` → 4 unsubstantiated claims (deals + win rate + from-pricing).

PASS пример: `EXACT STRING: "Active in mid-market cross-border M&A · Refinitiv 2024 league table (DACH sub-cat) · fees per mandate letter"`.

**ПРАВИЛО 6 — Indicative valuation / fee structure (НИКОГДА exact pricing в крео) + "free consultation" Rule 1.18 trigger:**

Exact pricing в HIGH_TICKET_PRO_SERVICES крео = двойной риск: (1) financial-promotion regulation (FCA s.21 FSMA / SEC Marketing Rule / FINRA 2210 require fee disclosure context — «$50k retainer» без context = misleading), (2) competitive misuse (конкурент использует ваш fee-pitch против вас).

Запрет в крео: «$50k retainer» / «1.5% success fee» / «$800/hour partner rate» / «1% AUM annual fee» / «50bps performance fee».

PASS формулировки по сегменту:
— **M&A:** «fees per success-fee schedule disclosed at engagement» / «retainer + success-fee structure per mandate letter».
— **Private banking / wealth advisory (US):** «fees per ADV Part 2A Brochure (available on request / SEC.gov)».
— **Private banking (UK):** «fees per Client Agreement, in line with FCA COBS 6.1A disclosure requirements».
— **Legal (corporate / M&A):** «hourly rates and scope per engagement letter» / «alternative fee arrangement per mandate scope».
— **Family office:** «fees structured per family-office relationship, disclosed at mandate signing».

Indicative valuation на бизнес клиента в крео («we'll get you 6-8x EBITDA») = ОТДЕЛЬНЫЙ FAIL — это implicit guarantee + opinion shop. Замена: «valuation range depends on sector multiples + diligence findings — assessed at engagement» / «we work to optimize valuation through structured process».

**"Free consultation" CTA триггер ABA Rule 1.18 (prospective clients) (NEW — T.6-B КЕЙС 5):** «Free 30-min consultation» создаёт prospective-client relationship → conflict-check obligations. Reel должен disclaim «Consultation does not create attorney-client relationship until engagement letter signed». Для UK SRA — аналогично риск non-paid intro = solicitation если cold-targeting.

FAIL пример: `Dialogue: "Our retainer is $50k upfront, 1.5% success fee, and we typically deliver 6-8x EBITDA outcomes · Free 30-min consultation"` → 4 нарушения (exact retainer + exact success-fee + implicit valuation guarantee + Rule 1.18 без disclaimer).

PASS пример: `Dialogue: "Fees structured per mandate letter — retainer plus success-fee. Valuation outcomes depend on sector multiples and diligence — discussed at engagement. Initial conversation does not create attorney-client relationship until engagement letter signed."`.

**ПРАВИЛО 7 — REGULATORY DISCLAIMERS pack по гео + сегменту + state bar matrix US + pre-clearance flag:**

Не «опционально к рассмотрению». Overlay-disclaimer обязателен в bottom-third для соответствующего гео + сегмента. Формат: 12-18pt Inter Regular / Garamond, white-90% на gradient-darken bottom-strip, present 0-end, ≤120 chars per line.

**US — investment advisory (RIA / private banking / family office):**
— «Past performance does not guarantee future results.»
— «Investment advisory services through {Firm Legal Name}, an SEC-registered investment adviser. Registration does not imply skill or training.»
— ADV Part 2A reference на лендинге обязательна.
— SEC Marketing Rule 206(4)-1: если показ performance — net-of-fees + prescribed time periods + standardized methodology.

**US — broker-dealer (FINRA 2210):**
— «Securities offered through {BD Name}, member FINRA/SIPC.»
— Pre-use approval registered principal + Filing с FINRA для retail communications в 10 business days.

**US — law firm (ABA Model Rules 7.1-7.5 + state bar matrix — NEW T.6-B КЕЙС 5):**
— Universal: «Attorney Advertising. Prior results do not guarantee a similar outcome.» (mandatory NY, CA, FL, TX — практически all states).
— **NY** — Rules of Professional Conduct 7.1(d): disclaimer must appear on the **same frame** as the success-claim (not separate bottom-overlay if claim в hook).
— **CA** — CRPC 1-400 + Rule 7.4: «specialist / certified» ONLY если State Bar Legal Specialization certification.
— **TX** — Lawyer Advertising Review Committee pre-clearance required для определённых categories (quantifiable past results, comparison claims) — flag `tx_advertising_review_required: true` если применимо.
— **FL** — Rule 4-7.13: pre-publication review by Florida Bar для quantifiable claims (e.g. «89% success rate») — flag `fl_pre_clearance_required: true`. Без pre-clearance в FL = disciplinary risk.
— No «expert / specialist» claim если нет state-recognized certification (ABA 7.4 + state bar).

**UK — financial services (FCA COBS):**
— «{Firm Name} is authorised and regulated by the Financial Conduct Authority, Firm Reference Number {FRN}.»
— Financial promotion approval per s.21 FSMA gateway — sign-off authorised person required PRE-launch. Поле `s21_approver_name` + `approval_date` обязательны в intake.
— COBS 4.5 (retail) / 4.6 (eligible counterparty) — risk-warning prominence equal to benefit-claim prominence.
— **Consumer Duty + PROD 3 target-market match (NEW T.6-B КЕЙС 2):** financial promo для UHNWI не может идти в open Instagram feed без targeting filter (age + income + interests + geo). Flag «open-targeting + UHNWI claim = FCA risk».

**UK — law firm (SRA + BSB):**
— Solicitors: «{Firm Name} is authorised and regulated by the Solicitors Regulation Authority (SRA No. {N}).»
— Barristers (BSB rC10): запрещено имена клиентов даже generic recognizable, запрещено «success rate %» — переписать в «recognized in {directory}». **Default — НЕ генерировать AI-likeness barrister, использовать generic «chambers» voice-over без identifiable face.**

**EU — Poland (Kodeks Etyki Adwokackiej §23 — cross-ref meta-policy-checker строки 475-481):**
— «Adwokat wpisany na listę {Izba Adwokacka w {City}}, nr wpisu {N}.»
— Запрет comparative ranking, запрет client testimonials в открытой рекламе, запрет «najlepszy / wiodący / №1», запрет «liczba wygranych».
— Cross-border solicitation (PL adwokat reklamует к diaspora в DE/UK) → flag jurisdictional reach + GDPR Art. 9 special-category targeting через language-based lookalike (NEW T.6-B КЕЙС 3).

**EU — Germany (BRAK BORA — cross-ref meta-policy-checker строки 482-485):**
— Запрет sensational ad style, объективная информация only (§43b Sachlichkeitsgebot).
— Если Fachanwalt designation — exact specialization wording per BRAK directory.
— §6 — success fee запрет в большинстве категорий.

**EU — funds (MiFID II + AIFMD + UCITS + PRIIPs):**
— KIID / KID reference обязательна при mention specific fund.
— Suitability target-market disclosure если retail-facing.
— Risk indicators 1-7 scale в крео для PRIIP-classified products.

**CH — Swiss FinSA / FIDLEG:**
— «{Firm} regulated by FINMA, license {N}» (если FINMA-licensed).
— Prospectus reference required при offering qualifying instruments.
— Swiss attorney-client privilege (StGB Art. 321) — абсолютная, НЕ waiveable клиентом для marketing.

GUARDRAIL: Если гео-mix кампании (US + UK + EU) — overlay rotation по placement-set (один disclaimer на каждое гео в своём set), НЕ один collapsed overlay со всеми регуляторами (нечитаемо + не соответствует ни одному регулятору properly).

**ПРАВИЛО 8 — AI DISCLOSURE pack для senior partner Soul ID — обязательно даже без regulatory trigger:**

Если Soul ID = senior partner в публичном domain (firm website partner page / Chambers profile / LinkedIn / earnings calls / interview) → AI DISCLOSURE pack ОБЯЗАТЕЛЕН независимо от гео и независимо от того есть ли direct regulatory mandate. В B2B SaaS Enterprise это правило применяется к public CEO; в HIGH_TICKET_PRO_SERVICES — расширяется на ВСЕХ name-partner-level Soul ID, потому что senior partner — это «firm face» и AI-likeness без disclosure ломает client trust на уровне fiduciary relationship (не просто marketing).

Дополнительные правовые слои поверх B2B Enterprise §8:
— **US:** Lanham Act + state right-of-publicity (CA Civil Code §3344 + §3344.1 post-mortem / NY Civil Rights Law §50-51 / TX Property Code §26.001+ / TN Personal Rights Protection Act) + ABA Model Rule 7.1 (false or misleading communication — undisclosed AI-likeness реального partner = misleading representation that partner personally endorses).
— **UK:** SRA Code Principle 5 (act with integrity) + Image Rights case law (Robyn Rihanna Fenty v. Topshop).
— **EU AI Act art.50** (effective 2026): transparency obligation для AI-generated content depicting real person — extraterritorial для EU-visible ads.
— **CH:** FINMA Conduct Rules + Swiss personality rights (Art. 28 ZGB).

Overlay-формат: `«AI-assisted visual · {Name}, {Title} {Firm}»` (bottom-third, present 0-end, ≤90 chars, Inter Regular 14pt, white-90% on gradient-darken). Для FINRA-registered PM добавить CRD #: `«AI-assisted visual · {Name}, Portfolio Manager · CRD #XXXXX»`.

GUARDRAIL #1: даже если senior partner лично дал sign-off на marketing use of likeness — sign-off на marketing ≠ sign-off на AI-generation. Это **разные** rights. AI DISCLOSURE pack нужен дополнительно к sign-off, не вместо.

GUARDRAIL #2: для barristers (UK BSB) — AI-likeness barrister на marketing = additional risk поверх BSB ad rules (barristers не могут soliciting client work через personal-image marketing типа). Default — НЕ генерировать AI-likeness barrister, использовать generic «chambers» voice-over без identifiable face.

GUARDRAIL #3: для law firm partners в jurisdictions где «specialist / expert» claim требует state certification — AI-rendered partner в кадре + claim «specializes in M&A» = potential ABA 7.4 violation если не сертифицирован.

**ПРАВИЛО 9 — OPERATIONAL GUARDRAILS (sanctions/OFAC + Reg D general-solicitation + dual-credentialing + cross-border) — NEW T.6-B GAP-list:**

Четыре оперативных guardrail-а, которые НЕ покрываются V1-V22 и НЕ покрываются meta-policy-checker:

**(a) Sanctions / OFAC / SECO / EU geo-screening:**
Любое targeting в sanctions-relevant geo (RU / BY / IR / KP / VE + SDN list) → hard-block + escalation на compliance до запуска. Особенно критично для CH/UK/US private banking + family-office (FINMA AML / OFAC SDN screening / EU GBAML). Если кампания target «ex-USSR HNWI» — geo whitelist по country без RU/BY обязателен.

**(b) Reg D general-solicitation trigger (US private placements):**
Если клиент offers securities under Reg D 506(b) (запрет general solicitation) → ЛЮБОЙ performance claim в open Meta/LinkedIn feed = loss of safe harbor → потеря Reg D exemption → registration violation. Flag в intake: `client_offers_securities: y/n` → если yes, либо переключение на Reg D 506(c) с investor verification, либо удаление всех performance / fund-raising claims из крео.

**(c) Dual-credentialing detection (banker + licensed attorney / advisor + broker-dealer):**
Если Soul ID имеет двойную credential (банкир-JD / advisor + Series 7) — rule-set применяется кумулятивно (FINRA + state bar + SEC RIA), не disjunctive. Триггер: bio mention «JD + Series 7» / «attorney + investment advisor» — preset applies ABA 7.1 + FINRA 2210 + SEC 206(4)-1 simultaneously, любой violation в любом frameworks = FAIL.

**(d) GDPR special-category targeting через language-based lookalike:**
Targeting «PL-speakers в DE» / «RU-speakers в US» через Meta lookalike audiences = ethnicity proxy через language = special-category processing под GDPR Art. 9 без explicit consent. EU DPA (PL UODO / DE BfDI) могут treated как breach. PASS условие: либо отказ от language-based targeting в EU, либо explicit consent collection через лендинг до retargeting (combined identifier risk также cross-ref CRISIS-AUDIT-LAYER C4 строка 3058).

**HIGH_TICKET_PRO_SERVICES_PRESET — финальный чек-лист (9 проверок перед выдачей промта):**

| # | Проверка | PASS если | FAIL → |
|---|---|---|---|
| 1 | Cinema Studio + Veo 3.1 + PORTRAIT CU + REFLECTION + FABRIC + HAIR senior packs | Да | Переключить workspace, подключить недостающие packs |
| 2 | EXECUTIVE-CALIBRATED H-stack (SKIP H1/H5/H6/H9, MODIFY H2/H4, OK H3/H7/H8/H10 — cross-ref §21 строки 2456-2475) | Да | Убрать «wisp» / «wrinkled» / «handheld» / «puffy» из промта |
| 3 | Premium polish prompt-фраза включена («patina on brass, used legal pads, natural age-appropriate skin texture, dust motes in window light, worn leather patina») | Да | Дописать |
| 4 | NDA / confidentiality жёсткий generic alias + НЕТ aggregated client-count + НЕТ visible documents + setting integrity (registered office или нейтральный) | Да | Заменить recognizable alias / aggregated count / blurred documents / убрать identifying landmark |
| 5 | Substantiation цифр third-party verifiable (Form ADV / Companies House / Bloomberg / Mergermarket / Chambers) с методологией + датой; percentage success-rate — sample-size + on-frame disclaimer; «from X%» — заменён на «typical X%, minimum Y%» | Да | Запросить source / добавить disclaimer / переписать pricing |
| 6 | Pricing / valuation НЕ exact (формулировка «fees per mandate letter / ADV Part 2A / engagement letter»), valuation outcomes qualified, «Free consultation» CTA с Rule 1.18 disclaimer | Да | Заменить exact pricing на mandate-letter; убрать valuation guarantee; добавить Rule 1.18 disclaimer |
| 7 | REGULATORY DISCLAIMERS pack под гео + сегмент (US: ADV + Attorney Advertising + state bar matrix NY/CA/TX/FL / UK: FCA FRN + SRA + s.21 approver / EU: Izba + KIID + BRAK / CH: FINMA), при гео-mix — rotation по placement-set, pre-clearance flag TX/FL отмечен | Да | Добавить нужный overlay, развести гео-mix по placement-set, escalate на pre-clearance |
| 8 | AI DISCLOSURE pack включён (overlay «AI-assisted visual · {Name}, {Title} {Firm}» + CRD # если FINRA), sign-off на marketing ≠ sign-off на AI-generation проверен отдельно; barrister default — без identifiable face | Да | Добавить overlay; запросить отдельный AI-generation sign-off; для barrister — переключить на chambers voice-over |
| 9 | OPERATIONAL guardrails: sanctions/OFAC geo-whitelist + Reg D general-solicitation flag + dual-credentialing rule-set cumulative + GDPR Art. 9 language-based lookalike consent | Да | Escalate на compliance, удалить performance claim из cold feed, добавить explicit consent на лендинг |

9/9 PASS → промт выпускается ученику.
≤8/9 PASS → return to editor, не выпускается. Конкретные FAIL-причины перечисляются в return-note.

**HIGH_TICKET_PRO_SERVICES — 3-STEP FUNNEL GRANULARITY (NEW T.6-C дыра 3):**

В отличие от плоской CTA-альтернативы строки 2751-2752, для HIGH_TICKET_PRO_SERVICES funnel-step разбивка обязательна (по аналогии с CRISIS_EXPERT 3-STEP FUNNEL):

| Step | Цель | Арка | CTA | Регуляторный риск |
|------|------|------|-----|---|
| TOF | Awareness — industry trend / market intelligence | G через §19B EDUCATIONAL-PROGRESSION (process / data visualization без лиц) | «Download market briefing» / «Subscribe to our quarterly outlook» / «Get our M&A 2026 outlook» | Низкий (educational, не financial promotion) |
| MOF | Nurture — methodology + process credibility | C (партнёр Soul ID tripod) / F через §19B ANIMATED-DIAGRAM | «Watch our M&A process explainer» / «Get our valuation framework» / «Anonymized case-study download» | Средний (substantiation на process claims) |
| BOF | Close — confidential, pre-qualified | C (партнёр Soul ID) | «Schedule confidential intro call» / «Speak to partner» / «Request engagement proposal» | Высокий (ABA 7.3 / SRA solicitation если cold; FCA s.21 если financial promo) |

GUARDRAIL: Cold BOF CTA (US ABA 7.3 «solicitation» / UK SRA Code 8.4 + 8.5) — высокий риск violation. Default — soft TOF/MOF в cold-аудитории, BOF только в retargeting/warm. Для FCA-regulated firm BOF в cold open feed = s.21 FSMA violation если ad не pre-approved authorised person.

═══════════════════════════════════════════════════

KIDS_PARENTS (детские курсы, развивайки) — короткие дефолты:
— Workspace: Marketing Studio
— Hook: H5 (контраст — ребёнок в Roblox vs ребёнок с собственной игрой)
— Лицо ребёнка → ТОЛЬКО с письменным согласием родителей, иначе back-of-head / ECU экрана с проектом
— Format: 9:16 + 6-7s

**Для полного workflow KIDS_PARENTS используй KIDS_PARENTS_PRESET ниже (волна Т.5 — 8 правил + финальный чек-лист).**

═══════════════════════════════════════════════════
KIDS_PARENTS_PRESET — отдельный пресет (волна Т.5 после Т.5-5 мета-аудита 25 дыр)
═══════════════════════════════════════════════════

Контекст: до волны Т.5 правила KIDS_PARENTS состояли из 4 строк дефолтов + CHILDREN IN FRAME pack (28 строк) + 5 строк V17-diaspora + однострочные упоминания в V19-BIOCLAIM / CTA-matrix / §19B. В 5-10 раз меньше, чем B2B_SAAS_ENTERPRISE_PRESET (130 строк) или CRISIS-AUDIT-LAYER (200 строк). Агент при сборке промта для USA-KIDS_PARENTS теряет 90% guardrails (COPPA combined-identifier / FTC §255.5 parent-endorser / state-laws CA AB-2839 + NY Marsh's Law / accreditation substantiation / DEI representation / 3-step funnel). Этот пресет — единая точка истины.

**КОГДА АКТИВИРУЕТСЯ KIDS_PARENTS_PRESET:**

Профиль клиента = KIDS_PARENTS, и любой из триггеров:
— Аудитория = родители детей 8-14 (mother-primary / father-primary).
— Soul ID опции содержат: real parent endorser / AI parent-actor / teacher / дети в кадре (любая форма).
— Чек $80+/мес subscription ИЛИ $300+ одноразовый курс.
— Гео USA / UK / Canada / EU (любая комбинация).
— Любой accreditation claim (CSTA / Roblox Education / state charter / college-prep).
— Любой substantiation на cohort metrics («N+ выпускников за Y лет»).

Если хотя бы один триггер — все 8 правил ниже **обязательны**.

**ПРАВИЛО 1 — Workspace + модель + packs (дефолт жёсткий):**
— Workspace = Marketing Studio (по умолчанию) ИЛИ Cinema Studio (если parent-endorser в Soul ID + чек >$200/мес — EXECUTIVE-CALIBRATED).
— Модель = Veo 3.1 (parent-endorser talking-head с lip-sync) ИЛИ Kling 3.0 + VO FALLBACK PACK (если рот ребёнка крупно нужен — НЕ генерируй, только voice-over).
— Packs = PORTRAIT CU + LIGHT CONSISTENCY + ANTI-AI-LOOK (ОБЯЗАТЕЛЕН) + CHILDREN IN FRAME pack + DEI representation lock для USA.
— Статика-слой (accreditation-бейдж / гайд-обложка / инфографика курса) = Nano Banana 2 + инлайн `NEGATIVE PROMPT:` в том же блоке (per R9 — негатив парсится только в image-моделях; для видео-шотов строку НЕ добавлять).
— Format = 9:16 + 6-9s primary.

**ПРАВИЛО 2 — 3 acceptable Soul ID modes (точная классификация):**

| Mode | Что включает | Что обязательно |
|------|------|------|
| **A. Real parent endorser** | Реальный родитель-актёр (не AI-генерированный) рассказывает о ребёнке | FTC §255.5 disclosure («#paid» / «#ad» на лендинге) + sign-off на marketing use + V19 sign-off на формулировку + AI DISCLOSURE pack НЕ обязателен (нет AI-likeness) |
| **B. AI parent-actor** | AI-сгенерированный родитель (Soul ID) | AI DISCLOSURE pack ОБЯЗАТЕЛЕН + cast diversity lock + sign-off на marketing use ≠ sign-off на AI-generation (отдельно) + state-laws (CA AB-2839 / NY Marsh's Law если AI похож на real person) |
| **C. Teacher Soul ID** | AI или real-teacher (с accreditation) рассказывает о методе | Если teacher = real person в reg. registry (CSTA member / state-licensed) → AI DISCLOSURE pack ОБЯЗАТЕЛЕН per CRISIS-AUDIT-LAYER C8 generalization + accreditation badge в кадре через Nano Banana 2 |

**ПРАВИЛО 3 — 5 acceptable child-in-frame modes + 4 запрещённых (КРИТИЧНО):**

**OK моды:**
1. Silhouette / back-of-head (anonymized);
2. Hands-only ECU on keyboard (no face);
3. Over-shoulder PoV at screen (parent или ребёнок — без лица);
4. Group lifestyle wide shot (≥3 детей в кадре, NO facial CU, diverse representation для USA);
5. Project showcase без identifying (screen of game / drawing / code — voiceover родителя narrates, no child voice).

**ЗАПРЕЩЁННЫЕ моды (любой = FAIL):**
1. AI-rendered child face frontal любого возраста (COPPA + state laws + Meta CSR);
2. Real child face frontal БЕЗ written dual-parent consent + IRB-style ethics review for commercial use (даже с consent — высокий риск, тщательно взвешивать);
3. Before/after «двоечник → отличник» (Meta Category 7 запрет line 583 + sensational frame для minor);
4. Negative emotion child CU (грусть / страх / усталость) — Meta Category 7 запрет + sensational.

**Между acceptable и запрещённым — child face CU с POSITIVE emotion (focused on code / laughing at successful build) — ТРЕБУЕТСЯ:** dual-parent consent + accreditation body sign-off если product = education + FTC «typicality» disclaimer. Default — избегать positive CU тоже, использовать over-shoulder PoV.

**ПРАВИЛО 4 — Parent-endorser claim substantiation (V19 + FTC §255.5):**

Если parent говорит «my {Name} прошёл курс / собрал игру / сделал project» — triggers:

PASS условия:
1. Sign-off родителя на use of likeness + AI-generation use отдельно (если AI parent-actor);
2. FTC §255.5 «typicality» disclaimer на лендинге («Results not typical; individual progress varies»);
3. COPPA combined-identifier check: имя ребёнка + школа + sequence курса = identifiable. Если risk — генерик alias: «my son / my daughter» (НЕ «my Alex»);
4. Child opt-in if 13+ (COPPA threshold) / dual-parent consent if <13;
5. Substantiation за конкретный outcome — cohort batch data ИЛИ переписать в качественный quantifier.

FAIL пример: `"My Alex, 12, San Diego, finished Python in 12 weeks — now sells games in Roblox marketplace"` → 4 нарушения (combined identifier + non-substantiated + child commercial activity + name+age+geo).

PASS пример: `"My son worked through the Python track for one semester. He started building games on his own"` → generic alias + qualified outcome.

**ПРАВИЛО 5 — Accreditation claim guardrail (CSTA / Roblox Education / state charter / college-prep):**

Любое accreditation claim требует:
1. Verifiable public registry reference (CSTA member directory URL / Roblox Education partner badge URL / state charter registry).
2. Verification date ≤90 days до запуска (membership active, не expired).
3. Badge в кадре через Nano Banana 2 EXACT STRING ИЛИ в Meta primary text.
4. Запрет «лучший в США» / «#1 школа» / «leading platform» (superlative + named cohort = FAIL).

FAIL пример: `"CodeJunior — лучшая школа программирования для детей в США. CSTA accreditation."` → superlative + accreditation без registry verification.

PASS пример: `"CSTA-accredited curriculum (Member directory: csta.example/members/codejunior) · Roblox Education Partner since 2022"`.

**ПРАВИЛО 6 — MINORS_AI_LIKENESS + state-laws (USA expansion):**

Любой AI-likeness child в крео для USA-аудитории — дополнительные state-laws поверх COPPA/GDPR-K:
- **CA AB-2839 (effective 2025):** civil + criminal penalties за «substantially manipulated image of minor in commercial use without parent + minor consent».
- **NY Marsh's Law (2024):** civil right of action для deepfake-of-minor (включает AI-generated likeness даже если не real-person).
- **TX SB-1361:** similar to CA.
- **EU AI Act art.50 extraterritorial:** AI-generated minor likeness в EU-visible ads = transparency obligation.

AI DISCLOSURE pack для child-AI — усиленный overlay:
`«AI-generated character · not real child · {Brand} Inc.»` (bottom-third, present 0-end, ≤60 chars, Inter Regular).

Pre-launch для USA кампаний с AI-child: Meta Standards request + при возможности pre-disclosure email to Meta CSR team для AI-child кампаний.

GUARDRAIL: даже AI «cartoon-style» (явно stylized) — overlay требуется, потому что Meta image-of-minor policy НЕ различает realistic vs stylized AI.

**ПРАВИЛО 7 — 3-step funnel granularity для KIDS_PARENTS (закрытие D4):**

Если профиль KIDS_PARENTS с 3+ шагами funnel (typical: парент-крео hook → лендинг → бронь free trial → trial attended → подписка/одноразовый чек), пачка крео должна содержать минимум по 1 крео на step.

Таблица сюжетных арок × funnel-step для KIDS_PARENTS:

| Step | Цель | Арка (§20) | EXACT STRING focus | CTA |
|------|------|------|------|------|
| TOF | Awareness parent | F (process visual через §19B) | «4-month Python curriculum for ages 8-14» | «See trial schedule» (soft) |
| MOF | Trust building | C (teacher + curriculum) через Soul ID tripod | «CSTA-accredited · Roblox Edu partner · {N}+ alumni since {year}» | «Book a free trial» |
| BOF | Subscribe close | A (project showcase + parent voice) | «$129/mo subscription · 1-on-1 with mentor · monthly cancellation» | «Start subscription / Talk to coach» |

Правило пачки для KIDS_PARENTS:
- LITE (3 крео): TOF + MOF + BOF — по одному каждого. **НЕ 3 TOF.**
- STANDARD (5 крео): 2 TOF + 2 MOF + 1 BOF.
- PRO (7 крео): 3 TOF + 3 MOF + 1 BOF.

GUARDRAIL: НЕ смешивай TOF hook («4-month Python curriculum» — awareness) + BOF CTA («Start subscription $129/mo») в одном крео — разрыв воронки.

**ПРАВИЛО 8 — V17 KIDS_PARENTS hook table (закрытие D5):**

Базовый KIDS_PARENTS (не diaspora) — таблица замен parent-victim → ambition:

| FAIL hook (parent-victim / fear) | PASS replacement (parent-ambition / child-result) |
|---|---|
| «Ваш ребёнок отстаёт от сверстников?» | «За 12 уроков ребёнок собрал первую игру в Roblox» |
| «У ребёнка нет навыков 21 века?» | «Сын просыпается и сам открывает ноутбук — доделать игру» |
| «Не дайте ребёнку остаться позади» | «Следующий поток — 5 ноября, 12 мест из 18» (substantiated time-anchor) |
| «Mommy guilt — ты подводишь его будущее» | «Вы хотели чтобы ребёнок программировал — вот первый шаг» |
| «Хороший родитель не упустит шанс» | «Free trial class — посмотрите подходит ли формат вашему ребёнку» |
| «100% выпускников получили работу» | «Многие выпускники продолжают учиться в кодинге в старших классах» |
| «Каждый день промедления стоит 1% потенциала» | удалить + переписать через «3 acceptable Soul ID modes» |
| «Двоечник → отличник за 3 месяца» | удалить + переписать в WHAT-демонстрацию (over-shoulder PoV экрана с проектом) |

**KIDS_PARENTS_PRESET — финальный чек-лист (8 проверок перед выдачей промта):**

| # | Проверка | PASS если | FAIL → |
|---|---|---|---|
| 1 | Workspace + модель + packs (ANTI-AI-LOOK + CHILDREN IN FRAME + DEI lock) | Да | Подключить недостающие packs |
| 2 | Soul ID mode классифицирован (A real parent / B AI parent-actor / C teacher) с соответствующим disclosure | Да | Добавить FTC §255.5 disclaimer / AI DISCLOSURE pack / accreditation badge |
| 3 | Child-in-frame mode из 5 acceptable (silhouette / hands-only / over-shoulder / group / project showcase) | Да | Переснять кадр в acceptable mode |
| 4 | Parent-endorser claim substantiated + generic alias (не combined identifier) + FTC typicality | Да | Заменить «my Alex» на «my son», добавить typicality disclaimer |
| 5 | Accreditation claim с public registry URL + verification date ≤90 days + без superlative | Да | Добавить registry reference, удалить «лучший / #1» |
| 6 | AI DISCLOSURE pack (усиленный overlay для AI-child + state-laws для USA) | Да | Добавить overlay «AI-generated character · not real child · {Brand}» |
| 7 | 3-step funnel granularity соблюдена (пачка содержит TOF+MOF+BOF, hook step соответствует CTA step) | Да | Перераспределить пачку по step |
| 8 | V17 hook прошёл (нет parent-victim / fear / guilt-trip / before-after child) | Да | Заменить hook по таблице правила 8 |

8/8 PASS → промт выпускается.
≤7/8 PASS → return to editor с конкретными FAIL.

═══════════════════════════════════════════════════

═══════════════════════════════════════════════════
KIDS_PARENTS_EDTECH_PRESET — sub-profile поверх KIDS_PARENTS_PRESET (волна Т.10 после Т.10-А создателя)
═══════════════════════════════════════════════════

Контекст: KIDS_PARENTS_PRESET (волна Т.5, ~210 строк) покрывает общие guardrails для родительской ниши — CHILDREN IN FRAME, FTC §255.5 parent-endorser, MINORS_AI_LIKENESS state-laws (CA AB-2839 / NY Marsh's Law / TX SB-1361), accreditation substantiation в общем виде, 3-step funnel. EDTECH-слой (онлайн-обучение детей — language learning Duolingo Kids / Reading IQ / ABCmouse, STEM-курсы Khan Academy Kids, coding Code.org / Tynker, math tutoring, Roblox Education, Minecraft Education, EdTech-приложения Outschool) поверх этого добавляет специфические federal+state законы (COPPA / SOPIPA / SOPPA / NY Ed Law §2-d / FERPA), accreditation bodies (Cognia / WASC / SACS / MSCHE), AAP/WHO screen-time guidelines для age-appropriate marketing, Click-to-Cancel для subscription EdTech, outcome substantiation для standardized testing claims. Этот sub-profile — единая точка истины для EDTECH-flight'ов поверх базы KIDS_PARENTS.

**КОГДА АКТИВИРУЕТСЯ KIDS_PARENTS_EDTECH_PRESET:**

Сначала срабатывает KIDS_PARENTS_PRESET (см. триггеры строки 4138-4148). EDTECH-слой подключается дополнительно, если выполнен ХОТЯ БЫ ОДИН триггер EDTECH:
— Продукт = онлайн-курс / приложение / SaaS-платформа обучения для детей <18 (language / STEM / coding / math / reading / Roblox Edu / Minecraft Edu).
— Любая форма коллекции personal info от детей <13 (имя / email / голос / фото / геолокация / device ID / cookie) — COPPA-trigger.
— Любая интеграция со школой / district / classroom-use (LMS Canvas / Schoology / Google Classroom / Clever SSO) — SOPIPA/SOPPA/NY Ed Law §2-d / FERPA-trigger.
— Любой claim accreditation (Cognia / WASC / SACS / MSCHE / state-recognized) или affiliation (Roblox Education partner / Code.org affiliate / Common Sense Media kidSAFE certified).
— Любой outcome claim («improves SAT 200 pts» / «boosts grades by 30%» / «1.5 grade levels in N months») — FTC §5 substantiation.
— Subscription / free-trial-to-paid model (FTC Click-to-Cancel 16 CFR §425).
— Гео USA любого state ИЛИ EU/UK (GDPR-K) ИЛИ диаспора в EU/USA (cross-ref EU_RUSSIAN_DIASPORA_PRESET).

Если триггер EDTECH сработал — все 9 правил ниже **обязательны ДОПОЛНИТЕЛЬНО** к 8 правилам KIDS_PARENTS_PRESET.

**ПРАВИЛО 1 — Workspace + модель + packs (EDTECH-specific layers):**
— Workspace = Marketing Studio (дефолт) ИЛИ Cinema Studio (если parent-endorser talking-head + чек $300+/мес EdTech subscription).
— Модель = Kling 3.0 (over-shoulder PoV родителя на экран приложения, screen-share UI motion) ИЛИ Seedance 2.0 (multi-shot: hands-on-keyboard → screen UI → project showcase, 4-5 шотов через TRANSFORMATION mode) ИЛИ Veo 3.1 (parent-endorser с Dialogue: блоком, lip-sync на EN).
— **НИКОГДА Kling 3.0 + ребёнок-голос в кадре крупно** (CHILDREN IN FRAME pack lockout) — voice-over только в CapCut, голос ребёнка не генерируется AI.
— Packs ОБЯЗАТЕЛЬНО: ANTI-AI-LOOK + CHILDREN IN FRAME + DEI representation lock (USA) + **LEARNING ENVIRONMENT pack** (classroom / home-desk / kitchen-table light setup, soft warm key 4200K, no fluorescent green) + **WHITEBOARD/SCREEN-SHARE pack** (для course UI demo через Nano Banana 2 → @image1 → Kling 3.0 soft node-by-node reveal, см. ANIMATED-DIAGRAM PACK строка 984) + **EDTECH SCREEN MOCKUP overlay** (Nano Banana 2 рендер app UI с generic brand alias — НЕ копировать реальный Duolingo / Khan Academy интерфейс, FTC §43(a) trade dress risk).
— Format = 9:16 + 6-9s primary, для 3-tier subscription comparison → 1:1 + COMPARISON-CARDS PACK (строка 930).

**ПРАВИЛО 2 — COPPA verifiable parental consent matrix (15 USC §6501-6506 + FTC COPPA Rule §312.5):**

Если продукт собирает personal info от детей <13 (любой combined-identifier: имя+age, голос child, фото child, voice recording, persistent ID для behavioral retargeting, геолокация device) — требуется verifiable parental consent (VPC) ДО collection. Метод VPC зависит от использования info:

| Use of info | VPC method (per §312.5(b)) | Документация |
|---|---|---|
| Internal use only (no disclosure to 3rd parties, no behavioral ads) | «Email Plus» — email confirmation + delayed confirmation (phone call / signed form / 2nd email после 24h) | Лог email-цепи + timestamp |
| Disclosure to 3rd parties / behavioral advertising / public display child profile | Sliding-scale stronger: credit-card $0.50 charge / video confirmation / government ID + face-match / signed form via mail-fax / knowledge-based authentication | Receipt / video archive / signed PDF |
| Federally registered identity service | Use of FTC-approved §312.5(b)(2)(vii) method (e.g. SuperAwesome KidSafe) | API audit trail |

В крео для EDTECH с продуктом <13: ОБЯЗАТЕЛЬНО показывать parent-consent step в funnel UI (Nano Banana 2 рендер screen «Parent: verify your identity to enable {Brand} for {child name}»). Запрещено в крео изображать ребёнка <13 как самостоятельно регистрирующегося / вводящего email / нажимающего «I agree» — это сигнал агрессивной regulator: «коллекция данных от minor без parent involvement» = COPPA §312.5 violation.

FAIL пример: «8-year-old создаёт аккаунт сам, мама в фоне варит кофе» → суггерирует bypass parent consent.
PASS пример: «Mom logs in, taps "Add child profile", verifies with credit-card $0.50 charge screen on phone» → демонстрирует VPC compliance.

**ПРАВИЛО 3 — State student-data privacy laws (per state-targeting check):**

COPPA — federal floor для <13. Над ним state laws для K-12 students любого age (включая 13-17). При targeting в крео on a state-by-state basis — проверка матрицы:

| State | Law | Triggers + что требуется в крео/funnel |
|---|---|---|
| **CA** | SOPIPA (Student Online Personal Information Protection Act 2014) | K-12 students любого age. Запрет targeted ads + sale данных student. В крео: «No ads. No data sale. SOPIPA-compliant.» badge OK если в privacy policy подтверждено. |
| **IL** | SOPPA (Student Online Protection Act 2020) | Granular consent + breach notification 60 days. School-targeting ads требуют district-level approval. В крео для IL avoid «sign up your school» CTA без disclaimer «school approval required». |
| **NY** | Ed Law §2-d + Part 121 NYSED regs | District-level data protection officer. Operator agreement обязателен. В крео — НЕ заявлять «used in NY schools» без verifiable district contract list. |
| **CT** | PA 16-189 + 17-200 | Contract registry public. Запрет behavioral ads to students. |
| **FL** | HB 1547 (2023) | Notice + opt-out для parent. Запрет sale student data. |
| **CO** | HB 16-1423 + SB 17-068 | Student PII protection + transparency requirement. |

Pre-flight для US-EDTECH крео с state-specific targeting (Lookalike audience by state): запустить `meta-policy-checker` категория «KIDS_PARENTS_EDTECH state student-data privacy». Если state не верифицирован в operator agreement — broad-geo USA targeting без state-named CTA («used in NY schools» → «used in classrooms nationwide»).

**ПРАВИЛО 4 — Accreditation substantiation (Cognia / WASC / SACS / MSCHE / state recognition):**

Любой EDTECH-claim accreditation требует verifiable public registry reference + verification date ≤90 days до запуска (то же правило что KIDS_PARENTS_PRESET Правило 5, но расширенный список bodies для EDTECH):

| Accreditation body | Scope | Verification URL pattern |
|---|---|---|
| **Cognia** (former AdvancED) | K-12 schools + programs, global | `cognia.org/find-a-school` directory + accreditation ID |
| **WASC** (Western Association of Schools and Colleges) | K-12 + post-secondary, Western US + Pacific Rim | `acswasc.org/directory-of-schools` |
| **SACS** (Southern Association of Colleges and Schools, part of Cognia) | K-12 + post-secondary, Southern US | через Cognia directory |
| **MSCHE** (Middle States Commission on Higher Education) | Post-secondary (если EDTECH = bridge-to-college) | `msche.org/institutions` |
| **State recognition** | CA Dept of Ed / NY State Ed Dept / TX TEA — для K-12 charter / private school programs | State directory URL |
| **Common Sense Media kidSAFE** | EdTech apps кids-targeted (privacy + content) | `kidsafeseal.com/certifiedproducts` |
| **Roblox Education Partner** | Roblox education curriculum providers | `education.roblox.com/partners` (если public listing) |
| **Code.org Affiliate Network** | CS curriculum для K-12 | `code.org/educate/regional-partner` |

FAIL пример: `"Accredited STEM curriculum · trusted by 500+ US schools"` → нет accreditation body named + нет registry URL + numeric claim без proof.
PASS пример: `"Cognia-accredited K-8 STEM program (cognia.org/find-a-school/{ID}) · Code.org Affiliate since 2022"` → named body + verifiable URL + dated.

Запрет superlatives: «#1 EdTech for kids» / «Best math app in USA» / «Leading coding platform for children» — без named ranking source (e.g. Common Sense Media Award 2024 + URL) это FTC §5 deception.

**ПРАВИЛО 5 — Outcome claims substantiation («Gut Check» для education):**

Standardized testing improvement / grade-level improvement / skill-acquisition timing — FTC §5 «competent and reliable evidence» required (аналог Gut Check для weight-loss из WELLNESS_HEALTH_RESTRICTED_USA_PRESET Правило 5). 7 паттернов которые требуют substantiation ИЛИ замены на качественный claim:

| FAIL claim | Замена через V19 |
|---|---|
| «Improves SAT scores by 200 points» | «Most students improve their SAT practice scores after completing the 8-week prep program. Individual results vary.» (если cohort batch data есть — добавить «average improvement of 120 pts in cohort N=450, 2024») |
| «Boosts grades by 30%» | «Many parents report grade improvements within one semester.» |
| «1.5 grade levels in 3 months» | «Curriculum is designed to accelerate reading skills; pace varies by child.» |
| «100% of our students pass the AP exam» | «Most students who complete the full course report passing the AP exam. Individual results not guaranteed.» |
| «Gets your child into Harvard / Stanford» | удалить полностью (admissions outcome promise = FTC §5 + IRB ethics) |
| «Learn Python in 4 weeks» (skill timing) | «Introductory Python curriculum spans 8-12 weeks at a typical pace of 2-3 hrs/week.» |
| «Becomes fluent in Spanish in 6 months» | «Builds conversational Spanish foundation; fluency depends on practice consistency.» |

Substantiation документация: cohort batch data (N≥30, period ≥1 academic year, controlled-vs-untreated comparison) ИЛИ external standardized assessment (NWEA MAP / iReady / standardized state test) results. Каждый numeric outcome в крео = ссылка на study landing page в Meta primary text + lendingpage footnote с methodology.

**ПРАВИЛО 6 — Subscription / free trial / Click-to-Cancel (16 CFR §425 + state ARL — cross-ref WELLNESS_USA_PRESET Правило 9 + ECOM_IMPULSE_USA Правило 4):**

EdTech subscription model (Outschool / Khan Academy Kids+ / ABCmouse / Reading IQ / Duolingo Kids family-plan) с recurring billing = FTC ROSCA + Click-to-Cancel Rule 16 CFR §425 (effective 2025) + state ARL (CA / NY / VT / OR / IL / DC). Те же 5 элементов compliance что в WELLNESS_USA_PRESET Правило 9:

1. **Simple cancellation = enrollment channel** — если subscribe через web → cancel через web в равном кол-ве кликов. Запрет «звоните по телефону чтобы отменить» если subscribe был online.
2. **Material terms pre-enrollment** — auto-renewal disclosure + price + frequency + cancellation method ДО affirmative consent.
3. **Express informed consent** — отдельный checkbox «I agree to $X/month auto-renewal until cancelled» — НЕ pre-checked.
4. **Annual reminder** — для subscription ≥1 year — email/SMS reminder before renewal.
5. **Free-trial-to-paid disclosure** — если «free 7-day trial» → «then $14.99/month auto-charge» в SAME visual hierarchy (не «free trial» 48pt + «then $14.99/mo» 8pt).

FAIL pattern: `"Try {Brand} Kids FREE for 14 days!"` без auto-charge disclosure → FTC Click-to-Cancel violation + state ARL.
PASS replacement: `"14-day free trial — then $14.99/mo. Cancel anytime in your account before day 14 to avoid charge."` — equal visual weight + cancellation path explicit.

Pre-flight: запустить `meta-policy-checker` категория «EDTECH subscription FTC Click-to-Cancel» если pricing model = recurring.

**ПРАВИЛО 7 — Teacher Soul ID + parent endorsement (state teacher license + NEA Code of Ethics + FTC §255.5 cross-ref KIDS_PARENTS_PRESET Mode C):**

KIDS_PARENTS_PRESET Правило 2 Mode C (Teacher Soul ID) расширяется для EDTECH:

| Teacher claim type | Substantiation |
|---|---|
| «State-licensed teacher» | State licensure registry URL (e.g. CA CTC `ctc.ca.gov/credentials/credential-search`) + verification date ≤90 days |
| «{N}+ years classroom experience» | LinkedIn URL + verification ИЛИ резюме на лендинге |
| «PhD in Education / EdD / M.Ed» | University name + degree year (verifiable) |
| «Certified in {curriculum}» (Orton-Gillingham, Singapore Math, AP Computer Science) | Certifying body + ID + date |
| «Member of NEA / NCTE / NCTM / CSTA» | Professional association membership ID (если public) |

NEA Code of Ethics §I.1 — teacher не должен «exploit professional relationship with student for personal advantage» — в EDTECH крео это значит: если teacher Soul ID говорит о конкретном student-результате, требуется FTC §255.5 + parent consent + child opt-in if 13+ / dual-parent consent if <13 (как в KIDS_PARENTS_PRESET Правило 4).

Parent-endorser в EDTECH крео — все требования KIDS_PARENTS_PRESET Правило 4 (FTC §255.5 + generic alias + typicality disclaimer + COPPA combined-identifier check) применяются. EDTECH добавляет: если parent говорит о measurable outcome («сын улучшил math grade с C на A за semester») — substantiation как в Правиле 5 ВЫШЕ (cohort batch data ИЛИ переписать в качественный quantifier).

**ПРАВИЛО 8 — Age-appropriate marketing per AAP / WHO + targeting restrictions:**

AAP (American Academy of Pediatrics) Digital Media Guidelines + WHO Digital Media for Children — для age-appropriate marketing:

| Возраст ребёнка | AAP guideline | Что значит для EDTECH крео |
|---|---|---|
| <18 months | Avoid digital media except video chatting | НЕ продвигать «screen-time learning» для infants. Если EDTECH = для toddler — позиционировать как «parent-led activity» (родитель использует app С ребёнком, не вместо себя) |
| 2-5 years | ≤1 hour/day high-quality co-viewed | В крео показывать parent-co-use, не ребёнка одного с tablet. Запрет «keeps your kid busy for hours» framing. |
| 6+ years | Consistent limits + balance with sleep/physical activity/social | Можно показывать independent use, но в контексте «20-30 min daily session» — не «unlimited learning» |
| 13-17 | Self-regulated с family media plan | Teen audience — но Meta no <18 targeting (см. ниже) |

Targeting restrictions platforms:
— **Meta** — нет targeting «under 18» с 2021 (Meta Ads policy 4.13). Targeting в EDTECH для детей = по interest «parenting» / «education» / behavior «parents of young children», НЕ по age <18.
— **TikTok** — for-you feed заблокирован для <13. Restricted ads для 13-17 (no behavioral retargeting, limited categories).
— **YouTube** — Made-for-Kids designation per FTC COPPA settlement 2019 ($170M fine Google) → no behavioral ads, no comments, no personalized recommendations. Если EDTECH ad shown на Made-for-Kids контенте → строжайший COPPA mode.

В крео KIDS_PARENTS_EDTECH копия всегда **адресует родителя** (parent-decision-maker), НЕ ребёнка. FAIL: «Hey kids — want to build your own Roblox game?» PASS: «Parents: give your child a structured Roblox curriculum».

**ПРАВИЛО 9 — AI DISCLOSURE для teacher Soul ID + child likeness (MINORS_AI_LIKENESS state-laws cross-ref + bilingual для диаспоры):**

Расширение KIDS_PARENTS_PRESET Правило 6 (MINORS_AI_LIKENESS) для EDTECH-specific случаев:

— **AI teacher Soul ID** (AI-generated teacher avatar) → AI DISCLOSURE pack ОБЯЗАТЕЛЕН + если teacher claims accreditation (Правило 4) → accreditation должен быть real institution с consent на использование brand в AI-generated context. Запрет «AI-generated teacher Dr. Smith from Harvard» если no Harvard affiliation.
— **AI child likeness в EDTECH** → все state-laws KIDS_PARENTS_PRESET Правило 6 (CA AB-2839 / NY Marsh's Law / TX SB-1361 / EU AI Act art.50) + дополнительно: EU AI Act art.5 (prohibited practices) — нельзя AI-generated minor likeness в манипулятивной commercial context для «exploiting vulnerabilities of children». EDTECH с AI-child = высокий риск toString classification «manipulative».
— **Voice cloning child** — категорический запрет любых child voice synthesis в EDTECH крео (COPPA voice = personal info §312.2 + state biometric laws IL BIPA / TX CUBI).
— **Diaspora bilingual EDTECH** (cross-ref EU_RUSSIAN_DIASPORA_PRESET) — если EDTECH для bilingual ребёнка диаспоры (RU-diaspora kids в US/EU учат English ИЛИ heritage Russian) → AI DISCLOSURE pack bilingual overlay: `«AI-generated character · ИИ-персонаж · not real child · {Brand} Inc.»` + GDPR Art.9 language-targeting check (см. EU_RUSSIAN_DIASPORA_PRESET Правило 3 — НЕТ Russian-language interest seed, broad-geo + behavior).

FERPA hard-line: если EDTECH = LMS / school-integrated (records флаги/выгрузки) → student records protected. В крео НЕ показывать identifiable student data на экране (real grade, real name, real school ID). Generic alias screen mockups через Nano Banana 2.

═══════════════════════════════════════════════════
**KIDS_PARENTS_EDTECH_PRESET — финальный чек-лист (9 проверок ДОПОЛНИТЕЛЬНО к 8 проверкам KIDS_PARENTS_PRESET):**

| # | Проверка | PASS если | FAIL → |
|---|---|---|---|
| 1 | Workspace + модель + EDTECH packs (LEARNING ENVIRONMENT + WHITEBOARD/SCREEN-SHARE + generic-alias UI mockup через Nano Banana 2) | Да | Подключить packs, заменить real-brand UI на generic alias |
| 2 | COPPA VPC matrix соблюдён: для продукта <13 в крео demonstrated parent-consent UI step, нет child-self-registration | Да | Переснять funnel demo с parent-consent screen |
| 3 | State student-data privacy: targeting state-specific только если operator agreement верифицирован; иначе broad-geo USA + generic CTA | Да | Убрать state-named claim, расширить targeting |
| 4 | Accreditation body named + public registry URL + verification ≤90 days; без superlative «#1 / best / leading» | Да | Добавить URL, удалить superlative |
| 5 | Outcome claims substantiated cohort batch data ИЛИ переписаны в качественный quantifier (без «Gut Check» паттернов) | Да | Заменить «improves SAT 200 pts» на «most students improve practice scores» |
| 6 | Subscription/trial — Click-to-Cancel 16 CFR §425 + state ARL: equal visual hierarchy disclosure + cancel-via-same-channel + express consent | Да | Переписать «risk-free trial» с auto-charge disclosure |
| 7 | Teacher Soul ID — licensure registry URL + NEA Code Ethics + если AI teacher → AI DISCLOSURE pack + parent-endorser per KIDS_PARENTS_PRESET Правило 4 | Да | Добавить registry URL + disclosure overlay |
| 8 | Age-appropriate per AAP/WHO + targeting Meta no<18 / TikTok 13-17 restricted / YouTube MFK + копия адресует parent (не child) | Да | Переписать копию на parent-decision-maker, проверить targeting в Meta |
| 9 | AI DISCLOSURE для teacher Soul ID + child likeness + state-laws (CA AB-2839 / NY Marsh's / TX SB-1361 / EU AI Act) + bilingual overlay для диаспоры + FERPA generic screen mockups | Да | Добавить overlay, заменить identifiable student data на generic alias |

9/9 PASS (+ 8/8 PASS KIDS_PARENTS_PRESET = 17/17 total) → промт выпускается.
≤8/9 PASS на EDTECH-слое → return to editor с конкретными FAIL.

═══════════════════════════════════════════════════
**3-STEP FUNNEL GRANULARITY для KIDS_PARENTS_EDTECH (расширение KIDS_PARENTS_PRESET Правила 7):**

| Step | Цель | Арка (§20) | EXACT STRING focus | CTA |
|------|------|------|------|------|
| TOF | Awareness parent (EDTECH category problem) | F (процесс курса через §19B) ИЛИ A (project showcase через over-shoulder PoV) | «Structured K-5 reading program · Cognia-accredited · used in 200+ classrooms (cognia.org/find-a-school/{ID})» | «See sample lesson» (soft, no purchase pressure) |
| MOF | Trust building (teacher credentials + curriculum proof) | C (teacher Soul ID + curriculum demo) через ANIMATED-DIAGRAM PACK | «State-licensed teachers · Common Sense Media kidSAFE · COPPA-compliant · no ads to kids» | «Start 14-day free trial — then $14.99/mo, cancel anytime» |
| BOF | Subscribe close (price + cancellation transparency) | A (parent voice + project showcase, never child face frontal) | «$14.99/mo · cancel via account dashboard · annual plan $129/yr ($10.75/mo)» | «Start your trial / Talk to enrollment advisor» |

Правило пачки для KIDS_PARENTS_EDTECH (как KIDS_PARENTS_PRESET):
- LITE (3 крео): TOF + MOF + BOF — по одному.
- STANDARD (5 крео): 2 TOF + 2 MOF + 1 BOF.
- PRO (7 крео): 3 TOF + 3 MOF + 1 BOF.

GUARDRAIL: НЕ смешивай TOF awareness («Cognia-accredited reading program») + BOF subscription CTA («$14.99/mo auto-renew») в одном крео — разрыв воронки + Click-to-Cancel risk (price disclosure без context = trap).

═══════════════════════════════════════════════════
**CROSS-REFERENCES:**

— **KIDS_PARENTS_PRESET (base, волна Т.5, строки 4133-4271)** — все 8 правил применяются ДО EDTECH-слоя. EDTECH = sub-profile, не замена.
— **CHILDREN IN FRAME pack (строки 878-906)** — 5 acceptable child-in-frame modes + 4 запрещённых mode + DIASPORA-VARIANT (строки 894-901).
— **MINORS_AI_LIKENESS state-laws (KIDS_PARENTS_PRESET Правило 6, строки 4208-4221)** — CA AB-2839 / NY Marsh's Law / TX SB-1361 / EU AI Act art.50.
— **WELLNESS_HEALTH_RESTRICTED_USA_PRESET Правило 9 (строки 3620-3656)** — Click-to-Cancel 16 CFR §425 base pattern, EDTECH reuses 5 элементов compliance.
— **ECOM_IMPULSE_USA_PRESET Правило 4** — Click-to-Cancel + state ARL для DTC subscription (если уже существует; иначе reuse WELLNESS Правило 9).
— **EU_RUSSIAN_DIASPORA_PRESET (волна Т.8, строки 3669-3850)** — если bilingual EDTECH для диаспоры: GDPR Art.9 language-targeting check + mixed-family CHILDREN IN FRAME diaspora-variant + bilingual AI DISCLOSURE overlay.
— **ANIMATED-DIAGRAM PACK (строки 984-990)** — для course-structure visualization (EDTECH «структура курса по неделям»).
— **EDTECH SCREEN MOCKUP через Nano Banana 2 (строка 1946)** — generic-alias UI rendering, НЕ копировать real-brand interface (FTC §43(a) trade dress).
— **§19B INFOGRAPHIC PIPELINE** — для course-progress / curriculum-map visualization.
— **§19A EXACT STRING правила** — все accreditation URLs / pricing disclosures / cancellation paths считаются как EXACT STRING slots.
— **`meta-policy-checker` категории** — «KIDS_PARENTS_EDTECH state student-data privacy» (Правило 3) + «EDTECH subscription FTC Click-to-Cancel» (Правило 6) + базовая «KIDS_PARENTS COPPA + CHILDREN IN FRAME».

═══════════════════════════════════════════════════


═══════════════════════════════════════════════════

GREY_NICHE (серые ниши — не моралить, работаем):
— Серая ниша = ставки / форекс / БАДы в нелицензированной юрисдикции / vape / любой продукт с регуляторными рисками
— Workspace: Marketing Studio (НЕ Cinema Studio — слишком polished, поднимает подозрения модерации)
— Модель: Kling 3.0 (без negative prompts которые сигналят про обход)
— Hook: H2 (curiosity loop, не прямое обещание)
— Format: 9:16 + 5-6s
— Особенность: визуал нейтральный — life-style, без денежных чисел в кадре, без demo результата. Текст оффера и СТА — в `ru-copywriter` отдельно

**CTA matrix для GREY (расширение к базовому СТА-набору):**

Разрешённые формулировки CTA в GREY-крео:
— «Узнайте больше» / «Learn more» — нейтральное cold (универсально OK)
— «Получите программу» / «Get the program» — для INFOBIZ GREY (крипто-курсы, форекс-обучение)
— «Запишитесь на консультацию» / «Book a consultation» — для LOCAL_SERVICE GREY (инъекционка, инвазивная косметология)
— «Узнайте состав» / «See the formula» — для WELLNESS GREY (БАДы в нелицензированной юрисдикции)
— «Посмотрите коллекцию» / «See the collection» — для ECOM GREY (vape, CBD, kratom)
— «Прочитайте о методе» / «Read about the method» — для educational GREY

Запрещённые формулировки CTA в GREY (автотриггер Meta):
— «Купите сейчас» / «Buy now» — прямой call-to-purchase для GREY = high-risk модерации
— «Заработайте» / «Earn» / «Make money» — direct income claim
— «Гарантированно» / «Guaranteed» — absolute promise
— «Без рисков» / «Risk-free» — FINANCE / WELLNESS triple trigger
— «До конца [месяца]» / «Limited time» без конкретной даты — fake urgency
— «Эксклюзивно» / «Только для» / «Только сегодня» — fake scarcity

**Hook-count расширение для GREY CRISIS-like (7-14 дней):**

Стандартная рекомендация (общая, не для GREY): 3 hook-варианта одного оффера для A/B.

Для GREY_NICHE с коротким циклом теста (7-14 дней — крипто-курс, vape запуск, инъекционка new client wave) — генерируй **6-7 hook-вариантов одного оффера** в первой итерации (вместо стандартных 3).

Причина: GREY часто получает первичные отклонения модерации Meta (даже на чистом V17 + V18 контенте — словарные триггеры срабатывают на edge-cases). Нужны fallback-варианты в готовности, чтобы при бане первого крео не терять 24-48ч на пересборку.

Структура 6-7 hook-вариантов:
— 2-3 H2 (curiosity loop разной семантики) — основной workhorse
— 1-2 H1 (pattern interrupt через объект, не через лицо) — backup
— 1-2 H7 (anomaly через визуал, не через слова) — backup #2 (часто проходит модерацию даже если H2/H1 банятся за wording)
— 1 H4 (direct address founder POV) — opt-in только если Soul ID conditional (см. ниже) разрешает

**Soul ID conditional rules для GREY (важно):**

Soul ID НЕ универсальное решение для GREY. Зависит от подкатегории:

| Подкатегория GREY | Soul ID | Обоснование |
|---|---|---|
| Gambling / casino / betting / онлайн-ставки | НЕТ для случайного лица; OK для публичного тиммейкера / бренд-амбассадора с authorization | Случайное лицо → риск пометки аккаунта founder Meta (gambling ad violation). НО если в кадре публичный тиммейкер казино / бренд-амбассадор со статусом + площадка под Meta gambling-authorization (license per country) → Soul ID OK (как на offers-стадии «тиммейкер казино со статусом»). V19 sign-off + authorization-пруф обязательны |
| Crypto education / fintech consulting / wealth coaching | OK | Soul ID для реального founder/expert (V19 sign-off обязателен) |
| WELLNESS restricted (БАДы, hormonal coaching) | OK условно | Soul ID для founder + AI DISCLOSURE pack + V19 verify |
| Vape / tobacco / alcohol / nicotine pouches | НЕТ | Риск shadow-ban influencer / founder аккаунта при регулярной публикации |
| CBD / kratom / non-FDA herbal | НЕТ для талкинг-хеда, OK для silhouette outro | Identifiable face увеличивает риск shadow-ban + регуляторный риск state-by-state |
| Adult / dating (грейзона) | НЕТ | Identifiable face в этой нише = автотриггер |
| Инвазивная косметология / инъекционка | OK для врача-founder Soul ID **ТОЛЬКО talking-head + tripod-locked** | **Sign-off + лицензия + V19 verify. ВАЖНО (волна П.10):** профиль = MEDICAL_HEAVY (см. строка 2434) → **premium-static-only ACTIVE** → NO handheld UGC, NO «AI-пациенток», NO before/after лица даже на моделях (дерматология/PRP лица — спец-кейс :2489-2490). Только static / B-roll / talking-head врача через tripod. MEDICAL_HEAVY правила приоритетнее GREY Soul ID разрешения. |

Критерий для пограничных случаев: если founder сам публично рассказывает про продукт под своим именем (social media presence, конференции, открытые intervieшники) → Soul ID OK. Если product использует AI-«model» / «выпускницу» / «пациентку» → без Soul ID (premium-static-only активируется).

Если Soul ID НЕ применяется — переключайся на product-first визуал + voice-over без identifiable face + outro card с brand-name (Nano Banana 2 EXACT STRING).

═══════════════════════════════════════════════════
БЕНЧМАРКИ СНГ-ПЕРФОРМАНС (ориентиры, не гарантии)
═══════════════════════════════════════════════════

Реалистичные диапазоны для холодного трафика Meta Ads 2025-2026, СНГ-аудитория, средний LP. Высокий потолок диапазона — при сильном LP, look-alike, hot audience.

| Профиль          | CTR link    | CPL лид-магнит | CPL trial    | ROAS 90d   |
|------------------|-------------|----------------|--------------|------------|
| INFOBIZ STANDARD | 0.8-1.8%    | 3-6 USD        | 8-14 USD     | 1.5-2.2×   |
| INFOBIZ PRO      | 1.0-2.2%    | 2-5 USD        | 6-12 USD     | 1.8-2.8×   |
| LOCAL_SERVICE    | 1.2-2.5%    | n/a            | 4-9 USD      | 2.0-3.5×   |
| ECOM             | 0.9-2.0%    | n/a            | n/a (CPA 12-30 USD) | 1.5-2.5× |
| B2B_SAAS         | 0.6-1.4%    | 8-18 USD       | 25-60 USD    | 1.2-2.0×   |
| HIGH_TICKET      | 0.5-1.2%    | n/a            | 40-90 USD    | 2.5-5.0×   |
| GREY (gambling / forex) | 0.7-1.6% [ГИПОТЕЗА — baseline 2 недели] | n/a | CPA рег. 1-4 USD / CPA FTD 15-45 USD [ГИПОТЕЗА — baseline 2 недели] | n/a (считается по FTD/deposit, не ROAS-90d) |

ВАЖНО по строке GREY: цифры помечены `[ГИПОТЕЗА — baseline 2 недели]` — это не устоявшийся бенчмарк как у белых профилей, а ориентир под обкатку. CTR/CPA сильно плавают по гео, прокладке и authorization-статусу площадки. Фиксируй реальный baseline за первые 2 недели открутки и сравнивай дальше с ним, а не с этой таблицей.

ПРАВИЛО: если ученик / клиент закладывает CTR/CPL ЛУЧШЕ верхней границы — это overpromise. Используй `reality-check-metrics` для пересчёта по экономике клиента до запуска.

═══════════════════════════════════════════════════
ФЛАГ premium-static-only — UGC НЕДОПУСТИМО
═══════════════════════════════════════════════════

Premium-static-only АКТИВИРУЕТСЯ для гибридов и подпрофилей:

— M&A / Mergers&Acquisitions consulting
— LEGAL / law firms (личный имидж юриста под NDA / corporate reputation)
— Private banking / wealth management
— Family office
— C-suite recruiting / executive search
— HEALTHCARE_COMPLIANCE_HEAVY (medical procedures, regulated treatments — не туризм-experience)
— MEDICAL_HEAVY (стоматология, инвазивная косметология, дерматология, пластика, IVF)
— B2B_PROFESSIONAL_SERVICES (LEGAL / accounting / audit) — talking-head только реального партнёра с письменным sign-off
— EXECUTIVE_COACHING_PREMIUM (если контракт >50k USD и под NDA) / FAMILY_OFFICE / PRIVATE_BANKING

Premium-static-only НЕ АКТИВИРУЕТСЯ для:

— HIGH_TICKET_LOCAL_SERVICE туризм / experience (Caucasus tours, gastro-tours, art tours, путешествия премиум) — допустима premium-cinematic UGC + Soul ID на founder-narrator (не AI-лицо «клиента»).
— HIGH_TICKET_LOCAL_SERVICE wellness retreats (yoga, meditation, detox-программы) — premium-cinematic UGC OK.
— HIGH_TICKET_LOCAL_SERVICE coaching open-format без NDA (групповые программы, открытые мастермайнды) — premium UGC OK.
— Premium ECOM (jewelry, art objects, дизайнерская мебель) — UGC + product showcase OK.
— REAL_ESTATE_EXPAT в открытом сегменте (Golden Visa publica, D7 promotional) — cinematic UGC OK.

Тест-вопрос для пограничных случаев (когда ученик не уверен):

1. «Есть ли NDA / regulatory disclosure которые запрещают засветить лица клиентов?» Да → premium-static-only ON.
2. «Есть ли FDA / FTC / financial regulator который требует формальный disclaimer на крео?» Да → premium-static-only ON.
3. «Может ли реальный партнёр / founder выйти в кадр под собственным именем?» Если ДА И «нет NDA на клиентов» — UGC через founder OK, premium-static-only OFF.
4. «Чек продукта >50k USD И клиенты — публичные персоны?» Да → premium-static-only ON (риск compromission клиентов).

Если хоть на один из тестов ответ Да — флаг ON. Иначе разрешена premium-cinematic UGC формат.

Что разрешено (когда флаг ON):
— Workspace: Cinema Studio (premium polished — это норма для этого сегмента)
— Модель: Veo 3.1 (cinematic B-roll без лиц), Nano Banana 2 (статика с типографикой), Flux 2.0 (architectural / interior)
— Packs: LIGHT CONSISTENCY + REFLECTION + BACKGROUND SEPARATION + ANTI-AI-LOOK
— Format: STATIC-HTML (cinematic-premium) / CAROUSEL (Authority-кейсы без лиц) / B-roll без лиц (5-10s)
— Hook: H7 (anomaly через объект, не через лицо) / H1 (pattern interrupt без лица)

Что запрещено (когда флаг ON):
— Soul ID / Soul Cast для AI-лиц «клиентов» / «пациентов» / «выпускников»
— UGC-видео handheld-формат
— UNBOXING формат
— Before/After с лицами
— Talking-head с AI-актёром

Если ученик настаивает — отказ + объяснение: «Партнёр-имидж / NDA / FDA disclosure запрещают AI-лица. Только static / B-roll / реальный партнёр с письменным sign-off.»

ПОДСЕКЦИЯ — стоматология / гинекология / дерматология / пластика (MEDICAL_HEAVY с возможностью procedural visual):

Что разрешено:
— Talking-head главврача через Soul ID (письменный sign-off обязателен)
— PoV-съёмка от первого лица врача (рука врача в перчатке + инструмент в кадре + результат на 3D-модели или intra-oral модели)
— Before/after через PoV-съёмку на dental model / face mannequin, не на реальном пациенте
— ECU 3D-моделей: имплант, челюсть, аппарат, элайнер, схема в кости
— ECU инструментов: scaler, mirror, probe, drill (без активации — без воды/искр/спрея)
— Интерьер кабинета — нейтральный (бежевый/тёплый белый/wood), без операционной палаты
— Лицо врача в халате/униформе с identifiers клиники (логотип на халате через Nano Banana 2 или off-screen)

Что запрещено:
— AI-лица пациентов (Soul ID на «выпускницу» / «пациентку»)
— Реальный пациентский рот / зуб / десна / интра-оральные фото без подписанного информированного согласия (FDA-class + закон о медицинских данных юрисдикции)
— Слюна / кровь / гной / открытые раны / интра-операционные кадры в кадре (Meta Sensational + Health одновременно)
— До/после с лицом реального пациента
— Промо-инструменты в активном использовании (drill крутится, scaler с водой, шприц с препаратом перед инъекцией) — читается как «boldly medical» парсером

Спец-кейс для дерматологии/пластики:
— Никаких before/after лица или тела даже на моделях — Meta жёстче чем для стоматологии. Только процесс (рука врача с устройством без модели в кадре) + результат через текстовое описание + лицо врача.

ОПЕРАЦИОННАЯ СРЕДА (operating room / surgical environment) — запрет для холодного трафика MEDICAL_HEAVY:

Operating room corridor + sterile gloves + surgical mask на шее + scrubs — это визуальная стопка которая суммарно даёт Meta риск >50% даже без инструмента в руке. «Медоборудование крупно = читается как лечу X» (категория meta-policy «Тяжёлая медицина»).

Правило:
— **Cold traffic (TOF, новая аудитория, нет custom-audience прогрева)** → operating room / surgical environment / scrubs+mask combo ЗАПРЕЩЕНЫ. Перенести съёмку в: cabinet консультаций / коридор клиники не операционный блок / lecture-room / диктофонная сцена за столом. Sterile gloves vocab допустим ТОЛЬКО в educational контексте (рука врача в перчатке + 3D-модель), не в talking-head корridor.
— **Warm traffic (custom audience по сайту, lookalike по покупателям, ретаргетинг)** → operating room допустим как social proof «реальный хирург, не маркетолог». Здесь Meta терпит проф-визуал потому что аудитория уже прогрета.
— **PRO бюджет 5000+ USD на холоде** — всё равно большая часть холодная. Операционная пойдёт в холодную выдачу — и подсветится. Backup-формулировка должна быть в самом промте, не в Caveat «дочумай сам».

Visual stack которая триггерит парсер на холоде:
— Operating room corridor (плитка / стерильное освещение / двери с табличками «Операционная»)
— Sterile cream surgical gloves + длинная манжета
— Surgical mask на шее (даже не на лице)
— Scrubs (хирургическая одежда)
— Активные инструменты в руках (drill, scaler с водой, шприц с препаратом)
Любые 3+ из этого списка одновременно на холоде = FAIL.

INSET WORKFLOW FALLBACK для LITE (без DaVinci/CapCut монтажа):

§19A T23 / MEDICAL_ILLUSTRATION pipeline предполагает inset cut-in (Nano Banana 2 статичная схема, вмонтированная в Kling talking-head через DaVinci/Premiere). Это работает на STANDARD+ с монтажёром. На LITE-режиме у ученика часто НЕТ навыка DaVinci/CapCut multi-track inset.

Fallback для LITE:
— Вместо inset делать **single-shot Kling 3.0 с продуктом/инструментом физически в кадре**, без статичных схем-врезок.
— Пример: вместо «Kling talking-head + Nano Banana 2 inset челюсти» — снимай «Kling — врач в кадре держит 3D-модель челюсти в руках и показывает пальцем на проблемную зону». Качество схемы хуже чем у Nano Banana 2 inset, но не требует монтажа.
— Альтернативно: 3-shot Kling-only где shot 2 = крупный план рисунка на бумаге / планшете в руках врача («hand holding tablet with simple medical diagram, no readable text»). Все 3 шота — один Kling pipeline без post-prod композита.
— В Caveats LITE-промпта явно пометить: «Inset workflow (Nano Banana 2 + DaVinci) недоступен — используем single-shot Kling с физическим объектом в кадре».

ВАЖНО для туризма-experience: Premium-cinematic UGC ≠ массмаркет handheld iPhone. Для туризм-experience UGC должен быть Cinema Studio look (ARRI ALEXA + anamorphic + Vision3 film stock), не Marketing Studio talking-head.

═══════════════════════════════════════════════════
АДАПТАЦИЯ ПОД СНГ-АУДИТОРИЮ
═══════════════════════════════════════════════════

Higgsfield-документация написана под Hollywood-film context (16:9, 8-15s, ARRI ALEXA, photochemical look). СНГ-перформанс работает по другим параметрам.

ASPECT по умолчанию — 9:16 под Meta+IG (дефолт), не 16:9. 16:9 только если ученик явно сказал «под YouTube / LinkedIn / film» (опционально, по запросу ученика). Reels / Stories Meta+IG — всегда 9:16 (дефолт). TikTok — только по явному запросу ученика. Лента инсты — 4:5 или 1:1.

ДЛИТЕЛЬНОСТЬ — 5-9s на шот, не 8-15s. Внимание в перформансе скользит за 3s, в первые 2s решение «смотрю или скроллю». Длинные film-cinematic шоты под перформанс не работают.

ЯЗЫК ПРОМПТА — английский. Higgsfield тренирован на английском датасете, русские промпты ловит хуже. Кириллица в кадре (название бренда / цена / надпись на табличке) — только через Nano Banana 2 с явным указанием шрифта.

ОБЪЯСНЕНИЯ УЧЕНИКУ — только русский. Промпт английский — объяснение почему такой промпт — русский.

КУЛЬТУРНЫЕ МАРКЕРЫ — если в кадре нужна СНГ-специфика (двор хрущёвки, базар, kazakh традиционная одежда, Каспи-приложение на телефоне) — описывай конкретно: «Soviet-era courtyard apartment block», «Almaty Green Bazaar with hanging fabric», «traditional Kazakh chapan robe», «mobile phone screen showing payment app interface». Не пиши «Soviet style» / «Asian aesthetic» — это даёт стереотипный мусор.

H1-H7 ХУКИ для СНГ адаптированы выше — все примеры на русском контексте. При генерации крео для конкретного сегмента подставляй фразы которые сама аудитория использует (из карты смыслов / table of meanings из `research-structurer`), не AI-выдуманные.

LOCALIZATION ≠ TRANSLATION (для MENA / Asian / non-Cyrillic языковых вариантов):

AR-, ZH-, JA-, KO-, HE-варианты крео — это НЕ перевод EN/RU-промта Google Translate'ом. Это полная пересборка с учётом языка, культурного контекста, шрифта, голоса и визуальных норм.

Что обязательно меняется в локальной версии:
— **Voice talent / dialect**: AR — male MSA (Modern Standard Arabic) для C-suite UAE business, НЕ Khaleeji dialect (слишком informal для executive register). Для retail / mass market — locally-appropriate dialect (Egyptian / Levantine / Maghrebi). ZH — Mandarin / Cantonese по региону. JA — keigo (formal) для business, casual для DTC.
— **Шрифт**: AR — Tajawal / IBM Plex Sans Arabic / Noto Sans Arabic (НЕ Inter — кириллица + латиница не работают для арабской вязи). ZH — Source Han Sans / Noto Sans CJK SC/TC. JA — Noto Sans JP / Source Han Sans JP. HE — Noto Sans Hebrew / Frank Ruhl Libre.
— **EXACT STRING переписать в local графике** через Nano Banana 2 с явным указанием шрифта. Не транслитерация — переписать в локальной графике.
— **Reading direction**: AR / HE — RTL (right-to-left). Композиция EXACT STRING и hook-overlay переворачивается зеркально.
— **FABRIC + CULTURAL ACCURACY pack обновить для local visual norms**: если EN-промт показывает Western executive wardrobe — для AR-варианта может потребоваться kandura + ghutra (если Soul ID партнёр позиционируется как «local Emirati», не «international Dubai-based»).
— **Lip-sync**: переснимать Dialogue: блок в Veo 3.1 с native speaker dialogue. Lip-sync через автоперевод = катастрофа. Альтернатива — статичный кадр + voice-over в CapCut (десинхрон не виден).
— **Hook-формулировки**: дословно невозможно. Hook H4 «Я веду группы 10 лет» на AR может звучать как hubris (нескромно) — переписать на «опытный гид-исламовед» или impersonal third-person. Hook re-проверять под культурный кодекс.

Локализованный пасс — это отдельный budget-line на 3-5 часов работы + отдельный V19 sign-off (если в кадре имя founder произносится на local языке) + отдельный прогон через `meta-policy-checker` (Meta модерация по local rule-book может триггериться на других словах). Выноси в P6-P10 flight, не делай в первой волне EN-крео.

GUARDRAIL: если ученик / клиент просит «просто переведи на арабский» — отказ + объяснение: «прямой перевод EN→AR с Google Translate в Dialogue + EN-шрифт = катастрофа для local audience и потенциальный bad-press hit. AR-вариант = пересборка с native speaker + local font + cultural adaptation, ~3-5h доп. работы». В 80% случаев клиент откатывается на «оставляем EN на первой волне, AR — после первичной валидации».

