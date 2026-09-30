# Jarvis First Customer Package

**Status:** Proposed pilot offer for discovery and scoping. No price, integration availability, or performance outcome is promised by this document.

## Pilot offer

**Working name:** Lead Response and Booking Workflow Pilot.

**Outcome to validate:** a small business can capture an inquiry, collect agreed qualification details and consent, prepare or send an approved follow-up, and route a booking request to a calendar or human.

### Included

- One business, one workflow, one lead source/channel, one follow-up channel, and one booking destination.
- Up to three integrations, only if each is available, authorized, tested, and in the written scope.
- Qualification rubric and human review/handoff path.
- Test plan, failure/fallback steps, operator/customer walkthrough, and a written findings summary.
- Pilot period: `[start date]` to `[end date]`, agreed in writing.

### Excluded unless separately scoped

- Guaranteed leads, appointments, revenue, savings, accuracy, or response time.
- Unverified integrations, bulk outreach, automated financial transactions, or unattended external messaging.
- Regulated decisions/advice, complex multi-tenant SaaS deployment, 24/7 support, and custom model training.
- Data migration, phone/SMS/carrier charges, third-party subscription fees, or legal/compliance certification.

### Pricing placeholders

Use `[discovery fee]`, `[pilot setup fee]`, `[optional support fee]`, `[currency]`, `[payment schedule]`, and `[refund/cancellation terms]` until approved. Provide a written estimate only after discovery and cost/scope review. Third-party charges are separately identified. Do not publish a placeholder as a live price.

## Discovery questions

1. What type of inquiry is most valuable, and what makes it qualified?
2. Where do inquiries currently arrive, who responds, and what is the current delay/workaround?
3. What follow-up messages are permitted, through which channel, and how is consent/opt-out recorded?
4. What details are strictly necessary to qualify the request? What must never be collected?
5. Which CRM, inbox, or form is already used? Who owns it and can authorize access?
6. Which calendar/booking destination is authoritative? What appointment types and availability rules apply?
7. Which cases require a person immediately, and who is the handoff owner/backup?
8. How will success be measured against a baseline? What sample size and review window are reasonable?
9. What data retention, deletion, access, security, and vendor requirements apply?
10. What budget, decision process, deadlines, support expectations, and excluded work should be documented?

## Onboarding checklist

- [ ] Confirm fit, customer decision-maker, authorized account owner, written scope, price, dates, and exclusions.
- [ ] Identify lawful/appropriate basis and consent wording for collection and follow-up; obtain customer review.
- [ ] Agree on fields, access roles, data retention/deletion, escalation contact, and human coverage hours.
- [ ] Confirm selected providers, subscription/usage charges, permissions, and secure credential handoff.
- [ ] Create tenant/workspace separation and test with synthetic records before production access.
- [ ] Configure qualification rubric, approved templates, opt-out behavior, and fallback/handoff.
- [ ] Run test cases: duplicate lead, missing/ambiguous fields, no consent, opt-out, provider timeout, calendar conflict, invalid permissions, and deletion request.
- [ ] Obtain customer approval for test results, external copy, production enablement, and any publication/testimonial.
- [ ] Record baseline, KPI definitions, support route, incident contact, and pilot review date.
- [ ] At close, export agreed results, remove/revoke access, and delete/retain data according to the agreed policy.

## Success measures

Agree baseline and review interval before the pilot. Report capture completeness, qualification/handoff completeness, median time to first approved response, follow-up completion, booking-request outcomes, duplicate/error counts, opt-outs, incidents, operator time, and direct third-party costs. Segment manual vs automated outcomes. Success means the agreed process can be repeated safely and the customer judges it useful; no numerical business outcome is guaranteed. Stop or pause for unauthorized messages, uncertain consent, cross-customer data exposure, or unresolved critical defects.

## Outreach templates

### Permission-based discovery email

**Subject:** A short conversation about handling new inquiries

Hi `[Name]`,

I’m researching how `[business type]` teams capture, qualify, and follow up on new inquiries. I’m shaping a small, human-supervised pilot for that workflow—not a promise of leads or revenue.

Would you be open to a `[15–20]-minute` conversation about your current process? No account access or sensitive customer information is needed for discovery. If it is not relevant, let me know and I will not follow up.

Thanks,  
`[Name]`

### Follow-up after discovery

**Subject:** Proposed next step for `[business]`

Hi `[Name]`,

Thanks for explaining `[specific workflow issue]`. Based on what you shared, a possible pilot would cover `[one lead source]`, `[one approved follow-up channel]`, and `[one booking destination]`, with human review and a fallback to `[owner/team]`.

I have not verified `[unverified dependency]` yet, so it is not included as a committed capability. If useful, I can send a written scope with `[pricing placeholder]`, exclusions, data handling, and test criteria for review. Would you like that?

Thanks,  
`[Name]`

### Hostinger affiliate disclosure

Place near the referral CTA: **“Disclosure: I may earn a commission if you purchase through this Hostinger link, at no additional cost to you. I recommend it only where it fits the stated use case.”**

Use only after verifying the affiliate relationship, active destination, applicable program terms, and required disclosure language. Do not imply endorsement or guarantee a business result.
