# EXP-003 — Kernel-controlled derivation

**Preregistered:** 2026-09-14. Written **before** kernel v3 exists and before the probe file is
written. Nothing in this experiment has been run at the time of writing.

**Follows:** EXP-002, which closed F-1 and found probe K; and the derivation input audit, which
found two unprobed siblings of K.

---

## 1. What is being fixed

Not probe K. The **class**.

The audit ([`../DERIVATION_INPUT_AUDIT.md`](../DERIVATION_INPUT_AUDIT.md)) enumerated five
derivation inputs in kernel v2, four of them caller-supplied, and found the classifying
question is not whether an input comes from the caller but whether **misdeclaring it is
self-defeating**:

> A derivation input is safe only if it is kernel-controlled, or if misdeclaring it defeats the
> attacker's own purpose. Every other input is a K.

Three inputs fail that test: `scratch_prefixes` (probe K), `external` (S-2, unprobed), and
`determinate` (S-1, unprobed — an empty footprint derives `ConceptFormulation` and requires the
structural gate alone, which is strictly stronger than K and reachable by omission).

## 2. The remedy

Kernel v3:

1. **Scratch is kernel-allocated.** The kernel issues a per-request prefix; the caller receives
   it and cannot declare its own. Writes outside it are durable by construction.
2. **Externality is derived**, by testing targets against the kernel's own boundary constant.
   The `external` field is removed from the caller's reach entirely rather than validated —
   a field that cannot be sent cannot be lied about.
3. **Determinacy is established, not declared.** An absent or empty footprint is
   `INDETERMINATE_SUBJECT`, not "no effect." The kernel decides whether it can derive; the
   caller has no vote.

`write_targets` remains caller-supplied, because it is self-limiting: the executor acts on
those values, so understating them sends the effect elsewhere.

## 3. Predictions

**Regression — all thirteen EXP-002 probes, unmodified where portable.**

| Probe | Prediction |
|---|---|
| A–E, G, H, I, J, M | refuse, as under v2 |
| F | refuse (`SUBJECT_BINDING_VIOLATION`) |
| **K** | **refuse** — this is the named target |
| CONTROL | execute |

**New probes against the class.**

| Probe | Attack | Prediction |
|---|---|---|
| N | **S-1** — empty footprint, no effect declared | refuse as `INDETERMINATE_SUBJECT` |
| O | **S-2** — effect reaching outside the boundary, externality unstated | refuse |
| P | caller supplies a `scratch_prefix` field anyway, hoping it is honoured | refuse or ignore the field; must not widen scratch |
| Q | caller writes to the kernel-issued scratch prefix **plus** one durable path | refuse — partial scratch must not launder the durable write |

**Availability — the L-class set, replacing the single probe L.**
Withdrawn in EXP-002 because one request cannot support a no-denial-of-service claim.

| Probe | Legitimate request | Prediction |
|---|---|---|
| L1 | scratch-only analysis (ClaimProtocol) | execute |
| L2 | clean operational deployment (OperationalRequest) | execute |
| L3 | claim-state revision, reads only | execute |
| L4 | concept formulation with a genuinely empty effect, declared through the kernel's own path | execute |
| L5 | operational deployment writing to both kernel scratch and an authorized durable target | execute |

L4 is the sharp one: if determinacy is kernel-established, there must still be a legitimate way
to register a concept that touches nothing. If no such path exists, the fix has made a whole
subject class unreachable — a denial of service dressed as rigour. **L4 is the probe most likely
to fail, and it is a failure of the remedy, not of the caller.**

## 4. Unpredicted probes

EXP-002's lesson was that the probe with no prediction is the one that found the defect. Two
probes here carry **no prediction** and are reported as observed:

- **Probe R — derivation-order dependence.** Supply a footprint that satisfies two derivation
  branches at once. Whether the kernel's branch order, rather than the effect, decides the
  subject is not predicted.
- **Probe S — scratch reuse across requests.** Present a kernel-issued scratch prefix from a
  *previous* request on a new one. Whether the prefix is bound to the request that received it
  is not predicted.

Probe S is the one I expect to be wrong about, which is why it carries no prediction.

## 5. Primary endpoints

1. Regression: EXP-002 probes permitting execution. Target 0, K included.
2. Class closure: N, O, P, Q deviating from required. Target 0.
3. Availability: L1–L5 refused. **Target 0 refusals.** Any refusal here is a finding against the
   remedy.
4. R and S: reported as observed, not scored.

## 6. Stopping rules

Unchanged and binding. Kernel v3 is written before the probe file. Single run. First result
recorded. No probe removed after the run; no patch applied inside this experiment. An exception
is an error, not a refusal.

If an unpredicted probe executes, the class is **not** closed, and the residual is stated rather
than resolved here.

## 7. What this cannot establish

That the class is closed. Three fixed inputs and nine probes are three inputs and nine probes.
The audit itself says a v3 that adds an input adds a row.

That any of it transfers to CageOS. The finding that motivated this line was read from the
public `run_demo.py`, which is a post-hoc verifier, single-source and awaiting independent
digest confirmation — not the enforcement engine, which is not published.

That either framework works. No IS-\*, SR-\*, or CSRF-1–6 test is run here. These probes bind to
CP-T9 and CP-T4 per [`../TEST_BINDING.md`](../TEST_BINDING.md).
