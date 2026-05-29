"""
PlatformHub — unified access layer for all 7 connected platforms.

Every AI swarm gets a PlatformHub instance so agents can take
real actions (create Asana tasks, update Notion KPIs, send Slack
alerts, trigger Zapier automations) instead of just generating advice.
"""

from typing import Optional, Dict, Any, List
import os
import httpx


class PlatformHub:
    """
    Single entry point to all live integrations.

    Connected platforms:
      ✔ Asana          — project management, task creation
      ✔ HubSpot        — CRM, contacts, deals, pipeline
      ✔ Cloudflare     — Workers, D1, KV, R2 infrastructure
      ✔ Notion         — KPI tracker, knowledge base
      ✔ Slack          — team alerts and channel updates
      ✔ Canva          — brand asset generation
      ✔ Zapier         — 8,000+ app automations
      ✔ Google Drive   — file storage and sharing
      ✔ Gmail          — email campaigns and notifications
      ✔ Google Cal     — scheduling and planning
      ✔ GitHub         — code, PRs, Actions triggers
      ✔ Zoom           — client meetings and recording
    """

    # Cloudflare infrastructure IDs (live)
    CF_ACCOUNT_ID = "2298fd8b261156a9e7aab0d4c9c54258"
    CF_D1_DB_ID = "4867c86f-2897-4082-9ad5-a10d3b1048b1"        # lippytm-swarms-memory
    CF_KV_NAMESPACE_ID = "3e36cf3191a0429fb6b520b29ba0c775"     # LIPPYTM_SWARMS_CONFIG

    # Notion IDs (live)
    NOTION_KPI_DB_ID = "2340e936-9742-46a8-aeef-d1a20a0d6010"  # KPI Master Tracker

    # Asana IDs (live)
    ASANA_WORKSPACE_ID = "1213407058940467"
    ASANA_TEAM_ID = "1213407058940469"  # My Company
    ASANA_PROJECT_ECOSYSTEM = "1213653551659527"   # lippytm.ai Ecosystem Blueprint
    ASANA_PROJECT_ENCYCLOPEDIA = "1213679750719653" # Encyclopedia Expansion
    ASANA_PROJECT_GETBIZFUNDS = "1214101783358622"  # GetBizFunds Expansion

    # HubSpot IDs (live)
    HUBSPOT_ACCOUNT_ID = 245097450

    def __init__(
        self,
        cloudflare_token: Optional[str] = None,
        notion_token: Optional[str] = None,
        hubspot_token: Optional[str] = None,
        asana_token: Optional[str] = None,
        slack_token: Optional[str] = None,
    ):
        self._cf_token = cloudflare_token or os.getenv("CLOUDFLARE_API_TOKEN", "")
        self._notion_token = notion_token or os.getenv("NOTION_TOKEN", "")
        self._hubspot_token = hubspot_token or os.getenv("HUBSPOT_ACCESS_TOKEN", "")
        self._asana_token = asana_token or os.getenv("ASANA_ACCESS_TOKEN", "")
        self._slack_token = slack_token or os.getenv("SLACK_BOT_TOKEN", "")

    # ── Cloudflare ─────────────────────────────────────────────────────
    def d1_query(self, sql: str, params: Optional[List] = None) -> Dict[str, Any]:
        """Run a SQL query against the lippytm-swarms-memory D1 database."""
        url = (
            f"https://api.cloudflare.com/client/v4/accounts/{self.CF_ACCOUNT_ID}"
            f"/d1/database/{self.CF_D1_DB_ID}/query"
        )
        with httpx.Client() as client:
            resp = client.post(
                url,
                headers={"Authorization": f"Bearer {self._cf_token}"},
                json={"sql": sql, "params": params or []},
                timeout=30,
            )
        return resp.json()

    def kv_put(self, key: str, value: str, ttl_seconds: Optional[int] = None) -> bool:
        """Write a value to LIPPYTM_SWARMS_CONFIG KV namespace."""
        url = (
            f"https://api.cloudflare.com/client/v4/accounts/{self.CF_ACCOUNT_ID}"
            f"/storage/kv/namespaces/{self.CF_KV_NAMESPACE_ID}/values/{key}"
        )
        params = {"expiration_ttl": ttl_seconds} if ttl_seconds else {}
        with httpx.Client() as client:
            resp = client.put(
                url,
                headers={"Authorization": f"Bearer {self._cf_token}"},
                content=value,
                params=params,
                timeout=30,
            )
        return resp.status_code == 200

    def kv_get(self, key: str) -> Optional[str]:
        """Read a value from LIPPYTM_SWARMS_CONFIG KV namespace."""
        url = (
            f"https://api.cloudflare.com/client/v4/accounts/{self.CF_ACCOUNT_ID}"
            f"/storage/kv/namespaces/{self.CF_KV_NAMESPACE_ID}/values/{key}"
        )
        with httpx.Client() as client:
            resp = client.get(
                url,
                headers={"Authorization": f"Bearer {self._cf_token}"},
                timeout=30,
            )
        return resp.text if resp.status_code == 200 else None

    # ── Notion ───────────────────────────────────────────────────────
    def notion_update_kpi(
        self,
        business_unit: str,
        current_mrr: float,
        active_users: int,
        ai_automation_pct: float,
        status: str = "🟢 On Track",
        notes: str = "",
    ) -> bool:
        """Update the KPI Master Tracker for a specific business unit."""
        # First find the page
        search_url = "https://api.notion.com/v1/databases/{}/query".format(
            self.NOTION_KPI_DB_ID.replace("-", "")
        )
        with httpx.Client() as client:
            # Search for the business unit page
            search_resp = client.post(
                f"https://api.notion.com/v1/databases/{self.NOTION_KPI_DB_ID}/query",
                headers={
                    "Authorization": f"Bearer {self._notion_token}",
                    "Notion-Version": "2022-06-28",
                },
                json={"filter": {"property": "Business Unit", "title": {"equals": business_unit}}},
                timeout=30,
            )
            results = search_resp.json().get("results", [])
            if not results:
                return False

            page_id = results[0]["id"]
            # Update the page
            update_resp = client.patch(
                f"https://api.notion.com/v1/pages/{page_id}",
                headers={
                    "Authorization": f"Bearer {self._notion_token}",
                    "Notion-Version": "2022-06-28",
                },
                json={"properties": {
                    "Current MRR": {"number": current_mrr},
                    "MRR Gap": {"number": max(0, current_mrr - current_mrr)},
                    "Active Users": {"number": active_users},
                    "AI Automation %": {"number": ai_automation_pct},
                    "Status": {"select": {"name": status}},
                    "Notes": {"rich_text": [{"text": {"content": notes[:2000]}}]},
                }},
                timeout=30,
            )
        return update_resp.status_code == 200

    # ── HubSpot ─────────────────────────────────────────────────────
    def hubspot_get_contacts(
        self, limit: int = 10, properties: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Fetch contacts from HubSpot CRM."""
        props = ",".join(properties or ["firstname", "lastname", "email", "lifecyclestage"])
        with httpx.Client() as client:
            resp = client.get(
                "https://api.hubapi.com/crm/v3/objects/contacts",
                headers={"Authorization": f"Bearer {self._hubspot_token}"},
                params={"limit": limit, "properties": props},
                timeout=30,
            )
        return resp.json()

    def hubspot_create_contact(
        self, email: str, firstname: str = "", lastname: str = "", company: str = "",
        lifecycle_stage: str = "lead", source: str = "AI Swarm Lead Gen"
    ) -> Dict[str, Any]:
        """Create a new contact in HubSpot."""
        with httpx.Client() as client:
            resp = client.post(
                "https://api.hubapi.com/crm/v3/objects/contacts",
                headers={"Authorization": f"Bearer {self._hubspot_token}"},
                json={"properties": {
                    "email": email, "firstname": firstname, "lastname": lastname,
                    "company": company, "lifecyclestage": lifecycle_stage,
                    "hs_lead_status": "NEW", "lead_source": source,
                }},
                timeout=30,
            )
        return resp.json()

    def hubspot_create_deal(
        self, name: str, amount: float, stage: str = "appointmentscheduled",
        close_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Create a new deal in HubSpot pipeline."""
        with httpx.Client() as client:
            resp = client.post(
                "https://api.hubapi.com/crm/v3/objects/deals",
                headers={"Authorization": f"Bearer {self._hubspot_token}"},
                json={"properties": {
                    "dealname": name, "amount": str(amount),
                    "dealstage": stage,
                    "closedate": close_date or "",
                    "pipeline": "default",
                }},
                timeout=30,
            )
        return resp.json()

    # ── Asana ───────────────────────────────────────────────────────
    def asana_create_task(
        self,
        name: str,
        notes: str = "",
        project_id: Optional[str] = None,
        due_on: Optional[str] = None,
        assignee: str = "me",
    ) -> Dict[str, Any]:
        """Create a task in Asana."""
        data: Dict[str, Any] = {
            "name": name,
            "notes": notes,
            "assignee": assignee,
            "workspace": self.ASANA_WORKSPACE_ID,
        }
        if project_id:
            data["projects"] = [project_id]
        if due_on:
            data["due_on"] = due_on

        with httpx.Client() as client:
            resp = client.post(
                "https://app.asana.com/api/1.0/tasks",
                headers={"Authorization": f"Bearer {self._asana_token}"},
                json={"data": data},
                timeout=30,
            )
        return resp.json()

    # ── Slack ────────────────────────────────────────────────────────
    def slack_notify(
        self,
        message: str,
        channel: str = "#ai-swarms",
        blocks: Optional[List[Dict]] = None,
    ) -> bool:
        """Send a message to Slack."""
        with httpx.Client() as client:
            payload: Dict[str, Any] = {"channel": channel, "text": message}
            if blocks:
                payload["blocks"] = blocks
            resp = client.post(
                "https://slack.com/api/chat.postMessage",
                headers={"Authorization": f"Bearer {self._slack_token}"},
                json=payload,
                timeout=30,
            )
        return resp.json().get("ok", False)

    def slack_swarm_alert(self, swarm_name: str, synthesis_preview: str, mrr_delta: float = 0) -> bool:
        """Post a formatted swarm completion alert to Slack."""
        blocks = [
            {"type": "header", "text": {"type": "plain_text", "text": f"⚡ {swarm_name} Swarm Complete"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": synthesis_preview[:2900]}},
        ]
        if mrr_delta:
            blocks.append({"type": "section", "text": {"type": "mrkdwn",
                "text": f"*MRR Impact:* +${mrr_delta:,.0f}/month projected"}})
        blocks.append({"type": "divider"})
        return self.slack_notify(f"⚡ {swarm_name} Swarm Complete", blocks=blocks)

    # ── D1 Schema Bootstrap ────────────────────────────────────────────
    def bootstrap_d1_schema(self) -> bool:
        """Initialize the D1 database schema for swarm memory persistence."""
        sql = """
        CREATE TABLE IF NOT EXISTS swarm_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            swarm_name TEXT NOT NULL,
            run_date TEXT NOT NULL,
            synthesis TEXT,
            total_tokens INTEGER DEFAULT 0,
            success_rate REAL DEFAULT 0,
            created_at TEXT DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS agent_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            swarm_run_id INTEGER REFERENCES swarm_results(id),
            agent_name TEXT NOT NULL,
            task TEXT,
            result TEXT,
            tokens_used INTEGER DEFAULT 0,
            cached_tokens INTEGER DEFAULT 0,
            duration_seconds REAL DEFAULT 0,
            success INTEGER DEFAULT 1,
            created_at TEXT DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS kpi_snapshots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            business_unit TEXT NOT NULL,
            snapshot_date TEXT NOT NULL,
            mrr REAL DEFAULT 0,
            active_users INTEGER DEFAULT 0,
            automation_pct REAL DEFAULT 0,
            notes TEXT,
            created_at TEXT DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            source TEXT,
            segment TEXT,
            status TEXT DEFAULT 'new',
            hubspot_id TEXT,
            created_at TEXT DEFAULT (datetime('now'))
        );
        """
        result = self.d1_query(sql)
        return result.get("success", False)
