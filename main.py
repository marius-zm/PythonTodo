import sys
from PySide6.QtWidgets import (
    QApplication,
)
from app import ToDoApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())
