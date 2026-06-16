# src/suspension/infrastructure/state/selectors/plot.py
from typing import Dict, Any
from ..types.application import ApplicationState
from ..types.plot import PlotState


def select_plot_state(state: ApplicationState, plot_id: str) -> PlotState:
    """Select specific plot state"""
    return state.ui.plot_states.get(plot_id)


def select_plot_visibility(state: ApplicationState, plot_id: str) -> bool:
    """Select visibility of specific plot"""
    plot_state = state.ui.plot_states.get(plot_id)
    return plot_state.visible if plot_state else False


def select_plot_data(state: ApplicationState, plot_id: str) -> Dict[str, Any]:
    """Select data for specific plot"""
    plot_state = state.ui.plot_states.get(plot_id)
    return plot_state.data if plot_state else {}
