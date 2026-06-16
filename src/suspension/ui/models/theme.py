# src/suspension/ui/models/theme.py

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ThemeMode(str, Enum):
    """Theme mode options"""

    SYSTEM = "system"
    LIGHT = "light"
    DARK = "dark"


class ColorScheme(BaseModel):
    """
    Color scheme definition using hex color codes.
    All colors should be provided in "#RRGGBB" format.
    """

    # Base colors
    primary: str = Field(..., pattern="^#[0-9A-Fa-f]{6}$")
    secondary: str = Field(..., pattern="^#[0-9A-Fa-f]{6}$")
    background: str = Field(..., pattern="^#[0-9A-Fa-f]{6}$")
    surface: str = Field(..., pattern="^#[0-9A-Fa-f]{6}$")

    # Text colors
    text_primary: str = Field(..., pattern="^#[0-9A-Fa-f]{6}$")
    text_secondary: str = Field(..., pattern="^#[0-9A-Fa-f]{6}$")
    text_disabled: str = Field(..., pattern="^#[0-9A-Fa-f]{6}$")

    # UI element colors
    border: str = Field(..., pattern="^#[0-9A-Fa-f]{6}$")
    divider: str = Field(..., pattern="^#[0-9A-Fa-f]{6}$")

    # State colors
    error: str = Field(..., pattern="^#[0-9A-Fa-f]{6}$")
    warning: str = Field(..., pattern="^#[0-9A-Fa-f]{6}$")
    success: str = Field(..., pattern="^#[0-9A-Fa-f]{6}$")
    info: str = Field(..., pattern="^#[0-9A-Fa-f]{6}$")

    # Component specific colors
    toolbar: str = Field(..., pattern="^#[0-9A-Fa-f]{6}$")
    toolbar_text: str = Field(..., pattern="^#[0-9A-Fa-f]{6}$")
    sidebar: str = Field(..., pattern="^#[0-9A-Fa-f]{6}$")
    sidebar_text: str = Field(..., pattern="^#[0-9A-Fa-f]{6}$")


class Spacing(BaseModel):
    """Spacing units for consistent layout"""

    unit: int = 4  # Base unit for spacing calculations

    # Predefined spacings
    xxsmall: int = Field(default=2)  # 0.5x unit
    xsmall: int = Field(default=4)  # 1x unit
    small: int = Field(default=8)  # 2x unit
    medium: int = Field(default=16)  # 4x unit
    large: int = Field(default=24)  # 6x unit
    xlarge: int = Field(default=32)  # 8x unit
    xxlarge: int = Field(default=48)  # 12x unit


class Typography(BaseModel):
    """Typography definitions"""

    font_family: str
    mono_family: str  # For code/monospace text

    # Font sizes
    base_size: int = Field(default=12)

    # Heading sizes
    h1: int = Field(default=24)
    h2: int = Field(default=20)
    h3: int = Field(default=16)
    h4: int = Field(default=14)

    # Other sizes
    button: int = Field(default=12)
    caption: int = Field(default=11)
    small: int = Field(default=10)


class Shadows(BaseModel):
    """Shadow definitions for depth effects"""

    none: str = "none"
    small: str = "0 2px 4px rgba(0,0,0,0.1)"
    medium: str = "0 4px 8px rgba(0,0,0,0.1)"
    large: str = "0 8px 16px rgba(0,0,0,0.1)"


class ThemeMetadata(BaseModel):
    """Theme metadata for identification and management"""

    name: str
    description: Optional[str] = None
    version: str = "1.0.0"
    author: Optional[str] = None


class Theme(BaseModel):
    """Complete theme definition"""

    metadata: ThemeMetadata
    mode: ThemeMode
    colors: ColorScheme
    typography: Typography
    spacing: Spacing = Field(default_factory=Spacing)
    shadows: Shadows = Field(default_factory=Shadows)

    # UI element sizes
    border_radius: int = Field(default=4)
    icon_size: int = Field(default=16)

    # Animation durations (in milliseconds)
    animation_duration_fast: int = Field(default=100)
    animation_duration_normal: int = Field(default=200)
    animation_duration_slow: int = Field(default=300)

    class Config:
        arbitrary_types_allowed = True
