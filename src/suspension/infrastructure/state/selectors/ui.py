# src/suspension/infrastructure/state/selectors/ui.py
from typing import Dict, Optional

from .utils import create_selector
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


@create_selector(force_sync=True)
def select_status_message(state: ApplicationState) -> str:
    """
    Select the current status message based on navigation state.
    """
    nav_state = state.ui.navigation

    if nav_state.selected_item_id:
        # Clean up the item name (remove prefix if needed)
        item_name = (
            nav_state.selected_item_id.replace("suspension-", "")
            .replace("-", " ")
            .title()
        )
        message = f"Selected: {item_name}"

        if nav_state.current_page:
            message += f" ({nav_state.current_page})"

        return message

    return "Ready"
