import json,sys
from pathlib import Path
from datetime import datetime

def parse_ts(s):
    if not s: return None
    return datetime.fromisoformat(s.replace("Z","+00:00"))

def chain_state(c):
    reasons=[]
    if c.get("superseded"):
        return "SUPERSEDED",["chain explicitly superseded"]
    if c["authority"].get("status")!="valid":
        return "CONTRADICTED",["authority invalid"]
    if c["approval"].get("status")=="rejected":
        return "CONTRADICTED",["approval rejected"]
    if c["approval"].get("status")!="approved":
        return "NOT_PROVED",["approval missing/unproved"]
    if c["receipt"].get("status")!="valid":
        return "CONTRADICTED",["receipt invalid"]
    if c["document"].get("status")=="superseded":
        return "CONTRADICTED",["document superseded"]
    if c["document"].get("status")!="current":
        return "NOT_PROVED",["document missing/unproved"]
    if c["outcome"].get("status") in ("failed","reversed"):
        return "CONTRADICTED",[f"outcome {c['outcome'].get('status')}"]
    if c["outcome"].get("status")!="completed":
        return "NOT_PROVED",["external outcome missing"]
    if c["adoption"].get("status") in ("rejected","superseded"):
        return "CONTRADICTED",[f"adoption {c['adoption'].get('status')}"]
    if c["adoption"].get("status")!="recorded":
        return "NOT_PROVED",["institutional adoption missing"]
    if c["authority"].get("limit_eur",0)<c.get("amount_eur",0):
        return "CONTRADICTED",["authority amount insufficient"]
    if c["authority"].get("vendor_scope")!=c.get("vendor_id"):
        return "CONTRADICTED",["authority vendor scope mismatch"]
    return "VALID",["chain individually supports its own bounded history"]

def material_signature(c):
    return (c.get("transaction_id"),c.get("amount_eur"),c.get("vendor_id"),c.get("invoice_id"),
            c.get("document",{}).get("version"))

def evaluate(v):
    chains=v["chains"]
    states=[chain_state(c) for c in chains]
    target_tx=chains[0]["transaction_id"]
    relevant=[]
    for c,(state,reasons) in zip(chains,states):
        if c.get("transaction_id")==target_tx:
            relevant.append((c,state,reasons))

    valid=[x for x in relevant if x[1]=="VALID"]

    for c,state,reasons in valid:
        corrects=c.get("adoption",{}).get("corrects_record_id")
        if corrects:
            for other,ostate,oreasons in relevant:
                if other.get("adoption",{}).get("record_id")==corrects and other.get("superseded"):
                    return "PROVED",["later valid correction explicitly supersedes prior institutional chain"]

    if len(valid)==0:
        if any(x[1]=="CONTRADICTED" for x in relevant):
            return "CONTRADICTED",["no valid institutional chain; at least one relevant chain contradicted"]
        return "NOT PROVED",["no complete valid institutional chain"]

    if len(valid)==1:
        return "PROVED",["exactly one complete non-superseded institutional chain supports the bounded claim"]

    sigs={material_signature(c) for c,_,_ in valid}
    if len(sigs)>1:
        return "INCOMPLETE",["multiple individually valid chains disagree on material institutional facts"]

    identities={(c["approval"].get("approval_id"),c["receipt"].get("receipt_id"),
                 c["outcome"].get("settlement_id"),c["adoption"].get("record_id")) for c,_,_ in valid}
    if len(identities)>1:
        return "INCOMPLETE",["multiple individually valid unsuperseded chains support the same claim but differ in institutional history"]

    return "PROVED",["multiple records collapse to the same institutional history"]

if __name__=="__main__":
    v=json.loads(Path(sys.argv[1]).read_text())
    verdict,reasons=evaluate(v)
    print(json.dumps({"verdict":verdict,"reasons":reasons},indent=2))
