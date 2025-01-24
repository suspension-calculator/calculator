# src/suspension/core/domain/geometry.py
from typing import List, Optional

import numpy as np
from pydantic import BaseModel, Field, computed_field


class Point3D(BaseModel):
    """3D point with computed 2D properties"""

    x: float
    y: float
    z: float

    @computed_field
    def length_2d(self) -> float:
        """Calculate 2D length (x-z plane)"""
        return np.sqrt(self.x**2 + self.z**2)

    @computed_field
    def length_3d(self) -> float:
        """Calculate 3D length"""
        return np.sqrt(self.x**2 + self.y**2 + self.z**2)


class LinkMountPoints(BaseModel):
    """
    Represents mounting points for a link
    Includes computed properties needed for calculations
    """

    frame: Point3D
    axle: Point3D

    @computed_field
    def length_2d(self) -> float:
        """Calculate 2D length between mount points"""
        dx = self.frame.x - self.axle.x
        dz = self.frame.z - self.axle.z
        return np.sqrt(dx**2 + dz**2)

    @computed_field
    def length_3d(self) -> float:
        """Calculate 3D length between mount points"""
        dx = self.frame.x - self.axle.x
        dy = self.frame.y - self.axle.y
        dz = self.frame.z - self.axle.z
        return np.sqrt(dx**2 + dy**2 + dz**2)

    @computed_field
    def convergence_angle(self) -> float:
        """Calculate convergence angle"""
        dy = self.frame.y - self.axle.y
        return np.arccos(
            ((self.axle.x - self.frame.x) ** 2 - dy**2) / (self.length_2d**2)
        )


class SuspensionEnd(BaseModel):
    """
    Represents one end (front/rear) of suspension
    Includes properties needed for both UI and calculations
    """

    upper_links: List[LinkMountPoints]
    lower_links: List[LinkMountPoints]
    panhard: Optional[LinkMountPoints] = None

    # Configuration
    track_width: float = Field(..., gt=0)
    tire_radius: float = Field(..., gt=0)
    portal_height: float = Field(0.0, ge=0)
    axle_tube: float = Field(..., gt=0)
    tire_diameter: float = Field(..., gt=0)
    tire_width: float = Field(..., gt=0)

    # Travel limits
    bump: float
    droop: float

    # Mass properties
    unsprung_mass: float = Field(..., gt=0)

    @computed_field
    def upper_link_count(self) -> int:
        return len(self.upper_links)

    @computed_field
    def has_panhard(self) -> bool:
        return self.panhard is not None

    @computed_field
    def unsprung_cg_height(self) -> float:
        """Calculate CG height of unsprung mass"""
        return self.tire_radius + 0.5 * self.portal_height


class VehicleGeometry(BaseModel):
    """
    Complete vehicle geometry with computed properties
    """

    front: SuspensionEnd
    rear: SuspensionEnd
    wheelbase: float = Field(..., gt=0)
    mass: float = Field(..., gt=0)
    cg_height: float = Field(..., gt=0)
    weight_distribution: float = Field(..., ge=0, le=100)

    @computed_field
    def sprung_mass(self) -> float:
        return self.mass - self.front.unsprung_mass - self.rear.unsprung_mass

    @computed_field
    def cg_x(self) -> float:
        """X position of CG"""
        return self.wheelbase * (self.weight_distribution / 100.0)

    @computed_field
    def sprung_cg_height(self) -> float:
        """Calculate sprung mass CG height"""
        return (
            self.cg_height * self.mass
            - self.front.unsprung_mass * self.front.unsprung_cg_height
            - self.rear.unsprung_mass * self.rear.unsprung_cg_height
        ) / self.sprung_mass
