import json,sys
from pathlib import Path
from evaluator import evaluate
root=Path(__file__).parent
vectors=json.loads((root/"vectors.json").read_text())
results=[]; fails=0
for v in vectors:
    actual,reasons=evaluate(v); expected=v["expected"]; ok=actual==expected
    results.append({"id":v["id"],"name":v["name"],"expected":expected,"actual":actual,"pass":ok,"reasons":reasons})
    print(f"{v['id']} {v['name']}: expected={expected} actual={actual} {'PASS' if ok else 'FAIL'}")
    fails += 0 if ok else 1
(root/"RUN_RESULT.json").write_text(json.dumps(results,indent=2))
print(f"\n{'ALL' if fails==0 else fails} {len(results)} VECTORS {'PASS' if fails==0 else 'FAILED'}")
sys.exit(1 if fails else 0)
