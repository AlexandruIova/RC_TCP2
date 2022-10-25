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
Nota: per concatenare con le funzioni di python bisogna che le variabili siano liste.