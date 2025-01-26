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


def get_system_colors() -> ColorScheme:
    """Get colors from system palette"""
    app = QApplication.instance()
    palette = app.palette()

    return ColorScheme(
        primary=palette.button().color().name(),
        secondary=palette.highlight().color().name(),
        background=palette.window().color().name(),
        surface=palette.base().color().name(),
        error="#FF0000",  # Customize as needed
        text_primary=palette.windowText().color().name(),
        text_secondary=palette.text().color().name(),
    )


def get_system_font() -> Typography:
    """Get system font settings"""
    app = QApplication.instance()
    default_font = app.font()

    return Typography(
        font_family=default_font.family(),
        base_size=default_font.pointSize(),
        heading_1=default_font.pointSize() + 4,
        heading_2=default_font.pointSize() + 2,
        body=default_font.pointSize(),
    )


def create_system_theme() -> Theme:
    """
    Creates a theme that matches the current system settings.
    Uses Qt's palette to detect system colors.
    """
    # Get the application instance to access system palette
    app = QApplication.instance()
    if not app:
        raise RuntimeError("QApplication must be created before creating system theme")

    palette = app.palette()
    system_font = app.font()

    # Create theme using system colors
    return Theme(
        metadata=ThemeMetadata(
            name="System Default", description="Automatically matches system appearance"
        ),
        mode=ThemeMode.SYSTEM,
        colors=ColorScheme(
            # Base colors - derived from system palette
            primary=palette.color(QPalette.ColorRole.Highlight).name(),
            secondary=palette.color(QPalette.ColorRole.Highlight).lighter(110).name(),
            background=palette.color(QPalette.ColorRole.Window).name(),
            surface=palette.color(QPalette.ColorRole.Base).name(),
            # Text colors
            text_primary=palette.color(QPalette.ColorRole.WindowText).name(),
            text_secondary=palette.color(QPalette.ColorRole.Text).name(),
            text_disabled=palette.color(
                QPalette.ColorRole.Disabled, QPalette.ColorRole.Text
            ).name(),
            # UI colors
            border=palette.color(QPalette.ColorRole.Mid).name(),
            divider=palette.color(QPalette.ColorRole.Mid).name(),
            # State colors
            error="#DC3545",
            warning="#FFC107",
            success="#28A745",
            info="#17A2B8",
            # Component colors
            toolbar=palette.color(QPalette.ColorRole.Window).name(),
            toolbar_text=palette.color(QPalette.ColorRole.WindowText).name(),
            sidebar=palette.color(QPalette.ColorRole.Window).name(),
            sidebar_text=palette.color(QPalette.ColorRole.WindowText).name(),
        ),
        typography=Typography(
            font_family=system_font.family(),
            mono_family="Consolas" if system_font.family() == "Segoe UI" else "Menlo",
            base_size=system_font.pointSize(),
        ),
    )
