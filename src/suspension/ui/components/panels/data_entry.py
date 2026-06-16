# src/suspension/ui/components/panels/data_entry.py

"""
Dynamic data entry panel with support for form injection and real-time validation.
"""

from typing import ClassVar, Optional

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget

from suspension.utils import StructuredLogger, app_logger

from ...managers.layout import LayoutManager
from .base_panel import BasePanel


class DataEntryPanel(BasePanel):
    """
    Dynamic data entry panel that can render different input forms.
    Supports real-time validation and Redux state updates.

    Features:
    - Dynamic form component injection
    - Real-time validation support
    - State persistence
    - Form state management

    Signals:
        form_changed: Emitted when input form changes
        data_changed: Emitted when form data changes
    """

    logger: ClassVar[StructuredLogger] = app_logger
    form_changed = pyqtSignal()  # Emitted when input form changes
    data_changed = pyqtSignal()  # Emitted when form data changes

    def __init__(
        self,
        panel_id: str,
        layout_manager: LayoutManager,
        initial_form: Optional[QWidget] = None,
        parent: Optional[QWidget] = None,
    ) -> None:
        """
        Initialize the data entry panel.

        Args:
            panel_id: Unique identifier for the panel
            initial_form: Initial form widget to display
            parent: Parent widget
        """
        super().__init__(
            title="Data Entry",
            panel_id=panel_id,
            layout_manager=layout_manager,
            parent=parent,
            allow_close=True,
            allow_float=True,
        )

        self._current_form: Optional[QWidget] = None

        # Set initial form if provided
        if initial_form:
            self.set_form(initial_form)

    def set_form(self, form: QWidget) -> None:
        """
        Set the current input form.

        Args:
            form: Form widget to display
        """
        self.set_content(form)
        self._current_form = form
        self.form_changed.emit()

    def get_current_form(self) -> Optional[QWidget]:
        """
        Get the currently displayed form.

        Returns:
            Current form widget or None if no form is set
        """
        return self._current_form
