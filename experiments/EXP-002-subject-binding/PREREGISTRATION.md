# EXP-002 — Remediation of F-1 by subject binding

**Preregistered:** 2026-09-14, before kernel v2 was executed.
**Follows:** EXP-001, which found one open compensation channel (F-1, subject relabeling).
**Design rule carried forward:** single run, first result recorded, no tuning to green.

---

## 1. What is being tested

EXP-001 found that authority assigned by a *declared* subject can be steered by misdeclaring
it. Proposed invariant 16 (subject binding) was recorded but not implemented, because patching
a kernel inside the experiment that found the defect would convert the experiment into a
receipt.

This experiment implements it and then attacks it.

Two questions, in order:

1. **Does the remedy close F-1?** Re-run all eight original probes against kernel v2.
2. **What does the remedy open?** A fix is a change to the attack surface, not a reduction of
   it. Five new probes are written specifically against the remedy.

Question 2 is the one that matters. A remediation tested only by the probe it was built to
stop is a tautology.

## 2. The remedy as implemented

Kernel v2 derives the authoritative subject from the request's **effect footprint** — the
concrete parameters describing what the request would touch and whether the touch is durable —
rather than from a `subject` label the caller supplies.

Three rules:

- **Derivation.** If the footprint shows a durable external write, the subject is
  `OperationalRequest`, whatever the caller declared.
- **Mismatch is a refusal in its own right.** A declared subject that disagrees with the
  derived subject refuses as `SUBJECT_BINDING_VIOLATION` and is recorded against the requester.
  It does not silently fall through to the derived subject: silent correction would hide the
  attempt.
- **Indeterminacy refuses.** A footprint from which no subject can be derived refuses as
  `INDETERMINATE_SUBJECT`. Abstention is required; there is no default classification.

The declared subject is retained in the record but carries no authority. Labels may be emitted;
labels must not control truth.

## 3. Probes and predictions

**Regression set:** the eight probes of EXP-001, unmodified, plus the positive control.

| Probe | Prediction under v2 |
|---|---|
| A–E, G, H | refuse, as under v1 |
| **F** | refuse — this is the remedy's target |
| CONTROL | execute — the remedy must not break legitimate traffic |

**New probes against the remedy:**

| Probe | Attack on the fix | Required behavior | Prediction |
|---|---|---|---|
| I | **Indeterminate footprint** — a request whose effect cannot be derived | refuse as `INDETERMINATE_SUBJECT`, not default-classified | refuse |
| J | **Under-declared footprint** — declare a narrow effect while the parameters show a durable write | refuse; derivation must read the parameters, not the effect *claim* | refuse |
| K | **Second-order relabeling** — forge the footprint itself so derivation returns the attacker's preferred subject | **unknown** — see §4 | **not predicted** |
| L | **Availability** — a legitimate request with an unusual but determinate footprint | execute; the fix must not refuse valid work | execute |
| M | **Scope laundering** — a durable write aimed outside the declared target scope | refuse | refuse |

## 4. Probe K is the real experiment, and its outcome is not predicted

Probe K asks whether the remedy actually removes the trust in declaration or merely relocates
it one level down. If the footprint is itself caller-supplied data, then "derive the subject
from the footprint" may be the same defect wearing a different field name.

**No prediction is recorded for K.** Predicting it would bias the reading. The honest
possibilities:

- **K refuses** — the footprint is constrained by something the caller does not control, and
  the remedy is real within that constraint.
- **K executes** — the remedy is a relocation, not a fix, and invariant 16 as proposed is
  insufficient. That is a finding about the proposed invariant, and it supersedes the proposal.

Either result is reportable. The second is more valuable.

## 5. Primary endpoints

1. **Regression:** number of the eight original probes permitting execution. Target 0.
2. **Remedy surface:** number of new probes (I, J, L, M) whose behavior differs from required.
   Target 0.
3. **K:** reported as observed, with the mechanism, and not scored against a target.

## 6. Exclusions and stopping rules

- Kernel v2 is written before the new probes and is not modified after they are written.
- Single run. If a probe fails, it is reported, not patched.
- If probe K executes, invariant 16 is **not** promoted to accepted, and the residual is stated
  in the result rather than resolved by a further patch inside this experiment.
- An exception is an error, not a refusal.

## 7. What this cannot establish

It cannot show kernel v2 is secure — five new probes are five channels out of an unenumerated
space, and EXP-001 already demonstrated that the channel that matters is the one nobody wrote.

It cannot transfer to CageOS. The finding that motivated this experiment was confirmed by
reading the public `run_demo.py`, but that file is a post-hoc **verifier**; the enforcement
engine is a closed binary not present in the repository. Nothing here is evidence about the
engine.

It cannot rule out the mundane null, validate either framework, or serve as external
verification.

## 8. Claim state on completion

At most **supported under declared scope**, scope being: these thirteen channels, this
reference implementation, this lineage, one run. A remedy that survives thirteen probes is a
remedy that survives thirteen probes.
