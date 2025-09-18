# SQL: Python
- Python supports various databases, including relational databases like SQLite, MySQL, and PostgreSQL

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

## Choosing a database connector library
**Choosing a database connector library in Python depends on the specific database being used and the project's requirements**
- you can choose a **Database-Specific Connector** or **Object-Relational Mappers (ORMs)**, each represent different levels of abstraction for interacting with relational databases in Python
- choice depends on project requirements, team expertise, and the complexity of database interactions
- Connectors offer maximum control and performance tuning potential
- ORMs prioritize developer productivity and code maintainability, especially for applications with extensive CRUD operations
- a hybrid approach, where an ORM handles most interactions and raw SQL is used for specific performance-critical or complex queries, provides a balanced solution

### Database-Specific Connectors
- libraries that provide a direct, low-level interface for connecting to and interacting with a specific type of database such as  psycopg2 for PostgreSQL, PyMySQL for MySQL, or sqlite3 for SQLite
- typically adhere to the Python DB-API specification
- allow you to write raw SQL queries and use the connector's API to execute these queries, fetch results, and manage connections and transactions
- allows for granular control over SQL queries and database operations, allowing for fine-tuned performance optimization and handling of complex, database-specific features
- requires a good understanding of SQL and the specific database's dialect
- Easier to optimize complex queries manually but can be slower for common CRUD operations
- requires changing code for different databases


### Object-Relational Mappers (ORMs)
- provide a higher level of abstraction, allowing developers to interact with the database using object-oriented programming concepts (classes, objects) to map database tables to Python objects rather than raw SQL
- for more complex applications
- popular Python ORMs include SQLAlchemy, Django ORM, and Peewee
- allow you to define database tables as Python classes and manipulate records as objects
    - the ORM translates these object-oriented operations into SQL queries behind the scenes
- reduces boilerplate SQL code and allows developers to work primarily within their chosen programming language's paradigm
- can accelerate development, improve code readability and maintainability, and help prevent SQL injection vulnerabilities through parameterized queries
- introduce a learning curve for the ORM itself, may generate less optimized SQL for complex queries, and can sometimes obscure the underlying database operations
- faster for common CRUD operations and generates SQL automatically
- more aligned with object-oriented code and can abstract away database specifics (with ORM support)


### Considerations for Choosing:
- **Database Compatibility:** Ensure the chosen library explicitly supports the target database.
- **Ease of Use:** Consider the learning curve and developer experience provided by the library's API.
- **Features:** Evaluate if the library offers necessary features like connection pooling, transaction management, or ORM capabilities.
- **Performance:** For high-performance applications, consider the library's efficiency and potential for optimization.
- **Community Support and Documentation:** A well-supported library with good documentation can significantly aid development and troubleshooting.
- **Project Scale and Complexity:** For simple scripts, a direct connector might suffice, while larger, more complex applications might benefit from an ORM like SQLAlchemy.