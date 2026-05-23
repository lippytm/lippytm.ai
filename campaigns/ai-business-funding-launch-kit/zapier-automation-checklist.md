# Zapier Automation Checklist — Business of Businesses

## Purpose

Use Zapier as the connection layer for LippytmAI and the Business of Businesses, especially where leads, tasks, notifications, GitHub issues, campaign logs, and sales follow-ups need to move between apps.

## Core Zapier principles

- One Zap should have one clear business purpose.
- Start simple before creating complex multi-step automation.
- Test every automation with sample data.
- Avoid sending sensitive financial, legal, or personal data to unnecessary tools.
- Name Zaps clearly so their purpose is obvious.
- Keep a written log in GitHub or Zo for every active Zap.
- Include a failure/retry process.
- Do not make guarantees of funding, income, approval, or success in automated messages.

## Recommended Zap naming system

```text
[Business Area] Trigger → Outcome
```

Examples:

```text
GetBizFunds Lead → CRM + Notification + GitHub Issue
AI Funding eBook Signup → Delivery Email + Campaign Log
GitHub Campaign Issue → Task Tracker + Canva Reminder
Published Article Commit → Social Repurposing Queue
```

## Zap 1 — GetBizFunds Lead Follow-up

### Business purpose

Turn business funding interest into organized follow-up.

### Trigger

New lead or form submission from the funding site or connected form system.

### Actions

1. Add/update lead in CRM or spreadsheet.
2. Send notification to Charles.
3. Create GitHub issue in the relevant repo.
4. Add campaign source tag.
5. Send approved follow-up email if an email tool is connected.

### Suggested fields

- Name.
- Email.
- Phone.
- Business name.
- Funding need.
- Approximate amount requested.
- Timeframe.
- Source page.
- Consent/status.

### Failure handling

- If CRM update fails, send alert.
- If email is missing, create a review task instead of sending follow-up.
- If duplicate lead is detected, update existing record rather than creating another one.

## Zap 2 — AI Funding eBook Signup

### Business purpose

Deliver the eBook and segment people interested in AI automation/business funding.

### Trigger

New eBook signup, buyer, or form submission.

### Actions

1. Add contact to CRM/spreadsheet.
2. Tag as `AI Business Funding Launch Kit`.
3. Send eBook delivery or next-step email.
4. Add row to campaign performance tracker.
5. Create reminder for follow-up offer.

### Follow-up offer ideas

- Business Funding Readiness Review.
- AI Automation Starter Plan.
- Website + Funnel Improvement Review.
- Affiliate Marketing Platform Starter Session.
- Zapier Business Automation Setup.

## Zap 3 — GitHub Campaign Issue to Task System

### Business purpose

Make sure GitHub planning becomes action.

### Trigger

New GitHub issue with label `campaign`, `revenue`, `ebook`, `zapier`, or `ai-coding`.

### Actions

1. Add task to preferred task tracker.
2. Add row to campaign log.
3. Notify Charles.
4. Add due date or review reminder.

## Zap 4 — Published GitHub Content to Repurposing Queue

### Business purpose

Turn every new article/eBook/campaign file into more marketing assets.

### Trigger

New GitHub commit touching:

- `/articles`
- `/campaigns`
- `/ebooks`
- `/docs`

### Actions

1. Add item to content repurposing queue.
2. Create Canva reminder.
3. Create social post task.
4. Add URL/commit to tracking sheet.

## Zap 5 — Canva Export to Publishing Queue

### Business purpose

Move Canva graphics into publishing workflows.

### Trigger

New approved Canva export or manual upload to a watched folder.

### Actions

1. Add asset to campaign tracker.
2. Notify Charles.
3. Create GitHub issue to mirror asset if needed.
4. Create social scheduling task.

## Zap 6 — AI Coding Request Intake

### Business purpose

Capture coding ideas from forms, ChatGPT Business summaries, or business planning sessions.

### Trigger

New coding idea submitted through a form or added to a tracker.

### Actions

1. Create GitHub issue.
2. Add label `ai-coding`.
3. Add business value and revenue lane fields.
4. Notify Charles.
5. Add review task for Zo implementation.

## Active Zap register template

```md
# Zap Register Entry

## Zap name

## Business purpose

## Trigger

## Actions

## Apps connected

## Data fields used

## Owner

## Test result

## Failure handling

## Last reviewed
```

## Best first implementation order

1. AI Funding eBook Signup → Delivery/Log.
2. GetBizFunds Lead → CRM/Notification/Issue.
3. GitHub Campaign Issue → Task/Reminder.
4. Published GitHub Content → Repurposing Queue.
5. AI Coding Request → GitHub Issue.
