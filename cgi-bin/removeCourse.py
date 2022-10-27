#!/usr/bin/env python3

import sqlite3
import cgi
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    
form = cgi.FieldStorage()

course_id = str(form["course_id"].value)

db_connection = sqlite3.connect('curricularUnits.db')
cursor = db_connection.cursor()
cursor.execute("SELECT COUNT(*) FROM Courses WHERE course_id = ?;", [course_id])
nC = cursor.fetchone()
try:
    if(nC[0] > 0):
        cursor.execute('DELETE FROM Courses WHERE course_id = ?', [course_id])
        print("Content-type:text/html\n\n \
            <!DOCTYPE html> \
            <head> \
                <h3> Course " + course_id + " was removed</h3> \
            </head> \
            <body> ")
    else:
        print("Content-type:text/html\n\n \
            <!DOCTYPE html> \
            <head> \
                <h3> Course " + course_id + " doesn't exist </h3> \
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