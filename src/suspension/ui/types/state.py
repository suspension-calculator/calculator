"""
Type definitions for UI state management.
"""

from typing import Dict, Union, Optional, TypedDict


StateValue = Union[bool, str, int, None]
StateDict = Dict[str, Union[StateValue, Dict[str, StateValue]]]


class ActionState(TypedDict, total=False):
    """Type definition for action state."""

    checked: Optional[bool]


class MenuState(TypedDict, total=False):
    """Type definition for menu state."""

    visible: bool
    actions: Dict[str, ActionState]
    submenus: Dict[str, "MenuState"]


class ToolbarState(TypedDict, total=False):
    """Type definition for toolbar state."""

    visible: bool
    position: str
    actions: Dict[str, ActionState]
