"""Audiobook Generator -- converts ebook chapters into TTS-ready narration scripts.

Pipeline:
1. Markdown chapter -> cleaned narration script (strip markdown, add pacing)
2. Script -> pacing markup ([PAUSE], [EMPHASIS]) for natural delivery
3. TTS manifest: chapter audio file naming, voice selection, synthesis instructions
4. Integration points: OpenAI TTS (tts-1-hd) or ElevenLabs

Note: actual audio synthesis requires an API call with a TTS provider + valid key.
This module prepares production-ready scripts and manifests for that step.
"""
from __future__ import annotations

import os
import re
import json
from dataclasses import dataclass, asdict
from pathlib import Path

import anthropic

VOICE_PROFILES = {
    "alloy": "Neutral, balanced -- good for business/educational content",
    "echo": "Warm, conversational -- good for narrative/story content",
    "fable": "Expressive, storytelling -- good for case studies",
    "onyx": "Deep, authoritative -- good for strategic/executive content",
    "nova": "Energetic, upbeat -- good for marketing/motivational content",
    "shimmer": "Soft, calm -- good for meditative/reflective content",
}


@dataclass
class AudioChapter:
    number: int
    title: str
    narration_script: str
    estimated_duration_minutes: float
    voice: str
    pause_markers: int = 0


@dataclass
class AudiobookManifest:
    title: str
    author: str
    narrator_voice: str
    chapters: list
    total_duration_minutes: float = 0.0
    tts_provider: str = "openai_tts"
    tts_model: str = "tts-1-hd"

    def to_dict(self) -> dict:
        d = asdict(self)
        return d


class AudiobookGenerator:
    """Converts ebook manuscripts into audiobook-ready narration scripts."""

    WORDS_PER_MINUTE = 150

    def __init__(self, api_key: str | None = None):
        self.client = anthropic.Anthropic(api_key=api_key or os.environ.get("ANTHROPIC_API_KEY"))

    def _clean_markdown(self, text: str) -> str:
        text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)
        text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
        text = re.sub(r"\*(.+?)\*", r"\1", text)
        text = re.sub(r"`(.+?)`", r"\1", text)
        text = re.sub(r"```[\s\S]*?```", "", text)
        text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
        text = re.sub(r"^[-*]\s+", "", text, flags=re.MULTILINE)
        text = re.sub(r"^\d+\.\s+", "", text, flags=re.MULTILINE)
        return text.strip()

    def chapter_to_narration(self, chapter_title: str, chapter_content: str, chapter_number: int) -> str:
        """Use Claude to convert written content into natural spoken narration."""
        cleaned = self._clean_markdown(chapter_content)
        prompt = f"""Convert this written chapter into a natural AUDIOBOOK NARRATION SCRIPT.

Chapter {chapter_number}: {chapter_title}

Original text:
{cleaned[:4000]}

Rules for the narration script:
- Add a spoken chapter intro: \"Chapter {chapter_number}: {chapter_title}\"
- Convert bullet/numbered lists into flowing spoken sentences (\"First... Second... Finally...\")
- Add natural pauses with [PAUSE] markers at section transitions
- Add emphasis markers [EMPHASIS]word[/EMPHASIS] for key terms (sparingly, 3-5 per chapter)
- Remove any text that only makes sense visually (e.g., \"see the table below\")
- Keep the same information and structure, just optimized for listening
- End with a brief transition: \"In the next chapter, we'll explore...\"

Output the narration script only."""

        resp = self.client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=3000,
            messages=[{"role": "user", "content": prompt}],
        )
        return resp.content[0].text

    def generate_from_ebook(self, ebook_manifest: dict, voice: str = "onyx") -> AudiobookManifest:
        """Generate full audiobook manifest from an EbookGenerator manifest dict."""
        audio_chapters = []
        for ch in ebook_manifest["chapters"]:
            script = self.chapter_to_narration(ch["title"], ch["content"], ch["number"])
            word_count = len(script.split())
            duration = round(word_count / self.WORDS_PER_MINUTE, 1)
            audio_chapters.append(AudioChapter(
                number=ch["number"],
                title=ch["title"],
                narration_script=script,
                estimated_duration_minutes=duration,
                voice=voice,
                pause_markers=script.count("[PAUSE]"),
            ))

        total_duration = sum(c.estimated_duration_minutes for c in audio_chapters)
        return AudiobookManifest(
            title=ebook_manifest["title"],
            author=ebook_manifest["author"],
            narrator_voice=voice,
            chapters=audio_chapters,
            total_duration_minutes=round(total_duration, 1),
        )

    def tts_synthesis_instructions(self, manifest: AudiobookManifest) -> list:
        """Generate the exact API calls needed to synthesize audio (for execution with valid keys)."""
        instructions = []
        for ch in manifest.chapters:
            clean_script = ch.narration_script.replace("[PAUSE]", "... ").replace("[EMPHASIS]", "").replace("[/EMPHASIS]", "")
            instructions.append({
                "chapter": ch.number,
                "output_file": f"chapter_{ch.number:02d}.mp3",
                "api_call": "openai.audio.speech.create",
                "params": {
                    "model": manifest.tts_model,
                    "voice": manifest.narrator_voice,
                    "input": clean_script[:4096],
                    "response_format": "mp3",
                },
                "needs_chunking": len(clean_script) > 4096,
            })
        return instructions

    def write_to_disk(self, manifest: AudiobookManifest, output_dir: str = "dist/audiobooks") -> Path:
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        slug = re.sub(r"[^a-z0-9]+", "-", manifest.title.lower()).strip("-")

        for ch in manifest.chapters:
            script_path = out / f"{slug}_ch{ch.number:02d}_script.txt"
            script_path.write_text(ch.narration_script, encoding="utf-8")

        manifest_dict = manifest.to_dict()
        manifest_dict["chapters"] = [asdict(c) for c in manifest.chapters]
        manifest_path = out / f"{slug}.manifest.json"
        manifest_path.write_text(json.dumps(manifest_dict, indent=2), encoding="utf-8")

        instructions_path = out / f"{slug}.tts_instructions.json"
        instructions_path.write_text(
            json.dumps(self.tts_synthesis_instructions(manifest), indent=2), encoding="utf-8"
        )
        return manifest_path
