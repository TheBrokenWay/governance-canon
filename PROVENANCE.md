# Concept Provenance

Concept-level lineage for the canon: where each idea entered this archive, what it means now,
and how its identity changed.

This is one of the three provenance graphs. Artifact and chronological provenance live in the
commit history and release tags of this repository. The private research log that the canon
derives from is not published, so the cross-references below cannot be independently checked
against it.

Dates here are `recorded_origin` under rule 7: the earliest occurrence recovered in this
archive. They are not a claim of novelty or priority. No prior-art review has been performed,
and no concept here is asserted to be new.

## Governing rules

These are quoted from `canon/TRIPLE_GOVERNANCE.md` §2 and constrain every record below.

> 7. `recorded_origin` means the earliest explicit occurrence recovered in this archive. It is
>    not a claim of novelty or priority in the scientific literature.
> 8. Registration records lineage only. It does not count as evidence for the concept.
> 9. Concept IDs are opaque. Their numbers carry no rank, age, truth, maturity, or dependency
>    meaning.

Rules 1–6 govern identity under change: renaming preserves `concept_id`; a genuine split
creates children with `split_from` / `split_into` edges; a merge records every source;
supersession retires from normative use but never deletes; revival appends with a reason and
does not erase the retirement interval; moving a concept between documents changes
`specified_in`, not identity.

---

## CP-00081 — Unified intelligent-scientific reasoning program

```text
Lifecycle status: Split
Split into:       CCTF — candidate intelligent-systems theory and architecture
                  CSRF — candidate scientific-reasoning framework
Reason:           Computational and methodological claims became independently testable
Revision:         R6
Specified in:     canon/CCTF.md §0, §13; canon/CSRF.md §1, §15
```

The parent concept is retired from normative use and retained in full. Every "not established
here" list in the two children is a retraction of something the unified program could have
been read as claiming.

## CP-00047 — Claim-relative evidence

```text
Canonical name:   Claim-relative evidence relation
Aliases:          EvidenceRelation
Program:          CSRF
Lifecycle status: Active
Recorded origin:  Conversation 2026-07-21 — first explicit formulation recovered
                  in this archive
Specified in:     canon/CSRF.md §3.6
Tests:            SR-2, AG, AH
Depends on:       Observation · Claim · Context estimate · Provenance
Supersedes:       Intrinsic evidence polarity
Current version:  v4
```

Formulation history:

| Version | Formulation |
|---|---|
| v1 | Evidence polarity |
| v2 | Evidence polarity is not intrinsic to an observation |
| v3 | Evidence is relative to observation, claim, and context |
| v4 | Typed `EvidenceRelation` including rival hypotheses, source dependence, uncertainty, and provenance |

The superseded formulation — *an observation has intrinsic evidence polarity* — is retained
as a retired formulation, not deleted. The current position, quoted:

> "Evidence is a relation, not a property stored permanently on an observation."

Polarity values: `supports`, `weakens`, `contradicts`, `presently uninformative`. Polarity
must be recomputed when the claim, rival set, context estimate, or dependence structure
changes.

## CP-00012 — Compatibility

```text
Program:          CCTF
Lifecycle status: Active
Derived from:     Constraint compatibility
Split at:         R3
Split into:       Physical compatibility · Epistemic compatibility ·
                  Normative compatibility · Goal compatibility
Specified in:     canon/CCTF.md §3.4
```

Each compatibility assertion must declare its type, arguments, context, generator, units or
scale, calibration target, uncertainty, and prohibited uses. Combining types into one scalar
requires a declared aggregation rule and explicit non-compensable dimensions.

> "Compatibility does not explain itself."

## CP-00041 — Claim revision

```text
Program:          CSRF
Lifecycle status: Active
Specified in:     canon/CSRF.md §3.8
Tests:            SR-11
Current version:  v4
```

| Version | Formulation |
|---|---|
| v1 | Model updates |
| v2 | Versioned claims |
| v3 | Append-only revision history |
| v4 | Auditable `ClaimRevisionRecord` |

## Amendment record

| Concept | Amendment | Date | Scope |
|---|---|---|---|
| Kernel-controlled derivation | `experiments/EXP-003-kernel-controlled-derivation/RESULT.md` | 2026-09-14 | **proposed — not accepted.** Class closed (0 of 12 regression, 0 of 4 class). Availability contradicted: L4, a legitimate empty concept formulation, refuses — `ConceptFormulation` unreachable. |
| Invariant 16 — insufficiency of derived subject binding | `experiments/EXP-002-subject-binding/RESULT.md` | 2026-09-14 | **proposed — not accepted.** EXP-002 closed F-1 (0 of 8 regression, 0 of 4 remedy surface) and found probe K: deriving from a caller-supplied footprint inherits the defect. Invariant 16 not promoted. |
| Invariant 1 — subject binding (proposed inv. 16) | `amendments/2026-09-14-experiment-infrastructure.md` | 2026-09-14 | **proposed — not accepted.** Consolidates four-lineage review and EXP-001. Reports one open compensation channel; proposes an invariant that is not implemented or tested. |
| Triple Governance constitution count | `amendments/2026-09-14-constitution-count.md` | 2026-09-14 | **proposed — not accepted.** Editorial; states the three-constitutions / four-subjects resolution at first use. No gate, invariant, law, or decision state changed. |

---

## Maturity — derived interface projection, non-authoritative

Per `canon/TRIPLE_GOVERNANCE.md` §3, the five maturity dimensions answer different questions
and must not be collapsed into one status or score. This table is an interface projection and
is not an authoritative input to any gate.

| Concept | Lifecycle | Formulation | Evidence | Transfer | Operational |
|---|---|---|---|---|---|
| CP-00081 | split | — | — | — | — |
| Invariant 1 (non-compensability) | active | — | contradicted_under_declared_scope | not_cross_domain_tested | not_assessed |
| Proposed invariant 16 (subject binding) | proposed | — | weakened | not_cross_domain_tested | not_assessed |
| Kernel-controlled derivation (v3) | proposed | — | mixed | not_cross_domain_tested | not_assessed |
| CP-00047 | active | — | none | not_cross_domain_tested | not_assessed |
| CP-00012 | active | — | none | not_cross_domain_tested | not_assessed |
| CP-00041 | active | — | none | not_cross_domain_tested | not_assessed |

Invariant 1 is the one row carrying a non-`none` evidence state: EXP-001 found one open
compensation channel in a reference implementation, which contradicts it as a general guarantee
within that declared scope. Every other row is `none`, not `exploratory_only`. `exploratory_only` would assert that data
were acquired and inspected; none have been. No `ClaimStateRevision` exists for any concept
here, no comparative experiment has been run, and no concept has entered a confirmatory
protocol under a preregistered endpoint.

The Formulation column is blank because no structural gate has been executed against any
formulation in this archive. Per §3 and §7 that column is derived from a `StructuralGateReceipt`;
no receipt exists, so there is nothing to derive it from.
