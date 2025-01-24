# src/suspension/infrastructure/state/types/analysis.py
from typing import Optional

from pydantic import BaseModel, Field

from suspension.core.domain import SuspensionResults


class AnalysisState(BaseModel):
    results: Optional[SuspensionResults] = None
    is_running: bool = False
    error: Optional[str] = None
    progress: float = Field(0.0, ge=0.0, le=1.0)
    last_update: Optional[float] = None
