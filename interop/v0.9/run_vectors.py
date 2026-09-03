import json, sys
from pathlib import Path
from evaluator import evaluate
from fixtures import base_vector, apply_mutation

root=Path(__file__).parent
specs=json.loads((root/"vectors.json").read_text())
results=[]; fails=0
for spec in specs:
    v=apply_mutation(base_vector(), spec["mutation"])
    v.update({"id":spec["id"],"name":spec["name"]})
    actual,reasons=evaluate(v); expected=spec["expected"]; ok=actual==expected
    results.append({"id":spec["id"],"name":spec["name"],"mutation":spec["mutation"],"expected":expected,"actual":actual,"pass":ok,"reasons":reasons})
    print(f"{spec['id']} {spec['name']}: expected={expected} actual={actual} {'PASS' if ok else 'FAIL'}")
    fails += 0 if ok else 1
(root/"RUN_RESULT.json").write_text(json.dumps(results,indent=2))
print(f"\n{'ALL' if fails==0 else fails} {len(results)} VECTORS {'PASS' if fails==0 else 'FAILED'}")
sys.exit(1 if fails else 0)
