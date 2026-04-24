from __future__ import annotations

from pathlib import Path
from typing import Dict


LANE_FILES = {
    'hub': ['README.md', 'ROADMAP.md', 'ARCHITECTURE.md', 'QUALITY_CHECKLIST.md', 'INTEGRATIONS.md'],
    'control': ['README.md', 'ROADMAP.md', 'ARCHITECTURE.md', 'QUALITY_CHECKLIST.md', 'INTEGRATIONS.md'],
    'swarm': ['README.md', 'ROADMAP.md', 'ARCHITECTURE.md', 'QUALITY_CHECKLIST.md', 'INTEGRATIONS.md'],
    'revenue': ['README.md', 'ROADMAP.md', 'ARCHITECTURE.md', 'QUALITY_CHECKLIST.md', 'INTEGRATIONS.md'],
    'product': ['README.md', 'ROADMAP.md', 'ARCHITECTURE.md', 'QUALITY_CHECKLIST.md', 'INTEGRATIONS.md'],
    'commerce': ['README.md', 'ROADMAP.md', 'ARCHITECTURE.md', 'QUALITY_CHECKLIST.md', 'INTEGRATIONS.md'],
    'knowledge': ['README.md', 'ROADMAP.md', 'ARCHITECTURE.md', 'QUALITY_CHECKLIST.md', 'INTEGRATIONS.md'],
    'lab': ['README.md', 'ROADMAP.md', 'ARCHITECTURE.md', 'QUALITY_CHECKLIST.md', 'INTEGRATIONS.md'],
}


def bootstrap_lane(target_root: str, lane: str) -> Dict[str, object]:
    if lane not in LANE_FILES:
        raise ValueError(f'Unknown lane: {lane}')

    root = Path(target_root)
    root.mkdir(parents=True, exist_ok=True)
    created = []
    for filename in LANE_FILES[lane]:
        path = root / filename
        if not path.exists():
            path.write_text(f'# {lane.title()} Template File: {filename}\n', encoding='utf-8')
            created.append(str(path))

    return {
        'lane': lane,
        'target_root': str(root),
        'created_files': created,
        'created_count': len(created),
    }
