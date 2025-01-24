# src/suspension/ui/pages/base_page.py

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QVBoxLayout


class BasePage(QWidget):
    """Base class for all content pages"""

    # Signals
    state_changed = pyqtSignal(dict)  # Emitted when page state changes

    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui()

    def _setup_ui(self):
        """Setup the basic UI structure"""
        self.layout = QVBoxLayout(self)

    def save_state(self) -> dict:
        """Save the page state"""
        return {}

    def restore_state(self, state: dict):
        """Restore the page state"""
        pass

    def validate(self) -> bool:
        """Validate the page data"""
        return True
