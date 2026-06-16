# src/suspension/ui/components/base/placeholder.py

"""Placeholder widget for initial panel content."""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class PlaceholderWidget(QWidget):
    """
    Simple placeholder widget displaying centered text.
    Used for initial panel content before real content is loaded.
    """

    def __init__(
        self, text: str = "Content coming soon...", parent: QWidget | None = None
    ) -> None:
        """
        Initialize placeholder widget.

        Args:
            text: Text to display
            parent: Parent widget
        """
        super().__init__(parent)

        layout = QVBoxLayout(self)
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
