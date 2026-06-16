# src/suspension/state/middleware/persistence_middleware.py

from typing import Callable, Optional
from pathlib import Path
from ..store import Store
from ..types import Action, ActionType, ApplicationState
from ..persistence import PersistenceManager


class PersistenceMiddleware:
    """Middleware for handling state persistence"""

    def __init__(self):
        self.persistence_manager = PersistenceManager()
        self._last_save_path: Optional[Path] = None

    def __call__(
        self,
        store: Store[ApplicationState],
        action: Action,
        next: Callable[[Action], None],
    ) -> None:
        # First let the action process
        next(action)

        # Handle persistence actions
        if action.type == ActionType.SAVE_STATE:
            self._handle_save(store, action)
        elif action.type == ActionType.LOAD_STATE:
            self._handle_load(store, action)

    def _handle_save(self, store: Store[ApplicationState], action: Action) -> None:
        """Handle save state action"""
        try:
            file_path = action.payload.get("file_path") if action.payload else None
            file_path = self.persistence_manager.save(
                store.state, Path(file_path) if file_path else None
            )
            self._last_save_path = file_path
        except Exception as e:
            # Dispatch error action
            store.dispatch(
                Action(
                    type=ActionType.ANALYSIS_ERROR,
                    payload={"error": f"Failed to save state: {str(e)}"},
                )
            )

    def _handle_load(self, store: Store[ApplicationState], action: Action) -> None:
        """Handle load state action"""
        try:
            file_path = action.payload.get("file_path") if action.payload else None
            loaded_state = self.persistence_manager.load(
                ApplicationState, Path(file_path) if file_path else None
            )
            # Update store with loaded state
            store.dispatch(
                Action(type=ActionType.INITIALIZE, payload=loaded_state.model_dump())
            )
        except Exception as e:
            store.dispatch(
                Action(
                    type=ActionType.ANALYSIS_ERROR,
                    payload={"error": f"Failed to load state: {str(e)}"},
                )
            )
