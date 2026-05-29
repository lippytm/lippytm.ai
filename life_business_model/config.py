"""Master configuration for the Business of Businesses AI Swarms ecosystem."""

from dataclasses import dataclass, field
from typing import List, Dict
import os


@dataclass
class BusinessConfig:
    """Single source of truth for all swarm and business configuration."""

    # Identity
    owner: str = "lippytm"
    owner_name: str = "Charles Lipshay"
    hub_url: str = "https://lippytm.ai"
    email: str = "lippytimemachines@gmail.com"

    # Claude API — use opus for strategic work, haiku for high-volume tasks
    anthropic_api_key: str = field(default_factory=lambda: os.getenv("ANTHROPIC_API_KEY", ""))
    primary_model: str = "claude-opus-4-8"
    fast_model: str = "claude-haiku-4-5-20251001"
    reasoning_model: str = "claude-opus-4-8"  # extended thinking

    # All 20 business repositories
    repositories: List[str] = field(default_factory=lambda: [
        "lippytm/lippytm.ai",
        "lippytm/factory.ai",
        "lippytm/allbots.com",
        "lippytm/allbots.com.ai",
        "lippytm/web3ai",
        "lippytm/chatlippytm.ai.bots",
        "lippytm/evolutionary-evolutions-social-multimedia-networks-agency-",
        "lippytm/lippytm-lippytm.ai-tower-control-ai",
        "lippytm/the-encyclopedia-of-everything-applied-chataibots",
        "lippytm/the-encyclopedia-of-law-civilian-law-military-law-business-law-ai-law.-",
        "lippytm/time-machines-builders-",
        "lippytm/ai-time-machines",
        "lippytm/quantum-questions-of-the-many-worlds-universes-of-reruns-",
        "lippytm/docs",
        "lippytm/lippytmai.getbizfunds.com-",
        "lippytm/lippytmai.zo.computer-",
        "lippytm/ai-intergalactic-zoological-social-multimedia-agency-networks-",
        "lippytm/ai-autonomous-systems-for-all-of-my-lippytm.ai-repositories-research-and-development-integration-",
        "lippytm/ai-full-stack-ai-devops-synthetic-intelligence-engines-agentsbots-web3-websites-",
        "lippytm/transparency-logic-time-machine-bots-",
    ])

    # Affiliate partners
    affiliates: Dict[str, str] = field(default_factory=lambda: {
        "twin_so": "https://twin.so?via=charles-lipshay",
    })

    # Swarm execution settings
    max_parallel_agents: int = 8
    agent_timeout_seconds: int = 300
    max_conversation_turns: int = 6  # kept in agent memory
    enable_prompt_caching: bool = True  # reduces API costs significantly

    # Financial targets
    target_mrr: float = 167_000.0
    target_arr: float = 2_000_000.0
    target_automation_pct: float = 85.0
    target_hours_per_week: int = 20


CONFIG = BusinessConfig()
