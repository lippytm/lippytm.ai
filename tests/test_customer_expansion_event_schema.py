import json
from pathlib import Path


def test_customer_expansion_event_schema_has_core_events():
    path = Path('brainkit/contracts/customer-expansion-event-schema.json')
    data = json.loads(path.read_text(encoding='utf-8'))
    values = set(data['properties']['event_type']['enum'])
    assert 'customer.expansion_candidate' in values
    assert 'customer.followup_due' in values
    assert 'customer.repeat_engagement' in values


def test_customer_expansion_event_schema_requires_core_fields():
    path = Path('brainkit/contracts/customer-expansion-event-schema.json')
    data = json.loads(path.read_text(encoding='utf-8'))
    required = set(data['required'])
    assert 'event_id' in required
    assert 'event_type' in required
    assert 'contact_id' in required
