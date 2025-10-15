DARK_STYLESHEET = """
QMainWindow {
    background-color: #121212;
}
QWidget {
    background-color: #121212;
    color: #E0E0E0;
    font-size: 14px;
}
QPushButton {
    background-color: #1E1E1E;
    border: 1px solid #3A3A3A;
    padding: 6px 10px;
    border-radius: 5px;
}
QPushButton:hover {
    background-color: #2A2A2A;
}
QLineEdit, QComboBox, QDateEdit, QListWidget {
    background-color: #1E1E1E;
    border: 1px solid #3A3A3A;
    border-radius: 5px;
    padding: 6px;
    color: #E0E0E0;
}
QMenuBar {
    background-color: #1E1E1E;
    color: #E0E0E0;
}
QMenuBar::item:selected {
    background-color: #0078D7;
}
QMenu {
    background-color: #1E1E1E;
    color: #E0E0E0;
    border: 1px solid #3A3A3A;
}
QMenu::item:selected {
    background-color: #0078D7;
    color: #FFFFFF;
}
QListWidget::item:selected {
    background-color: #0078D7;
    color: #FFFFFF;
}
"""

LIGHT_STYLESHEET = """
QWidget {
    background-color: #f0f0f0;
    color: #000000;
    font-size: 14px;
}
QPushButton {
    background-color: #e1e1e1;
    border: 1px solid #adadad;
    padding: 6px 10px;
    border-radius: 5px;
}
QPushButton:hover {
    background-color: #f0f0f0;
}
QLineEdit, QComboBox, QDateEdit, QListWidget {
    background-color: #ffffff;
    border: 1px solid #adadad;
    border-radius: 5px;
    padding: 6px;
}
QMenuBar, QMenuBar::item {
    background-color: #f0f0f0;
    color: #000000;
}
QMenu {
    background-color: #ffffff;
    color: #000000;
}
QMenu::item:selected {
    background-color: #0078d7;
    color: #ffffff;
}
QListWidget::item:selected {
    background-color: #0078d7;
    color: #ffffff;
}
"""