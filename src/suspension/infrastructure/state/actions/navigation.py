# src/suspension/infrastructure/state/actions/navigation.py
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Any


class NavigationActionType(Enum):
    SELECT_ITEM = "SELECT_ITEM"
    SET_ACTIVE_ITEM = "SET_ACTIVE_ITEM"
    TOGGLE_EXPANDED = "TOGGLE_EXPANDED"
    SET_NAV_VISIBLE = "SET_NAV_VISIBLE"
    UPDATE_PAGE = "UPDATE_PAGE"


@dataclass
class NavigationAction:
    """Base class for navigation actions"""

    type: NavigationActionType
    payload: Optional[Any] = None


@dataclass
class SelectItemAction:
    """Action to select a navigation item"""

    def __post_init__(self):
        self.payload = {"item_id": self.item_id}

    item_id: str
    type: NavigationActionType = NavigationActionType.SELECT_ITEM


@dataclass
class SetActiveItemAction:
    """Action to set the active navigation item"""

    def __post_init__(self):
        self.payload = {"item_id": self.item_id}

    item_id: str
    type: NavigationActionType = NavigationActionType.SET_ACTIVE_ITEM


@dataclass
class ToggleExpandedAction:
    """Action to toggle item expansion"""

    def __post_init__(self):
        self.payload = {"item_id": self.item_id}

    item_id: str
    type: NavigationActionType = NavigationActionType.TOGGLE_EXPANDED


@dataclass
class SetNavVisibleAction:
    """Action to set navigation visibility"""

    def __post_init__(self):
        self.payload = {"visible": self.visible}

    visible: bool
    type: NavigationActionType = NavigationActionType.SET_NAV_VISIBLE


@dataclass
class UpdatePageAction:
    """Action to update the current page"""

    def __post_init__(self):
        self.payload = {"page": self.page}

    page: str
    type: NavigationActionType = NavigationActionType.UPDATE_PAGE


# Action creators
def select_item(item_id: str) -> SelectItemAction:
    """Create an action to select a navigation item"""
    return SelectItemAction(item_id=item_id)


def set_active_item(item_id: str) -> SetActiveItemAction:
    """Create an action to set the active navigation item"""
    return SetActiveItemAction(item_id=item_id)


def toggle_expanded(item_id: str) -> ToggleExpandedAction:
    """Create an action to toggle item expansion"""
    return ToggleExpandedAction(item_id=item_id)


def set_nav_visible(visible: bool) -> SetNavVisibleAction:
    """Create an action to set navigation visibility"""
    return SetNavVisibleAction(visible=visible)


def update_page(page: str) -> UpdatePageAction:
    """Create an action to update the current page"""
    return UpdatePageAction(page=page)
