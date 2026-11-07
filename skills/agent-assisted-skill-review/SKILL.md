---
name: agent-assisted-skill-review
description: Use when an agent is available to help collect skill-evaluation triggers, diagnose which failure class a skill run belongs to, or detect overlap between skills. This skill bounds what such an agent may and may not do. Not for an agent applying changes to a skill — no agent may do that.
compatibility: Created for Zo Computer, GitHub Copilot coding agents, and Claude sessions
metadata:
  author: lippytmai.zo.computer
  canonical_repo: lippytm/lippytm.ai
  created: 2026-11-07
  version: 1.0.0
---

# Agent-Assisted Skill Review

## Purpose

An agent adds real value to skill improvement in exactly three places, and is dangerous in a fourth. This skill names the line so the value is captured without the danger.

## The division of labour

| Agent may | Agent may not |
|---|---|
| Scan run records, PR comments, CI logs, and session notes for evaluation triggers | Decide which revision to apply |
| Classify a failed run into one of the four failure classes | Edit a skill file |
| Detect overlap between two skills' triggers | Bump a version |
| Draft a proposed diagnosis for human review | Mark a trigger as valid on its own authority |
| Propose a patch as a diff in a comment | Merge, promote, or retire anything |

**The line:** an agent may diagnose. An agent may not author the change of record. A patch an agent applies without a human-authored PR is self-modification with a reviewer-shaped alibi, and the repository's governance skills exist to prevent exactly that.

## Why the boundary sits here

An agent that both collects triggers and applies fixes will drift toward finding whatever it can fix. That is not malice, it is an objective function. The version-bump requirement is the defence: every change must cite a trigger from a real event, and a trigger the agent proposed about itself is not a real event.

## The three jobs, in order of value

### Job 1 — Trigger collection (highest value, lowest risk)

`skill-improvement-engine` states in its own limits that it cannot detect a skill that was ignored unless the run is recorded somewhere it can read. An agent fixes that by reading where the work actually happened: closed PRs, CI logs, review comments, and commit messages.

A scan returns, per finding:

```
- date, source (PR / CI run / commit / review comment), skill implicated, observed behaviour, why it is a trigger
```

Rules:

- Read-only. The scan never writes to a skill.
- A finding without a linkable source is discarded, not reported as a hypothesis.
- Findings the agent cannot date are reported as undated, not guessed.

### Job 2 — Failure-class diagnosis

The four classes — not selected, selected-not-followed, followed-wrong-result, obsolete — are stated in `skill-improvement-engine`. An agent classifies a finding by reading the run against the skill text.

A diagnosis returns:

```
- finding, skill, class, the passage in the skill that caused it, confidence, what would falsify the classification
```

Rules:

- The agent must **quote the skill passage** it blames. A diagnosis without a quoted passage is a guess.
- State what would falsify the classification. A diagnosis that cannot be wrong is not a diagnosis.
- One class per finding. If two seem true, the agent reports which it thinks is primary and why.

### Job 3 — Overlap detection

Read all `description` fields and report any pair that will both route to the same task.

Rules:

- Compare triggers, not topics. Two skills about the same subject with different triggers do not overlap.
- Report the overlapping phrase and which skill should carry an exclusion.
- Never propose a merge. Report the overlap; the merge decision is `skill-improvement-engine`'s and a human's.

## Job 4 — The one it must not do

An agent must not apply a change. Specifically it must not:

- Write into `skills/`
- Commit a version bump
- Set a skill's `metadata.version`
- Mark a skill retired
- Approve its own proposal
- Evaluate a change it proposed itself — that is `sandboxed-skill-evaluation`'s job, with an independent judge

## Agent operational rules

1. **Read-only by default.** Where an agent needs write access for a legitimate reason, it is to a scratch area, never to `skills/`.
2. **Every claim carries its source.** A PR number, a CI run id, a commit SHA, or an explicit "no source found."
3. **No fabricated triggers.** An agent that cannot find a trigger says so. Inventing one to justify a change is the specific failure this skill prevents.
4. **One pass, then stop.** An agent does not loop over its own findings re-deriving them.
5. **No cross-repository writes.** A review agent reads across the fleet and writes nothing outside its scratch area.
6. **Secrets never enter a finding.** A trigger that would require quoting a credential is reported as "redacted trigger."
7. **Escalate rather than resolve.** An owner-only question is reported as blocked, never decided.
8. **Declare the model and the date.** A diagnosis is only meaningful with both.
9. **No self-evaluation.** An agent never judges its own output as correct.
10. **Zero authority over promotion.** An agent's highest possible output is a reviewed recommendation.

## Refusal conditions

An agent stops and reports blocked when:

- It is asked to apply, merge, promote, or version-bump anything.
- The only available evidence for a trigger is its own earlier output.
- A finding requires reading a credential, a private key, or customer data.
- The run records needed to classify a finding do not exist.
- It is asked to evaluate a change it proposed.

## Output format

```
## Triggers found
- Date, source, skill, observed behaviour, why it is a trigger

## Diagnoses
- Finding, skill, class, quoted passage, confidence, falsifier

## Overlaps
- Skill A ↔ Skill B, overlapping phrase, who should add the exclusion

## Blocked
- Item, condition that fired

## Boundaries observed
- What the agent did not do, and the model and date of the pass
```

## Acceptance test

1. Every trigger names a linkable source, or is marked "no source found."
2. Every diagnosis quotes the skill passage it blames.
3. Every diagnosis states a falsifier.
4. No file under `skills/` was modified by the pass.
5. Every overlap names a phrase and a suggested exclusion, and proposes no merge.
6. The pass declares its model and date.
7. No self-evaluation appears.
8. Every owner-only question appears under Blocked rather than resolved.
9. No credential or private datum appears in any finding.
10. The output contains no applied change, no bump, and no promotion.

## Known limits

- Without run records there is little to read. The agent's value is proportional to how much of the fleet's work is logged. If nothing records runs, Job 1 returns empty and that emptiness is itself the finding.
- An agent classifying a failure can be wrong in a way a human would catch. That is why the class is a proposal with a quoted passage, and the decision stays with `skill-improvement-engine` under human review.
- This skill bounds an agent. It does not run one, schedule one, or grant one access.
