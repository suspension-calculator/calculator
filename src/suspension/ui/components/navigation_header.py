# src/suspension/ui/components/navigation_header.py
import qtawesome as qta
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QDockWidget,
)

from suspension.ui.styles.theme import Theme


class NavigationHeader(QWidget):
    def __init__(self, dock_widget: QDockWidget, theme: Theme, parent=None):
        super().__init__(parent)
        self.dock_widget = dock_widget

        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 2, 5, 2)

        # Title label
        self.title_label = QLabel("Navigation")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Close button (minus icon)
        self.close_button = QPushButton()
        self.close_button.setFixedSize(32, 32)
        self.close_button.setIcon(qta.icon("fa5s.minus"))
        self.close_button.setToolTip("Hide Navigation Panel")
        self.close_button.clicked.connect(self.dock_widget.hide)

        layout.addWidget(self.title_label, 1)
        layout.addWidget(self.close_button)

        self.setStyleSheet(theme.navigation_header_style())
