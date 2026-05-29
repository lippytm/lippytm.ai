"""Knowledge & Research Swarm — builds the lippytm knowledge empire and research engine."""

from typing import Optional, Dict, Any
from .base_swarm import BaseSwarm, SwarmResult
from ..agents.base_agent import BaseAgent
from ..config import CONFIG


class KnowledgeResearchSwarm(BaseSwarm):
    """
    Two knowledge-focused agents:
      - Encyclopedia Architect  — structures knowledge bases and courses
      - Research Engine Agent   — continuous research and insight generation
    """

    def _setup_agents(self):
        self.add_agent(BaseAgent(
            name="Encyclopedia Architect Agent",
            role=(
                "Build and curate the lippytm knowledge empire spanning AI bots, law, "
                "time machines, and quantum theory. Design knowledge structures that "
                "generate revenue through courses, subscriptions, and licensing."
            ),
            client=self.client,
            model=CONFIG.primary_model,
        ))

        self.add_agent(BaseAgent(
            name="Research Engine Agent",
            role=(
                "Continuously surface cutting-edge insights in AI, Web3, business automation, "
                "and emerging technology. Transform research into actionable intelligence "
                "for the lippytm Business of Businesses strategy."
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
            "Encyclopedia Architect Agent": """Design the lippytm Knowledge Empire monetization strategy.

Existing knowledge repos:
- Encyclopedia of Everything Applied ChatAIBots
- Encyclopedia of Law (Civilian, Military, Business, AI Law)
- Quantum Questions of the Many Worlds Universes
- AI Time Machines
- Transparency Logic Time Machine Bots

Deliver:
1. Content architecture for each encyclopedia (top-level categories + 20 article titles each)
2. Monetization model: free articles (SEO) → premium deep dives → certification courses
3. AI-powered knowledge generation workflow using Claude API
4. Cross-linking strategy between encyclopedias and product repos (SEO + conversion)
5. Knowledge licensing program: B2B clients pay for API access to knowledge base
6. 6-month publishing roadmap: articles/week target and team structure""",

            "Research Engine Agent": """Generate the 2026 Research Intelligence Briefing for lippytm.

Research domains:
1. AI agent architectures: what's new in swarm intelligence, multi-agent frameworks
2. Web3 developments: L2 maturation, account abstraction, on-chain AI
3. Business automation: agentic workflows replacing SaaS tools
4. Legal tech: AI law, smart contract regulation, compliance automation
5. Creator economy: how AI is reshaping content monetization

For each domain deliver:
- 3 most important developments right now
- Impact on lippytm business units
- Action items to capitalize within 30 days
- 12-month trajectory prediction""",
        }

        agent_results = self.run_parallel(tasks, context)
        synthesis = self.synthesize(agent_results)

        return SwarmResult(
            swarm_name=self.name,
            objective=objective or self.objective,
            agent_results=agent_results,
            synthesis=synthesis,
        )
