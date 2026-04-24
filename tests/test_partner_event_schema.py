import json
from pathlib import Path


def test_partner_event_schema_has_core_events():
    path = Path('brainkit/contracts/partner-event-schema.json')
    data = json.loads(path.read_text(encoding='utf-8'))
    values = set(data['properties']['event_type']['enum'])
    assert 'partner.created' in values
    assert 'partner.routed' in values
    assert 'partner.lead' in values


def test_partner_event_schema_requires_core_fields():
    path = Path('brainkit/contracts/partner-event-schema.json')
    data = json.loads(path.read_text(encoding='utf-8'))
    required = set(data['required'])
    assert 'event_id' in required
    assert 'event_type' in required
    assert 'partner_id' in required
