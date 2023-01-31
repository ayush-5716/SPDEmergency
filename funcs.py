import mysql.connector
import hashlib
import datetime
import random
import smtplib
import math

db = mysql.connector.connect(host="localhost", username="root", password="sqlsme", database="library")
cr = db.cursor()


def library_status():
    return 8 < datetime.datetime.now().hour < 20


def time_right_now():
    return datetime.datetime.now().strftime("%X")

#penalty
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
    cr.execute("SELECT name, mail_id FROM users WHERE reg_no=%s", (user_id,))
    return user_id, *cr.fetchone()


def personal_info_submit(user_id, name, mail):
    cr.execute("UPDATE users SET name=%s, mail_id=%s WHERE reg_no=%s", (name, mail, user_id))
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
