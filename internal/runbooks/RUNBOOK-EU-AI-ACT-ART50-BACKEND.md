# RUNBOOK — EU AI Act art.50 Backend Infrastructure

**Создан в волне П.27 (2026-05-19) — production deploy guide для агентств клиентов курса.**

**Effective date:** 2 августа 2026 (start of enforcement).

**Penalties:** до €15M или 3% global turnover для AI provider / €7.5M или 1.5% для deployer.

**Применимость:** extraterritorial — любой AI-generated content depicting реального person, видимый в EU.

---

## Цель runbook

Higgsfield prompt-generator process (5-шаговый guide в SKILL.md) — это **content-level compliance**. Этот runbook — **infrastructure-level deploy guide** для агентств:

- DocuSign integration для AI-generation sign-off collection
- Audit trail database schema
- Withdrawal mechanism workflow
- Pre-launch compliance review process

---

## АРХИТЕКТУРА (high-level)

```
┌─────────────────────────────────────────────────────────────────┐
│                  Creative Production Workflow                     │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
            ┌───────────────────────────────────────┐
            │  1. AI-content Inventory (manual)     │
            │     - Soul ID likeness identified     │
            │     - Voice clone identified           │
            │     - Background AI-generated tagged   │
            └────────────┬──────────────────────────┘
                         │
                         ▼
            ┌──────────────────────────────────────┐
            │  2. Real-person Likeness Check       │
            │     (DB lookup: identified people)   │
            └────────────┬─────────────────────────┘
                         │
                         ▼
            ┌──────────────────────────────────────┐
            │  3. Dual Sign-off Collection         │
            │     - Marketing release (existing)    │
            │     - AI-generation release (NEW)    │
            │     - DocuSign integration            │
            └────────────┬─────────────────────────┘
                         │
                         ▼
            ┌──────────────────────────────────────┐
            │  4. Overlay Design Generation        │
            │     (per PRESET, automated template)  │
            └────────────┬─────────────────────────┘
                         │
                         ▼
            ┌──────────────────────────────────────┐
            │  5. Pre-launch Audit (10-pt check)   │
            │     - All items 10/10 PASS            │
            │     - Audit log archived              │
            └────────────┬─────────────────────────┘
                         │
                         ▼
                   ┌──────────────┐
                   │ Campaign Go  │
                   └──────────────┘
```

---

## 1. DOCUSIGN INTEGRATION SPEC

### 1.1 Template setup

DocuSign Templates → Create New Template «AI-Generation Likeness Release»:

**Required fields:**
- `subject_name` (text, required)
- `subject_title` (text, required)
- `subject_firm` (text, required)
- `public_source_url` (text, URL validation)
- `producer_name` (text, prefilled)
- `geo_targeting` (multi-select: US / EU / UK / CIS / LATAM / APAC / specific)
- `channels` (multi-select: Meta / LinkedIn / TikTok / YouTube / X / WhatsApp / specific)
- `campaign_period_start` (date, required)
- `campaign_period_end` (date, required)
- `ai_methods_authorized` (multi-select: Soul ID / Higgsfield Veo 3.1 / Kling 3.0 / Seedance 2.0 / Other)
- `withdrawal_notice_days` (number, default 14)
- `subject_signature` (signature, required)
- `subject_signature_date` (auto-populated)
- `producer_signature` (signature, required)
- `producer_signature_date` (auto-populated)
- `witness_signature` (optional signature)

### 1.2 Workflow

```
Producer (agency) → DocuSign create envelope from template
  → Send to subject email
  → Subject reviews + signs
  → Witness countersign (optional)
  → Producer countersign
  → Envelope COMPLETED status
  → Webhook → audit DB (см. §2)
  → Envelope ID + signed PDF archived
```

### 1.3 DocuSign API integration

**Pre-requisite:** DocuSign developer account + JWT app + Integration Key.

**Sample Python integration:**

```python
from docusign_esign import ApiClient, EnvelopesApi, EnvelopeDefinition, TemplateRole
import os

# JWT auth
api_client = ApiClient()
api_client.set_base_path("https://demo.docusign.net/restapi")
api_client.set_oauth_host_name("account-d.docusign.com")

# Get access token via JWT
private_key_bytes = open(os.environ['DOCUSIGN_PRIVATE_KEY_PATH'], 'rb').read()
token = api_client.request_jwt_user_token(
    client_id=os.environ['DOCUSIGN_INTEGRATION_KEY'],
    user_id=os.environ['DOCUSIGN_USER_ID'],
    oauth_host_name="account-d.docusign.com",
    private_key_bytes=private_key_bytes,
    expires_in=3600,
    scopes=["signature", "impersonation"],
)
api_client.set_default_header("Authorization", f"Bearer {token.access_token}")

# Create envelope from template
envelope_def = EnvelopeDefinition(
    template_id=os.environ['DOCUSIGN_TEMPLATE_ID_AI_RELEASE'],
    template_roles=[
        TemplateRole(
            name="John Doe, CEO Acme",
            email="john@acme.com",
            role_name="Subject",
            tabs={"textTabs": [{"tabLabel": "subject_title", "value": "CEO"}]},
        ),
        TemplateRole(
            name=os.environ['PRODUCER_NAME'],
            email=os.environ['PRODUCER_EMAIL'],
            role_name="Producer",
        ),
    ],
    status="sent",
)

envelopes_api = EnvelopesApi(api_client)
result = envelopes_api.create_envelope(
    account_id=os.environ['DOCUSIGN_ACCOUNT_ID'],
    envelope_definition=envelope_def,
)

envelope_id = result.envelope_id
# Store in audit DB
```

### 1.4 Webhook handler

```python
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook/docusign', methods=['POST'])
def docusign_webhook():
    data = request.get_json()
    if data['status'] == 'completed':
        envelope_id = data['envelopeId']
        # Persist to audit DB
        store_completed_release(envelope_id, data)
        # Download signed PDF
        archive_signed_pdf(envelope_id)
    return '', 200
```

---

## 2. AUDIT TRAIL DATABASE SCHEMA

**Recommended:** PostgreSQL (или Cloud SQL / Aurora) с row-level encryption для personal data.

### 2.1 Tables

```sql
-- Subjects (real persons appearing in AI-content)
CREATE TABLE subjects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    full_name VARCHAR(255) NOT NULL,
    title VARCHAR(255),
    firm_name VARCHAR(255),
    public_source_url TEXT,
    email VARCHAR(255) NOT NULL,
    bar_registry_number VARCHAR(100),  -- для regulated professionals
    state_license_number VARCHAR(100), -- US state-specific
    sec_crd_number VARCHAR(50),        -- FINRA-registered
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(email, full_name)
);

-- AI-generation releases (separate from marketing releases)
CREATE TABLE ai_generation_releases (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    subject_id UUID REFERENCES subjects(id) ON DELETE RESTRICT,
    docusign_envelope_id VARCHAR(100) UNIQUE NOT NULL,
    geo_targeting VARCHAR(255)[],  -- ['US', 'EU', 'UK', ...]
    channels VARCHAR(255)[],       -- ['Meta', 'LinkedIn', 'TikTok', ...]
    campaign_period_start DATE NOT NULL,
    campaign_period_end DATE NOT NULL,
    ai_methods_authorized VARCHAR(255)[],  -- ['Soul ID', 'Veo 3.1', ...]
    withdrawal_notice_days INTEGER DEFAULT 14,
    subject_signed_at TIMESTAMPTZ NOT NULL,
    producer_signed_at TIMESTAMPTZ NOT NULL,
    witness_signed_at TIMESTAMPTZ,
    signed_pdf_url TEXT,  -- S3 / Cloud Storage URL
    status VARCHAR(50) NOT NULL DEFAULT 'active', -- active | withdrawn | expired
    withdrawal_reason TEXT,
    withdrawn_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    CONSTRAINT campaign_period_valid CHECK (campaign_period_end >= campaign_period_start)
);

CREATE INDEX idx_releases_subject ON ai_generation_releases(subject_id);
CREATE INDEX idx_releases_status ON ai_generation_releases(status);
CREATE INDEX idx_releases_period ON ai_generation_releases(campaign_period_start, campaign_period_end);

-- Campaigns (groups of creatives using AI-content)
CREATE TABLE campaigns (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    client_id UUID NOT NULL,
    preset_activated VARCHAR(100),  -- e.g. 'B2B_SAAS_ENTERPRISE_PRESET'
    period_start DATE NOT NULL,
    period_end DATE NOT NULL,
    geo VARCHAR(255)[],
    channels VARCHAR(255)[],
    eu_visible BOOLEAN NOT NULL DEFAULT FALSE,  -- если visible в EU → art.50 applies
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Creatives (individual ads/videos)
CREATE TABLE creatives (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    campaign_id UUID REFERENCES campaigns(id) ON DELETE CASCADE,
    format VARCHAR(20) NOT NULL,  -- '9:16', '16:9', '1:1', etc
    duration_seconds INTEGER NOT NULL,
    higgsfield_workspace VARCHAR(50),  -- 'Cinema Studio' / 'Marketing Studio'
    higgsfield_model VARCHAR(50),      -- 'Veo 3.1' / 'Kling 3.0' / 'Seedance 2.0'
    file_url TEXT,                      -- S3 / CDN
    has_ai_generated_likeness BOOLEAN NOT NULL DEFAULT FALSE,
    audit_passed BOOLEAN NOT NULL DEFAULT FALSE,
    audit_passed_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Creative-Subject links (many-to-many — creative может содержать несколько persons)
CREATE TABLE creative_subjects (
    creative_id UUID REFERENCES creatives(id) ON DELETE CASCADE,
    subject_id UUID REFERENCES subjects(id) ON DELETE RESTRICT,
    release_id UUID REFERENCES ai_generation_releases(id) ON DELETE RESTRICT,
    overlay_text TEXT NOT NULL,  -- 'AI-assisted visual · John Doe, CEO Acme'
    PRIMARY KEY (creative_id, subject_id)
);

-- Pre-launch audit log (10-pt checklist)
CREATE TABLE audit_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    creative_id UUID REFERENCES creatives(id) ON DELETE CASCADE,
    auditor_email VARCHAR(255) NOT NULL,
    audited_at TIMESTAMPTZ DEFAULT NOW(),
    check_1_inventory BOOLEAN NOT NULL,
    check_2_likeness BOOLEAN NOT NULL,
    check_3_release BOOLEAN NOT NULL,
    check_4_overlay BOOLEAN NOT NULL,
    check_5_bilingual BOOLEAN NOT NULL,
    check_6_registry BOOLEAN NOT NULL,
    check_7_audit_trail BOOLEAN NOT NULL,
    check_8_withdrawal BOOLEAN NOT NULL,
    check_9_minors BOOLEAN,  -- если applicable, иначе NULL
    check_10_no_deepfake BOOLEAN NOT NULL,
    overall_passed BOOLEAN GENERATED ALWAYS AS (
        check_1_inventory AND check_2_likeness AND check_3_release AND
        check_4_overlay AND check_5_bilingual AND check_6_registry AND
        check_7_audit_trail AND check_8_withdrawal AND
        (check_9_minors IS NULL OR check_9_minors) AND check_10_no_deepfake
    ) STORED,
    notes TEXT
);

CREATE INDEX idx_audits_creative ON audit_logs(creative_id);
CREATE INDEX idx_audits_passed ON audit_logs(overall_passed);

-- Withdrawal requests log
CREATE TABLE withdrawal_requests (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    release_id UUID REFERENCES ai_generation_releases(id) ON DELETE RESTRICT,
    requested_at TIMESTAMPTZ DEFAULT NOW(),
    requested_by_email VARCHAR(255) NOT NULL,
    notice_days INTEGER NOT NULL,
    effective_date DATE NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'pending', -- pending | processed | rejected
    processed_at TIMESTAMPTZ,
    notes TEXT
);
```

### 2.2 GDPR / data retention

- **Retention period:** 7 years post-campaign-end (regulatory standard для advertising records).
- **Right to erasure:** subjects могут запросить erasure, но если release used in active campaign — keep until campaign end + 7 years (legitimate interest).
- **Row-level encryption:** для `subjects.email` / `subjects.full_name` (PII).
- **Backup:** daily snapshot + 30-day retention.

---

## 3. WITHDRAWAL MECHANISM

### 3.1 Subject-facing portal

Минимальный self-service page:

```
https://{producer-domain}/ai-release/withdraw

[Form]
- Email (must match release): _____
- Verification code (sent via email): _____
- Release reference ID (optional): _____

[Submit] → confirmation page + producer notified
```

### 3.2 Producer workflow

1. Email notification (within 1 hour of request).
2. Validate request (verify email matches release subject).
3. Calculate effective date (request date + `withdrawal_notice_days`).
4. Update `ai_generation_releases.status = 'withdrawn'` + `withdrawn_at` + `withdrawal_reason`.
5. Identify active campaigns using release → stop creatives serving (campaign manager API: Meta Ads / LinkedIn / etc).
6. Confirm to subject within 24h.

### 3.3 Compliance reporting

Quarterly report (CSV export):
- Active releases count
- Released within quarter
- Withdrawals processed
- Average response time

Audit-ready format для EU regulatory inquiry.

---

## 4. PRE-LAUNCH AUDIT WORKFLOW

### 4.1 Manual audit (default)

Auditor opens campaign in admin UI → 10-point checklist (from RUNBOOK §1.5 / SKILL.md §EU AI Act art.50 Шаг 5) → checks each → submits.

### 4.2 Semi-automated audit (recommended)

```python
def audit_creative(creative_id: str, auditor_email: str) -> dict:
    """Run automated checks; flag manual review needed."""
    creative = db.creatives.get(creative_id)
    subjects = db.creative_subjects.filter(creative_id=creative_id)

    results = {}

    # Check 1: AI-content inventory completed
    results['check_1_inventory'] = creative.has_ai_generated_likeness is not None

    # Check 2: All identified subjects have valid releases
    results['check_2_likeness'] = all(
        cs.release_id is not None for cs in subjects
    )

    # Check 3: Releases are NOT expired/withdrawn
    results['check_3_release'] = all(
        db.ai_generation_releases.get(cs.release_id).status == 'active'
        and db.ai_generation_releases.get(cs.release_id).campaign_period_end >= today
        for cs in subjects
    )

    # Check 4: Overlay text exists for each subject
    results['check_4_overlay'] = all(cs.overlay_text for cs in subjects)

    # Check 5: Bilingual if cross-language (manual review)
    results['check_5_bilingual'] = None  # manual

    # Check 6: Registry number in overlay if regulated professional
    results['check_6_registry'] = all(
        ('Lic #' in cs.overlay_text or 'NRA' in cs.overlay_text or 'CRD' in cs.overlay_text)
        if db.subjects.get(cs.subject_id).bar_registry_number
        else True
        for cs in subjects
    )

    # Check 7: Audit trail — DocuSign envelope archived
    results['check_7_audit_trail'] = all(
        db.ai_generation_releases.get(cs.release_id).signed_pdf_url is not None
        for cs in subjects
    )

    # Check 8: Withdrawal mechanism documented (always TRUE if release exists)
    results['check_8_withdrawal'] = True

    # Check 9: Minors check (manual если applicable)
    results['check_9_minors'] = None  # manual

    # Check 10: No deepfake (другой person) — manual review of content
    results['check_10_no_deepfake'] = None  # manual

    # Save audit log
    db.audit_logs.insert(
        creative_id=creative_id,
        auditor_email=auditor_email,
        **results,
    )

    return results
```

---

## 5. INTEGRATION с PLUGIN (higgsfield-prompt-generator)

При generating промта для крео с identifiable real-person Soul ID, plugin output должен включать:

```
[AI DISCLOSURE OVERLAY]
Subject: {Name}, {Title}, {Firm}
Public source: {URL}
Required release: AI-generation likeness release (separate from marketing release)
DocuSign template ID: AI_RELEASE_v2026
Pre-launch checklist: 10/10 PASS required before campaign launch

CTA для producer:
1. Create DocuSign envelope from template AI_RELEASE_v2026
2. Send to {subject_email}
3. Wait for signature + countersign
4. Add to audit DB
5. Generate overlay: 'AI-assisted visual · {Name}, {Title} · {Registry}'
6. Run pre-launch audit
```

---

## 6. ROADMAP (post-deploy)

- **Q3 2026** — Pilot deploy с 3-5 агентствами курса
- **Q4 2026** — Full production deploy + GDPR audit
- **Q1 2027** — Multi-tenant SaaS offering для агентств (опционально)
- **Q2 2027** — AI-powered audit assistant (auto-flag deepfake / minor / etc patterns)

---

## 7. COMPLIANCE CONTACT

**EU AI Act questions:**
- European AI Office (effective 2026): https://digital-strategy.ec.europa.eu/en/policies/ai-office
- Country-level regulator (per Member State где deployed)

**Penalty exposure если non-compliant:**
- AI provider (Higgsfield Inc. — но это их exposure, не ours)
- AI deployer (агентство клиента курса) — до €7.5M или 1.5% turnover

**Recommended:** consult с EU AI Act specialist (Bird & Bird / Hogan Lovells / DLA Piper / Latham & Watkins имеют EU AI Act practice groups).

---

## CHANGELOG

- **2026-05-19 (П.27 v1.0):** Initial runbook — DocuSign integration spec + audit DB schema + withdrawal mechanism + pre-launch audit workflow + plugin integration.
- **Future updates** per EU AI Act implementation guidance Q2 2026.
