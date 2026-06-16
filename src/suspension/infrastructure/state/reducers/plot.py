# src/suspension/infrastructure/state/reducers/plot.py
from typing import Dict

from ..types.common import Action, ActionType
from ..types.plot import PlotState


def plot_reducer(state: Dict[str, PlotState], action: Action) -> Dict[str, PlotState]:
    match action.type:
        case ActionType.UPDATE_PLOT:
            plot_id = action.payload.plot_id
            current_state = state.get(plot_id, PlotState())

            return {
                **state,
                plot_id: PlotState(
                    **current_state.model_dump(), **action.payload.updates
                ),
            }

        case _:
            return state
