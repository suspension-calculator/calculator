# src/suspension/ui/base/models.py
from enum import Enum
from typing import Dict, Optional, Any, List, Tuple, Callable

from pydantic import BaseModel, Field


class InputField(BaseModel):
    """Model for input field configuration"""

    label: str
    default: float = 0.0
    validator: Optional[Callable[[float], bool]] = None
    width: int = 6
    unit: Optional[str] = None


class NavButtonConfig(BaseModel):
    """Model for navigation button configuration"""

    text: str
    command: Optional[Callable[[], None]] = None
    width: int = 10
    enabled: bool = True


class PlotType(str, Enum):
    SUSPENSION = "suspension"
    MOTION_RATIO = "motion_ratio"
    FORCE_CURVE = "force_curve"


class PlotStyle(BaseModel):
    face_color: str = Field(default="#2b2b2b")
    edge_color: str = Field(default="#ffffff")
    grid_color: str = Field(default="#404040")
    text_color: str = Field(default="#ffffff")
    dpi: int = Field(default=100)
    figsize: Tuple[float, float] = Field(default=(8, 6))


class PlotConfig(BaseModel):
    plot_type: PlotType
    title: Optional[str] = None
    xlabel: Optional[str] = None
    ylabel: Optional[str] = None
    style: PlotStyle = Field(default_factory=PlotStyle)
    additional_config: Dict[str, Any] = Field(default_factory=dict)


class PlotData(BaseModel):
    x: List[float]
    y: List[float]
    label: Optional[str] = None
    style: Dict[str, Any] = Field(default_factory=dict)


class TabState(BaseModel):
    """Base model for tab state management"""

    tab_name: str
    plot_configs: Dict[str, PlotConfig] = Field(default_factory=dict)
    plot_data: Dict[str, List[PlotData]] = Field(default_factory=dict)
    ui_state: Dict[str, Any] = Field(default_factory=dict)
