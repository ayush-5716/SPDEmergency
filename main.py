from PyQt5.QtWidgets import QPushButton, QDialog, QApplication, QStackedWidget, QTableWidgetItem
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
        self.pushButton.clicked.connect(self.apply)

        name, email, phone = funcs.personal_info_fetch(rno)

        self.rno.setText(rno)
        self.nameT.setText(name)
        self.emailT.setText(email)
        self.phoneT.setText(phone)
    # TODO: apply in afterwards
    def goBack(self):
        widget.removeWidget(widget.currentWidget())

    def apply(self):
        funcs.personal_info_submit(rno, self.nameT.text(), self.phoneT.text(), self.emailT.text())


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
        self.myBooksButton.clicked.connect(self.goToMyBooks)
        self.libBooksbutton.clicked.connect(self.goToLibBooks)
        self.notifButton.clicked.connect(self.goToNotif)

    def goToNotif(self):
        N = notif_page()
        widget.addWidget(N)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goToLibBooks(self):
        LB = libBooks()
        widget.addWidget(LB)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goBack(self):
        widget.removeWidget(widget.currentWidget())

    def go_to_profile(self):
        profile_page_var = profile_page()
        widget.addWidget(profile_page_var)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goToMyBooks(self):
        my_books_page = myBP()
        widget.addWidget(my_books_page)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class notif_page(QDialog):
    def __init__(self):
        super(notif_page,self).__init__()
        uic.loadUi("UIPages/notifSet.ui",self)

        self.backButton.clicked.connect(self.goBack)

    def goBack(self):
        widget.removeWidget(widget.currentWidget())


class libBooks(QDialog):
    def __init__(self):
        super(libBooks,self).__init__()
        uic.loadUi("UIPages/libBooksPage.ui",self)

        self.backButton.clicked.connect(self.goBack)

    def goBack(self):
        widget.removeWidget(widget.currentWidget())


class myBP(QDialog):
    def __init__(self):
        super(myBP, self).__init__()
        uic.loadUi("UIPages/myBooksP.ui", self)

        self.backButton.clicked.connect(self.goBack)
        self.bookHistory.clicked.connect(self.goToBookHist)
        self.currBooks.clicked.connect(self.goToCurrBooks)
        self.remainders.clicked.connect(self.goToRemPage)

    def goBack(self):
        widget.removeWidget(widget.currentWidget())

    def goToBookHist(self):
        bH = bookHist()
        widget.addWidget(bH)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goToCurrBooks(self):
        currBS = currB()
        widget.addWidget(currBS)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def goToRemPage(self):
        RP = remPage()
        widget.addWidget(RP)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class remPage(QDialog):
    def __init__(self):
        super(remPage, self).__init__()
        uic.loadUi("UIPages/remPage.ui", self)

        self.backButton.clicked.connect(self.goBack)

    def goBack(self):
        widget.removeWidget(widget.currentWidget())


class currB(QDialog):
    def __init__(self):
        super(currB, self).__init__()
        uic.loadUi("UIPages/currBooks.ui", self)
        self.backButton.clicked.connect(self.goback)

    def goback(self):
        widget.removeWidget(widget.currentWidget())

    def load_data(self):
        books = funcs.current_books_fetch(rno)
        self.tableWidget.setRowCount(len(books))
        for row, book in enumerate(books):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(book[0]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(book[1]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(book[2])))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(book[3])))


class bookHist(QDialog):
    def __init__(self):
        super(bookHist, self).__init__()
        uic.loadUi("UIPages/bookHistory.ui", self)

        self.tableWidget.setColumnWidth(0, 160)
        self.load_data()
        self.backButton.clicked.connect(self.goBack)

    def goBack(self):
        widget.removeWidget(widget.currentWidget())

    def load_data(self):
        books = funcs.book_history_fetch(rno)
        self.tableWidget.setRowCount(len(books))
        for row, book in enumerate(books):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(book[0]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(book[1]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(book[2])))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(str(book[3])))


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
