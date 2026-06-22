"""Video Generator -- converts content into video scripts/storyboards, and
(when OPENAI_API_KEY + moviepy/Pillow are available) renders real mp4 files.

Formats supported:
- YouTube long-form (8-15 min): tutorial/deep-dive
- YouTube Shorts / TikTok / Reels (30-60 sec): hooks + punchy value
- Explainer/demo videos (2-4 min): product walkthroughs
- Webinar/presentation scripts (20-40 min): slide-by-slide narration

Output: scene-by-scene breakdown with visual direction, voiceover script,
on-screen text, and B-roll suggestions, plus an optional rendered mp4 via
VideoRenderEngine (slides + TTS narration -- no third-party video API needed).
"""
from __future__ import annotations

import os
import json
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path

import anthropic


@dataclass
class Scene:
    number: int
    duration_seconds: int
    visual_direction: str
    voiceover: str
    on_screen_text: str = ""
    b_roll_suggestion: str = ""


@dataclass
class VideoScript:
    title: str
    format: str
    platform: str
    total_duration_seconds: int
    hook: str
    scenes: list
    cta: str
    thumbnail_brief: str = ""
    description: str = ""
    tags: list = field(default_factory=list)

    def to_dict(self) -> dict:
        d = asdict(self)
        return d


class VideoGenerator:
    """Generates platform-specific video scripts and storyboards using Claude."""

    FORMAT_SPECS = {
        "long_form": {"duration": (480, 900), "platform": "youtube", "scene_count": (8, 12)},
        "short": {"duration": (30, 60), "platform": "tiktok", "scene_count": (4, 6)},
        "explainer": {"duration": (120, 240), "platform": "youtube", "scene_count": (6, 8)},
        "webinar": {"duration": (1200, 2400), "platform": "youtube", "scene_count": (15, 25)},
    }

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key
        self.client = anthropic.Anthropic(api_key=api_key or os.environ.get("ANTHROPIC_API_KEY"))

    def generate(self, topic: str, format: str = "short", source_content: str = "") -> VideoScript:
        spec = self.FORMAT_SPECS.get(format, self.FORMAT_SPECS["short"])
        min_dur, max_dur = spec["duration"]
        min_scenes, max_scenes = spec["scene_count"]

        source_note = f"Source material: {source_content[:2000]}" if source_content else ""
        prompt = f"""Create a complete video script for lippytm.ai (AI Business Automation brand).

Topic: {topic}
Format: {format} ({min_dur}-{max_dur} seconds, {min_scenes}-{max_scenes} scenes)
Platform: {spec['platform']}
{source_note}

Return JSON only:
{{
  "title": "...",
  "hook": "first 3-second hook line (critical for retention)",
  "scenes": [
    {{
      "number": 1,
      "duration_seconds": 5,
      "visual_direction": "what's on screen (talking head / screen recording / B-roll / text overlay)",
      "voiceover": "exact spoken words",
      "on_screen_text": "text overlay if any",
      "b_roll_suggestion": "stock footage or graphic idea"
    }}
  ],
  "cta": "exact call-to-action spoken at the end",
  "description": "YouTube/platform description with affiliate link placeholder",
  "tags": ["tag1", "tag2"]
}}

Make the hook impossible to scroll past. Front-load value. Total scene durations
must sum to approximately the target duration."""

        resp = self.client.messages.create(
            model="claude-opus-4-8",
            max_tokens=2500,
            messages=[{"role": "user", "content": prompt}],
        )
        data = json.loads(resp.content[0].text)

        scenes = [Scene(**s) for s in data["scenes"]]
        total_duration = sum(s.duration_seconds for s in scenes)

        thumbnail_resp = self.client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=150,
            messages=[{"role": "user", "content":
                f"Write a Canva/DALL-E thumbnail design brief for a video titled '{data['title']}'. "
                f"Bold, high-contrast, click-worthy. Max 60 words."}],
        )

        return VideoScript(
            title=data["title"],
            format=format,
            platform=spec["platform"],
            total_duration_seconds=total_duration,
            hook=data["hook"],
            scenes=scenes,
            cta=data["cta"],
            thumbnail_brief=thumbnail_resp.content[0].text,
            description=data.get("description", ""),
            tags=data.get("tags", []),
        )

    def generate_series(self, source_content: str, topic_base: str) -> list:
        """Generate a multi-format content series from ONE source (content multiplication)."""
        return [
            self.generate(f"{topic_base} (long-form deep dive)", "long_form", source_content),
            self.generate(f"{topic_base} (60-second hook)", "short", source_content),
            self.generate(f"{topic_base} (explainer)", "explainer", source_content),
        ]

    def render_video_file(self, script: VideoScript, output_dir: str = "dist/videos/rendered", voice: str = "onyx") -> Path:
        """Actually render a real mp4 (slides + TTS narration). Requires OPENAI_API_KEY + moviepy + Pillow."""
        from .video_render import VideoRenderEngine

        engine = VideoRenderEngine(api_key=self.api_key, voice=voice)
        slug = re.sub(r"[^a-z0-9]+", "-", script.title.lower()).strip("-")
        output_path = Path(output_dir) / f"{slug}_{script.format}.mp4"

        script_dict = script.to_dict()
        script_dict["scenes"] = [asdict(s) for s in script.scenes]
        return engine.render(script_dict, str(output_path))

    def write_to_disk(self, script: VideoScript, output_dir: str = "dist/videos") -> Path:
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        slug = re.sub(r"[^a-z0-9]+", "-", script.title.lower()).strip("-")

        script_dict = script.to_dict()
        script_dict["scenes"] = [asdict(s) for s in script.scenes]
        path = out / f"{slug}_{script.format}.json"
        path.write_text(json.dumps(script_dict, indent=2), encoding="utf-8")

        shotlist = [f"# {script.title} ({script.format}, {script.total_duration_seconds}s)\n",
                    f"**Hook:** {script.hook}\n", "## Shot List\n"]
        for s in script.scenes:
            shotlist.append(f"### Scene {s.number} ({s.duration_seconds}s)")
            shotlist.append(f"**Visual:** {s.visual_direction}")
            shotlist.append(f"**Voiceover:** {s.voiceover}")
            if s.on_screen_text:
                shotlist.append(f"**On-screen text:** {s.on_screen_text}")
            if s.b_roll_suggestion:
                shotlist.append(f"**B-roll:** {s.b_roll_suggestion}")
            shotlist.append("")
        shotlist.append(f"**CTA:** {script.cta}")

        shotlist_path = out / f"{slug}_{script.format}_shotlist.md"
        shotlist_path.write_text("\n".join(shotlist), encoding="utf-8")
        return path
