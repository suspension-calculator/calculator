# src/suspension/infrastructure/state/types/common.py
import time
from enum import Enum
from typing import Any, Dict, Generic, TypeVar, Optional, Callable

from pydantic import BaseModel, Field, ConfigDict

# Remove the ApplicationState import and use TypeVar instead
StateT = TypeVar("StateT")
PayloadT = TypeVar("PayloadT")


class ActionType(str, Enum):
    """Base action types common across the application"""

    # Application State
    LOAD_STATE = "LOAD_STATE"
    SAVE_STATE = "SAVE_STATE"
    INITIALIZE = "INITIALIZE"
    RESET = "RESET"

    # Geometry Actions
    UPDATE_SUSPENSION_CONFIG = "UPDATE_SUSPENSION_CONFIG"
    UPDATE_VEHICLE_CONFIG = "UPDATE_VEHICLE_CONFIG"
    UPDATE_LINK_POSITION = "UPDATE_LINK_POSITION"

    # Analysis Actions
    UPDATE_ANALYSIS_RESULTS = "UPDATE_ANALYSIS_RESULTS"
    START_ANALYSIS = "START_ANALYSIS"
    ANALYSIS_COMPLETE = "ANALYSIS_COMPLETE"
    ANALYSIS_ERROR = "ANALYSIS_ERROR"

    # UI State Actions
    UPDATE_PAGE = "UPDATE_PAGE"
    UPDATE_PLOT = "UPDATE_PLOT"
    UPDATE_INPUT_VALUES = "UPDATE_INPUT_VALUES"
    UPDATE_NAV_VISIBILITY = "UPDATE_NAV_VISIBILITY"

    # Navigation Actions
    SELECT_ITEM = "SELECT_ITEM"
    SET_ACTIVE_ITEM = "SET_ACTIVE_ITEM"
    TOGGLE_EXPANDED = "TOGGLE_EXPANDED"
    SET_NAV_VISIBLE = "SET_NAV_VISIBLE"


class Action(BaseModel, Generic[PayloadT]):
    """Type-safe action with generic payload"""

    type: ActionType
    payload: Optional[PayloadT] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    timestamp: float = Field(default_factory=time.time)

    model_config = ConfigDict(arbitrary_types_allowed=True)


# Use StateT instead of ApplicationState
ActionHandler = Callable[[StateT, Action], StateT]
Middleware = Callable[["Store[StateT]", Action, Callable], None]
Selector = Callable[[StateT], Any]
