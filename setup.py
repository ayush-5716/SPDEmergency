import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="sqlsme")
cr = db.cursor()

cr.execute(
    """create database library;
use library;

create table users(
reg_no varchar(20) primary key,
password char(64) not null,
name varchar(30),
mail_id varchar(40),
book1 varchar(15),
date1 date,
book2 varchar(15),
date2 date,
book3 varchar(15)
date3 date);

create table books(
book_id varchar(15) primary key,
wished_people varchar(40),
copies int not null,
book_name varchar(256),
author varchar(30),
category varchar(20),
hotness int);"""
)

db.close()