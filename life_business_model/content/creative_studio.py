"""Creative Studio -- the Content Multiplication Engine.

Takes ONE source idea and multiplies it into every format:
  Source Topic
    |-- Ebook (lead magnet or paid product)
    |     `-- Audiobook (narration script + real .mp3, when render_real_media=True)
    |-- Video series (long-form, short, explainer; real .mp4 when render_real_media=True)
    |-- Blog post (SEO-optimized)
    `-- Social posts (LinkedIn, Twitter, Instagram)

Diversity engine: uses CreativeEnsemble (Claude + ChatGPT) for headline/hook
generation so output isn't single-model-flavored.

This is the system that turns 1 hour of swarm intelligence into a week of content.
"""
from __future__ import annotations

import os
import json
import re
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path

import anthropic

from .ebook_generator import EbookGenerator
from .audiobook_generator import AudiobookGenerator
from .video_generator import VideoGenerator
from ..integrations.openai_bridge import CreativeEnsemble


@dataclass
class ContentBundle:
    topic: str
    generated_at: str
    ebook: dict = None
    audiobook: dict = None
    videos: list = field(default_factory=list)
    blog_post: str = ""
    social_posts: dict = field(default_factory=dict)
    title_options: dict = None

    def to_dict(self) -> dict:
        return asdict(self)


class CreativeStudio:
    """Orchestrates the full content multiplication pipeline."""

    def __init__(self, api_key: str | None = None, openai_key: str | None = None):
        self.client = anthropic.Anthropic(api_key=api_key or os.environ.get("ANTHROPIC_API_KEY"))
        self.ebook_gen = EbookGenerator(api_key=api_key)
        self.audiobook_gen = AudiobookGenerator(api_key=api_key)
        self.video_gen = VideoGenerator(api_key=api_key)
        self.ensemble = CreativeEnsemble(anthropic_key=api_key, openai_key=openai_key)

    def generate_title_options(self, topic: str) -> dict:
        """Use the Claude+ChatGPT ensemble for maximum headline diversity."""
        task = (f"Generate 5 distinct, high-converting title options for content about: {topic}. "
                "Vary the angle (curiosity, numbers/stats, contrarian, how-to, story). "
                "Return as a numbered list only.")
        return self.ensemble.run(task, max_tokens=400)

    def generate_blog_post(self, topic: str) -> str:
        prompt = f"""Write a 1800-word SEO-optimized blog post for lippytm.ai on: {topic}

Structure: hook intro, H2 sections with actionable content, conclusion with CTA.
Include the affiliate link naturally: https://twin.so?via=charles-lipshay
Format: Markdown."""
        resp = self.client.messages.create(
            model="claude-opus-4-8", max_tokens=3000,
            messages=[{"role": "user", "content": prompt}],
        )
        return resp.content[0].text

    def generate_social_posts(self, topic: str) -> dict:
        prompt = f"""Generate platform-native social posts for: {topic}

Return JSON: {{"linkedin": "...", "twitter": "...", "instagram_caption": "..."}}
Each optimized for its platform's format and audience expectations."""
        resp = self.client.messages.create(
            model="claude-haiku-4-5-20251001", max_tokens=800,
            messages=[{"role": "user", "content": prompt}],
        )
        try:
            return json.loads(resp.content[0].text)
        except json.JSONDecodeError:
            return {"raw": resp.content[0].text}

    def full_bundle(
        self,
        topic: str,
        include_ebook: bool = True,
        include_audiobook: bool = True,
        include_videos: bool = True,
        render_real_media: bool = False,
    ) -> ContentBundle:
        """Generate the full content bundle. If render_real_media=True, also calls
        the TTS and video-render engines to produce actual .mp3/.mp4 files
        (requires OPENAI_API_KEY, and moviepy+Pillow for video)."""
        bundle = ContentBundle(topic=topic, generated_at=datetime.now(timezone.utc).isoformat())

        bundle.title_options = self.generate_title_options(topic)

        ebook_dict = None
        if include_ebook:
            ebook_manifest = self.ebook_gen.generate(topic, chapter_count=6)
            ebook_dict = ebook_manifest.to_dict()
            ebook_dict["chapters"] = [
                {"number": c.number, "title": c.title, "summary": c.summary,
                 "content": c.content, "word_count": c.word_count}
                for c in ebook_manifest.chapters
            ]
            bundle.ebook = ebook_dict

            if include_audiobook:
                audio_manifest = self.audiobook_gen.generate_from_ebook(ebook_dict)
                bundle.audiobook = audio_manifest.to_dict()
                if render_real_media:
                    try:
                        audio_files = self.audiobook_gen.synthesize_real_audio(audio_manifest)
                        bundle.audiobook["rendered_audio_files"] = [str(p) for p in audio_files]
                    except (ImportError, EnvironmentError) as e:
                        bundle.audiobook["render_error"] = str(e)

        if include_videos:
            series = self.video_gen.generate_series(
                source_content=json.dumps(ebook_dict)[:2000] if ebook_dict else "",
                topic_base=topic,
            )
            bundle.videos = [v.to_dict() for v in series]
            if render_real_media:
                for video_dict, script_obj in zip(bundle.videos, series):
                    try:
                        rendered_path = self.video_gen.render_video_file(script_obj)
                        video_dict["rendered_video_file"] = str(rendered_path)
                    except (ImportError, EnvironmentError) as e:
                        video_dict["render_error"] = str(e)

        bundle.blog_post = self.generate_blog_post(topic)
        bundle.social_posts = self.generate_social_posts(topic)

        return bundle

    def write_bundle_to_disk(self, bundle: ContentBundle, output_dir: str = "dist/content_bundles") -> Path:
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        slug = re.sub(r"[^a-z0-9]+", "-", bundle.topic.lower()).strip("-")[:60]
        path = out / f"{slug}_bundle.json"
        path.write_text(json.dumps(bundle.to_dict(), indent=2), encoding="utf-8")
        return path


CONTENT_PIPELINE_TOPICS = [
    "How to Automate 85% of Your Business with AI Swarms",
    "Building a $167K MRR Business of Businesses",
    "The AI Twin Revolution: Selling While You Sleep",
    "20 Repos, 8 AI Swarms, 1 Automated Empire",
    "From $0 to $8.5K MRR: My First 30 Days with AI Automation",
]


if __name__ == "__main__":
    import argparse
    import datetime as dt
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", default=None)
    parser.add_argument("--output", default="dist/content_bundles")
    parser.add_argument("--render-real-media", action="store_true")
    args = parser.parse_args()

    week = dt.date.today().isocalendar()[1]
    topic = args.topic or CONTENT_PIPELINE_TOPICS[week % len(CONTENT_PIPELINE_TOPICS)]

    studio = CreativeStudio()
    bundle = studio.full_bundle(topic, render_real_media=args.render_real_media)
    path = studio.write_bundle_to_disk(bundle, args.output)
    print(f"Content bundle written to: {path}")
