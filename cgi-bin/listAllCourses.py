#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#!
import sqlite3
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

print("""Content-type:text/html\n\n
<!DOCTYPE html>
<head>
    <title> Course List </title>
</head>
<body>
    
    <h1> Course List </h1>
    """)

db_connection = sqlite3.connect('curricularUnits.db')
cursor = db_connection.cursor()
try:
    cursor.execute("SELECT * FROM Courses;")
    linhas = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM Courses;")
    nCourses = cursor.fetchone()
    cursor.execute("SELECT SUM(students_enrolled) FROM Courses;")
    sumStud = cursor.fetchone()
    cursor.execute("SELECT AVG(students_enrolled) FROM Courses;")
    avg = cursor.fetchone()
except sqlite3.Error as er:
	print('Error in SELECT: ', er)
    
print('<ul>')

for linha in linhas:
    print( '<li>' + str(linha[0]) + ' ' + linha[1] + ' ' + str(linha[2]) + '</li>')

print('</ul>')

print('<hr>')

print("<div>Number of courses:" + str(nCourses[0]) + "   Number of students:" + str(sumStud[0]) + "    Average number of students:" + str(avg[0]) + "</div>")

print('<hr>')

print("""</body> </html>""")

db_connection.commit()
db_connection.close()

