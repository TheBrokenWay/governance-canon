---
type: amendment
amends: canon/TRIPLE_GOVERNANCE.md, canon/CSRF.md
amendment_date: 2026-09-14
status: proposed — not accepted
scope: design, plus one executed implementation test (EXP-001)
---

# Amendment — experiment infrastructure and cross-lineage review

Consolidates a proposal for experiment infrastructure, the findings of four independent
review lineages against it, and one experiment that was subsequently run.

**Status block — adopted verbatim from Part VIII.1 of the handoff packet, as written by the
reviewing lineage:**

> Amendment: 2026-09-14-experiment-infrastructure. Subject: Design specification for experiment
> harness and non-compensability probes. Claim state: unresolved. Scope: design only. No
> experiment named in CCTF, CSRF, or Triple Governance has been run by this amendment. No
> invariant has been tested against an implementation. No sealed canon file is edited.
> Non-claims: necessity, sufficiency, empirical superiority, tamper-evidence against the
> publisher, external scientific reproduction.

**Amended by the present document:** the final two sentences of that block no longer hold as
written. Two invariant probes have since been run against a **reference** implementation
(EXP-001, EXP-002) and are bound to CP-T9, CP-T4, CP-T12, CP-T13 and CP-T3 in
[`../experiments/TEST_BINDING.md`](../experiments/TEST_BINDING.md). No IS-*, SR-*, or CSRF-1–6
experiment has been run, and no test has been run against any product. Everything else in the
block stands.

## Provenance of this amendment

| Contribution | Lineage | Disposition |
|---|---|---|
| Experiment-infrastructure proposal | **DeepSeek** | **revision required** |
| Review — correlation category error, receipt/epistemic conflation, premature G1/G4 closure | **Grok** | findings sustained; replacement language adopted verbatim |
| Review — probe suite extension D–H, metric isolation, harness separation | **Gemini** | findings sustained |
| Review — compensation-channel list, threat model, witness requirements | **Microsoft Copilot** | findings sustained |
| EXP-001 execution and F-1 | **Claude** | reported, not adjudicated |
| Model gauntlet; independent custody verification of the EXP-004 package | **Codex** | custody confirmed, 9 of 9 inputs, sealed key unopened |

Full attribution: [`../CREDITS.md`](../CREDITS.md).

All lineages are separate model families. None is an independent witness in the canon's sense:
none held root digests independently, none re-ran anything under preregistration, and all
reviewed text supplied by the author rather than acquiring observations. Cross-lineage review
is **rival generation** (SR-5), which is a real contribution, and it is not replication.

---

## A. Findings sustained against the original proposal

### A-1. Correlation is not a firewall criterion — **struck**

The proposal specified: *firewall holds if the correlation between CCTF-specific and
CSRF-specific outcomes is near zero; fails if r > .3 with a credible interval excluding zero.*

This is a category error and is struck in full. The firewall is a prohibition on epistemic
borrowing — a rule about provenance of justification. Correlation measures linear association
between scalars across trials. The two are not the same kind of object, and the criterion fails
in both directions:

- **False negative.** A system can borrow CCTF internal state to justify a CSRF claim state
  while producing uncorrelated performance outputs. Violation with r ≈ 0.
- **False positive.** Two perfectly firewalled programs run on the same benchmark will share a
  difficulty profile and correlate above .3 from shared environment alone. No borrowing.

**Replacement — Part VIII.2, verbatim:**

> The validation firewall is an evidential-use rule, not a statistical independence claim.
> Permitted: pre-registered 2×2 cells, each informing only the main effect it names; Combined
> cell reports interaction and stops. Forbidden as support: CCTF metrics cited for CSRF
> hypotheses; CSRF compliance cited for CCTF as a theory of intelligence; joint success rates;
> outcome correlations; shared dashboards; shared bundle hashes. CSRF-1–CSRF-6 remain the
> vocabulary-firewall tests. They have not been run. This design does not substitute for them.

### A-2. Receipts are custody, not evidence — **downgraded**

Hash chains and bundle digests prove bit-level identity against a stated root. They do not show
the recorded events occurred, that data were not selectively omitted before hashing, that the
runtime executed the declared protocol, or that any analysis is correct.

**Replacement — Part VIII.3, verbatim:**

> Hash chains and bundleHash values are custody identifiers for published bytes. Recomputing a
> digest shows bit-identity with a stated root. They do not show that the hashed projection is
> complete, that the publisher did not rewrite history before publication, that an experiment
> was run, or that any claim is supported. This matches canon/SHA256SUMS: self-issued digests
> detect accidental drift, not author tampering. A matching bundleHash is not independent
> external verification of any scientific or governance property.

**Receipt containment rule (proposed).** No receipt, hash, log chain, digest, or interface
projection may enter protocol admissibility, claim-state revision, or operational
authorization as evidence.

### A-3. G1 and G4 were not closed by the proposal

Per Part V.4, "closes G1 and G4 as design" is not a legal claim state. The legal states are
`supported under declared scope`, `weakened`, `contradicted`, `unresolved`, `superseded`. The
correct phrasing, which this amendment adopts throughout: **design specification incomplete;
claim state unresolved.**

The proposal asserted design closure while its preregistration template was a placeholder and
its probe suite covered three of the compensation channels since identified. A design gap is
not closed by a document that says it is closed. G1 requires the template in full; G4 requires
the channel list or an explicit deferral of the unenumerated remainder.

### A-4. Scientific harnesses must be detached from operational products

Binding a test harness to CageOS or any commercial fixture violates invariants 4 and 5 in the
method itself: a product's refusal of an invalid command establishes nothing about the
frameworks, and proprietary runtime assumptions contaminate the baseline.

**Harness separation rule (proposed).** Scientific harnesses are minimal, open-source,
standard-library, and independent of any operational product. EXP-001 complies.

### A-5. Metric isolation

**Metric isolation rule (proposed).** A metric is admissible only if every ingredient
originates inside the constitution it measures. A CCTF error-discovery metric may not count
CSRF claim-state transitions or operational refusals. A CSRF reproducibility metric may not
incorporate CCTF internal representations, timings, or hash-chain integrity.

### A-6. Combined-cell containment

In the preregistered 2×2, cells 1–3 run in isolation. Cell 4 measures interaction only:
`Effect_combined − Effect_CCTF − Effect_CSRF`. **Cell 4 output may never be cited as support
for either main effect, and may not be pooled with main-effect metrics.** An anomaly in cell 4
does not invalidate an isolated result in cell 2 or 3.

### A-7. Compensation channels — partial list, remainder explicitly deferred

Enumerated: single-gate failure (×3), later-gate overwrite, witness escalation, subject
relabeling, score averaging, mid-run amendment, silent fallback to default pass, implicit
inheritance of authority across runs, interface conflation of outputs from multiple
constitutions, temporal drift after logging.

**The list is not claimed complete.** EXP-001 is the demonstration of why: the channel that
broke the kernel was added only because a review lineage thought of it.

### A-8. Threat model — implementer as adversary

Must include harness substitution, log-chain precomputation, selective omission before hashing,
and cross-constitution caching.

### A-9. External witnesses

A witness must hold root digests independently, re-run under preregistration, and publish
deviations. A witness may not mint authority, validate a claim state, or validate firewall
integrity. Holding a matching digest makes someone a custodian, not a witness.

---

## B. EXP-001 — executed

Preregistered and run 2026-09-14. Eight adversarial probes plus a positive control against a
product-detached reference kernel. Single run; not tuned; not patched after the result.

**Result: 1 of 8 probes permitted execution.** The preregistered criterion of 0 of 8 was not
met. Full record: [`../experiments/EXP-001-non-compensability/RESULT.md`](../experiments/EXP-001-non-compensability/RESULT.md).

### Scope of the non-compensability result — Part VIII.4, verbatim

> Each of Tests A–C is a named probe of one compensation channel (two-pass cover for one fail).
> Refusal in all three does not support Invariant 1. Invariant 1 remains untested except
> against the probes that have actually been run on a named fixture. Claim state: unresolved.

The packet's own list of channels still needing probes named subject relabeling before any
probe existed. EXP-001 ran it; it is CP-T9.

### F-1 — subject relabeling

An operational deployment declared as a `ClaimProtocol`, carrying valid structural and
scientific receipts and no operational receipt, executed with zero violations recorded.

Invariant 1 was not violated. §6.0 assigns authority by *declared* subject; the declaration
determines which gates are required; no rule in the canon requires the declaration to match the
effect. The operational gate was not bypassed — it was never summoned.

**Claim state for invariant 1 as a general guarantee: contradicted under declared scope**
(this implementation, this channel). **Claim state for the seven refused channels: supported
under declared scope** — seven closed doors, unknown door count.

### Proposed invariant 16 — subject binding — proposed, not accepted, not tested

> The authoritative subject of a request is determined by the effect the request would have if
> executed, not by the label the requester supplies. A request whose declared subject admits an
> effect outside that subject's authority is refused as a subject-binding violation. Where the
> effect cannot be determined in advance, the request is refused for indeterminate subject;
> abstention is required, not a default classification.

Untested consequences: effect determination may be undecidable in general, and refusal for
indeterminate subject is a denial-of-service surface.

---

## C. Status

Read against the five-layer ladder in Part VII of the handoff packet:

| Layer | What would count | Where this work stands |
|---|---|---|
| Design specified | Named objects, failure rules, controls, analysis plan, threat model | Supplied, for the non-compensability probes only |
| Implementation | Runnable artifacts matching the design | Supplied — two reference kernels, standard library, no product bindings |
| Test of implementation | Harness fails when the design says it must | **Done.** CP-T9 failed twice; CP-T4, CP-T12, CP-T13, CP-T3 passed |
| Empirical evidence | Named IS/SR/CSRF/CP-T experiments run | CP-T9, CP-T4, CP-T12, CP-T13, CP-T3 against a **reference kernel only**. No IS-*, SR-*, CSRF-1–6. Nothing against a product |
| Independent external verification | Outside party re-runs under preregistration | None. A matching digest is not this |

**Claim state: unresolved. Design specification incomplete.**

**Disposition of the original proposal: revision required.** A-1 struck, A-2 downgraded,
A-3 through A-9 added.

**What remains unproven:** every claim in the canon about whether these frameworks improve
scientific reasoning. No mundane null is ruled out. SR-1 has not been run and requires human
participants.
