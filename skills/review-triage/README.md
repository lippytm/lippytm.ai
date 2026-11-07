# Review Triage — pack 1

This skill teaches an agent to take an accumulated pull-request backlog and reduce it to a small number of recorded decisions.

## Read this first

`SKILL.md` is the skill. It follows the same front-matter format as the other skills in this repository (`name`, `description`, `compatibility`, `metadata`), so it can be orchestrated alongside `agentic-swarm-governance`, `autonomous-self-improvement-engine`, and `lippytmai-skill-orchestrator`.

## What it changes about current behaviour

The repo already carries an autonomous improvement loop with a safe/approval-required split. That split works for *changes*. It does not cover *decisions*, which is why a backlog can grow while every individual change in it looked safe at the time it was proposed.

This pack adds the missing half: an explicit gate for work that is already proposed and now needs a verdict. It plugs in as the step between "detect improvement opportunities" and "apply safe improvements" — a PR is neither safe nor unsafe to apply until somebody has said what it is.

## How it connects to the rest of the stack

| Existing skill | Relationship |
|---|---|
| `autonomous-self-improvement-engine` | Its step 2 detects opportunities. This pack decides what happens to the proposals that result. |
| `agentic-swarm-governance` | Supplies the role pattern and the approval checkpoints. This pack's Reviewer role is where it runs. |
| `self-healing-agent-operations` | Its findings become triage items once they produce a PR. |
| `lippytmai-skill-orchestrator` | Add `review-triage` to the "AI coding and automation stack" alongside `agentic-swarm-governance`. |

## Why it is a skill and not a one-off cleanup

The backlog in this fleet was produced by agents that were each behaving correctly in isolation. Seven PRs on one integration happened because each agent session started fresh with no record of what the previous session had already proposed. A skill is the mechanism that survives between sessions. Written once here, every future agent session inherits the same three gates instead of inventing a new approach.

## Known limits

- This skill does not run itself on a schedule. Scheduling is the job of whatever executes skills; this pack describes the procedure only.
- It cannot merge, and it should not be given the ability to.
- It cannot resolve an owner-only question. Where the correct gate depends on a product decision, it must refuse and hand back.
- The worked example uses placeholder counts. Any run that reuses those numbers instead of counting is a failed run.
