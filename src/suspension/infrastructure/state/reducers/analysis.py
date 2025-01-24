# src/suspension/infrastructure/state/reducers/analysis.py
from typing import cast
from ..types.common import Action, ActionType
from ..types.analysis import AnalysisState


def analysis_reducer(state: AnalysisState, action: Action) -> AnalysisState:
    match action.type:
        case ActionType.START_ANALYSIS:
            return AnalysisState(
                is_running=True,
                error=None,
                progress=0.0,
                results=state.results,
                last_update=state.last_update,
            )

        case ActionType.ANALYSIS_COMPLETE:
            return AnalysisState(
                is_running=False,
                results=action.payload.results,
                progress=1.0,
                error=None,
                last_update=state.last_update,
            )

        case ActionType.ANALYSIS_ERROR:
            return AnalysisState(
                is_running=False,
                error=action.payload.error,
                progress=0.0,
                results=state.results,
                last_update=state.last_update,
            )

        case ActionType.UPDATE_ANALYSIS_RESULTS:
            return AnalysisState(
                **state.model_dump(),
                results=action.payload.results,
                progress=action.payload.progress,
            )

        case _:
            return state
