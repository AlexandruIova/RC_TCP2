#!/usr/bin/env python3

import sqlite3
import cgi
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print("""Content-type:text/html\n\n
<!DOCTYPE html>
<head>
    <title> New course </title>
</head>
<body> """)

errc = 0   
form = cgi.FieldStorage()

footer = """  <p> <a href="../index.html" > Return to main page </a> </p>     
</body> 
</html>"""

course_id = str(form["course_id"].value)
name = str(form["name"].value)
students_enrolled = str(form["students_enrolled"].value)

if ((course_id == "") or (name == "") or (students_enrolled == "")):
    print('<h2> Please fill in all the field </h2>')
    print(footer)
    sys.exit(-1)

if ((not course_id.isdigit() and (not students_enrolled.isdigit()))):
    print('<h2> Input [Course id AND Students enrolled] error, should be an integer </h2>')
    print(footer)  
    sys.exit(-1)

if not course_id.isdigit():
    print('<h2> Input [Course id] error, should be an integer </h2>')
    print(footer)  
    sys.exit(-1)

if not students_enrolled.isdigit():
    print('<h2> Input [Students enrolled] error, should be an integer </h2>')
    print(footer)  
    sys.exit(-1)

db_connection = sqlite3.connect('curricularUnits.db')
cursor = db_connection.cursor()

try:
    cursor.execute('INSERT INTO Courses VALUES( ?, ?, ?);' , \
               	( int(course_id), name, int(students_enrolled)))
except sqlite3.Error as er:
	print('Error in INSERT: ', er)
	errc = er
db_connection.commit()
db_connection.close()

if(errc==0):
    print('<h2> A new course was added ' + \
    str(course_id) + ', ' + name + '</h2> <p>')
print(footer)

