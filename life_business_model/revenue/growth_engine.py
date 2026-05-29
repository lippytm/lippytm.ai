"""Growth engine — orchestrates all revenue activation channels together.

Coordinates: affiliate funnel + email sequences + bot flows + landing pages
into a unified daily revenue activation pipeline.
"""
from __future__ import annotations

import os
import json
import logging
from datetime import datetime, timezone
from dataclasses import dataclass, asdict
from typing import Optional

import anthropic

from .affiliate_funnel import AffiliateFunnel, LeadCapture, AFFILIATE_LINK
from .email_sequences import EmailSequenceEngine, EmailSegment
from .bot_flows import BotFlowEngine
from .landing_pages import AffiliateLandingPage

logger = logging.getLogger(__name__)


@dataclass
class GrowthReport:
    date: str
    total_leads: int
    qualified_leads: int
    conversions: int
    mrr_generated: float
    commission_earned: float
    top_channel: str
    ai_recommendations: str
    next_actions: list[str]

    def to_dict(self) -> dict:
        return asdict(self)


class GrowthEngine:
    """Unified revenue activation orchestrator."""

    REVENUE_TARGETS = {
        "month_1": {"mrr": 8500, "affiliate_commission": 500, "leads": 50},
        "month_3": {"mrr": 45000, "affiliate_commission": 2000, "leads": 300},
        "month_6": {"mrr": 172000, "affiliate_commission": 5000, "leads": 1000},
    }

    def __init__(self, api_key: str | None = None):
        api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.client = anthropic.Anthropic(api_key=api_key)
        self.affiliate = AffiliateFunnel(api_key=api_key)
        self.email_engine = EmailSequenceEngine(api_key=api_key)
        self.bot_engine = BotFlowEngine(api_key=api_key)
        self.landing_page = AffiliateLandingPage()

    def daily_briefing(self) -> GrowthReport:
        """Generate a daily growth briefing using Claude."""
        dashboard = self.affiliate.dashboard()
        prompt = f"""You are the revenue growth AI for lippytm.ai, a Business of Businesses targeting $167K MRR.

Today's metrics:
{json.dumps(dashboard, indent=2)}

Targets:
{json.dumps(self.REVENUE_TARGETS, indent=2)}

Affiliate link: {AFFILIATE_LINK}

Generate a concise daily growth briefing:
1. Current trajectory vs target (1 sentence)
2. Top 3 immediate actions to accelerate revenue TODAY
3. Which channel to prioritize this week
4. One creative tactic not yet tried

Format as JSON:
{{
  "trajectory": "...",
  "top_3_actions": ["...", "...", "..."],
  "priority_channel": "...",
  "creative_tactic": "..."
}}"""

        response = self.client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=600,
            messages=[{"role": "user", "content": prompt}],
        )

        try:
            ai_data = json.loads(response.content[0].text)
        except (json.JSONDecodeError, IndexError):
            ai_data = {
                "trajectory": "Analysis pending",
                "top_3_actions": ["Post affiliate content", "Follow up hot leads", "Test new bot flow"],
                "priority_channel": "linkedin",
                "creative_tactic": "DM everyone who liked your last post",
            }

        return GrowthReport(
            date=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            total_leads=dashboard["leads_by_segment"] and sum(dashboard["leads_by_segment"].values()) or 0,
            qualified_leads=len(dashboard.get("hot_leads", [])),
            conversions=dashboard.get("conversions", 0),
            mrr_generated=dashboard.get("mrr_generated", 0.0),
            commission_earned=dashboard.get("commission_earned", 0.0),
            top_channel=dashboard.get("top_source", "linkedin"),
            ai_recommendations=ai_data.get("trajectory", ""),
            next_actions=ai_data.get("top_3_actions", []),
        )

    def content_calendar_export(self, days: int = 30) -> str:
        """Export 30-day content calendar as JSON string."""
        calendar = self.affiliate.get_content_calendar(days)
        return json.dumps(calendar, indent=2)

    def bot_export_for_manychat(self) -> str:
        """Export bot flows as ManyChat import JSON."""
        return json.dumps(self.bot_engine.export_manychat(), indent=2)

    def generate_landing_page(self, output_dir: str = "dist/affiliate") -> str:
        """Generate and write landing page, return path."""
        path = self.landing_page.write_to_disk(output_dir)
        return str(path)

    def full_activation_report(self) -> dict:
        """Run all activation components and return unified report."""
        briefing = self.daily_briefing()
        return {
            "activation_report": briefing.to_dict(),
            "affiliate_dashboard": self.affiliate.dashboard(),
            "email_sequences": self.email_engine.get_all_sequences_summary(),
            "bot_flows": self.bot_engine.get_flow_stats(),
            "affiliate_link": AFFILIATE_LINK,
            "targets": self.REVENUE_TARGETS,
        }


if __name__ == "__main__":
    engine = GrowthEngine()
    report = engine.full_activation_report()
    print(json.dumps(report, indent=2))
