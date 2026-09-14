# Credits

Author and architect: **James Andrew Tillar**, Tillar Technologies. The three frameworks, the
method, and every decision about what this repository claims are his.

Six AI systems contributed. Each is credited for what the record shows it did, at the strength
the record supports — which is the same standard the documents here are held to. None is an
independent witness in this canon's sense: none held root digests independently before the
work, none re-ran anything under preregistration, and all worked from material the author
supplied. Cross-lineage review is **rival generation** (SR-5). It is valuable and it is not
replication.

---

## Implementation and execution

**Claude** (Anthropic — Cowork) built the reference kernels v1, v2 and v3, wrote the probe
suites, ran EXP-001, EXP-002 and EXP-003, performed the derivation input audit, and assembled
this repository.

Found by execution: **F-1** (subject relabeling defeats non-compensability without violating
it), **K** (deriving from a caller-supplied field inherits the defect), **L4** (the remedy made
a subject class unreachable), and the two siblings **S-1** and **S-2** found by mechanical audit
before either was probed.

Also recorded against it, because the method requires it: it claimed the run had found the
subject-relabeling channel when a reviewing lineage had named it first — an overclaim in its
own favour, retracted in
[`experiments/TEST_BINDING.md`](experiments/TEST_BINDING.md). It built the probe series unbound
to this canon's own test catalogue, which is precisely the defect `G-new-5` names. It shipped
an integrity manifest whose three digests all failed. Each was caught by review, not by the
author of the work.

## Model verification and custody

**Codex** (OpenAI, GPT lineage) owns local model verification and the blob manifests, ran the
thirteen-model gauntlet, and performed the independent custody check on the EXP-004 package —
verifying 9 of 9 frozen inputs and confirming the sealed answer key matched its published
digest without opening it. That check is the first real test of the hash-commitment mechanism
used here, and it held.

## Review

Four lineages reviewed the experiment-infrastructure proposal and this repository before
publication. Their sustained findings changed the documents materially.

**DeepSeek** authored the original experiment-infrastructure contribution — preregistration
template, firewall operationalization, bypass tests, logging scheme. Disposition: revision
required. Its structure survived; three of its mechanisms did not, and the document is the
reason the others had something specific to attack.

**Grok** produced the independent review that struck the proposal's central mechanism:
outcome correlation as a firewall criterion is a **category error**, not a weak threshold — an
evidential-use prohibition and a statistical independence claim are different kinds of object,
and the rule fails in both directions. Also: hash chains and bundle digests are **custody, not
evidence**, and "closes G1 and G4 as design" is not a legal claim state. Its replacement
language for the firewall and custody sections is adopted verbatim in
[`amendments/2026-09-14-experiment-infrastructure.md`](amendments/2026-09-14-experiment-infrastructure.md).

**Gemini** extended the non-compensability probe suite from three channels to eight — adding
later-gate pardon, witness escalation, **subject relabeling**, score averaging and
amendment-as-weakening. Subject relabeling is the channel that broke the first kernel. It also
established the **metric isolation** and **harness separation** rules: a scientific harness
bound to an operational product cannot produce a clean baseline, which is why every kernel here
is standard-library and product-detached.

**Microsoft Copilot** consolidated the review chain and added the compensation channels the
others had not listed — silent fallback, implicit inheritance, interface conflation, temporal
drift — the implementer-as-adversary threat model, and the requirements an external witness
must meet: hold independent root digests, re-run under preregistration, publish deviations, and
mint no authority.

---

## What the review chain did and did not establish

Between them the four reviewers caught a category error, a threat-model mismatch, an illegal
claim state, a missing control, and five unexamined attack channels — before any of it was
published.

None of them found **K**, and none found the two siblings. Those needed execution and a
mechanical audit. And Gemini named subject relabeling as a channel needing a probe, while the
demonstration that it *executes* — and why — came from running it. Naming a channel and
demonstrating it are different acts, and both are credited here as what they were.

The reviewers all worked from text supplied by the author rather than acquiring their own
observations. That is the limit of what this chain can support, and it is why the
`independent external verification` rung of the ladder in [`METHOD.md`](METHOD.md) remains
empty.
