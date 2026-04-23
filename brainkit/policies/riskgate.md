# BrainKit RiskGate Policy

RiskGate is the fleet decision framework for determining whether a proposed action can proceed automatically, needs human review, or must be blocked.

Its purpose is to enable fast AI-assisted building **without losing control**.

---

## Core principle

AI may propose broadly.

AI may execute narrowly.

High-impact changes must be reviewed or explicitly approved according to risk.

---

## RiskGate Decisions

Every proposed action receives one of four outcomes:

| Outcome | Meaning |
|---|---|
| `allow` | Safe to proceed automatically |
| `review` | Requires human or supervisor review before execution |
| `approve` | Requires explicit approval from an authorized operator |
| `block` | Must not proceed under current conditions |

---

## Risk Dimensions

RiskGate evaluates actions across these dimensions:

### 1. Scope Risk
How much of the system could be affected?

### 2. Security Risk
Could credentials, secrets, permissions, or trust boundaries be affected?

### 3. Revenue Risk
Could monetization flows, offers, payment logic, or customer-facing conversion paths be damaged?

### 4. Operational Risk
Could the change break deployment, routing, workflows, or control-plane stability?

### 5. Data Risk
Could user data, lead data, event logs, or business records be corrupted or exposed?

### 6. Reputational Risk
Could public messaging, product behavior, or content damage trust or brand clarity?

---

## Sensitivity Classes

| Class | Meaning |
|---|---|
| `S0` | Harmless documentation or isolated sandbox changes |
| `S1` | Low-impact code or content changes with limited blast radius |
| `S2` | Moderate workflow, integration, or product-surface changes |
| `S3` | High-impact production, control, routing, or revenue changes |
| `S4` | Critical security, payment, identity, or fleet-governance changes |

---

## Default Policy by Sensitivity Class

| Class | Default Outcome |
|---|---|
| `S0` | `allow` |
| `S1` | `review` |
| `S2` | `review` |
| `S3` | `approve` |
| `S4` | `block` unless explicitly approved under controlled procedure |

---

## Automatically Allowed Actions

These are normally eligible for `allow` if they are isolated and well-scoped:

- adding documentation in non-sensitive folders
- adding roadmap entries
- creating sandbox assets
- adding prompt drafts in experimental prompt folders
- generating reports or read-only diagnostics
- adding non-sensitive schemas or standards documents

---

## Review-Required Actions

These normally receive `review`:

- changing workflow behavior
- changing routing logic
- adding or modifying prompts used in automated production flows
- editing product-surface copy tied to offers or user actions
- changing config that affects multiple repos or agents
- adding new integrations without complete documentation

---

## Approval-Required Actions

These normally receive `approve`:

- changes to production deployment logic
- changes to payment or subscription flows
- modifying approval, policy, or permission code
- altering swarm-control logic with operational blast radius
- enabling autonomous write actions across multiple repos
- deleting important files or replacing architecture-critical modules

---

## Blocked Actions

These are blocked by default unless a controlled exception process exists:

- exposing or moving secrets into code or public config
- removing auditability from fleet-critical actions
- disabling essential security checks in critical repos
- bypassing approval rules in control, commerce, or hub repos
- writing to protected paths marked as approval-only
- destructive bulk operations without rollback planning

---

## Protected Paths

Repositories may define protected paths such as:

- `.github/workflows/`
- `src/security/`
- `src/fleet/`
- `brainkit/policies/`
- payment or billing route folders
- contract deployment configuration

Changes to protected paths should default to `review` or `approve` depending on repo lane.

---

## RiskGate Evaluation Template

```yaml
action_id: example-123
repo: lippytm/example
path: src/fleet/policy.js
change_type: update
sensitivity_class: S3
scope_risk: high
security_risk: moderate
revenue_risk: low
operational_risk: high
data_risk: low
reputational_risk: low
recommended_outcome: approve
reason: core fleet policy logic affects orchestrated execution
```

---

## Lane-Based Defaults

| Lane | Minimum RiskGate Strictness |
|---|---|
| `hub` | high |
| `control` | high |
| `swarm` | medium-high |
| `revenue` | medium-high |
| `product` | medium |
| `commerce` | very high |
| `knowledge` | low-medium |
| `lab` | low |

---

## Human Approval Roles

Suggested approval roles:

- operator
- architect
- security reviewer
- monetization reviewer
- release reviewer

One person may hold multiple roles in a solo-operated ecosystem, but the decision type should still be recorded.

---

## Audit Expectations

For every `review`, `approve`, or `block` outcome, record:

- what action was proposed
- who or what proposed it
- why the decision was made
- what conditions would change the decision

---

## Rule of thumb

If a change can affect trust, money, routing, permissions, or cross-repo operations, treat it as a governed action, not just a code edit.
