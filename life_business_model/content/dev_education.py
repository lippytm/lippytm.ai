"""Dev Education Studio -- teaches programmers and blockchain developers
through the same Creative Engine pipeline, tuned for technical accuracy:
runnable code examples and a teaching voice instead of a sales voice.

Reuses CreativeStudio's full pipeline (ebook -> audiobook -> video -> blog
-> social) by enriching the topic with teaching context before generation,
then restoring the clean topic on the resulting bundle for filenames/slugs.
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional

from .creative_studio import CreativeStudio, ContentBundle

CURRICULUM = [
    {"topic": "Smart Contract Security: Auditing Solidity Like a Pro", "track": "blockchain"},
    {"topic": "Building Your First DeFi Protocol from Scratch", "track": "blockchain"},
    {"topic": "Gas Optimization Techniques for Ethereum Smart Contracts", "track": "blockchain"},
    {"topic": "Web3 Wallet Integration: MetaMask, WalletConnect, and Beyond", "track": "blockchain"},
    {"topic": "Understanding Zero-Knowledge Proofs for Developers", "track": "blockchain"},
    {"topic": "Building a Full-Stack dApp: React + Solidity + Hardhat", "track": "blockchain"},
    {"topic": "Python AI Agent Development: From Zero to Production", "track": "programming"},
    {"topic": "AI-Assisted Coding: Using Claude as a Pair Programmer", "track": "programming"},
    {"topic": "Clean Architecture for Production Python Services", "track": "programming"},
    {"topic": "Testing Strategies That Actually Catch Bugs", "track": "programming"},
]

TEACHING_CONTEXT = (
    "Teaching context: this is for programmers and blockchain developers leveling "
    "up their skills. Include real, runnable code examples (Solidity, Python, or "
    "TypeScript as appropriate) -- never pseudocode unless explicitly teaching a "
    "concept before its implementation. Call out common bugs and security pitfalls "
    "by name. End each major section with a short hands-on exercise the learner can "
    "do immediately. No sales language, no calls to action beyond 'try this yourself.'"
)


class DevEducationStudio:
    """
    Generates full teaching bundles (ebook + audiobook + video + blog) for a
    programming/blockchain curriculum, using the same Creative Engine as the
    business content pipeline but framed for teaching rather than selling.

    Usage:
        studio = DevEducationStudio()
        bundle = studio.generate_lesson(
            "Building Your First DeFi Protocol from Scratch",
            render_real_media=True,   # produces real .mp3/.mp4 files, needs OPENAI_API_KEY
        )
        studio.write_lesson_to_disk(bundle)
    """

    def __init__(self, api_key: Optional[str] = None, openai_key: Optional[str] = None):
        self.creative = CreativeStudio(api_key=api_key, openai_key=openai_key)

    def generate_lesson(self, topic: str, render_real_media: bool = False) -> ContentBundle:
        framed_topic = f"{topic}\n\n{TEACHING_CONTEXT}"
        bundle = self.creative.full_bundle(
            framed_topic,
            include_ebook=True,
            include_audiobook=True,
            include_videos=True,
            render_real_media=render_real_media,
        )
        bundle.topic = topic  # restore the clean title for filenames/display
        return bundle

    def write_lesson_to_disk(self, bundle: ContentBundle, output_dir: str = "dist/dev_education") -> Path:
        return self.creative.write_bundle_to_disk(bundle, output_dir)


if __name__ == "__main__":
    import argparse
    import datetime as dt

    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", default=None)
    parser.add_argument("--track", choices=["blockchain", "programming"], default=None)
    parser.add_argument("--render-real-media", action="store_true")
    parser.add_argument("--output", default="dist/dev_education")
    args = parser.parse_args()

    pool = [c for c in CURRICULUM if not args.track or c["track"] == args.track]
    week = dt.date.today().isocalendar()[1]
    topic = args.topic or pool[week % len(pool)]["topic"]

    studio = DevEducationStudio()
    bundle = studio.generate_lesson(topic, render_real_media=args.render_real_media)
    path = studio.write_lesson_to_disk(bundle, args.output)
    print(f"Dev education lesson written to: {path}")
