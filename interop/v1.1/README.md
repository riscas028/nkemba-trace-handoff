# N'KEMBA v1.1 — Public Competing Institutional Chains Vectors

This public vector set tests a hard institutional-reconstruction failure mode:

> Two independently plausible institutional histories can coexist for the same bounded transaction.

The evaluator must not choose one arbitrarily.

## Expected decision rules

- two complete valid unsuperseded chains for the same bounded transaction, with different material facts -> `INCOMPLETE`
- two complete valid unsuperseded chains with the same material facts but different institutional histories -> `INCOMPLETE`
- one complete valid chain plus an incomplete or contradicted rival -> `PROVED`
- an explicit later correction that supersedes the earlier chain -> `PROVED`
- a valid chain for a different transaction -> irrelevant to the bounded claim

## Reproduce locally

```bash
python interop/v1.1/run_vectors.py
```

The runner exits non-zero if any expected/actual verdict differs.

## Falsification invitation

Change `vectors.json`, add a competing chain, alter a supersession relationship, or introduce a new ambiguity. If the evaluator promotes more institutional certainty than the evidence supports, that is a useful counterexample.

## Scope

Synthetic controlled institutional-logic vectors only.

This is not TRACE conformance, legal adjudication, compliance certification, or independent audit.
