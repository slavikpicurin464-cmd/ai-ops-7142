#!/usr/bin/env python3
"""
Verify single test result against expected criteria (P.26 CI infrastructure).

Usage:
    python verify_test.py /results/TEST-44.json
    python verify_test.py /results/*.json    # Batch

Verification methods (per automation_notes.verification_method):
- regex_match: simple regex pattern matching on raw_output
- structured_output_validation: parse output for PRESET activation, validation rules, overlays
- llm_judge: use Claude as judge (supervised — outputs prompt for human reviewer)
- human_review: skip automated verification, output template for reviewer

Output: appends verification result to source JSON + prints PASS/FAIL.
"""

import argparse
import json
import re
import sys
from pathlib import Path

try:
    from rich.console import Console
    from rich.panel import Panel
except ImportError:
    print("ERROR: missing rich. Install: pip install rich")
    sys.exit(1)


console = Console()


def verify_regex_match(result: dict) -> tuple[bool, str]:
    """Verify expected regulatory_overlays content_pattern matches in raw_output."""
    expected = result.get('expected', {})
    overlays = expected.get('regulatory_overlays', [])
    raw = result['raw_output']

    failures = []
    successes = []

    for overlay in overlays:
        pattern = overlay.get('content_pattern', '')
        if not pattern:
            continue
        try:
            if re.search(pattern, raw, re.IGNORECASE | re.DOTALL):
                successes.append(f"✓ {overlay['jurisdiction']}/{overlay['type']}: matched")
            else:
                failures.append(f"✗ {overlay['jurisdiction']}/{overlay['type']}: pattern '{pattern}' NOT found")
        except re.error as e:
            failures.append(f"✗ {overlay['jurisdiction']}/{overlay['type']}: invalid regex {e}")

    if not overlays:
        return True, "No overlays defined — auto-PASS"

    if failures:
        return False, "\n".join(failures + successes)
    return True, "\n".join(successes)


def verify_structured(result: dict) -> tuple[bool, str]:
    """Verify PRESET activation + checks_passed structure in raw_output."""
    expected = result.get('expected', {})
    raw = result['raw_output']
    notes = []

    # Check PRESET activated
    preset = expected.get('preset_activated')
    if preset:
        if preset in raw:
            notes.append(f"✓ PRESET '{preset}' mentioned")
        else:
            notes.append(f"✗ PRESET '{preset}' NOT mentioned")

    # Check validation rules
    checks = expected.get('checks_passed', {})
    for rule in checks.get('validation_rules', []):
        if rule in raw:
            notes.append(f"✓ {rule} mentioned")
        else:
            notes.append(f"✗ {rule} NOT mentioned")

    # Check pre-validators
    for pv in checks.get('pre_validators', []):
        if pv in raw or pv.replace('.', '\\.') in raw:
            notes.append(f"✓ Pre-валидатор {pv} mentioned")
        else:
            notes.append(f"✗ Pre-валидатор {pv} NOT mentioned")

    # Check meta-policy categories
    for cat in checks.get('meta_policy_categories', []):
        if cat in raw:
            notes.append(f"✓ Meta category '{cat[:50]}...' mentioned")
        else:
            notes.append(f"✗ Meta category '{cat[:50]}...' NOT mentioned")

    # Also run regex match
    overlay_passed, overlay_notes = verify_regex_match(result)
    notes.append(f"\nOverlay verification:\n{overlay_notes}")

    failures = [n for n in notes if n.startswith('✗')]
    return (len(failures) == 0, "\n".join(notes))


def verify_llm_judge_prompt(result: dict) -> tuple[bool, str]:
    """Generate prompt for human LLM-judge (returns PROMPT, not auto-PASS)."""
    expected = result.get('expected', {})
    fail_mode = result['fail_mode']

    prompt = f"""LLM JUDGE PROMPT for test {result['test_id']}:

INPUT given to Claude:
{json.dumps(result['input'], indent=2, ensure_ascii=False)}

EXPECTED behavior:
{json.dumps(expected, indent=2, ensure_ascii=False)}

FAIL MODE (regression description):
{fail_mode}

ACTUAL Claude output:
{result['raw_output']}

JUDGE: Did Claude's actual output match the expected behavior?
- Did the right PRESET activate?
- Were the right validation rules / Pre-validators / META categories mentioned?
- Were the right regulatory overlays added?
- Would this catch the fail mode (regression)?

Respond: PASS / FAIL / PARTIAL with brief justification.
"""
    return False, f"LLM JUDGE PROMPT (run separately):\n{prompt}"


def verify(result: dict) -> dict:
    """Dispatch to verification method per automation_notes."""
    method = result.get('automation_notes', {}).get('verification_method', 'human_review')

    if method == 'regex_match':
        passed, notes = verify_regex_match(result)
    elif method == 'structured_output_validation':
        passed, notes = verify_structured(result)
    elif method == 'llm_judge':
        passed, notes = verify_llm_judge_prompt(result)
    else:  # human_review
        passed, notes = (None, "Manual human review required — examine raw_output against expected")

    return {
        'method': method,
        'passed': passed,
        'notes': notes,
    }


def main():
    parser = argparse.ArgumentParser(description="Verify test results against expected criteria")
    parser.add_argument('result_files', nargs='+', help='Result JSON file(s)')
    args = parser.parse_args()

    for result_file in args.result_files:
        path = Path(result_file)
        if not path.exists():
            console.print(f"[red]ERROR:[/red] {result_file} not found")
            continue

        with open(path, 'r', encoding='utf-8') as f:
            result = json.load(f)

        verification = verify(result)
        result['verification'] = verification

        # Save back
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        # Pretty print
        status = verification['passed']
        color = "green" if status is True else "red" if status is False else "yellow"
        label = "PASS" if status is True else "FAIL" if status is False else "PENDING (supervised)"

        console.print(Panel(
            f"[{color}]{label}[/{color}]\n\n{verification['notes']}",
            title=f"{result['test_id']} ({verification['method']})",
            border_style=color,
        ))


if __name__ == '__main__':
    main()
