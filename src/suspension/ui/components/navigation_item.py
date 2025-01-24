# src/suspension/ui/components/navigation_item.py
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt

from suspension.ui.styles.theme import Theme


class NavigationItem(QWidget):
    def __init__(self, text: str, is_child: bool = False, parent=None):
        super().__init__(parent)
        self.setObjectName("NavigationItem")  # For styling

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        if is_child:
            # Indentation spacer for child items
            spacer = QWidget()
            spacer.setFixedWidth(16)
            spacer.setObjectName("NavigationSpacer")
            layout.addWidget(spacer)

        self.label = QLabel(text)
        self.label.setObjectName("NavigationLabel")
        layout.addWidget(self.label)
        layout.addStretch()

        # Apply theme
        self.setStyleSheet(Theme.current().navigation_item_style())
