#  Summary of Lecture 7.4 - Application Design and Development4.pdf 
**Summary**
**Module 34: Application Design and Development/4: Python and PostgreSQL**

**Objectives**

* To understand how to access PostgreSQL database from Python
* To understand Python Web Application with PostgresSQL

**Outline**

* Accessing PostgreSQL from Python
* Developing Web Application with Python

**Working with PostgreSQL and Python**

**Python Modules for PostgreSQL**

* psycopg2
* pg8000
* py-postgresql
* PyGreSQL
* ocpgdb
* bpgsql
* SQLAlchemy (needs any of the above to be installed separately)

**Package psycopg2**

* Advantages of psycopg2
    * Most popular and stable module to work with PostgreSQL
    * Used in most of the Python and Postgres frameworks
    * An actively maintained package and supports Python 2.x and 3.x
    * Thread-safe and designed for heavily multi-threaded applications.

**Steps to access PostgresSQL from Python**

1. Create connection
2. Create cursor
3. Execute the query
4. Commit/rollback
5. Close the cursor
6. Close the connection

**Python psycopg2 Module APIs: connection objects**

* psycopg2.connect(database="mydb", user="myuser", password="mypass"
host="127.0.0.1", port="5432")
This API opens a connection to the PostgreSQL database. If database is opened
successfully, it returns a connection object.
* connection.close()
This method closes the database connection.

**Important psycopg2 module routines for managing cursor object:**

* connection.cursor()
This routine creates a cursor which will be used throughout the program.
* cursor.close()
This method closes the cursor.

**Python psycopg2 Module APIs: insert, delete, update & stored procedures**

* cursor.execute(sql [, optional parameters])
This routine executes an SQL statement. The SQL statement may be parameterized
(i.e., placeholders instead of SQL literals). The psycopg2 module supports placeholder
using %s sign. For example: cursor.execute("insert into people values (%s,\r\n
%s)", (who, age))
* cursor.executemany(sql, seq of parameters)
This routine executes an SQL command against all parameter sequences or mappings
found in the sequence SQL.
* cursor.callproc(procname[, parameters])
This routine executes a stored database procedure with the given name. The sequence
of parameters must contain one entry for each argument that the procedure expects.
* cursor.rowcount
This is a read-only attribute which returns the total number of database rows that have
been modified, inserted, or deleted by the last execute().

**Python psycopg2 Module APIs: select**

* cursor.fetchone()
This method fetches the next row of a query result set, returning a single sequence, or
None when no more data is available.
* cursor.fetchmany([size=cursor.arraysize])
This routine fetches the next set of rows of a query result, returning a list. An empty list
is returned when no more rows are available. The method tries to fetch as many rows as
indicated by the size parameter.
* cursor.fetchall()
This routine fetches all (remaining) rows of a query result, returning a list. An empty
list is returned when no rows are available.

**Python psycopg2 Module APIs: commit & rollback**

* connection.commit()
This method commits the current transaction. If you do not call this method, anything
you did since the last call to commit() is not visible to other database connections.
* connection.rollback()
This method rolls back any changes to the database since the last call to commit().

**Connect to a PostgreSQL Database Server**

```python
import psycopg2

def connectDb(dbname, usrname, pwd, address, portnum):
    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(database = dbname, user = usrname, \
                            password = pwd, host = address, port = portnum)
        print ("Database connected successfully")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close() # close the connection

connectDb("mydb", "myuser", "mypass", "127.0.0.1", "5432") # function call
```

**Steps to execute SQL commands**

1. Use the psycopg2.connect() method with the required arguments to connect Post
gresSQL. It would return an Connection object if the connection established successfully.
2. Create a cursor object using the cursor() method of connection object.
3. The execute() methods run the SQL commands and return the result.
4. Use cursor.fetchall() or fetchone() or fetchmany() to read query result.
5. Use commit() to make the changes in database persistent, or use rollback() to revert
the database changes.
6. Use cursor.close() and connection.close() method to close the cursor and Post
gresSQL connection.

**CREATE new PostgreSQL tables**

```python
import psycopg2

def createTable():
    conn = None
    try:
        conn = psycopg2.connect(database = "mydb", user = "myuser", \
                            password = "mypass", host = "127.0.0.1", port = "5432") # connect to the database
        cur = conn.cursor() # create a new cursor
        cur.execute('''CREATE TABLE EMPLOYEE \
    (emp_num INT PRIMARY KEY NOT NULL, \
    emp_name VARCHAR(40) NOT NULL, \
    department VARCHAR(40) NOT NULL)''') # execute the CREATE TABLE statement
        conn.commit() # commit the changes to the database
        print ("Table created successfully")
        cur.close() # close the cursor
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close() # close the connection

createTable() #function call
```

**Executing INSERT statement from Python**

```python
import psycopg2

def insertRecord(num, name, dept):
    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(database = "mydb", user = "myuser", \
                            password = "mypass", host = "127.0.0.1", port = "5432")
        cur = conn.cursor() # create a new cursor
        # execute the INSERT statement
        cur.execute("INSERT INTO EMPLOYEE (emp_num, emp_name, department) \
VALUES (%s, %s, %s)", (num, name, dept))
        conn.commit() # commit the changes to the database
        print ("Total number of rows inserted :", cur.rowcount);
        cur.close() # close the cursor
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close() # close the connection

insertRecord(110, ‘Bhaskar’, ’HR’) #function call
```

**Executing DELETE statement from Python**

```python
import psycopg2

def deleteRecord(num):
    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(database = "mydb", user = "myuser", \
                            password = "mypass", host = "127.0.0.1", port = "5432")
        cur = conn.cursor() # create a new cursor
        # execute the DELETE statement
        cur.execute("DELETE FROM EMPLOYEE WHERE emp_num = %s", (num,))
        conn.commit() # commit the changes to the database
        print ("Total number of rows deleted :", cur.rowcount)
        cur.close() # close the cursor
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close() # close the connection

deleteRecord(110) #function call
```

**Executing UPDATE statement from Python**

```python
import psycopg2

def updateRecord(num, dept):
    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(database = "mydb", user = "myuser", \
                            password = "mypass", host = "127.0.0.1", port = "5432")
        cur = conn.cursor() # create a new cursor
        # execute the UPDATE statement
        cur.execute("UPDATE EMPLOYEE set department = %s where emp_num = \
%s", (dept, num))
        conn.commit() # commit the changes to the database
        print ("Total number of rows updated :", cur.rowcount)
        cur.close() # close the cursor
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close() # close the connection

updateRecord(110, "Finance") #function call
```

**Executing SELECT statement from Python**

```python
import psycopg2

def selectAll():

