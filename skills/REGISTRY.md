# LippytmAI Skills Registry

All skills in this repository, with the trigger each one routes on. Generated 2026-11-07 from the skill directories present in this repository.

## How to read this

The **Select when** column is the routing signal. An orchestrator chooses between skills on this line, so a skill whose trigger is vague will be chosen for work it cannot do.

## Core platform skills

| Skill | Select when |
|---|---|
| `skill-authoring-standard` | Writing, rewriting, versioning, or reviewing any SKILL.md; deciding whether a workflow deserves to be a skill |
| `skill-improvement-engine` | Reviewing the skills library as a whole; a skill failed, was ignored, or overlaps another |
| `lippytmai-skill-orchestrator` | Choosing a skill stack before building an agent, workflow, campaign, or swarm |

## Governance and safety

| Skill | Select when |
|---|---|
| `agentic-swarm-governance` | Designing or reviewing agents, swarms, permissions, approval checkpoints, audit trails |
| `agentic-red-team-safety-review` | Finding risk before an agent, page, campaign, or automation reaches users or money |
| `agent-factory-quality-control` | Scoring an agent, template, or automation before production use |

## Build and operations

| Skill | Select when |
|---|---|
| `swarm-manufacturing-line` | Designing a repeatable mass-production system for agents and swarms |
| `toolkit-adapter-factory` | Creating a reusable adapter with a standard task and result packet |
| `agent-interoperability-bridge` | Connecting an agent to an external toolkit, framework, or swarm |
| `self-healing-agent-operations` | Diagnosing and repairing a failure, drift, or stale state |
| `review-triage` | A pull-request or issue backlog exceeds review capacity |

## Evaluation and memory

| Skill | Select when |
|---|---|
| `swarm-observability-evaluation` | Designing metrics, scorecards, or review cadence for a swarm |
| `agent-memory-knowledge-base` | Deciding where durable knowledge should live |
| `autonomous-self-improvement-engine` | Designing an observe-detect-apply improvement loop |

## Product and revenue

| Skill | Select when |
|---|---|
| `agentic-product-design-lab` | Turning an agentic idea into a viable offer |
| `ai-agent-productization` | Turning an existing agent or workflow into a product |

## ChatGPT and Zo bridges

| Skill | Select when |
|---|---|
| `chatgpt-business-integration-hub` | Making ChatGPT Business a first-class source in the build process |
| `chatgpt-business-import-automation` | Unpacking and classifying a ChatGPT export |
| `chatgpt-business-export-automation` | Packaging Zo work for a ChatGPT session |
| `chatgpt-zo-full-workspace-exporter` | ChatGPT needs the whole ecosystem rather than a slice |
| `chatgpt-zo-command-router` | Converting ChatGPT output into routed action packets |
| `chatgpt-zo-api-action-connector` | A Custom GPT action calling a secured Zo endpoint |
| `chatgpt-zo-bidirectional-bridge` | Running the two-way operating model end to end |
| `chatgpt-github-sync-automation` | Moving refined work into a GitHub repository |

## Suggested default stacks

Amend `lippytmai-skill-orchestrator` when a stack changes; this table is a view of it, not a second source.

| Stack | Skills |
|---|---|
| Instruction quality | `skill-authoring-standard` → `skill-improvement-engine` → `review-triage` |
| Fleet maintenance | `review-triage` → `self-healing-agent-operations` → `swarm-observability-evaluation` |
| New agent or swarm | `lippytmai-skill-orchestrator` → `swarm-manufacturing-line` → `agentic-swarm-governance` → `agent-factory-quality-control` |
| External connection | `agent-interoperability-bridge` → `toolkit-adapter-factory` → `agentic-red-team-safety-review` |

## Known gaps

These are observed from the fleet, not invented. Each becomes a pack when it recurs.

- No skill covers the Hostinger verification gate (product, entitlement, interface contract). Blocked on an owner-held fact, so it cannot be completed as a skill yet.
- No skill covers device-labelled continuation, because no device-labelled session exists to test it against.
- No skill covers repository-role classification, though the need is recorded in the fleet registry with 28 repositories unclassified.

## Maintenance

Add a row when a skill is added. Change a row when a `description` changes, because the trigger is the routing key. Retire a row when `skill-improvement-engine` retires the skill, and leave the row in place marked retired.
