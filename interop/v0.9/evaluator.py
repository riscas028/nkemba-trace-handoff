import json, sys, base64, hashlib
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from cryptography.exceptions import InvalidSignature

def b64ud(s):
    return base64.urlsafe_b64decode(s + "="*((4-len(s)%4)%4))
def canonical(o):
    return json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def digest(o):
    return "sha256:"+hashlib.sha256(canonical(o)).hexdigest()

def verify_record(rec):
    if not rec.get("signature"): return "missing"
    unsigned=json.loads(json.dumps(rec)); sig=unsigned.pop("signature")
    try:
        jwk=unsigned["cnf"]["jwk"]
        pk=Ed25519PublicKey.from_public_bytes(b64ud(jwk["x"]))
        pk.verify(b64ud(sig),canonical(unsigned))
        return "valid"
    except (KeyError,ValueError,InvalidSignature):
        return "invalid"

def verify_receipt(ar):
    if not ar or not ar.get("signature"): return "missing"
    try:
        pk=Ed25519PublicKey.from_public_bytes(b64ud(ar["public_key_x"]))
        pk.verify(b64ud(ar["signature"]),canonical(ar["payload"]))
        return "valid"
    except (KeyError,ValueError,InvalidSignature):
        return "invalid"

def evaluate(v):
    rec=v["trace_shaped_record"]; inst=v["institutional_evidence"]
    rs=verify_record(rec)
    if rs=="invalid": return "CONTRADICTED",["upstream record signature invalid"]
    if rs=="missing": return "NOT PROVED",["upstream record signature missing"]

    # TRACE semantics preserved: software-only/log-import is not treated as attested hardware evidence.
    # It can still be a signed upstream record, but cannot complete the institutional claim alone.

    resolved=inst.get("resolved_references",{})
    refs={r["rel"]:r for r in rec.get("references",[])}
    required_refs=("authorized-intent","approval-outcome")
    for rel in required_refs:
        if rel not in resolved:
            return "NOT PROVED",[f"{rel} reference unresolved; pointer is not proof"]
        if rel in refs and refs[rel].get("digest") and digest(resolved[rel]) != refs[rel]["digest"]:
            return "CONTRADICTED",[f"{rel} resolved object does not match signed digest"]

    auth=resolved["authorized-intent"]
    approval=resolved["approval-outcome"]
    if auth.get("limit_eur",0) < 25000:
        return "CONTRADICTED",["authority limit below transaction amount"]
    if auth.get("vendor_scope") != "VENDOR-SYNTH-001":
        return "CONTRADICTED",["authority vendor scope mismatch"]
    if approval.get("decision") != "approved":
        return "CONTRADICTED",["approval outcome is not approved"]

    ar=inst.get("action_receipt")
    ars=verify_receipt(ar)
    if ars=="invalid": return "CONTRADICTED",["action receipt signature invalid"]
    if ars=="missing": return "NOT PROVED",["action receipt missing/unverifiable"]
    rp=ar["payload"]

    doc=inst.get("document",{})
    if doc.get("status")=="superseded": return "CONTRADICTED",["operative document superseded"]
    if doc.get("status") in (None,"missing"): return "NOT PROVED",["operative document missing"]
    for k in ("amount_eur","vendor_id","invoice_id"):
        if doc.get(k)!=rp.get(k): return "CONTRADICTED",[f"document/receipt mismatch: {k}"]

    out=inst.get("external_outcome",{})
    if out.get("status") in ("failed","reversed"): return "CONTRADICTED",[f"external outcome {out.get('status')}"]
    if out.get("status") in (None,"missing"): return "NOT PROVED",["external outcome missing"]
    for k in ("amount_eur","vendor_id","invoice_id"):
        if out.get(k)!=rp.get(k): return "CONTRADICTED",[f"outcome/receipt mismatch: {k}"]

    adoption=inst.get("institutional_adoption",{})
    if adoption.get("status") in ("rejected","superseded"): return "CONTRADICTED",[f"institutional adoption {adoption.get('status')}"]
    if adoption.get("status") in (None,"missing"): return "NOT PROVED",["institutional adoption missing"]
    if adoption.get("receipt_id")!=rp.get("receipt_id"): return "CONTRADICTED",["adoption references different receipt"]
    if adoption.get("invoice_id")!=rp.get("invoice_id"): return "CONTRADICTED",["adoption references different invoice"]
    if adoption.get("settlement_id")!=out.get("settlement_id"): return "CONTRADICTED",["adoption references different settlement"]

    return "PROVED",["signed upstream evidence plus independently checked institutional evidence are mutually consistent"]

if __name__=="__main__":
    v=json.loads(Path(sys.argv[1]).read_text())
    verdict,reasons=evaluate(v)
    print(json.dumps({"verdict":verdict,"reasons":reasons},indent=2))
