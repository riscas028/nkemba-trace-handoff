# N’KEMBA — OpenShell V1 Audit Corpus

This directory freezes the N’KEMBA documentary audit corpus for NVIDIA OpenShell at **V1 / 274 test cases**.

This is an **independent audit methodology**, not a claim that NVIDIA OpenShell is defective.

## Evidence discipline

- **DOCUMENTARY** — mechanism supported by current NVIDIA documentation.
- **EXPERIMENT REQUIRED** — mechanism documented, concrete runtime behaviour still requires reproducible execution.
- **N’KEMBA METHOD** — proposed audit/evidence mechanism, not a native OpenShell guarantee.

No test is represented as executed merely because it is in this matrix.

## Frozen baseline

Primary sources are NVIDIA's current OpenShell documentation and public repository. NVIDIA distinguishes sandbox base policy from effective policy and documents provider-derived policy composition and synchronization. citeturn0search2turn0search5

The official NVIDIA/OpenShell repository is public and Apache-2.0 licensed. citeturn0search3

## Files

- `METHODOLOGY.md`
- `MATRIX-274.csv`
- `SOURCES.md`

## Publication rule

Every future finding must distinguish what NVIDIA documents, what N’KEMBA proposes/tests, and what an executed experiment actually demonstrated. A documentation limitation is not automatically a product failure.
