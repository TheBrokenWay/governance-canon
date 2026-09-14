#!/usr/bin/env python3
"""Compare a fresh harness run with its immutable recorded result.

The comparison deliberately ignores environment strings and nonce-like values,
but fails on endpoint classifications, errors, probe IDs, and verdicts.
"""
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).parent
RUNS = [
    ("experiments/EXP-001-non-compensability", "RESULT-v0.2.0.json", "primary_endpoint"),
    ("experiments/EXP-002-subject-binding", "RESULT-v0.2.0.json", "endpoint_1_regression"),
    ("experiments/EXP-003-kernel-controlled-derivation", "RESULT-v0.2.0-final.json", "endpoint_1_regression"),
]


def stable(data):
    """Remove only run-specific nonce text; retain all semantic record fields."""
    if isinstance(data, str):
        return re.sub(r"[0-9a-f]{12,}", "<nonce>", data)
    if isinstance(data, list):
        return [stable(item) for item in data]
    if isinstance(data, dict):
        return {key: stable(value) for key, value in data.items()
                if key not in {"environment", "source_digests"}}
    return data


def source_digests(directory):
    return {name: hashlib.sha256((directory / "harness" / name).read_bytes()).hexdigest()
            for name in ("kernel.py", "probes.py", "run.py")
            if (directory / "harness" / name).exists()}


def main():
    failures = []
    for rel, result_name, endpoint in RUNS:
        d = ROOT / rel
        recorded = json.loads((d / result_name).read_text())
        if recorded.get("source_digests") != source_digests(d):
            failures.append(f"{rel}: recorded source digests do not match current tree")
            continue
        with tempfile.TemporaryDirectory(prefix="canon-repro-") as td:
            output = str(Path(td) / "result.json")
            proc = subprocess.run([sys.executable, str(d / "harness" / "run.py"), output],
                                  capture_output=True, text=True, check=False)
        if proc.returncode:
            failures.append(f"{rel}: harness exited {proc.returncode}")
            continue
        fresh = json.loads(proc.stdout)
        for key in (endpoint, "records", "control_valid", "errors"):
            if stable(recorded.get(key)) != stable(fresh.get(key)):
                failures.append(f"{rel}: {key} differs")
    if failures:
        print("REPRODUCIBILITY FAILED")
        print("\n".join(failures))
        return 1
    print("REPRODUCIBILITY PASS: endpoints and probe classifications match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
