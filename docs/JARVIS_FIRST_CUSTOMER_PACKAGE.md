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

## Delivery status and scope boundary

Repository review at PR head `c7445bba8faead902d9a218f42861a427d85384f` on 2026-10-09 supports preparation and synthetic rehearsal. It does **not** establish a production-ready pilot. Discovery notes, a workflow map, qualification rubric, message drafts, a test plan, and an operator walkthrough can be prepared from the existing assets. Live customer operation, including manual operation, requires the gates below.

| Step | Repository evidence | Committable behavior before live verification |
|---|---|---|
| Capture and lead storage | CRM roadmap and JSON definitions; no verified intake-to-storage implementation identified | Map fields and rehearse with synthetic records; customer-authorized manual intake is an option only after validation |
| Qualification | Proposed rubric and handoff; no tested decision engine | Human reviews the agreed rubric; ambiguous or high-risk requests go to staff |
| Follow-up | Draft templates and proposed events; no verified send adapter or suppression store | Draft for human review; do not promise automatic sending or delivery |
| Booking | Proposed contracts and calendar scenarios; no verified availability/write adapter | Prepare a request or route to staff; only provider-confirmed appointments count as booked |
| Reliability and privacy | Policies and proposed contracts, not demonstrated enforcement | Specify and test controls; do not claim implemented isolation, encryption, deletion, retries, or monitoring |

The example `brainkit/connector.template.js` sets `connected = true` without provider authentication and returns an empty array from `fetchData()`. Its status is not integration evidence. Existing event-schema tests inspect required-field lists and enum values; they do not validate real payloads, dispatch events, or exercise the pilot.

Record every workflow step as **proposed**, **synthetic rehearsal**, **verified manual**, or **verified integration**, with owner, version, test date, evidence, and limitations. Never promote a simulation or a generic connector status to live verification.

Count each distinct external system accessed automatically in the pilot toward the three-integration cap, including storage/CRM, middleware, model APIs, and booking/messaging services. Record all vendors and manual tools in the data-flow inventory even when they are not automated integrations. If the selected design exceeds three, reduce the design or use explicitly scoped, verified manual steps; do not silently expand the cap. Existing ChatGPT/Codex account connections do not prove customer account permissions or a deployable Jarvis service.

## Required scope and onboarding record

Complete these fields privately before quoting delivery; use synthetic examples in public documentation:

- Customer signatory/account owner; Principal; delivery operator and backup; named approver for each outbound message and appointment action.
- Exact source, follow-up channel, authoritative booking destination, integration count, implementation/version, and manual steps. Define appointment types, time zone, hours, duration, buffers, capacity, cancellation/rescheduling, and what constitutes provider confirmation.
- Minimum field list, qualification rubric, prohibited data, permitted purposes, recipient/channel consent evidence, suppression owner, and approved copy/version.
- Pilot dates, volume cap, operator coverage hours, approval turnaround, escalation and fallback contact, support response expectations, and change-request procedure. Start dates depend on verified access and passing acceptance checks; the 30-day plan is a planning sequence, not a delivery SLA.
- Deliverables: workflow/data map, evidence-backed configuration or manual runbook, synthetic acceptance results, customer walkthrough, measured findings, and closeout record.
- Approved price/currency, payment milestones, third-party costs and spending cap, cancellation/refund terms, acceptance criteria, and support inclusion/exclusions. Payment collection requires its own approved process.
- Baseline window, review interval, numerical process targets agreed after baseline, acceptance signatories, and continue/revise/stop date. No customer, price, or target is inferred from this template.

### Consent and privacy gate

Customer authorization to connect an account and a lead's permission to receive a message are separate checks. A form submission, public email address, checklist download, or booked discovery call is not blanket permission for marketing, affiliate promotion, another channel, or model-provider processing.

Before collection or sending, the Principal and customer must identify the applicable jurisdictions, message purpose, channel/provider rules, and required notices or consent. Record recipient, purpose, channel, source, timestamp, notice/wording version, and withdrawal status in access-controlled storage. Unknown or disputed permission blocks follow-up and routes to a human. Keep requested-service follow-up separate from optional educational/affiliate marketing; obtain a separate permitted basis for the latter. The discovery email below is a draft, not evidence that contacting any recipient is permitted.

For U.S. commercial email, review accurate sender/subject information, required identification/address, and working opt-out handling against the [FTC CAN-SPAM guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business). Calling a message “transactional” or manually sending it does not settle its legal classification. SMS, calls, social DMs, and other jurisdictions need their own review before selection; email review does not authorize them.

Suppress withdrawn contacts before the next send, cancel queued follow-ups, and recheck permission at execution time. Retain only the minimum suppression evidence needed to prevent recontact, under the agreed policy; document how this interacts with deletion requests.

Approve a data-flow inventory covering source, storage, logs, exports, booking, messaging, and any model provider. Record fields/purpose, access roles, customer/operator/vendor responsibilities, hosting locations, provider terms and any required processing agreement, model retention/training settings, retention period, deletion method, backups, and incident notification responsibilities. Unknown provider handling blocks sending production data to that provider. Demonstrate least-privilege access, customer/workspace separation, protected storage and transport, redacted logs, and access revocation rather than treating policy text as proof.

Use synthetic data for testing. Keep credentials and private lead data out of public GitHub, public reports, and unapproved AI prompts. Test access/correction/deletion requests across downstream copies; explain any lawful retention or backup expiry instead of claiming immediate universal deletion. See [Data Classification](../security/DATA_CLASSIFICATION.md) and the [FTC security guide](https://www.ftc.gov/business-guidance/resources/start-security-guide-business) for the supporting minimization, access, and vendor-review principles.

### Approval and recovery gate

Every outbound message and appointment create/change/cancel action requires human approval throughout this pilot, even after an integration passes testing. Record the approver, timestamp, exact recipient/destination, content or action version, consent check, and resulting provider ID/status. Editing an approved action invalidates its approval. A scope approval or template approval does not authorize all future actions.

Lead text is untrusted input: requests embedded in an inquiry cannot change policy, reveal other records, or authorize a send/booking. Approval occurs outside lead-controlled content. Recheck recipient, consent, current availability, and scope immediately before execution; approval is not a substitute for these checks.

On a timeout or uncertain provider result, reconcile provider state before retrying. Preserve a stable operation ID, prevent duplicate sends/bookings, bound retries, and route exhausted or ambiguous work to the operator. A human fallback is verified only when its owner/backup receives the context and demonstrates the next step. If coverage is unavailable, queue safely and state the approved contact path without promising an unagreed response time.

Pause for unapproved actions, uncertain consent, failed suppression, suspected exposure, duplicate bookings, unavailable fallback, or unresolved high/critical defects. Record containment and customer communication responsibilities; resume only after reconciliation, synthetic retest, and Principal/customer authorization.

## Acceptance evidence required before production

These are required future checks, **not passed results**. For each, record scenario, expected/observed result, execution mode, version, date, operator, redacted evidence, and reviewer. Manual steps require a reproducible walkthrough; implemented automated steps require appropriate automated regression tests plus named-provider end-to-end evidence.

| Check | Minimum acceptance behavior |
|---|---|
| Happy path and source reconciliation | Every eligible synthetic inquiry reaches the correct restricted workspace; source counts reconcile to captured, rejected, duplicate, or failed records |
| Duplicate/replayed input | Repeated lead/event or concurrent replay creates no duplicate send or appointment; changed payload under the same operation key is rejected |
| Missing, ambiguous, malicious input | Missing fields route to staff; injected instructions cannot bypass approval, reveal data, or trigger actions |
| No permission and withdrawal | No send for absent/uncertain/wrong-purpose permission; withdrawal after approval but before execution cancels queued work |
| Approval enforcement | Unapproved, altered, expired, or wrong-recipient actions are blocked; provider outcome and human approval can be reconciled |
| Authentication and isolation | Wrong account/workspace/resource and revoked access are denied, including negative tests against another synthetic customer |
| Provider failure | Timeout, rate limit, partial success, and lost response do not cause blind retries or false success; fallback and reconciliation work |
| Booking rules | Time zones/DST, conflicts, stale availability, cancellation/rescheduling, and repeated requests are handled; a request is never reported as confirmed |
| Privacy and closeout | Logs/exports contain no secrets or unnecessary lead content; downstream deletion/retention and access revocation are demonstrated |
| Operator recovery | Stop control, backup coverage, customer handoff, and controlled restart are exercised |

Block launch if a mandatory check fails or remains unknown. Deferred automation may be replaced only by a customer-approved, tested manual process with adequate coverage; safety/privacy/consent requirements cannot be deferred. A successful synthetic rehearsal alone does not demonstrate a live integration. Use authorized test accounts and only enable production after customer and Principal approval.

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

Keep a private ledger of eligible inquiries and source timestamps, approval/send timestamps, qualification decisions, due follow-ups, opt-outs, booking attempts/confirmations, failures, handoffs, operator hours, and costs. Use opaque IDs in shared reports. Report numerator/denominator, time window, data source, sample size, missing data, and manual versus integrated execution. A zero denominator means “not applicable,” not 100% success.

- Capture completeness: unique eligible inquiries captured / unique eligible source inquiries; report exclusions and failures separately.
- Qualification/handoff completeness: cases with rubric decision or a named handoff owner and next action / cases reviewed.
- First-response time: median and range from inquiry receipt to actual approved first send, with unanswered inquiries reported separately; distinguish elapsed time from covered business hours and draft preparation from sending.
- Follow-up completion: completed permitted follow-ups / permitted follow-ups due; show suppressed, failed, and overdue counts separately.
- Booking completion: provider-confirmed appointments / eligible booking requests; separately show requests routed to staff, conflicts, failures, cancellations, and no-shows if measured.
- Safety/economics: unapproved-action and duplicate counts, permission/suppression failures, privacy incidents, unresolved defects, delivery/support hours, and actual tool/usage costs.

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
