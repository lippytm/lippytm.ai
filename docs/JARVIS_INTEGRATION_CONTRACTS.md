# Jarvis Integration Contracts

**Status:** Proposed cross-repository contract, not a deployed API specification. Adapt and version with implementation owners before connecting systems. This proposal does not assert that billing, CRM, model routing, booking, or connectors work today.

## Request envelope

Required fields: `contract_version`, unique `request_id`, `correlation_id`, `tenant_id`, `occurred_at` (UTC RFC 3339), `actor`, `action`, and `data`. `idempotency_key` is required for any action that can create/update an external record or send a message. Use opaque IDs; never put credentials or unnecessary personal data in metadata.

```json
{
  "contract_version": "1.0",
  "request_id": "req_01JABC",
  "correlation_id": "corr_01JABC",
  "idempotency_key": "sha256:opaque-stable-operation-key",
  "tenant_id": "tenant_opaque_123",
  "occurred_at": "2026-09-30T12:00:00Z",
  "actor": {
    "type": "human",
    "id": "user_opaque_456"
  },
  "action": "lead.qualify",
  "data": {
    "lead_id": "lead_opaque_789",
    "consent": {
      "status": "granted",
      "captured_at": "2026-09-30T11:59:00Z",
      "purpose": "requested appointment follow-up"
    },
    "fields": {
      "business_need": "website inquiry response",
      "preferred_contact_window": "weekday afternoon"
    }
  }
}
```

## Response envelope

Return the same `contract_version`, `request_id`, `correlation_id`, and `tenant_id`; include `status`, `result`, and structured `error` (null on success). A timeout must not be represented as success. A `pending` result means the caller must use status/event updates rather than repeat an unsafe action.

```json
{
  "contract_version": "1.0",
  "request_id": "req_01JABC",
  "correlation_id": "corr_01JABC",
  "tenant_id": "tenant_opaque_123",
  "status": "succeeded",
  "result": {
    "lead_id": "lead_opaque_789",
    "qualification": "needs_human_review",
    "next_action": "handoff"
  },
  "error": null
}
```

Example error:

```json
{
  "contract_version": "1.0",
  "request_id": "req_01JABC",
  "correlation_id": "corr_01JABC",
  "tenant_id": "tenant_opaque_123",
  "status": "failed",
  "result": null,
  "error": {
    "code": "DEPENDENCY_UNAVAILABLE",
    "message": "Booking provider did not respond before the deadline.",
    "retryable": true
  }
}
```

## Event names and payload

Use lowercase dot-separated domain/action names. Initial proposed lifecycle events:

- `lead.captured`
- `lead.qualified`
- `lead.followup_due`
- `lead.followup_sent`
- `appointment.requested`
- `appointment.booked`
- `appointment.failed`
- `handoff.requested`
- `workflow.failed`

An event contains `contract_version`, unique `event_id`, `event_type`, `tenant_id`, `correlation_id`, `occurred_at`, and a minimal domain `data` object. Keep the event ID stable on redelivery. Existing BrainKit artifacts cover `customer.expansion_candidate`, `customer.followup_due`, `customer.repeat_engagement`, and partner events; those are repository assets, not proof of deployed event delivery. Adopt, map, or deprecate them through an explicit versioned migration.

```json
{
  "contract_version": "1.0",
  "event_id": "evt_01JDEF",
  "event_type": "lead.captured",
  "tenant_id": "tenant_opaque_123",
  "correlation_id": "corr_01JABC",
  "occurred_at": "2026-09-30T12:01:00Z",
  "data": {
    "lead_id": "lead_opaque_789",
    "source": "website_form",
    "consent_status": "granted"
  }
}
```

## Delivery and isolation rules

- **Tenant isolation:** derive tenant scope from authenticated server-side identity, then validate it against every resource; do not trust a caller-supplied `tenant_id` alone. Scope queries, queues, logs, caches, and object storage by tenant. Add negative cross-tenant tests.
- **Correlation:** propagate the same `correlation_id` through request, event, worker, and logs. `request_id` identifies one call; `event_id` identifies one event. Do not log access tokens or full message bodies by default.
- **Idempotency:** persist `(tenant_id, idempotency_key, action)` with outcome for a documented retention period. Same key and same payload returns the original outcome; same key with different payload returns conflict. Use provider idempotency support when available. Never blindly retry sends/bookings with uncertain completion.
- **Timeouts:** set explicit per-provider connect and total deadlines; an initial proposal is 3 seconds connect and 15 seconds total for synchronous calls, with long work moved to a job and `pending` response. Set final values from provider constraints and measured latency.
- **Retries:** retry only transient failures, with bounded exponential backoff and jitter; honor `Retry-After`; cap at 3 attempts within the operation deadline. Do not retry validation, authorization, consent, or idempotency conflicts. Dead-letter exhausted async work for human review.
- **Privacy:** validate schema and size, minimize fields, encrypt in transit/at rest, apply documented deletion and retention policies, and keep secrets in an approved secret store.

## Versioning and compatibility

Use explicit `major.minor` contract versions. Within a major version, additive optional fields are backward-compatible; changing required fields, meanings, privacy scope, or event semantics requires a new major version. Consumers ignore unknown optional fields. Producers publish schema and migration notes before rollout; deploy consumers before producers; support a bounded migration window; then remove old versions only with recorded owner approval and evidence that consumers have migrated. Breaking changes must not silently reinterpret customer data.

Before calling a contract implemented, publish its schema, contract tests, auth/tenant tests, idempotency and timeout tests, and observed end-to-end result for the named integration.
