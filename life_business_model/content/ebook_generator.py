"""Ebook Generator -- full pipeline from topic to publishable ebook.

Pipeline:
1. Topic -> outline (chapters + key points) via Claude
2. Outline -> full chapter drafts (parallel, ThreadPoolExecutor)
3. Compile -> Markdown manuscript + metadata manifest
4. Cover brief -> Canva-ready design prompt

Use cases:
- Lead magnet: "AI Automation Starter Kit" (free, drives email capture)
- Premium ebook: "$167K MRR Playbook" ($19-49, direct revenue)
- Repo-specific guides: one ebook per business unit
"""
from __future__ import annotations

import os
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path

import anthropic


@dataclass
class Chapter:
    number: int
    title: str
    summary: str
    content: str = ""
    word_count: int = 0


@dataclass
class EbookManifest:
    title: str
    subtitle: str
    author: str
    description: str
    target_audience: str
    chapters: list
    cover_brief: str = ""
    price_usd: float = 0.0
    generated_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    @property
    def total_word_count(self) -> int:
        return sum(c.word_count for c in self.chapters)

    @property
    def estimated_reading_minutes(self) -> int:
        return self.total_word_count // 200

    def to_dict(self) -> dict:
        d = asdict(self)
        return d


class EbookGenerator:
    """Generates complete ebooks from a topic using Claude."""

    AUTHOR = "Charles Lipshay"
    BRAND = "lippytm.ai"

    def __init__(self, api_key: str | None = None):
        self.client = anthropic.Anthropic(api_key=api_key or os.environ.get("ANTHROPIC_API_KEY"))

    def generate_outline(self, topic: str, target_audience: str, chapter_count: int = 8) -> dict:
        prompt = f"""Create a complete ebook outline.

Topic: {topic}
Target audience: {target_audience}
Author: {self.AUTHOR} ({self.BRAND})
Chapter count: {chapter_count}

Return JSON only:
{{
  "title": "...",
  "subtitle": "...",
  "description": "2-3 sentence back-cover description",
  "chapters": [
    {{"number": 1, "title": "...", "summary": "2-3 sentences on what this chapter covers"}}
  ]
}}

Make the title compelling and specific. Chapters should build progressively,
starting with foundational concepts and ending with advanced implementation."""

        resp = self.client.messages.create(
            model="claude-opus-4-8",
            max_tokens=1500,
            messages=[{"role": "user", "content": prompt}],
        )
        return json.loads(resp.content[0].text)

    def _write_chapter(self, chapter_info: dict, book_context: dict) -> Chapter:
        prompt = f"""Write Chapter {chapter_info['number']}: \"{chapter_info['title']}\"

Book: \"{book_context['title']}\" -- {book_context['description']}
Target audience: {book_context.get('target_audience', 'AI entrepreneurs')}
Chapter summary: {chapter_info['summary']}

Write 1200-1800 words of genuinely useful content. Requirements:
- Open with a hook (story, statistic, or provocative question)
- Use H2/H3 markdown subheadings to organize
- Include at least one concrete example or case study
- Include actionable takeaways (numbered list)
- Close with a transition to the next chapter's theme
- Tone: direct, peer-to-peer, no corporate fluff
- Format: Markdown"""

        resp = self.client.messages.create(
            model="claude-opus-4-8",
            max_tokens=3000,
            messages=[{"role": "user", "content": prompt}],
        )
        content = resp.content[0].text
        return Chapter(
            number=chapter_info["number"],
            title=chapter_info["title"],
            summary=chapter_info["summary"],
            content=content,
            word_count=len(content.split()),
        )

    def generate(self, topic: str, target_audience: str = "AI entrepreneurs and SMB owners",
                 chapter_count: int = 8, price_usd: float = 0.0) -> EbookManifest:
        outline = self.generate_outline(topic, target_audience, chapter_count)
        book_context = {**outline, "target_audience": target_audience}

        chapters = []
        with ThreadPoolExecutor(max_workers=4) as pool:
            futures = {
                pool.submit(self._write_chapter, ch, book_context): ch["number"]
                for ch in outline["chapters"]
            }
            for future in as_completed(futures):
                chapters.append(future.result())
        chapters.sort(key=lambda c: c.number)

        cover_prompt = f"""Write a Canva/DALL-E design brief for an ebook cover.

Title: {outline['title']}
Subtitle: {outline['subtitle']}
Genre: AI business / entrepreneurship
Style: modern, bold, tech-forward, dark background with accent color

Describe: color palette, typography style, imagery/iconography, composition.
Max 100 words."""
        cover_resp = self.client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=200,
            messages=[{"role": "user", "content": cover_prompt}],
        )

        return EbookManifest(
            title=outline["title"],
            subtitle=outline["subtitle"],
            author=self.AUTHOR,
            description=outline["description"],
            target_audience=target_audience,
            chapters=chapters,
            cover_brief=cover_resp.content[0].text,
            price_usd=price_usd,
        )

    def to_markdown(self, manifest: EbookManifest) -> str:
        parts = [
            f"# {manifest.title}",
            f"## {manifest.subtitle}",
            f"\n*by {manifest.author} -- {self.BRAND}*\n",
            f"> {manifest.description}\n",
            "---\n",
        ]
        for ch in manifest.chapters:
            parts.append(f"\n# Chapter {ch.number}: {ch.title}\n")
            parts.append(ch.content)
            parts.append("\n---\n")
        return "\n".join(parts)

    def write_to_disk(self, manifest: EbookManifest, output_dir: str = "dist/ebooks") -> Path:
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        slug = re.sub(r"[^a-z0-9]+", "-", manifest.title.lower()).strip("-")
        md_path = out / f"{slug}.md"
        md_path.write_text(self.to_markdown(manifest), encoding="utf-8")

        manifest_dict = manifest.to_dict()
        manifest_dict["chapters"] = [asdict(c) for c in manifest.chapters]
        manifest_path = out / f"{slug}.manifest.json"
        manifest_path.write_text(json.dumps(manifest_dict, indent=2), encoding="utf-8")
        return md_path


LEAD_MAGNET_TOPICS = [
    {
        "topic": "AI Automation Starter Kit: How to Replace an $8K/mo Team with $200/mo in AI Tools",
        "audience": "Small business owners 10-200 employees",
        "chapters": 6,
        "price": 0.0,
    },
    {
        "topic": "The $167K MRR Playbook: Building a Business of Businesses with AI Swarms",
        "audience": "AI entrepreneurs and indie hackers",
        "chapters": 10,
        "price": 29.0,
    },
    {
        "topic": "Twin.so Mastery: Turn Your AI Twin into a 24/7 Sales Machine",
        "audience": "Affiliate marketers and SaaS founders",
        "chapters": 7,
        "price": 19.0,
    },
]


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", default=LEAD_MAGNET_TOPICS[0]["topic"])
    parser.add_argument("--output", default="dist/ebooks")
    args = parser.parse_args()

    gen = EbookGenerator()
    manifest = gen.generate(args.topic)
    path = gen.write_to_disk(manifest, args.output)
    print(f"Ebook written to: {path}")
    print(f"Word count: {manifest.total_word_count} ({manifest.estimated_reading_minutes} min read)")
