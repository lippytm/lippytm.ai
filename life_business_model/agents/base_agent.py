"""Base Claude-powered agent — the atomic unit of every swarm."""

import anthropic
import time
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field


@dataclass
class AgentResult:
    agent_name: str
    task: str
    result: str
    success: bool
    duration_seconds: float
    tokens_used: int = 0
    cached_tokens: int = 0  # prompt cache hits
    metadata: Dict[str, Any] = field(default_factory=dict)

    @property
    def cost_efficiency(self) -> float:
        """Ratio of cached to total tokens — higher is cheaper."""
        if self.tokens_used == 0:
            return 0.0
        return self.cached_tokens / self.tokens_used


class BaseAgent:
    """
    A Claude-powered agent that executes focused tasks.

    Each agent has:
    - A specific role/persona (system prompt)
    - Conversation memory (last N turns)
    - Optional tools
    - Prompt caching for cost efficiency
    """

    def __init__(
        self,
        name: str,
        role: str,
        client: anthropic.Anthropic,
        model: str = "claude-opus-4-8",
        system_prompt: str = "",
        tools: Optional[List[Dict]] = None,
        enable_extended_thinking: bool = False,
        memory_turns: int = 6,
    ):
        self.name = name
        self.role = role
        self.client = client
        self.model = model
        self.system_prompt = system_prompt or self._build_system_prompt()
        self.tools = tools or []
        self.enable_extended_thinking = enable_extended_thinking
        self.memory_turns = memory_turns
        self._history: List[Dict] = []
        self.results: List[AgentResult] = []

    def _build_system_prompt(self) -> str:
        return (
            f"You are {self.name}, a specialized AI agent in the lippytm "
            "Business of Businesses AI swarm system.\n\n"
            f"Your role: {self.role}\n\n"
            "Operating principles:\n"
            "1. Be highly specific and actionable — no vague recommendations.\n"
            "2. Quantify everything: targets, timelines, ROI, resource costs.\n"
            "3. Think leverage: what 20% of actions drive 80% of results?\n"
            "4. Identify automation opportunities to maximize AI ratio.\n"
            "5. Surface cross-business synergies within the 20-repo ecosystem.\n"
            "6. Prioritize passive/recurring revenue over one-time income.\n\n"
            "Always structure your response with clear sections and bullet points."
        )

    def execute(
        self,
        task: str,
        context: Optional[Dict[str, Any]] = None,
        max_tokens: int = 4096,
    ) -> AgentResult:
        """Execute a task and return a structured result."""
        start = time.time()

        # Build context-enriched task
        content = task
        if context:
            import json
            content = f"{task}\n\n--- Context ---\n{json.dumps(context, indent=2, default=str)}"

        messages = list(self._history[-self.memory_turns:])
        messages.append({"role": "user", "content": content})

        try:
            kwargs: Dict[str, Any] = {
                "model": self.model,
                "max_tokens": max_tokens,
                "messages": messages,
                "system": [
                    {
                        "type": "text",
                        "text": self.system_prompt,
                        "cache_control": {"type": "ephemeral"},  # prompt caching
                    }
                ],
            }

            if self.tools:
                kwargs["tools"] = self.tools

            if self.enable_extended_thinking:
                kwargs["thinking"] = {"type": "enabled", "budget_tokens": 3000}

            resp = self.client.messages.create(**kwargs)

            text = "".join(
                block.text for block in resp.content if hasattr(block, "text")
            )

            # Track conversation memory
            self._history.append({"role": "user", "content": content})
            self._history.append({"role": "assistant", "content": text})

            usage = resp.usage
            total_tokens = usage.input_tokens + usage.output_tokens
            cached = getattr(usage, "cache_read_input_tokens", 0) or 0

            result = AgentResult(
                agent_name=self.name,
                task=task[:120],
                result=text,
                success=True,
                duration_seconds=time.time() - start,
                tokens_used=total_tokens,
                cached_tokens=cached,
            )

        except Exception as exc:
            result = AgentResult(
                agent_name=self.name,
                task=task[:120],
                result=f"Error: {exc}",
                success=False,
                duration_seconds=time.time() - start,
            )

        self.results.append(result)
        return result

    def reset(self):
        """Clear conversation memory for a fresh context."""
        self._history.clear()
