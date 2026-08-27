#!/usr/bin/env python3
"""External-safe negative cases for the TRACE -> N'KEMBA evidence boundary.

These tests intentionally model inputs where a naive downstream consumer might
promote technical verification into a stronger institutional claim.
"""
import json
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
HANDOFF = ROOT / "handoff.py"


def run_case(payload):
    with tempfile.TemporaryDirectory() as d:
        d = pathlib.Path(d)
        src = d / "input.json"
        out = d / "output.json"
        src.write_text(json.dumps(payload), encoding="utf-8")
        subprocess.run([sys.executable, str(HANDOFF), str(src), str(out)], check=True)
        return json.loads(out.read_text(encoding="utf-8"))


def assert_not_promoted(result):
    assert result["trace_evidence"]["status"] == "VERIFIED"
    assert result["action_evidence"]["physical_completion"] == "NOT_PROVED"
    assert result["institutional_claims"]["human_validation"] == "NOT_PROVED"
    assert result["institutional_claims"]["institutional_adoption"] == "NOT_PROVED"
    assert result["institutional_claims"]["legal_effect"] == "NOT_PROVED"
    assert result["institutional_claims"]["business_effect"] == "NOT_PROVED"


# NEG-001: verified payment instruction != settlement.
payment = run_case({
    "trace_verification": {"status": "VERIFIED", "source_id": "trace:neg-001"},
    "action_evidence": {"status": "ACCEPTED", "source_id": "tool:payment-instruction"},
})
assert_not_promoted(payment)

# NEG-002: verified notification action != proof a person was actually informed.
notification = run_case({
    "trace_verification": {"status": "VERIFIED", "source_id": "trace:neg-002"},
    "action_evidence": {"status": "ACCEPTED", "source_id": "tool:notification"},
})
assert_not_promoted(notification)
assert notification["institutional_claims"]["human_validation"] == "NOT_PROVED"

# NEG-003: verified runtime/tool action != institutional/legal/business outcome.
institutional = run_case({
    "trace_verification": {"status": "VERIFIED", "source_id": "trace:neg-003"},
    "action_evidence": {"status": "ACCEPTED", "source_id": "tool:institutional-action"},
    "outcome_evidence": {"status": "NOT_SUPPLIED"},
})
assert_not_promoted(institutional)

print("PASS NKEMBA-TRACE-NEGATIVE-CASES-001")
