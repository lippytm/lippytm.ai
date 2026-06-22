"""Creative content systems -- ebooks, audiobooks, videos, blog, social.

The Content Multiplication Engine: turns one topic into every format, and
(when render_real_media=True) renders real .mp3/.mp4 files via the TTS and
video-render engines.
"""
from .ebook_generator import EbookGenerator, EbookManifest, Chapter
from .audiobook_generator import AudiobookGenerator, AudiobookManifest, AudioChapter
from .video_generator import VideoGenerator, VideoScript, Scene
from .creative_studio import CreativeStudio, ContentBundle
from .dev_education import DevEducationStudio, CURRICULUM

__all__ = [
    "EbookGenerator", "EbookManifest", "Chapter",
    "AudiobookGenerator", "AudiobookManifest", "AudioChapter",
    "VideoGenerator", "VideoScript", "Scene",
    "CreativeStudio", "ContentBundle",
    "DevEducationStudio", "CURRICULUM",
]
