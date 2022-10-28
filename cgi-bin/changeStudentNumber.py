#!/usr/bin/env python3

from curses.ascii import isdigit
import sqlite3
import cgi
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("Content-type:text/html\n\n \
            <!DOCTYPE html> \
            <head> \
                <title>Change</title>\
            </head> \
            <body> ")
    
form = cgi.FieldStorage()

footer = """ <hr> 
<p> <a href="../index.html" > Return to main page </a> </p>
</body>
</html>"""


course_id = str(form["course_id"].value)
students_enrolled = str(form["students_enrolled"].value)

if ((course_id == "") or (students_enrolled == "")):
    print('<h2> Please fill in all the field </h2>')
    print(footer)
    sys.exit(-1)

if (not course_id.isdigit()) and (not students_enrolled.isdigit()): 
    print('<h2> Input [Course id AND Students enrolled] error, should be an integer </h2>')
    print(footer)
    sys.exit(-1)

if(not course_id.isdigit()):
    print('<h2> Input [Course id] error, should be an integer </h2>')
    print(footer)
    sys.exit(-1)


if(not students_enrolled.isdigit()):
    print('<h2> Input [Students enrolled] error, should be an integer </h2>')
    print(footer)
    sys.exit(-1)


db_connection = sqlite3.connect('curricularUnits.db')
cursor = db_connection.cursor()

try:
    cursor.execute('SELECT COUNT(*) FROM Courses WHERE course_id = ?', [course_id])
    n = cursor.fetchone()   # Check if user_id exists
    if (n[0] > 0):
        cursor.execute('UPDATE Courses SET students_enrolled = (?) WHERE course_id = (?)', (int(students_enrolled), int(course_id)))
        print("<h3> Course " + course_id + " number of students enrolled was set to " + students_enrolled + " </h3>")
    else:
        print("<h3> Course " + course_id + " does not exist </h3>")
except sqlite3.Error as er:
	print("<h3> UNEXPECTED ERROR " + str(er) + "</h3>")
db_connection.commit()
db_connection.close()

print(footer)