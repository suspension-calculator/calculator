# src/suspension/infrastructure/state/selectors/analysis.py
from typing import Optional

from suspension.core.domain import SuspensionResults
from ..types.application import ApplicationState


def select_analysis_results(state: ApplicationState) -> Optional[SuspensionResults]:
    """Select analysis results from state"""
    return state.analysis.results


def select_analysis_status(state: ApplicationState) -> bool:
    """Select whether analysis is currently running"""
    return state.analysis.is_running


def select_analysis_error(state: ApplicationState) -> Optional[str]:
    """Select any analysis error message"""
    return state.analysis.error


def select_analysis_progress(state: ApplicationState) -> float:
    """Select current analysis progress"""
    return state.analysis.progress
