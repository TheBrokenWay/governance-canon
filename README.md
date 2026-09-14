# Governance Canon

Three frameworks for building and evaluating governed intelligent systems, and the
firewall intended to keep them from validating each other.

Author: James Andrew Tillar · Tillar Technologies
Canon documents first drafted 2026-07-21. Published here with one declared redaction
(`canon/TRIPLE_GOVERNANCE.md` §8) — see `REDACTIONS.md`.

---

## The firewall comes first

These three documents began as one program. It was deliberately split.

```text
ConceptID:        CP-00081
Canonical name:   Unified intelligent-scientific reasoning program
Lifecycle status: Split
Split into:       CCTF — candidate intelligent-systems theory and architecture
                  CSRF — candidate scientific-reasoning framework
Reason:           Computational and methodological claims became independently testable
Revision:         R6
```

> "The split creates a validation firewall. CCTF performance cannot establish CSRF
> reliability, and CSRF process compliance cannot establish CCTF as a theory of intelligence."

The intent: a unified framework that explains everything can be graded only on elegance, while
two frameworks forbidden from vouching for each other can be graded on evidence. The split
renounces the ability to claim that success anywhere proves success everywhere.

**Whether the text actually prevents that borrowing is untested.** The firewall is a design
intent, not a demonstrated property. `CSRF-1`–`CSRF-6` and `CP-T1`–`CP-T14` specify how it
would be tested; none has been run. Reviewer question 2 below is the open form of this question.

The only sanctioned way the two may ever meet is a preregistered 2×2:

|  | Standard scientific workflow | CSRF workflow |
|---|---|---|
| Information-matched conventional architecture | Control | CSRF main effect |
| CCTF architecture | CCTF main effect | Combined |

> "This factorial firewall prevents either program from borrowing the other's success."

---

## What each document is

### CCTF — Contextual Compatibility and Transformation Framework
[`canon/CCTF.md`](canon/CCTF.md)

**Question it answers:** what representation, update process, and control architecture should
an intelligent system use when reality is only partially observed, context changes, actions
have consequences, and decisions must remain governable and auditable?

Ten hypotheses, `IS-H1`–`IS-H10`, each published alongside the condition that would falsify
it. Nine discriminating experiments, `IS-1`–`IS-9`, each with an explicit failure rule. A
three-level claim ladder — architecture, inductive bias, foundational intelligence — with
promotion between levels prohibited without new evidence of the appropriate kind.

Adjudications are `accept`, `reject`, `abstain`. Abstention is required when evidence is
insufficient, contradictory, outside the validated context, or not identifiable.

### CSRF — Constitutional Scientific Reasoning Framework
[`canon/CSRF.md`](canon/CSRF.md)

**Question it answers:** how should a human, AI, or hybrid research process acquire
observations, update models, compare explanations, govern decisions, and audit claims without
confusing names, coherence, confidence, or internal receipts with truth?

Sixteen non-compensable constitutional laws. Eleven hypotheses, `SR-H1`–`SR-H11`. Twelve
disconfirming experiments, `SR-1`–`SR-12`. A six-test vocabulary firewall suite, `CSRF-1`–`CSRF-6`.

The original design principle, in one line:

> "Labels may be emitted afterward, but labels must not control truth."

Claim states are `supported under declared scope`, `weakened`, `contradicted`, `unresolved`,
`superseded`. None is terminal. `knowledge` is not a state in this framework, because the word
implies a finality the framework will not represent.

### Triple Governance
[`canon/TRIPLE_GOVERNANCE.md`](canon/TRIPLE_GOVERNANCE.md)

**Question it answers:** what is an idea *permitted to do*, as distinct from where it came from?

> "The three provenance graphs describe lineage. The three governance layers control what an
> idea is permitted to do. Provenance and governance are orthogonal."

Three constitutions adjudicating four authoritative subjects:

| Constitution | Authoritative subject | Question |
|---|---|---|
| Structural | `ConceptFormulation@version` | Is this formulation well formed? |
| Scientific | `ClaimProtocol@version` | Admissible for confirmatory test? |
| Scientific | `ClaimStateRevision@version` | What does current evidence justify, under what scope? |
| Operational | `OperationalRequest@version` | May this privilege affect this target? |

The Scientific constitution issues two outputs that must never be merged: protocol
admissibility is not support, and support is not authorization. See the proposed amendment
[`amendments/2026-09-14-constitution-count.md`](amendments/2026-09-14-constitution-count.md),
which has not been accepted.

Fifteen separation invariants are specified; none has been tested against an implementation.
Four of them, quoted because the rest of this README depends on them:

> - **Invariant 1.** The gates are constitutions, not votes. Two passes cannot compensate for
>   one failed non-compensable rule.
> - **Invariant 3.** Structural approval cannot create evidential support.
> - **Invariant 4.** Scientific support cannot authorize deployment.
> - **Invariant 5.** Operational approval cannot make a scientific claim true.

And the rule governing what a failed gate does to an idea:

> "An idea does not need approval to exist in the archive. Archival existence is unconditional
> once proposed. Gates grant capabilities and state transitions; they do not erase ideas."

Independent observers and adversarial test agents form a **witness plane**, not a fourth
constitution. A witness may
disagree with the system it observes and may trigger review, quarantine, or revocation
processing — but it cannot mint authority.

---

## What is not claimed here

Status lines below are quoted from the canon files. Verify them there. This README is a lossy
projection and is not evidence about its own accuracy.

- **CCTF:** "Candidate architecture and falsifiable research program. No claim of necessity,
  sufficiency, general intelligence, consciousness, or empirical superiority has been
  established."
- **CSRF:** "It has not yet been shown to improve science, reproducibility, calibration, or
  error discovery over strong conventional practice."
- **Triple Governance:** "It is operationally useful as a traceability design, but it has not
  been shown to improve scientific reliability over simpler alternatives."

Each document also names the mundane null that would explain it away. CSRF names its own most
plainly:

> "The framework is ordinary good scientific practice expressed in new vocabulary... Any
> benefit comes from more attention and documentation, not a distinct epistemic framework."

That null has not been ruled out. No comparative experiment has been run.

---

## For reviewers

The useful adversarial questions, in order:

1. Does the mundane null explain the whole thing? Each document names its own; start there.
2. Is the firewall real, or does the text let one framework borrow the other's success anywhere?
3. Do the falsifiers actually falsify — could `IS-H1`–`IS-H10` and `SR-H1`–`SR-H11` fail as written?
4. Is any gate compensable in practice, whatever invariant 1 says?
5. Does any receipt, summary, or interface projection re-enter as independent evidence?

Three tests have been run. See below. The other twenty specified experiments have not, so every
remaining falsifier has the evidential weight of a sentence.

Issues and pull requests are welcome. Findings that survive review will be recorded as dated
amendments with claim states, including findings the author disagrees with.

---

## What has been tested

**EXP-001 — non-compensability of the three constitutions.** Preregistered 2026-09-14, run
once, not tuned. Eight adversarial probes and a positive control against a product-detached
reference kernel written from §§6–7.

**Result: 1 of 8 probes permitted execution.** The preregistered success criterion was 0 of 8
and was not met.

The open channel is **subject relabeling**. An operational deployment declared as a
`ClaimProtocol` — valid structural and scientific receipts, no operational receipt — executed
with zero violations recorded. Invariant 1 was not violated. §6.0 assigns authority by the
*declared* subject, the declaration decides which gates are required, and no rule in this canon
requires the declaration to match the effect. The operational gate was not bypassed; it was
never summoned.

The general form, which is not specific to this canon:

> Where authority is assigned by a declaration, the declaration is the attack surface. A
> non-compensability invariant constrains gates that are in scope and says nothing about what
> puts a gate in scope.

The kernel was **not patched** after the result. A proposed sixteenth invariant is recorded in
the amendment and is not implemented, because patching a reference implementation until its own
suite goes green turns an experiment into a receipt.

Run it yourself: `cd experiments/EXP-001-non-compensability/harness && python3 run.py`.
Standard library only, no dependencies, no product bindings.

**EXP-002 — remediation, and the limit of the remediation.** Kernel v2 derives the
authoritative subject from the request's effect footprint instead of its label. Preregistered
with a deliberately **unpredicted** probe, so the reading could not be steered.

- **Regression: 0 of 8.** F is closed — it now refuses as `SUBJECT_BINDING_VIOLATION`, and the
  mismatch is recorded against the requester rather than silently corrected. All seven
  previously-closed channels stay closed.
- **Remedy surface: 0 of 4.** An underivable footprint abstains rather than defaulting;
  an under-declared one is caught; a durable write outside the adjudicated scope is refused;
  legitimate work still executes, so the fix is not a denial of service.
- **Probe K executed.** The unpredicted one. It accepts that the subject is derived from the
  footprint and forges the footprint — declaring the durable release path as its own scratch
  prefix, so derivation returns a non-operational subject and the operational gate is never
  required.

The rule that follows supersedes the proposed invariant:

> A declaration-trust defect cannot be closed by deriving from another declaration. Trust must
> terminate at a value the caller does not control.

In kernel v2, `ADJUDICATED_SCOPE` is a kernel constant and probe M is refused because of it;
`scratch_prefixes` is caller-supplied and probe K executes because of it. Two fields in one
struct, one trusted and one not — that is the whole finding in miniature. Invariant 16 is
therefore **not promoted**, and was not patched inside the experiment that found its limit.

- Preregistration: [`experiments/EXP-002-subject-binding/PREREGISTRATION.md`](experiments/EXP-002-subject-binding/PREREGISTRATION.md)
- Result: [`experiments/EXP-002-subject-binding/RESULT.md`](experiments/EXP-002-subject-binding/RESULT.md) · [`RESULT.json`](experiments/EXP-002-subject-binding/RESULT.json)

**EXP-003 — fixing the class instead of the instance.** A mechanical audit of kernel v2's
derivation inputs ([`experiments/DERIVATION_INPUT_AUDIT.md`](experiments/DERIVATION_INPUT_AUDIT.md))
found that the classifying question is not whether an input comes from the caller but whether
**misdeclaring it is self-defeating** — and named two siblings of K before either was probed,
one of them stronger than K. Kernel v3 makes every derivation input kernel-controlled or
self-limiting.

- **Regression: 0 of 12.** K refuses, and so do both siblings.
- **Class: 0 of 4.** An undeclared footprint abstains; externality is derived, not declared; a
  forged grant is caught on provenance rather than shape; partial scratch does not launder a
  durable write.
- **Availability: 1 of 5 refused — L4.** A legitimate concept formulation that touches nothing
  is now indistinguishable from the empty-footprint attack, so it refuses. `ConceptFormulation`
  has no reachable path, which makes the structural constitution unreachable in this kernel.
  The preregistration named L4 in advance as the probe most likely to fail and as a failure of
  the remedy rather than the caller. It failed.
- Probe R refused **by branch ordering rather than by construction** — a latent defect recorded,
  not fixed.

| | EXP-001 | EXP-002 | EXP-003 |
|---|---|---|---|
| Defect | subject relabeling | footprint forgery | subject class unreachable |
| Introduced by | the specification | the EXP-001 remedy | the EXP-002 remedy |
| Fixed here? | no — reported | no — reported | no — reported |

- Preregistration: [`experiments/EXP-003-kernel-controlled-derivation/PREREGISTRATION.md`](experiments/EXP-003-kernel-controlled-derivation/PREREGISTRATION.md)
- Result: [`experiments/EXP-003-kernel-controlled-derivation/RESULT.md`](experiments/EXP-003-kernel-controlled-derivation/RESULT.md)

Three experiments, three defects, each introduced by the fix for the last. The loop closes each
time and has not terminated. That pattern is the finding — weight it above any single green
result inside it.

- Preregistration: [`experiments/EXP-001-non-compensability/PREREGISTRATION.md`](experiments/EXP-001-non-compensability/PREREGISTRATION.md)
- Result: [`experiments/EXP-001-non-compensability/RESULT.md`](experiments/EXP-001-non-compensability/RESULT.md) · [`RESULT.json`](experiments/EXP-001-non-compensability/RESULT.json)

What EXP-001 does **not** show: that invariant 1 holds — seven closed channels say nothing
about how many channels exist; that the frameworks improve scientific reasoning; that any
mundane null is ruled out. It is an implementation test by one lineage on its own harness, and
under Law 10 its output is a receipt, not proof.

Both experiments are bound to the canon's existing test catalogue rather than standing as a
parallel series — see [`experiments/TEST_BINDING.md`](experiments/TEST_BINDING.md). Probes F,
I, J and K are instances of **CP-T9, Authoritative-Subject Confusion**, which has now failed
twice against a reference kernel.

## Method

Every experiment above followed one procedure, and the procedure is published as instructions
rather than as a description: [`METHOD.md`](METHOD.md).

Its two load-bearing rules, because they are the ones that make the results above worth reading:

> **9. Do not patch the system to make the test pass.** If the test finds a failure, the failure
> stays in the record. Fixing and re-running converts the experiment into a receipt.
>
> **12. Retract your own overclaims in the record, not in private.** Name the direction of the
> error: "this was an overclaim in my own favor."

Rule 9 is why EXP-001's probe F, EXP-002's probe K and EXP-003's probe L4 are all still open in
the record rather than absent from it. Rule 12 is why this repository contains a dated
retraction of a claim its own author made in his own favour.

## Review history

Four independent model lineages reviewed this material before publication. Their sustained
findings — that correlation is not a valid firewall criterion, that hash chains establish
custody and not evidence, and that a scientific harness bound to an operational product cannot
produce a clean baseline — are consolidated in
[`amendments/2026-09-14-experiment-infrastructure.md`](amendments/2026-09-14-experiment-infrastructure.md).

Cross-lineage review is rival generation under SR-5. It is not replication: no reviewer held
root digests independently, re-ran anything under preregistration, or acquired its own
observations.

---

## Repository rules

Canon documents are sealed from the published commit forward: they are not edited, and
corrections are added under `amendments/` as dated notes that state their own scope. The §8
redaction and the cross-reference repairs predate publication and are declared in `REDACTIONS.md`.

`canon/SHA256SUMS` records the digests of the published bytes. Verify with
`cd canon && sha256sum -c SHA256SUMS`. The sums are self-issued and unsigned: they detect
accidental drift, not tampering by the author. A mismatch means the sealing claim has failed
and should be reported as a defect.

## License

Documents: CC BY 4.0. Attribution to James Andrew Tillar. Contributions are accepted under the
same terms.
