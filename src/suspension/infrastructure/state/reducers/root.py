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

    # Create a new state dictionary, removing keys that will be explicitly passed
    state_dict = state.model_dump()
    keys_to_remove = ["analysis", "ui", "vehicle_config", "suspension_config"]
    for key in keys_to_remove:
        state_dict.pop(key, None)

    # Apply individual reducers and construct new application state
    new_state = ApplicationState(
        **state_dict,
        analysis=analysis_reducer(state.analysis, action),
        ui=ui_reducer(state.ui, action),
        vehicle_config=updated_vehicle_state.vehicle_config,
        suspension_config=updated_vehicle_state.suspension_config,
    )

    print(f"New State: {new_state}\n")
    return new_state
