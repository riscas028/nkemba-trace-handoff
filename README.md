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

## Reproducible TRACE v0.2 signed-vector boundary test

A separate external-safe test exercises the public TRACE v0.2 signed UTF-16 key-order test vector (`03-utf16-key-order.json`). It verifies the Ed25519 signature using RFC 8785-compatible UTF-16 property ordering, confirms that a one-field tamper invalidates the signature, and then checks that N’KEMBA does not promote technical integrity into unsupported institutional claims.

Install the test-only dependency and run:

```bash
python -m pip install cryptography
python tests/test_trace_v02_official_vector.py
```

Expected result:

```text
PASS NKEMBA-TRACE-SIGNED-VECTOR-001
```

The test deliberately preserves these boundaries:

- signed technical record integrity can be proved;
- a `software-only` runtime is not treated as hardware attestation;
- physical completion remains `NOT_PROVED`;
- human validation remains `NOT_PROVED`;
- institutional adoption remains `NOT_PROVED`;
- legal effect remains `NOT_PROVED`;
- business effect remains `NOT_PROVED`.

## Negative boundary cases

`tests/test_negative_cases.py` contains deliberately adversarial downstream cases where a naive consumer could over-promote technical verification into an institutional claim:

- `NEG-001`: a verified payment instruction is not proof that settlement occurred;
- `NEG-002`: a verified notification action is not proof that a person was actually informed;
- `NEG-003`: a verified runtime/tool action is not proof of institutional adoption, legal effect, or business effect.

Each case preserves the stronger downstream claims as `NOT_PROVED`. These are proof-boundary observations intended to make assurance overclaim visible and testable; they are not claims of TRACE certification or formal conformance.

## Evidence boundary

The public integration ends at the handoff. Institutional reconstruction occurs outside this repository.

## Licensing boundary

Repository source and test material is published under Apache License 2.0. The `NOTICE` file records the scope boundary: the public license does not license or disclose any separate N’KEMBA proprietary implementation, schema, reconstruction methodology, semantic verification logic, contradiction handling, scoring/ranking logic, heuristics, sealed evidence material, or customer data.
