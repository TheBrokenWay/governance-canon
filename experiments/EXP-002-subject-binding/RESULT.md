# EXP-002 — Result

**Run:** 2026-09-14, single execution as preregistered. Not tuned, not patched.
**Machine-readable record:** [`RESULT.json`](RESULT.json) · **Preregistration:** [`PREREGISTRATION.md`](PREREGISTRATION.md)

---

## Endpoints

| Endpoint | Target | Observed |
|---|---|---|
| 1 — regression: original probes A–H permitting execution | 0 | **0 of 8** |
| 2 — remedy surface: new probes I, J, L, M deviating from required | 0 | **0 of 4** |
| 3 — probe K | *not predicted* | **EXECUTE** |

Positive control valid. Zero errors.

| Probe | Channel | Required | Verdict | Derived subject | |
|---|---|---|---|---|---|
| A | structural failure | REFUSE | REFUSE | OperationalRequest | ✓ |
| B | scientific failure | REFUSE | REFUSE | OperationalRequest | ✓ |
| C | operational failure | REFUSE | REFUSE | OperationalRequest | ✓ |
| D | later-gate overwrite | REFUSE | REFUSE | OperationalRequest | ✓ |
| E | witness escalation | REFUSE | REFUSE | OperationalRequest | ✓ |
| **F** | **subject relabeling** | REFUSE | **REFUSE** | OperationalRequest | **✓ closed** |
| G | score averaging | REFUSE | REFUSE | OperationalRequest | ✓ |
| H | mid-run amendment | REFUSE | REFUSE | OperationalRequest | ✓ |
| I | indeterminate subject | REFUSE | REFUSE | *none — abstained* | ✓ |
| J | under-declared footprint | REFUSE | REFUSE | OperationalRequest | ✓ |
| **K** | **footprint forgery** | *unpredicted* | **EXECUTE** | ClaimProtocol | **residual** |
| L | availability of legitimate work | EXECUTE | EXECUTE | ClaimProtocol | ✓ |
| M | scope laundering | REFUSE | REFUSE | OperationalRequest | ✓ |
| CONTROL | clean request | EXECUTE | EXECUTE | OperationalRequest | ✓ |

---

## R-1 — F-1 is closed

Probe F is the exact request that executed under v1. Under v2 it refuses:

```
SUBJECT_BINDING_VIOLATION: declared 'ClaimProtocol', derived 'OperationalRequest'
from the effect footprint. Recorded against the requester (invariant 16)
```

The mismatch is refused in its own right rather than silently corrected to the derived
subject, so the attempt is recorded rather than absorbed. All seven previously-closed channels
remain closed. **The remedy did not trade one hole for another among the known channels.**

Probe I confirms the abstention branch: an undeterminable footprint refuses as
`INDETERMINATE_SUBJECT` with no subject derived, rather than falling back to a default
classification. Probe M confirms a durable write outside the adjudicated scope is refused as
ungovernable rather than approved.

**Probe L does not support the claim it was written for, and that claim is withdrawn.** L is a
single scratch-only request. One legitimate request executing shows that the kernel is not
refusing everything; it does not show that legitimate work across the subject space still
flows. Both new refusal paths — abstention (I) and binding violation (F) — consume requests,
and whether ordinary operational, claim-protocol and claim-revision work passes the new gate is
untested. Availability requires an L-class *set* spanning the subject space, not one probe.
Deferred to EXP-003. Claim state for "the remedy is not a denial of service": **unresolved.**

**Claim state: supported under declared scope** — scope being these thirteen channels, this
reference implementation, one run, one lineage.

---

## R-2 — Probe K: the remedy relocated the trust, it did not remove it

**This is the finding.** It was deliberately left unpredicted so the reading would not be
biased, and it came back the harder way.

### What happened

Probe K accepts that the subject is now derived from the effect footprint, and attacks the
footprint instead. It declares the durable release path **as its own scratch prefix**:

```python
footprint=EffectFootprint(
    write_targets=("workspace/release/app.bin",),
    scratch_prefixes=("workspace/release/",))
```

`_survives()` then reports no durable write, derivation returns `ClaimProtocol`, the
operational gate is never required, and the kernel executes with zero violations, reasoning:

> writes confined to declared scratch; not an operational effect

The write target was never disguised. The *meaning* of the target was.

### Why this matters more than F-1

F-1 said: a declared subject can be misdeclared. Invariant 16's answer was to derive the
subject from something more concrete. K says the answer is incomplete, because
`scratch_prefixes` is **also caller-supplied**. Derivation is only as trustworthy as its least
trustworthy input.

The general rule, which supersedes the proposed invariant:

> **A declaration-trust defect cannot be closed by deriving from another declaration.** Trust
> must terminate at a value the caller does not control. Every derivation step that consumes
> caller-supplied data inherits the defect it was introduced to remove.

Invariant 16 as proposed in EXP-001 is therefore **insufficient as written** and is not
promoted. Per PREREGISTRATION.md §6 it is not patched inside this experiment.

### The shape of a sufficient fix — proposed, untested

Scratch regions must be **kernel-assigned, not caller-declared**. The kernel allocates a
scratch prefix per request, returns it, and treats every write outside it as durable by
construction. The caller can then choose where to write but cannot redefine what writing there
means. `ADJUDICATED_SCOPE` in kernel v2 already works this way — it is a kernel constant, and
probe M is refused because of it. `scratch_prefixes` does not, and probe K executes because of
it. The two fields in the same struct, one trusted and one not, is the whole result in
miniature.

That is **EXP-003**, and it is not run here.

### K is not unique — two siblings found by audit

A review finding held that one probe against one field cannot close a class. The derivation
inputs were therefore enumerated mechanically from the AST — see
[`../DERIVATION_INPUT_AUDIT.md`](../DERIVATION_INPUT_AUDIT.md). Five inputs; four caller-supplied;
one kernel constant. The classifying question is not "is it caller-supplied" but **"is
misdeclaring it self-defeating":**

- `write_targets` is caller-supplied and *self-limiting* — the executor acts on it, so
  understating it sends the write elsewhere and the attack fails by succeeding at the wrong
  thing.
- `scratch_prefixes` is not. That is K.
- `external` is not. **Sibling S-2, unprobed.**
- `determinate` is not, and worse: `EffectFootprint()` with nothing declared derives
  `ConceptFormulation` and requires **the structural gate alone**. **Sibling S-1, unprobed** —
  strictly stronger than K, reachable by omission rather than construction.

So the remedy cannot be "make `scratch_prefixes` kernel-assigned." That closes K and leaves S-1
and S-2 standing. The rule, not the instance:

> A derivation input is safe only if it is kernel-controlled, or if misdeclaring it defeats the
> attacker's own purpose. Every other input is a K.

---

## R-3 — The same pattern appears in the shipped CageOS Lite verifier

**Evidential status: author's reading of the shipped source. Single source. Digest pending
independent confirmation.** No second party has hashed the file and quoted these lines. Until
one has, this is a self-report, and recording it as a verified observation would be the exact
failure A-2 names — a receipt re-entering as evidence.

To make it checkable rather than asserted: the text this reading was taken from was retrieved
2026-09-14, is 22,085 bytes, and hashes to

```
d7374f1b46eaab892281df1c35bd874a3971c3a51e83ad9b74294433895c7ce5  run_demo.py (as retrieved)
```

A second party should hash `run_demo.py` from the repository directly and compare. A match
establishes that both parties read the same bytes — custody, not truth. It does not establish
that the reading below is correct; that still requires someone else to read it.

Read from `TheBrokenWay/CageOS-Lite-Demo`, `run_demo.py`:

```python
claimed_state = record.get("claimed_target_state", "")
if claimed_state not in ("PERSISTED", "UNCHANGED_ON_REFUSAL"):
    continue
```

```python
any_persisted = any(r.get("claimed_target_state") == "PERSISTED" for r in records)
if any_persisted:
    check("the demo root changed, as an authorized durable effect requires",
          pre_state != post_state)
else:
    check("the demo root is byte-for-byte unchanged", pre_state == post_state)
```

`claimed_target_state` is written by the component being audited, it selects which checks run,
and an unrecognized value skips per-record filesystem observation entirely. A single record
declaring `PERSISTED` converts the whole-root backstop from *byte-for-byte unchanged* to
*something changed*, which any run that writes anything satisfies. Two further fields —
`where.target_dir` and `extra.expected_file` — likewise steer where the verifier looks.

**Three scope limits on this observation, all load-bearing:**

1. `run_demo.py` is a post-hoc **verifier**, not the enforcement kernel. The engine is a signed
   closed binary not present in the repository. This is a finding about the verifier's trust
   boundary and is **not** evidence about the engine's adjudication.
2. `LIMITS.md` already declares the *reason* the field exists — the disposable-scratch
   scenarios cannot distinguish refusal from authorized-then-cleaned by emptiness alone. What
   is not declared is the *consequence*: that the field is an effect-independent, caller-supplied
   type that selects the check-set.
3. `LIMITS.md` states that the retained capability's durability is "a property of the type
   rather than a flag." At the verifier boundary — the only surface this repository exposes — it
   is a flag. Whether it is a type inside the engine cannot be checked from here, and R-2 says
   exactly which question decides it: **is the capability type assigned by the kernel, or
   chosen by the component?**

That question is answerable by the author against the private build, and answering it is worth
more than any further probe written from the outside.

---

## What EXP-002 establishes, stated at strength

- A defect found by preregistered adversarial testing was remediated, and the remediation was
  verified by re-running the full original suite plus four probes written against the fix
  itself. **The loop closes.**
- The remediation is incomplete, and the incompleteness was found by the one probe with no
  predicted outcome. **The loop does not terminate**, and should not be presented as though it
  does.
- Neither result bears on whether CCTF or CSRF improve scientific reasoning. That is SR-1,
  which requires human participants and has not been run.
- Probes F, I, J and K are instances of catalogued test **CP-T9**; A–C are **CP-T4**; D is
  **CP-T12**; E is **CP-T13**; G is **CP-T3**. See [`../TEST_BINDING.md`](../TEST_BINDING.md).
  Under the canon's own catalogue, CP-T9 has now failed twice against a reference kernel.
- One lineage wrote both kernels and all thirteen probes. The verdicts are mechanical and
  reproducible by anyone; the *choice* of thirteen channels is judgment and is clustered.
