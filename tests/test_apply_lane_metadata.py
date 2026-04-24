from pathlib import Path

from scripts.apply_lane_metadata import build_metadata, write_metadata


def test_build_metadata_for_revenue():
    metadata = build_metadata('revenue')
    assert metadata['primary_lane'] == 'revenue'
    assert metadata['value_role'] == 'direct'


def test_write_metadata_creates_file(tmp_path: Path):
    target = tmp_path / 'repo_b'
    path = write_metadata(str(target), 'product')
    assert path.endswith('METADATA.md')
    assert (target / 'METADATA.md').exists()
