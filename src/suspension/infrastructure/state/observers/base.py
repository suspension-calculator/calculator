# src/suspension/infrastructure/state/observers/base.py
from typing import Any, List, Generic, TypeVar, Protocol
from abc import abstractmethod

T = TypeVar("T")


class Observer(Protocol):
    """Protocol for observers instead of ABC to avoid metaclass conflicts"""

    @abstractmethod
    def on_state_changed(self, state: Any) -> None:
        pass


class Observable(Generic[T]):
    def __init__(self):
        self._observers: List[Observer] = []

    def add_observer(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, state: T) -> None:
        for observer in self._observers:
            observer.on_state_changed(state)
