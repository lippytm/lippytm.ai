#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/home/workspace')
OUT_ROOT = ROOT / 'Records' / 'Imports' / 'ChatGPT Business' / 'CommandPackets'

KEYWORDS = {
    'getbizfunds': ('GetBizFunds packet', 'Records/Workflows', 'lippytmai.getbizfunds.com-'),
    'funding': ('GetBizFunds packet', 'Campaigns', 'lippytmai.getbizfunds.com-'),
    'ebook': ('eBook packet', 'Ebooks', 'lippytm.ai'),
    'sales page': ('campaign packet', 'Campaigns', 'lippytm.ai'),
    'campaign': ('campaign packet', 'Campaigns', 'lippytm.ai'),
    'zapier': ('Zapier packet', 'Records/Workflows', 'lippytm.ai'),
    'canva': ('Canva packet', 'Campaigns', 'lippytm.ai'),
    'github': ('GitHub sync packet', 'Records/Workflows', 'lippytm.ai'),
    'skill': ('skill packet', 'Skills', 'lippytm.ai'),
    'agent': ('AgentBot swarm packet', 'Records/Workflows', 'lippytm.ai'),
    'swarm': ('AgentBot swarm packet', 'Records/Workflows', 'lippytm.ai'),
    'web3': ('Web3 affiliate packet', 'Records/Workflows', 'lippytm.ai'),
    'wallet': ('payment-wallet packet', 'Records/Workflows', 'lippytmai.getbizfunds.com-'),
    'payment': ('payment-wallet packet', 'Records/Workflows', 'lippytmai.getbizfunds.com-'),
    'crypto': ('payment-wallet packet', 'Records/Workflows', 'lippytmai.getbizfunds.com-'),
    'code': ('code/spec packet', 'Records/Workflows', 'lippytm.ai'),
    'programming': ('education packet', 'Campaigns', 'lippytm.ai'),
    'blockchain': ('education packet', 'Campaigns', 'lippytm.ai'),
    'robotics': ('education packet', 'Campaigns', 'lippytm.ai'),
}

SENSITIVE = ['payment', 'wallet', 'crypto', 'funding', 'legal', 'tax', 'investment', 'send email', 'publish', 'delete']


def slugify(text: str) -> str:
    text = re.sub(r'[^a-zA-Z0-9]+', '-', text.lower()).strip('-')
    return text[:60] or 'packet'


def classify(text: str):
    low = text.lower()
    for key, value in KEYWORDS.items():
        if key in low:
            return value
    return ('general planning packet', 'Records/Plans', 'lippytm.ai')


def split_sections(text: str):
    sections = re.split(r'\n(?=#{1,3}\s+)', text)
    if len(sections) == 1:
        paras = [p.strip() for p in re.split(r'\n\s*\n', text) if p.strip()]
        return paras[:50]
    return [s.strip() for s in sections if s.strip()]


def main():
    parser = argparse.ArgumentParser(description='Route ChatGPT Business output into Zo command packets.')
    parser.add_argument('source', help='Markdown/text file to route')
    args = parser.parse_args()

    src = Path(args.source).expanduser().resolve()
    text = src.read_text(errors='ignore')
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d-%H%M%S')
    out_dir = OUT_ROOT / f'{stamp}-{slugify(src.stem)}'
    out_dir.mkdir(parents=True, exist_ok=True)

    packets = []
    for i, section in enumerate(split_sections(text), 1):
        task_type, target_area, target_repo = classify(section)
        title_line = section.splitlines()[0].strip('# ').strip()[:90] or f'Packet {i}'
        approval = any(word in section.lower() for word in SENSITIVE)
        risk = 'high' if any(word in section.lower() for word in ['wallet', 'crypto', 'payment', 'legal', 'tax', 'investment']) else ('medium' if approval else 'low')
        packet = {
            'packet_id': f'{stamp}-{i:03d}-{slugify(title_line)}',
            'source_file': str(src),
            'title': title_line,
            'task_type': task_type,
            'target_area': target_area,
            'target_repo': target_repo,
            'approval_required': approval,
            'risk_level': risk,
            'suggested_next_step': 'Review, promote to durable workspace path, then sync to GitHub if approved.',
            'content_excerpt': section[:1200],
        }
        packets.append(packet)
        (out_dir / f"{packet['packet_id']}.json").write_text(json.dumps(packet, indent=2))

    index = out_dir / 'command-packet-index.md'
    lines = ['# ChatGPT Business Command Packet Index', '', f'Source: `{src}`', '', '| Packet | Type | Target | Repo | Risk | Approval |', '|---|---|---|---|---|---|']
    for p in packets:
        lines.append(f"| `{p['packet_id']}` | {p['task_type']} | {p['target_area']} | {p['target_repo']} | {p['risk_level']} | {p['approval_required']} |")
    index.write_text('\n'.join(lines) + '\n')
    print(out_dir)
    print(index)

if __name__ == '__main__':
    main()
