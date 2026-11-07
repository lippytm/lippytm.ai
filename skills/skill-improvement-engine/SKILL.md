---
name: skill-improvement-engine
description: Use when reviewing the skills library as a whole, when a skill failed or was ignored in practice, when two skills overlap, when a repeated mistake is not yet covered by any skill, or when scheduling a periodic skills review. Not for writing one new skill from scratch — use skill-authoring-standard for that.
compatibility: Created for Zo Computer, GitHub Copilot coding agents, and Claude sessions
metadata:
  author: lippytmai.zo.computer
  canonical_repo: lippytm/lippytm.ai
  created: 2026-11-07
  version: 1.0.0
---

# Skill Improvement Engine

## Purpose

Most self-improvement fails because it improves outputs and never improves the instructions that produce them. A swarm that gets better at a task while its skills stay stale has improved by accident and will regress on purpose.

This skill closes that loop. It is the meta-skill: it improves skills, rather than doing work.

## When to use

- A skill produced a wrong or unusable result.
- An agent was given a task a skill covers and did not select it.
- Two or more skills overlap in scope.
- The same mistake has appeared in three separate sessions and no skill forbids it.
- A scheduled review window arrives.

Do not use this to write a brand-new skill from nothing. That is `skill-authoring-standard`. This skill changes what already exists.

## The improvement loop

```
trigger -> evidence -> diagnosis -> decide (patch | rewrite | merge | retire) -> version bump -> re-test -> record
```

Every arrow is a separate, logged action. A change made without its trigger recorded is indistinguishable from drift.

### Step 1 — Collect triggers

Gather from real events only:

- Failed skill runs, with the point of failure.
- Tasks completed without the relevant skill being selected.
- Duplicate work that suggests overlapping skills.
- Repeating mistakes across sessions.

Write these to `skills/REVIEWS/<date>-triggers.md` before diagnosing anything. A trigger you cannot cite is an opinion.

### Step 2 — Diagnose against the four failure classes

| Class | Symptom | Usual cause |
|---|---|---|
| **Not selected** | The work happened, badly, without the skill | The `description` names a topic instead of a trigger, or omits exclusions |
| **Selected, not followed** | The skill was read and the steps were skipped | Steps too long, vague, or out of order; the finish line is unclear |
| **Followed, wrong result** | Steps executed, output unusable | A missing hard rule, a missing refusal condition, or a step that assumes a fact the agent cannot know |
| **Obsolete** | The skill describes a system that moved | No review after the underlying system changed |

Diagnose the class before proposing the fix. The same symptom has different fixes in different classes.

### Step 3 — Decide, and pick exactly one

| Decision | When | Version bump |
|---|---|---|
| **PATCH** | Wording, examples, clarity. Behaviour unchanged. | 1.0.0 → 1.0.1 |
| **MINOR** | A step added or reordered; the finish line is the same. | 1.0.0 → 1.1.0 |
| **REWRITE** | The trigger, inputs, or acceptance test was wrong. | 1.0.0 → 2.0.0 |
| **MERGE** | Two skills cover one job. One survives; the other is retired with a pointer. | survivor MAJOR |
| **RETIRE** | The system it described no longer exists. | Leave the file, mark it retired at the top. |

Do not patch a skill whose acceptance test is wrong. That is a REWRITE wearing a patch's clothes, and it will fail again.

### Step 4 — Change it, and nothing else

One decision per skill per cycle. A cycle that rewrites four skills at once cannot be evaluated — when results change, you will not know which change caused it.

### Step 5 — Re-test against the acceptance test

Run the changed skill's own acceptance test, including the case that triggered the review. A change that fixes the new case but breaks a previously working case is a regression, and the version bump must show it.

### Step 6 — Record where the next review will look

Append to `skills/REVIEWS/<date>-decisions.md`: skill, class, decision, version, evidence, re-test result, next review target.

## Automatic rewrite triggers

Escalate a PATCH to a REWRITE when any of these is true:

- The skill has failed the same way twice.
- Its acceptance test could pass while the real output is wrong.
- It selects itself for work its exclusions should prevent.
- It depends on a tool, account, or system that has since been removed, renamed, or made read-only.

## Hard rules

1. **Never change a skill without a recorded trigger.** No trigger, no edit.
2. **Never bump without recording the version.** An unversioned change breaks every orchestrator that selected it.
3. **Never improve more than one skill per cycle.** Attribution requires it.
4. **Never delete a retired skill's file.** It stays, marked, so the retirement is visible.
5. **Never treat a model's suggestion as the trigger.** A suggestion is a proposal; a failed run is a trigger.
6. **Never let this skill edit itself.** Self-modification without review is the failure mode this repository is built to prevent. Changes to this file come from a human-authored PR.

## Refusal conditions

Stop and hand back when:

- No trigger can be cited from a real event.
- The fix requires a decision only the owner holds (a product choice, an account state).
- The skill's failure is actually a tool or permission failure, not an instruction failure. Fix the tool, not the skill.
- Two skills must change together to work. That is one MERGE decision, not two rewrites.

## Output format

```
## Triggers
- Event, date, source, skill implicated

## Diagnosis
- Skill, failure class, cause

## Decision
- One decision, with the version transition

## Change
- Sections changed

## Re-test
- Acceptance-test result, including the triggering case

## Record
- Path of the decision log entry

## Next review target
- The skill and the reason it is next
```

## Acceptance test

1. Every change in the cycle cites a trigger from a real event.
2. Exactly one skill was changed.
3. The version changed, and the transition follows the decision table.
4. The triggering case now passes the skill's own acceptance test.
5. No previously passing case regressed.
6. A retired skill's file still exists and is marked.
7. This file is unchanged by the cycle.
8. The decision log entry exists at the recorded path.

## Known limits

- This skill does not schedule itself. Something else must call it.
- It cannot detect that a skill was ignored unless the run is recorded somewhere it can read. Without run records, half the triggers never surface.
- It judges instructions, not outcomes. If a skill was followed exactly and the business result was still poor, the problem is above the instruction layer.
