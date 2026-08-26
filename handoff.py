#!/usr/bin/env python3
import json
import hashlib
import sys


def digest(obj):
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: handoff.py input.json output.json")

    with open(sys.argv[1], encoding="utf-8") as f:
        src = json.load(f)

    trace = src.get("trace_verification", {})
    action = src.get("action_evidence", {})
    outcome = src.get("outcome_evidence", {})

    trace_state = trace.get("status", "NOT_SUPPLIED")
    if trace_state not in {"VERIFIED", "NOT_VERIFIED", "NOT_SUPPLIED"}:
        trace_state = "NOT_VERIFIED"

    out = {
        "profile": "nkemba.external-evidence-handoff/1",
        "trace_evidence": {
            "status": trace_state,
            "source_id": trace.get("source_id"),
            "verifier": trace.get("verifier"),
            "note": "Upstream verification state is preserved, not independently re-performed here.",
        },
        "action_evidence": {
            "status": action.get("status", "NOT_SUPPLIED"),
            "source_id": action.get("source_id"),
            "physical_completion": "NOT_PROVED",
        },
        "outcome_evidence": {
            "status": outcome.get("status", "NOT_SUPPLIED"),
            "source_id": outcome.get("source_id"),
            "scope": outcome.get("scope"),
            "boundary": "No inference beyond explicitly supplied and verified scope.",
        },
        "institutional_claims": {
            "human_validation": "NOT_PROVED",
            "institutional_adoption": "NOT_PROVED",
            "legal_effect": "NOT_PROVED",
            "business_effect": "NOT_PROVED",
        },
        "next_stage": "PRIVATE_NKEMBA_RECONSTRUCTION_NOT_INCLUDED",
    }

    out["handoff_digest"] = digest(out)

    with open(sys.argv[2], "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
