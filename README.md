# N’KEMBA Evidence Handoff

N’KEMBA Evidence Handoff is a minimal external-safe bridge for preserving verified TRACE-derived evidence states and explicit proof boundaries for downstream institutional reconstruction.

## What it does

This public integration accepts a verification result supplied by an upstream TRACE verifier, plus optional action/outcome evidence metadata, and emits a minimal handoff containing:

- source identifiers;
- verification states;
- explicit scope boundaries;
- claims that remain `NOT_PROVED`;
- an integrity digest over the handoff.

The handoff deliberately separates technical evidence from later institutional facts.

## What it does not claim

- It does not issue TRACE Trust Records.
- It does not independently verify raw TRACE JWT/CWT/COSE envelopes.
- It does not claim TRACE conformance or certification.
- It does not infer physical completion from controller acceptance.
- It does not infer human approval, institutional adoption, legal effect, or business effect without separate evidence.
- It does not expose N’KEMBA’s internal reconstruction methodology.

## Run

Python 3.11+:

```bash
python handoff.py example-input.json output.json
```

The example input is synthetic and contains no private or customer data.

## Evidence boundary

The public integration ends at the handoff. Institutional reconstruction occurs outside this repository.

## Licensing boundary

The open-source license in this repository applies only to the files published here. It does not license or disclose any separate N’KEMBA proprietary implementation, schema, reconstruction methodology, semantic verification logic, contradiction handling, scoring/ranking logic, heuristics, sealed evidence material, or customer data.
