# Event Catalog

This document lists the common event types used across the lippytm ecosystem for Synthetic Intelligence, swarm routing, revenue flows, commerce flows, and control-plane coordination.

## Common Event Families

### Mission Events
- `mission.created`
- `mission.classified`
- `mission.review`
- `mission.completed`
- `mission.rollback`

### Task Events
- `task.created`
- `task.assigned`
- `task.started`
- `task.completed`
- `task.failed`

### Swarm Events
- `swarm.broadcast`
- `swarm.escalated`
- `swarm.replayed`
- `swarm.dead_lettered`

### Revenue Events
- `lead.created`
- `lead.qualified`
- `lead.routed`
- `funnel.progressed`

### Commerce Events
- `billing.event`
- `checkout.created`
- `service.activated`
- `service.completed`

### Quality Events
- `quality.check.started`
- `quality.check.completed`
- `quality.check.failed`

## Best Practices
- keep event names consistent
- tie events to mission or task ids where possible
- use events to connect lanes without collapsing boundaries
