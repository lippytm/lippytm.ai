# Control Lane Integrations Template

## Common Connections
- reads state from most lanes
- coordinates missions across lanes
- receives commerce, swarm, and product events

## Emits
- mission events
- rollout events
- approval and review signals

## Receives
- integration events
- state snapshots
- feedback loop summaries

## Boundary Rule
Coordinate other lanes without becoming the permanent home for their domain logic.
