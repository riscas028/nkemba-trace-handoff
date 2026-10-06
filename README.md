# N’KEMBA Evidence Handoff

N’KEMBA Evidence Handoff is a minimal external-safe bridge for preserving verified TRACE-derived evidence states and explicit proof boundaries for downstream institutional reconstruction.

## Public independent audits

**Commercial pilot:** [N’KEMBA Independent AI Audit — Commercial Pilot](COMMERCIAL-PILOT.md)

N’KEMBA also publishes independent, evidence-bounded audits of AI runtime and governance systems. The current public audit covers NVIDIA OpenShell and reaches **#284**.

- [NVIDIA OpenShell audit boundary](audits/nvidia-openshell/README.md)
- [NVIDIA OpenShell audit ledger #001–#284](audits/nvidia-openshell/LEDGER.md)

The audit distinguishes documentary confirmation from experiments that still require controlled execution. It does not constitute NVIDIA certification or claim that every proposed test has been run.

## What it does

This public integration accepts a verification result supplied by an upstream TRACE verifier, plus optional action/outcome evidence metadata, and emits a minimal handoff containing:

- source identifiers;
- verification states;
- explicit scope boundaries;
- claims that remain `NOT_PROVED`;
- stable downstream reason codes for material proof gaps;
- an integrity digest over the handoff.

The handoff deliberately separates technical evidence from later institutional facts.

## Conservative TRACE-state preservation

The adapter preserves potentially material verification states separately instead of collapsing them into a single `VERIFIED`/`PASS` result:

- `verification_performed`: `YES`, `NO`, `INDETERMINATE`, or `NOT_SUPPLIED`;
- `revocation_check`: `CHECKED_PASS`, `CHECKED_FAIL`, `NOT_PERFORMED`, `INDETERMINATE`, or `NOT_SUPPLIED`;
- `reproducibility`: `REPRODUCED`, `DIVERGED`, `NOT_ATTEMPTED`, or `NOT_SUPPLIED`;
- optional `spec_version` and `verification_surface` provenance.

`NOT_PERFORMED` and `INDETERMINATE` are deliberately not promoted to positive verification.

## What it does not claim

- It does not issue TRACE Trust Records.
- It does not independently verify raw TRACE JWT/CWT/COSE envelopes in the handoff component.
- It does not claim TRACE conformance or certification.
- It does not infer physical completion from controller acceptance.
- It does not infer human approval, institutional adoption, legal effect, or business effect without separate evidence.
- It does not expose N’KEMBA’s internal reconstruction methodology.

## Run

Python 3.11+:

```bash
python handoff.py example-input.json output.json
python test_handoff.py
python tests/test_negative_cases.py
```

The example inputs are synthetic and contain no private or customer data.

## Evidence boundary

The public integration ends at the handoff. Institutional reconstruction occurs outside this repository.

## Interactive public demonstration

N’KEMBA’s public demonstration of the downstream institutional-reconstruction layer is available at:

https://nkemba.pt/pilot.html

## Licensing boundary

Repository source and test material is published under Apache License 2.0. The `NOTICE` file records the scope boundary: the public license does not license or disclose any separate N’KEMBA proprietary implementation, schema, reconstruction methodology, semantic verification logic, contradiction handling, scoring/ranking logic, heuristics, sealed evidence material, or customer data.
