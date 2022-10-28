#!/usr/bin/env python3

import sqlite3
import cgi
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    
form = cgi.FieldStorage()

footer = """ <hr> 
<p> <a href="../index.html" > Return to main page </a> </p>
</body>
</html>"""


course_id = str(form["course_id"].value)
students_enrolled = str(form["students_enrolled"].value)


try:
    course_id = int(course_id)
except Exception as e:
    print('<h2> Input [Course id] error, should be an integer </h2> <p>')
    print(footer)

try:
    students_enrolled = int(students_enrolled)
except Exception:
    print('<h2> Input [Students enrolled] error, should be an integer </h2> <p>')
    print(footer)


db_connection = sqlite3.connect('curricularUnits.db')
cursor = db_connection.cursor()

try:
    cursor.execute('SELECT COUNT(*) FROM Courses WHERE course_id = ?', [course_id])
    n = cursor.fetchone()   # Check if user_id exists
    if (n[0] > 0):
        cursor.execute('UPDATE Courses SET students_enrolled = (?) WHERE course_id = (?)', (int(students_enrolled), int(course_id)))
        print("Content-type:text/html\n\n \
            <!DOCTYPE html> \
            <head> \
                <h3> Course " + str(course_id) + " number of students enrolled was set to " + str(students_enrolled) + " </h3> \
            </head> \
            <body> ")
    else:
        print("Content-type:text/html\n\n \
            <!DOCTYPE html> \
            <head> \
                <h3> Course " + str(course_id) + " does not exist </h3> \
            </head> \
            <body> ")
except sqlite3.Error as er:
	print("Content-type:text/html\n\n \
        <!DOCTYPE html> \
        <head> \
            <h3> UNEXPECTED ERROR " + str(er) + "</h3> \
        </head> \
        <body> ")
db_connection.commit()
db_connection.close()

print(footer)