from __future__ import annotations

from pathlib import Path
from typing import Dict


DEFAULT_METADATA = {
    'hub': {'risk_level': 'critical', 'value_role': 'platform'},
    'control': {'risk_level': 'critical', 'value_role': 'platform'},
    'swarm': {'risk_level': 'high', 'value_role': 'platform'},
    'revenue': {'risk_level': 'high', 'value_role': 'direct'},
    'product': {'risk_level': 'moderate', 'value_role': 'supporting'},
    'commerce': {'risk_level': 'critical', 'value_role': 'direct'},
    'knowledge': {'risk_level': 'moderate', 'value_role': 'direct'},
    'lab': {'risk_level': 'low', 'value_role': 'experimental'},
}


def build_metadata(lane: str) -> Dict[str, object]:
    if lane not in DEFAULT_METADATA:
        raise ValueError(f'Unknown lane: {lane}')
    base = DEFAULT_METADATA[lane]
    return {
        'primary_lane': lane,
        'promotion_stage': 1 if lane == 'lab' else 3,
        'value_role': base['value_role'],
        'risk_level': base['risk_level'],
        'brainkit_managed': True,
        'fleet_managed': True,
    }


def write_metadata(target_root: str, lane: str) -> str:
    root = Path(target_root)
    root.mkdir(parents=True, exist_ok=True)
    metadata = build_metadata(lane)
    lines = ['# Lane Metadata', ''] + [f'- {key}: {value}' for key, value in metadata.items()]
    path = root / 'METADATA.md'
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return str(path)
