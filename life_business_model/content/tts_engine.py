"""Real TTS synthesis engine -- turns narration scripts into actual audio files.

Uses OpenAI's TTS API (tts-1-hd). Requires OPENAI_API_KEY. Chunks text over
the 4096-character API limit on sentence boundaries and concatenates the
resulting audio chunks into one file per chapter/scene.
"""
from __future__ import annotations

import os
import re
from pathlib import Path
from typing import List

try:
    import openai
    _OPENAI_AVAILABLE = True
except ImportError:
    _OPENAI_AVAILABLE = False

try:
    from pydub import AudioSegment
    _PYDUB_AVAILABLE = True
except ImportError:
    _PYDUB_AVAILABLE = False

MAX_CHARS = 4000  # stay under OpenAI's 4096-char input limit per request


def _chunk_text(text: str, max_chars: int = MAX_CHARS) -> List[str]:
    """Split on sentence boundaries so no chunk cuts a sentence mid-word."""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks, current = [], ""
    for sentence in sentences:
        if len(current) + len(sentence) + 1 > max_chars:
            if current:
                chunks.append(current.strip())
            current = sentence
        else:
            current = f"{current} {sentence}".strip()
    if current:
        chunks.append(current.strip())
    return chunks or [""]


class OpenAITTSEngine:
    """Synthesizes real audio files from narration scripts via OpenAI's TTS API."""

    def __init__(self, api_key: str | None = None, model: str = "tts-1-hd"):
        if not _OPENAI_AVAILABLE:
            raise ImportError("pip install openai to synthesize real audio")
        key = api_key or os.environ.get("OPENAI_API_KEY")
        if not key:
            raise EnvironmentError("OPENAI_API_KEY not set -- required to synthesize real audio")
        self.client = openai.OpenAI(api_key=key)
        self.model = model

    def _speak_chunk(self, text: str, voice: str, output_path: Path) -> None:
        with self.client.audio.speech.with_streaming_response.create(
            model=self.model, voice=voice, input=text
        ) as response:
            response.stream_to_file(str(output_path))

    def synthesize_text(self, text: str, voice: str, output_path: Path) -> Path:
        """Synthesize one narration script (chunked if needed) into a single audio file."""
        clean = (
            text.replace("[PAUSE]", " ... ")
            .replace("[EMPHASIS]", "")
            .replace("[/EMPHASIS]", "")
        )
        chunks = _chunk_text(clean)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        if len(chunks) == 1:
            self._speak_chunk(chunks[0], voice, output_path)
            return output_path

        part_paths = []
        for i, chunk in enumerate(chunks):
            part_path = output_path.with_suffix(f".part{i:02d}.mp3")
            self._speak_chunk(chunk, voice, part_path)
            part_paths.append(part_path)

        self._concatenate(part_paths, output_path)
        for p in part_paths:
            p.unlink(missing_ok=True)
        return output_path

    def _concatenate(self, parts: List[Path], output_path: Path) -> None:
        if _PYDUB_AVAILABLE:
            combined = AudioSegment.empty()
            for part in parts:
                combined += AudioSegment.from_mp3(str(part))
            combined.export(str(output_path), format="mp3")
        else:
            # MP3 frames concatenate cleanly enough for playback without pydub/ffmpeg
            with open(output_path, "wb") as out:
                for part in parts:
                    out.write(part.read_bytes())

    def synthesize_audiobook(self, audiobook_manifest, output_dir: str = "dist/audiobooks/audio") -> List[Path]:
        """Synthesize every chapter of an AudiobookManifest into a real mp3 file."""
        out = Path(output_dir)
        paths = []
        for ch in audiobook_manifest.chapters:
            file_path = out / f"chapter_{ch.number:02d}.mp3"
            self.synthesize_text(ch.narration_script, audiobook_manifest.narrator_voice, file_path)
            paths.append(file_path)
        return paths
