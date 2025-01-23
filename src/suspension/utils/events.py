# src/suspension/utils/events.py
from dataclasses import dataclass
from typing import Any, Callable, Dict, List


@dataclass
class Event:
    name: str
    data: Any


class EventBus:
    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event_name: str, callback: Callable):
        if event_name not in self.subscribers:
            self.subscribers[event_name] = []
        self.subscribers[event_name].append(callback)

    def publish(self, event: Event):
        for callback in self.subscribers.get(event.name, []):
            callback(event.data)
