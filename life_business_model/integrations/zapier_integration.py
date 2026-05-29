"""Zapier integration — trigger 8,000+ automations from swarm results.

Enabled apps: Google Drive (24), Microsoft Office 365 (38),
Notion (31), Gmail (20), GitHub (38), Canva (13)
"""
from .platform_hub import PlatformHub

class ZapierIntegration(PlatformHub):
    """Trigger Zapier webhooks from swarm events."""

    def __init__(self, zapier_webhook_url: str = "", **kwargs):
        super().__init__(**kwargs)
        self._webhook_url = zapier_webhook_url

    def trigger(self, event_name: str, data: dict) -> bool:
        """POST a Zapier catch-hook with event data."""
        import httpx
        if not self._webhook_url:
            return False
        try:
            with httpx.Client() as client:
                resp = client.post(
                    self._webhook_url,
                    json={"event": event_name, **data},
                    timeout=15,
                )
            return resp.status_code < 300
        except Exception:
            return False

    def swarm_complete(self, swarm_name: str, synthesis: str, report_url: str = "") -> bool:
        """Trigger the 'swarm_complete' Zapier zap — notifies Notion + Gmail + Drive."""
        return self.trigger("swarm_complete", {
            "swarm_name": swarm_name,
            "synthesis_preview": synthesis[:500],
            "report_url": report_url,
            "platform": "lippytm.ai",
        })
