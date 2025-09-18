- **[Data Definition Language(DDL)]():** for defining and modifying the database structure
    - **CREATE:** To create database objects like tables, views, indexes.
    - **ALTER:** To modify the structure of existing database objects.
    - **DROP:** To delete database objects.
    - **TRUNCATE:** To remove all records from a table, including space allocated for the records, but not the table structure itself.
    - **RENAME:** To rename a database object.


_______________________________________________________

# CREATE
- define and create new database objects
1. Creating a Database
    - `CREATE DATABASE db_name;`

2. Creating a Table
    - define and create a new table within a database 
    - specify the table name, column names, their data types, and any constraints
    ```
    CREATE TABLE table_name (
        column1 datatype [constraints],
        column2 datatype [constraints],
        ...
        columnN datatype [constraints]
    );
    ```

3. Creating an Index
    - used to create indexes on tables to improve the performance of data retrieval
    - indexes speed up data retrieval, they can add overhead to data modification operations (inserts, updates, deletes) as the index also needs to be updated
    - indexes should be created strategically on columns frequently used in WHERE clauses or JOIN conditions
        ```
        CREATE INDEX index_name
        ON table_name (column1, column2, ...);
        ```

# TRUNCATE
- `TRUNCATE TABLE table_name;`
- refers primarily to the TRUNCATE TABLE statement, which is used to quickly remove all rows from a table while preserving its structure
- is a Data Definition Language (DDL) operation in some database systems and a Data Manipulation Language (DML) operation in others, but its effect is to empty the table
- generally faster and uses fewer system and transaction log resources than DELETE without a WHERE clause
- TRUNCATE TABLE deallocates data pages and logs fewer individual row deletions
- **Logging:**  performs minimal logging, which contributes to its speed.
- **Rollback:** in most database systems, TRUNCATE TABLE cannot be rolled back if executed outside of an explicit transaction. Even within a transaction, its rollback behavior can differ from DELETE.
- **Triggers:** does not fire DELETE triggers, unlike the DELETE statement.
- **Identity Columns:** often resets identity (auto-incrementing) columns to their seed value, whereas DELETE does not.
- **Permissions:** specific permissions are required to execute TRUNCATE TABLE, which may differ from those required for DELETE.

# DROP
- `DROP TABLE tablename`
- deletes entire table

# ALTER
- allows for various changes, including adding, deleting, or modifying columns, as well as managing constraints

1. Adding Column
    ```
    ALTER TABLE table_name
    ADD column_name datatype;
    ```

2. Deleting a column
    ```
    ALTER TABLE table_name
    DROP COLUMN column_name;
    ```

3. Modifying a Column's Data Type or Size
    - Syntax may vary slightly between database systems like MySQL, SQL Server, PostgreSQL, Oracle
    - PostgreSQL
        ```
        ALTER TABLE table_name
        ALTER COLUMN column_name TYPE new_datatype;
        ```
    - MySQL
        ```
        ALTER TABLE table_name
        MODIFY COLUMN column_name TYPE new_datatype;
        ```
    - SQL Server
        ```
        ALTER TABLE table_name
        ALTER COLUMN column_name new_datatype;
        ```

4. Adding a Constraint
    ```
    ALTER TABLE table_name
    ADD CONSTRAINT constraint_name constraint_type (column_name);
    ```

5. Dropping a Constraint
    ```
    ALTER TABLE table_name
    DROP CONSTRAINT constraint_name;
    ```

6. Renaming a Table
    - MySQL/PostgreSQL/Oracle/SQLite
        ```
        ALTER TABLE old_table_name
        RENAME TO new_table_name;
        ```
    - SQL Server (using sp_rename)
        - `EXEC sp_rename 'old_table_name', 'new_table_name';`

7. Renaming a Column
    - MySQL
        ```
        ALTER TABLE table_name
        CHANGE old_column_name new_column_name datatype;
        ```
    - PostgreSQL
        ```
        ALTER TABLE table_name
        RENAME COLUMN old_column_name TO new_column_name;
        ```
    - SQL Server
        ```
        EXEC sp_rename 'table_name.old_column_name', 'new_column_name', 'COLUMN';
        ```