"""Finance & Funding Swarm — capital strategy, funding matchmaking, and financial optimization."""

from typing import Optional, Dict, Any
from .base_swarm import BaseSwarm, SwarmResult
from ..agents.base_agent import BaseAgent
from ..config import CONFIG


class FinanceFundingSwarm(BaseSwarm):
    """
    Two finance agents:
      - Capital Strategy Agent  — funding, investment, and capital allocation
      - Financial Optimizer     — cost reduction, margin improvement, and cash flow
    """

    def _setup_agents(self):
        self.add_agent(BaseAgent(
            name="Capital Strategy Agent",
            role=(
                "Design the capital strategy for the lippytm Business of Businesses: "
                "bootstrapping vs. fundraising decisions, investor targeting via GetBizFunds, "
                "grant opportunities, and strategic partnership capital. "
                "Goal: achieve $2M ARR without sacrificing majority ownership."
            ),
            client=self.client,
            model=CONFIG.primary_model,
        ))

        self.add_agent(BaseAgent(
            name="Financial Optimizer Agent",
            role=(
                "Maximize gross margins and minimize burn across all 20 lippytm platforms. "
                "Identify cost reduction opportunities in infrastructure, API usage, and tools. "
                "Build financial models to track path to profitability for each business unit."
            ),
            client=self.client,
            model=CONFIG.fast_model,
        ))

    def execute(
        self,
        objective: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
    ) -> SwarmResult:
        tasks = {
            "Capital Strategy Agent": """Design the capital strategy for lippytm.

Current assets: 20 GitHub repositories, existing Web3AI stack, BrainKit ecosystem,
monetization roadmap from MONETIZATION.md.
Goal: $2M ARR within 12 months, retain 80%+ ownership.

Deliver:
1. Bootstrap-first strategy: which revenue streams fund the next stage of growth
2. Funding options ranked by dilution vs. speed: angels, VCs, grants, revenue-based financing
3. Pitch deck outline for a $500K seed round (if needed)
4. GetBizFunds platform strategy: how to use the funding matchmaking repo to raise capital
5. Grant opportunities: AI research grants, Web3 ecosystem grants, SBIR (if applicable)
6. Strategic partnership capital: which big tech companies would pay to integrate with lippytm
7. 18-month financial forecast model structure (revenue, costs, burn, runway)""",

            "Financial Optimizer Agent": """Build the financial optimization model for lippytm.

Cost drivers: Claude API calls, hosting/infrastructure, GitHub Actions, third-party SaaS tools,
contractor/developer time.
Target gross margin: 80%+

Deliver:
1. Cost breakdown model: estimate monthly costs at $10K, $50K, and $167K MRR scale
2. Claude API cost optimization: prompt caching strategy, model tier routing, batch processing
3. Infrastructure cost ladder: cheapest path from MVP to scale (Cloudflare Workers, R2, D1)
4. Unit economics model: CAC, LTV, payback period for each customer segment
5. Gross margin improvement roadmap from current to 80% target
6. Automated financial reporting: which metrics to track weekly vs. monthly vs. quarterly
7. Break-even analysis for each business unit""",
        }

        agent_results = self.run_parallel(tasks, context)
        synthesis = self.synthesize(agent_results)

        return SwarmResult(
            swarm_name=self.name,
            objective=objective or self.objective,
            agent_results=agent_results,
            synthesis=synthesis,
        )
