# Failed Run Review Taxonomy

Purpose: categorize every failed GitHub Actions/security run so failures become a security improvement system instead of random noise.

## Important note

This taxonomy is the review framework. To classify historical failed runs with full precision, each failed run needs the workflow name, job log, run URL, commit SHA, and error text. If those logs are not available through automation, review them from the GitHub Actions tab and record them here or in a security-risk issue.

## Failure categories

### 1. Workflow configuration failure

Common signs:

- YAML syntax error.
- Invalid workflow trigger.
- Wrong file path.
- Missing action input.
- Unsupported matrix value.
- Workflow references a missing branch.
- Workflow references a missing package file.

Examples:

- CodeQL runs for Python when no Python files exist.
- npm audit runs when no `package.json` exists.
- pip audit runs when no `requirements.txt` exists.

Fix:

- Adjust triggers.
- Add path detection.
- Split workflows by ecosystem.
- Use conditional steps.
- Document why workflow applies.

### 2. Permissions failure

Common signs:

- `Resource not accessible by integration`.
- `security-events: write` permission missing.
- Dependency review cannot comment.
- Workflow cannot upload SARIF.
- Pull request from fork cannot access required permissions.

Fix:

- Set least-privilege `permissions:` block.
- Use correct permissions for CodeQL and dependency review.
- Avoid exposing secrets to untrusted PRs.
- Use human review for high-risk workflows.

### 3. Dependency failure

Common signs:

- Vulnerable npm/pip package.
- Dependabot alert.
- Dependency review fails on high severity.
- Package install fails due to lockfile mismatch.
- Deprecated package.

Fix:

- Update dependency.
- Remove unused dependency.
- Add lockfile hygiene.
- Review major upgrades manually.
- Track high/critical alerts as security-risk issues.

### 4. Language detection failure

Common signs:

- CodeQL language not found.
- Autobuild fails because repo is docs-only.
- Python or JavaScript analysis runs on a repo without that language.
- Generated/empty repo produces no source to scan.

Fix:

- Add language-specific workflows only where needed.
- Add repo classification.
- Use docs/security-only workflows for documentation repos.
- Add conditional scan notes.

### 5. True vulnerability

Common signs:

- CodeQL identifies injection, XSS, path traversal, hardcoded secret, unsafe deserialization, weak crypto, or auth flaw.
- Secret scanning identifies exposed token/key.
- Dependency review identifies exploitable high/critical package.
- Manual review finds private data exposure.

Fix:

- Create security-risk issue.
- Patch root cause.
- Rotate secrets if needed.
- Add regression checklist.
- Document incident if exposure occurred.

### 6. Quality/compliance failure

Common signs:

- Public copy includes guaranteed funding, income, legal, tax, investment, or cybersecurity outcome claims.
- Affiliate disclosure missing.
- CRM/bot copy asks for too much private information.
- Documentation conflicts with safety/security rules.

Fix:

- Rewrite claim.
- Add disclaimer.
- Reduce data collected.
- Add review gate.

## Review table

| Date | Repo | Workflow | Run URL | Category | Severity | Root Cause | Fix | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  | Workflow configuration / Permissions / Dependency / Language detection / True vulnerability / Quality-compliance |  |  |  |  |

## Review process

1. Open failed run in GitHub Actions.
2. Copy workflow name, job name, run URL, and failing error text.
3. Assign one category from this file.
4. If true vulnerability or private data exposure, create a `Security Risk` issue.
5. Fix the root cause.
6. Re-run failed job.
7. Add prevention checklist.
8. Record result in the review table.

## Best practice

Do not treat failed runs as only technical problems. A failed security run is a signal to improve quality, documentation, workflow design, and repository classification.
