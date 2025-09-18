# SQL Aggregation
- performing calculations on a set of values (rows) to return a single summary value
- is achieved using SQL aggregate functions, which are often used in conjunction with the GROUP BY clause
- GROUP BY clause is used to group rows that have the same values in specified columns into summary rows
    - Aggregate functions then operate on each of these groups independently, returning a single aggregated result for each group
- Most aggregate functions ignore NULL values, with the exception of COUNT(*)
- can be combined with other SQL clauses like HAVING (for filtering groups based on aggregate conditions)
#### Common SQL Aggregate Functions:
- **COUNT():** Returns the number of rows in a set. COUNT(*) counts all rows, while COUNT(column_name) counts non-NULL values in a specific column
- **SUM():** Calculates the total sum of values in a numerical column
- **AVG():** Calculates the average value of a numerical column
- **MIN():** Returns the smallest value within a selected column
- **MAX():** Returns the largest value within a selected column



