import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QListWidget,
    QMessageBox,
)
from PySide6.QtCore import Qt


class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meine To-Do-Liste")
        self.setGeometry(100, 100, 400, 500)  # x, y, Breite, Höhe

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Neue Aufgabe hier eingeben...")

        self.add_button = QPushButton("Hinzufügen")

        self.task_list = QListWidget()

        self.delete_button = QPushButton("Löschen")

        # --- Layout für den Eingabebereich ---
        # Ein horizontales Layout (QHBoxLayout) für das Eingabefeld und den Hinzufügen-Button.
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.add_button)

        # --- Widgets zum Hauptlayout hinzufügen ---
        main_layout.addLayout(input_layout)  # Fügt das horizontale Layout oben hinzu
        main_layout.addWidget(self.task_list)
        main_layout.addWidget(self.delete_button)

        # --- Signale mit Slots verbinden (Event-Handling) ---
        self.add_button.clicked.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)
        self.task_input.returnPressed.connect(self.add_task)

    def add_task(self):
        task_text = self.task_input.text().strip()

        if task_text:
            self.task_list.addItem(task_text)
            self.task_input.clear()
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setText("Das Eingabefeld ist leer.")
            msg_box.setInformativeText(
                "Bitte geben Sie eine Aufgabe ein, um sie hinzuzufügen."
            )
            msg_box.setWindowTitle("Achtung")
            msg_box.exec()

    def delete_task(self):
        selected_item = (
            self.task_list.currentItem()
        )  # Das aktuell ausgewählte Element abrufen

        if selected_item:
            # Das Element aus der Liste entfernen. takeItem gibt das Element zurück und entfernt es.
            self.task_list.takeItem(self.task_list.row(selected_item))
        else:
            # Optional: Eine Meldung anzeigen, wenn keine Aufgabe zum Löschen ausgewählt wurde.
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Keine Aufgabe ausgewählt.")
            msg_box.setInformativeText(
                "Bitte wählen Sie eine Aufgabe aus der Liste aus, die Sie löschen möchten."
            )
            msg_box.setWindowTitle("Information")
            msg_box.exec()


def main():
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
