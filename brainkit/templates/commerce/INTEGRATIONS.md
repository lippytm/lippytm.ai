# Commerce Lane Integrations Template

## Common Connections
- receives checkout handoffs from revenue lane
- emits service and billing events to control lane
- may grant access signals to product lane

## Emits
- billing events
- service activation events
- access events

## Receives
- checkout requests
- premium activation requests
- offer codes and customer references

## Boundary Rule
Keep monetized state here and connect outward through events rather than tight coupling.
