# src/suspension/infrastructure/state/middleware/validation_middleware.py
import logging
from typing import Callable, Dict, Any

from pydantic import ValidationError

from ..store import Store, StateError
from ..types.application import ApplicationState
from ..types.common import Action, ActionType

logger = logging.getLogger(__name__)


def validate_vehicle_config(config: Dict[str, Any]) -> None:
    """Validate vehicle configuration specific rules"""
    if config.get("mass", 0) <= 0:
        raise ValueError("Vehicle mass must be positive")
    if config.get("wheelbase", 0) <= 0:
        raise ValueError("Wheelbase must be positive")
    # Add more vehicle-specific validations as needed


def validate_suspension_config(config: Dict[str, Any]) -> None:
    """Validate suspension configuration specific rules"""
    if config.get("track_width", 0) <= 0:
        raise ValueError("Track width must be positive")
    # Add more suspension-specific validations as needed


def validation_middleware(
    store: Store[ApplicationState], action: Action, next: Callable[[Action], None]
) -> None:
    """
    Middleware for validating state changes and action payloads

    Validates:
    1. Action payload structure
    2. Domain-specific rules
    3. State consistency after action
    """

    try:
        # Pre-action validation
        if action.payload:
            # Validate action-specific payloads
            match action.type:
                case ActionType.UPDATE_VEHICLE_CONFIG:
                    validate_vehicle_config(action.payload)

                case ActionType.UPDATE_SUSPENSION_CONFIG:
                    validate_suspension_config(action.payload)

                case ActionType.UPDATE_ANALYSIS_RESULTS:
                    if "progress" in action.payload:
                        progress = action.payload["progress"]
                        if not 0 <= progress <= 1:
                            raise ValueError("Progress must be between 0 and 1")

                case ActionType.UPDATE_INPUT_VALUES:
                    # Validate numeric inputs are within reasonable ranges
                    for key, value in action.payload.items():
                        if not isinstance(value, (int, float)):
                            raise ValueError(f"Input {key} must be numeric")
                        if abs(value) > 1e6:  # Example reasonable limit
                            raise ValueError(f"Input {key} is outside reasonable range")

        # Process the action
        next(action)

        # Post-action validation
        new_state = store.state

        # Validate state consistency
        if new_state.vehicle_config and new_state.suspension_config:
            # Example: Validate wheelbase consistency
            if new_state.vehicle_config.wheelbase <= 0:
                raise StateError("Invalid wheelbase in vehicle configuration")

            # Example: Validate track width consistency
            if new_state.suspension_config.track_width <= 0:
                raise StateError("Invalid track width in suspension configuration")

        # Validate UI state
        if new_state.ui.current_page not in new_state.ui.tab_states:
            raise StateError("Current tab not found in tab states")

        # Validate analysis state
        if new_state.analysis.is_running:
            if new_state.analysis.progress < 0 or new_state.analysis.progress > 1:
                raise StateError("Analysis progress out of valid range")

        logger.debug(f"State validation passed for action: {action.type}")

    except ValidationError as e:
        logger.error(f"Validation error for action {action.type}: {str(e)}")
        # Convert Pydantic validation error to user-friendly format
        error_messages = []
        for error in e.errors():
            field = ".".join(str(x) for x in error["loc"])
            message = error["msg"]
            error_messages.append(f"{field}: {message}")

        store.dispatch(
            Action(
                type=ActionType.ANALYSIS_ERROR,
                payload={"error": "Validation failed", "details": error_messages},
            )
        )
        raise StateError(f"Validation failed: {error_messages}")

    except ValueError as e:
        logger.error(f"Value error for action {action.type}: {str(e)}")
        store.dispatch(
            Action(type=ActionType.ANALYSIS_ERROR, payload={"error": str(e)})
        )
        raise StateError(f"Invalid value: {str(e)}")

    except StateError as e:
        logger.error(f"State error for action {action.type}: {str(e)}")
        store.dispatch(
            Action(type=ActionType.ANALYSIS_ERROR, payload={"error": str(e)})
        )
        raise

    except Exception as e:
        logger.error(f"Unexpected error during validation: {str(e)}")
        store.dispatch(
            Action(
                type=ActionType.ANALYSIS_ERROR,
                payload={"error": "Unexpected validation error", "details": str(e)},
            )
        )
        raise StateError(f"Unexpected validation error: {str(e)}")
