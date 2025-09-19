# Python: Relational Databases
- Python supports various databases, including relational databases like SQLite, MySQL, and PostgreSQL
- Learn more about working with databases in Python [here](https://github.com/shanreed25/Python/blob/main/BeyondBasics/databases/README.md)

## Workflow for Relational Databases
1. **Import the Database Driver**
- use specific library for your chosen database (e.g., sqlite3 for SQLite, mysql.connector for MySQL, psycopg2 for PostgreSQL).
2. **Establish a Connection**
- create a connection object that represents the link to your database
- typically involves providing credentials like host, user, password, and database name
3. **Create a Cursor**
- obtain a cursor object from the connection
- the cursor is used to execute SQL statements
4. **Execute SQL Queries**
- use the cursor's `execute()` method to run SQL commands like CREATE TABLE, INSERT, SELECT, UPDATE, and DELETE.
5. **Fetch Results (for SELECT queries)**
- if you execute a SELECT query, use methods like `fetchone()`, `fetchmany()`, or `fetchall()` on the cursor to retrieve the data.
6. **Commit Changes (for DML operations)**
- for INSERT, UPDATE, or DELETE operations, you must commit the changes to make them permanent using `connection.commit()`.
7. `Close Connection and Cursor`
- close the cursor and the connection to release resources

____________________________________

- see an example of using pyppyodbc [here](https://github.com/shanreed25/Python-Cheatsheet/blob/main/databaseconnections/SQL/pypyodbc-connection.py)