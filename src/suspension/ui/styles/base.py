# src/suspension/ui/styles/base.py
from pydantic import BaseModel
from PyQt6.QtGui import QColor, QFont


class ColorScheme(BaseModel):
    """Base color scheme definition"""

    primary: str
    secondary: str
    background: str
    surface: str
    error: str
    text_primary: str
    text_secondary: str

    def to_qcolor(self, color_str: str) -> QColor:
        return QColor(color_str)


class Typography(BaseModel):
    """Typography definitions"""

    font_family: str
    base_size: int
    heading_1: int
    heading_2: int
    body: int

    def get_font(self, size: int) -> QFont:
        font = QFont(self.font_family, size)
        return font


class Spacing(BaseModel):
    """Layout spacing definitions"""

    unit: int = 8
    small: int = 4
    medium: int = 8
    large: int = 16


class BaseTheme(BaseModel):
    """Base theme with all required properties"""

    colors: ColorScheme
    typography: Typography
    spacing: Spacing
    border_radius: int = 4

    class Config:
        arbitrary_types_allowed = True
