# src/suspension/infrastructure/state/reducers/ui.py
from typing import cast
from ..types.common import Action, ActionType
from ..types.ui import UIState


def ui_reducer(state: UIState, action: Action) -> UIState:
    match action.type:
        case ActionType.UPDATE_INPUT_VALUES:
            return UIState(
                **state.model_dump(),
                input_values={**state.input_values, **action.payload.values},
            )

        case ActionType.UPDATE_NAV_VISIBILITY:
            return UIState(**state.model_dump(), nav_visible=action.payload.visible)

        case _:
            return state
