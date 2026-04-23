# Lane Separation Policy

This policy defines how repositories and product surfaces in the lippytm ecosystem should stay connected **without becoming blurred together**.

The purpose is to preserve:

- innovation without chaos
- creativity without commercial confusion
- commercial clarity without killing experimentation
- scalable expansion without loss of architectural identity

---

## Core Rule

Every repository, workflow, product surface, and content system must belong to a primary **lane**.

Connections across lanes are allowed.

Lane collapse is not.

---

## Lane Definitions

### `hub`
Shared standards, contracts, governance, templates, policies.

### `control`
Orchestration, registry, approvals, telemetry, rollout logic.

### `swarm`
Agent coordination, routing, escalation, task execution fabric.

### `revenue`
Landing pages, offers, forms, conversion flows, partner entry points.

### `product`
Assistants, bots, applications, operator tools, user-facing systems.

### `commerce`
Payments, subscriptions, access control, receipts, monetized usage.

### `knowledge`
Education, media, storytelling, worldbuilding, productized learning.

### `lab`
Experiments, sandboxes, prototypes, temporary or high-variance systems.

---

## Separation Rules

### 1. Labs stay experimental
Lab repos may inspire product or commercial systems, but they should not become public trust surfaces until promoted.

### 2. Creative mythos stays distinct from buyer clarity
Knowledge and mythos-heavy systems may feed brand and media products, but commercial pages must remain understandable and practical.

### 3. Commerce stays modular
Revenue pages may route into commerce systems, but payment logic should not dominate or clutter public content repos.

### 4. Control stays governing, not bloated
The control layer may observe and coordinate many systems, but should not absorb their domain-specific responsibilities.

### 5. Swarm stays infrastructural
The swarm lane should handle execution and routing, not become the public-facing explanation for everything.

---

## Allowed Cross-Lane Patterns

| From | To | Purpose |
|---|---|---|
| `knowledge` | `revenue` | educational trust-building into practical offers |
| `lab` | `product` | prototype promoted into usable system |
| `revenue` | `commerce` | checkout, subscriptions, service activation |
| `product` | `swarm` | assistant or bot sends structured tasks |
| `swarm` | `control` | escalations, fleet-state visibility |
| `control` | `hub` | policy, standards, and telemetry alignment |

---

## Anti-Patterns

Avoid these:

- putting premium checkout logic directly into idea repos
- mixing speculative mythos content into core conversion pages without framing
- storing experimental prototype behavior in production-critical repos without labels
- turning control or hub repos into dumping grounds for every idea
- forcing every creative repo to sound like a sales page

---

## Public Surface Rules

If a repo is public-facing and conversion-oriented, it should emphasize:

- practical value
- clear next steps
- understandable language
- structured offers
- low friction

If a repo is creative or exploratory, it may emphasize:

- imagination
- concept exploration
- education
- narrative structures
- experimental thinking

But its commercialization path should still be documented separately.

---

## Promotion Rule

A repo can move from one lane to a more production-oriented lane only when:

1. its role is clear
2. its architecture is documented
3. its value model is defined
4. its quality gates are declared
5. its integration boundaries are explicit

---

## Rule of thumb

Connected lanes create a healthy ecosystem. Blended lanes create confusion. Keep the bridges strong and the identities clear.
