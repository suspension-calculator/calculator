# src/suspension/infrastructure/state/types/plot.py
from pydantic import BaseModel, Field
from typing import Dict, Any

from suspension.ui.components.base import PlotConfig


class PlotState(BaseModel):
    """State for plot configuration and data"""

    config: PlotConfig
    visible: bool = True
    data: Dict[str, Any] = Field(default_factory=dict)
