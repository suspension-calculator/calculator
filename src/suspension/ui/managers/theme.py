# src/suspension/ui/managers/theme.py

"""
Theme management for the Suspension Calculator.
"""
import sys
from typing import Dict, Optional, cast

from PyQt6.QtCore import QObject, QSettings, QTimer, pyqtSignal
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QApplication

from ...exceptions import ThemeError
from ...utils.logging import app_logger
from ..constants import DARK_THEME, LIGHT_THEME
from ..models.theme import Theme, ThemeMode
from ..styles.stylesheet import StylesheetGenerator
from ..styles.system import create_system_theme, detect_system_theme_mode


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
    - System theme change monitoring

    Signals:
        theme_changed: Emitted when the theme changes
        theme_mode_changed: Emitted when theme mode changes
        error_occurred: Emitted when a theme-related error occurs
        system_theme_changed: Emitted when the OS theme changes
    """

    # Signals
    theme_changed = pyqtSignal(Theme)
    theme_mode_changed = pyqtSignal(ThemeMode)
    error_occurred = pyqtSignal(str)
    system_theme_changed = pyqtSignal()

    def __init__(self) -> None:
        """Initialize the theme manager."""
        super().__init__()

        # Initialize core attributes
        self._settings = QSettings()
        self._current_theme: Optional[Theme] = None
        self._theme_mode: ThemeMode = ThemeMode.SYSTEM
        self._available_themes: Dict[str, Theme] = {}
        self._stylesheet_generator: Optional[StylesheetGenerator] = None
        self._system_theme_timer: Optional[QTimer] = None
        self._last_known_system_mode: Optional[ThemeMode] = None

        # Setup logging
        self.logger = app_logger
        self._context = {"component": "ThemeManager"}

        try:
            # Register built-in themes
            self._register_built_in_themes()
            # Initialize theme system
            self._initialize_theme()
            # Start system theme monitoring
            self._setup_system_theme_monitoring()

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

    @property
    def theme(self) -> Optional[Theme]:
        """Get the current theme."""
        return self._current_theme

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

    def _setup_system_theme_monitoring(self) -> None:
        """Set up monitoring for system theme changes."""
        self._last_known_system_mode = detect_system_theme_mode()

        # Create timer for checking system theme changes
        self._system_theme_timer = QTimer(self)
        self._system_theme_timer.timeout.connect(self._check_system_theme)

        # Check every 2 seconds by default
        check_interval = 2000

        # Platform-specific optimizations
        if sys.platform == "win32":
            # Windows: Can detect theme changes via registry
            check_interval = (
                1000  # More frequent checks as it's less resource intensive
            )
        elif sys.platform == "darwin":
            # macOS: Can detect theme changes via system events
            check_interval = 1000
        else:
            # Linux: Depends on desktop environment
            check_interval = 3000  # Less frequent due to potential resource usage

        self._system_theme_timer.start(check_interval)

    def apply_theme_by_name(self, theme_name: str) -> None:
        """
        Apply a theme by its name.

        Args:
            theme_name: Name of the theme to apply

        Raises:
            ThemeError: If theme name is not found
        """
        try:
            if theme := self._available_themes.get(theme_name):
                self._apply_theme(theme)
                # If it's a built-in theme, update the mode
                if theme_name.lower() in ["light", "dark", "irate"]:
                    self._theme_mode = ThemeMode(theme_name.lower())
                    self._settings.setValue("theme/mode", self._theme_mode.value)
                self.logger.info(
                    f"Applied theme: {theme_name}",
                    context={**self._context, "theme": theme_name},
                )
            else:
                raise ThemeError(f"Theme not found: {theme_name}")

        except Exception as e:
            self.logger.error(
                "Failed to apply theme",
                error=e,
                context={**self._context, "theme_name": theme_name},
            )
            self.error_occurred.emit(f"Failed to apply theme: {theme_name}")
            raise

    @property
    def available_theme_names(self) -> list[str]:
        """Get list of available theme names."""
        return list(self._available_themes.keys())

    def _check_system_theme(self) -> None:
        """Check for system theme changes."""
        try:
            current_mode = detect_system_theme_mode()
            if (
                self._last_known_system_mode is not None
                and current_mode != self._last_known_system_mode
            ):

                self.logger.debug(
                    "System theme change detected",
                    context={
                        **self._context,
                        "old_mode": self._last_known_system_mode,
                        "new_mode": current_mode,
                    },
                )

                self._last_known_system_mode = current_mode
                self.system_theme_changed.emit()

                # Update theme if using system theme
                if self._theme_mode == ThemeMode.SYSTEM:
                    self._update_current_theme()

        except Exception as e:
            self.logger.error(
                "Error checking system theme",
                error=e,
                context=self._context,
            )

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
            if self._stylesheet_generator:
                drawer_style = self._stylesheet_generator.generate_component_stylesheet(
                    "drawer"
                )
                self.logger.debug(
                    "Generated drawer stylesheet",
                    {**self._context, "stylesheet": drawer_style},
                )

            # Get application instance with proper type casting
            app = QApplication.instance()
            if not app:
                raise RuntimeError("No QApplication instance found")

            # Cast to QApplication to satisfy type checker
            app = cast(QApplication, app)

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
                # Create fresh system theme to get latest OS colors
                system_theme = create_system_theme()
                self._apply_theme(system_theme)
            else:
                theme_name = self._theme_mode.capitalize()
                if theme := self._available_themes.get(theme_name):
                    self._apply_theme(theme)
                else:
                    raise ThemeError(f"Theme not found: {theme_name}")

        except Exception as e:
            self.logger.error(
                "Failed to update current theme", error=e, context=self._context
            )
            raise ThemeError("Failed to update current theme") from e

    def set_theme_mode(self, mode: ThemeMode) -> None:
        """
        Set the theme mode and update the theme accordingly.

        Args:
            mode: The theme mode to set
        """
        try:
            if mode != self._theme_mode:
                self._theme_mode = mode
                self._settings.setValue("theme/mode", mode.value)
                self._update_current_theme()
                self.theme_mode_changed.emit(mode)

                self.logger.info(
                    f"Theme mode changed to: {mode}",
                    context={**self._context, "mode": mode},
                )
        except Exception as e:
            self.logger.error(
                "Failed to set theme mode",
                error=e,
                context={**self._context, "mode": mode},
            )
            raise ThemeError(f"Failed to set theme mode: {mode}") from e

    def get_component_stylesheet(self, component_name: str) -> Optional[str]:
        """
        Get stylesheet for a specific component.

        Args:
            component_name: Name of the component to style

        Returns:
            Component-specific stylesheet or None if no style exists
        """
        if self._stylesheet_generator is None:
            return None
        return self._stylesheet_generator.generate_component_stylesheet(component_name)

    def cleanup(self) -> None:
        """Clean up resources used by the theme manager."""
        if self._system_theme_timer is not None:
            self._system_theme_timer.stop()

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


""
