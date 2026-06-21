# AI Business Funding Launch Kit Lead-Capture Implementation Plan

## Purpose

Create the next safe revenue step for the AI Business Funding Launch Kit: a measured lead-capture and download path that connects public interest to the Business of Businesses follow-up workflow without overpromising funding, income, legal, tax, or investment outcomes.

## Recommended approach

Use a staged, approval-gated rollout.

1. **Draft and validate the form fields** in this document and the existing Zapier lead automation template.
2. **Create or approve the first form endpoint** using Zapier Interfaces, a no-code form, or a secured custom route.
3. **Connect the form to the lead log** using the existing `Workflows/Zapier Lead Automation/business-of-businesses-lead-log-template.csv` schema.
4. **Send only consent-based follow-up** and keep any third-party outreach manual until approved.
5. **Measure conversions** before expanding public copy, paid traffic, or high-frequency automations.

## Current assets already available

- Public launch page: `https://lippytmai.zo.space/ai-business-funding-launch-kit`
- Public eBook page: `https://lippytmai.zo.space/ebook/ai-business-funding-launch-kit`
- Funding destination: `https://lippytmai.getbizfunds.com`
- Zapier template: `Workflows/Zapier Lead Automation/getbizfunds-ai-ebook-lead-automation-template.md`
- Lead log schema: `Workflows/Zapier Lead Automation/business-of-businesses-lead-log-template.csv`
- GitHub issue template: `Workflows/Zapier Lead Automation/github-lead-issue-template.md`
- Sales copy: `Ebooks/AI Business Funding Launch Kit/sales-page-copy.md`

## Minimum viable form fields

Use the smallest set that supports routing and compliance.

| Field | Required | Purpose |
|---|---:|---|
| `full_name` | yes | Identify the lead. |
| `email` | yes | Deliver the launch kit and follow up with consent. |
| `business_name` | recommended | Understand business context. |
| `primary_interest` | yes | Route to funding, eBook, automation, strategy, affiliate, or general queue. |
| `funding_amount_range` | conditional | Only ask when the lead requests business funding help. |
| `business_stage` | recommended | Segment readiness. |
| `urgency` | recommended | Prioritize manual review. |
| `short_description` | yes | Capture useful context without over-collecting private data. |
| `source_page` | yes | Attribute the conversion. |
| `campaign_source` | yes | Track campaign performance. |
| `consent_to_contact` | yes | Required before any automated follow-up. |

## Required public disclaimer language

Use educational and referral-safe language near the form CTA:

> The AI Business Funding Launch Kit is educational business-planning material. LippytmAI does not guarantee funding approval, income, profit, investment results, legal outcomes, or tax outcomes. If you submit your information, you consent to be contacted about the resource or business-growth path you selected. Affiliate or referral relationships may apply where disclosed.

## Recommended CTA structure

### Primary CTA

> Get the AI Business Funding Launch Kit

### Secondary CTA

> Explore business funding options through LippytmAI GetBizFunds

### Manual-review CTA

> Request a business growth and automation review

## Zapier routing design

### Path A — eBook lead

Trigger when `primary_interest = ai_business_funding_ebook`.

Actions:

1. Add or update lead log row.
2. Send educational launch-kit delivery email if `consent_to_contact = true`.
3. Create GitHub issue labeled `ebook-lead`.
4. Notify Charles with a concise internal summary.

### Path B — business funding help

Trigger when `primary_interest = business_funding_help`.

Actions:

1. Add or update lead log row.
2. Send funding-readiness next-step email if consent exists.
3. Create GitHub issue labeled `funding-lead` and `manual-review`.
4. Notify Charles as higher priority.
5. Do not promise approval or contact third parties automatically.

### Path C — AI automation or strategy

Trigger when `primary_interest` is `ai_business_setup`, `automation_services`, or `strategy_and_planning`.

Actions:

1. Add or update lead log row.
2. Send discovery follow-up if consent exists.
3. Create GitHub issue labeled `automation-lead` or `strategy-lead`.
4. Keep paid-service terms manual until approved.

### Path D — affiliate or partner interest

Trigger when `primary_interest = affiliate_partner_interest`.

Actions:

1. Add or update lead log row.
2. Create manual-review issue.
3. Do not publish partnership claims or send partner terms automatically.

## Approval gates

Charles approval is required before any of these actions:

- editing live lead forms on `lippytmai.getbizfunds.com`;
- activating or changing production Zapier automations;
- sending external messages beyond consent-based eBook delivery or confirmation copy that Charles has approved;
- adding payment, checkout, subscription, wallet, or affiliate payout flows;
- publishing stronger funding, income, investment, legal, or tax claims;
- sharing lead data with third parties.

## Observability metrics

Track these weekly after launch:

| Metric | Target use |
|---|---|
| Landing page visits | Know if traffic exists. |
| Form starts | Detect interest and friction. |
| Form completions | Measure conversion. |
| Consent rate | Ensure follow-up legality and trust. |
| Primary interest split | Decide which revenue lane is strongest. |
| GitHub issues created | Preserve follow-up audit trail. |
| Manual follow-ups completed | Measure operational throughput. |
| Funding CTA clicks | Measure GetBizFunds routing. |

## Red-team notes

- Avoid collecting sensitive financial records in the first form.
- Do not ask for Social Security numbers, bank credentials, tax returns, or private documents through this lead form.
- Make funding content educational and planning-oriented unless reviewed by qualified professionals.
- Use affiliate disclosure where partner or tool recommendations may generate compensation.
- Store secrets only in Zo Settings, not in files, ChatGPT prompts, GitHub, screenshots, or public pages.

## Rollback plan

- If using Zapier Interfaces or another no-code form, disable the form or turn off the Zap.
- If a Zo Space route is updated later, use route history to undo the change.
- If a GitHub issue template is changed, revert the commit or restore the prior file.
- If lead logging is noisy, pause automation and keep manual review only.

## Next safest build step

Create a draft form copy section and field map for Charles to approve before editing any public page or production automation.

## Proposed draft form copy

### Section headline

Get the AI Business Funding Launch Kit

### Supporting copy

Use the launch kit to organize your business funding plan, AI automation ideas, marketing priorities, and growth next steps. Choose the path that best fits your current goal so LippytmAI can route your request correctly.

### Field helper text

- **Primary interest:** Choose the closest reason you are here.
- **Funding amount range:** Estimate only; this does not represent approval, eligibility, or an offer.
- **Short description:** Share the business goal, project, or automation challenge you want to organize.

### Consent copy

By submitting, you agree that LippytmAI may contact you about the launch kit or selected business-growth path. This is educational and referral-oriented information, not a guarantee of funding, income, profit, investment results, legal outcomes, or tax outcomes.
