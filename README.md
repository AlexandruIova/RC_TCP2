# RC_TCP2

## SQLite
Basic information on how to use SQLite can be found [here](https://www.sqlite.org/cli.html):

## webServer.py
The server is the same used in Lab05. Nothing changed.

### 2.1 Adding courses to database
Just took `newEmpoyee.py` from Lab05 file and adapted it adding error messages. 

### 2.2 List information about all courses
Took `contactList.py` from Lab05 file and adapted it adding more SQL commands.


### 2.3 Deleting a course from the database
The usual command from deleting something from SQLite is:
`DELETE FROM table WHERE condition;`
With `try()...except` I handle the case in which there are no courses with that Id.
Nota: per concatenare con le funzioni di python bisogna che le variabili siano array/liste.

### 2.4 Change the number of students enrolled in a course
I first check if user_id exists and then I run the command. Otherwise the command would not give an error and I won't be able to catch it.

### 2.5 List information about all the courses (JavaScript Version)
Understood very little tbh but made it work.
As far as I understood AJAX makes so that the result will be in a "narrower" box but treated as a full page I guess.

## TODO
- [x] Change port to student's number
- [x] 2.2 handle the case where there are no courses in the database.
- [x] error cases
- [x] 2.3 fix problem removeCourse (if there's no element it tells removed)
- [x] Fix newCourse.py 