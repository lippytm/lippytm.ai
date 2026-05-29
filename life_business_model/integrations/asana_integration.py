"""Asana integration — project and task management for all business units."""
from .platform_hub import PlatformHub

class AsanaIntegration(PlatformHub):
    """Thin wrapper exposing Asana-specific helpers."""

    def create_swarm_tasks(self, swarm_name: str, actions: list, project_id: str = None) -> list:
        """Turn swarm action items into Asana tasks."""
        project = project_id or self.ASANA_PROJECT_ECOSYSTEM
        created = []
        for action in actions[:10]:  # cap at 10 tasks per swarm run
            result = self.asana_create_task(
                name=f"[{swarm_name}] {action.get('name', 'Swarm Action')}",
                notes=action.get('description', ''),
                project_id=project,
                due_on=action.get('due_on'),
            )
            if 'data' in result:
                created.append(result['data'])
        return created
