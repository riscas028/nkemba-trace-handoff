#!/usr/bin/env python3
import json
import hashlib
import sys


def digest(obj):
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def enum(value, allowed, fallback):
    return value if value in allowed else fallback


def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: handoff.py input.json output.json")

    with open(sys.argv[1], encoding="utf-8") as f:
        src = json.load(f)

    trace = src.get("trace_verification", {})
    action = src.get("action_evidence", {})
    outcome = src.get("outcome_evidence", {})

    trace_state = enum(
        trace.get("status", "NOT_SUPPLIED"),
        {"VERIFIED", "NOT_VERIFIED", "NOT_SUPPLIED"},
        "NOT_VERIFIED",
    )
    verification_performed = enum(
        trace.get("verification_performed", "NOT_SUPPLIED"),
        {"YES", "NO", "INDETERMINATE", "NOT_SUPPLIED"},
        "INDETERMINATE",
    )
    revocation_check = enum(
        trace.get("revocation_check", "NOT_SUPPLIED"),
        {"CHECKED_PASS", "CHECKED_FAIL", "NOT_PERFORMED", "INDETERMINATE", "NOT_SUPPLIED"},
        "INDETERMINATE",
    )
    reproducibility = enum(
        trace.get("reproducibility", "NOT_SUPPLIED"),
        {"REPRODUCED", "DIVERGED", "NOT_ATTEMPTED", "NOT_SUPPLIED"},
        "NOT_SUPPLIED",
    )

    reason_codes = []
    if verification_performed == "NO":
        reason_codes.append("NK-TRACE-VERIFICATION-NOT-PERFORMED")
    elif verification_performed == "INDETERMINATE":
        reason_codes.append("NK-TRACE-VERIFICATION-INDETERMINATE")

    if revocation_check == "NOT_PERFORMED":
        reason_codes.append("NK-TRACE-REVOCATION-NOT-PERFORMED")
    elif revocation_check == "INDETERMINATE":
        reason_codes.append("NK-TRACE-REVOCATION-INDETERMINATE")
    elif revocation_check == "CHECKED_FAIL":
        reason_codes.append("NK-TRACE-REVOCATION-FAILED")

    if reproducibility == "DIVERGED":
        reason_codes.append("NK-TRACE-REPRODUCIBILITY-DIVERGED")
    elif reproducibility == "NOT_ATTEMPTED":
        reason_codes.append("NK-TRACE-REPRODUCIBILITY-NOT-ATTEMPTED")

    out = {
        "profile": "nkemba.external-evidence-handoff/1",
        "trace_evidence": {
            "status": trace_state,
            "verification_performed": verification_performed,
            "revocation_check": revocation_check,
            "reproducibility": reproducibility,
            "source_id": trace.get("source_id"),
            "verifier": trace.get("verifier"),
            "spec_version": trace.get("spec_version"),
            "verification_surface": trace.get("verification_surface"),
            "reason_codes": reason_codes,
            "note": "Upstream TRACE states are preserved separately. VERIFIED is not promoted to institutional truth, and NOT_PERFORMED/INDETERMINATE remain distinct from positive verification.",
        },
        "action_evidence": {
            "status": action.get("status", "NOT_SUPPLIED"),
            "source_id": action.get("source_id"),
            "physical_completion": "NOT_PROVED",
            "reason_code": "NK-OUTCOME-NOT-ESTABLISHED",
        },
        "outcome_evidence": {
            "status": outcome.get("status", "NOT_SUPPLIED"),
            "source_id": outcome.get("source_id"),
            "scope": outcome.get("scope"),
            "boundary": "No inference beyond explicitly supplied and verified scope.",
        },
        "institutional_claims": {
            "human_validation": "NOT_PROVED",
            "human_authority": "NOT_PROVED",
            "institutional_adoption": "NOT_PROVED",
            "notification": "NOT_PROVED",
            "legal_effect": "NOT_PROVED",
            "business_effect": "NOT_PROVED",
            "reason_codes": [
                "NK-HUMAN-AUTHORITY-NOT-ESTABLISHED",
                "NK-NOTIFICATION-NOT-PROVEN",
                "NK-INSTITUTIONAL-OUTCOME-NOT-ESTABLISHED",
            ],
        },
        "next_stage": "PRIVATE_NKEMBA_RECONSTRUCTION_NOT_INCLUDED",
    }

    out["handoff_digest"] = digest(out)

    with open(sys.argv[2], "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
