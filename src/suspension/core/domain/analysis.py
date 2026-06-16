# src/suspension/core/domain/analysis.py
from typing import List, Optional

from pydantic import BaseModel, computed_field


class LinkAnalysis(BaseModel):
    """Analysis results for a single link"""

    force_curve: List[float]
    max_force: float
    convergence: float
    length_2d: float
    length_3d: float
    side_view_angle_range: tuple[float, float]
    top_view_angle_range: tuple[float, float]


class SuspensionAnalysis(BaseModel):
    """Analysis results for one end of suspension"""

    upper_link: LinkAnalysis
    lower_link: LinkAnalysis
    panhard: Optional[LinkAnalysis] = None
    roll_center_height: List[float]
    roll_slope: List[float]
    anti_features: List[float]
    travel_positions: List[float]
    pinion_angle: List[float]

    @computed_field
    def total_convergence(self) -> float:
        """Calculate total convergence angle"""
        if self.panhard:
            # Use panhard-based calculation
            return abs(self.panhard.convergence)
        else:
            # Use link-based calculation
            return abs(self.upper_link.convergence) + abs(self.lower_link.convergence)
