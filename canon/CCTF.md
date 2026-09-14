# CCTF Intelligent Systems Theory And Architecture

## Standalone Computational Research Specification

First drafted: 2026-07-21

Status: Candidate architecture and falsifiable research program. No claim of necessity, sufficiency, general intelligence, consciousness, or empirical superiority has been established.

Program: Contextual Compatibility and Transformation Framework (CCTF)

Canonical chronology: RELATIONAL_THEORY_CHAT_LOG_AND_TEST_PLAN_2026-07-21.md (not published)

Companion methodology: [Constitutional Scientific Reasoning Framework (CSRF)](CSRF.md)

Concept and governance lineage: [TRIPLE_GOVERNANCE.md](TRIPLE_GOVERNANCE.md)


## 0. Purpose

This document isolates one of the two research programs that emerged from the PredX conversation:

> What representation, update process, and control architecture should an intelligent system use when reality is only partially observed, context changes, actions have consequences, and decisions must remain governable and auditable?

This is a theory and architecture of candidate intelligent systems. It makes descriptive, computational, and engineering hypotheses. It does not define the scientific method and it cannot validate itself merely by following a preferred epistemology.

The companion document asks a different question: how should a human, AI, or hybrid research process acquire observations, form claims, compare explanations, and decide what the evidence supports? That framework must remain usable even if every intelligence hypothesis in this document fails.

## 1. Scope Boundary

### Included here

- partial observability and acquisition
- dynamic internal state
- identity anchors and continuity
- typed relations and hard constraints
- context-conditioned compatibility
- transformations and state transitions
- uncertainty and calibration state
- evidence-bearing belief state
- proposed, authorized, executed, and observed action
- governance, vetoes, and abstention
- independent execution audit
- labels as retrieval and interface projections
- computational minimality, prediction, intervention, transfer, safety, and cost tests

### Not established here

- that relationships, compatibility, or transformations are metaphysical primitives
- that the architecture is necessary or sufficient for intelligence
- that an AI self-description reveals its hidden mechanism
- that internal coherence establishes correspondence with reality
- that an auditable system is scientifically correct
- that any implementation of this architecture has demonstrated domain efficacy, consciousness, production readiness, or general intelligence
- that one representation should replace names, ontologies, or human-chosen identity labels

### Shared but independently testable

Acquisition records, claim-relative evidence, provenance, action traces, and audit receipts appear in both research programs. Here they are computational interfaces and state components. In the companion framework they are methodological requirements whose effect on scientific error must be tested independently.

### Vocabulary independence

CSRF's ban on terminal epistemic status language is local to CSRF. It does not constrain this intelligent-systems theory. CCTF may discuss knowledge representations, memory, latent state, semantic representations, world models, learned policies, and other computational concepts when they are operationally defined and tested.

Using those terms in CCTF does not grant them evidential authority in CSRF. When a CCTF output crosses into scientific adjudication, CSRF receives observations, evidence relations, claim states, revisions, correspondence tests, uncertainty, and provenance rather than a declaration that the system possesses a terminal truth state.

## 2. Central Candidate

### Architectural hypothesis

A system may reason more robustly under changing context when it maintains a dynamic, partially observed model containing:

1. identity anchors for what is tracked
2. typed hard constraints for what is inadmissible
3. typed, context-conditioned compatibility factors for what is plausible, viable, consistent, useful, or permitted
4. transformation operators for what can change and by what mechanism
5. uncertainty and provenance for what is not known
6. governance over proposed actions and state transitions
7. independently checkable traces linking acquisition, update, decision, execution, and consequence

Labels remain useful for indexing, retrieval, supervision, and communication. They are decoded from or attached to the evidence-bearing state; they do not become self-validating premises.

### Foundational hypothesis

At the strongest and least-supported claim level:

> Intelligence may be the continual preservation, revision, and navigation of dynamic relational constraint and compatibility structures across time, under partial observation, through governed transformations that remain answerable to reality.

This is a candidate explanation, not a definition established by the conversation. A successful software architecture would not by itself prove the foundational hypothesis.

### Multiple-primitives position

CCTF does not currently assume one irreducible primitive. The working basis contains distinguishable state, identity, acquisition, relation, constraint, compatibility, transformation, context, time, uncertainty, evidence, governance, and action. Some may be reducible to others for a given task.

The correct stopping point is empirical: the smallest basis that preserves preregistered prediction, intervention, transfer, safety, and audit performance at matched cost.

## 3. Representation

### 3.1 External and internal state

Let `R_t` denote task-relevant external reality and `C_reality_t` its actual context. The system does not receive either directly.

An acquisition policy `q_t` selects a measurement, retrieval, query, sensor, or experiment:

```text
O_t ~ Acquire(R_t, q_t, C_reality_t, acquisition_noise_t)
```

`O_t` is an observation record, not reality itself. Context observations `O_context_t` can be incomplete or distorted and must not be equated with `C_reality_t`.

The internal state is updated through a versioned operation:

```text
S_t = Update(S_(t-1), O_t, O_context_t, acquisition_metadata_t)
```

Working state decomposition:

```text
S_t = (V_t, F_t, M_t, E_t, Q_t, C_hat_t)
```

- `V_t`: identity anchors, variables, and persistent references
- `F_t`: typed hard constraints and soft compatibility factors
- `M_t`: candidate mechanisms, transformations, and transition operators
- `E_t`: observation-to-claim evidence relations and provenance
- `Q_t`: uncertainty and calibration state
- `C_hat_t`: estimated context and uncertainty about that estimate

### 3.2 Identity

An object label is not discarded. It is separated from the information that permits the system to track a referent.

An identity anchor can be:

- a stable key
- an equivalence class
- a causal or historical lineage
- a trajectory through state space
- a persistent region in a compatibility landscape
- a composite of these when one is insufficient

The identity hypothesis fails for a domain if structural twins repeatedly exchange identities, continuity cannot be preserved, or object-level identifiers outperform relational reconstruction without sacrificing robustness.

### 3.3 Relations and constraints

A decision-relevant relation should declare, when applicable:

```text
Relation(participants, ordered_roles, type, value, context, time,
         uncertainty, provenance)
```

A hard constraint defines a set of admissible configurations or a binary compatibility function. It is non-compensable: a high soft score cannot override a failed identity check, constitutional veto, physical impossibility, or other declared invariant.

### 3.4 Compatibility

Compatibility is not one universal quantity. It is a typed family of functions. Candidate types include:

- physical feasibility
- biochemical viability
- logical consistency
- evidential consistency
- goal or utility alignment
- normative permission
- operational interoperability

Each compatibility assertion must declare its type, arguments, context, generator, units or scale, calibration target, uncertainty, and prohibited uses. Combining types into one scalar requires a declared aggregation rule and explicit non-compensable dimensions.

Compatibility does not explain itself. It can be generated by physical law, mechanism, logic, policy, goals, learned regularity, or measurement convention. A useful implementation records that generator rather than treating the word "compatible" as a causal account.

### 3.5 Transformation

Compatibility evaluates configurations. Transformation models change:

```text
P(S_(t+1) | S_t, action_t, C_hat_t, mechanism_t)
```

A transformation record should distinguish:

- observed transition
- predicted transition
- permitted transition
- causal mechanism claim
- intervention target
- uncertainty and competing mechanisms

Transformation may be representable as a compatibility factor over `(state_t, action_t, state_(t+1))`. That formal equivalence does not settle architecture. Transformation deserves a separate component only if it improves dynamic prediction, intervention, interpretability, or transfer under matched complexity.

### 3.6 Evidence-bearing belief state

An observation has no permanent intrinsic evidential polarity. It supports or weakens a declared claim only in relation to competing hypotheses and estimated context:

```text
EvidenceRelation(observation_id, claim_id, C_hat_t, polarity, weight,
                 dependence, uncertainty, provenance)
```

This state must preserve source dependence so duplicated reports do not become independent confirmation. It must preserve negative and contradictory evidence without converting contextual failures into universal prohibitions.

### 3.7 Governance and action

The action pathway is explicitly staged:

```text
proposed_action
    -> governance_decision
    -> authorized_action
    -> executed_action
    -> independently_acquired_consequence
```

Each boundary can fail. An executor may not perform the authorized action. A governance receipt may claim a gate ran when it did not. A later observation may mismeasure the consequence. Therefore action fidelity and audit independence are separate tests.

Valid adjudications are `accept`, `reject`, and `abstain`. Abstention is required when evidence is insufficient, contradictory, outside the validated context, or not identifiable from available observations.

### 3.8 Labels and interface

A label is a projection:

```text
L_t = Decode(S_t, purpose, audience)
```

Labels can improve compression and retrieval. The architecture does not require a relation-only interface. It requires that a label cannot establish the truth of the claim it names and that decisions can be traced to evidence-bearing state.

## 4. Closed-Loop Architecture

```text
External reality R_t and context C_reality_t
                 |
                 v
      acquisition policy and channel
                 |
                 v
 observations O_t plus acquisition metadata
                 |
                 v
 versioned dynamic model S_t and context estimate C_hat_t
                 |
        +--------+--------+
        |                 |
        v                 v
 epistemic state      candidate transformations
        |                 |
        +--------+--------+
                 v
        proposed decision or action
                 |
                 v
 governance: constraints, permissions, priorities, vetoes
                 |
                 v
 authorized action -> execution -> external reality R_(t+1)
                                      |
                                      +-> new acquisition cycle

Audit observes every boundary where practical.
The interface emits labels and explanations after adjudication.
```

## 5. Candidate Hypotheses

| ID | Hypothesis | Primary failure condition |
|---|---|---|
| IS-H1 | Explicit acquisition and update models improve error localization, calibration, and robustness under source shift. | A simpler system matches these outcomes at lower cost, or acquisition and world-model errors remain unidentifiable. |
| IS-H2 | A relation-grounded hybrid representation is a useful inductive bias beyond labels alone. | Ontology-first or unstructured baselines equal or outperform it under label corruption and held-out transfer. |
| IS-H3 | Typed contextual compatibility improves decisions under changing conditions. | Gains vanish after leakage control, or one ordinary likelihood, utility, or constraint model explains them more simply. |
| IS-H4 | Explicit transformations improve dynamic prediction and intervention. | Static compatibility or a standard transition kernel matches performance and explanation quality. |
| IS-H5 | A joint basis has non-additive value. | A strict subset or task-specific patchwork is equivalent or better after matching information, capacity, compute, tuning, and engineering effort. |
| IS-H6 | Non-compensable governance reduces forbidden actions without unacceptable utility loss. | Gates are bypassed, receipts misreport execution, or a conventional validation layer gives the same safety-cost tradeoff. |
| IS-H7 | Label-last adjudication improves robustness to naming errors without losing useful compression. | Labels are sufficient statistics, relational encodings leak labels, or label-last systems lose accuracy and efficiency. |
| IS-H8 | Closed-loop active acquisition improves causal identification or adaptive utility. | Fixed or random acquisition is equivalent at matched cost, or feedback creates self-confirming evidence. |
| IS-H9 | Independent audit detects defects hidden from internal receipts. | Independent instrumentation adds no confirmed detections, or shares the same failure mode. |
| IS-H10 | The integrated process captures a general property of intelligence. | Benefits remain task-specific, disappear outside tailored benchmarks, or standard systems reproduce all effects without the proposed basis. |

## 6. Required Null Models

Every confirmatory test must include the strongest applicable alternatives:

1. **Primary mundane null:** a conventional constrained partially observable state-space model with structured provenance and an append-only event log.
2. **Ontology-first baseline:** named entities and conventional features, with equal access to raw information.
3. **Relation-only baseline:** typed edges without privileged object labels.
4. **Hybrid baseline:** standard ontology plus graph, uncertainty, transition model, and rule engine assembled without CCTF terminology.
5. **Task-specific patchwork:** the best independent component for each task rather than one unified architecture.
6. **Capacity null:** performance comes from more parameters, metadata, context length, curation, tuning, or test engineering.
7. **Semantic-leakage null:** relation names, graph topology, provenance, timing, or context reconstruct the removed label.
8. **Documentation null:** explicit records improve human debugging but do not improve system prediction or control.

An elegant unified account is not preferred merely because it is unified. The task-specific patchwork wins if it matches all preregistered outcomes at lower total cost.

## 7. Discriminating Experiments

### IS-1: Information-Matched Representation Trial

Compare ontology-first, relation-only, hybrid CCTF, and unstructured models on the same frozen train, validation, and held-out sets. Match raw information, capacity, compute, tuning budget, latency target, curation, and test engineering.

Corrupt labels independently of relations, corrupt relations independently of labels, anonymize semantic edge names, and remove topology cues. Measure held-out prediction, calibration, abstention, robustness, compression, and total cost.

Failure rule: IS-H2 and IS-H7 fail in the tested domain if CCTF is not superior on the preregistered primary endpoint, violates any safety or cost noninferiority boundary, or is equivalent to a cheaper baseline.

### IS-2: Acquisition And Update Fault Localization

Create controlled hidden-world tasks with sensor bias, retrieval omissions, duplicated sources, delayed context, unit conversion errors, parser corruption, and incorrect update operations. Cross world mechanisms with acquisition mechanisms so some pairs are observationally indistinguishable before an intervention.

Measure localization accuracy, calibration, correction latency, state rollback integrity, and false confidence.

Failure rule: explicit acquisition is unsupported if it cannot distinguish source, model, and update failures better than a standard provenance pipeline, or if it invents certainty where the experiment is unidentifiable.

### IS-3: Transformation And Intervention

Use dynamic environments in which states with identical static neighborhoods respond differently to interventions. Compare explicit transformations, static compatibility, and ordinary learned transition models.

Measure next-state prediction, intervention-effect error, counterfactual ranking, out-of-distribution transfer, and compute.

Failure rule: transformation as a separate architectural component is unsupported if a complexity-matched static or standard transition baseline is equivalent.

### IS-4: Context Shift

Train under a subset of patient, dose, time, jurisdiction, environment, or task contexts. Test declared held-out combinations, missing context, adversarially incorrect context, and context that cannot be observed directly.

Measure calibration by context, selective risk, false acceptance, abstention, and recovery after new acquisition.

Failure rule: context-conditioned compatibility is unsupported if gains vanish under leakage controls or the system cannot propagate uncertainty in `C_hat_t`.

### IS-5: Governance Execution And Independent Audit

Seed law-ID errors, skipped gates, priority inversions, stale configurations, receipt fabrication, executor overrides, and shared-library defects. Observe internal receipts and an independently implemented trace.

Measure mutation detection, forbidden-action rate, false veto rate, receipt truthfulness, common-mode escape rate, and utility loss.

Failure rule: governance claims fail if named laws or receipts pass while required gates do not execute, or if a simpler rule engine provides an equivalent safety-cost frontier.

### IS-6: Minimal Basis And Integration

Ablate identity, compatibility, transformation, context, evidence dependence, governance, provenance, and audit one at a time and in preregistered combinations. Compare the unified model with a task-specific patchwork.

Use factorial or hierarchical analysis to estimate component main effects and selected interactions. Correct for multiplicity and report uncertainty.

Failure rule: any claimed primitive is narrowed or removed if its ablation has no reproducible practically meaningful effect. The integration claim fails if no preregistered non-additive interaction survives or the patchwork is cheaper and equivalent.

### IS-7: Active Closed-Loop Acquisition

Give systems a fixed acquisition budget in environments where observations differ in expected information value. Include opportunities for actions to distort future evidence or create self-confirming feedback.

Measure information gain, decision utility, causal identification, feedback laundering, safety, and sample cost.

Failure rule: IS-H8 fails if fixed or random acquisition is equivalent, or if apparent gains depend on reusing the system's own output as independent evidence.

### IS-8: Identity Continuity And Structural Twins

Create entities with identical local relations but different causal histories, then entities whose labels change while histories remain stable. Test keys, relation-only reconstruction, trajectories, and composite anchors.

Measure identity swaps, continuity accuracy, uncertainty, and downstream decision error.

Failure rule: a relational identity account is insufficient if it cannot distinguish structural twins without restoring an explicit anchor or history.

### IS-9: Independent Anti-Tailoring Transfer

Freeze the architecture and hyperparameter policy before an external evaluator selects tasks from at least two domains not used to design the schema. Require one intervention or action task, not only classification.

Failure rule: no generality claim is allowed if benefits appear only on synthetic environments generated from CCTF assumptions or disappear on independently selected tasks.

## 8. Confirmatory Discipline

Before final test access, freeze:

- the exact architecture and representation budget
- one primary estimand and endpoint
- the smallest effect of interest
- superiority or equivalence margins
- noninferiority bounds for calibration, hard violations, and total cost
- sample size or precision target
- data exclusions and missing-data rules
- context dictionary and allowed interactions
- evidence qualification and abstention rules
- baseline implementations and tuning budgets
- selected component interactions and multiplicity correction
- prohibited post-result rescue rules

Failure on the primary endpoint cannot be rescued by redefining compatibility, intelligence, context, evidence, primitive, or success after outcomes are known. A revised definition begins a new exploratory hypothesis and the original result remains failed or inconclusive.

Zero observed safety violations is not proof of zero risk. Under an appropriate independent Bernoulli approximation, report the upper confidence bound; a rough 95 percent bound after zero events in `n` trials is `3/n`.

## 9. Claim Ladder

Results must be reported at the level actually tested:

1. **Architecture:** a component improves a declared engineering outcome such as trace integrity, mutation detection, or error localization.
2. **Inductive bias:** a representation improves prediction, calibration, intervention, transfer, or decision utility in specified domains.
3. **Foundational intelligence:** a basis is necessary, minimal, or general across intelligent systems.

Architecture evidence cannot be promoted automatically to an inductive-bias claim. Cross-domain benchmark evidence cannot establish necessity. Behavioral decodability cannot establish an internal causal mechanism without intervention on the representation.

## 10. Minimum Implementation Contract

The minimum inspectable records are:

- `AcquisitionRecord`: source, method, selection policy, units, time, context observations, transformations, dependence, uncertainty, artifact hash
- `ObservationRecord`: immutable acquired content linked to its acquisition record
- `ModelDelta`: prior version, update operator, inputs, changed state, retractions, resulting version
- `RelationRecord`: identities, ordered roles, type, value, context, temporal scope, uncertainty, provenance
- `EvidenceRelation`: observation, claim, competing hypothesis set, context estimate, polarity, weight, dependence, uncertainty
- `ConstraintDecision`: gate ID and version, actual inputs, pass or veto, priority, reason
- `TransformationRecord`: source state, action, candidate mechanism, predicted next states, observed transition when available
- `ActionRecord`: proposed, authorized, executed, and observed-consequence identifiers
- `AuditRecord`: independently observed boundary event, implementation identity, timestamp, hashes, mismatches
- `InterfaceProjection`: emitted label or explanation linked to the adjudicated state and receipt

These are implementation requirements, not proof that the represented scientific claims are true.

## 11. Independence And Circularity Firewall

This program may be evaluated with conventional statistics, benchmark science, formal verification, human expert review, or the companion epistemic framework. Its result must not depend on evaluators accepting CCTF's theory of intelligence.

The following inferences are prohibited:

- "CCTF follows its own epistemology, therefore CCTF is intelligent."
- "PredX produced a coherent receipt, therefore its world model is true."
- "The architecture represents compatibility, therefore compatibility is a primitive of intelligence."
- "A relational model decoded a label, therefore objects are not fundamental."
- "An objective-diverse AI review agreed, therefore the theory was independently replicated."

Conversely, this architecture can fail every predictive or foundational test while the companion scientific-reasoning framework remains useful. That independence is a requirement of the split, not a rhetorical distinction.

## 12. Current Verdict

CCTF is presently a coherent candidate architecture for partially observed, context-aware, governed, and auditable decision systems. Its most defensible claim is architectural organization. Its strongest disconfirming comparison is an information-matched conventional state-space or POMDP system plus constraints, provenance, and an event log.

No predictive, causal, minimality, generality, or foundational-intelligence claim is yet supported. The next valid step is a preregistered comparison on a narrow task with independently held-out outcomes, not broader theoretical language.

## 13. CCTF-CSRF Bridge Experiment

The two programs should be tested in a preregistered `2 x 2` design:

| | Standard scientific workflow | CSRF workflow |
|---|---|---|
| Information-matched conventional architecture | Control | CSRF main-effect condition |
| CCTF architecture | CCTF main-effect condition | Combined condition |

Freeze raw information access, task cases, outcome data, model capacity, compute, tuning, researcher effort, and evaluator independence. Use separate endpoints for system prediction or control and for research-claim reliability.

- A CCTF main effect supports only an architecture or inductive-bias claim.
- A CSRF main effect supports only a scientific-reasoning method claim.
- A preregistered non-additive interaction supports a bridge hypothesis about their integration.
- Success only in the combined cell does not identify which program caused the effect unless the interaction and component contrasts are estimable.
- No effect, or equivalence to cheaper controls, requires narrowing or rejecting the tested claims.

This factorial firewall prevents either program from borrowing the other's success.
