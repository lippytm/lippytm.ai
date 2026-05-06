# Incident Response Playbook

## Purpose

Provide a simple response process for security problems across lippytm repositories, websites, CRM, bots, databases, social platforms, and automations.

## Incident examples

- Secret/API key exposed.
- Private lead/customer data exposed.
- Dependency vulnerability found.
- GitHub Actions workflow abused or failing insecurely.
- Website form collecting too much sensitive data.
- Bot asking for private information.
- Database dump committed.
- Public claim creating legal/compliance risk.
- Suspicious account access.

## Response steps

### 1. Identify

Document:

- What happened?
- When was it found?
- Which repo/platform is affected?
- What data or system may be impacted?
- What is the risk level?

### 2. Contain

Immediate actions:

- Remove exposed data.
- Disable risky workflow.
- Revoke exposed token/key.
- Restrict access.
- Pause risky automation.
- Stop collecting sensitive data if needed.

### 3. Eradicate

Fix root cause:

- Patch code.
- Update dependency.
- Remove secret from history where needed.
- Update form/bot prompts.
- Harden permissions.
- Add validation or review.

### 4. Recover

Return to safe operation:

- Rotate secrets.
- Re-run security scans.
- Confirm workflows pass.
- Confirm website/bot/CRM behaves safely.
- Document safe state.

### 5. Learn

Add prevention:

- Update checklist.
- Add GitHub issue template or workflow.
- Improve documentation.
- Add quality gate.
- Add weekly review item.

## Severity levels

### Low

Documentation issue or low-risk public copy issue.

### Medium

Dependency vulnerability, unsafe workflow pattern, or non-sensitive data handling gap.

### High

Exposed secret, private lead/customer data exposure, auth/payment/database risk, or dangerous automation behavior.

### Critical

Active exploitation, major private data exposure, compromised account, or production credential compromise.

## Incident report template

```md
# Security Incident Report

Date found:
Reported by:
Affected repo/platform:
Severity:

## Summary

## Impact

## Immediate containment

## Root cause

## Fix applied

## Secrets rotated?

## Follow-up prevention

## Lessons learned
```

## Best practice

Treat every incident as a chance to improve the system. The goal is not blame; the goal is stronger quality, security, documentation, and automation.
