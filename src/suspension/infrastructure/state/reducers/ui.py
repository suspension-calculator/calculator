# src/suspension/infrastructure/state/reducers/ui.py
from ..types.application import ApplicationState
from ..types.common import Action
from ..actions.navigation import NavigationActionType
from ..reducers.navigation import navigation_reducer


def ui_reducer(state, action: Action):
    """Combine UI-related reducers"""

    # If it's a navigation action, use navigation reducer
    if action.type in [
        NavigationActionType.SELECT_ITEM,
        NavigationActionType.SET_ACTIVE_ITEM,
        NavigationActionType.TOGGLE_EXPANDED,
        NavigationActionType.SET_NAV_VISIBLE,
        NavigationActionType.UPDATE_PAGE,
    ]:
        new_ui_state = state.model_copy(
            update={
                "navigation": navigation_reducer(
                    ApplicationState(ui=state), action
                ).ui.navigation
            }
        )
    else:
        new_ui_state = state

    print(f"New UI State: {new_ui_state}\n")
    return new_ui_state
