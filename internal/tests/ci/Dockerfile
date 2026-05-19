# Dockerfile для CI test harness — ai-ops-7142 plugin integration tests
# Волна П.26 (2026-05-19)
# Использование: docker build -t ai-ops-7142-ci . && docker run --rm -v $(pwd)/results:/results ai-ops-7142-ci

FROM python:3.11-slim

LABEL maintainer="ai-ops-7142"
LABEL description="Integration test runner for ai-ops-7142 plugin (50 tests, supervised + automatable)"
LABEL version="1.0.0"

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    jq \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies для test harness
RUN pip install --no-cache-dir \
    jsonschema==4.21.1 \
    anthropic==0.39.0 \
    pyyaml==6.0.1 \
    pytest==8.0.0 \
    pytest-asyncio==0.23.4 \
    rich==13.7.0

# Working directory
WORKDIR /workspace

# Copy test infrastructure
COPY internal/tests/test-harness-schema.json /workspace/schema.json
COPY internal/tests/test-harness-example.json /workspace/tests.json
COPY internal/tests/ci/run_tests.py /workspace/run_tests.py
COPY internal/tests/ci/verify_test.py /workspace/verify_test.py

# Copy plugin skills for analysis
COPY skills/ /workspace/skills/

# Environment variables (overridden at runtime)
ENV ANTHROPIC_API_KEY=""
ENV CLAUDE_MODEL="claude-sonnet-4-5"
ENV TEST_FILTER=""
ENV PARALLEL_WORKERS="3"
ENV RESULTS_DIR="/results"

# Entrypoint — runs full test suite or filtered
ENTRYPOINT ["python", "/workspace/run_tests.py"]
CMD ["--all"]
