"""
Logging system for the Suspension Calculator application.
Provides structured logging with contextual information and error tracking.
"""

import logging
import sys
import platform
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any
import json
from dataclasses import dataclass, asdict
import traceback

from ..constants import LogLevel, APP_NAME, DEFAULT_CONFIG_PATH
from ..types import JsonDict, PathLike


@dataclass
class SystemInfo:
    """System information captured for debugging."""

    python_version: str
    platform_system: str
    platform_release: str
    platform_version: str
    platform_machine: str
    timestamp: str

    @classmethod
    def capture_current(cls) -> "SystemInfo":
        """Capture current system information."""
        return cls(
            python_version=sys.version,
            platform_system=platform.system(),
            platform_release=platform.release(),
            platform_version=platform.version(),
            platform_machine=platform.machine(),
            timestamp=datetime.now().isoformat(),
        )


class StructuredLogger:
    """
    Structured logger that provides context-aware logging with system information.

    Features:
    - Timestamps for all logs
    - System information capture
    - JSON-formatted logs for easy parsing
    - Error stack traces
    - Log rotation
    """

    def __init__(
        self,
        name: str,
        log_dir: Optional[PathLike] = None,
        level: LogLevel = LogLevel.INFO,
        max_logs: int = 5,
    ) -> None:
        """
        Initialize the logger.

        Args:
            name: Logger name
            log_dir: Directory for log files
            level: Minimum log level
            max_logs: Maximum number of log files to keep
        """
        self.name = name
        self.log_dir = Path(log_dir or DEFAULT_CONFIG_PATH / "logs")
        self.log_dir.mkdir(parents=True, exist_ok=True)

        # Create logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level.value)

        # Setup handlers
        self._setup_handlers()

        # Capture initial system info
        self.system_info = SystemInfo.capture_current()

        # Rotate logs
        self._rotate_logs(max_logs)

    def _setup_handlers(self) -> None:
        """Setup file and console handlers."""
        # File handler
        log_file = (
            self.log_dir / f"{self.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        )
        self.logger.addHandler(file_handler)

        # Console handler for development
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
        self.logger.addHandler(console_handler)

    def _rotate_logs(self, max_logs: int) -> None:
        """Rotate log files keeping only the most recent ones."""
        log_files = sorted(self.log_dir.glob(f"{self.name}_*.log"))
        while len(log_files) > max_logs:
            log_files[0].unlink()
            log_files = log_files[1:]

    def _format_message(
        self, message: str, context: Optional[Dict[str, Any]] = None
    ) -> str:
        """Format message with context as JSON."""
        log_data = {
            "message": message,
            "context": context or {},
            "system_info": asdict(self.system_info),
        }
        return json.dumps(log_data)

    def debug(self, message: str, context: Optional[JsonDict] = None) -> None:
        """Log debug message."""
        self.logger.debug(self._format_message(message, context))

    def info(self, message: str, context: Optional[JsonDict] = None) -> None:
        """Log info message."""
        self.logger.info(self._format_message(message, context))

    def warning(self, message: str, context: Optional[JsonDict] = None) -> None:
        """Log warning message."""
        self.logger.warning(self._format_message(message, context))

    def error(
        self,
        message: str,
        error: Optional[Exception] = None,
        context: Optional[JsonDict] = None,
    ) -> None:
        """
        Log error message with optional exception info.

        Args:
            message: Error message
            error: Optional exception object
            context: Optional context dictionary
        """
        error_context = context or {}
        if error:
            error_context.update(
                {
                    "error_type": type(error).__name__,
                    "error_message": str(error),
                    "stacktrace": traceback.format_exc(),
                }
            )
        self.logger.error(self._format_message(message, error_context))


# Create default application logger
app_logger = StructuredLogger(APP_NAME)
