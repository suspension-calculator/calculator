# src/suspension/infrastructure/state/selectors/vehicle.py
from typing import Optional

from suspension.core.domain import VehicleConfig, SuspensionConfig
from ..types.application import ApplicationState


def select_vehicle_config(state: ApplicationState) -> Optional[VehicleConfig]:
    """Select vehicle configuration from state"""
    return state.vehicle_config


def select_suspension_config(state: ApplicationState) -> Optional[SuspensionConfig]:
    """Select suspension configuration from state"""
    return state.suspension_config
