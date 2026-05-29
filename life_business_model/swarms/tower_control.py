"""Tower Control Swarm — the nerve center for monitoring, optimization, and resource allocation."""

from typing import Optional, Dict, Any
from .base_swarm import BaseSwarm, SwarmResult
from ..agents.base_agent import BaseAgent
from ..config import CONFIG


class TowerControlSwarm(BaseSwarm):
    """
    Four mission-critical agents:
      - System Health Monitor    — repo and platform health across all 20 units
      - KPI Tracker Agent        — metrics, leading indicators, and reporting
      - Automation Optimizer     — identifies and implements automation opportunities
      - Resource Allocation      — time, capital, and compute allocation across units
    """

    def _setup_agents(self):
        self.add_agent(BaseAgent(
            name="System Health Monitor",
            role=(
                "Monitor health and performance across all 20 lippytm repositories and platforms. "
                "Identify CI failures, stale code, missing integrations, security gaps, "
                "and infrastructure bottlenecks. Produce weekly health scorecards."
            ),
            client=self.client,
            model=CONFIG.fast_model,
        ))

        self.add_agent(BaseAgent(
            name="KPI Tracker Agent",
            role=(
                "Design and operate the master KPI dashboard for the Business of Businesses. "
                "Define leading and lagging indicators, set up alert thresholds, and "
                "produce actionable weekly reports. Target: $167K MRR, 100K users, 85% automation."
            ),
            client=self.client,
            model=CONFIG.primary_model,
        ))

        self.add_agent(BaseAgent(
            name="Automation Optimizer Agent",
            role=(
                "Identify every manual business process and design automation to replace it. "
                "Use GitHub Actions, Zapier, Claude API, and custom bots. "
                "Target: 85% of all business operations fully automated within 6 months."
            ),
            client=self.client,
            model=CONFIG.primary_model,
        ))

        self.add_agent(BaseAgent(
            name="Resource Allocation Agent",
            role=(
                "Optimize allocation of the owner's time, AI compute budget, and capital "
                "across all 20 business units. Use portfolio theory: balance growth bets "
                "vs. cash-flow generators. Protect the owner's <20 hrs/week constraint."
            ),
            client=self.client,
            model=CONFIG.primary_model,
        ))

    def execute(
        self,
        objective: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
    ) -> SwarmResult:
        tasks = {
            "System Health Monitor": """Perform a comprehensive health audit of the lippytm ecosystem.

20 repositories covering: core platforms, bots, Web3, legal, knowledge, time machines,
finance, marketing, transparency, and docs.

Deliver:
1. Health scorecard template (repo × criteria): CI status, test coverage, docs, security, integrations
2. Critical issues: top 5 things most likely to break or block revenue
3. Integration gaps: which repos are isolated vs. connected to the BrainKit hub
4. Security audit checklist tailored to AI platforms and Web3 repos
5. Performance baseline metrics to track: build time, test pass rate, uptime, response time
6. Automated monitoring setup: which GitHub Actions workflows to add immediately""",

            "KPI Tracker Agent": """Design the master KPI framework for the Business of Businesses.

Targets: $167K MRR, 100K users, 85% automation, <20 hrs/week, NPS 70+, churn <3%

Deliver:
1. Complete KPI hierarchy: North Star metric + 3 strategic KPIs per business unit
2. Leading indicators for each KPI (what to watch before the metric moves)
3. Weekly dashboard template: which 10 numbers to review every Monday
4. Alert thresholds: when to escalate vs. monitor vs. act immediately
5. Automated reporting pipeline: how to collect and visualize KPIs without manual work
6. Monthly business review template for portfolio-level decisions
7. OKR framework for quarterly goal-setting across all 20 units""",

            "Automation Optimizer Agent": """Map and automate every manual process in lippytm.

Current manual processes likely include:
- Lead gen, qualification, and onboarding
- Content creation, review, and publishing
- Customer support and issue resolution
- Code review, testing, and deployment
- Invoice generation and payment collection
- Performance analysis and reporting
- Market research and opportunity scanning
- Social media posting and engagement

Deliver:
1. Process inventory: 20 manual processes ranked by time cost (hrs/month)
2. Automation feasibility matrix: complexity vs. ROI for each process
3. Top 10 automation builds with exact tools (GitHub Actions, Zapier, Claude API, ManyChat)
4. Implementation sequence: quick wins (week 1) → medium builds (month 1) → complex systems (quarter 1)
5. Estimated hours saved per month after full automation
6. Automation testing and monitoring strategy to prevent silent failures""",

            "Resource Allocation Agent": """Design the optimal resource allocation model.

Constraints:
- Owner time: max 20 hours/week total
- AI compute: optimize cost, use prompt caching
- Development: prioritize highest-leverage repos first
- Capital: bootstrap-first, preserve equity

Deliver:
1. Portfolio matrix: 2×2 grid (revenue potential × automation readiness) placing all 12 business units
2. Weekly time budget: hour allocation by category (strategy, product, marketing, admin)
3. AI swarm deployment priority: which swarms to activate first for maximum ROI
4. Cloudflare infrastructure plan (D1, R2, Workers, KV) for zero-maintenance scalable hosting
5. 90-day sprint plan: top 3 business units to go all-in on, with specific deliverables
6. Decision criteria for when to hire vs. automate vs. outsource""",
        }

        agent_results = self.run_parallel(tasks, context)
        synthesis = self.synthesize(
            agent_results,
            synthesis_prompt="""Create the MASTER CONTROL TOWER REPORT.

Include:
1. EMPIRE STATUS: overall health score and summary for all 20 business units
2. TOP 5 CRITICAL ACTIONS: ranked by urgency and impact
3. AUTOMATION ROADMAP: path to 85% automation with weekly milestones
4. RESOURCE PLAYBOOK: exact time and capital allocation for next 90 days
5. KPI DASHBOARD: complete metrics framework and monitoring setup
6. NEXT 30-DAY SPRINT: specific, measurable goals and owner actions

Be concrete. The owner should be able to act on this report immediately.""",
        )

        return SwarmResult(
            swarm_name=self.name,
            objective=objective or self.objective,
            agent_results=agent_results,
            synthesis=synthesis,
        )
