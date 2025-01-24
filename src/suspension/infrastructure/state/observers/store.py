# src/suspension/infrastructure/state/observers/store.py
from typing import Generic, TypeVar

from .base import Observable

State = TypeVar("State")


class ObservableStore(Observable[State], Generic[State]):
    def __init__(self, initial_state: State):
        super().__init__()
        self._state = initial_state

    @property
    def state(self) -> State:
        return self._state

    def set_state(self, new_state: State) -> None:
        self._state = new_state
        self.notify_observers(self._state)
