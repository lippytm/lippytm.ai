"""lippytm Life/Business Model AI Swarms — Business of Businesses orchestration engine."""

from .orchestrator import MasterOrchestrator
from .models.business_model import LifeBusinessModel
from .config import CONFIG

__version__ = "2.0.0"
__author__ = "lippytm"
__all__ = ["MasterOrchestrator", "LifeBusinessModel", "CONFIG"]
