from pathlib import Path

from scripts.bootstrap_lane_template import bootstrap_lane


def test_bootstrap_lane_creates_files(tmp_path: Path):
    target = tmp_path / 'repo_a'
    result = bootstrap_lane(str(target), 'hub')
    assert result['lane'] == 'hub'
    assert result['created_count'] >= 1
    assert (target / 'README.md').exists()
    assert (target / 'ROADMAP.md').exists()
    assert (target / 'ARCHITECTURE.md').exists()
