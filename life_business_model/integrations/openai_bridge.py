"""ChatGPT/OpenAI bridge -- multi-LLM ensemble alongside Claude.

Why dual-LLM: Claude and GPT have different training, different creative
tendencies, different blind spots. Running both in parallel for creative
and strategic tasks increases diversity of output and catches single-model
blind spots before they reach production.

Usage:
    bridge = OpenAIBridge()
    result = bridge.generate("Write a tagline for an AI automation tool")

    ensemble = CreativeEnsemble()
    best = ensemble.run("Generate 5 ebook title options for an AI automation guide")
"""
from __future__ import annotations

import os
import logging
from dataclasses import dataclass

import anthropic

logger = logging.getLogger(__name__)

try:
    import openai
    _OPENAI_AVAILABLE = True
except ImportError:
    _OPENAI_AVAILABLE = False


@dataclass
class LLMResponse:
    model: str
    provider: str
    content: str
    tokens_used: int = 0


class OpenAIBridge:
    """Thin wrapper around OpenAI's ChatGPT API, mirroring the Claude agent interface."""

    def __init__(self, api_key: str | None = None, model: str = "gpt-4o"):
        if not _OPENAI_AVAILABLE:
            raise ImportError("pip install openai to use OpenAIBridge")
        self.client = openai.OpenAI(api_key=api_key or os.environ.get("OPENAI_API_KEY"))
        self.model = model

    def generate(self, prompt: str, system: str = "", max_tokens: int = 1500) -> LLMResponse:
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            max_tokens=max_tokens,
            messages=messages,
        )
        return LLMResponse(
            model=self.model,
            provider="openai",
            content=response.choices[0].message.content,
            tokens_used=response.usage.total_tokens if response.usage else 0,
        )

    def generate_image_brief(self, description: str) -> str:
        """DALL-E prompt engineering for creative assets (covers, thumbnails)."""
        resp = self.generate(
            prompt=f"Write an optimized DALL-E 3 image generation prompt for: {description}",
            system="You are an expert at writing DALL-E prompts for marketing assets.",
            max_tokens=300,
        )
        return resp.content

    def text_to_speech_manifest(self, text: str, voice: str = "alloy") -> dict:
        """Build a TTS synthesis manifest for OpenAI's audio API. Returns a manifest, not bytes."""
        return {
            "provider": "openai_tts",
            "model": "tts-1-hd",
            "voice": voice,
            "input_text": text,
            "note": "Call client.audio.speech.create(model='tts-1-hd', voice=voice, input=text) to generate audio bytes.",
        }


class CreativeEnsemble:
    """Runs creative tasks through BOTH Claude and ChatGPT, then Claude synthesizes the best.

    Diversity principle: two different model families produce genuinely different
    creative angles. The synthesis step picks/merges the strongest elements from each,
    rather than defaulting to whichever model ran first.
    """

    def __init__(self, anthropic_key: str | None = None, openai_key: str | None = None):
        self.claude = anthropic.Anthropic(api_key=anthropic_key or os.environ.get("ANTHROPIC_API_KEY"))
        self.gpt_available = _OPENAI_AVAILABLE and bool(openai_key or os.environ.get("OPENAI_API_KEY"))
        if self.gpt_available:
            self.gpt = OpenAIBridge(api_key=openai_key)

    def run(self, task: str, system: str = "", max_tokens: int = 1000) -> dict:
        claude_resp = self.claude.messages.create(
            model="claude-opus-4-8",
            max_tokens=max_tokens,
            system=system or "You are a world-class creative strategist.",
            messages=[{"role": "user", "content": task}],
        )
        claude_output = claude_resp.content[0].text

        gpt_output = None
        if self.gpt_available:
            try:
                gpt_output = self.gpt.generate(task, system=system, max_tokens=max_tokens).content
            except Exception as e:
                logger.warning("OpenAI call failed, continuing Claude-only: %s", e)

        if not gpt_output:
            return {"claude": claude_output, "gpt": None, "synthesis": claude_output, "mode": "claude_only"}

        synthesis_prompt = f"""Two AI models independently responded to this task:

TASK: {task}

CLAUDE'S RESPONSE:
{claude_output}

GPT'S RESPONSE:
{gpt_output}

Synthesize the BEST possible output by combining the strongest elements of both.
Where they agree, that's high-confidence. Where they diverge, pick the more creative/effective option.
Output only the final synthesized result, no commentary."""

        synthesis = self.claude.messages.create(
            model="claude-opus-4-8",
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": synthesis_prompt}],
        )

        return {
            "claude": claude_output,
            "gpt": gpt_output,
            "synthesis": synthesis.content[0].text,
            "mode": "ensemble",
        }
