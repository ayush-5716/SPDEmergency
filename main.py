from PyQt5.QtWidgets import QPushButton,QDialog,QApplication,QStackedWidget
from PyQt5 import uic
import sys

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        uic.loadUi("UIPages/login.ui",self)

        self.login_button.clicked.connect(self.go_to_homepage)

    def go_to_homepage(self):
        home_p = home_page()
        widget.addWidget(home_p)
        widget.setCurrentIndex(widget.currentIndex() + 1)




class home_page(QDialog):
    def __init__(self):
        super(home_page,self).__init__()
        uic.loadUi("UIPages/homepage.ui",self)

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