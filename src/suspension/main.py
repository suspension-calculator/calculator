# src/suspension/main.py
import sys
from typing import NoReturn

from PyQt6.QtWidgets import QApplication

from suspension.ui.windows.main_window import MainWindow


def main() -> NoReturn:
    """
    Main entry point for the Suspension Calculator application.
    Never returns as it enters the Qt event loop.
    """
    print("Starting application...")
    app = QApplication(sys.argv)
    print("Created QApplication")
    app.setApplicationName("Suspension Calculator")
    print("Set application name")

    # Create main window
    print("Creating main window...")
    window = MainWindow()
    print("Created main window")
    window.show()
    print("Showed window")
    sys.exit(app.exec())


if __name__ == "__main__":
    print("Entering main")
    main()
