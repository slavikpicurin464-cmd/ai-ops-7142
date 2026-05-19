# CI Infrastructure для ai-ops-7142 plugin integration tests

**Создано в волне П.26 (2026-05-19) — production-ready test harness.**

## Структура

```
internal/tests/
├── TESTS-27-50.md                  — 24 теста в markdown (П.24)
├── test-harness-schema.json        — JSON Schema (П.25)
├── test-harness-example.json       — 5 показательных тестов в JSON (П.25)
├── ci/                             — CI infrastructure (П.26)
│   ├── README.md                   — этот файл
│   ├── Dockerfile                  — контейнер для locally run + CI
│   ├── requirements.txt            — Python dependencies
│   ├── run_tests.py                — главный runner (async, parallel)
│   └── verify_test.py              — verifier (regex / structured / llm_judge / human)
└── (на main repo)
    .github/workflows/
    └── test-harness.yml            — GitHub Actions workflow
```

## Быстрый старт (локально)

```bash
# 1. Установка
pip install -r internal/tests/ci/requirements.txt

# 2. Запустить все тесты
export ANTHROPIC_API_KEY=sk-ant-...
python internal/tests/ci/run_tests.py --all \
  --schema internal/tests/test-harness-schema.json \
  --tests internal/tests/test-harness-example.json \
  --results /tmp/test-results

# 3. Verify результаты
for f in /tmp/test-results/TEST-*.json; do
  python internal/tests/ci/verify_test.py "$f"
done

# 4. Открыть summary
cat /tmp/test-results/SUMMARY.md
```

## Быстрый старт (Docker)

```bash
docker build -t ai-ops-7142-ci -f internal/tests/ci/Dockerfile .
docker run --rm \
  -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY \
  -v $(pwd)/results:/results \
  ai-ops-7142-ci --all
```

## Быстрый старт (GitHub Actions)

CI запускается автоматически на:
- Push в `main` если изменения в `skills/**` или `internal/tests/**`
- Pull request в `main`
- Nightly cron 03:00 UTC
- Manual trigger через workflow_dispatch

**Requires:** `ANTHROPIC_API_KEY` в GitHub Secrets.

## Filtering

```bash
# Single test
python run_tests.py --test TEST-44

# Multiple tests
python run_tests.py --test TEST-44,TEST-46,TEST-49

# По волнам
python run_tests.py --wave T.6,T.7,T.8

# По скилу
python run_tests.py --skill higgsfield-prompt-generator

# Только автоматизируемые (skip supervised)
python run_tests.py --all --automated-only

# Custom model
python run_tests.py --all --model claude-opus-4-1
```

## Verification methods

Каждый тест в JSON имеет `automation_notes.verification_method`:

| Method | Что делает | Auto/Manual |
|---|---|---|
| `regex_match` | Простой regex match на `regulatory_overlays.content_pattern` в `raw_output` | Auto |
| `structured_output_validation` | Парсит PRESET activation + validation rules + meta categories + overlays | Auto |
| `llm_judge` | Генерирует prompt для human-led LLM judge | Manual (с подсказкой) |
| `human_review` | Просто template для human reviewer | Manual |

## Расширение тестов

### Добавить новый тест:

1. Описать в `TESTS-27-50.md` (markdown) для документации
2. Формализовать в JSON формате per `test-harness-schema.json`
3. Добавить в `test-harness-example.json` массив `tests[]`
4. Schema-validate: `python -c "import json, jsonschema; ..."` (см. workflow)
5. Запустить: `python run_tests.py --test TEST-NN`

### Конвертация TESTS-27-50.md → JSON:

Markdown → JSON конвертер пока manual. Полная automation на roadmap (П.28).

## Roadmap (после П.26):

- **П.28** Markdown-to-JSON converter (parse TESTS-27-50.md → batch generate JSON)
- **П.29** Slack / Discord notification на test failures
- **П.30** Test result analytics dashboard (Streamlit / Grafana)
- **П.31** Mutation testing (intentional breakage → confirm tests catch it)

## Troubleshooting

**Schema validation fails:** проверь test JSON против `test-harness-schema.json` enum'ов.
**API errors:** проверь `ANTHROPIC_API_KEY` + rate limits.
**Test fails verification:** check `automation_notes.verification_method` — может быть `human_review`.
