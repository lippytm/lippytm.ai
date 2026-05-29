"""Master Orchestrator — the brain that coordinates all swarms across the Business of Businesses."""

import anthropic
import json
from typing import Optional, Dict, Any, List
from dataclasses import dataclass, field
from datetime import datetime

from .config import CONFIG
from .models.business_model import LifeBusinessModel
from .swarms.tower_control import TowerControlSwarm
from .swarms.business_intelligence import BusinessIntelligenceSwarm
from .swarms.revenue_generation import RevenueGenerationSwarm
from .swarms.content_marketing import ContentMarketingSwarm
from .swarms.web3_defi import Web3DeFiSwarm
from .swarms.knowledge_research import KnowledgeResearchSwarm
from .swarms.legal_compliance import LegalComplianceSwarm
from .swarms.finance_funding import FinanceFundingSwarm
from .swarms.base_swarm import SwarmResult


@dataclass
class OrchestratorReport:
    timestamp: datetime = field(default_factory=datetime.now)
    swarm_results: List[SwarmResult] = field(default_factory=list)
    master_synthesis: str = ""
    action_plan: str = ""
    success: bool = True

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp.isoformat(),
            "success": self.success,
            "master_synthesis": self.master_synthesis,
            "action_plan": self.action_plan,
            "swarms": [
                {
                    "name": r.swarm_name,
                    "objective": r.objective,
                    "synthesis": r.synthesis,
                    "success_rate": r.success_rate,
                    "total_tokens": r.total_tokens,
                    "cache_hit_rate": r.cache_hit_rate,
                }
                for r in self.swarm_results
            ],
        }


class MasterOrchestrator:
    """
    The central intelligence engine of the lippytm Business of Businesses.

    Coordinates 8 specialized AI swarms, each running multiple Claude agents
    in parallel, to generate autonomous strategic intelligence across every
    dimension of the empire: revenue, growth, marketing, Web3, legal, knowledge,
    finance, and system control.

    Usage:
        orchestrator = MasterOrchestrator()

        # Run everything
        report = orchestrator.run_full_analysis()
        orchestrator.print_report(report)

        # Run a single swarm
        result = orchestrator.run_swarm("revenue_generation")

        # Save report
        orchestrator.save_report(report, "reports/2026-05-29.json")
    """

    SWARM_REGISTRY = {
        "tower_control": (TowerControlSwarm, "Monitor and optimize all 20 business systems"),
        "business_intelligence": (BusinessIntelligenceSwarm, "Market intel and growth strategy"),
        "revenue_generation": (RevenueGenerationSwarm, "Maximize revenue to $2M ARR"),
        "content_marketing": (ContentMarketingSwarm, "Brand building and content at scale"),
        "web3_defi": (Web3DeFiSwarm, "Token economy, smart contracts, and DeFi yield"),
        "knowledge_research": (KnowledgeResearchSwarm, "Knowledge empire and research engine"),
        "legal_compliance": (LegalComplianceSwarm, "AI law and regulatory compliance"),
        "finance_funding": (FinanceFundingSwarm, "Capital strategy and financial optimization"),
    }

    # Priority order for sequential execution (dependencies first)
    DEFAULT_EXECUTION_ORDER = [
        "tower_control",
        "business_intelligence",
        "finance_funding",
        "revenue_generation",
        "content_marketing",
        "web3_defi",
        "legal_compliance",
        "knowledge_research",
    ]

    def __init__(self, api_key: Optional[str] = None):
        self.client = anthropic.Anthropic(
            api_key=api_key or CONFIG.anthropic_api_key
        )
        self.business_model = LifeBusinessModel()
        self._swarms: Dict[str, Any] = {}

    def _get_swarm(self, name: str):
        if name not in self._swarms:
            swarm_class, objective = self.SWARM_REGISTRY[name]
            self._swarms[name] = swarm_class(
                name=name.replace("_", " ").title(),
                objective=objective,
                client=self.client,
            )
        return self._swarms[name]

    def _build_context(self) -> Dict[str, Any]:
        summary = self.business_model.summary()
        summary["life_pillars"] = self.business_model.life_pillars
        summary["kpis"] = self.business_model.kpis
        summary["repositories"] = CONFIG.repositories
        summary["affiliate_partners"] = CONFIG.affiliates
        return summary

    def run_swarm(
        self,
        swarm_name: str,
        context: Optional[Dict] = None,
    ) -> SwarmResult:
        """Execute a single named swarm."""
        if swarm_name not in self.SWARM_REGISTRY:
            raise ValueError(
                f"Unknown swarm '{swarm_name}'. "
                f"Available: {list(self.SWARM_REGISTRY.keys())}"
            )
        ctx = context or self._build_context()
        return self._get_swarm(swarm_name).execute(context=ctx)

    def run_full_analysis(
        self,
        swarms: Optional[List[str]] = None,
    ) -> OrchestratorReport:
        """Run all (or a subset of) swarms and synthesize into a master report."""
        order = swarms or self.DEFAULT_EXECUTION_ORDER
        ctx = self._build_context()

        print("\n" + "="*70)
        print("  LIPPYTM BUSINESS OF BUSINESSES — AI SWARMS ACTIVATED")
        print("="*70)
        print(f"  Vision : {self.business_model.vision[:80]}...")
        print(f"  Target : ${self.business_model.total_monthly_revenue_target:,.0f}/month")
        print(f"  Swarms : {len(order)} active")
        print("="*70 + "\n")

        swarm_results: List[SwarmResult] = []
        for name in order:
            swarm = self._get_swarm(name)
            print(f"  ⚡ [{name.upper()}] Running {len(swarm.agents)} agents in parallel...")
            result = swarm.execute(context=ctx)
            swarm_results.append(result)
            print(f"     ✓ Done — success rate: {result.success_rate:.0%} | "
                  f"tokens: {result.total_tokens:,} | cache hits: {result.cache_hit_rate:.0%}")

        print("\n  🧠 Generating Master Strategic Synthesis...")
        master_synthesis = self._master_synthesis(swarm_results)
        action_plan = self._action_plan(swarm_results)

        return OrchestratorReport(
            swarm_results=swarm_results,
            master_synthesis=master_synthesis,
            action_plan=action_plan,
        )

    def _master_synthesis(self, swarm_results: List[SwarmResult]) -> str:
        all_syntheses = "\n\n".join(
            f"## {r.swarm_name}\n{r.synthesis}"
            for r in swarm_results
            if r.synthesis
        )

        resp = self.client.messages.create(
            model=CONFIG.primary_model,
            max_tokens=4096,
            system=(
                "You are the Master Strategic Intelligence for the lippytm Business of Businesses empire. "
                "Your synthesis must be concrete, prioritized, and immediately actionable. "
                "No fluff. Every sentence must drive towards $2M ARR and <20 hrs/week."
            ),
            messages=[{
                "role": "user",
                "content": f"""Synthesize all swarm intelligence into the MASTER STRATEGIC BRIEFING.

{all_syntheses}

---

Create a comprehensive master briefing with these exact sections:

# 🏆 BUSINESS OF BUSINESSES — MASTER STRATEGIC INTELLIGENCE BRIEFING

## 1. EMPIRE STATUS OVERVIEW
Current state snapshot, health score, biggest wins, and critical gaps.

## 2. THE TOP 3 HIGHEST-LEVERAGE MOVES RIGHT NOW
For each: what, why, how, expected outcome, who does it (owner vs. AI agent).

## 3. REVENUE ACCELERATION ROADMAP
Path to $167K MRR with specific monthly milestones.
Fastest streams to activate first. Which swarms drive which revenue.

## 4. THE AUTOMATION EMPIRE BLUEPRINT
How to hit 85% AI automation. Which processes, which tools, which order.
What the owner’s remaining 20 hrs/week actually looks like.

## 5. LIFE FREEDOM SCORECARD
Passive income ratio now vs. target. How many hours saved by AI swarms.
When does the owner hit full financial and time freedom?

## 6. THIS WEEK’S 7 NON-NEGOTIABLE ACTIONS
Specific, measurable, assigned (owner vs. automated). Expected outcome for each."""
            }],
        )
        return resp.content[0].text if resp.content else ""

    def _action_plan(self, swarm_results: List[SwarmResult]) -> str:
        resp = self.client.messages.create(
            model=CONFIG.primary_model,
            max_tokens=2048,
            system="You are a precision execution planner. Every item must be specific and doable.",
            messages=[{
                "role": "user",
                "content": """Based on all swarm analysis, produce THE 90-DAY EXECUTION PLAYBOOK.

Format exactly as follows:

## THIS WEEK (Days 1–7)
- [ ] [OWNER/AI] Action: specific task → expected outcome
(list 7 actions)

## THIS MONTH (Days 8–30)
- [ ] [OWNER/AI] Action: specific task → expected outcome
(list 10 actions)

## THIS QUARTER (Days 31–90)
- [ ] Milestone: measurable goal → business impact
(list 5 milestones)

## REVENUE CHECKPOINTS
- End of Week 4  : $___ MRR
- End of Month 3 : $___ MRR
- End of Month 6 : $___ MRR
- End of Month 12: $___ MRR

## AUTOMATION CHECKPOINTS
- Week 4  : ___% of operations automated
- Month 3 : ___% of operations automated
- Month 6 : ___% of operations automated"""
            }],
        )
        return resp.content[0].text if resp.content else ""

    def print_report(self, report: OrchestratorReport):
        """Pretty-print the full report to stdout."""
        divider = "=" * 70

        for sr in report.swarm_results:
            print(f"\n{divider}")
            print(f"  ⚡ {sr.swarm_name.upper()} SWARM")
            print(divider)
            if sr.synthesis:
                preview = sr.synthesis[:1500]
                print(preview)
                if len(sr.synthesis) > 1500:
                    print("  [...truncated — full content in saved report]")

        print(f"\n{divider}")
        print("  🧠 MASTER STRATEGIC SYNTHESIS")
        print(divider)
        print(report.master_synthesis)

        print(f"\n{divider}")
        print("  📋 90-DAY EXECUTION PLAYBOOK")
        print(divider)
        print(report.action_plan)

    def save_report(self, report: OrchestratorReport, path: str):
        """Save full report as JSON."""
        import os
        os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
        with open(path, "w") as f:
            json.dump(report.to_dict(), f, indent=2)
        print(f"\n  ✅ Report saved → {path}")
