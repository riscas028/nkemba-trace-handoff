# N’KEMBA Independent Audit — NVIDIA OpenShell

Status: **PUBLIC / DOCUMENTARY AUDIT + EXPERIMENTAL TEST PLAN**

This audit records N’KEMBA's independent examination of the public NVIDIA OpenShell documentation. It does **not** claim that every proposed experiment has been executed, and it does not treat documentation as proof of runtime behaviour.

## Audit boundary

N’KEMBA separates:

1. **Documentary confirmation** — what the public documentation explicitly states.
2. **Experimental confirmation** — what a reproducible controlled test demonstrates.
3. **Evidence gap** — what cannot be established from the available evidence.

A vendor statement is not treated as false merely because its documented scope is narrower than a broader interpretation.

## Core N’KEMBA proof rules

- Policy proof ≠ enforcement proof.
- Detection ≠ prevention.
- Base policy ≠ effective authority.
- Loaded ≠ action governed by that revision.
- Current state ≠ historical state.
- Event identity ≠ execution identity.
- Process identity ≠ operation identity.
- Content identity ≠ execution identity.
- Internal execution evidence ≠ external effect proof.
- External receipt ≠ internal authorship.
- Validation ≠ delivery.
- Last policy re-check ≠ final wire proof.
- Credential present ≠ credential resolvable ≠ request authorized.
- Administrative change ≠ effective change ≠ action time.
- Temporal proximity ≠ causal proof.
- Absence from observation ≠ absence of execution.
- Recovery after an observation gap ≠ continuous observation.

## Current scope

The series covers policy composition, policy revisions, provider profiles, credential lifecycle, middleware, process and executable identity, dynamic code, filesystem controls, OCSF evidence, event ordering, log loss, gateway restarts, policy reloads, WebSocket boundaries, external receipts, concurrent executions and revocation timing.

The current published sequence reaches **#284**. #285 and subsequent experiments remain pending.

## Key documentary sources

- NVIDIA OpenShell Developer Guide
- Sandbox Policies
- Manage Sandbox Policies
- Provider Profiles
- Accessing Logs
- Customize Sandbox Policies

Official documentation was checked on 2026-10-06.

## Important limitation

The series contains many **test designs**. Unless an item is explicitly marked as experimentally executed, its result must not be represented as an observed runtime result.

## N’KEMBA publication rule

Every public finding must preserve:

CLAIM → SCOPE → METHOD → EVIDENCE → RESULT → REPRODUCTION → LIMITATIONS.

A PASS means only that the stated proposition is supported at the stated evidence level. It is not a certification of OpenShell as a whole.
