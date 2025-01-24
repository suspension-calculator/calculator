# src/suspension/infrastructure/state/selectors/navigation.py
from typing import Optional, Set, Dict
from ..types.application import ApplicationState
from ..types.navigation import NavigationItem
from .utils import create_selector, STABLE_CACHE, DYNAMIC_CACHE


# State-based selectors with DYNAMIC_CACHE
@create_selector(**DYNAMIC_CACHE)
def select_selected_item_id(state: ApplicationState) -> Optional[str]:
    """Select the currently selected item ID"""
    return state.ui.navigation.selected_item_id


@create_selector(**DYNAMIC_CACHE)
def select_active_item_id(state: ApplicationState) -> Optional[str]:
    """Select the currently active item ID"""
    return state.ui.navigation.active_item_id


@create_selector(**DYNAMIC_CACHE)
def select_expanded_item_ids(state: ApplicationState) -> Set[str]:
    """Select the set of expanded item IDs"""
    return state.ui.navigation.expanded_item_ids


@create_selector(**DYNAMIC_CACHE)
def select_nav_pane_visible(state: ApplicationState) -> bool:
    """Select whether the navigation pane is visible"""
    return state.ui.navigation.nav_pane_visible


@create_selector(**DYNAMIC_CACHE)
def select_current_page(state: ApplicationState) -> Optional[str]:
    """Select the current page"""
    return state.ui.navigation.current_page


@create_selector(**DYNAMIC_CACHE)
def select_previous_page(state: ApplicationState) -> Optional[str]:
    """Select the previous page"""
    return state.ui.navigation.previous_page


# Structure-based selectors with STABLE_CACHE
@create_selector(**STABLE_CACHE)
def select_navigation_items(state: ApplicationState) -> Dict[str, NavigationItem]:
    """Select all navigation items"""
    return state.ui.navigation.items


@create_selector(**STABLE_CACHE)
def select_navigation_item(
    state: ApplicationState, item_id: str
) -> Optional[NavigationItem]:
    """Select a specific navigation item by ID"""
    return state.ui.navigation.items.get(item_id)


# Lightweight boolean checks - no memoization
def is_item_expanded(state: ApplicationState, item_id: str) -> bool:
    """Check if a specific item is expanded"""
    return item_id in state.ui.navigation.expanded_item_ids


def is_item_active(state: ApplicationState, item_id: str) -> bool:
    """Check if a specific item is currently active"""
    return state.ui.navigation.active_item_id == item_id


def is_item_selected(state: ApplicationState, item_id: str) -> bool:
    """Check if a specific item is currently selected"""
    return state.ui.navigation.selected_item_id == item_id


# More expensive structure-based selectors with STABLE_CACHE
@create_selector(**STABLE_CACHE)
def select_child_items(
    state: ApplicationState, parent_id: str
) -> Dict[str, NavigationItem]:
    """Select all child items for a given parent ID"""
    return {
        item_id: item
        for item_id, item in state.ui.navigation.items.items()
        if item.parent_id == parent_id
    }


@create_selector(**STABLE_CACHE)
def select_root_items(state: ApplicationState) -> Dict[str, NavigationItem]:
    """Select all root-level navigation items"""
    return {
        item_id: item
        for item_id, item in state.ui.navigation.items.items()
        if item.parent_id is None
    }
