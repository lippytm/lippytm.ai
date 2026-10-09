# Jarvis Operational Runbook

**Status:** Proposed routine for a human-led operation. It does not imply a running Jarvis service, alerting system, or model router.

## Roles and authority

- **Principal:** approves priorities, customer commitments, spend, data access, external publication, and go/no-go decisions.
- **AI Jarvis Assistant — Engineering Manager:** drafts engineering plans, review checklists, risk registers, and release recommendations. It cannot merge, deploy, change access, or declare an untested integration live.
- **AI Jarvis Assistant — Communications Manager:** drafts customer, campaign, affiliate, and media materials. A human approves every external send/publication and claim.
- **Operator/human reviewer:** executes runbooks, verifies outputs, records decisions, and owns human handoff.

## Daily 20-minute standup

1. **Revenue/customer (3 min):** leads, booked conversations, pilot status, support needs.
2. **Delivery (5 min):** top three outcomes for today; owner and acceptance criterion for each.
3. **Engineering (5 min):** changed code/assets, tests, release risks, and unverified dependencies.
4. **Communications/content (4 min):** drafts awaiting review, publication/disclosure checks, customer follow-ups due.
5. **Blockers and decisions (3 min):** assign an owner and due time; escalate privacy, security, safety, or customer-impacting incidents immediately.

Record date, participants, decisions, owners, due dates, and blockers in the chosen system of record. Do not store credentials or unnecessary customer data in the notes.

## Weekly review (Friday or final business day)

- Review leads, discovery calls, scopes accepted, measured workflow KPIs, support effort, costs, incidents, opt-outs, and content/affiliate attribution.
- Inspect work against the acceptance criteria in the [30-day plan](JARVIS_30_DAY_REVENUE_LAUNCH_PLAN.md).
- Decide keep/change/stop for each experiment; document the evidence and confidence.
- Review next week's three priorities, customer commitments, dependency status, and release gate.
- Review digital-media rights/edition status and the next publishable asset.
- Close or assign every incident and action item; no issue is resolved solely because an AI summary says it is.

## Model routing (human-operated)

| Model | Use first for | Required check |
|---|---|---|
| ChatGPT | Structured plans, task decomposition, synthesis, code/repo assistance | Verify claims against repository evidence and run tests |
| Claude | Long-form analysis, documentation drafts, careful comparison | Review factual assertions, scope, and privacy |
| Gemini | Multimodal review and alternative creative directions | Confirm media inputs are authorized and validate output |
| Perplexity | Current external research and competitor/source discovery | Open primary sources, record access date/citations, distinguish fact from inference |

These are suggested task assignments, not capability guarantees. Provide each model only the minimum authorized context. Do not put secrets or sensitive customer data into model prompts unless the applicable provider, account, and data terms have been reviewed and approved. If outputs conflict, ask for sources/assumptions and let the human decide. Jarvis may coordinate assignments; automated cross-model delegation is proposed, not asserted as implemented.

## Approval gates

| Gate | Human approval required before |
|---|---|
| Customer/data | Collecting production data, changing retention, connecting accounts, or expanding access |
| Communications | Sending outreach/follow-up, publishing content, making affiliate claims, or using testimonials |
| Commercial | Quoting final price, changing scope, accepting terms, issuing refunds, or making outcome claims |
| Engineering | Merging/releasing, enabling an integration, changing prompts/policies, or running destructive jobs |
| Incident recovery | Restarting a failed workflow that may repeat an external action or expose customer data |

Before release, require passing relevant tests, documented scope, least-privilege access, rollback/fallback, owner on call, and no unresolved critical/high-impact defect.

## Incident escalation and human handoff

1. **Stop:** pause affected workflow and external sends; do not retry an uncertain non-idempotent action.
2. **Protect:** revoke/rotate exposed credentials through the provider; preserve logs without copying secrets or excess personal data.
3. **Route:** notify the Principal and affected customer contact for suspected exposure, unauthorized message, data loss, financial action, or materially wrong advice. Use applicable legal/contractual incident procedures.
4. **Record:** time, affected tenant/workflow, observed impact, correlation ID, containment, and owner; omit secrets.
5. **Recover:** test the fix using synthetic data, verify no duplicates, obtain human authorization, then resume gradually.
6. **Learn:** document root cause, corrective action, owner, due date, and regression test.

Escalate immediately when identity/consent is unclear, the request involves regulated/high-risk advice, the customer disputes an action, a safety concern appears, or the bot cannot confidently complete the request. Human handoff includes a concise summary, collected fields, consent/opt-out status, attempted actions, errors, and next action. If a human is unavailable, acknowledge receipt without promising a response time and provide a safe alternative contact path.
