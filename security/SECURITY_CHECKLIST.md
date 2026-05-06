# Security Checklist

## Purpose

Use this checklist before publishing, deploying, connecting CRM, adding bots, changing workflows, or expanding repository automation.

## Repository checklist

- [ ] `SECURITY.md` exists.
- [ ] `QUALITY.md` exists or security is included in the quality checklist.
- [ ] Dependabot is configured.
- [ ] Code scanning is configured where supported.
- [ ] Dependency review is configured for pull requests.
- [ ] No secrets are committed.
- [ ] No `.env` files are committed.
- [ ] No private lead/customer lists are committed.
- [ ] No database dumps are committed.
- [ ] README explains security-sensitive areas.

## GitHub Actions checklist

- [ ] Workflow permissions use least privilege.
- [ ] Pull request workflows do not expose secrets to untrusted code.
- [ ] Third-party actions are trusted and preferably pinned or reviewed.
- [ ] Deployment workflows require review when appropriate.
- [ ] High-risk automation has human approval.

## Dependency checklist

- [ ] New dependencies are necessary.
- [ ] Dependency reputation is reviewed.
- [ ] Licenses are acceptable for the project.
- [ ] High/critical vulnerabilities are reviewed.
- [ ] Major upgrades are tested before merge.

## Website checklist

- [ ] HTTPS is enabled.
- [ ] Forms collect only necessary data.
- [ ] Contact forms do not request sensitive financial/private data unnecessarily.
- [ ] Public claims are safe and supportable.
- [ ] Affiliate disclosures are visible where needed.
- [ ] No guaranteed funding, income, approval, tax, legal, cybersecurity, or investment claims.

## CRM and lead data checklist

- [ ] CRM access is limited.
- [ ] Leads are tagged by source.
- [ ] Sensitive data is minimized.
- [ ] Data exports are protected.
- [ ] Retention/deletion practices are documented.
- [ ] Private lead data is not committed to GitHub.

## Bot and AI automation checklist

- [ ] Bot has clear job and boundaries.
- [ ] Human handoff exists.
- [ ] Bot does not collect unnecessary sensitive data.
- [ ] Bot follow-up messages are reviewed.
- [ ] AI does not receive secrets or private data unless explicitly approved and safe.
- [ ] Autonomous actions require approval when high risk.

## Database checklist

- [ ] Database credentials are stored securely.
- [ ] Database access uses least privilege.
- [ ] Sensitive fields are identified.
- [ ] Backups are protected.
- [ ] Logs do not expose sensitive data.
- [ ] Test data is not real private customer data.

## Canva/social checklist

- [ ] Public designs do not include private data.
- [ ] QR codes point to official pages.
- [ ] Affiliate claims include disclosure where needed.
- [ ] Screenshots do not expose private dashboards, API keys, emails, or CRM data.
- [ ] Brand assets reduce impersonation risk by using consistent naming and links.

## Weekly review

Every week:

- [ ] Review Dependabot alerts.
- [ ] Review failed security workflows.
- [ ] Review open security issues.
- [ ] Check if any secrets were accidentally exposed.
- [ ] Review new CRM/bot/website data handling.
- [ ] Update security documentation if needed.

## Quality principle

Security is part of quality. If a change is not secure, documented, and reviewable, it is not ready.
