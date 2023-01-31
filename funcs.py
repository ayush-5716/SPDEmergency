import mysql.connector
import hashlib
import datetime
import random
import smtplib
import json

db = mysql.connector.connect(host="localhost", username="root", password="sqlsme", database="library")
cr = db.cursor()


def auto_library_status():
    return 8 < datetime.datetime.now().hour < 20


def time_right_now():
    return datetime.datetime.now().strftime("%X")


def login_check(user_id, password):
    cr.execute("SELECT reg_no FROM users WHERE reg_no=%s", (user_id,))
    if cr.fetchone():
        cr.execute("SELECT password FROM users WHERE reg_no=%s", (user_id,))
        hashed = hashlib.sha256(password.encode()).hexdigest()
        if hashed == cr.fetchone()[0]:
            return 0
        else:
            return 1
    else:
        return 2


def personal_info_fetch(user_id):
    cr.execute("SELECT name, phone_number, mail_id FROM users WHERE reg_no=%s", (user_id,))
    return user_id, *cr.fetchone()


def personal_info_submit(user_id, name, phone, mail):
    cr.execute("UPDATE users SET name=%s, phone_number=%s, mail_id=%s WHERE reg_no=%s", (name, phone, mail, user_id))
    db.commit()


def new_user(user_id, password):
    cr.execute("INSERT INTO users (reg_no, password) VALUES (%s, %s)", (user_id, password))
    db.commit()


def generate_otp():
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = ""
    for i in range(6):
        OTP += string[random.choice(string)]
    return OTP
    # TODO: Implement json file for sender mail


def send_otp():
    # TODO
    pass


def table_for_user(user_id):
    cr.execute(f"create table {user_id}_bh (book_id varchar(15) primary key, book_name varchar(256), \
date_of_borrowed date, date_of_return date)")
    db.commit()


def book_history_fetch(user_id):
    # TODO: Add in sign in page
    cr.execute(f"SELECT * FROM {user_id}_bh")
    return cr.fetchall()


def current_books_fetch(user_id):
    val = (user_id,)
    cr.execute(f"SELECT book1, date1, book2, date2, book3, date3 FROM users WHERE reg_no=%s", val)
    books_list = []
    data = cr.fetchone()
    for i in range(0, 6, 2):
        if data[i] is not None:
            cr.execute("SELECT book_name FROM books WHERE book_id=%s", (data[i],))
            name = cr.fetchone()[0]
            re = str(data[i+1] + datetime.timedelta(weeks=1))
            books_list.append((data[i], name, str(data[i+1]), re))


def wish_book_ids_fetch(user_id):
    with open("wishlist.json", 'r') as f:
        d = json.load(f)
        book_list = d[user_id]
        return book_list


def wish_list_fetch(user_id):
    book_infos = []
    for book_id in wish_book_ids_fetch(user_id):
        cr.execute("SELECT book_name, author FROM book_id=%s", (book_id,))
        x = cr.fetchone()
        book_infos.append((book_id, x[0], x[1]))
    return book_infos
