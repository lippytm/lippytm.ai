# Lane Event Matrix

This document maps common event flow between lanes.

| Lane | Common Emits | Common Receives |
|---|---|---|
| hub | policy updates, standards updates | rollout lessons, quality feedback |
| control | mission events, approval signals | integration events, state snapshots |
| swarm | routing events, escalation events | task envelopes, normalized events |
| revenue | lead events, funnel events | content support, service activation updates |
| product | interaction events, handoff events | service status, premium access signals |
| commerce | billing events, service events | checkout requests, activation requests |
| knowledge | content assets, educational modules | packaging requests, audience signals |
| lab | experiment results, promotion signals | concept inputs, diagnostic requests |

## Best Practices
- keep lane interfaces explicit
- use events for cross-lane coordination
- avoid tight coupling where event flow is enough
