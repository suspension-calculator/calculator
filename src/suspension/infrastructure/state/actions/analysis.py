# src/suspension/infrastructure/state/actions/analysis.py
from dataclasses import dataclass
from enum import Enum

from suspension.core.domain import SuspensionResults


class AnalysisActionType(Enum):
    UPDATE_ANALYSIS_RESULTS = "UPDATE_ANALYSIS_RESULTS"
    START_ANALYSIS = "START_ANALYSIS"
    ANALYSIS_COMPLETE = "ANALYSIS_COMPLETE"
    ANALYSIS_ERROR = "ANALYSIS_ERROR"


@dataclass
class UpdateAnalysisResultsAction:
    """Action to update analysis results"""

    results: SuspensionResults
    type: AnalysisActionType = AnalysisActionType.UPDATE_ANALYSIS_RESULTS


@dataclass
class StartAnalysisAction:
    """Action to start analysis"""

    type: AnalysisActionType = AnalysisActionType.START_ANALYSIS


@dataclass
class AnalysisCompleteAction:
    """Action for completed analysis"""

    results: SuspensionResults
    type: AnalysisActionType = AnalysisActionType.ANALYSIS_COMPLETE


@dataclass
class AnalysisErrorAction:
    """Action for analysis error"""

    error: str
    type: AnalysisActionType = AnalysisActionType.ANALYSIS_ERROR


# Action creators
def update_analysis_results(results: SuspensionResults) -> UpdateAnalysisResultsAction:
    """Create an action to update analysis results"""
    return UpdateAnalysisResultsAction(results=results)


def start_analysis() -> StartAnalysisAction:
    """Create an action to start analysis"""
    return StartAnalysisAction()


def analysis_complete(results: SuspensionResults) -> AnalysisCompleteAction:
    """Create an action for completed analysis"""
    return AnalysisCompleteAction(results=results)


def analysis_error(error: str) -> AnalysisErrorAction:
    """Create an action for analysis error"""
    return AnalysisErrorAction(error=error)
