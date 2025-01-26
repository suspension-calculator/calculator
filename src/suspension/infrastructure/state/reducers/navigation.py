# src/suspension/infrastructure/state/reducers/navigation.py
import logging

from ..actions.navigation import (
    NavigationAction,
    SetActiveItemAction,
    ToggleExpandedAction,
    SetNavVisibleAction,
    UpdatePageAction,
)
from ..types.application import ApplicationState

logger = logging.getLogger(__name__)


def navigation_reducer(
    state: ApplicationState, action: NavigationAction
) -> ApplicationState:
    """Handle navigation state updates"""
    match action:
        case ToggleExpandedAction():
            current_expanded = state.ui.navigation.expanded_item_ids.copy()
            item_id = action.payload["item_id"]

            if item_id in current_expanded:
                current_expanded.remove(item_id)
            else:
                current_expanded.add(item_id)

            return ApplicationState(
                ui=state.ui.model_copy(
                    update={
                        "navigation": state.ui.navigation.model_copy(
                            update={"expanded_item_ids": current_expanded}
                        )
                    }
                )
            )

        case SetActiveItemAction():
            item_id = action.payload["item_id"]
            return ApplicationState(
                ui=state.ui.model_copy(
                    update={
                        "navigation": state.ui.navigation.model_copy(
                            update={"active_item_id": item_id}
                        )
                    }
                )
            )

        case ToggleExpandedAction():
            current_expanded = state.ui.navigation.expanded_item_ids.copy()
            item_id = action.payload["item_id"]
            logger.debug(f"Toggling expansion for item: {item_id}")
            logger.debug(f"Current expanded items before: {current_expanded}")

            if item_id in current_expanded:
                current_expanded.remove(item_id)
            else:
                current_expanded.add(item_id)

            logger.debug(f"Current expanded items after: {current_expanded}")

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
            visible = action.payload["visible"]
            logger.debug(f"Setting nav pane visibility to: {visible}")

            return ApplicationState(
                ui=state.ui.model_copy(
                    update={
                        "navigation": state.ui.navigation.model_copy(
                            update={"nav_pane_visible": visible}
                        )
                    }
                )
            )

        case UpdatePageAction():
            current_page = state.ui.navigation.current_page
            page = action.payload["page"]

            return ApplicationState(
                ui=state.ui.model_copy(
                    update={
                        "navigation": state.ui.navigation.model_copy(
                            update={
                                "current_page": page,
                                "previous_page": current_page,
                            }
                        )
                    }
                )
            )

        case _:
            return state
