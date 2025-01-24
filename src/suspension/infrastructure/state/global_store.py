# src/suspension/state/global_store.py
import logging
from typing import Optional

from .middleware import logging_middleware, validation_middleware
from .middleware.persistence_middleware import PersistenceMiddleware
from .reducers import root_reducer
from .store import Store
from .types import ApplicationState, UIState, AnalysisState
from .types.common import ActionType, Action

logger = logging.getLogger(__name__)

# Initialize default state
DEFAULT_STATE = ApplicationState(
    ui=UIState(
        current_page="geometry",  # Changed from current_tab
        plot_states={},
        input_values={},
        page_states={},  # Changed from tab_states
        is_loading=False,
        error_message=None,
        nav_visible=True,
    ),
    analysis=AnalysisState(),
    version="1.0.0",
)


class GlobalStore:
    _instance: Optional[Store[ApplicationState]] = None

    @classmethod
    def get_instance(cls) -> Store[ApplicationState]:
        if cls._instance is None:
            cls._instance = Store[ApplicationState](
                initial_state=DEFAULT_STATE,
                reducer=root_reducer,
                middleware=[
                    logging_middleware,
                    validation_middleware,
                    PersistenceMiddleware(),
                ],
            )
            logger.info("Global store initialized")
        return cls._instance

    @classmethod
    def reset(cls) -> None:
        """Reset store to initial state (useful for testing)"""
        if cls._instance is not None:
            cls._instance.dispatch(Action(type=ActionType.RESET))
            logger.info("Global store reset")


# Create global store instance
store = GlobalStore.get_instance()
