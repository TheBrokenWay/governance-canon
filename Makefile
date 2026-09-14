PYTHON ?= python3

.PHONY: test verify compile

test:
	$(PYTHON) -c 'import tempfile, pathlib, subprocess, sys; runs=["experiments/EXP-001-non-compensability", "experiments/EXP-002-subject-binding", "experiments/EXP-003-kernel-controlled-derivation"]; td=tempfile.TemporaryDirectory(prefix="governance-canon-"); [subprocess.run([sys.executable, str(pathlib.Path(d)/"harness/run.py"), str(pathlib.Path(td.name)/(pathlib.Path(d).name+".json"))], check=True, stdout=subprocess.DEVNULL) for d in runs]; td.cleanup()'

verify: compile
	$(PYTHON) verify_reproducibility.py
	cd canon && sha256sum -c SHA256SUMS

compile:
	$(PYTHON) -m compileall -q experiments verify_reproducibility.py
