# src/suspension/ui/managers/theme.py

"""
Theme management for the Suspension Calculator.
"""

from typing import Optional, Dict

from PyQt6.QtCore import QObject, pyqtSignal, QSettings
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QApplication

from ..constants import LIGHT_THEME, DARK_THEME
from ..models.theme import Theme, ThemeMode
from ..styles.stylesheet import StylesheetGenerator
from ..styles.system import create_system_theme, detect_system_theme_mode
from ...exceptions import ThemeError
from ...utils.logging import app_logger


class ThemeManager(QObject):
    """
    Manages application theming.

    Features:
    - Theme loading and application
    - Theme persistence
    - OS theme detection and updates
    - Theme switching
    - Preset theme management
    - Component-specific styling

    Signals:
        theme_changed: Emitted when the theme changes
        theme_mode_changed: Emitted when theme mode changes
        error_occurred: Emitted when a theme-related error occurs
    """

    # Signals
    theme_changed = pyqtSignal(Theme)
    theme_mode_changed = pyqtSignal(ThemeMode)
    error_occurred = pyqtSignal(str)

    def __init__(self) -> None:
        """Initialize the theme manager."""
        super().__init__()

        # Initialize core attributes
        self._settings = QSettings()
        self._current_theme: Optional[Theme] = None
        self._theme_mode: ThemeMode = ThemeMode.SYSTEM
        self._available_themes: Dict[str, Theme] = {}
        self._stylesheet_generator: Optional[StylesheetGenerator] = None

        # Setup logging
        self.logger = app_logger
        self._context = {"component": "ThemeManager"}

        try:
            # Register built-in themes
            self._register_built_in_themes()
            # Initialize theme system
            self._initialize_theme()

            self.logger.info(
                "Theme manager initialized",
                context={
                    **self._context,
                    "theme_mode": self._theme_mode,
                    "available_themes": list(self._available_themes.keys()),
                },
            )
        except Exception as e:
            self.logger.error(
                "Failed to initialize theme manager", error=e, context=self._context
            )
            self.error_occurred.emit(str(e))
            raise ThemeError("Failed to initialize theme manager") from e

    def _initialize_theme(self) -> None:
        """Initialize the theme system."""
        try:
            # Load theme mode preference
            saved_mode = self._settings.value("theme/mode", ThemeMode.SYSTEM.value, str)
            self._theme_mode = ThemeMode(saved_mode)

            # Try to load saved theme
            saved_theme = self._load_saved_theme()
            if saved_theme:
                self._apply_theme(saved_theme)
            else:
                # Apply theme based on mode
                self._update_current_theme()

        except Exception as e:
            self.logger.error(
                "Error initializing theme", error=e, context=self._context
            )
            self.error_occurred.emit(f"Error initializing theme: {str(e)}")
            # Fallback to system theme
            self._apply_theme(create_system_theme())

    def register_theme(self, theme: Theme) -> None:
        """
        Register a new theme.

        Args:
            theme: Theme to register
        """
        try:
            self._available_themes[theme.metadata.name] = theme
            self.logger.debug(
                f"Registered theme: {theme.metadata.name}",
                context={**self._context, "theme": theme.metadata.dict()},
            )
        except Exception as e:
            self.logger.error(
                "Failed to register theme",
                error=e,
                context={**self._context, "theme": theme.metadata.dict()},
            )
            raise ThemeError(f"Failed to register theme: {theme.metadata.name}") from e

    def _load_saved_theme(self) -> Optional[Theme]:
        """Load the saved theme from settings."""
        theme_data = self._settings.value("theme/current")
        if theme_data:
            try:
                return Theme.parse_raw(theme_data)
            except Exception as e:
                self.logger.error(
                    "Error loading saved theme", error=e, context=self._context
                )
                self.error_occurred.emit(f"Error loading saved theme: {str(e)}")
        return None

    def _apply_theme(self, theme: Theme) -> None:
        """Apply the theme to the application."""
        try:
            app = QApplication.instance()
            if not app:
                raise RuntimeError("No QApplication instance found")

            # Store the new theme
            self._current_theme = theme

            # Create stylesheet generator
            self._stylesheet_generator = StylesheetGenerator(theme)

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
            app.setStyleSheet(self._stylesheet_generator.generate_global_stylesheet())

            # Emit theme changed signal
            self.theme_changed.emit(theme)

            # Save theme preference
            self._save_current_theme()

            self.logger.info(
                f"Applied theme: {theme.metadata.name}",
                context={
                    **self._context,
                    "theme": theme.metadata.dict(),
                    "mode": self._theme_mode,
                },
            )

        except Exception as e:
            self.logger.error(
                "Error applying theme",
                error=e,
                context={**self._context, "theme": theme.metadata.dict()},
            )
            self.error_occurred.emit(f"Error applying theme: {str(e)}")

    def _update_current_theme(self) -> None:
        """Update the current theme based on theme mode."""
        try:
            if self._theme_mode == ThemeMode.SYSTEM:
                # Detect system theme mode
                detected_mode = detect_system_theme_mode()
                theme_name = "Light" if detected_mode == ThemeMode.LIGHT else "Dark"
            else:
                theme_name = self._theme_mode.capitalize()

            new_theme = self._available_themes[theme_name]
            self._apply_theme(new_theme)

        except Exception as e:
            self.logger.error(
                "Failed to update current theme", error=e, context=self._context
            )
            raise ThemeError("Failed to update current theme") from e

    def _save_current_theme(self) -> None:
        """Save current theme to settings."""
        if self._current_theme:
            self._settings.setValue("theme/current", self._current_theme.json())
            self._settings.setValue("theme/mode", self._theme_mode.value)

    def _register_built_in_themes(self) -> None:
        """Register the built-in theme presets."""
        # Register light and dark themes
        self.register_theme(LIGHT_THEME)
        self.register_theme(DARK_THEME)
        # Register system theme
        self.register_theme(create_system_theme())
