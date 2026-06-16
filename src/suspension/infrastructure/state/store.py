# src/suspension/infrastructure/state/store.py
from typing import Callable, List, Optional, TypeVar, Generic, Type, cast
from pydantic import BaseModel, ValidationError
import logging
import time

# Import directly from modules instead of from types package
from .types.common import Action, ActionHandler, Middleware
from .types.application import ApplicationState


class StoreError(Exception):
    """Base exception for store-related errors"""

    pass


class ActionError(StoreError):
    """Error during action dispatch"""

    pass


class StateError(StoreError):
    """Error during state update"""

    pass


T = TypeVar("T", bound=BaseModel)


class Store(Generic[T]):
    """
    Type-safe state container with enhanced error handling and validation
    """

    def __init__(
        self,
        initial_state: T,
        reducer: ActionHandler,
        middleware: Optional[List[Middleware]] = None,
        state_type: Type[T] = cast(Type[T], ApplicationState),
    ):
        self._state: T = initial_state
        self._reducer = reducer
        self._subscribers: List[Callable[[T], None]] = []
        self._middleware: List[Middleware] = middleware or []
        self._logger = logging.getLogger(__name__)
        self._state_type = state_type
        self._last_action: Optional[Action] = None
        self._action_timestamp: Optional[float] = None

    @property
    def state(self) -> T:
        """Get current state (immutable copy)"""
        return self._state.model_copy(deep=True)

    @property
    def last_action(self) -> Optional[Action]:
        """Get the last dispatched action"""
        return self._last_action

    def dispatch(self, action: Action) -> None:
        """
        Dispatch an action to update state with enhanced error handling
        """
        try:
            self._logger.debug(f"Dispatching action: {action.type}")
            self._action_timestamp = time.time()
            self._last_action = action

            # Apply middleware
            for middleware in self._middleware:
                try:
                    middleware(self, action, self._dispatch)
                except Exception as e:
                    self._logger.error(f"Middleware error for {action.type}: {str(e)}")
                    raise ActionError(f"Middleware failed: {str(e)}") from e

            self._dispatch(action)

        except ValidationError as e:
            self._logger.error(f"Validation error for action {action.type}: {str(e)}")
            raise StateError(f"State validation failed: {str(e)}") from e
        except Exception as e:
            self._logger.error(f"Error dispatching action {action.type}: {str(e)}")
            raise ActionError(f"Action dispatch failed: {str(e)}") from e

    def _dispatch(self, action: Action) -> None:
        """Internal dispatch implementation with validation"""
        try:
            old_state = self._state
            new_state = self._reducer(old_state, action)

            # Validate new state
            if not isinstance(new_state, self._state_type):
                raise StateError(f"Invalid state type: {type(new_state)}")

            self._state = new_state

            # Notify subscribers
            for subscriber in self._subscribers:
                try:
                    subscriber(self._state)
                except Exception as e:
                    self._logger.error(f"Subscriber error: {str(e)}")
                    # Continue notifying other subscribers

        except Exception as e:
            self._logger.error(f"State update error: {str(e)}")
            raise StateError(f"State update failed: {str(e)}") from e

    def subscribe(self, callback: Callable[[T], None]) -> Callable[[], None]:
        """Subscribe to state changes with type safety"""
        if not callable(callback):
            raise ValueError("Subscriber must be callable")

        self._subscribers.append(callback)
        return lambda: self._subscribers.remove(callback)

    def add_middleware(self, middleware: Middleware) -> None:
        """Add middleware with type checking"""
        if not callable(middleware):
            raise ValueError("Middleware must be callable")
        self._middleware.append(middleware)
