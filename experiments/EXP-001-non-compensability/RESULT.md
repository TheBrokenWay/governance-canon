# EXP-001 — Result

**Run:** 2026-09-14, single execution as preregistered. Not re-run, not tuned.
**Machine-readable record:** [`RESULT.json`](RESULT.json)
**Preregistration:** [`PREREGISTRATION.md`](PREREGISTRATION.md)

---

## Primary endpoint

**1 of 8 adversarial probes permitted execution.** Probe F.

The preregistered success criterion for invariant 1 was 0 of 8. That criterion was not met.

Positive control valid: the clean request executed, so the kernel is not refusing
indiscriminately and the seven refusals are informative. Zero errors.

| Probe | Channel | Required | Verdict | |
|---|---|---|---|---|
| A | structural failure | REFUSE | REFUSE | ✓ |
| B | scientific failure | REFUSE | REFUSE | ✓ |
| C | operational failure | REFUSE | REFUSE | ✓ |
| D | later-gate overwrite / retroactive pardon | REFUSE | REFUSE | ✓ |
| E | witness escalation | REFUSE | REFUSE | ✓ |
| **F** | **subject relabeling** | **REFUSE** | **EXECUTE** | **✗** |
| G | score averaging | REFUSE | REFUSE | ✓ |
| H | mid-run amendment weakening | REFUSE | REFUSE | ✓ |
| CONTROL | all gates pass | EXECUTE | EXECUTE | ✓ |

---

## F-1 — Subject relabeling defeats non-compensability without ever violating it

**Claim state: contradicted under declared scope.** Scope: invariant 1 as a guarantee that a
failed or absent non-compensable gate blocks execution, in this reference implementation.

### What happened

Probe F submitted an operational deployment with its `subject` declared as `ClaimProtocol`
rather than `OperationalRequest`. It carried a valid structural receipt and a valid scientific
receipt. It carried **no operational receipt at all**.

The kernel returned `EXECUTE` with the reason *"all required gates passed independently"* and
recorded **zero violations**.

### Why this is not a coding error

Invariant 1 was never violated. Neither was 3, 4, 5, or 14. Every gate that was required
passed, honestly, on its own.

The mechanism is upstream of the invariants. §6.0 assigns adjudicative authority *by declared
subject type*. `required_constitutions()` derives which gates must be consulted from that same
declared type. So the declaration determines the obligation — and nothing in
`canon/TRIPLE_GOVERNANCE.md` requires the declared subject to correspond to what the action
actually does.

The operational gate was not bypassed. **It was never summoned.** An invariant about
compensation between gates cannot fire when the gate in question was never in scope.

### Why this is a finding about the specification, not the harness

A reader might object that a correct implementation would validate the subject against the
action. Three reasons that objection does not dispose of it:

1. **The specification does not say so.** §6.0 gives four subjects and their authorities.
   §§6.1–6.3 give the gate outputs. §7 gives fifteen invariants, none of which constrains
   subject declaration. §2's nine identity rules govern concept identity under renaming and
   splitting — not the binding of a request to its authoritative subject. There is no rule to
   implement.

2. **§2 rule 1 arguably licenses it.** *"A rename or improved wording retains the same
   `concept_id` and creates a new formulation."* Relabeling is framed in the canon as
   identity-preserving and benign. In the provenance graph it is. In the governance graph it
   changes which constitution has authority. Two graphs the canon insists are orthogonal meet
   at this point, and the canon does not say what happens when they do.

3. **It is the canon's own attack pattern.** CP-T9 is *Authoritative-Subject Confusion* and
   CP-T6 is *Concept-Artifact Independence*. The canon anticipated this class. What it did not
   do is state the rule that closes it. The tests name the threat; no invariant answers it.

This is the difference between a specification gap and a bug. A bug is a failure to implement
a stated rule. Here there is no stated rule to fail.

### The general form

> Where authority is assigned by a declaration, the declaration is the attack surface. A
> non-compensability invariant constrains gates that are in scope; it says nothing about what
> puts a gate in scope. Any system that derives its obligations from a self-reported type can
> be steered by misreporting that type, without ever violating a rule about what happens
> afterward.

This generalizes past this canon. It applies to any policy architecture whose enforcement
points are selected by a caller-supplied classification — which, on its own published account,
includes the enforcement-point model described in the September UPA paper, whose stated
limitation is that *"the architecture only governs operations that pass through a recognized
enforcement point."* F-1 is the constructive version of that sentence: recognition is itself a
governed act, and no examined specification governs it.

### Not patched

Per PREREGISTRATION.md §2, the kernel was not modified after the run. Patching a reference
implementation until its own suite goes green converts the experiment into a receipt — Law 10.
The proposed remedy below is recorded as a **proposed amendment, unaccepted**, and is not
implemented in the harness.

### Proposed remedy — proposed, not accepted, not tested

A sixteenth separation invariant:

> **16. Subject binding.** The authoritative subject of a request is determined by the effect
> the request would have if executed, not by the label the requester supplies. A request whose
> declared subject admits an effect outside that subject's authority is refused as a
> subject-binding violation, and the refusal is recorded against the requester. Where the
> effect cannot be determined in advance, the request is refused for indeterminate subject;
> abstention is required, not a default classification.

Consequences that would need their own testing: the clause introduces an effect-determination
step that may be undecidable in the general case, and "refused for indeterminate subject" is a
denial-of-service surface. Neither has been analyzed. Proposing an invariant is not closing a
gap.

---

## What the seven refusals do and do not show

Probes A–E, G and H were refused with the invariant cited by name in each case. Under the
preregistered analysis that supports one narrow statement:

**Claim state: supported under declared scope.** Scope: these seven channels, this reference
implementation, this lineage, this single run.

It does not show invariant 1 holds. The space of compensation channels is not enumerated and
may not be enumerable — F-1 is the direct demonstration, since F was only added because a
review lineage thought of it, and probe I is presumably also unthought-of by everyone so far.
Seven closed doors say nothing about the number of doors.

---

## Limitations

- **One lineage wrote both the kernel and the probes.** They may share blind spots. What
  survives this: the kernel returns `EXECUTE` or it does not, and anyone can run
  `python3 harness/run.py` and get the same bytes. The *selection* of eight channels is
  judgment and is clustered.
- **A reference implementation is not the specification.** F-1 is argued above to be a
  specification gap rather than an implementation defect, but that argument is reasoning, not
  measurement. An independent implementer who reads §6.0 differently would settle it.
- **This says nothing about CageOS or any other system.** Invariants 4 and 5 both forbid the
  inference. The harness is deliberately product-detached for exactly this reason.
- **This is not external verification.** One lineage running its own harness is not a witness.
- **The output is a receipt.** Law 10: a testable claim about process execution, not proof that
  the process occurred as described.

## Correction — this channel was named in review before it was probed

Part VIII.4 of the 2026-09-14 handoff packet lists, among compensation channels still needing
probes, "subject relabeling across ClaimProtocol / ClaimStateRevision / OperationalRequest."
The reviewing lineage identified this channel. The run demonstrated that it executes, and why.
Those are different contributions and the first belongs to the review.

This probe is an instance of catalogued test **CP-T9, Authoritative-Subject Confusion** — see
[`../TEST_BINDING.md`](../TEST_BINDING.md). It is not a new test.

## What would close what this leaves open

1. An independent implementer writes a second kernel from §§6–7 without seeing this one, and
   probe F is run against it. If it also executes, the gap is in the specification. If it
   refuses, the gap is in this reading, and that is worth knowing too.
2. Probe I onward, contributed by lineages that did not write this suite.
3. SR-1 — the experiment that would actually bear on whether the frameworks help. It requires
   human reviewers, seeded defect dossiers, and effort-matched arms. It has not been run and is
   not runnable here.
