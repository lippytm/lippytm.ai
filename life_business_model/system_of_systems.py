"""System of Systems — the unifying meta-architecture.

Hierarchy:
  Life OS (Wealth / Freedom / Impact / Legacy)
    -> Business of Businesses (12 business units / 20 repositories)
         -> AI Swarm Network (8 specialized Claude swarms)
              -> Creative Engine (ChatGPT-ensemble content multiplication)
                   -> Platform Mesh (GitHub, Slack, Notion, Cloudflare, HubSpot, Asana)

This module composes the existing layers into a single object so the
empire can be queried, scored, and operated as one coherent system instead
of disconnected modules. It does not replace MasterOrchestrator,
LifeBusinessModel, or CreativeStudio — it sits above them.
"""

import json
import os
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, Optional

from .config import CONFIG
from .models.business_model import LifeBusinessModel
from .models.life_os import LifeOS
from .orchestrator import MasterOrchestrator
from .platform_mesh import PlatformMesh

try:
    from .content.creative_studio import CreativeStudio
    _CREATIVE_AVAILABLE = True
except ImportError:
    _CREATIVE_AVAILABLE = False


@dataclass
class SystemReport:
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    life_os: Dict[str, Any] = field(default_factory=dict)
    business: Dict[str, Any] = field(default_factory=dict)
    platform_mesh: Dict[str, Any] = field(default_factory=dict)
    swarm_report: Optional[Dict[str, Any]] = None
    creative_bundle: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "life_os": self.life_os,
            "business": self.business,
            "platform_mesh": self.platform_mesh,
            "swarm_report": self.swarm_report,
            "creative_bundle": self.creative_bundle,
        }


class SystemOfSystems:
    """
    The single entry point for the entire lippytm Life/Business of
    Businesses empire: Life OS -> Business Model -> AI Swarms -> Creative
    Engine -> Platform Mesh, queryable and operable as one system.

    Usage:
        sos = SystemOfSystems()
        sos.print_full_status()                          # instant, no API calls
        report = sos.run(run_swarms=True, run_creative=True, creative_topic="...")
        sos.save_report(report, "reports/system_of_systems.json")
    """

    def __init__(self, api_key: Optional[str] = None, openai_key: Optional[str] = None):
        self.api_key = api_key or CONFIG.anthropic_api_key
        self.openai_key = openai_key or os.getenv("OPENAI_API_KEY")
        self.business_model = LifeBusinessModel()
        self.life_os = LifeOS(business_model=self.business_model)
        self.mesh = PlatformMesh()
        self._orchestrator: Optional[MasterOrchestrator] = None
        self._creative = None

    @property
    def orchestrator(self) -> MasterOrchestrator:
        if self._orchestrator is None:
            self._orchestrator = MasterOrchestrator(api_key=self.api_key)
        return self._orchestrator

    @property
    def creative(self):
        if not _CREATIVE_AVAILABLE:
            raise ImportError("Creative Engine requires the content modules plus anthropic/openai packages.")
        if self._creative is None:
            self._creative = CreativeStudio(api_key=self.api_key, openai_key=self.openai_key)
        return self._creative

    def status_snapshot(self) -> Dict[str, Any]:
        """Free, instant snapshot of the whole system — no API calls."""
        return {
            "life_os": self.life_os.to_dict(),
            "business": self.business_model.summary(),
            "platform_mesh": self.mesh.status(),
            "swarms_registered": list(MasterOrchestrator.SWARM_REGISTRY.keys()),
            "creative_engine_available": _CREATIVE_AVAILABLE,
        }

    def print_full_status(self) -> None:
        self.life_os.print_scorecard()
        self.mesh.print_status()
        bm = self.business_model.summary()
        print("\n" + "─" * 70)
        print("  🏢 BUSINESS OF BUSINESSES")
        print("─" * 70)
        print(
            f"  Units: {bm['business_units']}   "
            f"Monthly target: ${bm['total_monthly_revenue_target']:,.0f}   "
            f"Avg automation: {bm['average_automation_pct']:.0%}"
        )
        print("\n" + "─" * 70)
        print(f"  ⚡ AI SWARM NETWORK — {len(MasterOrchestrator.SWARM_REGISTRY)} swarms registered")
        print("─" * 70)
        for name, (_, objective) in MasterOrchestrator.SWARM_REGISTRY.items():
            print(f"    • {name:<24} {objective}")
        print("\n" + "─" * 70)
        print(f"  🎨 CREATIVE ENGINE — {'available' if _CREATIVE_AVAILABLE else 'not installed'}")
        print("─" * 70)

    def run(
        self,
        run_swarms: bool = False,
        run_creative: bool = False,
        creative_topic: Optional[str] = None,
        notify: bool = True,
    ) -> SystemReport:
        """Run the full system end to end and return one unified report."""
        report = SystemReport(
            life_os=self.life_os.to_dict(),
            business=self.business_model.summary(),
            platform_mesh=self.mesh.status(),
        )

        if run_swarms:
            orch_report = self.orchestrator.run_full_analysis()
            report.swarm_report = orch_report.to_dict()

        if run_creative and creative_topic:
            bundle = self.creative.full_bundle(creative_topic)
            report.creative_bundle = {
                "topic": bundle.topic,
                "generated_at": bundle.generated_at,
                "has_ebook": bundle.ebook is not None,
                "has_audiobook": bundle.audiobook is not None,
                "video_count": len(bundle.videos),
            }

        if notify:
            self.mesh.notify_slack(
                f"\U0001f9ec *System of Systems run complete* — "
                f"Life OS score: {self.life_os.overall_score:.0%} | "
                f"swarms: {'ran' if run_swarms else 'skipped'} | "
                f"creative: {'ran' if run_creative else 'skipped'}"
            )

        return report

    def save_report(self, report: SystemReport, path: str) -> None:
        os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
        with open(path, "w") as f:
            json.dump(report.to_dict(), f, indent=2, default=str)
        print(f"\n  ✅ System of Systems report saved → {path}")


def _cli():
    import argparse

    parser = argparse.ArgumentParser(
        prog="system_of_systems",
        description="Query and operate the full empire as one system",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("status", help="Print full status snapshot (free, instant)")

    p_run = sub.add_parser("run", help="Run the full system")
    p_run.add_argument("--swarms", action="store_true", help="Run all 8 AI swarms")
    p_run.add_argument("--creative", help="Run the creative engine with this topic")
    p_run.add_argument("--output", "-o", help="Save report as JSON")
    p_run.add_argument("--no-notify", action="store_true", help="Skip Slack notification")

    args = parser.parse_args()
    sos = SystemOfSystems()

    if args.command == "status":
        sos.print_full_status()
    elif args.command == "run":
        report = sos.run(
            run_swarms=args.swarms,
            run_creative=bool(args.creative),
            creative_topic=args.creative,
            notify=not args.no_notify,
        )
        if args.output:
            sos.save_report(report, args.output)
        else:
            print(json.dumps(report.to_dict(), indent=2, default=str))


if __name__ == "__main__":
    _cli()
