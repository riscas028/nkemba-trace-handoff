#!/usr/bin/env python3
import json
import pathlib
import subprocess
import sys
import tempfile

root = pathlib.Path(__file__).parent

with tempfile.TemporaryDirectory() as d:
    out = pathlib.Path(d) / "out.json"
    subprocess.run(
        [sys.executable, str(root / "handoff.py"), str(root / "example-input.json"), str(out)],
        check=True,
    )
    with open(out, encoding="utf-8") as f:
        x = json.load(f)

    assert x["trace_evidence"]["status"] == "VERIFIED"
    assert x["trace_evidence"]["verification_performed"] == "YES"
    assert x["trace_evidence"]["revocation_check"] == "NOT_PERFORMED"
    assert x["trace_evidence"]["reproducibility"] == "NOT_ATTEMPTED"
    assert "NK-TRACE-REVOCATION-NOT-PERFORMED" in x["trace_evidence"]["reason_codes"]
    assert "NK-TRACE-REPRODUCIBILITY-NOT-ATTEMPTED" in x["trace_evidence"]["reason_codes"]
    assert x["action_evidence"]["physical_completion"] == "NOT_PROVED"
    assert x["action_evidence"]["reason_code"] == "NK-OUTCOME-NOT-ESTABLISHED"
    assert x["institutional_claims"]["human_validation"] == "NOT_PROVED"
    assert x["institutional_claims"]["human_authority"] == "NOT_PROVED"
    assert x["institutional_claims"]["notification"] == "NOT_PROVED"
    assert x["institutional_claims"]["legal_effect"] == "NOT_PROVED"
    assert x["next_stage"] == "PRIVATE_NKEMBA_RECONSTRUCTION_NOT_INCLUDED"

print("PASS")
