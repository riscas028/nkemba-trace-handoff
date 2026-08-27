# TRACE → N’KEMBA interoperability observations

Status: external-safe implementation observations. These are not claims of
TRACE certification or formal conformance.

## Purpose

This matrix records negative proof-boundary cases: inputs for which a naive
consumer could promote valid technical evidence into an unsupported physical,
human, institutional, legal, or business conclusion. The public N’KEMBA
handoff preserves the upstream state while leaving the stronger conclusion
`NOT_PROVED` unless separately attributable evidence establishes it.

| ID | Upstream state | Naive overclaim | Required downstream result |
| --- | --- | --- | --- |
| NEG-001 | Verified payment instruction | The payment settled | Settlement/physical completion remains `NOT_PROVED` |
| NEG-002 | Verified notification action | The person was informed | Human receipt/validation remains `NOT_PROVED` |
| NEG-003 | Verified runtime or tool action | The institution adopted it or it acquired legal/business effect | Institutional adoption, legal effect, and business effect remain `NOT_PROVED` |
| NEG-004 | `outcome_unknown` after a potentially irreversible action | The action either definitely occurred or definitely did not occur | Preserve `outcome_unknown`; do not resolve it downstream |
| NEG-005 | External reference resolves and its digest/location is available | The referenced external fact is attested and true | Preserve reference scope; the external fact and its effects remain `NOT_PROVED` |
| NEG-006 | Human approval is asserted but not independently verified or attributable | A human validly reviewed and approved the outcome | Human validation remains `NOT_PROVED` |

## Executable observation

All six cases are exercised by `tests/test_negative_cases.py`. Each case uses
synthetic identifiers and contains no private, customer, or sealed evidence.
The test fails if the external-safe handoff promotes the technical input into
any of the protected institutional claims.

Run:

```bash
python tests/test_negative_cases.py
```

Expected result:

```text
PASS NKEMBA-TRACE-NEGATIVE-CASES-001
```

## Boundary

This repository ends at the external evidence handoff. It demonstrates
preservation of proof boundaries only. Documentary reconstruction, semantic
verification, contradiction handling, human attribution, evidence ranking,
and conclusions about institutional or legal effect remain outside this public
repository.
