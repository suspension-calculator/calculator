# src/suspension/infrastructure/state/actions/__init__.py
from .analysis import (
    AnalysisActionType,
    UpdateAnalysisResultsAction,
    StartAnalysisAction,
    AnalysisCompleteAction,
    AnalysisErrorAction,
    update_analysis_results,
    start_analysis,
    analysis_complete,
    analysis_error,
)
from .navigation import (
    NavigationActionType,
    SelectItemAction,
    SetActiveItemAction,
    ToggleExpandedAction,
    SetNavVisibleAction,
    UpdatePageAction,
    select_item,
    set_active_item,
    toggle_expanded,
    set_nav_visible,
    update_page,
)

__all__ = [
    # Navigation actions
    "NavigationActionType",
    "SelectItemAction",
    "SetActiveItemAction",
    "ToggleExpandedAction",
    "SetNavVisibleAction",
    "UpdatePageAction",
    "select_item",
    "set_active_item",
    "toggle_expanded",
    "set_nav_visible",
    "update_page",
    # Analysis actions
    "AnalysisActionType",
    "UpdateAnalysisResultsAction",
    "StartAnalysisAction",
    "AnalysisCompleteAction",
    "AnalysisErrorAction",
    "update_analysis_results",
    "start_analysis",
    "analysis_complete",
    "analysis_error",
]
