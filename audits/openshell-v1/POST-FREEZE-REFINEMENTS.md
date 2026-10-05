# N’KEMBA OpenShell V1 — Post-Freeze Refinements

**Status:** public research addendum  
**Date:** 2026-10-05  
**Relationship to V1:** this document does not modify the frozen 274-case V1 corpus.

## Why this exists

The V1 corpus was frozen at 274 cases. Subsequent analysis identified additional refinements and repetitions of existing proof boundaries. To preserve reproducibility and avoid silently rewriting the frozen matrix, these observations are recorded separately rather than renumbering the original corpus.

## Refinements discussed after the V1 freeze

| Ref | Refinement | Status |
|---|---|---|
| PF-01 | Current policy after gateway restart is not historical proof of the policy that governed an earlier execution. | Documentary boundary / experiment required |
| PF-02 | Provider context is part of effective authority history; base-policy history alone is insufficient. | Documentary boundary / experiment required |
| PF-03 | Provider-profile changes can alter effective authority while the sandbox-authored base policy remains unchanged. | Documentary |
| PF-04 | Different sandboxes may observe a provider-profile update on different configuration-sync boundaries. | Documentary mechanism / experiment required |
| PF-05 | A running process may retain its prior credential reference while new processes receive the updated reference. | Documentary |
| PF-06 | Provider revocation is not retroactive rollback of an already-forwarded request. | Documentary |
| PF-07 | Authorization time, forward time, revocation time, destination receipt time and response time are distinct evidence fields. | Method / experiment required |
| PF-08 | An external receipt proves an external effect but does not, by itself, prove internal authorship. | Method / experiment required |
| PF-09 | Internal execution evidence does not, by itself, prove remote receipt. | Method / experiment required |
| PF-10 | Identical request content can belong to distinct executions; content hashes must not be used as execution identity. | Method / experiment required |

## Publication discipline

These refinements are **not represented as executed experiments**. No runtime result is claimed here.

They also do not constitute a finding that NVIDIA OpenShell is defective. They identify proof boundaries that should be tested against the exact OpenShell version, configuration and evidence channels under examination.

## Freeze rule

The authoritative V1 corpus remains:

- 274 test cases;
- frozen matrix: `MATRIX-274.csv`;
- source baseline: `SOURCES.md`;
- methodology: `METHODOLOGY.md`.

Any future executed tests should receive a new corpus/version rather than modifying the historical V1 matrix.
