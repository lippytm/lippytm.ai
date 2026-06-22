"""Real video rendering engine -- turns video scripts into actual mp4 files.

Renders each scene as a developer-familiar dark-mode slide (scene counter +
on-screen text/code) using Pillow, narrates it with OpenAI TTS, and stitches
the slides + narration into one mp4 with moviepy. No third-party video
generation API is required -- text + voice is exactly what tutorial and
code-walkthrough teaching content needs.
"""
from __future__ import annotations

import os
import textwrap
from pathlib import Path
from typing import Optional

try:
    from moviepy.editor import AudioFileClip, ImageClip, concatenate_videoclips
    _MOVIEPY_AVAILABLE = True
except ImportError:
    _MOVIEPY_AVAILABLE = False

try:
    from PIL import Image, ImageDraw, ImageFont
    _PIL_AVAILABLE = True
except ImportError:
    _PIL_AVAILABLE = False

from .tts_engine import OpenAITTSEngine

WIDTH, HEIGHT = 1920, 1080
BG_COLOR = (13, 17, 23)        # GitHub-dark style background -- developer-familiar
ACCENT_COLOR = (88, 166, 255)  # link-blue accent
TEXT_COLOR = (230, 237, 243)

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


class VideoRenderEngine:
    """Renders a VideoScript dict into a real mp4 file: slides + TTS narration."""

    def __init__(self, api_key: Optional[str] = None, voice: str = "onyx"):
        if not _MOVIEPY_AVAILABLE:
            raise ImportError("pip install moviepy to render real video files")
        if not _PIL_AVAILABLE:
            raise ImportError("pip install pillow to render slide images")
        self.tts = OpenAITTSEngine(api_key=api_key)
        self.voice = voice

    def _font(self, size: int):
        for path in FONT_CANDIDATES:
            if os.path.exists(path):
                return ImageFont.truetype(path, size)
        return ImageFont.load_default()

    def _render_slide(self, scene_number: int, total: int, visual_direction: str, on_screen_text: str) -> Image.Image:
        img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
        draw = ImageDraw.Draw(img)

        draw.text((80, 60), f"SCENE {scene_number} / {total}", font=self._font(36), fill=ACCENT_COLOR)
        draw.line([(80, 120), (WIDTH - 80, 120)], fill=ACCENT_COLOR, width=3)

        body = (on_screen_text or visual_direction or "").strip()
        wrapped = textwrap.fill(body, width=44)
        draw.multiline_text((80, 220), wrapped, font=self._font(54), fill=TEXT_COLOR, spacing=20)

        return img

    def render(self, video_script: dict, output_path: str) -> Path:
        """Render a VideoScript dict (from VideoGenerator.to_dict()) into a real mp4 file."""
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)

        scenes = video_script["scenes"]
        total = len(scenes)
        clips, tmp_assets = [], []

        for scene in scenes:
            slide = self._render_slide(
                scene["number"], total, scene["visual_direction"], scene.get("on_screen_text", "")
            )
            slide_path = out.parent / f".tmp_slide_{out.stem}_{scene['number']}.png"
            slide.save(slide_path)
            tmp_assets.append(slide_path)

            audio_path = out.parent / f".tmp_audio_{out.stem}_{scene['number']}.mp3"
            self.tts.synthesize_text(scene["voiceover"], self.voice, audio_path)
            tmp_assets.append(audio_path)

            audio_clip = AudioFileClip(str(audio_path))
            image_clip = ImageClip(str(slide_path)).set_duration(audio_clip.duration).set_audio(audio_clip)
            clips.append(image_clip)

        final = concatenate_videoclips(clips, method="compose")
        final.write_videofile(str(out), fps=24, codec="libx264", audio_codec="aac", logger=None)

        final.close()
        for clip in clips:
            clip.close()
        for asset in tmp_assets:
            asset.unlink(missing_ok=True)

        return out
