import logging
from typing import Optional, Dict

from PyQt6.QtCore import QObject, pyqtSignal, QSettings
from PyQt6.QtGui import QFont, QPalette, QColor
from PyQt6.QtWidgets import QApplication

from ..models.theme import Theme, ThemeMode
from ..styles.stylesheet import StylesheetGenerator
from ..styles.system import create_system_theme
from ...exceptions import ThemeError

logger = logging.getLogger(__name__)


class ThemeManager(QObject):
    """
    Manages application theming.

    Handles:
    - Theme loading and application
    - Theme persistence
    - OS theme detection and updates
    - Theme switching

    Signals:
        theme_changed: Emitted when the theme changes
        error_occurred: Emitted when a theme-related error occurs
    """

    # Signals
    theme_changed: pyqtSignal = pyqtSignal(Theme)
    error_occurred: pyqtSignal = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self._settings = QSettings()
        self._current_theme: Optional[Theme] = None
        self._cached_themes: Dict[str, Theme] = {}

        try:
            self._initialize_theme()
        except ThemeError as e:
            logger.error(f"Failed to initialize theme: {e}")
            self.error_occurred.emit(str(e))
            raise

    def _initialize_theme(self) -> None:
        """Initialize the theme system."""
        try:
            # Try to load saved theme preference
            saved_theme = self._load_saved_theme()
            if saved_theme:
                self._apply_theme(saved_theme)
            else:
                # Fall back to system theme
                system_theme = create_system_theme()
                self._apply_theme(system_theme)
        except Exception as e:
            self.error_occurred.emit(f"Error initializing theme: {str(e)}")
            # Fallback to system theme on error
            self._apply_theme(create_system_theme())

    def _load_saved_theme(self) -> Optional[Theme]:
        """Load the saved theme from settings."""
        theme_data = self._settings.value("theme/current")
        if theme_data:
            try:
                return Theme.parse_raw(theme_data)
            except Exception as e:
                self.error_occurred.emit(f"Error loading saved theme: {str(e)}")
        return None

    def _save_current_theme(self) -> None:
        """Save current theme to settings."""
        if self._current_theme:
            self._settings.setValue("theme/current", self._current_theme.json())

    def _apply_theme(self, theme: Theme) -> None:
        """Apply the theme to the application."""
        try:
            app = QApplication.instance()
            if not app:
                raise RuntimeError("No QApplication instance found")

            # Store the new theme
            self._current_theme = theme

            # Create stylesheet generator
            stylesheet_generator = StylesheetGenerator(theme)

            # Create and apply palette
            palette = QPalette()
            colors = theme.colors

            # Update palette colors
            palette.setColor(QPalette.ColorRole.Window, QColor(colors.background))
            palette.setColor(QPalette.ColorRole.WindowText, QColor(colors.text_primary))
            palette.setColor(QPalette.ColorRole.Base, QColor(colors.surface))
            palette.setColor(QPalette.ColorRole.Text, QColor(colors.text_primary))
            palette.setColor(QPalette.ColorRole.Button, QColor(colors.primary))
            palette.setColor(QPalette.ColorRole.ButtonText, QColor(colors.text_primary))
            palette.setColor(QPalette.ColorRole.Highlight, QColor(colors.primary))
            palette.setColor(
                QPalette.ColorRole.HighlightedText, QColor(colors.text_primary)
            )

            # Apply the palette
            app.setPalette(palette)

            # Apply global stylesheet
            app.setStyleSheet(stylesheet_generator.generate_global_stylesheet())

            # Apply fonts
            app.setFont(self.get_font())

            # Store generator for component-specific styles
            self._stylesheet_generator = stylesheet_generator

            # Emit theme changed signal
            self.theme_changed.emit(theme)

            # Save theme preference
            self._save_current_theme()

        except Exception as e:
            self.error_occurred.emit(f"Error applying theme: {str(e)}")

    def get_component_stylesheet(self, component_name: str) -> str:
        """Get stylesheet for a specific component."""
        if not self._current_theme or not hasattr(self, "_stylesheet_generator"):
            return ""
        return self._stylesheet_generator.generate_component_stylesheet(component_name)

    def get_current_theme(self) -> Optional[Theme]:
        """Get the currently active theme."""
        return self._current_theme

    def get_font(self, size_key: str = "base_size") -> QFont:
        """Get a font from the current theme."""
        if not self._current_theme:
            return QApplication.instance().font()

        typography = self._current_theme.typography
        size = getattr(typography, size_key, typography.base_size)
        font = QFont(typography.font_family, size)
        return font

    def get_spacing(self, key: str = "medium") -> int:
        """Get spacing value from current theme."""
        if not self._current_theme:
            return 8  # Default fallback
        return getattr(
            self._current_theme.spacing, key, self._current_theme.spacing.medium
        )

    def switch_theme(self, theme: Theme) -> None:
        """Switch to a new theme."""
        self._apply_theme(theme)

    def update_system_theme(self) -> None:
        """Update the system theme (useful when OS theme changes)."""
        if self._current_theme and self._current_theme.mode == ThemeMode.SYSTEM:
            self._apply_theme(create_system_theme())
