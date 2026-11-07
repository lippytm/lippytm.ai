---
name: sandboxed-skill-evaluation
description: Use when a skill has changed and you need to know whether the change helped, when a skill's acceptance test cannot be judged by reading it, when replaying a historical failure to prove a fix, or when deciding whether to promote a skill revision past a draft branch. Not for authoring a skill (skill-authoring-standard) or for deciding what to change (skill-improvement-engine).
compatibility: Created for Zo Computer, GitHub Copilot coding agents, and Claude sessions
metadata:
  author: lippytmai.zo.computer
  canonical_repo: lippytm/lippytm.ai
  created: 2026-11-07
  version: 1.0.0
---

# Sandboxed Skill Evaluation

## Purpose

This skill closes the largest hole in the skills library: a skill revision that was never tested.

`skill-improvement-engine` can decide what to change and can bump a version. It cannot tell you whether the change worked. Reading a revised instruction and believing it is better is not evidence, and an acceptance test that can only be checked by reading is not a test. This skill runs a revised skill against a known case inside an isolated environment and compares the result with the unchanged version.

## When to use / when not to use

**Use when:**

- A skill's version has changed and the change has not been exercised.
- A historical failure exists that the revision claims to fix.
- A hard rule needs to be shown holding under an adversarial input.
- A B/C/D variant of the same instruction is being compared.
- A promotion decision is pending between a draft branch and the default branch.

**Do not use for:**

- Deciding *what* to change — that is `skill-improvement-engine`.
- Writing the skill — that is `skill-authoring-standard`.
- Testing a repository's code. This skill evaluates instructions, not programs. A code change has its own CI.
- Anything requiring a live account, live site, or real money. A sandbox that can spend is not a sandbox.

## What this repository already has, and what it does not

**Already built (Tower Control):** a sandbox architecture with four sandbox layers — lesson, workflow, blockchain, reflection; a promotion scorecard scored out of 35 with bands at 29-35, 22-28, 15-21, below 15; a cross-sandbox reuse model with four reuse layers; sandbox lineage records per system; a sandbox-to-platform promotion matrix; and a `SANDBOX_BUILDER_TEMPLATE` and `AI_SANDBOX_REGISTER_TEMPLATE`.

**Already built (Chatlippytm.ai.Bots):** `agents/sandbox_agent.py`, a `SandboxAgent` that provisions, terminates, and assists inside isolated environments, with a `SandboxEnvironment` descriptor carrying `sandbox_id`, `owner_address`, `modules`, `status`, `cpu_limit`, `memory_mb`. Its own docstring states that all operations are simulated in-process and that a real deployment would call a container orchestrator.

**Missing:** none of that evaluates a **skill**. This repository has 22 skills and no test for any of them. The sandbox machinery exists; the skill-evaluation use case was never wired to it.

This skill is the missing use case, not a new sandbox.

## The evaluation cell

Every run happens in one isolated cell with three parts.

| Part | Contents |
|---|---|
| **Fixture** | A frozen case with a known expected outcome: a task, the inputs, and the result a correct run must produce |
| **Arm** | Exactly one skill version. `A` is the unchanged baseline. `B`, `C`, `D` are revisions |
| **Judge** | A second, independent evaluation of the arm's output against the fixture |

One cell holds one arm. Comparing two versions means two cells sharing one fixture. Never put two versions in one cell; the point is to compare, not to blend.

## Procedure

### Step 1 — Pick the fixture before the change

A fixture must have a **known expected outcome**, or the comparison yields nothing.

Sources, in order of value:

1. **A historical failure with a recorded wrong output.** Strongest — the answer is already known. In this fleet: the seven AI-Time-Machines PRs reaching for one integration (a cluster-detection fixture for `review-triage`); a 442-file PR (a split-decision fixture); the credential-scan CI false positives (a rule-precision fixture).
2. **A task where the correct behaviour is refusal.** Run the arm against an input a hard rule forbids, and check it refuses.
3. **A synthetic task with an authored expected output.** Weakest, and must be labelled synthetic.

Write the fixture to `skills/EVALS/<skill>/<fixture-id>.md` and freeze it. **A fixture edited after a run is a new fixture.** Say so in its filename or it silently invalidates the comparison.

### Step 2 — State the hypothesis as a falsifiable claim

Before running anything, write one sentence:

> Revision `B` of `<skill>` will `<specific change in outcome>` on fixture `<id>`, which version `A` does not do.

If the sentence cannot be made specific, the evaluation has no question. Stop.

### Step 3 — Run each arm in its own cell

For each arm:

1. Provision an isolated cell. If running in this workspace, use a fresh directory per arm and never the working copy of `skills/`.
2. Place the arm's skill version and the frozen fixture in the cell.
3. Give the cell the fixture only. **Do not give it the expected outcome.** An arm that can read the answer is testing its own reading comprehension.
4. Execute the task.
5. Capture the complete output, including refusals, and the reason for any refusal.
6. Record the cell's `sandbox_id`, start and end time, arm version, and the fixture hash.

### Step 4 — Judge independently

Judge the output against the fixture's expected outcome, not against what you hoped.

- Prefer a **second, independent judge** over the same model that ran the arm. Self-evaluation is not verification.
- The judge returns one of: `pass`, `fail`, `refused-correctly`, `refused-incorrectly`, `unusable`.
- `unusable` is a real verdict. An arm whose output cannot be parsed has not passed.
- The judge records *what* differed, not just whether it did.

### Step 5 — Compare, and state the result in one line

| Outcome | Meaning |
|---|---|
| `A` fail → `B` pass | The change works. Evidence for the version bump. |
| `A` pass → `B` pass | No regression, no improvement. The bump may be PATCH-only. |
| `A` pass → `B` fail | **Regression.** Reject the revision, whatever it claims. |
| Both fail | The hypothesis was wrong, or the fixture tests something else. Do not bump. |
| Both refuse correctly | Rule compliance holds. Valuable, and not an improvement. |

A regression blocks the revision. There is no "mostly works."

### Step 6 — Score promotion readiness against the existing scorecard

Use Tower Control's `docs/SANDBOX_PROMOTION_SCORECARD.md` rather than inventing a second scale. Its seven areas — Scenario Clarity, Repeatability, Diagnostic Value, Reuse Potential, Packaging Readiness, Documentation and Transparency, Promotion Value — are scored 1-5, out of 35.

For a skill evaluation, the areas read as:

| Score area | What it means for a skill |
|---|---|
| Scenario Clarity | The fixture names a situation a reader recognises |
| Repeatability | The cell produces the same verdict on a re-run |
| Diagnostic Value | A failure tells you which failure class it was |
| Reuse Potential | The fixture tests more than one skill |
| Packaging Readiness | The fixture and cell can be handed to another session |
| Documentation and Transparency | Assumptions, model, and limits recorded |
| Promotion Value | The revision is worth landing on the default branch |

Interpretation stays the same: **29-35** promote, **22-28** improve then promote, **15-21** more shaping, **below 15** early-stage.

### Step 7 — Record the receipt

Write to `skills/EVALS/<skill>/<date>-<fixture-id>.md`:

- Skill, versions of each arm, fixture id and hash
- Hypothesis, verbatim from step 2
- Per-arm: cell id, verdict, judge's note on what differed
- Comparison result from the table in step 5
- Scorecard total and band
- Promotion recommendation, or the refusal to give one
- Everything that was **not** tested

### Step 8 — Refuse to promote on any of these

The evaluation does not promote when:

- Only one arm was run (nothing was compared).
- The fixture had no expected outcome.
- The judge was the same process that ran the arm, with no second check.
- The result was produced outside the cell.
- A regression appeared.
- The score lands below 22.

## Hard rules

1. **One variable per comparison.** One skill version. A run that changes two things proves nothing about either.
2. **The fixture is frozen before the run.** A fixture changed mid-evaluation restarts it.
3. **The expected outcome never enters the cell.**
4. **The judge is not the runner**, wherever a second judge is available. Where none is, say so in the receipt and mark the verdict `self-judged`.
5. **A sandboxed run has no credentials, no live accounts, no network egress, no money, and no write access to the real skills directory.** If a test needs any of those, it is not a sandbox test — refuse it.
6. **Promotion is a human action.** This skill produces a recommendation and a receipt. It never edits the default branch.
7. **A historical failure is replayed from a recording, not from memory.** If the original output was not recorded, say the fixture is reconstructed and downgrade the confidence.
8. **Record what was not tested.** A receipt without a limits section is an overclaim.
9. **Never let the sandbox write outward.** It reads fixture, skill, and nothing else; it writes only to its own cell directory.
10. **A vacuous pass is a failure.** If the arm passed because the fixture was too easy, that is a fixture defect, and it is recorded as one.

## Refusal conditions

Stop and hand back when:

- No fixture with a known expected outcome can be constructed.
- The skill's behaviour cannot be observed without a live account, credential, or paid call.
- The evaluation would require comparing two skills that are also being changed.
- The revision's own author is the only available judge.
- The skill under test is this one. `sandboxed-skill-evaluation` does not evaluate itself.

## Output format

```
## Hypothesis
- Skill, arms, fixture id and hash, one falsifiable sentence

## Cells
- Arm, cell id, provisioned/terminated times, verdict

## Judge
- Verdict per arm, what differed, judge identity or "self-judged"

## Comparison
- One row from the outcome table

## Scorecard
- Seven areas, total, band

## Recommendation
- Promote / improve-then-promote / reshape / hold, or a refusal with its condition

## Not tested
- Every relevant thing this run does not cover

## Receipt
- Path written
```

## Acceptance test

1. Every arm has its own cell, and no cell held two skill versions.
2. Every fixture has a stated expected outcome and a hash.
3. No cell contained the expected outcome.
4. The judge differs from the runner, or the receipt says `self-judged`.
5. The comparison cites the outcome table and names the row.
6. Any regression blocked the revision.
7. The scorecard used Tower Control's seven areas and bands rather than a new scale.
8. The receipt contains a limits section listing what was not tested.
9. No credential, network call, or write outside the cell occurred.
10. Promotion is a recommendation, and no default branch was modified.

## Worked example — the shape of a real run

Values below are placeholders. Reusing them instead of running is a failed run.

```
## Hypothesis
- review-triage 1.0.x → 1.1.0 will cluster the seven AI-Time-Machines
  integration PRs into one survivor plus six closures; 1.0.x lists seven items.
  Fixture: cluster-seven-integration-prs (frozen <hash>)

## Cells
- Arm A (1.0.x): cell <id>, 00:00-00:09, verdict fail
- Arm B (1.1.0): cell <id>, 00:00-00:11, verdict pass

## Judge
- Independent judge, different model. A produced seven separate decisions
  with no cluster section. B produced one cluster, one survivor, six closures
  each naming the survivor.

## Comparison
- A fail → B pass — evidence for the version bump

## Scorecard
- Clarity 5, Repeatability 4, Diagnostic 4, Reuse 3, Packaging 4,
  Transparency 5, Promotion 4 = 29 — promote band

## Recommendation
- Promote to draft branch. Owner merges.

## Not tested
- Fixtures with no historical recording; skills needing credentials;
  cross-skill interaction; long-run drift.
```
