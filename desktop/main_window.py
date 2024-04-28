from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import requests
from desktop.auth_window import AuthWindow
from desktop.chat_window import ChatWindow
from desktop.ui.ui_main import Ui_MainWindow
from models.user.user_get_dto import UserGetDto


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.auth_data = []
        auth_window = AuthWindow(self.auth_data)
        while not self.auth_data:
            auth_window.exec_()
        self.auth_data: UserGetDto = self.auth_data[0]
        self.chat = []

        self.tableWidget.cellDoubleClicked.connect(self.open_chat)

        self.request_user_chats()


    def request_user_chats(self):
        response = requests.get("http://127.0.0.1:5000/chat/user-chats",
                                params={"user_id": self.auth_data.id})
        messages = response.json()
        self.tableWidget.setRowCount(0)
        for message in messages:
            chat_id = message["id"]
            chat_name = message["name"]
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            self.tableWidget.setItem(row_position, 0, QTableWidgetItem(str(chat_id)))
            self.tableWidget.setItem(row_position, 1, QTableWidgetItem(chat_name))

    def open_chat(self, row, column):
        chat_id = int(self.tableWidget.item(row, 0).text())
        self.chat.append(ChatWindow(chat_id, self.auth_data))
        self.chat[-1].show()
