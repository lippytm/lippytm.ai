# Commerce Lane Template

Use this template for checkout, subscriptions, access control, service receipts, and monetized usage repositories.

## Recommended files
- README.md
- ROADMAP.md
- ARCHITECTURE.md
- MONETIZATION.md
- docs/commerce/
- docs/integrations/
- backend/ or src/
- contracts/ when relevant
- tests/

## Metadata block
```yaml
primary_lane: commerce
promotion_stage: 4
value_role: direct
risk_level: critical
public_surface: false
brainkit_managed: true
fleet_managed: true
```

## Best practices
- keep checkout and access logic modular
- use higher scrutiny on monetized flows
- connect to revenue and control lanes through events rather than tight coupling
