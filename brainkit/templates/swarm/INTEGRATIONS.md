# Swarm Lane Integrations Template

## Common Connections
- receives tasks from product and control lanes
- sends execution summaries to control lane
- may react to commerce or revenue events through structured task envelopes

## Emits
- routing events
- escalation events
- mission summaries

## Receives
- task envelopes
- normalized events
- supervisor directives

## Boundary Rule
Handle routing and execution here; keep user-facing complexity in product lanes.
