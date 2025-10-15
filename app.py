import json
import os
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
    QComboBox,
    QDateEdit,
    QListWidgetItem,
)
from PySide6.QtGui import QColor, QAction
from PySide6.QtCore import QDate, Qt
from themes import DARK_STYLESHEET, LIGHT_STYLESHEET


class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tasks_file = "tasks.json"
        self.current_theme_stylesheet = LIGHT_STYLESHEET

        self.priority_map = {
            "Hoch": {
                "icon": "🔴",
                "light_color": QColor("#FFD2D2"),
                "dark_color": QColor("#B22222"),
            },
            "Mittel": {
                "icon": "🟡",
                "light_color": QColor("#FFFDD2"),
                "dark_color": QColor("#D4AF37"),
            },
            "Niedrig": {
                "icon": "🟢",
                "light_color": QColor("#D2FFD2"),
                "dark_color": QColor("#228B22"),
            },
        }

        self.init_ui()
        self.load_tasks()
        self.set_theme(LIGHT_STYLESHEET)

    def init_ui(self):
        self.setWindowTitle("Meine To-Do-Liste")
        self.setGeometry(100, 100, 500, 600)

        # --- Menü ---
        menu_bar = self.menuBar()
        theme_menu = menu_bar.addMenu("Theme")
        theme_menu.addAction(
            QAction(
                "Helles Theme", self, triggered=lambda: self.set_theme(LIGHT_STYLESHEET)
            )
        )
        theme_menu.addAction(
            QAction(
                "Dunkles Theme", self, triggered=lambda: self.set_theme(DARK_STYLESHEET)
            )
        )

        # --- Layouts ---
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        input_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Neue Aufgabe...")

        self.priority_input = QComboBox()
        self.priority_input.addItems(["Niedrig", "Mittel", "Hoch"])
        self.priority_input.setCurrentIndex(1)

        self.date_input = QDateEdit(QDate.currentDate())
        self.date_input.setCalendarPopup(True)

        self.add_button = QPushButton("Hinzufügen")

        input_layout.addWidget(self.task_input)
        input_layout.addWidget(self.priority_input)
        input_layout.addWidget(self.date_input)
        input_layout.addWidget(self.add_button)

        self.task_list = QListWidget()
        self.delete_button = QPushButton("Ausgewählte Aufgabe löschen")

        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.task_list)
        main_layout.addWidget(self.delete_button)

        # --- Events ---
        self.add_button.clicked.connect(self.add_task)
        self.task_input.returnPressed.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)
        self.task_list.itemChanged.connect(self.task_state_changed)

    def add_task(self):
        text = self.task_input.text().strip()
        if not text:
            QMessageBox.warning(self, "Achtung", "Das Eingabefeld ist leer.")
            return

        task = {
            "text": text,
            "priority": self.priority_input.currentText(),
            "due_date": self.date_input.date().toString("yyyy-MM-dd"),
            "done": False,
        }
        self.create_task_item(task)
        self.task_input.clear()

    def create_task_item(self, task):
        p_info = self.priority_map.get(task["priority"])
        display_text = f"{p_info['icon']} {task['text']}  (Fällig: {task['due_date']})"

        item = QListWidgetItem(display_text)
        item.setData(Qt.UserRole, task)
        item.setFlags(
            item.flags()
            | Qt.ItemIsUserCheckable
            | Qt.ItemIsEnabled
            | Qt.ItemIsSelectable
        )
        item.setCheckState(Qt.Checked if task["done"] else Qt.Unchecked)

        self.update_task_appearance(item)
        self.task_list.addItem(item)

    def update_task_appearance(self, item):
        task = item.data(Qt.UserRole)
        p_info = self.priority_map[task["priority"]]
        is_dark = self.current_theme_stylesheet == DARK_STYLESHEET
        color = p_info["dark_color"] if is_dark else p_info["light_color"]
        item.setBackground(color)

        font = item.font()
        font.setStrikeOut(task["done"])
        item.setFont(font)
        item.setForeground(
            QColor("#AAAAAA")
            if task["done"]
            else QColor("#FFFFFF" if is_dark else "#000000")
        )

    def task_state_changed(self, item):
        task = item.data(Qt.UserRole)
        task["done"] = item.checkState() == Qt.Checked
        item.setData(Qt.UserRole, task)
        self.update_task_appearance(item)

    def delete_task(self):
        item = self.task_list.currentItem()
        if not item:
            QMessageBox.information(self, "Information", "Keine Aufgabe ausgewählt.")
            return
        self.task_list.takeItem(self.task_list.row(item))

    def load_tasks(self):
        if os.path.exists(self.tasks_file):
            try:
                with open(self.tasks_file, "r", encoding="utf-8") as f:
                    for task in json.load(f):
                        self.create_task_item(task)
            except (json.JSONDecodeError, TypeError):
                QMessageBox.warning(
                    self,
                    "Fehler",
                    f"Konnte Aufgaben aus {self.tasks_file} nicht laden.",
                )

    def save_tasks(self):
        tasks = [
            self.task_list.item(i).data(Qt.UserRole)
            for i in range(self.task_list.count())
        ]
        with open(self.tasks_file, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)

    def update_task_item_colors(self):
        for i in range(self.task_list.count()):
            self.update_task_appearance(self.task_list.item(i))

    def set_theme(self, stylesheet):
        self.current_theme_stylesheet = stylesheet
        QApplication.instance().setStyleSheet(stylesheet)
        self.update_task_item_colors()

    def closeEvent(self, event):
        self.save_tasks()
        event.accept()
