# Fleet Security Status

Purpose: track security maturity, rollout progress, failed runs, and next security upgrades across lippytm repositories.

## Security mission

Quality and Quality Assurance is Job #1. Security is an ongoing system of documentation, automation, monitoring, incident response, database protection, CRM data safety, bot workflow safety, and continuous improvement.

## Maturity levels

| Level | Name | Description |
| ---: | --- | --- |
| 0 | Unknown | No documented security posture |
| 1 | Documented | Security policy/checklists/data/incident docs exist |
| 2 | Automated | Dependabot, dependency review, and CodeQL/security workflows exist |
| 3 | Reviewed | Failed runs are categorized and reviewed weekly |
| 4 | Controlled | RiskGate, PR review, least privilege, and approval gates exist |
| 5 | Continuous | Security reports, automation, and improvements run continuously |

## Phase 1 status

| Repository | Security Docs | Automation | Risk Template | Status | Next Action |
| --- | --- | --- | --- | --- | --- |
| `lippytm/lippytm.ai` | Yes | Yes | Yes | Control repo started | Review new workflow runs and categorize failures |
| `lippytm/Chatlippytm.ai.Bots` | Yes | Yes | Yes | Minimum + full docs added | Review Actions runs and classify failures |
| `lippytm/AllBots.com` | Yes | Yes | Yes | Minimum + full docs added | Review Actions runs and classify failures |
| `lippytm/lippytm-lippytm.ai-tower-control-ai` | Yes | Yes | Yes | Tower package added | Review Actions runs and classify failures |

## Phase 2 target repos

| Repository | Security Docs | Automation | Risk Template | Status | Next Action |
| --- | --- | --- | --- | --- | --- |
| `lippytm/Clawlippytm.ai.Bots` | Pending | Pending | Pending | Not started | Roll out minimum package |
| `lippytm/OpenClaw-lippytm.AI-` | Pending | Pending | Pending | Not started | Roll out minimum package |
| `lippytm/AllBots.com.ai` | Pending | Pending | Pending | Not started | Roll out minimum package |

## Failed run review table

Use `security/FAILED_RUN_REVIEW_TAXONOMY.md`.

| Date | Repo | Workflow | Run URL | Category | Severity | Root Cause | Fix | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Workflow configuration / Permissions / Dependency / Language detection / True vulnerability / Quality-compliance |  |  |  |  |

## Weekly review checklist

- [ ] Review failed GitHub Actions runs.
- [ ] Classify every failed run.
- [ ] Review Dependabot alerts and PRs.
- [ ] Review CodeQL/security findings.
- [ ] Review dependency review failures.
- [ ] Review open security-risk issues.
- [ ] Check for exposed secrets or private data.
- [ ] Review website/CRM/bot data handling.
- [ ] Update this status file.
- [ ] Add prevention controls.

## Current known issue patterns to watch

### CodeQL language detection

If CodeQL fails because a repo has no supported source code yet, classify as:

```text
Language detection / workflow configuration
```

Do not automatically classify it as a true vulnerability.

### Dependabot ecosystem missing files

If Dependabot checks npm or pip in a repo without `package.json` or `requirements.txt`, classify as:

```text
Workflow configuration / repository classification
```

Potential fix:

- Use repo-specific Dependabot configs.
- Add conditional documentation.
- Remove unsupported ecosystems until source exists.

### Permissions failures

If dependency review, CodeQL, or SARIF upload fails due to permission, classify as:

```text
Permissions failure
```

Potential fix:

- Add least-privilege permissions needed for that workflow.
- Avoid exposing secrets in PRs from forks.

## Security R&D backlog

- [ ] Conditional security workflow based on repo language.
- [ ] Docs-only repo security workflow.
- [ ] Fleet security status automation.
- [ ] RiskGate decision log.
- [ ] Pull request template with security checklist.
- [ ] Link/QR/affiliate disclosure audit checklist.
- [ ] Bot prompt safety scanner concept.
- [ ] CRM data minimization audit.
- [ ] Public claims compliance audit.
- [ ] Security scorecard per repo.

## Next best moves

1. Review new Actions runs in Phase 1 repos.
2. Categorize failures using taxonomy.
3. Adjust CodeQL strategy if repos are docs-only.
4. Start Phase 2 rollout.
5. Update this file weekly.
