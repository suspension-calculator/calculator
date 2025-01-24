# src/suspension/infrastructure/state/reducers/navigation.py
from ..actions.navigation import (
    NavigationAction,
    SelectItemAction,
    SetActiveItemAction,
    ToggleExpandedAction,
    SetNavVisibleAction,
    UpdatePageAction,
)
from ..types.application import ApplicationState


def navigation_reducer(
    state: ApplicationState, action: NavigationAction
) -> ApplicationState:
    """Handle navigation state updates"""
    match action:
        case SelectItemAction():
            return ApplicationState(
                ui=state.ui.model_copy(
                    update={
                        "navigation": state.ui.navigation.model_copy(
                            update={"selected_item_id": action.item_id}
                        )
                    }
                )
            )

        case SetActiveItemAction():
            return ApplicationState(
                ui=state.ui.model_copy(
                    update={
                        "navigation": state.ui.navigation.model_copy(
                            update={"active_item_id": action.item_id}
                        )
                    }
                )
            )

        case ToggleExpandedAction():
            current_expanded = state.ui.navigation.expanded_item_ids.copy()
            if action.item_id in current_expanded:
                current_expanded.remove(action.item_id)
            else:
                current_expanded.add(action.item_id)

            return ApplicationState(
                ui=state.ui.model_copy(
                    update={
                        "navigation": state.ui.navigation.model_copy(
                            update={"expanded_item_ids": current_expanded}
                        )
                    }
                )
            )

        case SetNavVisibleAction():
            return ApplicationState(
                ui=state.ui.model_copy(
                    update={
                        "navigation": state.ui.navigation.model_copy(
                            update={"nav_pane_visible": action.visible}
                        )
                    }
                )
            )

        case UpdatePageAction():
            current_page = state.ui.navigation.current_page
            return ApplicationState(
                ui=state.ui.model_copy(
                    update={
                        "navigation": state.ui.navigation.model_copy(
                            update={
                                "current_page": action.page,
                                "previous_page": current_page,
                            }
                        )
                    }
                )
            )

        case _:
            return state
