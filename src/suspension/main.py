# src/suspension/main.py
import sys

from PyQt6.QtWidgets import QApplication

from suspension.ui.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Suspension Calculator")

    # Create main window
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
