import requests
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

from desktop.auth_window import AuthWindow
from desktop.ui.ui_chat import Ui_MainWindow


class ChatWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.auth_data = []
        auth_window = AuthWindow(self.auth_data)
        while not self.auth_data:
            auth_window.exec_()
        self.request_chat_messages(6)
        self.pushButton.clicked.connect(self.push_chat_message)

    def request_chat_messages(self, chat_id: int):
        response = requests.get("http://127.0.0.1:5000/message/get-all-from-chat",
                                params={"chat_id": chat_id})
        messages = response.json()
        self.tableWidget.setRowCount(0)
        for message in messages:
            user_login = message["user"]["login"]
            time = message["time"]
            text = message["text"]
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(user_login))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(time))
            self.tableWidget.setItem(row_position, 2, QTableWidgetItem(text))

    def push_chat_message(self):
        user_id = self.auth_data[0]["id"]
        chat_id = 6
        text = self.textEdit.toPlainText()
        response = requests.post("http://127.0.0.1:5000/message/",
                                json={"chat_id": chat_id,
                                      "user_id": user_id,
                                      "text": text})
        self.request_chat_messages(6)

