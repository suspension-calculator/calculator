# src/suspension/ui/components/base/drawer.py

from typing import Optional
from PyQt6.QtCore import QPropertyAnimation
from PyQt6.QtWidgets import QWidget, QPushButton, QFrame, QVBoxLayout

from ...models.theme import Theme
from ...styles import StylesheetGenerator


class Drawer(QWidget):
    """
    A generic animated drawer component.

    Features:
    - Collapsible/expandable with animation
    - Theme integration
    - Customizable content
    - Toggle button
    """

    def __init__(
        self,
        content: QWidget,
        parent: Optional[QWidget] = None,
        width: int = 250,
        animation_duration: int = 200,
    ) -> None:
        """
        Initialize the drawer.

        Args:
            content: Widget to display in the drawer
            parent: Parent widget
            width: Expanded drawer width
            animation_duration: Animation duration in milliseconds
        """
        super().__init__(parent)
        self.setObjectName("base_drawer")

        # Setup layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Create drawer frame
        self.drawer_frame = QFrame(self)
        self.drawer_frame.setObjectName("drawer_frame")

        # Add content to drawer frame
        drawer_layout = QVBoxLayout(self.drawer_frame)
        drawer_layout.setContentsMargins(0, 0, 0, 0)
        drawer_layout.addWidget(content)

        # Create toggle button
        self.toggle_button = QPushButton("≡", self)
        self.toggle_button.setObjectName("drawer_toggle")
        self.toggle_button.setFixedSize(24, 24)
        self.toggle_button.clicked.connect(self.toggle_drawer)

        # Add widgets to layout
        layout.addWidget(self.toggle_button)
        layout.addWidget(self.drawer_frame)

        # Setup animation
        self.animation = QPropertyAnimation(self.drawer_frame, b"maximumWidth")
        self.animation.setDuration(animation_duration)

        # Initial state
        self.drawer_width = width
        self.drawer_frame.setFixedWidth(width)
        self.is_open = True

    def toggle_drawer(self) -> None:
        """Toggle the drawer open/closed state."""
        if self.is_open:
            self.animation.setStartValue(self.drawer_width)
            self.animation.setEndValue(0)
            self.toggle_button.setText("☰")
        else:
            self.animation.setStartValue(0)
            self.animation.setEndValue(self.drawer_width)
            self.toggle_button.setText("×")

        self.animation.start()
        self.is_open = not self.is_open

    def apply_theme(self, theme: Theme) -> None:
        """Apply theme to the drawer."""
        window = self.window()
        if window is not None:
            stylesheet_generator = window.property("stylesheet_generator")
            if stylesheet_generator and isinstance(
                stylesheet_generator, StylesheetGenerator
            ):
                self.setStyleSheet(
                    stylesheet_generator.generate_component_stylesheet("drawer")
                )

        self.drawer_frame.setStyleSheet(
            f"""
            QFrame {{
                background-color: {theme.colors.sidebar};
                border-right: 1px solid {theme.colors.border};
            }}
        """
        )
