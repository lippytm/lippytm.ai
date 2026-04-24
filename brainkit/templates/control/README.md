# Control Lane Template

Use this template for orchestration, registry, approval, telemetry, and rollout-control repositories.

## Recommended files
- README.md
- ROADMAP.md
- ARCHITECTURE.md
- OPERATIONS.md
- docs/control/
- docs/workflows/
- src/fleet/
- tests/fleet/

## Metadata block
```yaml
primary_lane: control
promotion_stage: 4
value_role: platform
risk_level: critical
public_surface: false
brainkit_managed: true
fleet_managed: true
```

## Best practices
- coordinate across lanes without absorbing them
- keep policy and rollout traceable
- treat orchestration changes as governed actions
