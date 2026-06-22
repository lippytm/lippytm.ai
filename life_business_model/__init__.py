"""lippytm Life/Business Model AI Swarms — Business of Businesses orchestration engine."""

from .orchestrator import MasterOrchestrator
from .models.business_model import LifeBusinessModel
from .models.life_os import LifeOS
from .platform_mesh import PlatformMesh
from .system_of_systems import SystemOfSystems
from .config import CONFIG

__version__ = "3.0.0"
__author__ = "lippytm"
__all__ = [
    "MasterOrchestrator", "LifeBusinessModel", "LifeOS",
    "PlatformMesh", "SystemOfSystems", "CONFIG",
]
