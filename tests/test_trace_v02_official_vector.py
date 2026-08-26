#!/usr/bin/env python3
"""External-safe interoperability test for a TRACE v0.2 signed test vector.

The vector values below are the public TRACE v0.2 UTF-16 key-order test vector
(03-utf16-key-order.json). This test verifies only the signed technical record
integrity and then asserts N'KEMBA's downstream proof boundary. It does not
claim TRACE certification, hardware attestation, or institutional facts.
"""
import base64
import json

try:
    from cryptography.exceptions import InvalidSignature
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
except ImportError as exc:
    raise SystemExit("Install test dependency: pip install cryptography") from exc

TRUSTED_X = "Be97jkxfFpVXzj9B-gwpMzv5t8PH30Edd-J7AIlrdoA"
SIGNATURE = "CjOuPwCnxnwegFjguiSCi-_xPg3iOwnCgyKuKYnV0OorofjPJrkOLn3dUFa-6tVf0z8EDiHaczl6AN46MuBtCQ"

RECORD = {
    "eat_profile": "tag:agentrust-io.com,2026:trace-v0.2",
    "iat": 1785000000,
    "subject": "spiffe://factory.example/agent/payments/prod",
    "model": {"provider": "anthropic", "model_id": "claude-sonnet-4-6"},
    "runtime": {"platform": "software-only", "measurement": "sha256:" + "0" * 64},
    "policy": {"bundle_hash": "sha256:" + "a" * 64, "enforcement_mode": "enforce"},
    "data_class": "confidential",
    "build_provenance": {"slsa_level": 0, "digest": "sha256:" + "b" * 64},
    "appraisal": {"status": "affirming", "verifier": "https://verifier.example/v1"},
    "transparency": "https://rekor.example/api/v1/log/entries/0",
    "cnf": {"jwk": {"kty": "OKP", "crv": "Ed25519", "x": TRUSTED_X,
                    "zk😀": "sorts-first-under-rfc-8785",
                    "zk�": "sorts-second-under-rfc-8785"}},
}


def b64u(value):
    return base64.urlsafe_b64decode(value + "=" * ((4 - len(value) % 4) % 4))


def jcs(value):
    """Minimal RFC 8785 canonicalizer sufficient for this official vector."""
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    if isinstance(value, list):
        return "[" + ",".join(jcs(v) for v in value) + "]"
    if isinstance(value, dict):
        keys = sorted(value, key=lambda s: s.encode("utf-16-be"))
        return "{" + ",".join(jcs(k) + ":" + jcs(value[k]) for k in keys) + "}"
    raise TypeError(type(value))


def verifies(record):
    public_key = Ed25519PublicKey.from_public_bytes(b64u(TRUSTED_X))
    try:
        public_key.verify(b64u(SIGNATURE), jcs(record).encode("utf-8"))
        return True
    except InvalidSignature:
        return False


assert verifies(RECORD), "official signed vector did not verify"

tampered = json.loads(json.dumps(RECORD, ensure_ascii=False))
tampered["data_class"] = "public"
assert not verifies(tampered), "tampered record unexpectedly verified"

boundary = {
    "technical_record_integrity": "PROVED_BY_SIGNATURE",
    "hardware_attestation": "NOT_PROVED_SOFTWARE_ONLY",
    "physical_completion": "NOT_PROVED",
    "human_validation": "NOT_PROVED",
    "institutional_adoption": "NOT_PROVED",
    "legal_effect": "NOT_PROVED",
    "business_effect": "NOT_PROVED",
}

assert boundary["physical_completion"] == "NOT_PROVED"
assert boundary["human_validation"] == "NOT_PROVED"
assert boundary["legal_effect"] == "NOT_PROVED"
assert boundary["business_effect"] == "NOT_PROVED"

print("PASS NKEMBA-TRACE-SIGNED-VECTOR-001")
