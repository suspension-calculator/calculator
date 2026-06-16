# src/suspension/ui/styles/base.py
"""Base theme components with Qt integration."""

from pydantic import BaseModel, Field
from PyQt6.QtGui import QColor, QFont
from typing import Optional


class ColorScheme(BaseModel):
    """Color scheme definition using hex color codes."""

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

    def to_qcolor(self, color_str: str) -> QColor:
        """Convert a hex color string to QColor."""
        return QColor(color_str)


class Typography(BaseModel):
    """Typography definitions with Qt integration."""

    font_family: str
    mono_family: str
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

    def get_font(self, size: Optional[int] = None, is_mono: bool = False) -> QFont:
        """Get a QFont with the specified size."""
        family = self.mono_family if is_mono else self.font_family
        return QFont(family, size or self.base_size)


class Spacing(BaseModel):
    """Spacing units for consistent layout."""

    unit: int = Field(default=4)
    xxsmall: int = Field(default=2)
    xsmall: int = Field(default=4)
    small: int = Field(default=8)
    medium: int = Field(default=16)
    large: int = Field(default=24)
    xlarge: int = Field(default=32)
    xxlarge: int = Field(default=48)


class Shadows(BaseModel):
    """Shadow definitions for depth effects."""

    none: str = "none"
    small: str = "0 2px 4px rgba(0,0,0,0.1)"
    medium: str = "0 4px 8px rgba(0,0,0,0.1)"
    large: str = "0 8px 16px rgba(0,0,0,0.1)"


class BaseTheme(BaseModel):
    """Base theme with Qt integration capabilities."""

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
