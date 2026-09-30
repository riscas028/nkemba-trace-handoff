# N’KEMBA — Public System Overview

N’KEMBA is a documentary and institutional reconstruction architecture for AI-assisted and digitally mediated decisions.

It is designed to answer a question that individual audit, provenance, execution-trace, document-management, and cryptographic systems do not answer on their own:

> **Does the available evidence actually support the institutional conclusion being asserted?**

## The complete public model

N’KEMBA brings together, in one evidence-oriented reconstruction:

**sources → documents → versions → chronology → events → technical execution → authority → human decisions → external outcomes → institutional adoption → proof status**

The system keeps these dimensions distinct while allowing them to be evaluated together.

A technically valid event is not automatically an authorized decision.
A authorized action is not automatically proof of external completion.
A document digest is not automatically proof that the document was operative.
A human assertion is not automatically proof of human validation.
A runtime attestation is not automatically proof of institutional adoption.

N’KEMBA therefore preserves the boundary between what the record establishes and what remains unsupported.

## Proof states

The public model explicitly preserves states such as:

- `PROVED`
- `NOT_PROVED`
- `INCOMPLETE`
- `CONTRADICTED`
- unknown / unavailable evidence

The purpose is not to manufacture certainty from incomplete records.

Where a required evidentiary dimension is missing, unresolved, conflicting, stale, or otherwise unsupported, the conclusion remains constrained accordingly.

## What N’KEMBA adds to existing evidence systems

N’KEMBA can consume evidence produced by other systems rather than replacing them.

For example, verified TRACE execution evidence can support the runtime dimension of an N’KEMBA reconstruction. It does not, by itself, establish authority, operative documents, external completion, or institutional adoption.

The public TRACE/N’KEMBA cross-walk documents this separation explicitly.

## Evidence Pack and independent verification

N’KEMBA can produce a portable Evidence Pack containing the relevant evidence state, provenance, integrity information, proof boundaries, and human validation context.

Integrity mechanisms can establish that the package or selected records have not been altered after sealing.

They do **not** by themselves establish factual truth, legal validity, completeness, regulatory compliance, or independent certification.

An independent verifier can therefore check integrity without having to trust the application UI.

## Contradictions and negative evidence

N’KEMBA does not treat contradictory or missing information as an inconvenience to be silently resolved.

The public demonstrations include adversarial cases where:

- verified execution does not prove settlement;
- a verified notification does not prove that a person was informed;
- a verified tool action does not prove institutional adoption;
- an unknown outcome remains unknown;
- a reference or digest does not become an attestation of the referenced fact;
- an asserted approval does not become verified human authority without supporting evidence.

## Interoperability

N’KEMBA is designed to sit above heterogeneous evidence sources.

TRACE is one interoperable evidence source. Other documentary, technical, organizational, and external records can be evaluated alongside it.

The objective is not to redefine upstream standards. It is to preserve their evidence states and evaluate the downstream institutional question without silently promoting one layer into another.

## Public boundary

This repository intentionally demonstrates the public behaviour, interfaces, evidence boundaries, reproducible tests, interoperability model, and evaluation surface.

It does **not** disclose the proprietary implementation of N’KEMBA’s institutional-reconstruction engine, internal semantic logic, contradiction handling, heuristics, or other confidential R&D.

The public release is therefore intended to make the system understandable and testable without publishing the mechanism that would enable direct reproduction of the proprietary core.

## Important limitation

N’KEMBA is a verification and reconstruction architecture. It is not a guarantee that every conclusion is factually true, legally valid, complete, or correct merely because evidence exists.

Its central discipline is narrower and more useful:

> **Never claim more than the evidence supports.**