import requests
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QTableWidgetItem, QWidget

from desktop.ui.ui_chat import Ui_Form
from models.user.user_get_dto import UserGetDto


class ChatWindow(QWidget, Ui_Form):
    def __init__(self, chat_id: int, current_user: UserGetDto):
        super().__init__()
        self.setupUi(self)
        self.chat_id = chat_id
        self.current_user = current_user
        self.timer = QTimer(self)

        self.timer.timeout.connect(self.request_chat_messages)
        self.pushButton.clicked.connect(self.push_chat_message)
        self.pushButton_update.clicked.connect(self.request_chat_messages)

        self.request_chat_messages()
        self.timer.start(2000)

    def request_chat_messages(self):
        response = requests.get("http://127.0.0.1:5000/message/get-all-from-chat",
                                params={"chat_id": self.chat_id})
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
        v_scroll_bar = self.tableWidget.verticalScrollBar()
        v_scroll_bar.setValue(v_scroll_bar.maximum())

    def push_chat_message(self):
        text = self.textEdit.toPlainText()
        response = requests.post("http://127.0.0.1:5000/message/",
                                json={"chat_id": self.chat_id,
                                      "user_id": self.current_user.id,
                                      "text": text})
        self.request_chat_messages()

