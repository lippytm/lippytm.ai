"""Cloudflare integration — D1 persistence, KV config, Worker deployment."""
from .platform_hub import PlatformHub

class CloudflareIntegration(PlatformHub):
    """Infrastructure operations for the swarms system."""

    def save_swarm_result(self, swarm_name: str, synthesis: str,
                         total_tokens: int, success_rate: float) -> bool:
        """Persist a swarm run result to D1 for memory and analytics."""
        from datetime import date
        result = self.d1_query(
            "INSERT INTO swarm_results (swarm_name, run_date, synthesis, total_tokens, success_rate) "
            "VALUES (?, ?, ?, ?, ?)",
            [swarm_name, date.today().isoformat(), synthesis[:10000], total_tokens, success_rate]
        )
        return bool(result.get('success'))

    def get_swarm_history(self, swarm_name: str, limit: int = 10) -> list:
        """Retrieve recent run history for a swarm from D1."""
        result = self.d1_query(
            "SELECT * FROM swarm_results WHERE swarm_name = ? ORDER BY created_at DESC LIMIT ?",
            [swarm_name, limit]
        )
        return result.get('result', [{}])[0].get('results', [])
