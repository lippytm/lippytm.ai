# Security Diagnostics Log

Purpose: record failed runs, vulnerabilities, workflow issues, data handling risks, bot/CRM risks, and repairs in a transparent and auditable way.

## Diagnostic table

| Date | Repo | Signal Type | Workflow/File | Category | Severity | Root Cause | Repair | Verification | Prevention Added | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Failed run / CodeQL / Dependabot / Dependency review / Secret risk / Bot risk / CRM risk / Website risk / Database risk / Autonomous risk |  | Workflow config / Permissions / Dependency / Language detection / True vulnerability / Quality-compliance / Autonomous risk | Low / Medium / High / Critical |  |  |  |  | Open / Fixed / Monitoring |

## Diagnostic reasoning note template

```md
# Security Diagnostic Reasoning Note

Date:
Repo:
Workflow/file/platform:
Signal:
Category:
Severity:

## Observation

## Context

## Risk reasoning

## False-positive / configuration check

## Root cause

## Repair plan

## Verification

## Prevention

## Status
```

## Verification methods

Use one or more:

- Workflow re-run passes.
- Dependency alert resolved.
- CodeQL finding closed or dismissed with documented reason.
- Secret rotated.
- Bot prompt updated.
- CRM/form no longer collects risky data.
- Documentation updated.
- Security-risk issue closed.
- Fleet security status updated.

## Best practice

A security repair is not complete until it is verified and prevention is documented.