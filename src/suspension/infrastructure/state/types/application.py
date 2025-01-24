# src/suspension/infrastructure/state/types/application.py
import re
from typing import Optional

from pydantic import BaseModel, Field, field_validator

# Import directly from the modules instead of through types/__init__.py
from .ui import UIState
from .analysis import AnalysisState
from suspension.core.domain import VehicleConfig, SuspensionConfig


class ApplicationState(BaseModel):
    """Root application state with enhanced validation"""

    ui: UIState
    vehicle_config: Optional[VehicleConfig] = None
    suspension_config: Optional[SuspensionConfig] = None
    analysis: AnalysisState = Field(default_factory=AnalysisState)
    version: str = "1.0.0"
    last_saved: Optional[float] = None

    @field_validator("version")
    @classmethod
    def validate_version(cls, v: str) -> str:
        if not re.match(r"^\d+\.\d+\.\d+$", v):
            raise ValueError("Invalid version format")
        return v
