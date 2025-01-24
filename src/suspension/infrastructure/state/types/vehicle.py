# src/suspension/infrastructure/state/types/vehicle.py
from pydantic import BaseModel
from typing import Optional

from suspension.core.domain import VehicleConfig, SuspensionConfig


class VehicleState(BaseModel):
    vehicle_config: Optional[VehicleConfig] = None
    suspension_config: Optional[SuspensionConfig] = None
