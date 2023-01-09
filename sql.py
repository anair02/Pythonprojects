import sqlite3

connection = sqlite3.connect("practice.db")

crsr = connection.cursor()

sql_command = """CREATE TABLE student (
std_id INTEGER PRIMARY KEY,
name VARCHAR(20),
gpa SINGLE PRECISION,
gender CHAR(1),);"""

insert_command = """INSERT INTO student (std_id, name, gpa, gender)
Values
(128, 'John', 3.46, 'M'),
(154, 'Maria', 3.8, 'F'), 
(165, 'Delia', 4.0, 'M')"""
crsr.execute(insert_command)

connection.close()