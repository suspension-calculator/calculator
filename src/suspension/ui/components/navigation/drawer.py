# /src/suspension/ui/components/navigation/drawer.py

from typing import ClassVar, Optional

import qtawesome as qta  # type: ignore
from PyQt6.QtCore import QEasingCurve, QPropertyAnimation, QSize
from PyQt6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from ....utils.logging import StructuredLogger, app_logger
from ... import Theme
from ...managers.layout import LayoutManager
from ...managers.navigation import NavigationManager


class Drawer(QWidget):
    """
    A generic animated drawer component.

    Features:
    - Collapsible/expandable with animation
    - Theme integration
    - Customizable content
    - Toggle button with FontAwesome icons
    - Layout state management via LayoutManager
    """

    logger: ClassVar[StructuredLogger] = app_logger

    def __init__(
        self,
        content: QWidget,
        nav_manager: NavigationManager,
        layout_manager: LayoutManager,
        parent: Optional[QWidget] = None,
        width: int = 250,
        animation_duration: int = 200,
    ) -> None:
        """Initialize drawer with content and layout management.

        Args:
            content: Widget to display in drawer
            layout_manager: Manager for layout state
            parent: Parent widget
            width: Initial drawer width
            animation_duration: Duration of open/close animation
        """
        super().__init__(parent)
        self._context = {"component": "Drawer"}
        self.logger.info("Initializing drawer", self._context)

        self.setObjectName("base_drawer")

        self._nav_manager = nav_manager
        self._layout_manager = layout_manager

        # Store initial configuration
        self.drawer_width = width
        self.collapsed_width = 48
        self.is_open = nav_manager.get_drawer_state()

        # Set initial collapsed state
        self.setProperty("collapsed", not self.is_open)

        # Create main layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Setup components
        self._setup_header()
        self._setup_content_frame(content)
        self._setup_animation(animation_duration)

        # Set initial sizes
        if self.is_open:
            self.setFixedWidth(width)
            self.drawer_frame.setFixedWidth(width)
        else:
            self.setFixedWidth(self.collapsed_width)
            self.drawer_frame.setFixedWidth(0)

        # Connect to navigation manager
        nav_manager.drawer_state_changed.connect(self._handle_state_change)

    def _setup_header(self) -> None:
        """Create and setup the drawer header."""
        self.header = QWidget()
        self.header.setObjectName("drawerHeader")
        header_layout = QHBoxLayout(self.header)
        header_layout.setContentsMargins(8, 0, 8, 0)
        header_layout.setSpacing(8)

        # Create toggle button
        self.toggle_button = QPushButton(self.header)  # Note: setting parent
        self.toggle_button.setObjectName("drawer_toggle")
        self.toggle_button.setFixedSize(32, 32)
        self.toggle_button.clicked.connect(self.toggle_drawer)

        # Set initial icon
        self.menu_icon = qta.icon("fa5s.bars", color="white")
        self.close_icon = qta.icon("fa5s.times", color="white")
        self.toggle_button.setIcon(self.close_icon if self.is_open else self.menu_icon)
        self.toggle_button.setIconSize(QSize(16, 16))

        header_layout.addWidget(self.toggle_button)

        # Add header text
        self.header_label = QLabel("Navigation", self.header)  # Note: setting parent
        self.header_label.setObjectName("drawerHeaderText")
        header_layout.addWidget(self.header_label)
        header_layout.addStretch()

        self.main_layout.addWidget(self.header)

    # def _setup_button_container(self) -> None:
    #     """Create and setup the toggle button container."""
    #     self.button_container = QWidget(self)
    #     self.button_container.setObjectName("button_container")
    #     self.button_container.setFixedHeight(48)
    #
    #     self.toggle_button = QPushButton(self.button_container)
    #     self.toggle_button.setObjectName("drawer_toggle")
    #     self.toggle_button.setFixedSize(32, 32)
    #     self.toggle_button.move(8, 8)
    #     self.toggle_button.clicked.connect(self.toggle_drawer)
    #
    #     # Set initial icon
    #     self.menu_icon = qta.icon("fa5s.bars", color="white")
    #     self.close_icon = qta.icon("fa5s.times", color="white")
    #     self.toggle_button.setIcon(self.close_icon)
    #     self.toggle_button.setIconSize(QSize(16, 16))
    #
    #     self.main_layout.addWidget(self.button_container)

    def _setup_content_frame(self, content: QWidget) -> None:
        """Create and setup the content frame.

        Args:
            content: Widget to display in the drawer
        """
        self.drawer_frame = QFrame(self)
        self.drawer_frame.setObjectName("drawer_frame")

        drawer_layout = QVBoxLayout(self.drawer_frame)
        drawer_layout.setContentsMargins(0, 0, 0, 0)
        drawer_layout.setSpacing(0)
        drawer_layout.addWidget(content)

        self.main_layout.addWidget(self.drawer_frame)

    def _setup_animation(self, duration: int) -> None:
        """Setup the drawer animation.

        Args:
            duration: Animation duration in milliseconds
        """
        self.width_animation = QPropertyAnimation(self, b"maximumWidth", self)
        self.width_animation.setDuration(duration)
        self.width_animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.width_animation.valueChanged.connect(self._handle_animation_value_changed)
        self.width_animation.finished.connect(self._on_animation_finished)

    def toggle_drawer(self) -> None:
        """Toggle the drawer open/closed state."""
        try:
            # Only notify navigation manager, it will trigger state change
            self._nav_manager.set_drawer_visible(not self.is_open)
        except Exception as e:
            self.logger.error("Failed to toggle drawer", e, self._context)
            raise

    def _handle_animation_value_changed(self, value: float) -> None:
        """Handle animation value changes."""
        try:
            current_width = int(value)
            self.setFixedWidth(current_width)

            # Update collapsed state early
            is_collapsed = value <= (self.collapsed_width + 10)  # More buffer
            if is_collapsed != self.property("collapsed"):
                self.setProperty("collapsed", is_collapsed)
                self.style().unpolish(self)
                self.style().polish(self)
                self.update()

            # Handle frame width
            if is_collapsed:
                self.drawer_frame.setFixedWidth(0)
                self.header_label.setVisible(False)
            else:
                frame_width = max(0, current_width - self.collapsed_width)
                self.drawer_frame.setFixedWidth(frame_width)
                # Only show text when drawer is mostly open
                self.header_label.setVisible(value > (self.drawer_width * 0.75))

            self.logger.debug(
                "Animation value changed",
                {
                    **self._context,
                    "value": value,
                    "drawer_width": self.width(),
                    "frame_width": self.drawer_frame.width(),
                    "collapsed": is_collapsed,
                },
            )
        except Exception as e:
            self.logger.error(
                "Failed to handle animation value change", e, self._context
            )
            raise

    def _handle_state_change(self, visible: bool) -> None:
        """Handle state changes from navigation manager.

        Args:
            visible: New visibility state
        """
        if visible == self.is_open:
            return  # Prevent duplicate animations

        self.is_open = visible

        # Start animation
        if not visible:
            self.width_animation.setStartValue(self.width())
            self.width_animation.setEndValue(self.collapsed_width)
            self.toggle_button.setIcon(self.menu_icon)
        else:
            self.width_animation.setStartValue(self.width())
            self.width_animation.setEndValue(self.drawer_width)
            self.toggle_button.setIcon(self.close_icon)

        self.width_animation.start()

        self.logger.debug(
            "Handling drawer state change",
            {**self._context, "visible": visible, "current_width": self.width()},
        )

    def _on_animation_finished(self) -> None:
        """Handle animation completion."""
        try:
            final_width = self.drawer_width if self.is_open else self.collapsed_width
            self.setFixedWidth(final_width)

            if self.is_open:
                self.drawer_frame.setFixedWidth(self.drawer_width)
            else:
                self.drawer_frame.setFixedWidth(0)

            # Save size in layout manager
            self._layout_manager.save_component_size(
                "drawer",
                {"width": final_width, "frame_width": self.drawer_frame.width()},
            )

            self.logger.info(
                "Animation finished",
                {
                    **self._context,
                    "final_width": final_width,
                    "frame_width": self.drawer_frame.width(),
                    "is_open": self.is_open,
                },
            )
        except Exception as e:
            self.logger.error("Failed to handle animation completion", e, self._context)
            raise

    def apply_theme(self, theme: Theme) -> None:
        """Apply theme to the drawer components.

        Args:
            theme: Theme to apply
        """
        try:
            # Update icon colors based on theme
            self.menu_icon = qta.icon("fa5s.bars", color=theme.colors.text_primary)
            self.close_icon = qta.icon("fa5s.times", color=theme.colors.text_primary)

            # Update current icon
            current_icon = self.menu_icon if not self.is_open else self.close_icon
            self.toggle_button.setIcon(current_icon)

            # The stylesheet should be applied by the parent window
            # We need to force a style refresh
            self.style().unpolish(self)
            self.style().polish(self)
            self.update()

            self.logger.debug(
                "Applied theme to drawer",
                {**self._context, "theme": theme.metadata.name},
            )
        except Exception as e:
            self.logger.error("Failed to apply theme to drawer", e, self._context)
            raise
