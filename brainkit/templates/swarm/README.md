# Swarm Lane Template

Use this template for routing, agent coordination, escalation, replay, and mission-supervision repositories.

## Recommended files
- README.md
- ROADMAP.md
- ARCHITECTURE.md
- docs/swarm/
- swarm/
- tests/
- prompts/agents/

## Metadata block
```yaml
primary_lane: swarm
promotion_stage: 4
value_role: platform
risk_level: high
public_surface: false
brainkit_managed: true
fleet_managed: true
```

## Best practices
- keep execution explainable
- keep escalation and dead-letter handling first-class
- separate public-facing simplicity from backend routing complexity
