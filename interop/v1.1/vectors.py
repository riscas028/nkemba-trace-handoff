import copy

CLAIM = "An AI-assisted EUR 25,000 supplier payment was institutionally approved and completed."

BASE_A = {
    "chain_id":"A","transaction_id":"TX-001","amount_eur":25000,"vendor_id":"VENDOR-001","invoice_id":"INV-v3",
    "authority":{"status":"valid","authority_id":"AUTH-01","limit_eur":50000,"vendor_scope":"VENDOR-001"},
    "approval":{"status":"approved","approval_id":"APR-A","decision_at":"2026-09-03T08:00:00Z"},
    "receipt":{"status":"valid","receipt_id":"RCP-A","issued_at":"2026-09-03T08:01:00Z"},
    "document":{"status":"current","version":"v3","effective_from":"2026-09-03T07:00:00Z"},
    "outcome":{"status":"completed","settlement_id":"SET-A","completed_at":"2026-09-03T08:05:00Z"},
    "adoption":{"status":"recorded","record_id":"INST-A","recorded_at":"2026-09-03T08:10:00Z"},
    "superseded":False
}
BASE_B = copy.deepcopy(BASE_A)
BASE_B.update({
    "chain_id":"B",
    "approval":{"status":"approved","approval_id":"APR-B","decision_at":"2026-09-03T08:00:30Z"},
    "receipt":{"status":"valid","receipt_id":"RCP-B","issued_at":"2026-09-03T08:01:30Z"},
    "outcome":{"status":"completed","settlement_id":"SET-B","completed_at":"2026-09-03T08:05:30Z"},
    "adoption":{"status":"recorded","record_id":"INST-B","recorded_at":"2026-09-03T08:10:30Z"}
})

def V(i,name,expected,note=""):
    return {"id":f"NK-COMP-{i:03d}","name":name,"claim":CLAIM,"chains":[copy.deepcopy(BASE_A),copy.deepcopy(BASE_B)],"expected":expected,"note":note}

def build_vectors():
    out=[]
    v=V(1,"two_fully_valid_same_material_chains","INCOMPLETE","Two independently plausible institutional histories for the same bounded claim must not be arbitrarily collapsed."); out.append(v)
    v=V(2,"competing_valid_chains_different_vendor","INCOMPLETE"); v["chains"][1]["vendor_id"]="VENDOR-002"; v["chains"][1]["authority"]["vendor_scope"]="VENDOR-002"; out.append(v)
    v=V(3,"competing_valid_chains_different_invoice","INCOMPLETE"); v["chains"][1]["invoice_id"]="INV-v4"; out.append(v)
    v=V(4,"competing_valid_chains_different_amount","INCOMPLETE"); v["chains"][1]["amount_eur"]=24000; out.append(v)
    v=V(5,"one_valid_one_failed_outcome","PROVED","A contradicted rival should not defeat a complete valid chain."); v["chains"][1]["outcome"]["status"]="failed"; out.append(v)
    v=V(6,"chain_a_superseded_chain_b_valid","PROVED"); v["chains"][0]["superseded"]=True; out.append(v)
    v=V(7,"chain_b_superseded_chain_a_valid","PROVED"); v["chains"][1]["superseded"]=True; out.append(v)
    v=V(8,"one_valid_one_missing_adoption","PROVED"); v["chains"][1]["adoption"]["status"]="missing"; out.append(v)
    v=V(9,"one_valid_one_invalid_authority","PROVED"); v["chains"][1]["authority"]["status"]="invalid"; out.append(v)
    v=V(10,"same_transaction_conflicting_document_versions","INCOMPLETE"); v["chains"][1]["document"]["version"]="v4"; out.append(v)
    v=V(11,"one_valid_one_rejected_approval","PROVED"); v["chains"][1]["approval"]["status"]="rejected"; out.append(v)
    v=V(12,"one_valid_one_missing_outcome","PROVED"); v["chains"][1]["outcome"]["status"]="missing"; out.append(v)
    v=V(13,"later_correction_explicitly_supersedes_first","PROVED"); v["chains"][0]["superseded"]=True; v["chains"][1]["adoption"]["corrects_record_id"]="INST-A"; out.append(v)
    v=V(14,"unrelated_second_valid_chain","PROVED","A separate transaction must not contaminate the bounded claim for TX-001."); v["chains"][1]["transaction_id"]="TX-999"; v["chains"][1]["amount_eur"]=18000; v["chains"][1]["vendor_id"]="VENDOR-999"; v["chains"][1]["invoice_id"]="INV-OTHER"; out.append(v)
    return out
