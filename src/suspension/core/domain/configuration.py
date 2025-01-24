# src/suspension/core/domain/configuration.py

from pydantic import BaseModel, Field


class VehicleConfig(BaseModel):
    wheelbase: float = Field(..., description="Vehicle wheelbase in mm")
    track_width_front: float
    track_width_rear: float
    weight_distribution: float = Field(..., ge=0, le=100)
    mass: float
    cg_height: float
