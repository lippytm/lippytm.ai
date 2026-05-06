# Data Classification and Database Security

## Purpose

Define how data should be classified, protected, documented, and handled across lippytm repositories, websites, CRM systems, bots, databases, and business platforms.

## Data classes

### Public

Examples:

- Public README files.
- Public roadmap files.
- Published website copy.
- Canva prompts without private information.
- Public social posts.

Handling:

- Safe to publish.
- Still review for accuracy and compliance.

### Internal

Examples:

- Draft strategy documents.
- Internal campaign notes.
- Non-sensitive performance logs.
- Internal task checklists.

Handling:

- Do not publish unless reviewed.
- Keep in controlled repos or private systems when necessary.

### Confidential

Examples:

- Lead/contact information.
- CRM exports.
- Business financial details.
- Unpublished partnership terms.
- Customer/project notes.

Handling:

- Do not commit to public GitHub repos.
- Store only where access is controlled.
- Limit access.
- Protect exports.

### Restricted / High Risk

Examples:

- Passwords.
- API keys.
- Tokens.
- Private keys.
- `.env` files.
- Payment credentials.
- Bank/SSN/tax documents.
- Database credentials.
- Private customer records.

Handling:

- Never commit to GitHub.
- Rotate immediately if exposed.
- Use secure secret storage.
- Restrict access to only what is necessary.

## Database security principles

- Collect the minimum data needed.
- Avoid storing sensitive financial/private data unless required and protected.
- Separate public content from private lead/customer data.
- Use least privilege database users.
- Back up important data securely.
- Do not commit database dumps.
- Do not use real customer data in test fixtures.
- Redact logs and screenshots before publishing.

## CRM data handling

CRM records may include:

- Name.
- Email/contact.
- Business/project.
- Source platform.
- Interest tag.
- Follow-up notes.

Do not store unnecessary sensitive details. If a lead needs funding, tax, legal, or financial support, route carefully and avoid collecting private documents through insecure channels.

## Bot data handling

Bots should not ask for:

- Passwords.
- Banking credentials.
- SSNs.
- Full payment information.
- Private keys.
- Sensitive legal/tax documents.

Bots may ask for:

- Business name.
- Contact info.
- General business need.
- Preferred next step.
- Non-sensitive workflow information.

## Canva/social data handling

Before publishing graphics:

- Check screenshots for private data.
- Hide emails, tokens, dashboard IDs, invoices, CRM leads, and private messages.
- Use mock/demo data where possible.

## Incident rule

If restricted data is exposed:

1. Remove exposure.
2. Rotate secrets if applicable.
3. Notify necessary stakeholders if applicable.
4. Document the issue.
5. Add prevention controls.
