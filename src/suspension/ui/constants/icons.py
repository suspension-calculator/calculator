# src/suspension/ui/constants/icons.py
from enum import Enum
from typing import Optional, Dict, Any
import qtawesome as qta  # type: ignore  # Missing stubs for qtawesome


class AppIcon(str, Enum):
    """Application icon definitions using FontAwesome"""

    GEOMETRY = "fa5s.ruler"
    SUSPENSION = "fa5s.car"
    ANALYSIS = "fa5s.chart-line"
    SETTINGS = "fa5s.cog"
    MAXIMIZE = "fa5s.expand"
    MINIMIZE = "fa5s.compress"

    def to_icon(
        self, color: Optional[str] = None, size: Optional[int] = None
    ) -> qta.icon:
        options: Dict[str, Any] = {}
        if color:
            options["color"] = color
        if size:
            options["scale_factor"] = size
        return qta.icon(self.value, **options)
