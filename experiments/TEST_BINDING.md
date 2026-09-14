# Binding of experiment probes to the canon's test catalog

Written in response to **G-new-5** of the 2026-09-14 handoff packet:

> "Parallel unofficial experiment catalog if new infrastructure is not bound to IS-\*, SR-\*,
> CSRF-1–6, CP-T\*."

EXP-001 and EXP-002 were written as a fresh probe series (A–M) without binding to the
canon's existing adversarial tests. That is the defect G-new-5 names, and this file closes it.
Where a probe instantiates a catalogued test, it is now recorded as an instance of that test,
not as a new one.

## Bindings

| Probe | Canon test | Relationship |
|---|---|---|
| A, B, C | **CP-T4** Three-Gate Non-Compensation | Direct instances — single-gate failure with the other two passing, one per constitution. |
| D | **CP-T12** Mediated Revocation | Instance — an operational assertion attempting to pardon an upstream scientific failure directly rather than through a typed invalidation event. |
| E | **CP-T13** Witness Disagreement | Instance — a witness attempting to mint authority instead of triggering review. |
| **F, I, J, K** | **CP-T9** Authoritative-Subject Confusion | Direct instances. F is the positive case (subject misdeclared, executed under v1). I is the abstention branch. J and K attack the derivation that v2 substituted for the declaration. |
| G | **CP-T3** Maturity Leakage | Instance — aggregation of gate outcomes into a composite score, the collapse CP-T3 names. |
| M | **CP-T6** Concept-Artifact Independence | Partial — a durable effect aimed outside the adjudicated boundary. CP-T6 is about concept/artifact separation; the fit is loose and this binding is weak. |
| H | *unbound* | Amendment-as-weakening during a run. No catalogued test covers it. Proposed as **CP-T15**, not accepted. |
| L | *unbound* | Availability control. Not an adversarial test; it exists so a refuse-everything kernel cannot score as secure. |
| CONTROL | *unbound* | Positive control, same reason. |

## Consequence for how the results are read

CP-T9 is the test that both experiments turn on. Under the canon's own catalogue, **CP-T9 has
now been run against a reference implementation twice and failed twice** — once as declaration
(EXP-001, probe F) and once as derivation-from-declaration (EXP-002, probe K). CP-T4, CP-T12,
CP-T13 and CP-T3 passed against that same implementation in both runs.

No IS-\*, SR-\*, or CSRF-1–6 test has been run. Those bear on the frameworks; these bear on one
kernel.

## Correction of the record

An earlier statement in this session held that four reviewing lineages had failed to find the
subject-relabeling channel. **That is false and is retracted.** Part VIII.4 of the handoff
packet lists, among the channels still needing probes:

> "subject relabeling across ClaimProtocol / ClaimStateRevision / OperationalRequest"

The channel was named in review before it was probed. What the run added was not the
identification — it was the demonstration that the channel *executes*, the mechanism (authority
is derived from the declaration, so the gate is never summoned rather than bypassed), and the
subsequent finding that deriving from a second declaration inherits the same defect.

Naming a channel and demonstrating it are different acts. Crediting the run with the
identification was an overclaim, and it is the kind an author makes in his own favour.
