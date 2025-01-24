# src/suspension/infrastructure/state/reducers/__init__.py
from .navigation import navigation_reducer
from .root import root_reducer

__all__ = ["root_reducer", "navigation_reducer"]
