# src/suspension/state/persistence/persistence.py

import logging
from pathlib import Path
from typing import Optional, Type, TypeVar

from pydantic import BaseModel

from .exceptions import PersistenceError, FileFormatError
from .formats import FormatAdapter, JsonFormat, LegacyCSVFormat

logger = logging.getLogger(__name__)
T = TypeVar("T", bound=BaseModel)


class PersistenceManager:
    """Manages persistence operations for application state"""

    def __init__(self):
        self.format_handlers: list[FormatAdapter] = [
            JsonFormat(),  # Primary format
            LegacyCSVFormat(),  # Legacy format support
        ]
        self._default_extension = ".json"

    def save(self, data: BaseModel, file_path: Optional[Path] = None) -> Path:
        """Save application state to file"""
        if file_path is None:
            file_path = self._get_default_path()

        # Ensure the directory exists
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Default to JSON format for saving
        try:
            self.format_handlers[0].write(file_path, data)
            logger.info(f"Successfully saved state to {file_path}")
            return file_path
        except Exception as e:
            raise PersistenceError(f"Failed to save state: {str(e)}") from e

    def load(self, model_type: Type[T], file_path: Optional[Path] = None) -> T:
        """Load application state from file"""
        if file_path is None:
            file_path = self._get_default_path()

        if not file_path.exists():
            raise FileFormatError(f"File not found: {file_path}")

        # Try each format handler until one works
        last_error = None
        for handler in self.format_handlers:
            try:
                if handler.can_read(file_path):
                    return handler.read(file_path, model_type)
            except Exception as e:
                last_error = e
                continue

        raise PersistenceError(
            f"Failed to load state from {file_path}: {str(last_error)}"
        )

    def _get_default_path(self) -> Path:
        """Get the default file path for state persistence"""
        # You might want to customize this based on your needs
        return (
            Path.home() / ".suspension_calculator" / f"state{self._default_extension}"
        )
