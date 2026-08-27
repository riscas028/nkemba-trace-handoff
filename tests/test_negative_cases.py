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

# NEG-004: an upstream outcome_unknown state must not be resolved downstream.
unknown_outcome = run_case({
    "trace_verification": {"status": "VERIFIED", "source_id": "trace:neg-004"},
    "action_evidence": {"status": "ACCEPTED", "source_id": "tool:irreversible-action"},
    "outcome_evidence": {"status": "outcome_unknown", "source_id": "cmcp:neg-004"},
})
assert_not_promoted(unknown_outcome)
assert unknown_outcome["outcome_evidence"]["status"] == "outcome_unknown"

# NEG-005: a resolvable external reference/digest != attested external fact.
resolved_reference = run_case({
    "trace_verification": {"status": "VERIFIED", "source_id": "trace:neg-005"},
    "action_evidence": {"status": "ACCEPTED", "source_id": "tool:reference-resolution"},
    "outcome_evidence": {
        "status": "REFERENCE_RESOLVED",
        "source_id": "institutional-record:neg-005",
        "scope": "digest-and-location-only",
    },
})
assert_not_promoted(resolved_reference)
assert resolved_reference["outcome_evidence"]["scope"] == "digest-and-location-only"

# NEG-006: an asserted but unverified approval != attributable human validation.
unverified_approval = run_case({
    "trace_verification": {"status": "VERIFIED", "source_id": "trace:neg-006"},
    "action_evidence": {"status": "ACCEPTED", "source_id": "tool:approval-request"},
    "outcome_evidence": {
        "status": "ASSERTED_NOT_VERIFIED",
        "source_id": "approval-claim:neg-006",
        "scope": "human-approval-assertion",
    },
})
assert_not_promoted(unverified_approval)
assert unverified_approval["institutional_claims"]["human_validation"] == "NOT_PROVED"

print("PASS NKEMBA-TRACE-NEGATIVE-CASES-001")
