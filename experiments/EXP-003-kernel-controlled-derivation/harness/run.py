"""Runner for EXP-003. Single run, first result recorded."""
import json, platform, sys, hashlib
from pathlib import Path
from probes import (PROBES, REQUIRED, REGRESSION, CLASS, AVAILABILITY, UNPREDICTED)
HERE = Path(__file__).parent

def main():
    recs = []
    for fn in PROBES:
        try:
            pid, ch, d = fn()
            req = REQUIRED[pid]
            recs.append({"probe": pid, "channel": ch, "required": req,
                         "verdict": d.verdict, "derived_subject": d.derived_subject,
                         "matches_required": (None if req is None else d.verdict == req),
                         "violations": d.violations, "reasons": d.reasons, "error": None})
        except Exception as e:  # noqa: BLE001
            recs.append({"probe": fn.__name__, "channel": None, "required": None,
                         "verdict": None, "derived_subject": None,
                         "matches_required": False, "violations": [], "reasons": [],
                         "error": f"{type(e).__name__}: {e}"})
    g = lambda s: [r for r in recs if r["probe"] in s]
    out = {
      "experiment": "EXP-003-kernel-controlled-derivation", "preregistered": "2026-09-14",
      "environment": {"python": sys.version.split()[0], "platform": platform.platform()},
      "source_digests": {n: hashlib.sha256((HERE/n).read_bytes()).hexdigest()
                         for n in ("kernel.py","probes.py","run.py")},
      "endpoint_1_regression": {
        "definition": "EXP-002 probes permitting execution (target 0, K included)",
        "value": sum(1 for r in g(REGRESSION) if r["verdict"]=="EXECUTE"),
        "of": len(REGRESSION),
        "permitting": [r["probe"] for r in g(REGRESSION) if r["verdict"]=="EXECUTE"]},
      "endpoint_2_class": {
        "definition": "N,O,P,Q deviating from required (target 0)",
        "value": sum(1 for r in g(CLASS) if not r["matches_required"]), "of": len(CLASS),
        "deviating": [r["probe"] for r in g(CLASS) if not r["matches_required"]]},
      "endpoint_3_availability": {
        "definition": "L1-L5 refused (target 0 refusals)",
        "value": sum(1 for r in g(AVAILABILITY) if r["verdict"]!="EXECUTE"),
        "of": len(AVAILABILITY),
        "refused": [r["probe"] for r in g(AVAILABILITY) if r["verdict"]!="EXECUTE"]},
      "endpoint_4_unpredicted": {r["probe"]: {"verdict": r["verdict"],
        "derived_subject": r["derived_subject"], "violations": r["violations"],
        "reasons": r["reasons"]} for r in g(UNPREDICTED)},
      "control_valid": next(r for r in recs if r["probe"]=="CONTROL")["verdict"]=="EXECUTE",
      "errors": sum(1 for r in recs if r["error"]), "records": recs}
    print(json.dumps(out, indent=2))
    (HERE.parent/"RESULT.json").write_text(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
