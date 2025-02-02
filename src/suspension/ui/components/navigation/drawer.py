# /src/suspension/ui/components/navigation/drawer.py

from typing import Optional

import qtawesome as qta  # type: ignore
from PyQt6.QtCore import QEasingCurve, QPropertyAnimation, QSize
from PyQt6.QtWidgets import QFrame, QPushButton, QVBoxLayout, QWidget

from ....utils.logging import app_logger
from ... import Theme


class Drawer(QWidget):
    """
    A generic animated drawer component.

    Features:
    - Collapsible/expandable with animation
    - Theme integration
    - Customizable content
    - Toggle button with FontAwesome icons
    """

    def __init__(
        self,
        content: QWidget,
        parent: Optional[QWidget] = None,
        width: int = 250,
        animation_duration: int = 200,
    ) -> None:
        """Initialize the drawer."""
        super().__init__(parent)
        self._context = {"component": "Drawer"}
        app_logger.info("Initializing drawer", self._context)

        self.setObjectName("base_drawer")

        # Store initial width
        self.drawer_width = width
        self.collapsed_width = 48  # Width when collapsed (enough for the button)

        # Create main layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Create container for toggle button
        self.button_container = QWidget(self)
        self.button_container.setObjectName("button_container")
        self.button_container.setFixedHeight(48)

        # Create toggle button with icon
        self.toggle_button = QPushButton(self.button_container)
        self.toggle_button.setObjectName("drawer_toggle")
        self.toggle_button.setFixedSize(32, 32)
        self.toggle_button.move(8, 8)
        self.toggle_button.clicked.connect(self.toggle_drawer)

        # Set initial icon
        self.menu_icon = qta.icon("fa5s.bars", color="white")
        self.close_icon = qta.icon("fa5s.times", color="white")
        self.toggle_button.setIcon(self.close_icon)
        self.toggle_button.setIconSize(QSize(16, 16))

        # Create drawer frame
        self.drawer_frame = QFrame(self)
        self.drawer_frame.setObjectName("drawer_frame")

        # Add content to drawer frame
        drawer_layout = QVBoxLayout(self.drawer_frame)
        drawer_layout.setContentsMargins(0, 0, 0, 0)
        drawer_layout.setSpacing(0)
        drawer_layout.addWidget(content)

        # Add widgets to main layout
        self.main_layout.addWidget(self.button_container)
        self.main_layout.addWidget(self.drawer_frame)

        # Setup width animation for the frame
        self.width_animation = QPropertyAnimation(self, b"maximumWidth", self)
        self.width_animation.setDuration(animation_duration)
        self.width_animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.width_animation.valueChanged.connect(self._handle_animation_value_changed)
        self.width_animation.finished.connect(self._on_animation_finished)

        # Set initial sizes
        self.setFixedWidth(width)  # This sets both min and max width
        self.drawer_frame.setMinimumWidth(width)

        # Initial state
        self.is_open = True
        app_logger.info("Drawer initialized", {**self._context, "width": width})

    def toggle_drawer(self) -> None:
        """Toggle the drawer open/closed state."""
        try:
            animation_context = {
                **self._context,
                "current_state": "open" if self.is_open else "closed",
                "current_width": self.width(),
                "frame_width": self.drawer_frame.width(),
            }
            app_logger.info("Starting drawer toggle", animation_context)

            # Allow widget to be resized
            self.setMinimumWidth(self.collapsed_width)
            self.setMaximumWidth(self.drawer_width)

            if self.is_open:
                # Collapse
                self.width_animation.setStartValue(self.drawer_width)
                self.width_animation.setEndValue(self.collapsed_width)
                self.toggle_button.setIcon(self.menu_icon)
            else:
                # Expand
                self.width_animation.setStartValue(self.collapsed_width)
                self.width_animation.setEndValue(self.drawer_width)
                self.toggle_button.setIcon(self.close_icon)

            self.width_animation.start()

            self.is_open = not self.is_open
            app_logger.info(
                "Drawer toggle initiated",
                {
                    **animation_context,
                    "new_state": "open" if self.is_open else "closed",
                },
            )
        except Exception as e:
            app_logger.error("Failed to toggle drawer", e, self._context)
            raise

    def _handle_animation_value_changed(self, value: float) -> None:
        """Handle animation value changes."""
        try:
            self.setFixedWidth(int(value))
            if self.is_open:
                self.drawer_frame.setFixedWidth(int(value))
            else:
                self.drawer_frame.setFixedWidth(
                    max(0, int(value - self.collapsed_width))
                )

            app_logger.debug(
                "Animation value changed",
                {
                    **self._context,
                    "value": value,
                    "drawer_width": self.width(),
                    "frame_width": self.drawer_frame.width(),
                },
            )
        except Exception as e:
            app_logger.error(
                "Failed to handle animation value change", e, self._context
            )
            raise

    def _on_animation_finished(self) -> None:
        """Handle animation completion."""
        try:
            if self.is_open:
                self.setFixedWidth(self.drawer_width)
                self.drawer_frame.setFixedWidth(self.drawer_width)
            else:
                self.setFixedWidth(self.collapsed_width)
                self.drawer_frame.setFixedWidth(0)

            animation_context = {
                **self._context,
                "final_width": self.width(),
                "frame_width": self.drawer_frame.width(),
                "is_open": self.is_open,
            }
            app_logger.info("Animation finished", animation_context)
        except Exception as e:
            app_logger.error("Failed to handle animation completion", e, self._context)
            raise

    def apply_theme(self, theme: Theme) -> None:
        """Apply theme to the drawer components."""
        try:
            # Update icon colors based on theme
            self.menu_icon = qta.icon("fa5s.bars", color=theme.colors.text_primary)
            self.close_icon = qta.icon("fa5s.times", color=theme.colors.text_primary)

            # Update current icon
            current_icon = self.menu_icon if not self.is_open else self.close_icon
            self.toggle_button.setIcon(current_icon)

            app_logger.debug(
                "Applied theme to drawer",
                {**self._context, "theme": theme.metadata.name},
            )
        except Exception as e:
            app_logger.error("Failed to apply theme to drawer", e, self._context)
            raise
