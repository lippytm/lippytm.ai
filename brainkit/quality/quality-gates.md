# BrainKit Quality Gates

This document defines the minimum quality gates for repositories, workflows, prompts, and agent-generated outputs in the lippytm ecosystem.

The purpose is to preserve innovation **with discipline**.

---

## Quality Philosophy

Quality is Job #1 across the fleet.

That means:

- creative ideas are welcome
- experiments are encouraged
- production changes still require evidence, structure, and review

A repository is not considered manufacturing-ready until its required quality gates are documented and passable.

---

## Fleet Quality Objectives

Every active repo should aim to improve these outcomes:

1. clarity
2. correctness
3. maintainability
4. operational safety
5. integration reliability
6. product usefulness
7. monetization alignment
8. upgrade readiness

---

## Quality Gate Levels

### Level 0 — Idea Capture
Use for early concept repos or very early drafts.

Requirements:
- clear README
- declared repo role
- rough roadmap
- separated experimental area

### Level 1 — Structured Prototype
Use for labs and early product proofs.

Requirements:
- architecture note or product design note
- repeatable setup steps
- core config documented
- test or validation approach declared

### Level 2 — Managed Build
Use for active repos with repeated internal use.

Requirements:
- lint or validation checks
- documented workflows
- known integration surfaces
- quality checklist
- operator recovery notes

### Level 3 — Production Ready
Use for revenue, control, swarm, or customer-facing systems.

Requirements:
- automated tests where applicable
- security review
- integration verification
- rollback or failure plan
- release quality checklist
- observability or logging strategy

### Level 4 — Fleet Critical
Use for payment, control-tower, standards, or security-sensitive systems.

Requirements:
- strict review policy
- least-privilege design
- approval gates for sensitive actions
- traceable events and auditability
- recovery drill documentation
- dependency and secrets hygiene

---

## Mandatory Quality Gates by Repo Lane

| Lane | Minimum Level |
|---|---|
| `hub` | Level 4 |
| `control` | Level 4 |
| `swarm` | Level 3 |
| `revenue` | Level 3 |
| `product` | Level 2 |
| `commerce` | Level 4 |
| `knowledge` | Level 1 |
| `lab` | Level 1 |

---

## Required Checks for Code Repos

### Documentation Gate
The repo must explain:
- purpose
- architecture or product structure
- setup steps
- integration surfaces
- next priorities

### Structure Gate
The repo must separate:
- runtime code
- config
- tests
- prompts
- sandboxes
- docs

### Validation Gate
At least one of the following must exist:
- unit tests
- integration tests
- schema validation
- static checks
- reproducible manual validation steps

### Change Safety Gate
The repo must define:
- risky paths
- protected files
- approval requirements for sensitive changes
- rollback or restore path for major failures

### Integration Gate
If the repo connects to other systems, it must document:
- inbound connections
- outbound connections
- data or event shapes
- dependency expectations

---

## Required Checks for Prompt Assets

Each reusable prompt should declare:
- intended agent or role
- purpose
- inputs
- constraints
- expected output shape
- failure modes

Prompt assets should be reviewed for:
- ambiguity
- unsafe permissions
- missing constraints
- lack of output structure

---

## Required Checks for Agent Outputs

Agent output should be scored on:

| Dimension | Question |
|---|---|
| Clarity | Is the output understandable to the next operator or agent? |
| Correctness | Is it likely accurate and internally consistent? |
| Actionability | Can it be used without major rework? |
| Safety | Does it avoid risky or uncontrolled actions? |
| Alignment | Does it support the repo’s role and business purpose? |
| Traceability | Can the source task or prompt be identified? |

A failed score in safety or alignment blocks production use.

---

## Release Readiness Checklist

Before release or production rollout:

- README is current
- roadmap is current enough to guide next work
- architecture docs reflect the current state
- sensitive configuration is not hard-coded
- required tests or validations pass
- protected paths were not changed without approval
- integration assumptions were checked
- release notes or summary exist

---

## Quality Metrics to Track

Each active repo should track some combination of:

- documentation completeness
- test pass rate
- lint pass rate
- issue resolution speed
- deployment success rate
- rollback frequency
- prompt reuse quality
- agent false-positive rate
- lead conversion rate for revenue repos
- uptime or workflow success rate for operational repos

---

## Quality Failure Triggers

Immediate review is required if any of the following happens:

- repeated failed deployments
- broken routing between repos
- stale docs causing operator confusion
- agent changes without clear constraints
- secrets exposure risk
- monetization path broken in a revenue repo
- critical event flow not logged or traceable

---

## Rule of thumb

A system is not scalable just because it can automate. It is scalable when it can automate, recover, explain itself, and improve without losing control.
