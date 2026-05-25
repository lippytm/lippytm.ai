#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/home/workspace')
EXPORT_ROOT = ROOT / 'Exports' / 'ChatGPT-Zo-Full-Bridge'
STAMP = datetime.now(timezone.utc).strftime('%Y-%m-%d-%H%M%S')
PACKAGE = EXPORT_ROOT / STAMP

INCLUDE_DIRS = [
    'Records/Plans',
    'Records/Workflows',
    'Records/Templates',
    'Campaigns',
    'Ebooks',
    'Skills',
]
INCLUDE_FILES = [
    'AGENTS.md',
    'About.md',
]
EXCLUDE_PARTS = {'Trash', 'node_modules', '.git', '__pycache__', 'Raw'}
MAX_FILE_BYTES = 2_000_000


def safe_copy_file(src: Path, dest: Path):
    if any(part in EXCLUDE_PARTS for part in src.parts):
        return
    if src.is_file() and src.stat().st_size <= MAX_FILE_BYTES:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)


def copy_tree(rel: str):
    src_root = ROOT / rel
    if not src_root.exists():
        return
    for src in src_root.rglob('*'):
        if not src.is_file():
            continue
        if any(part in EXCLUDE_PARTS for part in src.relative_to(ROOT).parts):
            continue
        if src.suffix.lower() not in {'.md', '.json', '.csv', '.yaml', '.yml', '.txt', '.py', '.ts', '.tsx'}:
            continue
        safe_copy_file(src, PACKAGE / 'workspace' / src.relative_to(ROOT))


def run(cmd: list[str], cwd: Path = ROOT) -> str:
    try:
        return subprocess.check_output(cmd, cwd=str(cwd), stderr=subprocess.STDOUT, text=True, timeout=20)
    except Exception as exc:
        return f'COMMAND_FAILED: {cmd}: {exc}'


def write_manifest():
    repo_summary = run(['bash', '-lc', "gh repo list lippytm --limit 100 --json name,description,url,visibility,updatedAt,primaryLanguage --jq '.' 2>/dev/null || true"])
    space_routes = run(['bash', '-lc', "python3 - <<'PY2'\nprint('Zo Space routes are available through Zo route tools during agent sessions.')\nPY2"])
    manifest = {
        'created_at_utc': datetime.now(timezone.utc).isoformat(),
        'purpose': 'Full ChatGPT Business to Zo Computer bridge export',
        'included_dirs': INCLUDE_DIRS,
        'included_files': INCLUDE_FILES,
        'excluded': sorted(EXCLUDE_PARTS),
        'next_prompt': 'Records/Templates/ChatGPTZoBridge/full-workspace-chatgpt-prompt.md',
    }
    (PACKAGE / 'manifest.json').write_text(json.dumps(manifest, indent=2))
    (PACKAGE / 'github-repos.json').write_text(repo_summary)
    (PACKAGE / 'space-route-note.md').write_text(space_routes)


def main():
    if PACKAGE.exists():
        shutil.rmtree(PACKAGE)
    PACKAGE.mkdir(parents=True)
    for rel in INCLUDE_FILES:
        src = ROOT / rel
        if src.exists():
            safe_copy_file(src, PACKAGE / 'workspace' / rel)
    for rel in INCLUDE_DIRS:
        copy_tree(rel)
    write_manifest()
    zip_path = shutil.make_archive(str(PACKAGE), 'zip', PACKAGE)
    print(PACKAGE)
    print(zip_path)

if __name__ == '__main__':
    main()
