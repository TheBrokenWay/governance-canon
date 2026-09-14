---
type: amendment
amends: canon/TRIPLE_GOVERNANCE.md, canon/CSRF.md
amendment_date: 2026-09-14
recorded_by: James Andrew Tillar
status: proposed — not accepted
---

# Framework amendment — 2026-09-14

This note **amends and does not edit**. The three source documents dated 2026-07-21 are
unchanged. Per the standing rule, sealed files are never edited; amendments are new versions.
Source documents are held in a private archive and published here as `canon/`.

## A-1. Constitution count: three constitutions, four authoritative subjects

**Observed.** `canon/CSRF.md` §3.13 reads
"Three non-compensable constitutions govern different privileges:" and then enumerates four
numbered items. `canon/TRIPLE_GOVERNANCE.md` §6.0 likewise
tabulates four authoritative subjects under the name "Triple Governance."

**Reconciliation already present in the source.** §6.2 states that the scientific constitution
"has two outputs that must remain distinct" — protocol admissibility and claim state. The count
is therefore consistent as written, but only to a reader who reaches §6.2.

**Amendment.** State the resolution at first use:

> Triple Governance names **three constitutions** — Structural, Scientific, Operational — which
> adjudicate **four authoritative subjects**. The Scientific constitution issues two outputs that
> must never be merged: protocol admissibility (`ClaimProtocol@version`) and claim state
> (`ClaimStateRevision@version`). Passing the protocol gate is not support. Support is not
> authorization.

**Why this matters beyond tidiness.** If these documents become standing agent instructions, an
agent that reads "three" and finds four has to guess which pair to merge. The likeliest wrong
merge is protocol-admissible into supported — which is the precise collapse CSRF Law 8 and
separation invariants 3, 4 and 5 exist to prevent. An ambiguity here defeats the rule it
describes.

**Scope of this amendment.** Editorial and clarifying. It changes no gate, invariant, law, or
decision state. Nothing in the 2026-07-21 record is recoded.

## A-2. Witness plane — restate the negative at first use

§6.4 states that independent observers and adversarial test agents are not a fourth
constitution. That sentence arrives after
the reader has already counted four subjects and may be reaching for a fourth constitution to
put them in. Recommend the disclaimer move up beside A-1, so the count and the exclusion are
read together.

## A-3. Concept-provenance record for this amendment

```text
ConceptID:        (to be assigned by the architect)
Canonical name:   Triple Governance constitution count
Program:          Triple Governance
Lifecycle status: Active
Recorded origin:  Amendment 2026-09-14 — first explicit statement of the
                  three-constitutions / four-subjects resolution at first use.
                  Not a claim of novelty or priority; the reconciliation is
                  already present at §6.2 of the 2026-07-21 source.
Formulation:      v1 — three constitutions, four authoritative subjects,
                  Scientific issuing two separated outputs
Depends on:       CSRF §3.13, Triple Governance §6.0, §6.2, §6.4
Supersedes:       nothing. The source formulation stands.
```

## Claim states recorded by this note

| Claim | State |
|---|---|
| The source documents contain a count ambiguity at first use | supported under declared scope (direct quotation, §3.13 and §6.0) |
| The ambiguity is resolved later in the same document | supported under declared scope (§6.2) |
| The ambiguity would cause agent error if used as standing instruction | unresolved — argued, not tested |
