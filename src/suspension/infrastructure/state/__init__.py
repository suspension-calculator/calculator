# src/suspension/infrastructure/state/__init__.py
from .global_store import store, GlobalStore
from .store import Store, StoreError, ActionError, StateError


__all__ = [
    # Store
    "Store",
    "StoreError",
    "ActionError",
    "StateError",
    # Global store
    "store",
    "GlobalStore",
]
