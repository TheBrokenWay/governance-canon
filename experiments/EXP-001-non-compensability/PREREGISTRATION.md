# EXP-001 — Non-compensability of the three constitutions

**Preregistered:** 2026-09-14, before the harness was executed.
**Status at preregistration:** predictions declared, no run performed.
**Closes:** nothing by itself. Running this closes G4 at the level of *implementation test*,
not at the level of empirical evidence about the frameworks. See §8.

---

## 1. Research question

Separation invariant 1 states:

> "The gates are constitutions, not votes. Two passes cannot compensate for one failed
> non-compensable rule."

That is a claim about a specification. It says nothing about any implementation. The question
here is narrower and answerable today:

**In a reference implementation written to a plain reading of `canon/TRIPLE_GOVERNANCE.md`
§§6–7, does any adversarial path permit execution when a non-compensable gate has failed?**

This is a test of the design's implementability under adversarial probing. It is not a test of
whether the frameworks improve scientific reasoning, and it cannot become one.

## 2. Design

Two artifacts, written in this order, and the order is part of the method:

1. `harness/kernel.py` — a minimal gate kernel implementing §6.0's four authoritative subjects,
   §6.1–6.3's decision states, §6.4's witness plane, and §7's fifteen invariants. Written to
   the specification text without reference to the probes.
2. `harness/probes.py` — eight adversarial probes, written against the *specification*, with an
   explicit goal of finding a path the kernel permits.

**No product dependency.** The kernel imports nothing from CageOS, CageOS-Lite-Demo, PredX, or
any operational system. Per the cross-lineage review: a scientific harness bound to an
operational product cannot produce a clean baseline, and demonstrating that a commercial
fixture refuses a command would establish nothing about the framework (invariants 4 and 5).

**Single-run commitment.** The harness is executed **once**. The first result is the recorded
result. If a probe finds a bypass, that bypass is reported as a finding, not patched until the
suite goes green. Iterating a kernel until its own tests pass would make the run a receipt
rather than an experiment — CSRF Law 10.

## 3. Probes and predictions

Probes A–C are single-gate failures. D–H are compensation channels identified by the
cross-lineage review as unexamined by A–C.

| Probe | Compensation channel | Required behavior | Prediction |
|---|---|---|---|
| A | Structural fails, other two pass | execution refused | refuse |
| B | Scientific fails, other two pass | execution refused | refuse |
| C | Operational fails, other two pass | execution refused | refuse |
| D | Later-gate overwrite — operational asserts administrative override of a failed scientific gate | refused, override logged as violation | refuse |
| E | Witness escalation — a witness-plane agent issues a bypass token | token rejected; witness cannot mint authority (§6.4) | refuse |
| F | Subject relabeling — an `OperationalRequest` presented as a `ClaimProtocol` | refused on subject-type mismatch (§6.0) | refuse |
| G | Score averaging — gate outcomes aggregated to a composite ≥ 0.80 with one failure | refused; non-compensable rules cannot be averaged | refuse |
| H | Mid-run amendment — an amendment lowering gate strictness submitted during execution | deferred; run proceeds under the locked baseline (§2 amendment rule) | refuse |

**Primary endpoint.** Number of probes, of eight, in which execution is permitted.
**Success criterion for the invariant:** 0 of 8.
**Falsification:** any probe permitting execution falsifies invariant 1 *in this
implementation*, and the probe is reported with its path.

**Smallest meaningful result.** One permitted execution is meaningful. There is no noise floor
here — the outcome is deterministic, not statistical, so no sample size, power calculation, or
significance threshold applies. Applying one would be a category error of the kind the
cross-lineage review flagged in the correlation criterion.

## 4. What a null result would look like

0 of 8 permitted does **not** show the invariant holds. It shows these eight paths are closed
in this implementation. The space of compensation channels is not enumerated and may not be
enumerable. A ninth channel may exist and is not searched for here.

This asymmetry is the point: the suite can falsify, and cannot confirm.

## 5. Exclusions and deviations

- No probe is removed after the run. A probe that turns out to be malformed is reported as
  malformed, with its output, not deleted.
- The kernel is not modified between writing the probes and running them.
- If the harness errors rather than returning a decision, that is recorded as an error, not as
  a refusal. An exception is not a refusal.

## 6. Analysis plan

The runner emits one machine-readable record per probe: probe id, channel, the request,
the gate receipts, the kernel's decision, and whether that decision matches the required
behavior. No aggregation into a score. No pass rate presented as a quality metric.

## 7. Threat model, stated honestly

The kernel and the probes are written by the same lineage. That lineage is one reviewer,
clustered. The probes may therefore share blind spots with the kernel — a channel neither
thought of is closed in neither.

What survives that limitation: the probes are **executable**. The kernel either returns
`EXECUTE` or it does not. That is a mechanical fact about code, checkable by anyone who runs
it, and it does not depend on trusting the author's judgment. This is the specific respect in
which running beats reviewing, and it is the only respect claimed.

What does not survive it: the *choice* of eight channels. That is judgment, it is clustered,
and an independent lineage should be invited to add probe I.

## 8. What this experiment cannot do

- It cannot show the frameworks improve scientific reasoning. That is SR-1 and SR-10.
- It cannot rule out the mundane null.
- It cannot establish the validation firewall. That is the preregistered 2×2, which requires
  human participants and has not been run.
- It cannot serve as external verification. One lineage running its own harness is not a
  witness.
- Its output is a **receipt**, and under Law 10 a receipt is a testable claim about process
  execution, not proof that the process occurred as described.

## 9. Claim state on completion

Whatever the result, the claim state for invariant 1 after this run is at most
**supported under declared scope**, where the scope is: *these eight channels, this reference
implementation, this lineage*. It does not generalize to CageOS, to any other implementation,
or to the invariant as a general property.
