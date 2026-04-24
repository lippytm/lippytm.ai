from __future__ import annotations

from typing import Dict, List


REQUIRED_FILES = ['README.md', 'ROADMAP.md', 'ARCHITECTURE.md']


def score_repo(present_files: List[str], lane_known: bool, tests_present: bool, integrations_present: bool) -> Dict[str, object]:
    score = 0
    present = set(present_files)
    missing = [name for name in REQUIRED_FILES if name not in present]

    score += 30 if 'README.md' in present else 0
    score += 20 if 'ROADMAP.md' in present else 0
    score += 20 if 'ARCHITECTURE.md' in present else 0
    score += 10 if lane_known else 0
    score += 10 if tests_present else 0
    score += 10 if integrations_present else 0

    return {
        'score': score,
        'missing_required_files': missing,
        'lane_known': lane_known,
        'tests_present': tests_present,
        'integrations_present': integrations_present,
    }
