# 🛞 Relational Databases
- store and organize data in structured tables with pre-defined relationships, using a tabular format of rows and columns to represent records and attributes
- managed by a Relational Database Management System (RDBMS), which allows users to define, query, and manipulate data using structured query language (SQL)
- maintains data integrity through transactions and ensures relationships between different tables are robust and accessible
    - robust: strong, reliable, and performs well under various conditions, including errors, invalid inputs, and environmental changes, minimizing failures and ensuring consistent functionality and security for users
- normalization, which involves organizing data in a way that reduces redundancy and improves data integrity within the database

### 📍 Where are they located?
**Relational Databases can be located in various places, including on local servers, in desktop applications, or within cloud-based systems offered by providers like Amazon Web Services, Google Cloud, and Microsoft Azure**
- **On-Premises/Local Systems:** can be hosted on dedicated hardware within an organization's own data centers or on individual personal computers for smaller applications. 
- **Desktop Applications:** some desktop applications, such as Microsoft Access, use relational database models to store and manage data locally. 
- **Cloud-Based Services:** major cloud providers offer managed relational database services, making them accessible and scalable for applications hosted in the cloud. 
- **Web Applications and Websites:** many websites and online applications rely on relational databases to store user data, product catalogs, and order information. 

### 📔 How Relational Databases Work
- **Tables (or Relations):** data is stored in tables, each designed around a single entity (like a customer or a product). 
- **Columns (Attributes):** each table has columns that define specific data attributes, such as a customer's "name" or "address". 
- **Rows (Tuples):** each row in a table represents a single instance of that data, like a specific customer's information. 
- **Relationships:** tables are connected through defined relationships, often by using unique identifiers (like a customer ID) in multiple tables. This allows users to link and combine data from different tables to gain insights.

- [SQL](./SQL/README.md)
- [SQL: Python](./Python/README.md)