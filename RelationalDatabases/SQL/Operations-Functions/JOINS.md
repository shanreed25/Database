# JOIN clauses
- used to combine columns from two or more tables based on a related column between them
- essential for querying relational databases where data is spread across multiple tables
- TABLE BEFORE JOIN IS LEFT TABLE
- TABLE AFTER JOIN IS RIGHT TABLE

## Types of JOINs
- **JOIN or INNER JOIN:**
    - returns only the rows where there is a match in both tables based on the join condition
- **LEFT (OUTER) JOIN:** 
    - returns all rows from the left table, and the matching rows from the right table
    - if no match is found in the right table, NULL values are returned for the right table's columns
- **RIGHT (OUTER) JOIN:**
    - returns all rows from the right table, and the matching rows from the left table
    - if no match is found in the left table, NULL values are returned for the left table's columns.
- **FULL (OUTER) JOIN:**
    - returns all rows from both tables, with NULL values for columns where no match is found in the other table.
- **CROSS JOIN:**
    - returns the Cartesian product of the two tables, meaning every row from the first table is combined with every row from the second table


SELECT c.customer_name, o.order_date, p.product_name
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Products p ON o.product_id = p.product_id;


In this example, the Customers table is joined with Orders, and then the result is joined with Products to retrieve customer names, order dates, and product names for each order. You can chain multiple JOIN clauses to connect more than two tables.