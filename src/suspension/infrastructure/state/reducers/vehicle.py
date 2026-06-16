# src/suspension/infrastructure/state/reducers/vehicle.py
from ..types.common import Action, ActionType
from ..types.vehicle import VehicleState


def vehicle_reducer(state: VehicleState, action: Action) -> VehicleState:
    match action.type:
        case ActionType.UPDATE_VEHICLE_CONFIG:
            return VehicleState(
                **state.model_dump(), vehicle_config=action.payload.config
            )

        case ActionType.UPDATE_SUSPENSION_CONFIG:
            return VehicleState(
                **state.model_dump(), suspension_config=action.payload.config
            )

        case _:
            return state
