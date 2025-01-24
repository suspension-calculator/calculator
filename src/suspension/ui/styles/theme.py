# src/suspension/ui/styles/theme.py

from dataclasses import dataclass

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QApplication


def blend_colors(color1: QColor, color2: QColor, ratio: float = 0.5) -> QColor:
    """Blend two colors with a given ratio."""
    return QColor(
        int(color1.red() * (1 - ratio) + color2.red() * ratio),
        int(color1.green() * (1 - ratio) + color2.green() * ratio),
        int(color1.blue() * (1 - ratio) + color2.blue() * ratio),
        int(color1.alpha() * (1 - ratio) + color2.alpha() * ratio),
    )


class SystemPalette:
    """Wrapper for system palette colors with convenient access methods."""

    def __init__(self):
        self.palette = QApplication.instance().palette()

    def color(self, role: QPalette.ColorRole) -> QColor:
        return self.palette.color(role)

    @property
    def window(self) -> QColor:
        return self.color(QPalette.ColorRole.Window)

    @property
    def window_text(self) -> QColor:
        return self.color(QPalette.ColorRole.WindowText)

    @property
    def base(self) -> QColor:
        return self.color(QPalette.ColorRole.Base)

    @property
    def alternate_base(self) -> QColor:
        return self.color(QPalette.ColorRole.AlternateBase)

    @property
    def highlight(self) -> QColor:
        return self.color(QPalette.ColorRole.Highlight)

    @property
    def highlighted_text(self) -> QColor:
        return self.color(QPalette.ColorRole.HighlightedText)


@dataclass
class ThemeColors:
    """Container for theme-specific colors."""

    # Main colors
    background: QColor
    foreground: QColor
    accent: QColor

    # UI element colors
    surface: QColor
    surface_alt: QColor

    # Interactive elements
    hover: QColor
    pressed: QColor
    selected: QColor

    # Text colors
    text: QColor
    text_dimmed: QColor
    text_accent: QColor

    @classmethod
    def from_system_palette(cls, system: SystemPalette) -> "ThemeColors":
        """Create theme colors from system palette."""
        return cls(
            background=system.window,
            foreground=system.window_text,
            accent=system.highlight,
            surface=blend_colors(system.window, system.base, 0.5),
            surface_alt=system.alternate_base,
            hover=blend_colors(system.window, system.highlight, 0.1),
            pressed=blend_colors(system.window, system.highlight, 0.2),
            selected=blend_colors(system.window, system.highlight, 0.15),
            text=system.window_text,
            text_dimmed=blend_colors(system.window_text, system.window, 0.4),
            text_accent=system.highlighted_text,
        )


class Theme:
    """
    Enhanced theme system that provides consistent styling across the application.
    """

    def __init__(self):
        self._system = SystemPalette()
        self._colors = ThemeColors.from_system_palette(self._system)

    @property
    def colors(self) -> ThemeColors:
        return self._colors

    def navigation_item_style(self) -> str:
        return f"""
            QWidget#NavigationItem {{
                background: transparent;
            }}

            QLabel#NavigationLabel {{
                color: {self._colors.text.name()};
                padding: 4px;
                border-radius: 4px;
            }}

            QLabel#NavigationLabel:hover {{
                background-color: {self._colors.hover.name()};
            }}

            QWidget#NavigationSpacer {{
                background: transparent;
            }}
        """

    def dock_widget_style(self) -> str:
        """Generate stylesheet for dock widgets."""
        return f"""
            QDockWidget {{
                border: none;
                padding: 0px;
                margin: 0px;
                background: transparent;
            }}
        """

    def navigation_header_style(self) -> str:
        """Generate stylesheet for NavigationHeader component."""
        return f"""
            QWidget {{
                background-color: {self._colors.surface.name()};
            }}

            QLabel {{
                color: {self._colors.text.name()};
                font-weight: bold;
            }}
        """

    def navigation_tree_style(self) -> str:
        return f"""
            QTreeWidget {{
                border: none;
                background-color: {self._colors.surface.name()};
                show-decoration-selected: 0;
            }}

            QTreeWidget::item {{
                padding: 4px;
                border-radius: 4px;
                color: {self._colors.text.name()};
                height: 24px;  /* Ensure enough vertical space */
                margin: 2px 0;  /* Add some vertical separation */
            }}

            QTreeWidget::item:hover {{
                color: {self._colors.hover.name()};
                cursor: pointer;
            }}

            QTreeWidget::item:selected {{
                color: {self._colors.accent.name()};
                background: transparent;
            }}

            QTreeWidget::branch {{
                background: transparent;
                border: none;
                width: 0;
                padding: 0;
                margin: 0;
                min-width: 0;
                max-width: 0;
                image: none;
            }}
        """

    @classmethod
    def current(cls) -> "Theme":
        """Get or create the current theme instance."""
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def navigation_strip_style(self) -> str:
        """Generate stylesheet for NavigationStrip component."""
        return f"""
            NavigationStrip {{
                background-color: {self._colors.surface.name()};
                border: none;
                border-right: 1px solid {self._colors.surface_alt.name()};
            }}

            QPushButton {{
                border: none;
                border-radius: 4px;
                padding: 4px;
                margin: 2px;
                background: transparent;
            }}

            QPushButton:hover {{
                background-color: {self._colors.hover.name()};
            }}

            QPushButton:checked {{
                background-color: {self._colors.selected.name()};
            }}
        """
