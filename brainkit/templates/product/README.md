# Product Lane Template

Use this template for assistants, bots, applications, operator tools, and user-facing product systems.

## Recommended files
- README.md
- ROADMAP.md
- PRODUCT.md or ARCHITECTURE.md
- docs/product/
- docs/integrations/
- app/ or src/
- tests/

## Metadata block
```yaml
primary_lane: product
promotion_stage: 3
value_role: supporting
risk_level: moderate
public_surface: true
brainkit_managed: true
fleet_managed: true
```

## Best practices
- keep the user-facing surface simple
- connect product experiences to deeper systems through clean handoffs
- preserve room for premium and partner variants without bloating the base product
