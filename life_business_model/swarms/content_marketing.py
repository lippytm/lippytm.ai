"""Content Marketing Swarm — brand building, content at scale, and social media automation."""

from typing import Optional, Dict, Any
from .base_swarm import BaseSwarm, SwarmResult
from ..agents.base_agent import BaseAgent
from ..config import CONFIG


class ContentMarketingSwarm(BaseSwarm):
    """
    Three content and marketing agents:
      - Brand Architect        — positioning, voice, and narrative
      - Content Factory Agent  — AI-generated content at scale
      - Social Growth Agent    — organic and paid social media domination
    """

    def _setup_agents(self):
        self.add_agent(BaseAgent(
            name="Brand Architect Agent",
            role=(
                "Define and evolve the lippytm brand across all 20 business units. "
                "Ensure consistent positioning, tone of voice, and visual identity. "
                "Build a brand that commands premium pricing and category leadership."
            ),
            client=self.client,
            model=CONFIG.primary_model,
        ))

        self.add_agent(BaseAgent(
            name="Content Factory Agent",
            role=(
                "Design and operate an AI-powered content factory that produces "
                "high-quality blog posts, tutorials, case studies, and lead magnets "
                "at scale for all 20 lippytm platforms. Target: 50 pieces/month, "
                "90% AI-generated, 10% human-curated."
            ),
            client=self.client,
            model=CONFIG.fast_model,
        ))

        self.add_agent(BaseAgent(
            name="Social Growth Agent",
            role=(
                "Drive explosive growth on X/Twitter, LinkedIn, YouTube, and TikTok "
                "through AI-automated content, community building, and strategic engagement. "
                "Target: 50K social followers within 90 days, 10% engaged audience."
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
            "Brand Architect Agent": """Build the complete lippytm brand architecture.

Business context: 20 AI repositories, Business of Businesses model, targeting entrepreneurs,
developers, and Web3 builders who want AI-powered automation and freedom.

Deliver:
1. Brand positioning statement (1-2 sentences that command premium)
2. Brand personality framework (5 traits with behavioral examples)
3. Tone of voice guide with 3 writing samples per platform (web, social, email)
4. Umbrella brand vs. sub-brand strategy for the 20 repos
5. Brand moat: what makes lippytm impossible to replicate
6. Premium pricing narrative: why charge 3x competitors""",

            "Content Factory Agent": """Design the AI content production pipeline for lippytm.

Goal: 50 pieces/month across all platforms, mostly AI-generated using Claude API.

Deliver:
1. Content architecture: pillar pages, cluster content, and conversion content for each of the top 5 business units
2. AI content workflow: prompt templates for blog posts, tutorials, case studies (include 3 actual prompts)
3. SEO keyword strategy: top 20 keywords by business unit with search volume estimates
4. Repurposing system: 1 long-form → 10 content assets (blog → social → email → video script)
5. Content calendar template for 30 days
6. Quality control process: AI draft → human review → publish in under 30 minutes""",

            "Social Growth Agent": """Design the social media domination strategy.

Target platforms: X/Twitter (developers/builders), LinkedIn (B2B/enterprise), 
YouTube (tutorials), TikTok (creators/entrepreneurs)

Deliver:
1. Platform-specific growth playbook for each (posting frequency, content types, engagement tactics)
2. Viral content formats that work for AI/business topics in 2026
3. AI automation workflow: generate post → schedule → engage → analyze (tools + cadence)
4. Community building strategy: Discord/Slack for lippytm ecosystem users
5. Influencer and cross-promotion strategy in the AI/Web3 space
6. 30-day challenge: specific actions to gain first 10K followers""",
        }

        agent_results = self.run_parallel(tasks, context)
        synthesis = self.synthesize(agent_results)

        return SwarmResult(
            swarm_name=self.name,
            objective=objective or self.objective,
            agent_results=agent_results,
            synthesis=synthesis,
        )
