"""Business Intelligence Swarm — market analysis, competitive intel, and growth strategy."""

from typing import Optional, Dict, Any
from .base_swarm import BaseSwarm, SwarmResult
from ..agents.base_agent import BaseAgent
from ..config import CONFIG


class BusinessIntelligenceSwarm(BaseSwarm):
    """
    Four intelligence agents working in parallel:
      - Market Research Agent       — market sizing and trend analysis
      - Competitive Intelligence    — competitor strengths, gaps, attack vectors
      - Opportunity Scanner         — new markets and partnership targets
      - Growth Strategy Agent       — PLG, virality, platform flywheel design
    """

    def _setup_agents(self):
        self.add_agent(BaseAgent(
            name="Market Research Agent",
            role=(
                "Analyze market size, growth rates, and dynamics for the AI agent platforms, "
                "bot marketplaces, Web3AI convergence, and business automation sectors. "
                "Surface white spaces where lippytm can establish category leadership."
            ),
            client=self.client,
            model=CONFIG.primary_model,
        ))

        self.add_agent(BaseAgent(
            name="Competitive Intelligence Agent",
            role=(
                "Monitor and dissect competitors in AI agent orchestration, bot platforms, "
                "Web3 dev tools, and AI SaaS hubs. Identify attack vectors, pricing gaps, "
                "and collaboration opportunities for lippytm."
            ),
            client=self.client,
            model=CONFIG.fast_model,
        ))

        self.add_agent(BaseAgent(
            name="Opportunity Scanner Agent",
            role=(
                "Continuously identify the highest-value new opportunities: partnerships, "
                "acquisition targets, emerging platforms, regulatory tailwinds, and underserved "
                "niches that align with the lippytm 20-repo ecosystem."
            ),
            client=self.client,
            model=CONFIG.primary_model,
        ))

        self.add_agent(BaseAgent(
            name="Growth Strategy Agent",
            role=(
                "Design the growth engine using PLG, viral loops, network effects, and "
                "platform flywheel models. Optimize for capital-efficient, AI-accelerated "
                "growth to 100K users within 12 months."
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
            "Market Research Agent": """Analyze the 2026 market landscape for the lippytm Business of Businesses.

Markets to size and analyze:
1. AI agent orchestration & swarm platforms
2. Bot marketplaces and no-code automation
3. Web3 + AI convergence (DeFi, NFTs, smart contracts)
4. Developer tools and AI coding assistants
5. Business automation SaaS

For each market deliver:
- Total Addressable Market (TAM) and Serviceable Addressable Market (SAM)
- YoY growth rate and 3-year CAGR
- Top 3 trends shaping the market
- lippytm's best positioning angle
- Time-to-revenue estimate for entering/dominating""",

            "Competitive Intelligence Agent": """Competitive deep-dive for the lippytm ecosystem.

Analyze these competitor groups:
1. AI agent platforms: AutoGPT, CrewAI, LangGraph, Microsoft Copilot Studio, Zapier AI
2. Bot platforms: ManyChat, Chatfuel, Botpress, Tidio
3. Web3 dev tools: Alchemy, Thirdweb, Moralis, Hardhat/Foundry
4. AI SaaS hubs: Make (Integromat), n8n, Activepieces

For each competitor deliver:
- Core strength and unique moat
- Pricing model and revenue range
- Customer base and ICP
- Biggest weakness lippytm can exploit
- Collaborate or compete? Recommendation""",

            "Opportunity Scanner Agent": """Identify the top 10 highest-value opportunities for lippytm in 2026.

Scanning dimensions:
- New AI model capabilities (Claude 4, GPT-5 series, Gemini Ultra)
- Web3 cycle dynamics and emerging L2/L3 ecosystems
- Enterprise AI adoption acceleration patterns
- Creator economy and AI content monetization
- Regulatory changes opening new markets
- Strategic acquisition targets (sub-$500K valuation)

For each opportunity deliver:
- Market size potential ($)
- Time-to-first-revenue (weeks)
- Required resources (low/med/high)
- Strategic fit score (1-10)
- Recommended entry strategy""",

            "Growth Strategy Agent": """Design the master growth engine for lippytm Business of Businesses.

Objective: 10x growth in 12 months, capital-efficient, AI-automated.

Deliver:
1. Product-Led Growth (PLG) blueprint for lippytm.ai hub
   - Free tier viral loop design
   - Activation event definition and optimization
   - PQL (product-qualified lead) scoring model

2. Network effect design for AllBots.com marketplace
   - Liquidity bootstrapping strategy
   - Cross-side network effects between bot creators and buyers
   - Defensibility moat analysis

3. Viral coefficient optimization
   - Referral mechanics and incentive structure
   - K-factor target and how to achieve it

4. Platform flywheel model
   - The reinforcing loop diagram (text description)
   - Flywheel acceleration tactics

5. Land-and-expand enterprise playbook
   - Entry-level product for enterprise
   - Expansion trigger points and upsell sequence

6. 12-month growth milestones: users, MRR, repos active, automation %""",
        }

        agent_results = self.run_parallel(tasks, context)
        synthesis = self.synthesize(agent_results)

        return SwarmResult(
            swarm_name=self.name,
            objective=objective or self.objective,
            agent_results=agent_results,
            synthesis=synthesis,
        )
