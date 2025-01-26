# src/suspension/types.py
from typing import TypeVar, Dict, Any, Union
from pathlib import Path
from PyQt6.QtGui import QColor

PathLike = Union[str, Path]
ColorValue = Union[str, QColor]
JsonDict = Dict[str, Any]

T = TypeVar("T")  # Generic type for type-safe functions
