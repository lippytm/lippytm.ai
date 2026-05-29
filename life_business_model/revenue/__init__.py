"""Revenue activation layer — affiliate, email, bots, landing pages."""
from .affiliate_funnel import AffiliateFunnel, AffiliateMetrics, LeadCapture
from .email_sequences import EmailSequenceEngine, EmailSegment
from .bot_flows import BotFlowEngine, BotFlow
from .landing_pages import AffiliateLandingPage, LandingPageConfig

__all__ = [
    "AffiliateFunnel",
    "AffiliateMetrics",
    "LeadCapture",
    "EmailSequenceEngine",
    "EmailSegment",
    "BotFlowEngine",
    "BotFlow",
    "AffiliateLandingPage",
    "LandingPageConfig",
]
