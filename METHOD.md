# Method


The method that produced every experiment in this repository, stated as instructions rather
than as a description. EXP-001, EXP-002 and EXP-003 are what it looks like when followed,
including the parts where it produced results the author did not want.

Author: James Andrew Tillar. Published under the same CC BY 4.0 terms as the canon.

## What this method is for

Use this method when you are asked to evaluate whether a design, specification, policy, or
system actually does what it claims. The skill produces a preregistered experiment, an honest
result, and a durable record — in that order, without reordering them.

This method is not for building things. It is for finding out whether the things you built are
wrong, and for recording what you found in a way someone else can check.

## The core sequence

Follow these steps in order. Do not skip ahead. Do not reorder. Each step exists because
skipping it produces a specific failure mode named beside it.

### 1. Restate the claim under test as a falsifiable sentence

Write the claim in one sentence of the form: "Under [scope], [system] will [behavior] in all
cases where [condition]."

- If you cannot write this sentence, you are not ready to test. Say so and stop.
- **Failure mode if skipped:** you test a vibe, and any result can be read as support.

### 2. Enumerate the channels that could falsify it

List every distinct way the claim could fail. Number them. Assign each a name.

- Include the ones you think are impossible.
- Include the ones that would be embarrassing if they succeeded.
- When you think the list is complete, write: **"This list is not claimed complete. The channel
  that breaks it may not be on it."** This sentence is mandatory. It stays in every version.
- **Failure mode if skipped:** you test the channels you already thought of, which are the ones
  your design already handles.

### 3. Write the success criterion before running anything

State what counts as a pass and a fail, numerically if possible. "0 of 8 probes permitting
execution" is the form. Do not change it after seeing results.

- **Failure mode if skipped:** you move the goalposts, usually without noticing.

### 4. Specify the scope of every claim you will make

Name the scope in the same sentence as the result: "this implementation, these channels, this
lineage, this single run." Scope is not a hedge. It is part of the claim. A claim without scope
is a claim about everything, which is a claim about nothing.

- **Failure mode if skipped:** narrow results get quoted as general ones.

### 5. Build the apparatus detached from anything it might be tempted to validate

No proprietary bindings, no shared code paths that make a pass trivially true, no fixtures from
the thing being graded. Standard tools. Runnable by a stranger with one command.

- **Failure mode if skipped:** the test passes because the test and the system agree, not
  because the system works.

### 6. Include a positive control — and enough of them to span the legitimate space

One case where the system should succeed, through the same apparatus. If the control fails, the
apparatus is broken and no result from it is meaningful. If it passes, the refusals are
informative.

One control shows the apparatus works. It does **not** show the system still does its job. Any
claim of the form "this restriction does not block legitimate work" needs a **set** of controls
spanning the legitimate input space — one per class of valid request. A fix drawn one notch too
wide passes every adversarial probe and quietly makes a whole class of valid work unreachable,
and a single control will not see it.

- **Failure mode if skipped:** a system that refuses everything scores as perfectly secure.
- **Failure mode if only one control:** a remedy that breaks legitimate work reports clean.

### 7. Preregister before running

Claim, channels, criterion, scope, apparatus, date — to a file. Never edited afterward. Something
you think of mid-run becomes a probe for the next run, not a change to this one.

**Carry at least one probe with no recorded prediction.** Predicting every outcome biases how
you read the ones you got wrong. The unpredicted probe is disproportionately the one that finds
the defect. Report it as observed; do not score it against a target.

- **Failure mode if skipped:** the experiment becomes a demonstration of what you already
  believed.

### 8. Run once. Do not tune.

Record the result. Do not adjust and re-run for a cleaner one. If the result is embarrassing,
the result is the result.

- **Failure mode if skipped:** the output is a receipt for a process you chose after seeing the
  outcome.

### 9. Do not patch the system to make the test pass

The hardest rule and the one that matters most. If the test finds a failure, the failure stays
in the record. Fixing and re-running converts the experiment into a receipt — you are then
demonstrating that a thing you built passes a test you wrote, which proves nothing.

The remedy goes in an amendment marked **proposed, not accepted, not tested**, with a new
experiment named that would test it.

- **Failure mode if skipped:** the loop closes prematurely and the finding disappears into a
  git diff.

### 10. For every remedy, write the probes that attack the remedy before running it

Do not stop at "this fixes it." Write the probes that would break the fix, then preregister them
alongside it.

- **Failure mode if skipped:** the fix works against the original attack and fails against its
  own input — deriving authority from a declaration inherits that declaration's defect one level
  down.

### 11. State what the result does not show

Every result document ends with what remains unproven. "This does not show the framework
improves reasoning. This does not rule out the mundane null. This is not external verification."

- **Failure mode if skipped:** readers supply their own overclaim, and it is always larger than
  yours would have been.

### 12. Retract your own overclaims in the record, not in private

If you claimed more than the evidence supports — especially in your own favor — write a dated
correction in the record. Do not quietly edit. Do not soften. Name the direction of the error:
"this was an overclaim in my own favor."

- **Failure mode if skipped:** the record accumulates unearned credit and nobody trusts anything
  in it.

## The general rules that survive any specific project

1. **A declaration-trust defect cannot be closed by deriving from another declaration.** Trust
   must terminate at a value the caller does not control. If your fix consumes caller-supplied
   data, the fix has the same defect one level down.
2. **The test for whether a caller-supplied input is safe is not "does it come from the caller"
   — it is "is misdeclaring it self-defeating."** An input the executor actually acts on is
   self-limiting: understating it sends the effect elsewhere, so the attack fails by succeeding
   at the wrong thing. An input that only describes what other inputs *mean* costs nothing to
   lie about. Rule 1 applied without this distinction refuses all caller input and produces an
   unusable system.
3. **A passing test proves the test passed.** It does not prove the system works. "The loop
   closes" and "the loop does not terminate" must both appear, or the document is propaganda.
4. **Refusals are informative only if the positive control passed.** Seven closed doors say
   nothing about how many doors exist.
5. **Receipts establish custody, not evidence.** A hash proves two parties hold the same bytes.
   It does not prove the bytes describe what happened.
6. **Cross-review by other agents is rival generation, not replication.** Valuable, and not
   external verification. Say which one you have.
7. **Every remedy is a new experiment, not a conclusion.** Proposing an invariant is not closing
   a gap.
8. **One lineage writing both the system and the tests is a known limitation, not a solved
   problem.** State it every time.

## Output files

- **PREREGISTRATION.md** — claim, channels, criterion, scope, apparatus, date. Before the run,
  never edited after.
- **RESULT.md** — what happened, the channel table, positive control status, and the sections
  "what this does not show" and "what would close what this leaves open."
- **RESULT.json** — machine-readable record of the same.
- **An amendment entry** — remedies proposed but not accepted, dated, with scope and claim state.

Claim states: `supported under declared scope`, `weakened`, `contradicted`, `unresolved`,
`superseded`. Never *proven*, never *closed*, never *validated*. Those words are not in this
vocabulary for a reason.

Where the project already has a catalogue of named tests, **bind each probe to the catalogued
test it instantiates** rather than creating a parallel numbering. An unbound probe series becomes
a second, unofficial catalogue nobody reconciles with the first.

## How to know you're done

You are never done. You are at a state. State the state and stop:

1. design specified
2. implementation supplied
3. test of implementation run
4. empirical evidence gathered (scoped to what was tested)
5. independent external verification obtained

Most work stops at rung three. **Saying you're at rung three when you're at rung three is the
whole skill.** Claiming rung four when you're at rung three is the failure this method exists to
prevent.

## Two drift signals

**Rule 9 will feel unnatural.** The default instinct is to fix the problem and report success.
This method requires the opposite: report the failure and stop, then propose the fix as an
untested amendment. **If you find yourself patching the system so the suite goes green, that
drift is the signal the skill is being applied wrong.** Stop, revert the patch, record the
failure.

**Rule 12 is mandatory, not optional.** It is the step most often skipped by whoever made the
claim, because they are the one it costs. Apply it to your own prior statements in the same
session, without being asked.
