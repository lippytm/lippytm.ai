# Protected Paths Policy

This policy defines which paths in the lippytm ecosystem should be treated as higher-sensitivity zones for Synthetic Intelligence, swarm automation, and self-improving engineering workflows.

## Purpose

Protected paths reduce the risk of uncontrolled change by marking files and folders that require stronger review, approval, or rollback awareness.

---

## Protection Principles

Protected paths should be used for assets that affect:

- governance
- security
- payment and access logic
- rollout behavior
- fleet-wide control
- public trust surfaces with high impact

---

## Default Protected Path Classes

### Class A — Governance and Policy
Examples:
- `brainkit/policies/`
- `brainkit/contracts/`
- `brainkit/quality/`
- `src/fleet/policy.js`
- `src/fleet/registry.js`

### Class B — Security and Authentication
Examples:
- `src/security/`
- auth middleware
- token validation modules
- secret handling logic

### Class C — Commerce and Access
Examples:
- payment routes
- subscription logic
- service receipt logic
- checkout handoff logic
- smart contract deployment configuration

### Class D — Rollout and Control Workflows
Examples:
- `.github/workflows/`
- deployment workflows
- rollback logic
- fleet mission orchestration paths

### Class E — High-Impact Public Flows
Examples:
- major landing-page conversion logic
- intake routing that affects revenue delivery
- premium offer activation paths

---

## Default Handling Rules

| Path Class | Default Handling |
|---|---|
| Class A | review or approve |
| Class B | approve |
| Class C | approve |
| Class D | review or approve |
| Class E | review |

---

## Best Practices

- keep protected paths clearly documented
- avoid broad autonomous writes into protected zones
- require stronger event traceability when protected paths are touched
- define rollback expectations before changing protected areas

---

## Rule of thumb

If a change can alter trust, control, money, permissions, or fleet governance, it belongs in a protected path or should be treated like one.
