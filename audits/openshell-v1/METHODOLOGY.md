# N’KEMBA OpenShell V1 — Methodology

## Objective

Determine whether a security/control claim can be converted into reproducible, version-bound, causally attributable proof.

## Core proof boundaries

- Policy Proof ≠ Enforcement Proof.
- Detection ≠ Prevention.
- Accepted ≠ Validated ≠ Loaded.
- Loaded ≠ Action Governed.
- Current State ≠ Historical State.
- Event Identity ≠ Execution Identity.
- Process Identity ≠ Operation Identity.
- Internal Execution Proof ≠ External Effect Proof.
- External Receipt ≠ Internal Authorship.
- Validation ≠ Delivery.
- Delivery ≠ Causal Attribution.

## Version binding

Preserve, where available: OpenShell version/revision; policy revision/effective policy; provider/profile identity and context; prover/schema version; sandbox/process/executable identity; execution ID/nonce; state/action timestamps; raw logs; external receipts; relevant hashes.

A later `policy get --full` result is not automatic proof of what governed an earlier action.

## Experimental design

Use a controlled sandbox, controlled destination where possible, unique nonce, independent receipt, independently recorded timestamps, local plus gateway/OCSF evidence, negative controls, reproducible configuration, raw artefacts and explicit uncertainty.

## Result classes

**DOCUMENTARY PASS:** official documentation directly supports the mechanism; not an execution result.

**EXPERIMENT REQUIRED:** documentation defines the mechanism; concrete runtime behaviour remains untested.

**PARTIAL / EVIDENCE GAP:** one part of the chain is proven but another is missing.

**NOT PROVED:** evidence is insufficient; gaps must not be filled by inference.

## Causal chain

Preferred chain:

`execution_id → process → policy/provider context → decision → request/hash → destination receipt`

A receipt proves an external effect; it does not automatically prove its internal author. An internal event does not automatically prove remote receipt.

## Observation loss and ordering

An observation channel is not reality itself. Missing stream evidence is not evidence that an action did not occur. Out-of-order arrival is not causal order. Preserve observation boundaries and uncertainty.

## Public reporting

Each finding should state claim, scope, source/version/date, method, raw evidence, result, reproduction, limitations, and documentary/experimental classification.

## Freeze

V1 contains exactly **274 test cases**. Later discoveries are V1 errata or V1.1/V2 additions. The frozen matrix must not silently change.
