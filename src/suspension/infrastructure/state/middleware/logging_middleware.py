# src/suspension/infrastructure/state/middleware/logging_middleware.py
import logging
from typing import Callable

from ..store import Store
from ..types.application import ApplicationState
from ..types.common import Action

logger = logging.getLogger(__name__)


def logging_middleware(
    store: Store[ApplicationState], action: Action, next: Callable[[Action], None]
) -> None:
    """Middleware for logging actions and state changes"""

    # Log action before processing
    logger.debug(f"Dispatching action: {action.type}")
    if action.payload:
        logger.debug(f"Action payload: {action.payload}")

    # Get state before action
    state_before = store.state

    # Process the action
    next(action)

    # Get state after action
    state_after = store.state

    # Log state changes (only if different)
    if state_before != state_after:
        logger.debug("State updated after action")

        # Log specific changes if needed
        # Note: You might want to customize this based on what changes you want to track
        if state_before.ui != state_after.ui:
            logger.debug("UI state changed")
        if state_before.analysis != state_after.analysis:
            logger.debug("Analysis state changed")
        if state_before.vehicle_config != state_after.vehicle_config:
            logger.debug("Vehicle configuration changed")
        if state_before.suspension_config != state_after.suspension_config:
            logger.debug("Suspension configuration changed")
