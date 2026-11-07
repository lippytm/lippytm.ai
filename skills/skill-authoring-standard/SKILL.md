---
name: skill-authoring-standard
description: Use when creating, rewriting, reviewing, or versioning a SKILL.md in this repository, when a skill has grown vague or unexecutable, or when deciding whether a repeated workflow deserves promotion to a skill at all. This is the standard every other skill is written against.
compatibility: Created for Zo Computer, GitHub Copilot coding agents, and Claude sessions
metadata:
  author: lippytmai.zo.computer
  canonical_repo: lippytm/lippytm.ai
  created: 2026-11-07
  version: 1.0.0
---

# Skill Authoring Standard

## Purpose

A skill is an instruction that survives a session. Everything in this repository that an agent is expected to do correctly twice should eventually be a skill. This document defines what makes one work, so that twenty-two skills read as one system instead of twenty-two good intentions.

## The test for whether something should be a skill

Promote a workflow to a skill only when all four hold:

1. It has repeated, or will repeat, at least three times.
2. Doing it wrong has a cost that compounds — stale state, unsafe action, lost evidence.
3. The procedure fits on one page and does not need a decision the skill cannot make.
4. It has a finish line somebody can check.

If any is false, it is a note, a plan, or a record — not a skill. Most bad skills were written because a workflow was interesting, not because it recurs.

## Required structure

Every SKILL.md carries these, in this order.

### Front matter

```yaml
---
name: kebab-case-matching-the-directory
description: Use when <specific trigger>. <What it produces>. Do not use for <adjacent thing that is a different skill>.
compatibility: Created for Zo Computer
metadata:
  author: lippytmai.zo.computer
  version: MAJOR.MINOR.PATCH
---
```

The `description` is the only part an orchestrator reads when choosing between skills. It must name the trigger, not the topic. "Use when a PR backlog exceeds review capacity" routes correctly; "about pull requests" does not. Always include the negative case, or the skill will be selected for work it cannot do.

### Body sections

| Section | Required | What it carries |
|---|---|---|
| Purpose | yes | One short paragraph. What changes after an agent reads this. |
| When to use / when not to | yes | Positive triggers and explicit exclusions. |
| Procedure | yes | Numbered, ordered, one action per step. |
| Hard rules | when the skill has any risk | The lines an agent must not cross, stated as prohibitions. |
| Refusal conditions | when a correct answer can be "no" | The conditions under which the agent stops and hands back. |
| Output format | yes | The exact shape of the result. |
| Acceptance test | yes | Checkable conditions proving the run succeeded. |
| Worked example | when the inverse is easy | The shape of a real run, with placeholder values declared as placeholders. |

## Writing rules

1. **One action per numbered step.** A step containing "and" is two steps.
2. **Name the artifact.** Every step that produces something names where it goes.
3. **Prohibitions are positive-negative pairs.** Not "be careful with secrets" but "never write a token into a file, a commit, or a log."
4. **No proxies for evidence.** If a step claims verification, it names the artifact that proves it.
5. **Bound the scope in the description**, not in a warning halfway down.
6. **Write the acceptance test first.** If you cannot state what a finished run looks like, you do not yet know the procedure.
7. **Never reference a capability the agent may not have.** Say what to do when it is missing.
8. **No skill depends on a session.** If a skill cites a previous conversation as the context, it is a note wearing a skill's clothes.
9. **Keep the reading time under about four minutes.** Past that, split it.

## Versioning

- **MAJOR** when the required inputs, the hard rules, or the acceptance test change.
- **MINOR** when steps are added or reordered without changing what a finished run looks like.
- **PATCH** for wording, typos, clearer examples.

Record the bump in the commit message. A skill whose behaviour changed without a version bump has silently broken every orchestrator that selects it.

## Anti-patterns

| Anti-pattern | Why it fails | Fix |
|---|---|---|
| A skill that describes a topic | Orchestrators cannot route to it | Name the trigger and the exclusions |
| A skill with no acceptance test | Two runs, two different standards | State the checkable finish |
| A skill that says "review for quality" | Unmeasurable, therefore unenforceable | Name the specific defect classes |
| A skill that duplicates another | Both get selected, work is done twice | Merge, or add the exclusion to both |
| A skill citing a chat as its source | The context is gone next session | Write the durable rule |
| A skill with the answer baked in | Fails the moment the data changes | Name the procedure, not the result |

## Acceptance test

A skill conforms when all of the following hold:

1. The directory name and the front-matter `name` match.
2. The `description` names a trigger and at least one exclusion.
3. Every required section is present and non-empty.
4. Every numbered step contains one action.
5. Hard rules exist whenever the skill can take a consequential action.
6. The acceptance test is checkable by a second person without reading the procedure.
7. Any worked example declares its values as placeholders.
8. No step references a prior conversation or session state.

## Output format

When authoring or revising a skill, return:

- Skill name and version
- Trigger and exclusions
- Sections added or changed
- Acceptance test
- Overlap check against the existing skills
- Commit message
