# N'KEMBA v0.9 — TRACE-shaped Cryptographic Interoperability Vectors

This pack tests the exact boundary N'KEMBA is proposing:

**valid upstream evidence is preserved, but it cannot be promoted into institutional proof without independently checked authority, operative documents, external outcomes and institutional adoption.**

The upstream fixture is deliberately **TRACE-shaped**, using current TRACE v0.2 field names including `eat_profile`, `runtime`, `policy`, `tool_transcript`, `origin`, `references`, `build_provenance`, `appraisal`, `cnf` and an embedded Ed25519 `signature`.

It is **not claimed to be a TRACE-conformant test vector**. It is a downstream interoperability demonstrator.

## Important TRACE semantics preserved

- `origin.kind = log-import` uses `runtime.platform = software-only`.
- `software-only` is not promoted to hardware-attested evidence.
- `references` are treated as signed pointers, not proof of their targets.
- an unresolved reference does not invalidate the signed upstream record; it leaves the downstream institutional fact unproved.
- a resolved object whose digest differs from the signed reference is rejected for the institutional reconstruction.
- a valid signed upstream record by itself returns `NOT PROVED` for the bounded institutional payment claim.

## Cryptographic checks

Two independent Ed25519 checks are performed:

1. embedded signature on the TRACE-shaped record, over canonical JSON with `signature` absent;
2. action receipt signature, over its canonical payload.

## Twelve vectors

The suite includes:
- full consistent chain -> PROVED
- valid upstream record only -> NOT PROVED
- tampered signed TRACE-shaped record -> CONTRADICTED
- unresolved authority pointer -> NOT PROVED
- insufficient authority -> CONTRADICTED
- tampered signed receipt -> CONTRADICTED
- failed outcome -> CONTRADICTED
- missing outcome -> NOT PROVED
- superseded document -> CONTRADICTED
- wrong adoption linkage -> CONTRADICTED
- missing adoption -> NOT PROVED
- resolved reference digest mismatch -> CONTRADICTED

Run `python run_vectors.py`. Non-zero exit means at least one vector failed.
