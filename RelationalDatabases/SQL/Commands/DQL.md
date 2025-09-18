- **[Data Query Language(DQL)]():** for retrieving data from the database
    - **SELECT:** To retrieve data from one or more tables


_______________________________________________________

# Select
- used to retrieve data from one or more tables in a database
- **FROM:** is mandatory and specifies the table(s) from which to retrieve the data
- can use expressions or functions in the SELECT clause, such as **COUNT(*)**, **SUM(column_name)**, or **column1 + column2**
- **DISTINCT:** keyword can be used to retrieve only unique values from a column, discarding duplicates

1. Selecting specific columns from a table
    - can list specific column names separated by commas
    ```
    SELECT column1, column2, ...
    FROM table_name;
    ```

2. Selecting all columns from a table
    - can use an asterisk (*) to select all columns from the specified table(s)
    ```
    SELECT *
    FROM tablename;
    ```

3. Selecting data with a **WHERE** clause
    - filters the rows based on specified conditions, returning only those that meet the criteria
    ```
    SELECT column1, column2
    FROM tablename
    WHERE condition;
    ```

4. Using **GROUP BY** and COUNT
    - clause groups rows that have the same values in specified columns into a summary row, often used with aggregate functions (e.g., COUNT, SUM, AVG)
    ```
    SELECT column1, COUNT(*) AS summaryRowName
    FROM tablename
    GROUP BY column1;
    ```

5. **ORDER BY:** Ordering the results
    - sorts the result set in ascending (ASC) or descending (DESC) order based on one or more columns
    ```
    SELECT column1, column2
    FROM tablename
    ORDER BY column1 ASC, column2 DESC;
    ```

6. **HAVING:**
    - filters the results of GROUP BY based on specified conditions for the aggregated data