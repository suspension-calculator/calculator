from datetime import timedelta
from typing import TypeVar, Callable, Optional, TypedDict, cast, ParamSpec

# Add type ignores for memoize imports since they lack type stubs
from memoize import Memoizer, LeastRecentlyUpdatedEvictionStrategy  # type: ignore
from memoize.configuration import DefaultInMemoryCacheConfiguration  # type: ignore

T = TypeVar("T")
P = ParamSpec("P")  # For capturing function parameters


class CacheConfig(TypedDict):
    """Type definitions for cache configuration"""

    update_after: timedelta
    expire_after: timedelta
    max_items: int


# Cache profiles with proper typing
STABLE_CACHE: CacheConfig = {
    "update_after": timedelta(seconds=5),
    "expire_after": timedelta(seconds=30),
    "max_items": 100,
}

DYNAMIC_CACHE: CacheConfig = {
    "update_after": timedelta(seconds=1),
    "expire_after": timedelta(seconds=5),
    "max_items": 100,
}

CALCULATION_CACHE: CacheConfig = {
    "update_after": timedelta(milliseconds=100),
    "expire_after": timedelta(seconds=1),
    "max_items": 50,
}

# Initialize memoizer with more specific typing
memoizer = cast(
    Callable[..., Callable[[Callable[P, T]], Callable[P, T]]],
    Memoizer(
        eviction_strategy=LeastRecentlyUpdatedEvictionStrategy,
        configuration=DefaultInMemoryCacheConfiguration(
            max_size=1000,
        ),
    ).memoize,
)


def create_selector(
    update_after: Optional[timedelta] = None,
    expire_after: Optional[timedelta] = None,
    max_items: Optional[int] = None,
    method_timeout: Optional[timedelta] = None,
    force_sync: bool = True,
) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """
    Create a memoized selector with specified caching behavior
    """

    def decorator(func: Callable[P, T]) -> Callable[P, T]:
        if update_after is None:
            return func

        memoized = memoizer(
            update_after=update_after,
            expire_after=expire_after,
            max_items=max_items,
            method_timeout=method_timeout,
            force_sync=force_sync,
        )
        return cast(Callable[P, T], memoized(func))

    return decorator
