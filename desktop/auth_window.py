import requests
from PyQt5.QtWidgets import QDialog, QLineEdit

from desktop.ui.ui_auth import Ui_Dialog


class AuthWindow(QDialog, Ui_Dialog):
    def __init__(self, auth_data):
        super().__init__()
        self.setupUi(self)
        self.line_edit_password.setEchoMode(QLineEdit.Password)
        self.pushButton.clicked.connect(self.login)
        self.auth_data = auth_data

    def login(self):
        login = self.line_edit_login.text()
        password = self.line_edit_password.text()
        response = requests.post("http://127.0.0.1:5000/user/sign-in",
                                 params={"login": login,
                                         "password": password})
        if response.status_code == 200:
            self.auth_data.append(response.json())
            self.close()
        else:
            print(response.json())
