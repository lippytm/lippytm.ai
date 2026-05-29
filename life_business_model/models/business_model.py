"""Codified Life/Business Model — the complete lippytm Business of Businesses data structure."""

from dataclasses import dataclass, field
from typing import List, Dict, Any
from enum import Enum
from datetime import datetime


class BusinessPhase(Enum):
    FOUNDATION = "foundation"    # Months 1-3
    EXPANSION = "expansion"      # Months 4-6
    SCALE = "scale"              # Months 7-12
    DOMINANCE = "dominance"      # Year 2+


class RevenueType(Enum):
    RECURRING = "recurring"
    ONE_TIME = "one_time"
    COMMISSION = "commission"
    TOKEN = "token"
    DATA = "data"
    YIELD = "yield"


@dataclass
class RevenueStream:
    name: str
    revenue_type: RevenueType
    monthly_target: float
    current_mrr: float = 0.0
    monthly_growth_rate: float = 0.10
    active: bool = True
    description: str = ""
    automation_level: float = 0.0  # 0.0 – 1.0


@dataclass
class BusinessUnit:
    name: str
    repository: str
    purpose: str
    revenue_streams: List[RevenueStream] = field(default_factory=list)
    kpis: Dict[str, Any] = field(default_factory=dict)
    swarm_type: str = ""
    phase: BusinessPhase = BusinessPhase.FOUNDATION
    ai_automation_pct: float = 0.0

    @property
    def monthly_revenue_target(self) -> float:
        return sum(s.monthly_target for s in self.revenue_streams)

    @property
    def current_mrr(self) -> float:
        return sum(s.current_mrr for s in self.revenue_streams)


@dataclass
class LifeBusinessModel:
    """
    The complete codified Life/Business Model for lippytm.

    This is a "Business of Businesses" — an AI-automated portfolio of
    interdependent platforms, each powered by specialized swarms that
    generate compounding, largely passive revenue.

    Life pillars:
      Wealth  — $2M+ ARR, 70% passive, AI-automated
      Freedom — <20 hrs/week, location-independent
      Impact  — 100K+ users served, 1K+ businesses empowered
      Legacy  — open knowledge, communities, long-term value
    """

    owner: str = "Charles Lipshay (lippytm)"
    vision: str = (
        "Build the most powerful AI-driven Business of Businesses: "
        "20 autonomous, AI-swarm-operated platforms generating $2M+ ARR "
        "while the owner works <20 hours per week."
    )
    mission: str = (
        "Deploy specialized AI swarms across every business domain so that "
        "strategy, marketing, revenue, compliance, and operations run "
        "autonomously — compounding wealth and freedom simultaneously."
    )

    business_units: List[BusinessUnit] = field(default_factory=lambda: [
        # ── TIER 1: Core Platforms ──────────────────────────────────────────
        BusinessUnit(
            name="lippytm.ai Hub",
            repository="lippytm/lippytm.ai",
            purpose="Central AI intelligence hub — orchestrates all 20 businesses and the BrainKit ecosystem",
            phase=BusinessPhase.EXPANSION,
            swarm_type="orchestrator",
            ai_automation_pct=0.70,
            revenue_streams=[
                RevenueStream("SaaS — Professional ($29/mo)", RevenueType.RECURRING, 29_000,
                              description="1,000 paying subscribers"),
                RevenueStream("SaaS — Enterprise (custom)", RevenueType.RECURRING, 25_000,
                              description="50 enterprise clients"),
                RevenueStream("API Access", RevenueType.RECURRING, 10_000,
                              description="$0.10/1K calls, 100M calls/month"),
                RevenueStream("Affiliate Commissions", RevenueType.COMMISSION, 5_000,
                              description="Twin.so + partner stack", automation_level=0.9),
            ],
        ),
        BusinessUnit(
            name="Factory.ai",
            repository="lippytm/factory.ai",
            purpose="Bot & swarm creation engine — productizes AI agents into deployable templates",
            phase=BusinessPhase.EXPANSION,
            swarm_type="production",
            ai_automation_pct=0.80,
            revenue_streams=[
                RevenueStream("Bot Template Sales", RevenueType.ONE_TIME, 15_000,
                              description="500 templates × $30 avg"),
                RevenueStream("Swarm Deployment SaaS", RevenueType.RECURRING, 20_000,
                              description="Managed swarm subscriptions"),
                RevenueStream("White-Label Licensing", RevenueType.RECURRING, 10_000,
                              description="Enterprise white-label"),
            ],
        ),
        BusinessUnit(
            name="AllBots.com",
            repository="lippytm/allbots.com",
            purpose="Bot marketplace and management platform — where the world buys and deploys bots",
            phase=BusinessPhase.FOUNDATION,
            swarm_type="marketplace",
            ai_automation_pct=0.60,
            revenue_streams=[
                RevenueStream("Marketplace Commissions (15%)", RevenueType.COMMISSION, 25_000,
                              description="$167K GMV × 15%", automation_level=0.95),
                RevenueStream("Bot Subscriptions", RevenueType.RECURRING, 10_000),
                RevenueStream("Featured Listings", RevenueType.RECURRING, 3_000),
            ],
        ),
        BusinessUnit(
            name="Web3AI",
            repository="lippytm/web3ai",
            purpose="AI + Blockchain convergence — smart contracts, DeFi, and token economy",
            phase=BusinessPhase.FOUNDATION,
            swarm_type="web3",
            ai_automation_pct=0.65,
            revenue_streams=[
                RevenueStream("Token Economy", RevenueType.TOKEN, 50_000,
                              description="Native utility token; staking, governance, access"),
                RevenueStream("Smart Contract Services", RevenueType.ONE_TIME, 20_000),
                RevenueStream("DeFi Yield (Treasury)", RevenueType.YIELD, 10_000,
                              automation_level=1.0),
                RevenueStream("NFT Membership Drops", RevenueType.ONE_TIME, 8_000),
            ],
        ),
        # ── TIER 2: Intelligence & Knowledge ─────────────────────────────────
        BusinessUnit(
            name="Tower Control AI",
            repository="lippytm/lippytm-lippytm.ai-tower-control-ai",
            purpose="System-wide monitoring, alerting, and optimization center for all 20 businesses",
            phase=BusinessPhase.FOUNDATION,
            swarm_type="control",
            ai_automation_pct=0.90,
            revenue_streams=[
                RevenueStream("Monitoring-as-a-Service", RevenueType.RECURRING, 8_000,
                              automation_level=1.0),
            ],
        ),
        BusinessUnit(
            name="AI Time Machines",
            repository="lippytm/ai-time-machines",
            purpose="Predictive intelligence — trend forecasting, temporal analysis, and future scenario modeling",
            phase=BusinessPhase.FOUNDATION,
            swarm_type="intelligence",
            ai_automation_pct=0.75,
            revenue_streams=[
                RevenueStream("Predictive Analytics SaaS", RevenueType.RECURRING, 12_000),
                RevenueStream("Strategy Consulting", RevenueType.ONE_TIME, 5_000),
            ],
        ),
        BusinessUnit(
            name="Encyclopedia of ChatAIBots",
            repository="lippytm/the-encyclopedia-of-everything-applied-chataibots",
            purpose="The definitive knowledge base and education platform for AI & bot development",
            phase=BusinessPhase.FOUNDATION,
            swarm_type="knowledge",
            ai_automation_pct=0.70,
            revenue_streams=[
                RevenueStream("Course & Certification Sales", RevenueType.ONE_TIME, 10_000),
                RevenueStream("Knowledge Subscriptions", RevenueType.RECURRING, 5_000),
                RevenueStream("Sponsored Content", RevenueType.RECURRING, 2_000),
            ],
        ),
        BusinessUnit(
            name="Encyclopedia of Law",
            repository="lippytm/the-encyclopedia-of-law-civilian-law-military-law-business-law-ai-law.-",
            purpose="AI-powered legal knowledge, compliance automation, and attorney-review platform",
            phase=BusinessPhase.FOUNDATION,
            swarm_type="legal",
            ai_automation_pct=0.60,
            revenue_streams=[
                RevenueStream("Legal Services & Reviews", RevenueType.ONE_TIME, 15_000),
                RevenueStream("Compliance SaaS", RevenueType.RECURRING, 8_000),
                RevenueStream("AI Law Consulting", RevenueType.ONE_TIME, 5_000),
            ],
        ),
        # ── TIER 3: Growth & Finance ──────────────────────────────────────────
        BusinessUnit(
            name="GetBizFunds",
            repository="lippytm/lippytmai.getbizfunds.com-",
            purpose="AI-powered business funding matchmaking — connects entrepreneurs with capital",
            phase=BusinessPhase.FOUNDATION,
            swarm_type="finance",
            ai_automation_pct=0.65,
            revenue_streams=[
                RevenueStream("Funding Referral Commissions", RevenueType.COMMISSION, 30_000,
                              description="2-3% of funded amounts", automation_level=0.8),
                RevenueStream("Financial Services SaaS", RevenueType.RECURRING, 10_000),
            ],
        ),
        BusinessUnit(
            name="Evolutionary Social Networks Agency",
            repository="lippytm/evolutionary-evolutions-social-multimedia-networks-agency-",
            purpose="AI-driven social media, content creation, and multimedia marketing agency",
            phase=BusinessPhase.FOUNDATION,
            swarm_type="marketing",
            ai_automation_pct=0.75,
            revenue_streams=[
                RevenueStream("Agency Retainers", RevenueType.RECURRING, 20_000,
                              description="10 clients × $2K/mo"),
                RevenueStream("Content Licensing", RevenueType.RECURRING, 5_000,
                              automation_level=0.9),
            ],
        ),
        BusinessUnit(
            name="Quantum Questions",
            repository="lippytm/quantum-questions-of-the-many-worlds-universes-of-reruns-",
            purpose="Speculative intelligence, many-worlds scenario planning, and strategic optionality",
            phase=BusinessPhase.FOUNDATION,
            swarm_type="intelligence",
            ai_automation_pct=0.80,
            revenue_streams=[
                RevenueStream("Premium Research Reports", RevenueType.ONE_TIME, 5_000),
                RevenueStream("Scenario Planning SaaS", RevenueType.RECURRING, 3_000),
            ],
        ),
        BusinessUnit(
            name="Intergalactic Zoological Agency",
            repository="lippytm/ai-intergalactic-zoological-social-multimedia-agency-networks-",
            purpose="Creative AI content studio — entertainment, viral content, and immersive media",
            phase=BusinessPhase.FOUNDATION,
            swarm_type="creative",
            ai_automation_pct=0.85,
            revenue_streams=[
                RevenueStream("Content Licensing", RevenueType.RECURRING, 8_000,
                              automation_level=0.9),
                RevenueStream("Sponsorships", RevenueType.RECURRING, 4_000),
            ],
        ),
    ])

    # ── Life Pillars ────────────────────────────────────────────────────────
    life_pillars: Dict[str, Dict] = field(default_factory=lambda: {
        "wealth": {
            "target_annual_revenue": 2_000_000,
            "target_mrr": 167_000,
            "passive_income_ratio": 0.70,
            "ai_automation_ratio": 0.85,
            "timeline_months": 12,
        },
        "freedom": {
            "target_hours_worked_weekly": 20,
            "location_independence": True,
            "business_autopilot_ratio": 0.80,
            "decision_making_delegated": 0.70,
        },
        "impact": {
            "target_users_served": 100_000,
            "businesses_empowered": 1_000,
            "developers_in_ecosystem": 5_000,
        },
        "legacy": {
            "open_source_repos": 20,
            "knowledge_articles_published": 1_000,
            "communities_built": 10,
            "next_gen_entrepreneurs_mentored": 100,
        },
    })

    # ── Master KPI Targets ──────────────────────────────────────────────────
    kpis: Dict[str, float] = field(default_factory=lambda: {
        "total_mrr_target": 167_000,
        "total_arr_target": 2_000_000,
        "active_users_target": 100_000,
        "paying_customers_target": 2_000,
        "ai_automation_pct": 85.0,
        "hours_worked_per_week_max": 20.0,
        "customer_satisfaction_target": 4.8,
        "net_promoter_score_target": 70.0,
        "monthly_churn_rate_max": 0.03,
        "ltv_cac_ratio_min": 5.0,
        "gross_margin_target": 0.80,
    })

    created_at: datetime = field(default_factory=datetime.now)
    version: str = "2.0.0"

    # ── Computed Properties ─────────────────────────────────────────────────
    @property
    def total_monthly_revenue_target(self) -> float:
        return sum(u.monthly_revenue_target for u in self.business_units)

    @property
    def total_current_mrr(self) -> float:
        return sum(u.current_mrr for u in self.business_units)

    @property
    def average_automation_pct(self) -> float:
        if not self.business_units:
            return 0.0
        return sum(u.ai_automation_pct for u in self.business_units) / len(self.business_units)

    def units_by_phase(self, phase: BusinessPhase) -> List[BusinessUnit]:
        return [u for u in self.business_units if u.phase == phase]

    def top_revenue_units(self, n: int = 5) -> List[BusinessUnit]:
        return sorted(self.business_units, key=lambda u: u.monthly_revenue_target, reverse=True)[:n]

    def summary(self) -> Dict[str, Any]:
        return {
            "owner": self.owner,
            "version": self.version,
            "business_units": len(self.business_units),
            "total_monthly_revenue_target": self.total_monthly_revenue_target,
            "total_annual_revenue_target": self.total_monthly_revenue_target * 12,
            "average_automation_pct": self.average_automation_pct,
            "phases": {
                phase.value: len(self.units_by_phase(phase))
                for phase in BusinessPhase
            },
            "top_revenue_units": [
                {"name": u.name, "monthly_target": u.monthly_revenue_target}
                for u in self.top_revenue_units()
            ],
        }
