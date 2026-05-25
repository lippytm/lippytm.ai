#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/home/workspace')
RAW_ROOT = ROOT / 'Records' / 'Imports' / 'ChatGPT Business' / 'Raw'
PROCESSED_ROOT = ROOT / 'Records' / 'Imports' / 'ChatGPT Business' / 'Processed'

CATEGORIES = {
    'getbizfunds': ['getbizfunds', 'funding', 'business funding', 'loan', 'capital'],
    'web3-affiliate': ['web3', 'affiliate', 'wallet', 'crypto', 'blockchain'],
    'agent-swarm': ['agentbot', 'swarm', 'agentic', 'synthetic intelligence', 'self-healing'],
    'ebook': ['ebook', 'book', 'chapter', 'lead magnet'],
    'campaign': ['campaign', 'ad copy', 'advertising', 'social post', 'video script'],
    'automation': ['zapier', 'automation', 'workflow', 'trigger', 'routing'],
    'code-spec': ['code', 'github', 'repository', 'api', 'frontend', 'backend'],
    'canva-brief': ['canva', 'thumbnail', 'cover', 'visual', 'brand kit'],
    'prompt': ['prompt', 'chatgpt', 'claude'],
    'payment-wallet': ['stripe', 'payment', 'checkout', 'subscription', 'wallet'],
    'strategy': ['strategy', 'business model', 'monetization', 'roadmap'],
}


def slugify(text: str) -> str:
    text = re.sub(r'[^a-zA-Z0-9]+', '-', text.lower()).strip('-')
    return text[:80] or 'chatgpt-item'


def classify(text: str) -> str:
    low = text.lower()
    scores = {cat: sum(1 for k in keys if k in low) for cat, keys in CATEGORIES.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else 'general'


def extract_zip(src: Path, workdir: Path) -> Path:
    out = workdir / 'extracted'
    out.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(src) as zf:
        zf.extractall(out)
    return out


def iter_text_files(path: Path):
    if path.is_file():
        yield path
        return
    for p in path.rglob('*'):
        if p.is_file() and p.suffix.lower() in {'.json', '.md', '.txt', '.html'}:
            yield p


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return ''


def conversation_items_from_json(path: Path):
    try:
        data = json.loads(read_text(path))
    except Exception:
        return []
    items = []
    if isinstance(data, list):
        for i, item in enumerate(data):
            title = item.get('title') if isinstance(item, dict) else f'item-{i+1}'
            text = json.dumps(item, ensure_ascii=False, indent=2)
            items.append((title or f'item-{i+1}', text))
    elif isinstance(data, dict):
        title = data.get('title') or path.stem
        items.append((title, json.dumps(data, ensure_ascii=False, indent=2)))
    return items


def write_markdown(outdir: Path, title: str, source: str, text: str) -> Path:
    cat = classify(text + '\n' + title)
    name = slugify(title)
    target_dir = outdir / cat
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / f'{name}.md'
    body = f'''# {title}

- Source: `{source}`
- Category: `{cat}`
- Imported: {datetime.now(timezone.utc).isoformat()}

## Imported content

```text
{text[:50000]}
```
'''
    target.write_text(body, encoding='utf-8')
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description='Import ChatGPT Business exports or copied files into processed markdown.')
    parser.add_argument('input', help='Path to ChatGPT export ZIP, directory, or file')
    args = parser.parse_args()

    src = Path(args.input).expanduser().resolve()
    if not src.exists():
        raise SystemExit(f'Input not found: {src}')

    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d-%H%M%S')
    raw_case = RAW_ROOT / stamp
    processed_case = PROCESSED_ROOT / stamp
    raw_case.mkdir(parents=True, exist_ok=True)
    processed_case.mkdir(parents=True, exist_ok=True)

    raw_copy = raw_case / src.name
    if src.is_dir():
        shutil.copytree(src, raw_copy)
    else:
        shutil.copy2(src, raw_copy)

    working = extract_zip(raw_copy, raw_case) if raw_copy.suffix.lower() == '.zip' else raw_copy
    created = []

    for f in iter_text_files(working):
        if f.suffix.lower() == '.json':
            items = conversation_items_from_json(f)
            if items:
                for title, text in items:
                    created.append(write_markdown(processed_case, title, str(f), text))
                continue
        text = read_text(f)
        if text.strip():
            created.append(write_markdown(processed_case, f.stem, str(f), text))

    index_lines = ['# Processed ChatGPT Business Import Index', '', f'- Raw input: `{raw_copy}`', f'- Processed folder: `{processed_case}`', '', '## Files']
    for p in created:
        index_lines.append(f'- `{p.relative_to(ROOT)}`')
    index = processed_case / 'processed-index.md'
    index.write_text('\n'.join(index_lines) + '\n', encoding='utf-8')

    print(processed_case)
    print(index)
    print(f'processed_files={len(created)}')

if __name__ == '__main__':
    main()
