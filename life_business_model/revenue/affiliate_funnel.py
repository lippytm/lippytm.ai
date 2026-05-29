"""Twin.so affiliate funnel — tracking, lead capture, ManyChat flow config.

Target: $5K/mo at 30% recurring commission (~166 paying referrals).
Affiliate link: https://twin.so?via=charles-lipshay
"""
from __future__ import annotations

import os
import json
import time
import hashlib
import logging
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Optional

import anthropic

logger = logging.getLogger(__name__)

AFFILIATE_LINK = "https://twin.so?via=charles-lipshay"
AFFILIATE_PROGRAM = "Twin.so"
COMMISSION_RATE = 0.30
MONTHLY_TARGET_REFERRALS = 166
AVG_PLAN_VALUE = 99.0  # USD/month


@dataclass
class LeadCapture:
    email: str
    source: str  # linkedin, twitter, manychat, landing_page, direct
    utm_campaign: str = ""
    utm_content: str = ""
    name: str = ""
    company: str = ""
    interest_score: int = 0  # 0-100, set by Claude qualification
    segment: str = ""  # ai_entrepreneur, business_owner, developer, marketer
    captured_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    converted: bool = False
    conversion_value: float = 0.0

    @property
    def lead_id(self) -> str:
        return hashlib.md5(f"{self.email}{self.captured_at}".encode()).hexdigest()[:12]


@dataclass
class AffiliateMetrics:
    month: str = field(default_factory=lambda: datetime.now(timezone.utc).strftime("%Y-%m"))
    clicks: int = 0
    leads_captured: int = 0
    trials_started: int = 0
    conversions: int = 0
    mrr_generated: float = 0.0
    commission_earned: float = 0.0
    top_source: str = ""

    @property
    def click_to_lead_rate(self) -> float:
        return self.leads_captured / self.clicks if self.clicks else 0.0

    @property
    def lead_to_conversion_rate(self) -> float:
        return self.conversions / self.leads_captured if self.leads_captured else 0.0

    @property
    def progress_to_target(self) -> float:
        return self.commission_earned / (MONTHLY_TARGET_REFERRALS * AVG_PLAN_VALUE * COMMISSION_RATE)


class AffiliateFunnel:
    """End-to-end affiliate funnel manager for Twin.so."""

    SEGMENTS = {
        "ai_entrepreneur": {
            "description": "Building AI-powered businesses, interested in scaling",
            "pain_points": ["too many manual tasks", "hard to scale", "need 24/7 presence"],
            "cta": "Create your AI twin to close deals while you sleep",
        },
        "business_owner": {
            "description": "Traditional or online business owners 10-200 employees",
            "pain_points": ["high customer acquisition cost", "sales team bottleneck", "inconsistent follow-up"],
            "cta": "Let an AI version of you handle 80% of sales calls",
        },
        "developer": {
            "description": "Engineers building AI products or automating their workflow",
            "pain_points": ["want to monetize AI skills", "need to demo 24/7", "async-first workflow"],
            "cta": "Ship an AI sales agent in under an hour",
        },
        "marketer": {
            "description": "Growth hackers, content creators, agency owners",
            "pain_points": ["lead quality", "follow-up speed", "personalization at scale"],
            "cta": "Qualify and convert leads 10x faster with your AI twin",
        },
    }

    CONTENT_HOOKS = [
        {
            "platform": "linkedin",
            "hook": "I automated 85% of my business with AI. Here's the exact stack:",
            "body": "→ Claude AI swarms for strategy\n→ Zapier for cross-platform sync\n→ Twin.so for AI-powered sales calls\n→ Cloudflare Workers as zero-cost backend\n\nTotal cost: ~$200/mo. Time saved: 40+ hours/week.",
            "cta": "Comment 'AI' for my free automation guide.",
            "hashtags": ["#AIAutomation", "#BusinessAutomation", "#ArtificialIntelligence", "#Entrepreneur"],
        },
        {
            "platform": "twitter",
            "hook": "How to make money with AI while you sleep (real numbers):",
            "body": "Month 1: $8.5K MRR\nMonth 3: $45K MRR target\nMonth 6: $167K MRR target\n\nKey unlock: Twin.so creates an AI version of you that handles sales 24/7.",
            "cta": f"Get started: {AFFILIATE_LINK}",
            "hashtags": ["#AI", "#PassiveIncome", "#StartupLife"],
        },
        {
            "platform": "instagram",
            "hook": "POV: Your AI twin just booked 3 sales calls while you were at the gym",
            "body": "This is the future of business.\n\nI built an AI version of myself using Twin.so.\nIt handles objections, books calls, follows up — 24/7.",
            "cta": "Link in bio to try it free.",
            "hashtags": ["#AIBusiness", "#FutureOfWork", "#AutomateEverything", "#Entrepreneur"],
        },
        {
            "platform": "youtube_short",
            "hook": "I made $5K last month promoting ONE tool. Here's how:",
            "body": "Twin.so pays 30% recurring commissions.\nI get paid every month my referrals stay subscribed.\n\n166 customers × $99/mo × 30% = $5K/mo passive income.",
            "cta": "Get your affiliate link in the description.",
            "hashtags": ["#AffiliateMarketing", "#PassiveIncome", "#AI"],
        },
    ]

    def __init__(self, api_key: str | None = None):
        self.client = anthropic.Anthropic(api_key=api_key or os.environ.get("ANTHROPIC_API_KEY"))
        self.leads: list[LeadCapture] = []
        self.metrics = AffiliateMetrics()

    def qualify_lead(self, lead: LeadCapture, context: str = "") -> LeadCapture:
        """Use Claude to score lead intent and assign segment."""
        prompt = f"""Qualify this affiliate lead for Twin.so (AI sales automation tool).

Lead info:
- Email: {lead.email}
- Source: {lead.source}
- Name: {lead.name}
- Company: {lead.company}
- Context: {context}

Available segments: {list(self.SEGMENTS.keys())}

Return JSON only:
{{"interest_score": 0-100, "segment": "<segment_name>", "reason": "<one line>"}}"""

        response = self.client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=150,
            messages=[{"role": "user", "content": prompt}],
        )
        try:
            data = json.loads(response.content[0].text)
            lead.interest_score = data.get("interest_score", 50)
            lead.segment = data.get("segment", "business_owner")
        except (json.JSONDecodeError, KeyError, IndexError):
            lead.interest_score = 50
            lead.segment = "business_owner"

        return lead

    def generate_personalized_pitch(self, lead: LeadCapture) -> str:
        """Generate a personalized affiliate pitch for a qualified lead."""
        segment_info = self.SEGMENTS.get(lead.segment, self.SEGMENTS["business_owner"])
        prompt = f"""Write a personalized 3-sentence pitch for Twin.so to send to a lead.

Lead segment: {lead.segment}
Segment description: {segment_info['description']}
Key pain points: {segment_info['pain_points']}
Primary CTA: {segment_info['cta']}
Affiliate link: {AFFILIATE_LINK}

Rules:
- First sentence: acknowledge their specific pain point
- Second sentence: explain exactly how Twin.so solves it
- Third sentence: CTA with affiliate link
- Tone: direct, peer-to-peer, no corporate speak
- Max 100 words total"""

        response = self.client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=200,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text.strip()

    def add_lead(self, lead: LeadCapture, qualify: bool = True) -> LeadCapture:
        """Capture a lead, optionally qualify it with Claude."""
        if qualify:
            lead = self.qualify_lead(lead)
        self.leads.append(lead)
        self.metrics.leads_captured += 1
        logger.info("Lead captured: %s (score=%d, segment=%s)", lead.email, lead.interest_score, lead.segment)
        return lead

    def record_conversion(self, email: str, plan_value: float = AVG_PLAN_VALUE) -> bool:
        """Mark a lead as converted and update metrics."""
        for lead in self.leads:
            if lead.email == email:
                lead.converted = True
                lead.conversion_value = plan_value
                self.metrics.conversions += 1
                self.metrics.mrr_generated += plan_value
                self.metrics.commission_earned += plan_value * COMMISSION_RATE
                return True
        return False

    def dashboard(self) -> dict:
        """Return current funnel metrics as a dict."""
        return {
            **asdict(self.metrics),
            "affiliate_link": AFFILIATE_LINK,
            "commission_rate": COMMISSION_RATE,
            "monthly_target_usd": MONTHLY_TARGET_REFERRALS * AVG_PLAN_VALUE * COMMISSION_RATE,
            "progress_pct": round(self.metrics.progress_to_target * 100, 1),
            "leads_by_segment": {
                seg: sum(1 for l in self.leads if l.segment == seg)
                for seg in self.SEGMENTS
            },
            "hot_leads": [
                asdict(l) for l in sorted(self.leads, key=lambda x: x.interest_score, reverse=True)
                if l.interest_score >= 70 and not l.converted
            ][:10],
        }

    def get_content_calendar(self, days: int = 30) -> list[dict]:
        """Generate a 30-day content calendar for affiliate promotion."""
        calendar = []
        hooks = self.CONTENT_HOOKS
        for day in range(days):
            hook = hooks[day % len(hooks)]
            calendar.append({
                "day": day + 1,
                "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                "platform": hook["platform"],
                "hook": hook["hook"],
                "body": hook["body"],
                "cta": hook["cta"],
                "hashtags": " ".join(hook["hashtags"]),
                "affiliate_link": AFFILIATE_LINK,
            })
        return calendar
