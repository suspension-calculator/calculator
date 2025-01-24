# src/suspension/infrastructure/state/selectors/ui.py
from typing import Dict, Optional
from ..types.application import ApplicationState


def select_input_values(state: ApplicationState) -> Dict[str, float]:
    """Select all input values"""
    return state.ui.input_values


def select_input_value(state: ApplicationState, key: str) -> Optional[float]:
    """Select specific input value"""
    return state.ui.input_values.get(key)


def select_error_message(state: ApplicationState) -> Optional[str]:
    """Select any UI error message"""
    return state.ui.error_message


def select_loading_state(state: ApplicationState) -> bool:
    """Select whether UI is in loading state"""
    return state.ui.is_loading
