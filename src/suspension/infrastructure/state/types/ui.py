# src/suspension/infrastructure/state/types/ui.py
from typing import Dict, Optional

from pydantic import BaseModel, Field, field_validator

# Import directly from their modules
from .plot import PlotState
from .navigation import NavigationState


class UIState(BaseModel):
    """Enhanced UI state with validation"""

    navigation: NavigationState = Field(default_factory=NavigationState)
    current_page: str = ""
    previous_page: Optional[str] = None
    plot_states: Dict[str, PlotState] = Field(default_factory=dict)
    input_values: Dict[str, float] = Field(default_factory=dict)
    is_loading: bool = False
    error_message: Optional[str] = None

    @field_validator("input_values")
    @classmethod
    def validate_input_values(cls, v: Dict[str, float]) -> Dict[str, float]:
        for key, value in v.items():
            if not isinstance(value, (int, float)):
                raise ValueError(f"Input value {key} must be a number")
            if abs(value) > 1e6:
                raise ValueError(f"Input value {key} is outside reasonable range")
        return v
