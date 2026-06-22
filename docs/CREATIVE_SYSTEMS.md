# Creative Environments -- Multi-LLM Content Systems

## Overview

The Creative Studio multiplies ONE idea into every content format using a
dual-LLM ensemble (Claude + ChatGPT) for maximum creative diversity, then
publishes through GitHub Actions automation with Slack notifications.

## Architecture

```
                    Topic / Idea
                 (from BI swarm or
                   manual input)
                         |
        +----------------+----------------+
        |                |                |
   Ebook Gen        Video Gen       Blog + Social
   (Claude)          (Claude)          (Claude)
        |                |
   Audiobook Gen   3 formats: long-form,
   (TTS scripts)    short, explainer

   CreativeEnsemble (Claude + ChatGPT)
   used for: titles, hooks, headlines -- diversity layer
```

## The 3 Pillars

### 1. ChatGPT Integration (`life_business_model/integrations/openai_bridge.py`)
- `OpenAIBridge`: thin wrapper mirroring the Claude agent interface
- `CreativeEnsemble`: runs creative tasks through BOTH models, Claude synthesizes the best elements of each
- Use cases: ebook titles, video hooks, ad copy variations -- anywhere creative diversity beats single-model consistency
- Setup: `pip install openai`, set `OPENAI_API_KEY`
- Degrades gracefully to Claude-only if no OpenAI key is set

### 2. GitHub Automation (`.github/workflows/content_factory_weekly.yml`)
- Runs every Monday 9AM UTC
- Rotates through `CONTENT_PIPELINE_TOPICS` (or accepts a manual topic via workflow_dispatch)
- Generates a full bundle: ebook + audiobook scripts + 3 video formats + blog + social posts
- Commits everything to `dist/` on the swarms branch
- Manual trigger: GitHub Actions tab -> Weekly Content Factory -> Run workflow

### 3. Slack Notifications
- Pipeline completion alert posted via `SLACK_WEBHOOK_URL` secret
- Runs on success AND failure (`if: always()`) so silent failures are caught
- Weekly digest links back to the generated `dist/content_bundles/` files

## Content Formats Generated Per Topic

| Format | Module | Output | Approx. Time |
|---|---|---|---|
| Ebook (6 ch, ~9K words) | `ebook_generator.py` | Markdown + manifest | ~3 min (parallel chapters) |
| Audiobook scripts | `audiobook_generator.py` | TTS-ready scripts + manifest | ~2 min |
| Long-form video (8-15 min) | `video_generator.py` | Shot list + script | ~30 sec |
| Short video (30-60 sec) | `video_generator.py` | Shot list + script | ~30 sec |
| Explainer video (2-4 min) | `video_generator.py` | Shot list + script | ~30 sec |
| Blog post (1800 words) | `creative_studio.py` | SEO-optimized Markdown | ~30 sec |
| Social posts (3 platforms) | `creative_studio.py` | Platform-native copy | ~20 sec |
| Title/hook options | `openai_bridge.py` ensemble | Claude+GPT synthesized list | ~15 sec |

**Total: roughly 7 minutes to generate a week's worth of content from one topic.**

## Setup

```bash
pip install anthropic openai
export ANTHROPIC_API_KEY=sk-ant-...
export OPENAI_API_KEY=sk-...        # optional, enables ensemble mode
export SLACK_WEBHOOK_URL=https://...  # for GitHub Actions notification step

# Generate one bundle manually
python -m life_business_model.content.creative_studio --topic "How to Automate 85% of Your Business with AI Swarms"
```

## Revenue Path

- **Ebooks**: free lead magnets grow the email list; $19-49 paid ebooks are direct revenue
- **Audiobooks**: upsell to ebook buyers (+$10), or distribute via Audible/Spotify
- **Videos**: YouTube ad revenue + organic lead generation + affiliate CTAs
- **Blog**: SEO-compounding traffic -> email capture -> Twin.so affiliate conversions
- **Social**: daily presence -> audience growth feeding every channel above

## TTS Audio Synthesis (Next Step)

The audiobook generator produces narration *scripts*, not audio files, since no
TTS API key is configured in this environment. To synthesize actual audio:

```python
from openai import OpenAI
client = OpenAI()
with open("chapter_01.mp3", "wb") as f:
    response = client.audio.speech.create(
        model="tts-1-hd", voice="onyx", input=open("chapter_01_script.txt").read()
    )
    f.write(response.content)
```

Or use ElevenLabs for higher-quality voice cloning/narration.
