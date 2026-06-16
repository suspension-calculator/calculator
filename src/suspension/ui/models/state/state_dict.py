from typing import Dict, Optional, Set, TypedDict


class ComponentState(TypedDict):
    """
    Type-safe component layout state.

    Attributes:
        dock_area: Qt dock area enum value for dockable components
        floating: Whether a dock widget is floating
        width: Current width for resizable components like drawers
        collapsed: Whether a collapsible component is collapsed
        size_ratio: Optional size within a splitter container (0-1)
        geometry: Base64 encoded geometry state
    """

    dock_area: Optional[int]  # None if not a dock widget
    floating: bool  # For dock widgets
    width: Optional[int]  # For resizable components like drawer
    collapsed: bool  # For collapsible components like drawer
    size_ratio: Optional[float]  # For splitter-based sizing (0-1)
    geometry: Optional[str]  # Base64 encoded geometry state


# class PanelState(TypedDict):
#     """Type-safe state definition for a panel."""
#
#     visible: bool
#     size: int  # Size in pixels
#     position: int  # Index in splitter


class PanelState(TypedDict):
    """Type-safe panel state definition."""

    layout: Dict[str, Dict[str, int]]  # panel_id -> {dock_area, index}
    visible: Set[str]  # Set of visible panel IDs


class LayoutState(TypedDict):
    """Type-safe state definition for the entire layout."""

    nav_panel: PanelState
    data_panel: PanelState
    plot_panel: PanelState
    toolbar_state: bytes
    geometry: bytes


class WindowState(TypedDict):
    """Type-safe state definition for window configuration."""

    geometry: bytes
    state: bytes  # Window state including toolbars
    maximized: bool
    fullscreen: bool
