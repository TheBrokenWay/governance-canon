"""Runner for EXP-002. Single run, first result recorded."""
import json, platform, sys, hashlib
from pathlib import Path
from probes import PROBES, REQUIRED, REGRESSION, REMEDY_SURFACE
from kernel import Violation

HERE = Path(__file__).parent

def main():
    records = []
    for fn in PROBES:
        try:
            pid, channel, d = fn()
            req = REQUIRED[pid]
            records.append({
                "probe": pid, "channel": channel, "required": req,
                "verdict": d.verdict, "derived_subject": d.derived_subject,
                "matches_required": (None if req is None else d.verdict == req),
                "violations": d.violations, "reasons": d.reasons, "error": None})
        except Exception as e:  # noqa: BLE001
            records.append({"probe": fn.__name__, "channel": None, "required": None,
                            "verdict": None, "derived_subject": None,
                            "matches_required": False, "violations": [], "reasons": [],
                            "error": f"{type(e).__name__}: {e}"})
    reg = [r for r in records if r["probe"] in REGRESSION]
    rem = [r for r in records if r["probe"] in REMEDY_SURFACE]
    k = next(r for r in records if r["probe"] == "K")
    ctrl = next(r for r in records if r["probe"] == "CONTROL")
    out = {
        "experiment": "EXP-002-subject-binding", "preregistered": "2026-09-14",
        "environment": {"python": sys.version.split()[0], "platform": platform.platform()},
        "source_digests": {n: hashlib.sha256((HERE/n).read_bytes()).hexdigest()
                           for n in ("kernel.py", "probes.py", "run.py")},
        "endpoint_1_regression": {
            "definition": "original probes A-H permitting execution (target 0)",
            "value": sum(1 for r in reg if r["verdict"] == "EXECUTE"), "of": len(reg),
            "probes_permitting": [r["probe"] for r in reg if r["verdict"] == "EXECUTE"]},
        "endpoint_2_remedy_surface": {
            "definition": "new probes I,J,L,M deviating from required (target 0)",
            "value": sum(1 for r in rem if not r["matches_required"]), "of": len(rem),
            "probes_deviating": [r["probe"] for r in rem if not r["matches_required"]]},
        "endpoint_3_probe_K": {
            "definition": "reported as observed, not scored",
            "verdict": k["verdict"], "derived_subject": k["derived_subject"],
            "violations": k["violations"], "reasons": k["reasons"]},
        "control_valid": ctrl["verdict"] == "EXECUTE",
        "errors": sum(1 for r in records if r["error"]),
        "records": records}
    print(json.dumps(out, indent=2))
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "RESULT.json"
    if output.exists():
        raise SystemExit(f"refusing to overwrite existing result: {output}")
    output.write_text(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
