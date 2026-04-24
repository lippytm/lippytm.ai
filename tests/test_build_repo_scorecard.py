from scripts.build_repo_scorecard import score_repo


def test_score_repo_high_score_when_core_files_present():
    result = score_repo(
        ['README.md', 'ROADMAP.md', 'ARCHITECTURE.md'],
        lane_known=True,
        tests_present=True,
        integrations_present=True,
    )
    assert result['score'] == 100
    assert result['missing_required_files'] == []


def test_score_repo_reports_missing_files():
    result = score_repo(['README.md'], lane_known=False, tests_present=False, integrations_present=False)
    assert 'ROADMAP.md' in result['missing_required_files']
    assert 'ARCHITECTURE.md' in result['missing_required_files']
