"""Base swarm class — coordinates multiple agents toward a shared objective."""

import anthropic
from typing import List, Dict, Any, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import datetime

from ..agents.base_agent import BaseAgent, AgentResult
from ..config import CONFIG


@dataclass
class SwarmResult:
    swarm_name: str
    objective: str
    agent_results: List[AgentResult] = field(default_factory=list)
    synthesis: str = ""
    success: bool = True
    timestamp: datetime = field(default_factory=datetime.now)

    @property
    def total_tokens(self) -> int:
        return sum(r.tokens_used for r in self.agent_results)

    @property
    def total_cached_tokens(self) -> int:
        return sum(r.cached_tokens for r in self.agent_results)

    @property
    def success_rate(self) -> float:
        if not self.agent_results:
            return 0.0
        return sum(1 for r in self.agent_results if r.success) / len(self.agent_results)

    @property
    def cache_hit_rate(self) -> float:
        if self.total_tokens == 0:
            return 0.0
        return self.total_cached_tokens / self.total_tokens


class BaseSwarm:
    """
    Coordinates a team of specialized agents toward a common business objective.

    Pattern:
      1. run_parallel()  — agents work concurrently on their domain
      2. synthesize()    — master model merges insights into actionable strategy
      3. execute()       — subclass wires both together for their domain
    """

    def __init__(
        self,
        name: str,
        objective: str,
        client: Optional[anthropic.Anthropic] = None,
    ):
        self.name = name
        self.objective = objective
        self.client = client or anthropic.Anthropic(api_key=CONFIG.anthropic_api_key)
        self.agents: List[BaseAgent] = []
        self._setup_agents()

    def _setup_agents(self):
        """Subclasses populate self.agents here."""
        pass

    def add_agent(self, agent: BaseAgent):
        self.agents.append(agent)

    def _agent_map(self) -> Dict[str, BaseAgent]:
        return {a.name: a for a in self.agents}

    def run_parallel(
        self,
        tasks: Dict[str, str],
        context: Optional[Dict[str, Any]] = None,
        max_workers: int = 5,
    ) -> List[AgentResult]:
        """Run named agents concurrently; return results in completion order."""
        results: List[AgentResult] = []
        agent_map = self._agent_map()

        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            futures = {
                pool.submit(agent_map[name].execute, task, context): name
                for name, task in tasks.items()
                if name in agent_map
            }
            for future in as_completed(futures):
                agent_name = futures[future]
                try:
                    results.append(future.result(timeout=CONFIG.agent_timeout_seconds))
                except Exception as exc:
                    results.append(AgentResult(
                        agent_name=agent_name,
                        task="parallel_task",
                        result=f"Timeout/Error: {exc}",
                        success=False,
                        duration_seconds=0,
                    ))
        return results

    def synthesize(
        self,
        agent_results: List[AgentResult],
        synthesis_prompt: str = "",
    ) -> str:
        """Use the primary model to distill agent outputs into unified strategy."""
        reports = "\n\n".join(
            f"## {r.agent_name}\n{r.result}"
            for r in agent_results
            if r.success
        )

        prompt = synthesis_prompt or (
            f"Synthesize the following {self.name} swarm agent reports into a "
            "unified, prioritized action plan.\n\n"
            "Focus on:\n"
            "1. Top 3 highest-leverage insights\n"
            "2. Immediate actions (next 7 days)\n"
            "3. 30-day milestones\n"
            "4. Revenue impact estimates\n"
            "5. Cross-business synergies\n\n"
            f"Agent Reports:\n{reports}"
        )

        resp = self.client.messages.create(
            model=CONFIG.primary_model,
            max_tokens=2048,
            system=(
                f"You are the synthesis engine for the {self.name} swarm in the "
                "lippytm Business of Businesses. Produce a clear, concise, and "
                "immediately actionable strategic brief."
            ),
            messages=[{"role": "user", "content": prompt}],
        )
        return resp.content[0].text if resp.content else ""

    def execute(
        self,
        objective: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
    ) -> SwarmResult:
        raise NotImplementedError("Subclasses must implement execute().")
