"""Legal & Compliance Swarm — AI law, regulatory compliance, and contract automation."""

from typing import Optional, Dict, Any
from .base_swarm import BaseSwarm, SwarmResult
from ..agents.base_agent import BaseAgent
from ..config import CONFIG


class LegalComplianceSwarm(BaseSwarm):
    """
    Two legal agents:
      - AI Legal Advisor    — AI law, TOS, privacy, and IP strategy
      - Compliance Monitor  — ongoing regulatory compliance across jurisdictions

    NOTE: All outputs are for informational/planning purposes.
    Consult a licensed attorney for binding legal advice.
    """

    def _setup_agents(self):
        self.add_agent(BaseAgent(
            name="AI Legal Advisor Agent",
            role=(
                "Provide AI-focused legal guidance for the lippytm ecosystem: "
                "terms of service, privacy policies, IP ownership, liability, "
                "and AI-specific regulations (EU AI Act, US AI legislation). "
                "Goal: protect all 20 business units with minimal legal spend."
            ),
            client=self.client,
            model=CONFIG.primary_model,
        ))

        self.add_agent(BaseAgent(
            name="Compliance Monitor Agent",
            role=(
                "Monitor and ensure compliance across all lippytm platforms: "
                "GDPR, CCPA, AML/KYC for Web3, securities law for token issuance, "
                "and platform liability rules. Proactively flag risks before they become liabilities."
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
            "AI Legal Advisor Agent": """Create the lippytm Legal Protection Blueprint.

Business context: 20 AI platforms, Web3 token, NFTs, data processing, affiliate program,
marketplace, consulting services. Users in multiple jurisdictions.

Deliver (informational/planning guidance, not legal advice):
1. Minimum viable legal structure for a Business of Businesses in 2026
2. Terms of Service must-have clauses for an AI platform marketplace
3. Privacy policy framework: GDPR + CCPA compliance checklist
4. IP strategy: who owns AI-generated content on lippytm platforms?
5. EU AI Act compliance checklist for the lippytm AI swarm system
6. Token issuance legal considerations: utility vs. security token framework
7. Estimated legal costs and priority order for each document""",

            "Compliance Monitor Agent": """Build the compliance monitoring system for lippytm.

Platforms: SaaS (data), marketplace (transactions), Web3 (tokens, DeFi), affiliate (payments)
Jurisdictions: US, EU, UK at minimum

Deliver:
1. Compliance risk matrix: each business unit × each regulation (high/med/low risk)
2. Automated compliance monitoring: what can be checked programmatically via APIs
3. Web3 KYC/AML requirements for token sales and DeFi features
4. Data retention and deletion policy for AI-generated user data
5. Affiliate program compliance: FTC disclosure requirements, cookie laws
6. Quarterly compliance review checklist
7. Incident response plan for a data breach or regulatory inquiry""",
        }

        agent_results = self.run_parallel(tasks, context)
        synthesis = self.synthesize(agent_results)

        return SwarmResult(
            swarm_name=self.name,
            objective=objective or self.objective,
            agent_results=agent_results,
            synthesis=synthesis,
        )
