# CSRF Concept Provenance And Triple Governance

First drafted: 2026-07-21

Status: Candidate research-record and governance specification. It is operationally useful as a traceability design, but it has not been shown to improve scientific reliability over simpler alternatives.

Canonical chronology: RELATIONAL_THEORY_CHAT_LOG_AND_TEST_PLAN_2026-07-21.md (not published)

CSRF specification: [CSRF.md](CSRF.md)

CCTF specification: [CCTF.md](CCTF.md)


## 1. The Three Provenance Graphs

The archive now needs three related but non-interchangeable provenance systems.

### 1.1 Artifact provenance

Question: Where did this file, dataset, receipt, model, or implementation artifact come from?

Primary relations include generation, use, transformation, derivation, revision, responsible actor, time, and artifact hash.

### 1.2 Chronological provenance

Question: When did an observation, formulation, decision, or revision enter the research record?

Primary relations include event order, revision order, contemporaneous rationale, triggering observations, and what information was available at the time.

### 1.3 Concept provenance

Question: Where did this idea enter this archive, what does it mean now, and how did its intellectual identity evolve?

Primary relations include stable identity, formulation history, aliases, dependencies, use, evaluation, derivation, split, merge, supersession, retirement, and revival.

These are different graphs. A concept can move between files without changing identity. A file can change without changing a concept. Two concepts can merge while all original artifacts remain intact.

The three graphs must cross-reference one another, but none may substitute for another.

## 2. Concept Identity And Formulation

A concept is a first-class research object. Its stable identity is distinct from every wording used to express it.

```text
ConceptIdentity(
    concept_id,
    canonical_name,
    aliases,
    program,
    lifecycle_status,
    recorded_origin,
    current_formulation_id,
    genealogy
)

ConceptFormulation(
    formulation_id,
    concept_id,
    version,
    text,
    recorded_at,
    recorded_by,
    specified_in,
    depends_on,
    used_by,
    evaluated_by,
    change_reason,
    limitations,
    artifact_hashes
)
```

Null hypotheses, empirical claim states, transfer results, and operational permissions are linked records rather than fields on `ConceptIdentity`.

Identity rules:

1. A rename or improved wording retains the same `concept_id` and creates a new formulation.
2. A genuine conceptual split creates child concept IDs and records `split_from` and `split_into` edges.
3. A merge creates a new identity or a declared surviving identity and records every source concept.
4. Supersession retires a formulation or concept from normative use but never deletes it.
5. Revival appends a new formulation with an explicit reason; it does not erase the retirement interval.
6. Moving a concept between documents changes `specified_in`, not concept identity.
7. `recorded_origin` means the earliest explicit occurrence recovered in this archive. It is not a claim of novelty or priority in the scientific literature.
8. Registration records lineage only. It does not count as evidence for the concept.
9. Concept IDs are opaque. Their numbers carry no rank, age, truth, maturity, or dependency meaning.

Recommended genealogy relations:

```text
renamed_from       same identity, prior label
derived_from       distinct identity influenced by a parent
split_from         child created by decomposition
split_into         parent points to all children
merged_from        successor created from multiple concepts
merged_into        source points to successor
supersedes         new concept or formulation replaces normative use
superseded_by      inverse of supersedes
related_to         association without inheritance
co_defined_with    explicit mutual definition; not a hidden dependency cycle
```

## 3. Maturity Is A Derived Vector

`Active`, `experimental`, `operational`, and `supported` answer different questions. They must not be collapsed into one status or score.

The vector is an interface projection, not an authoritative record attached to a concept. Each component is derived from a different typed subject:

- lifecycle status belongs to `ConceptIdentity`;
- formulation maturity belongs to a versioned `ConceptFormulation`;
- scientific protocol admissibility belongs to a `ClaimProtocol`;
- evidence maturity belongs to a scoped `ClaimStateRevision`;
- transfer maturity belongs to a declared cross-domain test program;
- operational permission belongs to an `OperationalRequest` for a specific privilege, target, and scope.

A concept may have multiple formulations, claims, tests, and operational requests in different states at the same time. Therefore no flat concept-level status may be used as authoritative input to another gate.

### 3.1 Lifecycle status

```text
proposed
active
split
merged
superseded
retired
```

### 3.2 Formulation maturity

```text
draft
structurally_admissible
operationalized
```

### 3.3 Evidence maturity

```text
none
exploratory_only
mixed
supported_under_declared_scope
weakened
contradicted_under_declared_scope
```

These are CSRF claim-relative states. They apply to one versioned claim under declared scope, not to the concept as a whole. `Supported` is never terminal and never applies globally without context, evidence relations, uncertainty, and revision.

### 3.4 Transfer maturity

```text
not_cross_domain_tested
cross_domain_tested
failed_to_transfer
```

### 3.5 Operational maturity

```text
not_assessed
sandbox_only
operationally_approved_under_scope
implemented
monitored
rolled_back
```

A user interface may therefore summarize a concept as active, containing a structurally admissible formulation, having one unresolved claim, not cross-domain tested, and linked to one sandbox-only operational request. The underlying typed records remain authoritative. This is more precise than calling the concept simply mature or valid.

## 4. Canonical Example

The initial record for claim-relative evidence is:

```text
Claim-relative evidence
Origin:
    Conversation 2026-07-21

Moved to:
    CSRF 3.6

Tests:
    SR-2
    AG
    AH

Depends on:
    Observation
    Claim
    Context estimate
    Provenance

Supersedes:
    Intrinsic evidence polarity
```

This is the minimal human-readable provenance view supplied by the architect. In the canonical graph, `Moved to` is normalized as `specified_in`: the concept retains identity while its current formulation becomes specified in CSRF 3.6. `Supersedes` targets the prior formulation, not every historical artifact that used it. The normalized record adds typed versions, source dependence, uncertainty, uses, limitations, and evaluation status without rewriting the originating formulation.

```text
ConceptID: CP-00047
Stable identity: Claim-relative evidence
Canonical name: Claim-relative evidence relation
Aliases: EvidenceRelation
Program: CSRF
Lifecycle status: Active

Recorded origin:
    Conversation 2026-07-21
    First explicit formulation recovered in this archive

Current specification:
    CSRF 3.6

Formulation history:
    v1: Evidence polarity
    v2: Evidence polarity is not intrinsic to an observation
    v3: Evidence is relative to observation, claim, and context
    v4: Typed EvidenceRelation including rival hypotheses,
        source dependence, uncertainty, and provenance

Superseded formulation:
    Observation has intrinsic evidence polarity

Depends on:
    Observation
    Claim state
    Context estimate
    Source dependence
    Uncertainty
    Provenance

Used by:
    ClaimRevisionRecord
    ClaimLifecycle
    EvidenceRelation
    RevisionAudit

Evaluated by:
    SR-2
    AG
    AH

Supplementary dependency test:
    SR-3 - acquisition and context identifiability

Primary evaluation protocol:
    Protocol ID: CP-00047-BENEFIT-v1
    Target claim: Claim-relative evidence improves scientific decisions
    Mundane null: Intrinsic evidence tagging is sufficient at equal
        reliability and cost

Current limitations:
    Not yet experimentally validated
    Context and dependence may be incompletely identifiable
    Added metadata may increase burden without improving decisions

Derived interface projection, non-authoritative:
    Current formulation: Structurally admissible
    Primary claim state: Unresolved; no comparative evidence acquired
    Transfer program: Not cross-domain tested
    Operational request: None issued

Retirement criteria:
    A simpler intrinsic or claim-light evidence model reaches an equivalent
    or better reliability-cost frontier across preregistered domains

Current version: v4
```

## 5. Genealogy Examples

### 5.1 Compatibility split

```text
ConceptID: CP-00012
Canonical name: Compatibility
Derived from: Constraint compatibility
Split revision: R3
Children:
    Physical compatibility
    Epistemic compatibility
    Normative compatibility
    Goal compatibility
```

The parent remains in the historical graph. The child concepts must not inherit support automatically; each receives its own claim protocols, nulls, scopes, tests, and derived maturity projection.

### 5.2 Research-program split

```text
ConceptID: CP-00081
Canonical name: Unified intelligent-scientific reasoning program
Lifecycle status: Split
Split into:
    CCTF - candidate intelligent-systems theory and architecture
    CSRF - candidate scientific-reasoning framework
Reason:
    Computational and methodological claims became independently testable
Revision: R6
```

The split creates a validation firewall. CCTF performance cannot establish CSRF reliability, and CSRF process compliance cannot establish CCTF as a theory of intelligence.

### 5.3 Formulation continuity

```text
ConceptID: CP-00041
Stable identity: Claim revision
Formulation history:
    v1: Model updates
    v2: Versioned claims
    v3: Append-only revision history
    v4: Auditable ClaimRevisionRecord
```

This is one concept only if reviewers judge that the referent remained continuous. If a later formulation changes the failure conditions, scope, or operational role enough to constitute a different idea, the registry must split it rather than preserve continuity for convenience.

## 6. Triple Governance

The three provenance graphs describe lineage. The three governance layers control what an idea is permitted to do. Provenance and governance are orthogonal.

An idea does not need approval to exist in the archive. Archival existence is unconditional once proposed. Gates grant capabilities and state transitions; they do not erase ideas.

### 6.0 Authoritative Subjects

Each constitution governs a different typed subject:

| Constitution | Authoritative subject | Question answered |
|---|---|---|
| Structural | `ConceptFormulation@version` | Is this formulation machine-representable and internally well formed? |
| Scientific protocol | `ClaimProtocol@version` | Is this claim and test protocol scientifically admissible for the declared evaluation? |
| Scientific claim state | `ClaimStateRevision@version` | What does the current evidence justify for this claim under this scope? |
| Operational | `OperationalRequest@version` | May this requested privilege affect this target under this scope? |

Concept identity is preserved across all decisions. A gate never grants a global property to the concept merely because one formulation, claim, or requested use passed.

### 6.1 Structural Constitution

Question: Is this versioned formulation sufficiently well formed to be referenced as a defined research object?

Non-compensable checks:

- stable concept identity and current formulation;
- explicit scope and terms;
- complete recorded origin and formulation history;
- resolvable dependencies, uses, and test links;
- internally consistent genealogy;
- explicit limitations and lifecycle or retirement criteria where applicable;
- resolvable links to any separately governed claim protocols;
- no duplicate identity or silent semantic drift;
- no provenance field represented as evidential support.

Passing grants `REGISTERED` or `STRUCTURALLY_ADMISSIBLE` to that formulation version. It says nothing about empirical truth, scientific value, or deployment readiness. Other possible outputs are `STRUCTURALLY_REJECTED` and `NEEDS_REVISION`; rejection preserves the formulation and reasons.

### 6.2 Scientific Constitution: CSRF

CSRF has two outputs that must remain distinct.

Protocol question: Is this versioned claim protocol admissible to a declared scientific evaluation?

Non-compensable checks:

- claim and scope are explicit;
- a mundane null and strongest plausible rivals are recorded;
- discriminating predictions and potential falsifiers exist;
- observations are separated from claim-relative evidence;
- acquisition, context, uncertainty, and source dependence are modeled;
- success criteria and prohibited rescue rules are frozen prospectively;
- negative results and revisions will remain auditable;
- evidence maturity is not inferred from structural approval.

Protocol outputs are `SCIENTIFICALLY_ADMISSIBLE_FOR_TEST`, `NEEDS_REVISION`, and `INADMISSIBLE_PROTOCOL`. Passing this gate does not mean supported, validated, or true.

Claim-state question: Given acquired observations and claim-relative evidence, what claim state is justified under the declared context and scope?

Claim-state outputs are `UNRESOLVED`, `SUPPORTED_UNDER_SCOPE`, `WEAKENED`, `CONTRADICTED`, and `SUPERSEDED`. Every output is a versioned `ClaimStateRevision` with uncertainty, evidence relations, provenance, rivals considered, revision triggers, and limitations. Procedural compliance cannot substitute for empirical support.

### 6.3 Operational Constitution: Platform Governance

Question: May this requested privilege influence a specific software target, experiment, user surface, external system, or production decision?

Non-compensable checks:

- intended operational scope and affected components are declared;
- the requested use declares its scientific requirement as `NONE`, `PROTOCOL_ADMISSIBLE`, or `SUPPORTED_UNDER_MATCHING_SCOPE`;
- risks, safety boundaries, reversibility, and rollback are defined;
- implementation and evaluator independence are assessed;
- exact tests and monitoring are specified;
- deployment authority is identified;
- receipts can be checked against actual execution;
- production impact cannot be inferred from scientific interest alone.

Possible decisions include `SANDBOX_ONLY`, `EXPERIMENT_APPROVED`, `SHADOW_APPROVED`, `DEPLOYMENT_APPROVED`, `REJECTED_FOR_OPERATION`, and `ROLLED_BACK`. Passing grants only the declared operational capability for the identified target, privilege, scope, policy version, and validity interval.

### 6.4 Independent Witness Plane

Independent observers and adversarial test agents are not a fourth constitution. They form a witness plane that records observations, executes adversarial tests, and compares gate receipts with actual postconditions.

A witness may disagree with the system it observes. It may trigger review, quarantine, or revocation processing, but it does not silently mint structural, scientific, or operational authority. Its identity, code digest, custody, inputs, observations, and limitations must be explicit.

## 7. Gate Separation Invariants

1. The gates are constitutions, not votes. Two passes cannot compensate for one failed non-compensable rule.
2. Gate decisions are not averaged into a scalar maturity or confidence score.
3. Structural approval cannot create evidential support.
4. Scientific support cannot authorize deployment.
5. Operational approval cannot make a scientific claim true.
6. Failure at any layer preserves the concept, decision, reasons, and evidence state.
7. A rejected formulation can be revised without acquiring a new concept ID if identity remains continuous.
8. A sandbox may host an unsupported hypothesis only when the operational receipt prohibits production influence and the interface preserves its evidence maturity.
9. A production decision based on a scientific claim requires all relevant gates, but each gate's receipt remains separate.
10. Every transition is scoped, versioned, reversible where possible, and auditable.
11. An upstream scientific change emits a typed invalidation or review event; it does not directly mutate operational permission.
12. Operational policy independently decides whether to retain, quarantine, revoke, or roll back the privilege and emits its own receipt.
13. High-risk privileges may fail closed automatically on a signed scientific invalidation only when that dependency and response were declared prospectively in operational policy.
14. A single issuer, signing key, service, or generic verdict field cannot satisfy multiple constitutions unless an explicit root policy grants each separate authority class; production policy should prohibit such concentration.
15. Interface summaries are lossy projections and may not re-enter any evidence or authorization graph as independent input.

The authoritative record surface is therefore relational rather than one concept-status object:

```text
ConceptIdentity
    -> ConceptFormulation -> StructuralGateReceipt
    -> ClaimProtocol -> ScientificProtocolReceipt
    -> ClaimStateRevision -> EvidenceRelation[]
    -> OperationalRequest -> OperationalGateReceipt
    -> WitnessObservation[]
```

Any flat lifecycle display is derived from these records. No field silently determines another.

## 8. Project-Family Mapping — redacted in the public edition

This section is withheld. It maps the constitutions onto a specific private implementation.
That is operational detail about one deployment, not part of the framework. One sentence removed
with it was normative rather than descriptive — a prohibition on unauthorized implementation —
and its substance is preserved in §10.

Nothing load-bearing is removed. Sections 1-7 define the constitutions, the authoritative
subjects, the gate outputs, and the fifteen separation invariants; sections 9-12 define the
adversarial tests, the current null, the standards boundary, and the verdict. The framework is
complete and testable without this section.

The redaction is declared rather than silent. `canon/SHA256SUMS` records the digests of the
published bytes; `REDACTIONS.md` separately records the digest of the unpublished full document,
so any later disclosure can be checked against the version that existed on the publication date.

## 9. Adversarial Tests

### CP-T1: Rename Versus New Identity

Seed renames, material scope changes, and entirely new concepts. Test whether reviewers and validators preserve IDs for genuine reformulations while splitting materially different ideas.

Failure: identity is preserved merely because wording overlaps, or a harmless rename destroys lineage.

### CP-T2: Split And Merge Integrity

Seed concept splits and merges with missing inverse edges, inherited evidence, dangling children, and cycles.

Failure: genealogy cannot be reconstructed, or descendants inherit empirical support automatically.

### CP-T3: Maturity Leakage

Mark a concept structurally admissible and operationalized but empirically unsupported.

Failure: an interface, reviewer, or downstream store reports it as scientifically supported or production-ready.

### CP-T4: Three-Gate Non-Compensation

Create cases that pass two gates and fail the third. Include a compelling but malformed idea, a well-formed but unfalsifiable idea, and a supported but unsafe deployment.

Failure: majority voting, score averaging, or narrative persuasion overrides the failed constitution.

### CP-T5: Archive Non-Erasure

Reject, supersede, split, merge, retire, revive, and roll back concepts.

Failure: an idea, formulation, gate receipt, prior maturity state, or rejection reason disappears from history.

### CP-T6: Concept-Artifact Independence

Move one concept across documents, duplicate its description, rename files, and edit unrelated text.

Failure: concept identity depends on a file path, duplicates become independent concepts, or unrelated edits create concept revisions.

### CP-T7: Provenance Agreement

Compare concept records with artifact hashes, chronological events, claim revisions, and implementation references.

Failure: the three graphs disagree without a declared correction or dependence relation.

### CP-T8: Simpler-Baseline Challenge

Compare this protocol with version control alone, a structured changelog, and a lightweight ontology registry at matched effort.

Failure: the triple system adds no reconstruction, error-detection, or decision-separation value at a competitive reliability-cost frontier.

### CP-T9: Authoritative-Subject Confusion

Create one concept with two formulations, three claims under different scopes, and two operational requests for different targets.

Failure: a pass, contradiction, or revocation on one subject is copied to the concept or unrelated subjects.

### CP-T10: Protocol-Support Confusion

Admit a rigorous protocol whose experiment has not run, and reject a malformed protocol whose motivating observation is strong.

Failure: protocol admissibility is reported as empirical support, or prior plausibility bypasses protocol defects.

### CP-T11: Cross-Constitution Receipt Forgery

Attempt to use one service identity, key, generic verdict, or copied receipt to satisfy two or three constitutions.

Failure: authority class, issuer allowlist, subject type, scope, policy version, or signature separation is not enforced.

### CP-T12: Mediated Revocation

Issue an operational privilege that prospectively depends on a scoped claim, then weaken or contradict that claim.

Failure: the scientific service directly mutates operational state, the operational layer ignores its declared dependency, or revocation occurs without a separate operational receipt.

### CP-T13: Witness Disagreement

Have the execution service report success while an independent witness observes a failed postcondition or cannot persist its audit event.

Failure: intended state wins automatically, audit failure is silent, or witness disagreement cannot trigger a fail-closed review path.

### CP-T14: Projection Feedback

Generate a concise status summary, remove its lineage metadata, and attempt to ingest it as a new observation, evidence relation, or authorization.

Failure: the summary corroborates its source claim, increases confidence, or grants privilege.

## 10. Current Null And Limitations

Primary null:

> Version control, a conventional ontology/changelog, ordinary scientific review, and existing platform gates provide equivalent traceability and safety with less burden.

Current limitations:

- no comparative experiment has been run;
- stable concept identity sometimes requires judgment rather than mechanical validation;
- dependency graphs can create administrative overhead and false precision;
- reviewers may confuse a complete concept record with a supported idea;
- three gates can become bureaucracy if their permissions overlap;
- one implementation could create common-mode failure across all three gates;
- concept numbering can be misread as priority or authority;
- the operational layer has not been exercised against a reference implementation.

## 11. External Standards Boundary

The implementation should reuse established provenance semantics where they fit rather than presenting every field as novel:

- W3C PROV supplies entity, activity, agent, derivation, revision, primary-source, specialization, and alternate relations.
- SKOS supplies stable concept resources, preferred and alternative labels, broader, narrower, related, history-note, change-note, and scope-note relations.
- RO-Crate is a possible export/package format for research artifacts and metadata.

CSRF-specific additions remain necessary for claim-relative evidence, current nulls, falsifiers, maturity separation, gate receipts, no-epistemic-finality behavior, and operational influence controls. Standards reuse is an interoperability decision, not evidence that CSRF is scientifically superior.

## 12. Current Verdict

Triple provenance and triple governance are compatible but distinct improvements.

The provenance system preserves what happened to artifacts, events, and concepts. The governance system prevents structural quality, scientific admissibility, empirical support, and operational permission from being silently promoted into one another.

The strongest formulation is not "an idea must pass three gates to exist." It is:

> Every idea may remain in the research record. Separate non-compensable constitutions govern whether it may be treated as well formed, admitted to confirmatory scientific testing, or allowed to influence the platform.

More precisely, each constitution grants a scoped privilege to its own typed subject. Concept-level status is only a derived interface view, scientific protocol admissibility is not empirical support, and independent observation is not authority.
