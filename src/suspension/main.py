# src/suspension/main.py
import sys

from PyQt6.QtWidgets import QApplication

from suspension.infrastructure.state.observers.navigation import NavigationStore
from suspension.infrastructure.state.types.navigation import NavigationState
from suspension.ui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Suspension Calculator")

    # Initialize stores
    nav_store = NavigationStore(NavigationState())

    # Create main window with dependencies
    window = MainWindow(nav_store=nav_store)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
