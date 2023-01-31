from PyQt5.QtWidgets import QPushButton,QDialog,QApplication,QStackedWidget
from PyQt5 import uic
import sys

import funcs


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi("UIPages/login.ui", self)

        self.login_button.clicked.connect(self.go_to_homepage)
        
    def go_to_homepage(self):
        global rno
        rno = self.usernameText.text()
        if funcs.login_check(rno, self.passwordText.text()):
            home_p = home_page()
            widget.addWidget(home_p)
            widget.setCurrentIndex(widget.currentIndex() + 1)


class editProfileP(QDialog):
    def __init__(self):
        super(editProfileP, self).__init__()
        uic.loadUi("UIPages/profileEditPage.ui", self)
        self.backButton.clicked.connect(self.goBack)

    def goBack(self):
        widget.removeWidget(widget.currentWidget())


class profile_page(QDialog):
    def __init__(self):
        super(profile_page, self).__init__()
        uic.loadUi("UIPages/profilepage.ui", self)

        self.backButton.clicked.connect(self.goBack)
        self.editprofile.clicked.connect(self.goToEditPage)

        name, email, phone = funcs.personal_info_fetch(rno)

        self.rno.setText(rno)
        self.name.setText(name)
        self.email.setText(email)
        self.phone.setText(phone)

    def goBack(self):
        widget.removeWidget(widget.currentWidget())

    def goToEditPage(self):
        eP = editProfileP()
        widget.addWidget(eP)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class home_page(QDialog):
    def __init__(self):
        super(home_page, self).__init__()
        uic.loadUi("UIPages/homepage.ui", self)

        self.logOut.clicked.connect(self.goBack)
        self.profileButton.clicked.connect(self.go_to_profile)
    
    def goBack(self):
        widget.removeWidget(widget.currentWidget())

    def go_to_profile(self):
        profile_page_var = profile_page()
        widget.addWidget(profile_page_var)
        widget.setCurrentIndex(widget.currentIndex() + 1)


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
