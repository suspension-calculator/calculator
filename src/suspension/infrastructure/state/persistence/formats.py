# src/suspension/state/persistence/formats.py

import json
import logging
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Type, TypeVar

from pydantic import BaseModel

from .exceptions import SerializationError

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)


class FormatAdapter(ABC):
    """Abstract base class for file format adapters"""

    @abstractmethod
    def can_read(self, file_path: Path) -> bool:
        """Check if the file can be read by this adapter"""
        pass

    @abstractmethod
    def read(self, file_path: Path, model_type: Type[T]) -> T:
        """Read and parse the file into the specified model type"""
        pass

    @abstractmethod
    def write(self, file_path: Path, data: BaseModel) -> None:
        """Write the model data to file"""
        pass


class JsonFormat(FormatAdapter):
    """Handler for JSON format (primary format)"""

    def can_read(self, file_path: Path) -> bool:
        if not file_path.exists():
            return False
        try:
            with file_path.open("r") as f:
                data = json.load(f)
                return isinstance(data, dict) and "version" in data
        except json.JSONDecodeError:
            return False
        except Exception:
            return False

    def read(self, file_path: Path, model_type: Type[T]) -> T:
        try:
            with file_path.open("r") as f:
                data = json.load(f)
            return model_type.model_validate(data)
        except json.JSONDecodeError as e:
            raise SerializationError(f"Invalid JSON format: {str(e)}")
        except Exception as e:
            raise SerializationError(f"Error reading JSON file: {str(e)}")

    def write(self, file_path: Path, data: BaseModel) -> None:
        try:
            # Add metadata before saving
            data_dict = data.model_dump()
            data_dict["_metadata"] = {
                "saved_at": datetime.now().isoformat(),
                "format_version": "1.0",
            }

            with file_path.open("w") as f:
                json.dump(data_dict, f, indent=2)
        except Exception as e:
            raise SerializationError(f"Error writing JSON file: {str(e)}")


class LegacyCSVFormat(FormatAdapter):
    """Handler for legacy CSV format (read-only)"""

    def can_read(self, file_path: Path) -> bool:
        if not file_path.exists():
            return False
        try:
            with file_path.open("r") as f:
                first_line = f.readline().strip()
                return first_line.startswith("units,")
        except Exception:
            return False

    def read(self, file_path: Path, model_type: Type[T]) -> T:
        from suspension.io.load_suspension import load_susp  # Lazy import

        try:
            # Use existing load function but capture its output
            # This will need to be adapted based on how load_susp works
            result = load_susp()  # You'll need to modify load_susp to return data

            # Convert the loaded data to the new format
            converted_data = self._convert_legacy_data(result)
            return model_type.model_validate(converted_data)
        except Exception as e:
            raise SerializationError(f"Error reading legacy CSV file: {str(e)}")

    def write(self, file_path: Path, data: BaseModel) -> None:
        raise NotImplementedError("Legacy CSV format is read-only")

    def _convert_legacy_data(self, legacy_data: Dict[str, Any]) -> Dict[str, Any]:
        """Convert legacy data format to new format"""
        # Implementation will depend on the specific data structures
        # This is a placeholder for the conversion logic
        return {
            "version": "1.0",
            "converted_from_legacy": True,
            # ... convert other fields
        }
