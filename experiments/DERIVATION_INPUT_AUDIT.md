# Derivation input audit — kernel v2

**Date:** 2026-09-14. **Scope:** `experiments/EXP-002-subject-binding/harness/kernel.py`.
**Status:** audit, not an experiment. No run. Claim state: unresolved.

Written to answer a review finding: probe K is one probe against one caller-supplied field.
The class is closed only when every input to derivation is enumerated and each is classified.
This is that enumeration.

## Method

Inputs were extracted mechanically from the AST of `derive_subject`, `_survives` and
`scope_violations` rather than by reading, so an input consumed but not discussed cannot be
missed by inattention. Each was then exercised directly against `derive_subject` to record the
subject and gate set it produces.

## The five inputs

| # | Input | Source | Misdeclaration self-defeating? | Class |
|---|---|---|---|---|
| 1 | `fp.write_targets` | caller | **Yes** | untrusted, self-limiting |
| 2 | `fp.scratch_prefixes` | caller | No | **untrusted — probe K** |
| 3 | `fp.external` | caller | No | **untrusted — unnamed sibling** |
| 4 | `fp.determinate` | caller | No | **untrusted — unnamed sibling** |
| 5 | `ADJUDICATED_SCOPE` | kernel constant | n/a | trusted |

**"Self-defeating" is the distinction that matters.** `write_targets` is the value the executor
acts on. A caller who understates it does not sneak a write past the gate — the write lands
somewhere else, and the attack fails by succeeding at the wrong thing. The other three
caller-supplied fields describe *what the targets mean*, and lying about meaning costs the
attacker nothing.

That yields the rule the audit exists to state:

> A derivation input is safe only if it is kernel-controlled, or if misdeclaring it defeats the
> attacker's own purpose. Every other input is a K.

Input 5 is why probe M refuses. Inputs 2–4 are why K executes and why two more probes are owed.

## Observed behaviour, measured

| Footprint | Derived subject | Gates required |
|---|---|---|
| `EffectFootprint()` — empty | `ConceptFormulation` | **structural only** |
| durable write + self-declared scratch (probe K) | `ClaimProtocol` | structural, scientific |
| `external=False` with an out-of-band effect | `ClaimProtocol` | structural, scientific |
| reads only | `ClaimProtocol` | structural, scientific |
| `determinate=False` | none — abstains | — |

## Two siblings, one worse than K

**S-1 — the empty footprint.** `EffectFootprint()` derives `ConceptFormulation`, which requires
**only the structural gate**. A caller who declares no effect at all reaches execution with a
single structural receipt — no scientific gate, no operational gate. This is strictly stronger
than K, which still had to clear two gates, and it requires no forged prefix. It is reachable
by omission rather than by construction, which is worse: omission is the default of a
malformed or lazy caller, not only of an adversarial one.

The kernel treats "no declared effect" as "no effect." It should treat it as
**indeterminate** — the distinction the abstention branch exists to draw, and the branch is
reached only when the caller explicitly sets `determinate=False`, which no attacker would.

**S-2 — the externality lie.** `fp.external` participates in the durable-or-external test and is
caller-supplied. An effect that reaches outside the adjudicated boundary through a channel not
represented in `write_targets` is invisible to derivation when `external` is left at its
default `False`. This is the same shape as K and was not probed.

Neither sibling is probed. Both are predicted refusals under a v3 that fixes the class rather
than the instance, which is the point of fixing classes.

## Consequence for EXP-003

The remedy cannot be "make `scratch_prefixes` kernel-assigned." That closes K and leaves S-1
and S-2 standing. The remedy has to be the rule above: **every derivation input is
kernel-controlled or self-defeating, and anything else refuses.** Concretely —

1. Scratch regions are kernel-allocated. The caller receives a prefix; writes outside it are
   durable by construction.
2. Externality is derived from the targets against the kernel's own boundary, not declared.
3. An absent or empty footprint is **indeterminate**, not "no effect." Determinacy is a
   property the kernel establishes, not a flag the caller sets.

## What this audit does not do

It does not show the enumeration is complete. It shows the five inputs *this* derivation
consumes, in *this* kernel version. A v3 that adds an input adds a row, and the audit has to be
re-run against it — which is the argument for keeping the extraction mechanical rather than
narrative.

It is also one lineage auditing its own code. The extraction is reproducible; the
classification in column 4 is judgment.
