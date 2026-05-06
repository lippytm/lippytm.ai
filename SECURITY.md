# Security Policy

## Mission

Quality and Quality Assurance is Job #1. Security is a foundation of quality, transparency, documentation, database management, automation, and trust.

## Supported security scope

This repository is part of the lippytm.ai Business of Businesses ecosystem. Security review applies to:

- GitHub repository content.
- Website and roadmap copy.
- Canva prompt and design workflows.
- CRM and lead routing plans.
- Bot and AI automation workflows.
- Affiliate and public-facing business claims.
- Future code, scripts, workflows, and deployments.

## Reporting a security issue

Do not post secrets, credentials, private customer data, or exploit details in a public issue.

For now, create a private note for the repository owner or use GitHub private vulnerability reporting if available in the repository settings.

If a public issue is necessary, describe the general risk without exposing exploit details or secrets.

## High-risk items

Treat the following as high risk:

- API keys, tokens, passwords, private keys, `.env` files.
- Authentication or authorization changes.
- Payment, wallet, or financial data workflows.
- CRM exports or private lead/customer information.
- Database schemas storing personal data.
- Workflow or deployment credential changes.
- Autonomous actions that publish, message, deploy, or modify external systems.

## Security rules

- Never commit secrets.
- Never commit private lead/customer lists.
- Never commit database dumps containing personal information.
- Use least privilege access.
- Use MFA on important accounts.
- Review dependencies before trusting them.
- Keep public claims safe, documented, and supportable.
- Include human review for high-risk automation.

## Security automation goals

- Dependabot enabled.
- CodeQL scanning enabled where supported.
- Dependency review enabled on pull requests.
- Secret scanning awareness and checklist.
- Security issue template.
- Quality checklist tied to security review.

## Incident response

If a security problem is found:

1. Stop the exposure.
2. Remove or protect sensitive data.
3. Rotate affected secrets.
4. Patch the root cause.
5. Document the issue.
6. Add a prevention checklist.
7. Improve automation so it is less likely to happen again.

## Public claims and compliance

Avoid guaranteed funding, income, approval, tax, legal, investment, cybersecurity, or business outcomes unless properly supported and reviewed. Use disclaimers and professional referrals where appropriate.
