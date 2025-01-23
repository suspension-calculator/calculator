# src/suspension/core/models/link_models.py
from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from enum import Enum


class LinkMeasurements(BaseModel):
    """Basic link measurements"""

    length_3d: float
    length_2d: float
    convergence_angle: Optional[float] = None


class LinkForces(BaseModel):
    """Forces calculated for links"""

    max_force: float
    current_force: float


class LinkPosition(BaseModel):
    """3D position data for link mounting points"""

    frame_x: float
    frame_y: float
    frame_z: float
    axle_x: float
    axle_y: float
    axle_z: float


class SuspensionConfig(BaseModel):
    """Configuration for one end of the suspension"""

    upper_link_count: int = Field(1, ge=1, le=2)
    has_panhard: bool = False
    bump_travel: float
    droop_travel: float
    unsprung_mass: float
    tire_radius: float
    track_width: float
    portal_height: float = 0.0
    axle_tube_diameter: float
    tire_diameter: float
    tire_width: float


class SuspensionResults(BaseModel):
    """Calculation results for one end"""

    anti_features: List[float]
    roll_center_height: List[float]
    roll_slope: List[float]
    pinion_angle: List[float]
    travel_positions: List[float]
