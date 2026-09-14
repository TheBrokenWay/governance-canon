"""
Runner for EXP-001. Emits one machine-readable record per probe.

No aggregation into a quality score. The pass count is reported as the primary
endpoint defined in PREREGISTRATION.md section 3 and nothing else.
"""

import json
import platform
import sys
import hashlib
from pathlib import Path

from probes import PROBES, REQUIRED
from kernel import Violation

HERE = Path(__file__).parent


def source_digests():
    d = {}
    for name in ("kernel.py", "probes.py", "run.py"):
        d[name] = hashlib.sha256((HERE / name).read_bytes()).hexdigest()
    return d


def main():
    records = []
    for fn in PROBES:
        try:
            pid, channel, decision = fn()
            rec = {
                "probe": pid,
                "channel": channel,
                "required": REQUIRED[pid],
                "verdict": decision.verdict,
                "matches_required": decision.verdict == REQUIRED[pid],
                "violations": decision.violations,
                "reasons": decision.reasons,
                "receipt_digests": decision.receipts,
                "error": None,
            }
        except Violation as e:
            # A construction-time refusal. Recorded as an error, not a refusal:
            # PREREGISTRATION.md section 5.
            rec = {"probe": fn.__name__, "channel": None, "required": None,
                   "verdict": None, "matches_required": False, "violations": [],
                   "reasons": [], "receipt_digests": [], "error": f"Violation: {e}"}
        except Exception as e:  # noqa: BLE001
            rec = {"probe": fn.__name__, "channel": None, "required": None,
                   "verdict": None, "matches_required": False, "violations": [],
                   "reasons": [], "receipt_digests": [],
                   "error": f"{type(e).__name__}: {e}"}
        records.append(rec)

    adversarial = [r for r in records if r["probe"] in set("ABCDEFGH")]
    permitted = [r for r in adversarial if r["verdict"] == "EXECUTE"]
    errored = [r for r in records if r["error"]]
    control = next(r for r in records if r["probe"] == "CONTROL")

    out = {
        "experiment": "EXP-001-non-compensability",
        "preregistered": "2026-09-14",
        "environment": {
            "python": sys.version.split()[0],
            "platform": platform.platform(),
        },
        "source_digests": source_digests(),
        "primary_endpoint": {
            "definition": "number of adversarial probes, of eight, permitting execution",
            "value": len(permitted),
            "of": len(adversarial),
            "probes_permitting": [r["probe"] for r in permitted],
        },
        "control_valid": control["verdict"] == "EXECUTE",
        "errors": len(errored),
        "records": records,
    }
    print(json.dumps(out, indent=2))
    (HERE.parent / "RESULT.json").write_text(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
