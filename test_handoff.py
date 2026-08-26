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
    assert x["action_evidence"]["physical_completion"] == "NOT_PROVED"
    assert x["institutional_claims"]["human_validation"] == "NOT_PROVED"
    assert x["institutional_claims"]["legal_effect"] == "NOT_PROVED"
    assert x["next_stage"] == "PRIVATE_NKEMBA_RECONSTRUCTION_NOT_INCLUDED"

print("PASS")
