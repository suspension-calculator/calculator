# src/suspension/ui/styles/system.py

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette
from ..models.theme import (
    Theme,
    ThemeMode,
    ColorScheme,
    Typography,
    ThemeMetadata,
)


from ..models.theme import (
    Spacing,
    Shadows,
)


def get_system_colors() -> ColorScheme:
    """Get colors from system palette"""
    app = QApplication.instance()
    if not app:
        raise RuntimeError("QApplication must be created before getting system colors")

    palette = app.palette()

    return ColorScheme(
        # Base colors
        primary=palette.button().color().name(),
        secondary=palette.highlight().color().name(),
        background=palette.window().color().name(),
        surface=palette.base().color().name(),
        # Text colors
        text_primary=palette.windowText().color().name(),
        text_secondary=palette.text().color().name(),
        text_disabled=palette.color(
            QPalette.ColorRole.Disabled, QPalette.ColorRole.Text
        ).name(),
        # UI element colors
        border=palette.mid().color().name(),
        divider=palette.mid().color().name(),
        # State colors
        error="#DC3545",  # Bootstrap-style error red
        warning="#FFC107",  # Bootstrap-style warning yellow
        success="#28A745",  # Bootstrap-style success green
        info="#17A2B8",  # Bootstrap-style info blue
        # Component specific colors
        toolbar=palette.window().color().name(),
        toolbar_text=palette.windowText().color().name(),
        sidebar=palette.window().color().name(),
        sidebar_text=palette.windowText().color().name(),
    )


def get_system_font() -> Typography:
    """Get system font settings"""
    app = QApplication.instance()
    if not app:
        raise RuntimeError("QApplication must be created before getting system font")

    default_font = app.font()
    base_size = default_font.pointSize()

    return Typography(
        font_family=default_font.family(),
        mono_family="Consolas" if default_font.family() == "Segoe UI" else "Menlo",
        base_size=base_size,
        h1=base_size + 12,  # 24px if base is 12
        h2=base_size + 8,  # 20px if base is 12
        h3=base_size + 4,  # 16px if base is 12
        h4=base_size + 2,  # 14px if base is 12
        button=base_size,
        caption=base_size - 1,
        small=base_size - 2,
    )


def create_system_theme() -> Theme:
    """
    Creates a theme that matches the current system settings.
    Uses Qt's palette to detect system colors and font settings.
    """
    app = QApplication.instance()
    if not app:
        raise RuntimeError("QApplication must be created before creating system theme")

    return Theme(
        metadata=ThemeMetadata(
            name="System Default",
            description="Automatically matches system appearance",
            version="1.0.0",
        ),
        mode=ThemeMode.SYSTEM,
        colors=get_system_colors(),
        typography=get_system_font(),
        spacing=Spacing(),  # Use default spacing
        shadows=Shadows(),  # Use default shadows
        border_radius=4,
        icon_size=16,
        animation_duration_fast=100,
        animation_duration_normal=200,
        animation_duration_slow=300,
    )


def detect_system_theme_mode() -> ThemeMode:
    """
    Detect if the system is using light or dark mode.
    Returns ThemeMode.SYSTEM if unable to detect.
    """
    app = QApplication.instance()
    if not app:
        return ThemeMode.SYSTEM

    palette = app.palette()
    background = palette.color(QPalette.ColorRole.Window)

    # Calculate perceived brightness
    brightness = (
        background.red() * 299 + background.green() * 587 + background.blue() * 114
    ) / 1000

    if brightness < 128:
        return ThemeMode.DARK
    return ThemeMode.LIGHT
