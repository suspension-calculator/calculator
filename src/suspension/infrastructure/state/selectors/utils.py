# src/suspension/infrastructure/state/selectors/utils.py

from datetime import timedelta
from typing import TypeVar, Callable, Optional

from memoize.wrapper import memoize
from memoize.configuration import (
    MutableCacheConfiguration,
    DefaultInMemoryCacheConfiguration,
)
from memoize.entrybuilder import ProvidedLifeSpanCacheEntryBuilder
from memoize.eviction import LeastRecentlyUpdatedEvictionStrategy
from memoize.invalidation import InvalidationSupport
from memoize.statuses import InMemoryLocks

T = TypeVar("T")

# Cache profiles for different types of selectors
STABLE_CACHE = {
    "update_after": timedelta(seconds=5),
    "expire_after": timedelta(seconds=30),
    "max_items": 100,
}

DYNAMIC_CACHE = {
    "update_after": timedelta(seconds=1),
    "expire_after": timedelta(seconds=5),
    "max_items": 100,
}

CALCULATION_CACHE = {
    "update_after": timedelta(milliseconds=100),
    "expire_after": timedelta(seconds=1),
    "max_items": 50,
}


def create_selector(
    update_after: Optional[timedelta] = None,
    expire_after: Optional[timedelta] = None,
    max_items: Optional[int] = None,
    method_timeout: Optional[timedelta] = None,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Create a memoized selector with configurable caching options.

    Args:
        update_after: Time after which cache should be updated (in background)
        expire_after: Time after which cache entry expires (blocking refresh)
        max_items: Maximum number of items in cache
        method_timeout: Maximum time for method execution

    Usage:
        @create_selector(**STABLE_CACHE)
        def select_navigation_items(state: ApplicationState) -> Dict[str, NavigationItem]:
            return state.ui.navigation.items
    """
    # Create configuration
    config = MutableCacheConfiguration()
    config.initialized_with(DefaultInMemoryCacheConfiguration())

    # Configure timeouts if provided
    if update_after or expire_after:
        entry_builder = ProvidedLifeSpanCacheEntryBuilder()
        entry_builder.update_timeouts(
            update_after=update_after, expire_after=expire_after
        )
        config.set_entry_builder(entry_builder)

    # Configure max items if provided
    if max_items is not None:
        config.set_eviction_strategy(LeastRecentlyUpdatedEvictionStrategy(max_items))

    # Configure method timeout if provided
    if method_timeout is not None:
        config.set_method_timeout(method_timeout)

    # Create invalidation support
    invalidation = InvalidationSupport()

    # Create update statuses
    update_statuses = InMemoryLocks()

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        return memoize(
            method=func,
            configuration=config,
            invalidation=invalidation,
            update_statuses=update_statuses,
        )

    return decorator
