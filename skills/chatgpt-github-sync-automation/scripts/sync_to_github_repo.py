#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

REPO_BASE = Path('/home/.z/workspaces/con_7aRPHn3ReoFA8bD1/github-research/repos')


def run(cmd, cwd):
    result = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise SystemExit((result.stdout + result.stderr).strip())
    return (result.stdout + result.stderr).strip()


def main():
    parser = argparse.ArgumentParser(description='Copy a file/folder into a cloned GitHub repo, commit, and push.')
    parser.add_argument('--source', required=True)
    parser.add_argument('--repo-dir', required=True, help='Local repo folder name under github-research/repos, e.g. lippytm.ai')
    parser.add_argument('--target', required=True, help='Path inside repo')
    parser.add_argument('--message', required=True)
    args = parser.parse_args()

    source = Path(args.source).expanduser().resolve()
    repo = (REPO_BASE / args.repo_dir).resolve()
    if not source.exists():
        raise SystemExit(f'Source not found: {source}')
    if not repo.exists():
        raise SystemExit(f'Repo not found: {repo}')

    run(['git', 'pull', '--ff-only'], repo)
    dest = repo / args.target
    dest.parent.mkdir(parents=True, exist_ok=True)
    if source.is_dir():
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(source, dest)
    else:
        shutil.copy2(source, dest)

    run(['git', 'add', args.target], repo)
    status = run(['git', 'status', '--short'], repo)
    if not status:
        print('No changes to commit')
        return
    run(['git', 'commit', '-m', args.message], repo)
    out = run(['git', 'push'], repo)
    commit = run(['git', 'rev-parse', '--short', 'HEAD'], repo)
    print(f'commit={commit}')
    print(out)

if __name__ == '__main__':
    main()
