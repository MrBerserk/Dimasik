import sys
import client
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QWidget, QTextEdit, QHBoxLayout


# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.update_list()

    def update_list(self):
        self.qvbox = QVBoxLayout()
        self.qvbox.addWidget(QLabel('Список тасков'))

        self.text = QTextEdit()
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.add_ticket)

        for ticket in client.get_tickets():
            self.qvbox.addWidget(TaskWidget(ticket, self.update_list))

        self.qvbox.addWidget(self.text)
        self.qvbox.addWidget(self.save_button)

        self.setWindowTitle("TODO list")
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.qvbox)
        self.setCentralWidget(self.central_widget)

    def add_ticket(self):
        client.add_ticket(self.text.toPlainText())
        self.text.setPlainText('')
        self.update_list()


class TaskWidget(QWidget):
    def __init__(self, data, callback):
        super().__init__()
        self.callback = callback
        self.data = data
        self.qvbox = QVBoxLayout()
        self.qvbox.addWidget(QLabel(f'UUID таска: {data["ticket_id"]}'))

        self.text = QTextEdit()
        self.text.setPlainText(data['text'])
        self.qvbox.addWidget(self.text)

        self.qhbox = QHBoxLayout()
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save)
        self.qhbox.addWidget(self.save_button)

        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete)
        self.qhbox.addWidget(self.delete_button)

        self.qvbox.addLayout(self.qhbox)
        self.setLayout(self.qvbox)

    def delete(self):
        client.delete_ticket(self.data['ticket_id'])
        self.callback()

    def save(self):
        client.edit_ticket(self.data['ticket_id'], self.text.toPlainText())
        self.callback()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()