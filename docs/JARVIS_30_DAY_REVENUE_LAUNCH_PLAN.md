# Jarvis 30-Day Revenue Launch Plan

**Operating assumption:** one narrow, human-supervised lead capture → qualification → follow-up → appointment-booking pilot. This plan schedules discovery and validation; it does not promise revenue or presume integrations exist.

## Owners

- **Principal:** final business, privacy, legal, pricing, access, and publication approval.
- **AI Jarvis Assistant — Engineering Manager (EM):** proposes technical tasks, test gates, risks, and release notes.
- **AI Jarvis Assistant — Communications Manager (CM):** drafts customer research, offers, outreach, and content.
- **Builder/Operator (BO):** human who verifies repository/code, configures tools, executes tests, and runs any manual pilot steps. One person may fill multiple human roles.

AI roles advise and draft. They do not independently make commitments, spend money, contact prospects, or deploy.

## Days 1–7: choose the problem and define the offer

| Day | Owner(s) | Deliverable and acceptance criteria | KPI / dependency |
|---|---|---|---|
| 1 | Principal + EM | Select one candidate niche and list three recurring lead-response pains; record assumptions and evidence in the commercial backlog. | 1 niche; 3 pains; depends on available customer access |
| 2 | CM + Principal | Prepare and conduct 3–5 discovery conversations or outreach requests; record consent and anonymized notes. | 3 completed conversations targeted; do not invent responses |
| 3 | Principal + EM | Choose one workflow and one ideal customer profile; define in-scope and out-of-scope actions. | 1 workflow, max 3 integrations |
| 4 | EM + BO | Map data fields, consent, routing, retention, failure path, and human handoff; mark every unverified connector proposed. | 100% workflow steps have an owner and fallback |
| 5 | CM + Principal | Draft pilot one-pager, customer journey, and disclosure language; verify claims against evidence. | 1 reviewed offer; 0 unsubstantiated claims |
| 6 | Principal + BO | Create discovery and onboarding forms that avoid unnecessary sensitive data; test submission and access controls if forms exist. | All required fields documented; no credentials collected |
| 7 | Principal | Gate 1: approve niche, workflow, written-scope template, and success measures or repeat discovery. | Written go/no-go; no build commitment before approval |

## Days 8–14: prove one safe workflow

| Day | Owner(s) | Deliverable and acceptance criteria | KPI / dependency |
|---|---|---|---|
| 8 | EM + BO | Inventory actual candidate tools and APIs; verify documentation, permissions, costs, and test access. | Evidence recorded for every proposed integration |
| 9 | BO + EM | Implement or manually simulate capture using test data; duplicate submission does not create duplicate lead. | 10/10 capture test cases pass |
| 10 | BO + EM | Test qualification fields and incomplete/ambiguous input paths; unclear inputs route to a human. | 10/10 cases classified or handed off |
| 11 | BO + CM | Draft follow-up templates; verify consent, opt-out, sender identity, and human approval path. | 100% messages approved before external send |
| 12 | BO + EM | Test booking destination with test availability; conflicts, unavailable slots, and failure route to staff. | 5/5 booking scenarios pass or remain manual |
| 13 | BO + EM | Test logs, tenant boundary assumptions, retries, idempotency, and deletion procedure using synthetic data. | No cross-customer data in tests; test evidence saved |
| 14 | Principal + EM | Gate 2: accept only the steps proven end-to-end; label all remaining steps manual/proposed. | Critical issues = 0; workflow fallback demonstrated |

## Days 15–21: prepare acquisition and delivery

| Day | Owner(s) | Deliverable and acceptance criteria | KPI / dependency |
|---|---|---|---|
| 15 | CM + Principal | Draft landing/offer copy and one lead magnet CTA; include scope limits, opt-in, and privacy notice. | 1 copy set approved |
| 16 | CM + BO | Prepare Hostinger page/funnel draft only if the affiliate relationship and destination are verified; place conspicuous disclosure beside link. | Affiliate status verified or link omitted |
| 17 | CM + Principal | Prepare 2 email and 2 social outreach variants; claims are factual and human-send only. | 4 reviewed drafts |
| 18 | CM + BO | Select one ebook excerpt and map a relevant CTA; confirm source ownership, edition status, and consent for list use. | 1 asset with rights/status record |
| 19 | BO + EM | Run pre-pilot checklist on test cases, access, rollback, incident contact, and manual fallback. | 100% checklist items pass or are explicitly deferred |
| 20 | Principal + BO | Onboard one consenting pilot prospect using a written scope; use sandbox/test records until customer authorizes production. | 1 signed/accepted scope targeted; never presume |
| 21 | Principal + EM | Gate 3: approve a limited pilot only if data flow and customer permissions are clear and unresolved severity-1 issues = 0. | Written approval; otherwise pause |

## Days 22–30: operate, measure, decide

| Day | Owner(s) | Deliverable and acceptance criteria | KPI / dependency |
|---|---|---|---|
| 22 | BO | Start controlled pilot with human review for every outbound message and appointment action. | 100% actions logged and reviewable |
| 23 | BO + EM | Reconcile captured leads against source; inspect duplicates and failed handoffs. | Capture completeness and duplicate count reported |
| 24 | CM + BO | Review response copy, opt-outs, and customer feedback; pause any confusing or unwanted message. | Opt-outs honored; zero unapproved sends |
| 25 | BO + EM | Review booking attempts and fallbacks with customer; verify calendar permissions and conflicts. | Success/failure counts, no assumed conversion target |
| 26 | CM | Publish one approved educational item and track its CTA with privacy-respecting attribution. | 1 item published if rights/approval clear |
| 27 | Principal + EM | Review pilot risks, support effort, model/tool cost, incidents, and customer satisfaction. | All incidents recorded; actual cost/effort measured |
| 28 | CM + Principal | Request permission for feedback/testimonial; publish none without explicit approval and substantiation. | Consent recorded or no testimonial |
| 29 | EM + BO | Produce reproducible runbook, test results, limitations, and prioritized fixes. | Acceptance tests rerunnable by another operator |
| 30 | Principal | Gate 4: continue, revise, or stop based on evidence; update offer and next-month backlog. | Decision and rationale recorded; no revenue target treated as guaranteed |

## KPI definitions

Report weekly with numerator, denominator, time window, source, and caveats:

- Qualified inquiries: inquiries satisfying the approved rubric / total inquiries reviewed.
- First-response time: median time from consented inquiry receipt to first human-approved response.
- Follow-up completion: due follow-ups completed / follow-ups due; separately count opt-outs and failures.
- Booking completion: confirmed bookings / booking requests; distinguish automated from manual.
- Handoff completeness: cases with owner, context, and next action / cases handed off.
- Workflow reliability: successful eligible test/production executions / total eligible executions.
- Acquisition: page visits, opted-in leads, booked discovery calls, and pilot scopes accepted; do not infer causation from small samples.
- Economics: measured delivery hours and direct tool costs per pilot; compare to proposed pricing only after actual costs are known.
- Media/affiliate: content published, CTA clicks, and verified referral events; disclose tracking limits and affiliate status.

Targets should be set after baseline data. Safety gates are non-negotiable: zero unapproved external actions; zero known cross-tenant disclosures; opt-outs handled; unresolved critical incidents block launch.
