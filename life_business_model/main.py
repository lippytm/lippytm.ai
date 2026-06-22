"""CLI entry point for the lippytm Life/Business Model AI Swarms."""

import argparse
import os
import sys
from datetime import datetime

from .orchestrator import MasterOrchestrator
from .models.business_model import LifeBusinessModel
from .system_of_systems import SystemOfSystems
from .config import CONFIG


AVAILABLE_SWARMS = [
    "tower_control",
    "business_intelligence",
    "revenue_generation",
    "content_marketing",
    "web3_defi",
    "knowledge_research",
    "legal_compliance",
    "finance_funding",
]


def print_model_overview():
    model = LifeBusinessModel()
    summary = model.summary()

    print("\n" + "─" * 70)
    print("  💎 LIPPYTM LIFE/BUSINESS MODEL — BUSINESS OF BUSINESSES")
    print("─" * 70)
    print(f"  Owner  : {model.owner}")
    print(f"  Version: {model.version}")
    print()
    print(f"  Vision : {model.vision}")
    print()
    print(f"  Total Monthly Revenue Target : ${summary['total_monthly_revenue_target']:>12,.0f}")
    print(f"  Total Annual Revenue Target  : ${summary['total_annual_revenue_target']:>12,.0f}")
    print(f"  Avg AI Automation %          : {summary['average_automation_pct']:>11.0%}")
    print(f"  Business Units               : {summary['business_units']:>12}")
    print()
    print("  TOP REVENUE UNITS:")
    for u in summary["top_revenue_units"]:
        print(f"    • {u['name']:<45} ${u['monthly_target']:>10,.0f}/mo")
    print()
    print("  LIFE PILLARS:")
    for pillar, data in model.life_pillars.items():
        print(f"    • {pillar.upper():<12} {data}")
    print("─" * 70)


def main():
    parser = argparse.ArgumentParser(
        prog="swarms",
        description="lippytm Business of Businesses — AI Swarms CLI",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # model: show business model overview
    sub.add_parser("model", help="Print the Life/Business Model overview")

    # full: run all swarms
    p_full = sub.add_parser("full", help="Run all 8 swarms and generate master report")
    p_full.add_argument("--output", "-o", help="Save report as JSON (e.g. reports/today.json)")
    p_full.add_argument("--swarms", nargs="+", choices=AVAILABLE_SWARMS,
                        help="Run a subset of swarms")

    # swarm: run one swarm
    p_swarm = sub.add_parser("swarm", help="Run a single named swarm")
    p_swarm.add_argument("name", choices=AVAILABLE_SWARMS)
    p_swarm.add_argument("--output", "-o", help="Save synthesis as text file")

    # list: list all swarms
    sub.add_parser("list", help="List all available swarms")

    # system: query/operate the unified System of Systems
    p_system = sub.add_parser(
        "system",
        help="Query/operate the System of Systems (Life OS + Business + Swarms + Creative + Platform Mesh)",
    )
    p_system.add_argument("action", choices=["status", "run"], default="status", nargs="?")
    p_system.add_argument("--swarms", action="store_true", help="Run all 8 AI swarms as part of the system run")
    p_system.add_argument("--creative", help="Run the creative engine with this topic")
    p_system.add_argument("--output", "-o", help="Save the system report as JSON")
    p_system.add_argument("--no-notify", action="store_true", help="Skip Slack notification")

    args = parser.parse_args()

    api_key = os.getenv("ANTHROPIC_API_KEY")
    requires_key = args.command not in ("model", "list") and not (
        args.command == "system" and args.action == "status"
    )
    if requires_key and not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)

    if args.command == "model":
        print_model_overview()

    elif args.command == "list":
        print("\nAvailable swarms:")
        for s in AVAILABLE_SWARMS:
            _, objective = MasterOrchestrator.SWARM_REGISTRY[s]
            print(f"  {s:<28} — {objective}")
        print()

    elif args.command == "swarm":
        orch = MasterOrchestrator(api_key=api_key)
        result = orch.run_swarm(args.name)
        print(f"\n{'='*60}")
        print(f"  {args.name.upper()} SWARM SYNTHESIS")
        print("=" * 60)
        print(result.synthesis)
        if args.output:
            with open(args.output, "w") as f:
                f.write(result.synthesis)
            print(f"\n  Saved → {args.output}")

    elif args.command == "full":
        print_model_overview()
        orch = MasterOrchestrator(api_key=api_key)
        report = orch.run_full_analysis(swarms=args.swarms)
        orch.print_report(report)
        if args.output:
            orch.save_report(report, args.output)

    elif args.command == "system":
        sos = SystemOfSystems(api_key=api_key)
        if args.action == "run":
            report = sos.run(
                run_swarms=args.swarms,
                run_creative=bool(args.creative),
                creative_topic=args.creative,
                notify=not args.no_notify,
            )
            if args.output:
                sos.save_report(report, args.output)
            sos.print_full_status()
        else:
            sos.print_full_status()


if __name__ == "__main__":
    main()
