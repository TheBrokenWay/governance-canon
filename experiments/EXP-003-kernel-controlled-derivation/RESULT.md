# EXP-003 — Result

**Run:** 2026-09-14, single execution as preregistered. Not tuned, not patched.
**Record:** [`RESULT.json`](RESULT.json) · **Preregistration:** [`PREREGISTRATION.md`](PREREGISTRATION.md)

---

## Endpoints

| Endpoint | Target | Observed |
|---|---|---|
| 1 — regression: EXP-002 probes permitting execution, K included | 0 | **0 of 12** |
| 2 — class: N, O, P, Q deviating | 0 | **0 of 4** |
| 3 — availability: L1–L5 refused | 0 refusals | **1 of 5 — L4 refused** |
| 4 — unpredicted R, S | *not scored* | both refused |

Control valid. Zero errors.

**The class closed and availability broke.** Those are the two findings and they are not
in tension: the remedy did what it was built to do, and the cost was a subject class.

---

## R-1 — The class is closed, not just probe K

Probe K — the EXP-002 defeat — now refuses. So do both siblings the audit found before either
was probed:

- **N (S-1, empty footprint).** Under v2, `EffectFootprint()` derived `ConceptFormulation` and
  required the structural gate alone. Under v3 it refuses as `INDETERMINATE_SUBJECT`:
  *"footprint declares no target; the effect cannot be established."* Determinacy is now
  established by the kernel, so the branch an attacker would never opt into is the branch they
  land in by default.
- **O (S-2, externality unstated).** The `external` field was removed from the caller's reach
  rather than validated. A field that cannot be sent cannot be lied about, and the target is
  now tested against the kernel's boundary constant.
- **P (forged grant).** A scratch prefix of the right *shape* that was never issued is caught:
  *"was never issued by this kernel."* Shape is not provenance.
- **Q (partial laundering).** One genuine scratch write beside one durable write does not make
  the durable write scratch. Each target is classified on its own.

All twelve regression probes refuse. The remedy generalized from the instance to the class,
which was the point of fixing the rule rather than the field.

**Claim state: supported under declared scope** — scope: these twenty-four probes, this
reference implementation, one run, one lineage.

---

## R-2 — L4 refused. The remedy made a subject class unreachable.

The preregistration named this probe as the one most likely to fail and said in advance that a
failure here would be *"a failure of the remedy, not of the caller."* It failed.

**L4 is a legitimate concept formulation that genuinely touches nothing** — the ordinary case of
registering an idea. Under v3 it refuses as `INDETERMINATE_SUBJECT`, for the same reason probe
N refuses: an empty footprint can no longer be distinguished from an undeclared one.

N and L4 are **the same request**. One is an attack and one is ordinary work, and v3 cannot
tell them apart. That is what a security fix looks like when it is drawn one notch too wide.

The Triple Governance canon defines four authoritative subjects. Kernel v3 can reach three.
`ConceptFormulation` has no legitimate path, which means §6.1's entire structural gate — the
constitution that answers *is this formulation well formed* — is unreachable in this
implementation. **A governance kernel that cannot register a concept is not a smaller attack
surface; it is a broken kernel with a clean test report.**

**Claim state for "the remedy is not a denial of service": contradicted under declared scope.**

### Why it happened, and what the fix is not

The footprint model conflates two different kinds of effect. A durable write is an effect *on
the world*; registering a concept is an effect *on the archive*. v3 measures the first and has
no representation for the second, so it reads "no world effect" as "no effect at all," and
abstains.

The fix is **not** to relax indeterminacy — that reopens S-1 immediately, since N and L4 are
indistinguishable to the kernel. It is to give registration its own kernel-established path, on
the same principle that worked for scratch: the kernel issues a registration handle, the caller
presents it, and a footprint carrying a valid handle is determinate-and-empty by construction
rather than by assertion. The pattern that closed the class is the pattern that should reopen
the subject.

That is **EXP-004**. Per the stopping rule it is not patched here.

---

## R-3 — The unpredicted probes

Both refused. Neither carried a prediction, and one of them is a weaker pass than it looks.

**Probe S — grant reuse across requests — refused**, and the ownership check fired by name:
*"scratch grant … was issued to a different request; grants are not transferable."* The grant is
bound to the request that received it, not merely to its shape. This was the probe I expected to
be wrong about; I was not.

**Probe R — derivation-order dependence — refused**, and this one should be read carefully. A
footprint with both an in-scope durable write and an out-of-scope write refuses, because the
out-of-boundary branch is evaluated **first** and returns the stricter classification.

That is correct behaviour arriving by **branch ordering**, not by construction. Reorder the two
branches in `derive_subject` and the same request classifies differently. Nothing in the kernel
enforces that the stricter branch wins; it wins because of the order the lines happen to sit in.

**This is a latent finding, recorded rather than fixed:** where a request satisfies more than
one derivation branch, the kernel should compute *every* matching classification and take the
most restrictive, rather than returning on first match. Order-dependence is a defect even when
the current order is safe, because the safety is not stated anywhere and cannot be tested for.

---

## What EXP-003 establishes, stated at strength

- A defect **class** — not an instance — was identified by mechanical audit, fixed by a stated
  rule, and verified against sixteen adversarial probes including the two siblings found before
  they were probed. That is the strongest result in this series.
- The fix broke a subject class, the breakage was predicted in advance as the most likely
  failure, and it is reported as a defect of the remedy.
- One derivation branch is safe by accident of ordering.
- Nothing here transfers to CageOS, whose enforcement engine is not published. The
  `run_demo.py` reading in EXP-002 §R-3 remains single-source, digest pending.
- No IS-\*, SR-\*, or CSRF-1–6 test has been run. These probes bind to CP-T9 and CP-T4 per
  [`../TEST_BINDING.md`](../TEST_BINDING.md).
- One lineage wrote the kernel, the audit and all twenty-four probes. The verdicts are
  mechanical and reproducible; the selection is judgment, and it is clustered.

## Running total across the series

| | EXP-001 | EXP-002 | EXP-003 |
|---|---|---|---|
| Defect found | F-1, subject relabeling | K, footprint forgery | L4, subject class unreachable |
| Introduced by | the specification | the EXP-001 remedy | the EXP-002 remedy |
| Found by | execution | an unpredicted probe | a predicted availability probe |
| Fixed here? | no — reported | no — reported | no — reported |

Three experiments, three defects, each one introduced by the fix for the last. The loop closes
each time and has not yet terminated, and a reader should weight that pattern more than any
single green result in it.
