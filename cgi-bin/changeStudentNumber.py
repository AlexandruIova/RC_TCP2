#!/usr/bin/env python3

import sqlite3
import cgi
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    
form = cgi.FieldStorage()

course_id = str(form["course_id"].value)
students_enrolled = str(form["students_enrolled"].value)

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
                <h3> Course " + course_id + " number of students enrolled was set to " + students_enrolled + " </h3> \
            </head> \
            <body> ")
    else:
        print("Content-type:text/html\n\n \
            <!DOCTYPE html> \
            <head> \
                <h3> Course " + course_id + " does not exist </h3> \
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

print('<hr>')
print("""  <p> <a href="../index.html" > Return to main page </a> </p>
</body>
</html>""")