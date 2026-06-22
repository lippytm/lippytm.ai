"""Platform Mesh — registry and dispatch layer for every external system
the Business of Businesses depends on: GitHub, Slack, Notion, Cloudflare,
HubSpot, Asana, and the Anthropic/OpenAI model providers.

This does not reimplement each platform's SDK. It gives the System of
Systems orchestrator one place to ask "what's connected, what does it do,
and how do I notify it" without hardcoding platform specifics everywhere.
"""

import json
import os
import urllib.request
from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class Platform:
    name: str
    role: str
    env_var: Optional[str] = None
    required: bool = False

    @property
    def connected(self) -> bool:
        if not self.env_var:
            return True  # reached via MCP tools / dashboard, not env-gated here
        return bool(os.getenv(self.env_var))


class PlatformMesh:
    """
    The integration layer of the System of Systems.

    Tracks which external platforms power the empire and exposes a single
    notify() call that fans out to whichever channels are actually configured.
    """

    REGISTRY: Dict[str, Platform] = {
        "github": Platform("GitHub", "Source of truth — code, Actions automation, 20 repos"),
        "slack": Platform("Slack", "Real-time notifications and team comms", env_var="SLACK_WEBHOOK_URL"),
        "notion": Platform("Notion", "Knowledge base, docs, meeting notes"),
        "cloudflare": Platform("Cloudflare", "Workers API, D1 memory, KV config, R2 storage"),
        "hubspot": Platform("HubSpot", "CRM, marketing automation, landing pages"),
        "asana": Platform("Asana", "Task and project tracking for the execution playbook"),
        "anthropic": Platform("Anthropic / Claude", "Primary reasoning engine for all swarms", env_var="ANTHROPIC_API_KEY", required=True),
        "openai": Platform("OpenAI / ChatGPT", "Creative ensemble diversity engine", env_var="OPENAI_API_KEY"),
    }

    def status(self) -> Dict[str, Any]:
        return {
            key: {
                "name": p.name,
                "role": p.role,
                "connected": p.connected,
                "required": p.required,
            }
            for key, p in self.REGISTRY.items()
        }

    def print_status(self) -> None:
        print("\n" + "─" * 70)
        print("  🕸️  PLATFORM MESH STATUS")
        print("─" * 70)
        for info in self.status().values():
            mark = "✅" if info["connected"] else ("❌" if info["required"] else "⚪")
            print(f"  {mark} {info['name']:<20} {info['role']}")
        print("─" * 70)

    def notify_slack(self, text: str) -> bool:
        webhook = os.getenv("SLACK_WEBHOOK_URL")
        if not webhook:
            return False
        payload = json.dumps({"text": text}).encode("utf-8")
        req = urllib.request.Request(webhook, data=payload, headers={"Content-Type": "application/json"})
        try:
            urllib.request.urlopen(req, timeout=10)
            return True
        except Exception:
            return False

    def notify(self, text: str) -> Dict[str, bool]:
        """Fan out a notification to every connected channel that supports push."""
        return {"slack": self.notify_slack(text)}
