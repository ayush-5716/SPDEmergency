from PyQt5.QtWidgets import QPushButton,QDialog,QApplication,QStackedWidget
from PyQt5 import uic
import sys

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        uic.loadUi("UIPages/login.ui",self)
        


app = QApplication(sys.argv)
widget = QStackedWidget()
login = Login()
widget.addWidget(login)
widget.setFixedHeight(900)
widget.setFixedWidth(1200)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exit")