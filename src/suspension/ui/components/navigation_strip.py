# src/suspension/ui/components/navigation_strip.py
import qtawesome as qta
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QFrame,
)

from suspension.ui.styles.theme import Theme


class NavigationStrip(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(40)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(2, 8, 2, 8)
        layout.setSpacing(8)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        # Create navigation button with larger icon
        self.nav_button = QPushButton()
        self.nav_button.setFixedSize(36, 36)
        icon = qta.icon("fa5s.compass")
        self.nav_button.setIcon(icon)
        self.nav_button.setIconSize(QtCore.QSize(24, 24))
        self.nav_button.setToolTip("Show/Hide Navigation Panel")
        self.nav_button.setCheckable(True)
        self.nav_button.setChecked(True)

        layout.addWidget(self.nav_button)
        layout.addStretch()

        # Apply theme styles
        self.setStyleSheet(Theme.current().navigation_strip_style())
