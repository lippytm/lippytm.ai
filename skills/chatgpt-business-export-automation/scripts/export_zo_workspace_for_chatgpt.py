#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/home/workspace')
EXPORT_ROOT = ROOT / 'Exports' / 'LippytmAI-Zo-Workspace-Export'
PACKAGE = EXPORT_ROOT / datetime.now(timezone.utc).strftime('%Y-%m-%d-%H%M%S')

FILES_TO_COPY = [
    'AGENTS.md',
    'Records/Plans/business-of-businesses-revenue-upgrade-plan.md',
    'Records/Plans/github-repository-command-map.md',
    'Records/Workflows/chatgpt-business-github-mirror-workflow.md',
    'Records/Workflows/chatgpt-business-zo-computer-integration-operating-system.md',
    'Records/Workflows/ai-coding-chatgpt-zapier-github-zo-workflow.md',
    'Records/Workflows/lippytmai-expansion-operating-system.md',
    'Records/Workflows/agentic-swarm-skill-stack-blueprint.md',
    'Records/Workflows/ai-agentic-super-synthetic-intelligence-engine-autonomous-upgrade-plan.md',
    'Records/Workflows/swarm-mass-manufacturing-operating-system.md',
    'Records/Workflows/web3-affiliate-hosting-payment-operating-system.md',
    'Records/Workflows/web3-affiliate-agentbot-swarm-network.md',
    'Records/Workflows/getbizfunds-web3-payment-and-wallet-system.md',
    'Campaigns/AI Business Funding Launch Kit/README.md',
    'Campaigns/AI Business Funding Launch Kit/social-post-pack.md',
    'Campaigns/AI Business Funding Launch Kit/video-campaign-pack.md',
    'Campaigns/AI Business Funding Launch Kit/chatgpt-business-master-prompt.md',
    'Campaigns/AI Business Funding Launch Kit/chatgpt-ai-coding-zapier-master-prompt.md',
    'Ebooks/AI Business Funding Launch Kit/ai-business-funding-launch-kit-ebook.md',
    'Ebooks/AI Business Funding Launch Kit/sales-page-copy.md',
]

PUBLIC_URLS = [
    ('Business of Businesses', 'https://lippytmai.zo.space/business-of-businesses'),
    ('AI Business Funding Launch Kit', 'https://lippytmai.zo.space/ai-business-funding-launch-kit'),
    ('AI Business Funding eBook', 'https://lippytmai.zo.space/ebook/ai-business-funding-launch-kit'),
    ('Zapier Lead Automation Template', 'https://lippytmai.zo.space/zapier-lead-automation-template'),
    ('AI Coding Automation Command Center', 'https://lippytmai.zo.space/ai-coding-automation-command-center'),
    ('AgentBots Command Center', 'https://lippytmai.zo.space/agentbots-command-center'),
    ('AgentBots Skill Improvement', 'https://lippytmai.zo.space/agentbots-skill-improvement'),
    ('Agent Interoperability Bridge', 'https://lippytmai.zo.space/agent-interoperability-bridge'),
    ('Swarm Factory', 'https://lippytmai.zo.space/swarm-factory'),
    ('Web3 Affiliate Platform', 'https://lippytmai.zo.space/web3-affiliate-platform'),
    ('GetBizFunds Web3 Payment System', 'https://lippytmai.zo.space/getbizfunds-web3-payment-system'),
]

GITHUB_REPOS = [
    'lippytm/lippytm.ai',
    'lippytm/lippytmai.getbizfunds.com-',
    'lippytm/lippytmai.zo.computer-',
    'lippytm/lippytm-lippytm.ai-tower-control-ai',
]


def run(cmd: list[str], cwd: Path | None = None) -> str:
    try:
        result = subprocess.run(cmd, cwd=str(cwd) if cwd else None, check=False, capture_output=True, text=True, timeout=20)
        return (result.stdout + result.stderr).strip()
    except Exception as exc:
        return f'Unable to run {cmd}: {exc}'


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')


def copy_file(rel: str) -> None:
    src = ROOT / rel
    if not src.exists():
        return
    dest = PACKAGE / 'workspace-files' / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)


def main() -> None:
    PACKAGE.mkdir(parents=True, exist_ok=True)

    for rel in FILES_TO_COPY:
        copy_file(rel)

    skills = sorted(str(p.relative_to(ROOT)) for p in (ROOT / 'Skills').glob('*/SKILL.md'))
    write(PACKAGE / 'skills-map.md', '# Skills Map\n\n' + '\n'.join(f'- `{s}`' for s in skills) + '\n')

    public_url_md = '# Public URL Map\n\n' + '\n'.join(f'- **{name}** — {url}' for name, url in PUBLIC_URLS) + '\n'
    write(PACKAGE / 'public-url-map.md', public_url_md)

    github_lines = ['# GitHub Map\n']
    for repo in GITHUB_REPOS:
        github_lines.append(f'## {repo}\n')
        github_lines.append('```text')
        github_lines.append(run(['gh', 'repo', 'view', repo, '--json', 'nameWithOwner,description,url,updatedAt,primaryLanguage', '--jq', '.']))
        github_lines.append(run(['gh', 'api', f'/repos/{repo}/commits', '--jq', '.[0:5][] | "\\(.sha[0:7]) \\(.commit.message | split("\\n")[0])"']))
        github_lines.append('```\n')
    write(PACKAGE / 'github-map.md', '\n'.join(github_lines))

    start = f'''# START HERE — LippytmAI Zo Computer Export for ChatGPT Business

Generated: {datetime.now().astimezone().isoformat()}

## Purpose

This package gives ChatGPT Business the latest usable state of the LippytmAI Zo Computer workspace, GitHub ecosystem, public pages, campaigns, skills, workflows, Web3 affiliate platform plans, GetBizFunds systems, and AI Agentic Super Synthetic Intelligence Engines AgentsBots Swarms.

## How ChatGPT Business should use this

1. Read `public-url-map.md`, `github-map.md`, and `skills-map.md`.
2. Read `workspace-files/AGENTS.md`.
3. Review the workflow files under `workspace-files/Records/Workflows/`.
4. Improve campaigns, eBooks, Web3 affiliate websites, GetBizFunds payment/wallet flows, Zapier automations, Canva briefs, GitHub specs, and AgentBots swarm systems.
5. Return structured recommendations that Zo Computer can turn into files, GitHub commits, pages, automations, or products.

## Best next prompt

Use `workspace-files/Records/Templates/ChatGPTBusiness/chatgpt-business-return-package-master-prompt.md` if present, or ask ChatGPT Business to create improved revenue-focused build plans from this export.
'''
    write(PACKAGE / 'START-HERE.md', start)

    shutil.copy2(ROOT / 'Records/Templates/ChatGPTBusiness/chatgpt-business-return-package-master-prompt.md', PACKAGE / 'chatgpt-business-return-package-master-prompt.md')

    zip_base = EXPORT_ROOT / PACKAGE.name
    shutil.make_archive(str(zip_base), 'zip', PACKAGE)
    print(PACKAGE)
    print(f'{zip_base}.zip')

if __name__ == '__main__':
    main()
