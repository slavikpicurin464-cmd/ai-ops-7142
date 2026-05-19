#!/usr/bin/env python3
"""
ai-ops-7142 plugin integration test runner (P.26 CI infrastructure).

Запускает тесты из test-harness-example.json (или full set когда конвертирован
из TESTS-27-50.md) с использованием Anthropic API.

Usage:
    python run_tests.py --all                    # Run all tests
    python run_tests.py --test TEST-44           # Single test
    python run_tests.py --wave T.6,T.7           # Filter by wave
    python run_tests.py --skill higgsfield-prompt-generator  # Filter by skill
    python run_tests.py --automated-only         # Skip supervised tests

Output: /results/{test_id}.json + /results/SUMMARY.md
"""

import argparse
import asyncio
import json
import os
import sys
from datetime import datetime
from pathlib import Path

try:
    from anthropic import AsyncAnthropic
    from jsonschema import validate, ValidationError
    from rich.console import Console
    from rich.table import Table
    from rich.progress import Progress
except ImportError as e:
    print(f"ERROR: missing dependency {e}. Install via: pip install anthropic jsonschema rich pyyaml")
    sys.exit(1)


console = Console()


def load_schema(path: Path) -> dict:
    """Load test harness JSON schema."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_tests(path: Path, schema: dict) -> list[dict]:
    """Load tests file and validate against schema."""
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    tests = data.get('tests', [])
    valid_tests = []

    for test in tests:
        try:
            validate(instance=test, schema=schema)
            valid_tests.append(test)
        except ValidationError as e:
            console.print(f"[yellow]WARNING:[/yellow] Test {test.get('id', 'unknown')} schema validation failed: {e.message}")

    return valid_tests


def filter_tests(
    tests: list[dict],
    test_ids: list[str] = None,
    waves: list[str] = None,
    skills: list[str] = None,
    automated_only: bool = False,
) -> list[dict]:
    """Apply CLI filters."""
    result = tests

    if test_ids:
        result = [t for t in result if t['id'] in test_ids]

    if waves:
        result = [t for t in result if t['wave'] in waves]

    if skills:
        result = [t for t in result if t['skill'] in skills]

    if automated_only:
        result = [
            t for t in result
            if not t.get('automation_notes', {}).get('supervised', True)
            or t.get('automation_notes', {}).get('claude_eval_compatible', False)
        ]

    return result


async def run_test(
    client: AsyncAnthropic,
    test: dict,
    model: str,
    results_dir: Path,
) -> dict:
    """Run a single test against Claude API."""
    test_id = test['id']
    started_at = datetime.utcnow().isoformat()

    # Build system prompt simulating plugin context
    system_prompt = (
        "You are Claude with the ai-ops-7142 plugin loaded. "
        "When responding to user requests, follow plugin rules for the matching skill. "
        "If a PRESET would activate (e.g. B2B_SAAS_ENTERPRISE_PRESET, "
        "REAL_ESTATE_EXPAT_USA_PRESET, etc), explicitly mention which PRESET activated "
        "and list which validation rules (V1-V21), Pre-валидаторы (A.1-A.5), "
        "humanization (H1-H10), rationality (RAT1-RAT8), and meta-policy categories "
        "should be triggered. Also list which regulatory overlays should be added."
    )

    # Build user message
    user_message = test['input']['content']
    if isinstance(user_message, list):
        user_message = "\n".join(user_message)

    context = test['input'].get('context', {})
    if context:
        context_str = "\n\nContext:\n" + "\n".join(f"- {k}: {v}" for k, v in context.items())
        user_message = user_message + context_str

    try:
        response = await client.messages.create(
            model=model,
            max_tokens=4096,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )
        output = response.content[0].text
        api_status = "success"
    except Exception as e:
        output = f"API ERROR: {e}"
        api_status = "error"

    # Save raw output
    test_result = {
        "test_id": test_id,
        "wave": test['wave'],
        "skill": test['skill'],
        "started_at": started_at,
        "finished_at": datetime.utcnow().isoformat(),
        "api_status": api_status,
        "model": model,
        "input": test['input'],
        "expected": test['expected'],
        "fail_mode": test['fail_mode'],
        "raw_output": output,
        "verification": None,  # filled by verify_test.py
        "automation_notes": test.get('automation_notes', {}),
    }

    # Write result file
    result_path = results_dir / f"{test_id}.json"
    with open(result_path, 'w', encoding='utf-8') as f:
        json.dump(test_result, f, indent=2, ensure_ascii=False)

    return test_result


def render_summary(results: list[dict], results_dir: Path):
    """Print summary table + write SUMMARY.md."""
    table = Table(title="Test Results Summary")
    table.add_column("Test ID", style="cyan")
    table.add_column("Wave", style="magenta")
    table.add_column("Skill")
    table.add_column("Status")
    table.add_column("Verification")

    for r in results:
        status = r['api_status']
        verification = r.get('verification', 'pending (supervised)')
        table.add_row(
            r['test_id'],
            r['wave'],
            r['skill'],
            status,
            str(verification),
        )

    console.print(table)

    # Write Markdown summary
    summary_path = results_dir / "SUMMARY.md"
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(f"# Test Run Summary\n\n")
        f.write(f"**Generated:** {datetime.utcnow().isoformat()}\n")
        f.write(f"**Total tests:** {len(results)}\n")
        f.write(f"**Success (API):** {sum(1 for r in results if r['api_status'] == 'success')}\n")
        f.write(f"**Errors (API):** {sum(1 for r in results if r['api_status'] == 'error')}\n")
        f.write(f"**Verification pending (supervised):** {sum(1 for r in results if r.get('verification') is None)}\n\n")

        f.write("## Per-test results\n\n")
        for r in results:
            f.write(f"- **{r['test_id']}** ({r['wave']} / {r['skill']}): {r['api_status']} — verification: {r.get('verification', 'pending')}\n")

        f.write("\n## Next step\n\n")
        f.write("Run `python verify_test.py /results/{test_id}.json` for each pending test to verify expected behavior.\n")
        f.write("For automated tests with `claude_eval_compatible: true`, verify_test.py can structured-match expected vs actual.\n")
        f.write("For supervised tests, human reviewer evaluates raw_output against expected criteria.\n")


async def main():
    parser = argparse.ArgumentParser(description="ai-ops-7142 plugin integration test runner")
    parser.add_argument('--all', action='store_true', help='Run all tests')
    parser.add_argument('--test', type=str, help='Run specific test ID(s), comma-separated')
    parser.add_argument('--wave', type=str, help='Filter by wave(s), comma-separated (e.g. T.6,T.7)')
    parser.add_argument('--skill', type=str, help='Filter by skill name')
    parser.add_argument('--automated-only', action='store_true', help='Only run claude_eval_compatible tests')
    parser.add_argument('--schema', type=str, default='/workspace/schema.json', help='Path to schema JSON')
    parser.add_argument('--tests', type=str, default='/workspace/tests.json', help='Path to tests JSON')
    parser.add_argument('--results', type=str, default=os.getenv('RESULTS_DIR', '/results'), help='Output directory')
    parser.add_argument('--model', type=str, default=os.getenv('CLAUDE_MODEL', 'claude-sonnet-4-5'), help='Anthropic model')
    parser.add_argument('--workers', type=int, default=int(os.getenv('PARALLEL_WORKERS', '3')), help='Parallel test execution')

    args = parser.parse_args()

    # Load schema + tests
    schema_path = Path(args.schema)
    tests_path = Path(args.tests)
    results_dir = Path(args.results)
    results_dir.mkdir(parents=True, exist_ok=True)

    if not schema_path.exists():
        console.print(f"[red]ERROR:[/red] Schema not found at {schema_path}")
        sys.exit(1)
    if not tests_path.exists():
        console.print(f"[red]ERROR:[/red] Tests not found at {tests_path}")
        sys.exit(1)

    schema = load_schema(schema_path)
    tests = load_tests(tests_path, schema)
    console.print(f"[green]Loaded[/green] {len(tests)} tests (schema-validated)")

    # Apply filters
    test_ids = args.test.split(',') if args.test else None
    waves = args.wave.split(',') if args.wave else None
    skills = args.skill.split(',') if args.skill else None
    filtered = filter_tests(tests, test_ids=test_ids, waves=waves, skills=skills, automated_only=args.automated_only)
    console.print(f"[cyan]Filtered to[/cyan] {len(filtered)} tests")

    if not filtered:
        console.print("[yellow]No tests match filters. Exiting.[/yellow]")
        return

    # Run tests
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        console.print("[red]ERROR:[/red] ANTHROPIC_API_KEY not set")
        sys.exit(1)

    client = AsyncAnthropic(api_key=api_key)

    semaphore = asyncio.Semaphore(args.workers)

    async def bounded_run(test):
        async with semaphore:
            return await run_test(client, test, args.model, results_dir)

    with Progress() as progress:
        task = progress.add_task(f"Running {len(filtered)} tests...", total=len(filtered))
        results = []
        for coro in asyncio.as_completed([bounded_run(t) for t in filtered]):
            result = await coro
            results.append(result)
            progress.update(task, advance=1)

    # Summary
    render_summary(results, results_dir)
    console.print(f"\n[green]Done.[/green] Results in {results_dir}")


if __name__ == '__main__':
    asyncio.run(main())
