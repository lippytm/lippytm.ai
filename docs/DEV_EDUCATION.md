# Dev Education + Real Media Rendering

Two additions to the Creative Engine:

1. **Real audio/video rendering** — the TTS and video pipelines no longer
   stop at scripts and manifests. When `render_real_media=True`, they call
   real APIs and produce actual `.mp3` and `.mp4` files.
2. **Dev Education Studio** — a teaching-focused vertical of the same
   pipeline, aimed at making programmers and blockchain developers better
   at their craft, not at selling them anything.

## Real audio: `life_business_model/content/tts_engine.py`

`OpenAITTSEngine` calls OpenAI's `tts-1-hd` model directly. It:
- Strips `[PAUSE]`/`[EMPHASIS]` narration markers into natural pacing
- Chunks any script over ~4000 characters on sentence boundaries (the API
  caps input at 4096 chars per call)
- Concatenates multi-chunk chapters into one `.mp3` (via `pydub` if
  installed, otherwise raw MP3-frame concatenation)

```python
from life_business_model.content.tts_engine import OpenAITTSEngine

engine = OpenAITTSEngine()  # requires OPENAI_API_KEY
paths = engine.synthesize_audiobook(audiobook_manifest, "dist/audiobooks/audio")
```

`AudiobookGenerator.synthesize_real_audio(manifest)` wraps this so the
existing audiobook pipeline can opt into real synthesis with one call.

## Real video: `life_business_model/content/video_render.py`

`VideoRenderEngine` renders each scene as a dark-mode, developer-familiar
slide (Pillow), narrates it with the same TTS engine, and stitches
slides + narration into one `.mp4` with `moviepy` — no third-party
video-generation API required. This is exactly the right fidelity for
tutorial/code-walkthrough teaching content: clear voice, readable on-screen
text, paced to the narration's actual duration.

```python
from life_business_model.content.video_generator import VideoGenerator

gen = VideoGenerator()
script = gen.generate("Gas optimization tricks", format="explainer")
gen.render_video_file(script)  # -> dist/videos/rendered/*.mp4, requires OPENAI_API_KEY + moviepy + Pillow
```

Both engines degrade explicitly: missing `OPENAI_API_KEY` raises
`EnvironmentError`, missing `moviepy`/`Pillow` raises `ImportError`.
`CreativeStudio.full_bundle(..., render_real_media=True)` catches both and
records `render_error` on the bundle instead of failing the whole run, so a
content bundle still gets produced (scripts only) even if rendering can't
run in a given environment.

## Dev Education: `life_business_model/content/dev_education.py`

`DevEducationStudio` reuses `CreativeStudio` end to end but frames every
topic with `TEACHING_CONTEXT`: demand real runnable code (Solidity, Python,
TypeScript), call out bugs and security pitfalls by name, end sections with
a hands-on exercise, no sales language. The curriculum spans two tracks:

**Blockchain:** smart contract security/auditing, building a DeFi protocol
from scratch, gas optimization, wallet integration, zero-knowledge proofs,
full-stack dApp development.

**Programming:** AI agent development, AI-assisted pair programming, clean
architecture, testing strategy.

```python
from life_business_model.content.dev_education import DevEducationStudio

studio = DevEducationStudio()
bundle = studio.generate_lesson(
    "Building Your First DeFi Protocol from Scratch",
    render_real_media=True,
)
studio.write_lesson_to_disk(bundle)  # -> dist/dev_education/*_bundle.json + rendered audio/video
```

CLI:
```bash
python -m life_business_model.content.dev_education --track blockchain --render-real-media
```

## Automation

`.github/workflows/dev_education_weekly.yml` runs every Thursday, installs
`ffmpeg` (moviepy's only system dependency), generates one curriculum
lesson with real media rendering on by default, commits `dist/dev_education/`,
and notifies Slack. Toggle real rendering off via the `render_real_media`
workflow input if you want scripts only on a given run.

Required secrets: `ANTHROPIC_API_KEY` (always), `OPENAI_API_KEY` (for real
audio/video — without it the lesson bundle still generates with scripts and
manifests only), `SLACK_WEBHOOK_URL` (optional, for notifications).
