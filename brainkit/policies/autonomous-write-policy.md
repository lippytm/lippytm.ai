# Autonomous Write Policy

This policy defines how Synthetic Intelligence agents, swarm systems, and higher-order automation may write changes across the lippytm ecosystem.

## Purpose

The goal is to allow fast improvement loops **without allowing uncontrolled repo mutation**.

---

## Write Modes

### 1. Read Only
Agents may inspect and summarize, but not modify files.

### 2. Proposal Only
Agents may generate suggested changes, but a separate approval or apply step is required.

### 3. Limited Autonomous Write
Agents may create or update low-risk files in approved areas.

### 4. Governed Autonomous Write
Agents may write to broader areas only when policy, path protection, and review conditions are satisfied.

### 5. Blocked
No autonomous write allowed.

---

## Default Lane Policy

| Lane | Default Write Mode |
|---|---|
| `hub` | proposal only |
| `control` | proposal only |
| `swarm` | limited autonomous write |
| `revenue` | limited autonomous write |
| `product` | limited autonomous write |
| `commerce` | proposal only |
| `knowledge` | limited autonomous write |
| `lab` | governed autonomous write |

---

## Allowed Autonomous Write Examples

Normally allowed with traceability:
- new docs in approved doc folders
- roadmap updates
- prompt drafts in prompt folders
- new test stubs in non-protected areas
- generated reports in artifacts folders
- safe schema additions in approved contract paths after review rules are met

---

## Restricted Autonomous Write Examples

Require stronger review or approval:
- policy changes
- payment logic changes
- workflow deployment changes
- registry and fleet-control changes
- auth and security changes
- high-impact public conversion logic

---

## Required Conditions For Autonomous Write

- repo lane known
- task objective known
- target path known
- protected path check completed
- event traceability enabled
- rollback path known for high-impact changes

---

## Best Practices

- default to smaller scope
- write low-risk assets first
- prefer proposals in higher-risk lanes
- keep every autonomous write tied to a mission or task id
- require approval for money, permissions, or fleet-governance changes

---

## Rule of thumb

Autonomous write is most powerful when it is narrow, traceable, and policy-aware.
