# src/suspension/infrastructure/state/reducers/root.py
from .analysis import analysis_reducer
from .ui import ui_reducer
from .vehicle import vehicle_reducer
from ..types.application import ApplicationState
from ..types.common import Action, ActionType
from ..types.vehicle import VehicleState


def root_reducer(state: ApplicationState, action: Action) -> ApplicationState:
    """
    Root reducer that combines all other reducers.
    Each reducer handles its own slice of the state.
    """
    # Handle top-level state reset/load
    if action.type == ActionType.RESET:
        return ApplicationState()

    if action.type == ActionType.LOAD_STATE:
        return ApplicationState(**action.payload)

    # Create vehicle state from current configs
    vehicle_state = VehicleState(
        vehicle_config=state.vehicle_config, suspension_config=state.suspension_config
    )

    # Apply vehicle reducer to get updated vehicle state
    updated_vehicle_state = vehicle_reducer(vehicle_state, action)

    # Apply individual reducers and construct new application state
    return ApplicationState(
        **state.model_dump(),
        analysis=analysis_reducer(state.analysis, action),
        ui=ui_reducer(state.ui, action),
        vehicle_config=updated_vehicle_state.vehicle_config,
        suspension_config=updated_vehicle_state.suspension_config,
    )
