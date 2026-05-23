# Zapier-Ready Lead Automation Template

## Template name

GetBizFunds + AI Funding eBook Lead → CRM Log + Email Follow-Up + GitHub Issue + Charles Notification

## Business purpose

Capture leads from `https://lippytmai.getbizfunds.com` and the AI Business Funding eBook funnel, organize them for follow-up, create a durable GitHub task trail, notify Charles, and route each lead into the right Business of Businesses path.

This is the first practical automation template for the LippytmAI revenue system.

## Recommended first version

Start with a simple, auditable Zap that does five things:

1. Receives a new lead.
2. Adds or updates the lead in a spreadsheet or CRM.
3. Classifies the lead by interest, stage, and urgency.
4. Sends a plain-language follow-up or eBook delivery email.
5. Creates a GitHub issue for manual review and next action.

Do not start with an overly complex automation. A reliable simple Zap is better than a fragile advanced Zap.

---

# Zap architecture

## Trigger options

Choose the trigger that matches the current form system.

### Option A — Webhooks by Zapier

Use this if `lippytmai.getbizfunds.com` can POST form submissions to a webhook.

- Trigger app: Webhooks by Zapier
- Trigger event: Catch Hook
- Best for: custom site forms, direct POSTs, future Zo API routes

### Option B — Zapier Interfaces / Zapier Forms

Use this if you want a fast Zapier-native lead form.

- Trigger app: Zapier Interfaces or Zapier Forms
- Trigger event: New Form Submission
- Best for: quick testing before custom site integration

### Option C — Google Forms / Typeform / Tally / Fillout

Use this if the form provider already exists.

- Trigger app: selected form app
- Trigger event: New Submission
- Best for: no-code lead capture

## Recommended starting trigger

Use **Zapier Interfaces or Webhooks by Zapier**.

- If the site form is ready: use Webhooks by Zapier.
- If the site form is not ready: use Zapier Interfaces for quick deployment.

---

# Input field schema

## Essential lead fields

| Field | Type | Required | Notes |
|---|---:|---:|---|
| `full_name` | text | yes | Person submitting the form |
| `email` | email | yes | Required for eBook delivery and follow-up |
| `phone` | phone | optional | Useful for high-intent funding leads |
| `business_name` | text | recommended | Company or project name |
| `website_or_social` | URL/text | optional | Website, LinkedIn, Facebook page, etc. |
| `primary_interest` | dropdown | yes | Main routing field |
| `funding_amount_range` | dropdown | conditional | Use for funding leads |
| `business_stage` | dropdown | recommended | Idea, startup, active, growing, established |
| `urgency` | dropdown | recommended | urgent, high, normal, low |
| `short_description` | long text | yes | Short context for review |
| `source_page` | URL/text | yes | Landing page or form page |
| `campaign_source` | text | recommended | Example: `ai_business_funding_ebook` |
| `consent_to_contact` | boolean | yes | Must be true before follow-up messaging |
| `created_at` | datetime | yes | Use Zapier timestamp if absent |

## Primary interest values

Use these exact values so routing stays clean:

- `business_funding_help`
- `ai_business_setup`
- `automation_services`
- `strategy_and_planning`
- `affiliate_partner_interest`
- `ai_business_funding_ebook`
- `general_question`

## Funding amount range values

- `under_25k`
- `25k_100k`
- `100k_500k`
- `500k_plus`
- `not_sure`

## Business stage values

- `idea_stage`
- `startup_stage`
- `active_business`
- `growing_business`
- `established_business`

## Urgency values

- `urgent`
- `high`
- `normal`
- `low`

---

# Zap steps

## Step 1 — Trigger: New lead submitted

Capture the lead from the form or webhook.

### Test payload

```json
{
  "full_name": "Sample Founder",
  "email": "founder@example.com",
  "phone": "555-555-0100",
  "business_name": "Sample Robotics Company",
  "website_or_social": "https://example.com",
  "primary_interest": "ai_business_funding_ebook",
  "funding_amount_range": "100k_500k",
  "business_stage": "active_business",
  "urgency": "high",
  "short_description": "We want funding to improve AI automation, marketing, and equipment planning.",
  "source_page": "https://lippytmai.zo.space/ebook/ai-business-funding-launch-kit",
  "campaign_source": "ai_business_funding_launch_kit",
  "consent_to_contact": true,
  "created_at": "{{zap_meta_human_now}}"
}
```

## Step 2 — Filter: require usable consent and email

Continue only if:

- `email` exists
- `consent_to_contact` is true

If the email is missing but the lead has other contact information, create a manual-review issue instead of sending automated email.

## Step 3 — Formatter: normalize fields

Recommended Formatter steps:

- Lowercase and trim email.
- Trim full name and business name.
- Convert blank values to `not_provided`.
- Ensure source page and campaign source are preserved.
- Convert urgency to one of the approved values.

## Step 4 — Paths by Zapier: route lead type

Create paths based on `primary_interest`.

### Path A — AI Business Funding eBook

Condition:

- `primary_interest` equals `ai_business_funding_ebook`

Actions:

1. Add/update CRM or spreadsheet row.
2. Send eBook delivery email.
3. Create GitHub issue with label `ebook-lead`.
4. Notify Charles.
5. Add follow-up reminder.

### Path B — Business Funding Help

Condition:

- `primary_interest` equals `business_funding_help`

Actions:

1. Add/update CRM or spreadsheet row.
2. Send funding-readiness follow-up email.
3. Create GitHub issue with label `funding-lead`.
4. Notify Charles as higher priority.
5. Add follow-up reminder.

### Path C — AI / Automation / Strategy

Condition:

- `primary_interest` is `ai_business_setup`, `automation_services`, or `strategy_and_planning`

Actions:

1. Add/update CRM or spreadsheet row.
2. Send discovery follow-up email.
3. Create GitHub issue with label `strategy-lead` or `automation-lead`.
4. Notify Charles.

### Path D — Partner / Affiliate

Condition:

- `primary_interest` equals `affiliate_partner_interest`

Actions:

1. Add/update CRM or spreadsheet row.
2. Send partner-interest confirmation.
3. Create GitHub issue with label `partner-lead`.
4. Add to partner review queue.

### Path E — General / unclear

Condition:

- `primary_interest` equals `general_question` or missing/unclear value

Actions:

1. Add/update CRM or spreadsheet row.
2. Create GitHub issue with label `manual-review`.
3. Send short confirmation if consent exists.

---

# CRM or spreadsheet schema

Create a table named:

```text
Business of Businesses Lead Log
```

## Columns

| Column | Purpose |
|---|---|
| `lead_id` | Unique ID generated by Zapier or spreadsheet formula |
| `created_at` | Submission time |
| `full_name` | Lead name |
| `email` | Lead email |
| `phone` | Lead phone |
| `business_name` | Company/project name |
| `website_or_social` | Public business link |
| `primary_interest` | Main routing category |
| `funding_amount_range` | Funding range, if applicable |
| `business_stage` | Business maturity |
| `urgency` | Follow-up priority |
| `short_description` | Lead context |
| `source_page` | Page where lead came from |
| `campaign_source` | Campaign attribution |
| `lead_stage` | Start with `new_lead` |
| `priority_band` | urgent/high/normal/low |
| `next_action` | Recommended next action |
| `github_issue_url` | GitHub task link |
| `email_sent` | yes/no |
| `last_touch_at` | Last follow-up time |
| `notes` | Manual notes |

## Default values

- `lead_stage`: `new_lead`
- `next_action`: `review_and_follow_up`
- `email_sent`: `no` until delivery succeeds

---

# Priority model

## Urgent

Use when:

- urgency is `urgent`
- funding amount is `500k_plus`
- short description indicates an immediate deadline
- lead is already an active business and requests funding or strategy help

## High

Use when:

- urgency is `high`
- funding amount is `100k_500k`
- business stage is `active_business`, `growing_business`, or `established_business`
- interest is funding, automation, or strategy

## Normal

Use when:

- urgency is `normal`
- eBook signup has no immediate funding request
- lead needs education before action

## Low

Use when:

- urgency is `low`
- business is in idea stage
- contact is incomplete
- request is unclear

---

# GitHub issue template

Create issues in one of these repositories:

- Preferred direct funding repo: `lippytm/lippytmai.getbizfunds.com-`
- Campaign/content repo: `lippytm/lippytm.ai`

## Issue title format

```text
[Lead] {{primary_interest}} — {{business_name}} — {{full_name}}
```

## Issue body template

```md
# New Business of Businesses Lead

## Lead summary
- Name: {{full_name}}
- Email: {{email}}
- Phone: {{phone}}
- Business: {{business_name}}
- Website/social: {{website_or_social}}

## Routing
- Primary interest: {{primary_interest}}
- Funding range: {{funding_amount_range}}
- Business stage: {{business_stage}}
- Urgency: {{urgency}}
- Priority band: {{priority_band}}
- Lead stage: new_lead
- Recommended next action: {{next_action}}

## Source
- Source page: {{source_page}}
- Campaign source: {{campaign_source}}
- Submitted: {{created_at}}

## Description
{{short_description}}

## Checklist
- [ ] Confirm contact details
- [ ] Review source/campaign context
- [ ] Decide funding, automation, strategy, partner, or nurture path
- [ ] Send next manual follow-up if needed
- [ ] Update lead log

## Compliance notes
Do not promise funding approval, income, investment returns, tax results, legal outcomes, or guaranteed success. Use educational and referral-safe language.
```

## Recommended issue labels

Use one or more:

- `lead`
- `funding-lead`
- `ebook-lead`
- `automation-lead`
- `strategy-lead`
- `partner-lead`
- `manual-review`
- `urgent-followup`
- `revenue`
- `zapier`

---

# Email templates

## Email 1 — eBook delivery

Subject:

```text
Your AI Business Funding Launch Kit
```

Body:

```text
Hi {{full_name}},

Thank you for requesting the AI Business Funding Launch Kit.

The guide is designed to help you think clearly about business funding, AI automation, marketing systems, and responsible growth planning.

Start here:
https://lippytmai.zo.space/ebook/ai-business-funding-launch-kit

If you are exploring funding, prepare these first:

1. What the funding would be used for
2. Your business stage
3. Your estimated funding range
4. Your current revenue or growth context
5. Your next practical business goal

You can also visit the funding site here:
https://lippytmai.getbizfunds.com

Important note: this information is educational and does not guarantee funding approval, income, or business results.

Best,
Charles Lipshay / LippytmAI
```

## Email 2 — funding lead confirmation

Subject:

```text
Your business funding request was received
```

Body:

```text
Hi {{full_name}},

Thank you for reaching out about business funding.

Your request has been received and will be reviewed based on your business stage, funding goal, timeline, and readiness.

To prepare for the next step, please gather:

1. Basic business information
2. Approximate funding amount needed
3. Intended use of funds
4. Business revenue or operating history, if available
5. Any urgent deadlines

You can revisit the funding site here:
https://lippytmai.getbizfunds.com

Important note: submitting information does not guarantee funding approval, terms, or results. The next step is to review fit, readiness, and available options.

Best,
Charles Lipshay / LippytmAI
```

## Email 3 — automation / strategy confirmation

Subject:

```text
Your AI automation and business systems request was received
```

Body:

```text
Hi {{full_name}},

Thank you for reaching out about AI automation, strategy, or business systems.

Your request has been received. The next step is to understand what you want to improve first: lead capture, follow-up, content creation, website conversion, AI coding, or workflow automation.

You can review the AI Coding and Automation Command Center here:
https://lippytmai.zo.space/ai-coding-automation-command-center

Important note: this process is educational and strategic. Specific business, income, funding, or technical outcomes are not guaranteed.

Best,
Charles Lipshay / LippytmAI
```

---

# Notification to Charles

Use SMS, email, or Zapier notification.

## Notification message template

```text
New Business of Businesses lead: {{full_name}} / {{business_name}}
Interest: {{primary_interest}}
Priority: {{priority_band}}
Source: {{campaign_source}}
Next action: {{next_action}}
GitHub issue: {{github_issue_url}}
```

---

# Follow-up timing

## Suggested sequence

- Immediate: confirmation or eBook delivery
- Day 1: practical readiness checklist
- Day 3: funding/automation education message
- Day 7: invite to next step or strategy review
- Day 14: nurture message with article, video, or related offer

## Suggested next-step offers

- Business Funding Readiness Review
- AI Automation Starter Plan
- Website + Funnel Improvement Review
- Affiliate Marketing Platform Starter Session
- Zapier Business Automation Setup
- Programming / Blockchain / Robotics Business Builder Track

---

# Testing checklist

Before turning on the Zap:

- [ ] Submit one sample eBook lead.
- [ ] Submit one sample funding lead.
- [ ] Submit one sample automation lead.
- [ ] Confirm spreadsheet/CRM row is created.
- [ ] Confirm duplicate email updates existing lead if possible.
- [ ] Confirm GitHub issue is created in the right repo.
- [ ] Confirm labels are applied.
- [ ] Confirm email copy is accurate and compliant.
- [ ] Confirm Charles receives a notification.
- [ ] Confirm no unnecessary sensitive data is sent to tools that do not need it.

---

# Compliance and best-practice guardrails

- Do not guarantee funding approval.
- Do not guarantee income or business results.
- Do not provide legal, tax, or investment advice in automated emails.
- Keep financial language educational and referral-safe.
- Preserve consent status.
- Do not over-collect sensitive information in first-touch forms.
- Keep automations simple enough to audit.
- Log every active Zap in GitHub or Zo.

---

# Version 2 improvements

After the first version works, add:

1. Lead scoring.
2. Deduplication by email.
3. Source tracking by article, eBook, video, or ad campaign.
4. Separate nurture sequences by interest.
5. Weekly performance summary.
6. Canva asset task creation.
7. GitHub campaign issue auto-linking.
8. Zap failure alerting.
9. AI-generated lead summary for manual review.
10. CRM lifecycle stage updates.
