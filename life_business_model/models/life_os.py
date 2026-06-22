"""Life OS — the top-level pillar model: Wealth, Freedom, Impact, Legacy.

Wraps the life_pillars data already defined on LifeBusinessModel into a
queryable, scored system so pillar health can be computed and tracked
alongside business and swarm telemetry, instead of living as a static
aspiration dict.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List


class PillarName(Enum):
    WEALTH = "wealth"
    FREEDOM = "freedom"
    IMPACT = "impact"
    LEGACY = "legacy"


@dataclass
class Metric:
    name: str
    target: float
    current: float = 0.0
    unit: str = ""
    higher_is_better: bool = True

    @property
    def progress(self) -> float:
        if self.target == 0:
            return 1.0
        ratio = self.current / self.target
        if not self.higher_is_better:
            ratio = self.target / self.current if self.current else 0.0
        return max(0.0, ratio)


@dataclass
class Pillar:
    name: PillarName
    description: str
    metrics: List[Metric] = field(default_factory=list)

    @property
    def score(self) -> float:
        if not self.metrics:
            return 0.0
        return sum(min(m.progress, 1.0) for m in self.metrics) / len(self.metrics)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name.value,
            "description": self.description,
            "score": round(self.score, 3),
            "metrics": [
                {
                    "name": m.name,
                    "target": m.target,
                    "current": m.current,
                    "unit": m.unit,
                    "progress": round(min(m.progress, 1.0), 3),
                }
                for m in self.metrics
            ],
        }


class LifeOS:
    """
    Queryable Life Operating System: Wealth / Freedom / Impact / Legacy.

    Built from LifeBusinessModel.life_pillars plus live business KPIs, so
    pillar health reflects what the business is actually doing rather than
    a fixed target dict.

    Usage:
        life_os = LifeOS()
        life_os.print_scorecard()
        life_os.update_metric("freedom", "Hours Worked / Week", 18)
    """

    def __init__(self, business_model=None):
        from .business_model import LifeBusinessModel  # avoid import cycle

        self.business_model = business_model or LifeBusinessModel()
        self.pillars: Dict[str, Pillar] = self._build_pillars()

    def _build_pillars(self) -> Dict[str, Pillar]:
        bm = self.business_model
        lp = bm.life_pillars

        wealth = Pillar(
            PillarName.WEALTH,
            "Financial abundance — $2M+ ARR, 70% passive, AI-automated",
            metrics=[
                Metric("Monthly Recurring Revenue", lp["wealth"]["target_mrr"], bm.total_current_mrr, "$/mo"),
                Metric("Annual Revenue Run Rate", lp["wealth"]["target_annual_revenue"], bm.total_current_mrr * 12, "$/yr"),
                Metric("AI Automation Ratio", lp["wealth"]["ai_automation_ratio"], bm.average_automation_pct, "ratio"),
            ],
        )
        freedom = Pillar(
            PillarName.FREEDOM,
            "Time and location independence — <20 hrs/week",
            metrics=[
                Metric("Hours Worked / Week", lp["freedom"]["target_hours_worked_weekly"], 0.0, "hrs", higher_is_better=False),
                Metric("Business Autopilot Ratio", lp["freedom"]["business_autopilot_ratio"], bm.average_automation_pct, "ratio"),
            ],
        )
        impact = Pillar(
            PillarName.IMPACT,
            "Reach and value delivered — 100K+ users, 1K+ businesses empowered",
            metrics=[
                Metric("Users Served", lp["impact"]["target_users_served"], 0.0, "users"),
                Metric("Businesses Empowered", lp["impact"]["businesses_empowered"], 0.0, "businesses"),
            ],
        )
        legacy = Pillar(
            PillarName.LEGACY,
            "Long-term value and knowledge — open repos, communities, mentorship",
            metrics=[
                Metric("Open Source Repos", lp["legacy"]["open_source_repos"], len(bm.business_units), "repos"),
                Metric("Knowledge Articles Published", lp["legacy"]["knowledge_articles_published"], 0.0, "articles"),
            ],
        )
        return {"wealth": wealth, "freedom": freedom, "impact": impact, "legacy": legacy}

    @property
    def overall_score(self) -> float:
        if not self.pillars:
            return 0.0
        return sum(p.score for p in self.pillars.values()) / len(self.pillars)

    def update_metric(self, pillar: str, metric_name: str, current: float) -> None:
        for m in self.pillars[pillar].metrics:
            if m.name == metric_name:
                m.current = current
                return
        raise ValueError(f"Unknown metric '{metric_name}' on pillar '{pillar}'")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "overall_score": round(self.overall_score, 3),
            "pillars": {k: v.to_dict() for k, v in self.pillars.items()},
        }

    def print_scorecard(self) -> None:
        print("\n" + "─" * 70)
        print("  🧬 LIFE OS — PILLAR SCORECARD")
        print("─" * 70)
        for key, pillar in self.pillars.items():
            print(f"\n  {key.upper():<10} score: {pillar.score:.0%}  — {pillar.description}")
            for m in pillar.metrics:
                print(f"    • {m.name:<32} {m.current:>10,.1f} / {m.target:>10,.1f} {m.unit:<10} ({min(m.progress, 1.0):.0%})")
        print("\n" + "─" * 70)
        print(f"  OVERALL LIFE OS SCORE: {self.overall_score:.0%}")
        print("─" * 70)
