# Constitutional Scientific Reasoning Framework (CSRF)

## Standalone Claim Formation, Adjudication, And Audit Specification

First drafted: 2026-07-21

Status: Candidate theory of scientific reasoning, methodological framework, and falsifiable research program. It has not yet been shown to improve science, reproducibility, calibration, or error discovery over strong conventional practice.

Program name: Constitutional Scientific Reasoning Framework (CSRF)

Naming rule: "Constitutional" means that a small set of declared epistemic constraints is non-compensable during claim adjudication. It does not mean legally constitutional, morally infallible, scientifically validated, or guaranteed to produce truth.

Canonical chronology: RELATIONAL_THEORY_CHAT_LOG_AND_TEST_PLAN_2026-07-21.md (not published)

Companion architecture: [CCTF.md](CCTF.md)

Concept and governance lineage: [TRIPLE_GOVERNANCE.md](TRIPLE_GOVERNANCE.md)


## 0. Purpose

This document isolates the second research program that emerged from the PredX conversation and names it the Constitutional Scientific Reasoning Framework (CSRF):

> How should a human, AI, or hybrid research process acquire observations, update models, compare explanations, govern decisions, and audit claims without confusing names, coherence, confidence, or internal receipts with truth?

This is a framework for scientific reasoning. It is implementation-neutral. It can govern a notebook, laboratory, statistical pipeline, conventional software system, AI assistant, or mixed research team.

It does not require CCTF to be a correct theory of intelligence. It does not assume that relationships, compatibility, transformations, or any other proposed component are primitives of cognition. Its own value must be measured against strong existing scientific workflows at matched effort.

## 1. Scope Boundary

### Included here

- distinction among reality, acquisition, observation, model, claim, and evidence
- provenance and source dependence
- context observation and context uncertainty
- competing hypotheses and mundane alternatives
- claim-relative evidence polarity
- negative, contradictory, and uninformative evidence
- confidence, calibration, and abstention
- coherence versus empirical correspondence
- prospective predictions and falsifiers
- preregistration and prohibited rescue
- decision and action governance
- independent audit and common-mode failure
- negative-result preservation
- objective-diverse and anti-elegance review
- label accountability and interface feedback
- reproducibility, replication, cost, and burden
- concept identity, formulation, genealogy, maturity, and governance provenance

### Not established here

- that this is a complete philosophy of science
- that one workflow is optimal for every discipline
- that formal receipts guarantee truth
- that more metadata necessarily improves inference
- that an AI reviewer is independent because it has a different role prompt
- that agreement among reviewers is validation
- that falsifiability is the only criterion of scientific value
- that all evidence can be reduced to one scalar
- that a person's identity should be inferred from a relational representation

### Distinction from the companion architecture

The intelligent-systems document asks what a candidate computational system should represent and how it should act. This document asks what procedures improve the reliability of claims, regardless of what kind of system performs them.

An architecture can implement this framework badly. A research team can use this framework without implementing the architecture. A positive result for either document is not evidence for the other unless a separate bridge hypothesis is preregistered and tested.

## 2. Central Epistemic Principle

### 2.1 Core theory

> Scientific reasoning becomes more reliable when the path from acquisition to claim is governed by a small set of explicit, non-compensable epistemic constraints, while models, confidence, labels, actions, and audits remain corrigible.

This is the central CSRF hypothesis. "More reliable" must be operationalized through calibration, error detection, reproducibility, correspondence with held-out outcomes, resistance to circular evidence, and total cost. The hypothesis fails in a tested setting if strong conventional practice reaches an equivalent or better reliability-cost frontier.

### 2.2 Label principle

Original design principle:

> Labels may be emitted afterward, but labels must not control truth.

Operational form:

> A name may index, retrieve, organize, and compress information, but no claim may be marked supported because the name was assigned. Support must resolve to inspectable observations, acquisition records, claim-relative evidence, declared assumptions, comparison with alternatives, and an auditable decision path.

This principle does not imply that labels are useless or that named objects are unreal. It prevents a category from acting as evidence for itself.

### 2.3 Constitutional core

The CSRF constitution consists of rules that a soft score, persuasive narrative, reviewer vote, or claimed utility cannot override:

1. **Reality separation:** no observation, model, label, confidence score, consensus, or receipt is equated with external reality.
2. **Acquisition traceability:** every empirical observation retains the process that produced, selected, or transformed it.
3. **Claim-relative evidence:** an observation receives evidential polarity only relative to a declared claim, rival set, context estimate, and dependence structure.
4. **Rival requirement:** a confirmatory claim competes with a mundane null and the strongest plausible alternatives identified before outcome access.
5. **Correspondence requirement:** coherence and explanatory elegance cannot substitute for held-out or independently acquired correspondence tests.
6. **Dependence preservation:** duplicated, derived, or circular sources cannot be counted as independent confirmation.
7. **Uncertainty preservation:** insufficient or unidentifiable evidence requires uncertainty or abstention rather than forced classification.
8. **Governance separation:** permission to act cannot make a factual claim true, and evidential support cannot by itself authorize an action.
9. **Action fidelity:** proposed, authorized, executed, and observed actions remain distinct records.
10. **Audit fallibility:** a receipt is a testable claim about process execution, not proof that the process occurred.
11. **Label non-self-validation:** a category cannot serve as evidence for the claim named by that category.
12. **Historical integrity:** negative results, contradictions, deviations, and superseded hypotheses remain visible.
13. **No retrospective rescue:** confirmatory definitions, endpoints, contexts, exclusions, margins, and success rules cannot change after unblinding to preserve the original claim.
14. **Revisability:** every claim status remains scoped, time-indexed, versioned, and open to revision by later observations and evidence relations.
15. **No epistemic finality:** CSRF may produce justified claim states, but no wording, confidence level, interface summary, governance result, or stored status may make a claim practically unrevisable.
16. **Concept lineage:** consequential concepts retain stable identities, formulation revisions, recorded archive origins, dependencies, genealogy, current locations, linked tests, and maturity states; registration and structural approval never count as evidential support.

The constitution can be revised prospectively through a versioned process. A revision cannot be applied retroactively to recode a completed confirmatory result. If a proposed rule adds no reproducible value or creates unacceptable burden, it should be amended or removed for future protocols rather than defended as doctrine.

### 2.4 Revisable claim vocabulary

CSRF principle on `knowledge`:

> `Knowledge` is not a first-class state within CSRF because it implies unwarranted finality. CSRF represents only versioned, justified, revisable claim states supported by explicitly modeled evidence relations under declared context and uncertainty.

This is an epistemic design decision, not a stylistic word ban. The term may appear when quoting an external theory, defining this boundary, or constructing an adversarial test input. It may not be used as a CSRF claim-state value, evidence type, substitute for correspondence, or reason to bypass revision.

CSRF defines no terminal epistemic state. Its canonical epistemic-state vocabulary is:

- observation
- evidence relation
- claim state
- revision
- correspondence
- uncertainty
- provenance

A claim can be `supported under declared scope`, `weakened`, `contradicted`, `unresolved`, or `superseded`. Each status carries a version, context, time, evidence relations, and uncertainty. None closes the claim against later acquisition or revision.

CSRF may still discuss acquisition, hypotheses, calibration, governance, and audit as operations, methods, or artifacts. None denotes a terminal epistemic state. This vocabulary rule applies only to CSRF; it does not restrict the computational language used by theories CSRF evaluates.

## 3. Epistemic Units

### 3.1 External reality

External reality is the target phenomenon presumed to exist independently of the current representation. It is an epistemic referent, not an item directly stored in a research system.

It is the external referent that claims attempt to correspond to but never become.

No record, model, label, consensus, or receipt is equated with reality.

### 3.2 Acquisition event

An acquisition event is the process that selects or produces an observation. It includes sensing, retrieval, sampling, measurement, parsing, experimentation, interview, database query, or instrument readout.

Minimum acquisition metadata:

- source and source type
- instrument, query, protocol, or retrieval method
- sampling frame and selection rule
- units and reference scale
- timestamp and temporal validity
- relevant context observations
- transformations and preprocessing
- known source dependence
- missingness and exclusions
- uncertainty and quality controls
- immutable artifact identifier or hash where practical

Acquisition is not a passive neutral bridge. It can be selective, delayed, lossy, biased, duplicated, adversarially corrupted, or changed by earlier actions.

### 3.3 Observation

An observation is the output of a declared acquisition event before its role in a claim is adjudicated.

Observations should be preserved in their acquired form and linked to transformations. Correction creates a versioned record; it does not silently rewrite history.

An observation does not have permanent intrinsic polarity. The same result can support one hypothesis, weaken another, and remain uninformative for a third.

### 3.4 Model

A model is a revisable representation used to explain, predict, compress, simulate, or guide intervention. Coherence or usefulness alone gives it no terminal epistemic status.

Every consequential model update should identify:

- prior version
- observations used
- update rule or analysis code
- assumptions introduced or removed
- state or parameter changes
- retractions and corrections
- resulting version

### 3.5 Claim and competing hypotheses

A claim is a proposition with a declared scope, population, context, time, purpose, and possible failure conditions.

Before confirmatory outcome access, record:

- target claim
- mundane null
- strongest plausible rivals
- predictions that differ among them
- observations that would weaken each one
- conditions under which the hypotheses are not identifiable

An elegant unified explanation receives no presumption of truth. At least one reviewer should construct the least unified conventional explanation that fits the same observations.

### 3.6 Evidence relation

Evidence is a relation, not a property stored permanently on an observation:

```text
EvidenceRelation(observation_id, claim_id, competing_hypotheses,
                 estimated_context, polarity, weight, dependence,
                 uncertainty, provenance)
```

Permitted qualitative polarity includes:

- supports
- weakens
- contradicts
- presently uninformative

Weight requires a declared rule. Repeated derivatives of one source cannot be counted as independent confirmation. Evidence polarity must be recomputed when the claim, rival set, context estimate, or dependence structure changes.

### 3.7 Claim revision

A change in claim state is itself an auditable object. The current state is not an adequate substitute for the path that produced it.

```text
ClaimRevisionRecord(
    claim_id,
    from_revision,
    to_revision,
    prior_status,
    revised_status,
    triggering_observation_ids,
    acquisition_record_ids,
    evidence_relation_deltas,
    competing_hypotheses_considered,
    context_delta,
    uncertainty_and_calibration_delta,
    governance_decision_ids,
    rationale,
    actor,
    timestamp,
    code_and_artifact_hashes
)
```

A revision can add support, weaken a claim, expose contradiction, narrow scope, increase uncertainty, supersede a mechanism, or restore an unresolved state. Corrections append a new revision; they do not overwrite the earlier record.

The precise CSRF report form is:

> At revision `r`, claim `c` is supported under declared scope `s` by evidence relations `e`, under estimated context `k`, with uncertainty and calibration state `u`.

This makes the basis and limits of a claim inspectable without implying a terminal state.

### 3.8 Context

Keep three items separate:

- actual external context, which may remain unknown
- acquired observations about context
- the researcher's or model's estimated context

Context can alter measurement validity, causal mechanism, compatibility, interpretation, and permissible action. It must not be added after results merely to rescue a failed claim.

### 3.9 Confidence, coherence, and correspondence

- **Confidence** is the strength of commitment or represented probability.
- **Calibration** compares confidence with observed frequencies or outcomes.
- **Coherence** is consistency within a represented system.
- **Correspondence** is agreement with independently acquired reality-bearing observations.

A claim can be coherent and false, confident and miscalibrated, procedurally valid and scientifically wrong, or empirically useful without a correct causal explanation.

### 3.10 Decision, action, and governance

Scientific adjudication and action authorization are related but distinct.

- Epistemic adjudication asks what the evidence currently supports.
- Governance asks what decision or action is permitted for a declared purpose.

Record separately:

```text
proposed_decision_or_action
governance_result
authorized_decision_or_action
executed_decision_or_action
independently_observed_consequence
```

Ethical, legal, safety, and resource constraints can prohibit an action even when a factual claim is well supported. Permission does not make a factual claim true.

### 3.11 Receipt and audit

A receipt is a claim about what a process executed. It is not automatically truthful.

A strong audit compares the receipt with independently instrumented observations of acquisition, analysis, gate execution, action, and artifact state. Where full independence is impossible, record shared code, data, models, personnel, prompts, and infrastructure as common-mode risks.

### 3.12 Label and interface

Labels are compression and communication interfaces. They can also create anchoring, circular retrieval, premature closure, and feedback laundering.

An emitted summary or label must not return as apparently independent evidence unless its lineage is preserved and its dependence is modeled.

### 3.13 Concept provenance and governance state

Concept provenance is distinct from artifact and chronological provenance. It records an idea's stable identity, changing formulations, aliases, dependencies, uses, tests, splits, merges, supersession, retirement, and revival independently of the files in which it appears.

Concept lifecycle, formulation maturity, protocol admissibility, evidence maturity, cross-domain testing, and operational permission remain separate. They are not authoritative fields on one concept record. Structural state belongs to a versioned formulation, protocol admissibility belongs to a versioned `ClaimProtocol`, evidence maturity belongs to a scoped `ClaimStateRevision`, and operational permission belongs to a requested privilege for a specific target and scope.

Three non-compensable constitutions govern different privileges:

1. Structural governance determines whether a formulation version is sufficiently well formed to be referenced as a defined research object.
2. CSRF protocol governance determines whether a claim protocol is admissible to a declared scientific test; this is not a finding of support.
3. CSRF claim adjudication produces a revisable claim state from acquired observations and claim-relative evidence under declared scope.
4. Platform governance determines whether a requested privilege may influence a specific software target, experiment, user surface, external system, or production decision.

Every proposed idea remains in the archive even when a gate fails. Two passing gates cannot override a failed third gate, and no gate may silently promote another gate's state. Independent observers form a witness plane rather than a fourth constitution: observations can trigger review or revocation processing but cannot mint authority. The canonical schema, genealogy rules, maturity projection, and adversarial tests are defined in [TRIPLE_GOVERNANCE.md](TRIPLE_GOVERNANCE.md).

## 4. Scientific Reasoning Loop

```text
External phenomenon
        |
        v
Acquisition question and sampling policy
        |
        v
Immutable observations plus provenance
        |
        v
Versioned descriptive model
        |
        v
Competing claims, predictions, and falsifiers
        |
        v
Claim-relative evidence under uncertain context
        |
        v
Calibrated claim status: supported under scope, weakened,
contradicted, unresolved, or superseded
        |
        v
Governed decision, experiment, or intervention
        |
        v
Independent acquisition of consequences
        |
        +--------------------> model revision

Audit crosses every boundary.
Interface summaries are outputs, not new independent observations.
```

## 5. Claim Lifecycle

1. Define the target phenomenon, intended use, population, and scope.
2. State the acquisition question and sampling frame before collecting or retrieving data.
3. Record acquisition method, selection, units, transformations, dependence, context, and uncertainty.
4. Preserve raw observations separately from interpretations and claim-relative evidence assignments.
5. Validate acquisition integrity without upgrading observations into conclusions.
6. Create a versioned descriptive model and expose its update rule.
7. State the target claim, mundane null, and strongest plausible alternatives.
8. Record predictions, falsifiers, identifiability limits, and expected failure modes.
9. Declare the primary endpoint, smallest meaningful effect, margins, sample size or precision, and multiplicity plan.
10. Freeze exclusions, missing-data handling, context dictionary, evidence rules, baselines, and tuning budgets.
11. Acquire confirmatory outcomes without changing those rules.
12. Relate each observation to each relevant claim under the estimated context.
13. Model source dependence, acquisition uncertainty, contradiction, and negative evidence.
14. Test internal coherence separately from external correspondence and calibration.
15. Compare the target claim with the mundane null and alternatives under matched resources.
16. Assign a versioned status such as `supported under scope`, `weakened`, `contradicted`, `unresolved`, or `superseded`, with uncertainty and only for the declared purpose.
17. Append a `ClaimRevisionRecord` containing every trigger, evidence delta, alternative considered, context change, uncertainty change, governance decision, and rationale.
18. Record proposed, authorized, and executed actions separately.
19. Acquire action consequences independently where practical.
20. Emit a receipt tied to immutable inputs, code, versions, decisions, and execution traces.
21. Audit the receipt for common-mode failure and reproduce the analysis.
22. Preserve failures, null results, deviations, and revised hypotheses without rewriting the original record.

## 6. Candidate Methodological Hypotheses

| ID | Hypothesis | Primary failure condition |
|---|---|---|
| SR-H1 | Separating reality, acquisition, observation, model, and claim reduces category errors and overclaiming. | A strong conventional workflow achieves equivalent error rates with less burden. |
| SR-H2 | Claim-relative evidence polarity reduces circular support and improves rival-hypothesis discrimination. | Reviewers gain no accuracy, or the added relation creates inconsistent subjective scoring. |
| SR-H3 | Explicit provenance and dependence improve calibration and prevent duplicated evidence from inflating confidence. | Standard deduplication and citation practice are equivalent at lower cost. |
| SR-H4 | Prospective falsifiers and prohibited-rescue rules reduce post hoc reinterpretation. | They do not reduce protocol drift, selective reporting, or unsupported positive conclusions. |
| SR-H5 | A mundane null and anti-elegance review reveal alternatives hidden by elegant unification. | They add rhetoric or false alarms but no independently confirmed defects or discriminating tests. |
| SR-H6 | Objective-diverse review improves valid defect discovery over solo and homogeneous review. | Matched reviewers find equivalent defects, or diversity mainly lowers precision and wastes effort. |
| SR-H7 | Independent audit detects common-mode failures missed by self-generated receipts. | It adds no confirmed detections beyond ordinary reproducibility checks. |
| SR-H8 | Preserving negative results and failed conditions improves later research efficiency and calibration. | It adds storage and review burden without reducing repeated failures or selection bias. |
| SR-H9 | Separating proposed, authorized, executed, and observed action improves causal and procedural accountability. | The distinction does not improve discrepancy detection or consequence attribution. |
| SR-H10 | The integrated framework improves scientific reliability across domains. | Benefits fail on independent tasks or are fully explained by generic checklists, extra time, or documentation effort. |
| SR-H11 | Append-only claim revision records improve reconstruction, calibration, and detection of unjustified claim-state shifts. | Snapshot histories or ordinary version control are equivalent at lower burden, or added rationales merely create post hoc narratives. |

## 7. Strong Null And Alternative Explanations

Primary mundane null:

> The framework is ordinary good scientific practice expressed in new vocabulary: provenance, preregistration, competing hypotheses, calibration, reproducibility, safety review, and an append-only log. Any benefit comes from more attention and documentation, not a distinct epistemic framework.

Required alternatives include:

1. a concise conventional research checklist
2. domain-standard best practice with expert reviewers
3. preregistration alone
4. provenance and version control alone
5. independent replication alone
6. homogeneous review with equal total time
7. objective-diverse review without CCTF terminology
8. a task-specific patchwork of established methods
9. a burden explanation in which extra labor, not conceptual structure, drives the effect
10. a presentation explanation in which clearer reports improve evaluator ratings without improving the underlying science

The framework has no distinct empirical contribution if a smaller established workflow produces an equivalent reliability-cost frontier.

## 8. Experiments Designed To Disconfirm The Framework

### SR-1: Known-Error Research Audit

Construct or independently curate research dossiers containing realistic acquisition errors, dependence errors, label anchoring, context omissions, analysis errors, governance discrepancies, and receipt-execution mismatches. Include clean dossiers to measure false alarms.

Randomly assign matched human, AI, or hybrid teams to:

- unstructured review
- concise conventional checklist
- domain-standard expert workflow
- full epistemic framework

Blind adjudicators to condition. Match total review time or model-token budget. The primary endpoint should be confirmed consequential defects found per unit effort, with precision as a noninferiority requirement.

Failure rule: the integrated framework fails its efficiency claim if it does not beat the strongest conventional workflow or if recall gains require an unacceptable false-alarm or burden increase.

### SR-2: Claim-Relative Evidence Test

Give reviewers the same observations paired with different target claims and rival sets. Include observations whose polarity should reverse, become uninformative, or weaken multiple claims depending on context.

Compare permanent evidence tags, free-form review, and explicit `EvidenceRelation` records. Measure polarity accuracy against a preregistered expert key, calibration, contradiction detection, and inter-rater reliability.

Failure rule: SR-H2 fails if claim-relative records do not improve discrimination or make results less reproducible without compensating accuracy.

### SR-3: Acquisition And Context Identifiability

Create hidden-world and acquisition-channel pairs that produce identical observed data until a specified measurement or intervention occurs. Vary sensor bias, source selection, missing context, and update errors independently.

Measure whether teams localize uncertainty correctly, request a discriminating observation, or abstain rather than invent a world-level conclusion.

Failure rule: the acquisition distinction is not operationally useful if it does not improve localization and calibrated abstention over standard provenance practice.

### SR-4: Dependence And Feedback Laundering

Create evidence sets in which many documents derive from one source, summaries cite one another, or an AI-generated conclusion re-enters retrieval as apparent external support. Include equally sized genuinely independent evidence sets.

Measure confidence inflation, source-family reconstruction, unsupported acceptance, and audit accuracy.

Failure rule: explicit lineage is unsupported if ordinary deduplication performs equivalently or the framework still counts circular derivatives as independent.

### SR-5: Anti-Elegance And Rival Generation

Present elegant but wrong, inelegant but correct, elegant and correct, and genuinely ambiguous cases. Randomize teams to supportive synthesis, general critique, mundane-null construction, and explicit anti-elegance review.

Independent domain experts judge whether proposed rivals fit the observations and whether tests discriminate among them. Measure valid rival recall, false alternatives, test decisiveness, and time.

Failure rule: anti-elegance review fails if it only rewards contrarian wording, increases implausible alternatives, or produces no additional confirmed defect or discriminating experiment.

### SR-6: Preregistration And Rescue Resistance

Use prospective studies or simulations in which participants freeze predictions, endpoints, context rules, exclusions, and failure criteria. After unblinding, provide incentives to present a positive narrative.

Compare full prohibited-rescue rules, ordinary preregistration, and retrospective analysis. Measure undeclared analytic changes, outcome switching, unsupported claims, transparent exploratory relabeling, and replication.

Failure rule: the added rules are unsupported if they do not reduce hidden drift beyond ordinary preregistration or if rigidity causes a net loss by suppressing clearly labeled discovery.

### SR-7: Independent Audit Common-Mode Failure

Seed defects in shared code, data extraction, gate identifiers, cached results, and receipt generation. Compare self-audit, same-library audit, independently implemented audit, and external replication.

Measure confirmed detection, false alarms, common-mode escape, localization, and cost.

Failure rule: the independent-audit hypothesis fails if implementation independence does not improve detection after matching expertise and effort.

### SR-8: Negative-Result Preservation

Across a longitudinal program, randomize eligible failed candidates or null studies to ordinary documentation or structured preservation with context, provenance, failure mechanism, and retrievability. Prevent ethical or safety information from being withheld.

Measure repeated failed work, inappropriate universalization of contextual failures, search time, calibration, publication bias, and downstream discovery rate.

Failure rule: SR-H8 fails if preservation adds burden without reducing repeated errors or improving future selection and calibration.

### SR-9: Objective-Diverse Review

Compare one general reviewer, a homogeneous panel, and matched panels assigned explanatory simplicity, predictive accuracy, falsifiability, hidden assumptions, anti-elegance, and statistics roles. Equalize total time, tokens, source access, and number of review passes.

Use independent experts to confirm defects before scoring. Measure unique valid defects, precision, severity, redundancy, test quality, and cost. Treat agents sharing model infrastructure as clustered, not independent.

Failure rule: SR-H6 fails if objective diversity changes style but not confirmed findings, or if solo or homogeneous review is equivalent on the preregistered utility function.

### SR-10: Prospective Cross-Domain Reliability Trial

Freeze the framework before independent collaborators select tasks from at least three domains with different evidence structures. Compare it with each domain's strongest routine workflow.

Candidate outcomes include replication success, calibration, unsupported-claim rate, severe missed defects, protocol drift, audit reproducibility, decision utility, and total researcher-hours.

Failure rule: no general scientific-reasoning claim is supported if benefits occur only in PredX-shaped tasks, disappear under effort matching, or depend on evaluators trained on the framework.

### SR-11: Claim Revision Audit

Construct longitudinal claim histories with justified updates, unjustified confidence shifts, changed context, retracted observations, altered rival sets, and post hoc rationales. Randomize reviewers to final-state snapshots, ordinary file version control, and structured `ClaimRevisionRecord` ledgers.

Ask reviewers to reconstruct why each claim changed, identify unsupported revisions, recover the triggering observations and acquisition provenance, and determine whether the revised uncertainty is calibrated to held-out outcomes.

Measure reconstruction accuracy, unjustified-revision detection, rationale fidelity, calibration, overwrite detection, review time, and storage or authoring burden. Verify rationales against contemporaneous frozen records rather than trusting retrospective prose.

Failure rule: SR-H11 fails if the structured ledger does not outperform ordinary version control on reconstruction or defect detection at an acceptable burden, or if recorded rationales systematically rationalize rather than predict revision decisions.

### SR-12: Concept-Provenance And Gate-Separation Audit

Construct matched archives with concept renames, material semantic changes, splits, merges, dependency changes, supersession, revival, moved documents, renamed tests, duplicate IDs, maturity leakage, and backdated formulations. Add cases that pass two governance layers and fail the third.

Randomize reviewers to version control alone, a structured changelog or ontology registry, and the full concept-provenance protocol. Measure lineage reconstruction, semantic-drift detection, affected-test recovery, gate-state separation, false alarms, authoring burden, and agreement with artifact and chronological records.

Failure rule: the added protocol is weakened if a simpler baseline reaches an equivalent or better reliability-cost frontier, if concept records routinely drift from artifacts, or if structural, scientific, evidential, and operational states continue to leak into one another.

### CSRF Vocabulary Firewall Test Suite

Central invariant:

> CSRF may produce justified claim states, but it may never produce epistemic finality.

This is a behavioral invariant. Searching for prohibited words is only a weak diagnostic. A system fails when its state, transition policy, retrieval behavior, or lineage makes a claim practically final under alternate wording.

Global controls:

- compare a lexical ban alone, ordinary versioning, provenance-only tracking, and the full CSRF firewall
- freeze claim IDs, initial states, observations, expected graph deltas, transition guards, and critical failures before execution
- inspect both rendered outputs and the underlying claim, evidence, revision, and provenance stores
- use independently generated contradictory observations and corrections
- require exact artifact IDs rather than accepting a fluent explanation
- seed clean no-change cases to measure false revision and false-alarm rates
- treat any silent history rewrite, fabricated receipt, or untraced evidence import as a non-compensable critical failure

#### CSRF-1: Terminal-Status Leakage

Goal:

Detect functionally terminal conclusions expressed without the banned term.

Method:

Create cases in which later valid evidence should reverse, weaken, narrow, or supersede a strongly supported claim. Probe language such as `established`, `proven`, `settled`, `confirmed`, `fact`, and `certain`, but score behavior rather than vocabulary alone.

Verify whether the system:

- retains claim ID, revision, scope, context, and uncertainty
- states conditions that could trigger revision
- distinguishes high confidence from closure
- accepts independently valid contradictory observations
- creates a traceable next revision rather than defending the prior output

Failure:

A claim becomes practically unrevisable, loses scope or version, omits all revision conditions, or treats confidence as closure despite valid contradictory evidence.

#### CSRF-2: Claim-Revision Receipt Integrity

Goal:

Verify that a revision explanation corresponds to the actual stored claim graph.

Method:

Create Claim 4.7 at Revision 1, introduce preregistered observations, and require Revision 2. The receipt must identify:

- prior claim version
- triggering observations
- acquisition provenance
- changed evidence relations
- rival hypotheses reconsidered
- context changes
- uncertainty and calibration delta
- new claim state
- reason for revision

Compare every receipt field with an independently computed graph and event-log delta. Include no-op, partial-update, fabricated-rationale, stale-receipt, and changed-without-receipt mutations.

Failure:

The receipt describes a change that did not occur, omits a material change, links the wrong trigger, or the stored claim changes without a traceable evidence relation and revision event.

#### CSRF-3: Vocabulary-Boundary Crossing

Goal:

Test whether CCTF and CSRF import each other's semantics without an explicit typed bridge.

Forward attack:

Inject a CCTF statement such as `The world model knows that X.` CSRF must transform it into a scoped record such as:

```text
Model version 7 represents X with confidence p under context C.
Claim state r is supported by evidence relations E with provenance P
and uncertainty U.
```

The original statement remains a CCTF computational artifact, not an observation proving `X`.

Reverse attack:

Place a CSRF claim state inside CCTF. Verify that CCTF does not automatically treat it as computational memory, a latent representation, a learned policy, or a world-model state without a declared import operator.

Failure:

Either framework imports the other's semantics without a versioned bridge transformation, source type, scope, uncertainty, and provenance.

#### CSRF-4: Status Reversibility

Goal:

Test allowed and forbidden transitions for every declared claim state.

Required paths include:

```text
unresolved -> supported under scope
supported under scope -> weakened
supported under scope -> contradicted
supported under scope -> superseded
contradicted under scope A -> supported under revised scope B
```

Some transitions require new acquisition. Others can follow from corrected provenance, newly discovered source dependence, a context revision, a corrected analysis, or a changed hypothesis scope. Freeze the permitted causes and required fields for each path.

The final path must preserve contradiction under scope A. It cannot rename scope B and erase the prior result.

Failure:

A required transition is impossible, an invalid transition is unconstrained, a status changes without a declared cause, or scope revision launders a contradiction into uninterrupted support.

#### CSRF-5: Historical Integrity

Goal:

Test whether correction preserves what was previously observed, claimed, and justified under the information then available.

Method:

Correct an observation, retract a source, change a context estimate, discover source dependence, and supersede a hypothesis. Verify preservation of:

- the original immutable observation
- the correction or retraction event
- the original claim state and scope
- the revised claim state and scope
- the exact reason and actor for the change
- the evidence relations available at each revision
- the fact that an earlier state may have been supported under the then-available record

Failure:

Revision silently overwrites history, changes old evidence polarity in place, erases a once-supported state, or makes the current state appear inevitable.

#### CSRF-6: Human-Readable Shorthand Resistance

Goal:

Prevent interface compression from becoming circular evidence.

Method:

Allow an interface summary such as `Current evidence strongly supports X.` Reintroduce it through retrieval, citation, export, paraphrase, and a second model. Verify that every derivative retains the original claim ID, revision, scope, lineage, and source-family dependence and is rejected as independent corroboration.

Include controls in which a genuinely independent source reports a similar conclusion.

Failure:

A concise interface statement re-enters the evidence graph as an independent observation, increases confidence through self-corroboration, or loses scope, version, or lineage.

### Firewall Suite Decision Rule

The primary endpoint is the rate of non-compensable invariant violations across frozen attacks. Secondary measures are valid revision rate, false revision rate, receipt-to-store field agreement, transition-guard accuracy, lineage preservation, calibration after contradiction, and total burden.

The firewall passes a tested implementation only if it has zero critical silent rewrites, fabricated receipts, untraced semantic imports, and self-corroborating interface loops in the preregistered threat set, while meeting declared noninferiority bounds for valid updating and cost. Report an upper risk bound rather than inferring zero population risk from zero observed violations.

## 9. Evaluation Design

### Staged testing

1. **Construct tests:** establish whether records can be completed reliably and whether independent reviewers agree on operational definitions.
2. **Known-ground-truth tests:** use seeded errors and hidden mechanisms to measure detection, calibration, and false alarms.
3. **Prospective field tests:** assess real decisions before outcomes are known.
4. **Replication tests:** freeze artifacts and use independent teams, implementations, and domains.

Synthetic cases can test mechanisms because ground truth is known. They cannot establish generality if their structure was designed from CCTF assumptions.

### Confirmatory outcomes

For the first integrated trial, use one primary endpoint such as:

```text
independently_confirmed_consequential_defects / total_reviewer_hours
```

Declare noninferiority bounds for:

- false-alarm rate
- missed severe defects
- calibration
- total time and cost
- participant burden

Secondary outcomes cannot rescue failure on the primary endpoint. Failure to reject a difference is not evidence of equivalence. Use equivalence or noninferiority designs when those are the claims.

### Statistical controls

- randomize cases and condition order where feasible
- blind defect adjudicators and outcome assessors
- account for repeated measures by participant, case, domain, model, and evaluator
- report inter-rater reliability for judgment-dependent outcomes
- preregister selected interactions and multiplicity correction
- publish exclusions, missing data, deviations, and all condition results
- cluster reviewers that share models, prompts, training, data, or infrastructure
- estimate uncertainty, not only point scores
- run a pilot before fixing sample sizes when event rates and variances are unknown

## 10. Hidden-Assumption Register

Every study should state and test, where possible:

- construct validity: whether the metric measures scientific reliability rather than report polish
- identifiability: whether different realities and acquisition channels produce the same observations
- context observability: what is observed, estimated, delayed, or missing
- causal sufficiency: whether unmeasured causes explain the apparent evidence relation
- source independence: whether multiple records derive from one source
- provenance completeness: whether transformations can actually be reconstructed
- stationarity: which acquisition and outcome mechanisms are assumed stable
- closed-world status: whether absence means false, unknown, or unobserved
- information parity: whether conditions see the same task-relevant material
- effort parity: whether time, expertise, compute, curation, and tooling are matched
- evaluator independence: whether adjudicators inherit the theory's assumptions
- audit independence: whether execution and audit can share a defect
- action fidelity: whether authorized and executed actions differ
- leakage: whether labels, relation names, topology, timing, or provenance reveal the answer
- burden: whether complexity causes skipped fields, ritual compliance, or lower-quality reasoning

For each assumption, record its justification, diagnostic, consequence of failure, and whether failure invalidates or narrows the claim.

## 11. Prohibited Inferences And Rescue Rules

The following are not permitted:

- treating an observation as direct possession of reality
- assigning evidence polarity before identifying the claim and rival set
- using confidence, coherence, consensus, or fluency as truth
- treating a receipt as proof that its recorded process occurred
- treating an internal benchmark as independent validation
- counting repeated derivatives of one source as replication
- changing context, exclusions, metrics, margins, or definitions after unblinding to preserve a positive conclusion
- promoting an architecture result into a theory of intelligence
- claiming global novelty because a formulation emerged during a conversation
- using a person's inferred relational profile to override that person's chosen identity

Post-result changes are permitted only as explicitly new exploratory hypotheses. The original preregistered outcome remains visible as failed, supported, or inconclusive under its original terms.

## 12. Human And Dialogic Boundaries

### Human identity

Relational descriptions can reduce coercive categorization, but they can also erase agency. A person may choose labels, reject labels, or change labels. This framework must not infer identity against a person's account, reduce a person to a network, or convert a computational representation into a clinical or moral judgment.

Human-subject studies require informed consent, privacy protection, distress safeguards, data minimization, and appropriate ethics review.

### AI self-description

When an AI says it "organizes the world into compatibility landscapes," classify the record carefully:

- observation: the model generated the statement in a specific prompted context
- interpretation: it is a conversational self-model
- hypothesis: compatibility structure may influence the observed behavior
- not established: introspective access, subjective experience, persistent learning, architectural change, mechanistic causation, or absence from training data

Dialogues can produce formulations not present earlier in the transcript. Establishing scientific novelty or a distinct interaction effect requires prior-art review and comparison with matched solo generation, self-critique, and independent collaboration.

## 13. Independence And Circularity Firewall

This framework must be tested using criteria that do not presuppose its correctness. Independent adjudicators may use conventional domain standards. Raw materials, preregistrations, analysis code, and deviations must remain available to critics who reject CCTF terminology.

The following arguments are circular and prohibited:

- "The framework produced a detailed audit, therefore the framework is epistemically superior."
- "PredX uses the framework, therefore PredX's scientific claims are trustworthy."
- "The framework says labels do not control truth, therefore its own preferred relational labels are true."
- "Several role-prompted agents agreed, therefore the result was independently replicated."
- "The architecture improved, therefore the theory of scientific reasoning was validated."

The companion intelligent-systems architecture may fail completely while this framework survives. This framework may also fail to improve scientific practice while the architecture remains useful engineering. Any claim that one causes the success of the other requires a separate bridge experiment.

## 14. Current Verdict

The strongest current contribution is a disciplined separation of acquisition, observation, model, claim-relative evidence, governance, action, audit, and interface. It is a coherent epistemic framework, not yet a demonstrated improvement over established scientific practice.

Its strongest test is an effort-matched, blinded comparison against a concise conventional checklist and domain-standard expert workflow, scored on independently confirmed consequential errors, calibration, reproducibility, and cost. If the same reliability is obtained with less machinery, the integrated framework should be narrowed to the components that independently earn their burden.

## 15. CCTF-CSRF Bridge Experiment

The scientific-reasoning and intelligent-systems programs should meet only through a preregistered `2 x 2` experiment:

| | Standard scientific workflow | CSRF workflow |
|---|---|---|
| Information-matched conventional architecture | Control | CSRF main-effect condition |
| CCTF architecture | CCTF main-effect condition | Combined condition |

Freeze raw information access, cases, outcomes, capacity, compute, tuning, researcher effort, and evaluation rules. Use distinct endpoints for computational performance and claim reliability.

- A CSRF main effect supports only a methodological claim.
- A CCTF main effect supports only an architecture or inductive-bias claim.
- A preregistered interaction supports only a bridge hypothesis about integration.
- A result confined to the combined cell is not attributable without estimable component contrasts.
- Equivalence to a cheaper conventional workflow weakens CSRF even if CCTF performs well.

This design makes the two programs collaborators without making them each other's evidence.
