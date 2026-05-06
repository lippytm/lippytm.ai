# RiskGate Decision Log

## Purpose

Track security and cybersecurity risk decisions before changes are executed across repositories, websites, bots, CRM paths, databases, automations, and autonomous systems.

## Operating principle

```text
AI proposes -> RiskGate classifies -> Human approves high-risk actions -> Executor acts -> Verification runs -> Documentation updates
```

## Risk levels

### Low

Examples:

- Documentation update.
- Public non-sensitive copy update.
- Canva prompt update.
- Checklist improvement.

Approval:

- Normal review.

### Medium

Examples:

- GitHub workflow change.
- Dependency update.
- Website form change.
- Bot prompt change.
- CRM routing update.
- Affiliate copy update.

Approval:

- Review recommended before merge.

### High

Examples:

- Secrets or credentials.
- Authentication.
- Payment flow.
- Database schema/data storage.
- Deployment workflow.
- Cross-repo automation.
- Autonomous actions that modify external systems.

Approval:

- Explicit human approval required.

### Critical

Examples:

- Exposed production credential.
- Compromised account.
- Major private data exposure.
- Active exploitation.
- Autonomous system causing broad unintended changes.

Approval:

- Immediate containment first, then owner-led incident response.

## Decision table

| Date | Repo/Platform | Change | Risk Level | Reason | Approval Needed | Decision | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | Low / Medium / High / Critical |  | Yes / No | Approved / Rejected / Needs changes / Monitoring |  |  |

## Decision checklist

Before approving a change, ask:

- [ ] Does this touch secrets or credentials?
- [ ] Does this touch private lead/customer data?
- [ ] Does this touch CRM, database, authentication, payment, or deployment?
- [ ] Does this create or change an autonomous action?
- [ ] Does this affect multiple repositories?
- [ ] Does this change public claims or affiliate disclosures?
- [ ] Does this need a rollback plan?
- [ ] Does this need human approval?

## Best practice

When unsure, classify one level higher and use a reviewable pull request.