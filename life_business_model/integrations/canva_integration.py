"""Canva integration — AI-powered brand asset generation.

Live designs generated:
- Logo candidates: https://www.canva.com/d/b-b1tVWzrRb9j1L
- Logo option 2:   https://www.canva.com/d/ZMkuGM0Ek_5_jje
- Logo option 3:   https://www.canva.com/d/BPyRx-gL9EAwnt6
- Logo option 4:   https://www.canva.com/d/F1vyBnHQ68FCY0a
- Pitch deck 1:    https://www.canva.com/d/W_CAnMKyjEddu5W  (10 slides)
- Pitch deck 2:    https://www.canva.com/d/tiouAPBTGEohl4L
- Pitch deck 3:    https://www.canva.com/d/zthDv_iXkImOOl_
- Pitch deck 4:    https://www.canva.com/d/GIeP24DMv8KhiEt
"""
from .platform_hub import PlatformHub

class CanvaIntegration(PlatformHub):
    """Brand asset references and generation helpers."""

    LOGO_DESIGNS = [
        "https://www.canva.com/d/b-b1tVWzrRb9j1L",
        "https://www.canva.com/d/ZMkuGM0Ek_5_jje",
        "https://www.canva.com/d/BPyRx-gL9EAwnt6",
        "https://www.canva.com/d/F1vyBnHQ68FCY0a",
    ]

    PITCH_DECK_DESIGNS = [
        "https://www.canva.com/d/W_CAnMKyjEddu5W",  # recommended
        "https://www.canva.com/d/tiouAPBTGEohl4L",
        "https://www.canva.com/d/zthDv_iXkImOOl_",
        "https://www.canva.com/d/GIeP24DMv8KhiEt",
    ]
