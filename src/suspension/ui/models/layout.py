# src/suspension/ui/models/state_dict.py
"""
Layout configuration models for the Suspension Calculator.
Defines type-safe models for window and panel layouts.
"""

from enum import Enum

from pydantic import BaseModel


class PanelType(str, Enum):
    """Types of panels in the application."""

    NAVIGATION = "navigation"
    DATA_ENTRY = "data_entry"
    PLOT_VIEW = "plot_view"


class PanelConfig(BaseModel):
    """Configuration for a panel."""

    panel_type: PanelType
    min_size: int
    max_size: int
    default_size: int
    resizable: bool = True
    collapsible: bool = True
