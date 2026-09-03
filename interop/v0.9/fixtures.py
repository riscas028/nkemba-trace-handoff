import json, base64, hashlib
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

def b64u(b):
    return base64.urlsafe_b64encode(b).rstrip(b"=").decode()

def canonical(o):
    return json.dumps(o, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()

def digest(o):
    return "sha256:" + hashlib.sha256(canonical(o)).hexdigest()

_seed = bytes.fromhex("33"*32)
_sk = Ed25519PrivateKey.from_private_bytes(_seed)
_pk = _sk.public_key()
_x = b64u(_pk.public_bytes(serialization.Encoding.Raw, serialization.PublicFormat.Raw))

AUTHORITY = {
    "authority_id":"AUTH-SYNTH-001","actor":"approver-17","role":"payment_approver",
    "limit_eur":50000,"vendor_scope":"VENDOR-SYNTH-001",
    "valid_from":"2026-01-01T00:00:00Z","valid_to":"2026-12-31T23:59:59Z"
}
APPROVAL = {
    "approval_id":"APR-SYNTH-001","authority_id":"AUTH-SYNTH-001","amount_eur":25000,
    "vendor_id":"VENDOR-SYNTH-001","invoice_id":"INV-2026-09-v3","decision":"approved"
}
BEHAVIOR = {"behavior_id":"BEH-SYNTH-001","tool_calls":1}

def signed_record():
    r = {
        "eat_profile":"tag:agentrust-io.com,2026:trace-v0.2",
        "iat":1788422400,
        "subject":"spiffe://example.org/agent/payment-01",
        "model":{"provider":"synthetic","model_id":"model-test","version":"1"},
        "runtime":{"platform":"software-only","measurement":"sha256:"+"11"*32},
        "policy":{"bundle_hash":"sha256:"+"22"*32,"enforcement_mode":"declared","version":"1"},
        "data_class":"internal",
        "tool_transcript":{"hash":"sha256:"+"44"*32,"call_count":1},
        "origin":{"kind":"log-import","producer":"synthetic-upstream","source_event_id":"evt-001","ingested_at":1788422460},
        "references":[
            {"rel":"authorized-intent","id":"AUTH-SYNTH-001","resolver":"synthetic-authority-registry","digest":digest(AUTHORITY)},
            {"rel":"approval-outcome","id":"APR-SYNTH-001","resolver":"synthetic-approval-system","digest":digest(APPROVAL)},
            {"rel":"behavior-trace","id":"BEH-SYNTH-001","resolver":"synthetic-behavior-store","digest":digest(BEHAVIOR)}
        ],
        "build_provenance":{"slsa_level":0,"digest":"sha256:"+"55"*32},
        "appraisal":{"status":"none","verifier":"https://example.org/synthetic-verifier"},
        "cnf":{"jwk":{"kty":"OKP","crv":"Ed25519","x":_x,"kid":"synthetic-ed25519-01"}}
    }
    r["signature"] = b64u(_sk.sign(canonical(r)))
    return r

def signed_receipt():
    p = {"receipt_id":"RCP-SYNTH-001","amount_eur":25000,"vendor_id":"VENDOR-SYNTH-001",
         "invoice_id":"INV-2026-09-v3","status":"issued"}
    return {"payload":p,"signature":b64u(_sk.sign(canonical(p))),"public_key_x":_x}

def base_vector():
    return {
        "claim":"An AI-assisted EUR 25,000 supplier payment was institutionally approved and completed.",
        "trace_shaped_record": signed_record(),
        "institutional_evidence":{
            "resolved_references":{
                "authorized-intent":json.loads(json.dumps(AUTHORITY)),
                "approval-outcome":json.loads(json.dumps(APPROVAL)),
                "behavior-trace":json.loads(json.dumps(BEHAVIOR))
            },
            "action_receipt": signed_receipt(),
            "document":{"status":"current","invoice_id":"INV-2026-09-v3","amount_eur":25000,"vendor_id":"VENDOR-SYNTH-001"},
            "external_outcome":{"status":"completed","amount_eur":25000,"vendor_id":"VENDOR-SYNTH-001","invoice_id":"INV-2026-09-v3","settlement_id":"SET-SYNTH-001"},
            "institutional_adoption":{"status":"recorded","receipt_id":"RCP-SYNTH-001","invoice_id":"INV-2026-09-v3","settlement_id":"SET-SYNTH-001"}
        }
    }

def apply_mutation(v, mutation):
    i=v["institutional_evidence"]
    if mutation=="none": pass
    elif mutation=="runtime_only":
        v["institutional_evidence"]={"resolved_references":{},"action_receipt":None,"document":{"status":"missing"},"external_outcome":{"status":"missing"},"institutional_adoption":{"status":"missing"}}
    elif mutation=="tamper_trace":
        v["trace_shaped_record"]["references"][0]["digest"]="sha256:"+"99"*32
    elif mutation=="unresolved_authority":
        i["resolved_references"].pop("authorized-intent",None)
    elif mutation=="insufficient_authority":
        i["resolved_references"]["authorized-intent"]["limit_eur"]=10000
    elif mutation=="tamper_receipt":
        i["action_receipt"]["payload"]["amount_eur"]=26000
    elif mutation=="failed_outcome":
        i["external_outcome"]["status"]="failed"
    elif mutation=="missing_outcome":
        i["external_outcome"]={"status":"missing"}
    elif mutation=="superseded_document":
        i["document"]["status"]="superseded"
    elif mutation=="wrong_adoption_receipt":
        i["institutional_adoption"]["receipt_id"]="RCP-SYNTH-999"
    elif mutation=="missing_adoption":
        i["institutional_adoption"]={"status":"missing"}
    elif mutation=="resolved_digest_mismatch":
        i["resolved_references"]["approval-outcome"]["amount_eur"]=24000
    else:
        raise ValueError("unknown mutation: "+mutation)
    return v
