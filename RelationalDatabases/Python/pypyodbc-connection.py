import pypyodbc as odbc
# TODO 1: Import Database Driver: pip install pypyodbc---------------------------------------------------------------------------------------------------
    # To connect to a database, we need a database driver, without a driver, we cannot establish a connection to the database.
    # pypyodbc module is used to connect to the SQL Server database, it is a pure Python ODBC module that allows you to connect to ODBC databases
        # provides a way to interact with the database using Python, and is compatible with Python 2 and 3, and it works on Windows, Linux, and macOS
        # is similar to pyodbc, but it is written in pure Python and does not require any C extensions
        # not as fast as pyodbc, but it is easier to install and use
    # without pypyodbc, you would need to install the ODBC driver for your database and configure it properly
    #


#----------------------------------------------------------------------------------------------------------------------------------------------

#TODO 2: Establish a Connection: Connection String
    # A connection string is needed to establish a connection, without a connection string, the application would not know how to connect to the database
    # a connection string is a string that specifies information about a data source and the means of connecting to it
    # the format of a connection string can vary depending on the database and the driver being used.
    # To connect to a SQL Server database using pypyodbc, you need to provide the following information a the connection string:
        # Driver Name
        # Server Name
        # Database Name

# Sync Connection Variables
DRIVER_NAME = 'SQL SERVER'
# driver name can be found in the ODBC Data Source Administrator tool on Windows
# is usually listed under the "Drivers" tab
# Common driver names for SQL Server include "SQL Server", "ODBC Driver 17 for SQL Server", and "ODBC Driver 18 for SQL Server"
SERVER_NAME = 'SHANNONHP\MSSQLSERVER01'
# server name can be found in SQL Server Management Studio (SSMS) when you connect to the database
# is usually in the format "hostname\instance_name" or just "hostname" if you are using the default instance
DATABASE_NAME = 'VeganRecipes'
# database name can be found in SQL Server Management Studio (SSMS) under the "Databases" node in the Object Explorer
# is the name of the specific database you want to connect to.

# Connection String: Specify the driver, server and database names
connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""
# Trust_Connection=yes; is used to enable Windows Authentication for the connection
# this means that the connection will use the credentials of the currently logged-in Windows 
# user to authenticate with the SQL Server database, rather than requiring a separate username and password
# this is often used in environments where security policies prefer integrated authentication methods.
# If you want to use SQL Server Authentication instead, you would replace Trust_Connection=yes; 
# with UID=your_username;PWD=your_password; in the connection string.
# Windows Authentication is generally considered more secure as it leverages the existing Windows security infrastructure,
#  while SQL Server Authentication can be more flexible in certain scenarios where Windows accounts are not available or practical to use.

#----------------------------------------------------------------------------------------------------------------------------------------------

# TODO 3: Establish a Connection: Connection Object
    # Without a connection object, you cannot interact with the database
    # the connect() method establishes the connection to the database and returns a connection object that represents the connection
    # the connection should be established once and reused throughout the application
    # this approach improves performance and resource utilization
    # once you have a connection object, it provides methods to create cursors, manage transactions, and close the connection
    # it is essential for executing SQL queries and commands against the database
    # the connect() method can take various parameters such as driver, server, database, user, password, etc.
    # depending on the database and the authentication method used
    # in this example, the connection string is used to specify the connection parameters
    # in a real-world application, consider using environment variables or configuration files
    # to manage sensitive information like database credentials
    # also, consider using error handling to manage connection failures gracefully
    # while this example uses a single connection for simplicity,
    # it is recommended to use a connection pool for better performance and resource management
    # without connection pooling, this is not suitable for a high-traffic web application
    # because it can lead to connection exhaustion and performance issues
    # in a real-world application, consider using a connection pool like `sqlalchemy` or `DBUtils`
    # to manage database connections efficiently


#connect function
conn = odbc.connect(connection_string)
    # typically has methods such as cursor(), commit(), rollback(), close(),
    # and properties like autocommit, dsn, and timeout
    # commit() is used to save changes made during a transaction, 
    # rollback() is used to undo changes made during a transaction,
   

print(conn)#print to see if the connection is successful
#----------------------------------------------------------------------------------------------------------------------------------------------
# TODO 4: Create a cursor object
    # the connection object has a method called cursor() that creates a cursor object
    #cursor() method-----------------------------------------------------------------------------------------------------
        # used to create a cursor object for executing SQL queries,
        # conn.cursor() returns a new cursor object using the connection, so they are created by the connection object
        # Multiple cursors can be created from a single connection
cursor = conn.cursor()#memory space

    #cursor object------------------------------------------------------------------------------------------------------------
        # Cursors are not thread-safe, so they should not be shared between threads
            # a thread is a separate flow of execution, meaning that your program can perform multiple operations at once
            # thread-safe, means that multiple threads can access the same resource without causing data corruption or inconsistency
            # in a web application, each request is handled by a separate thread

        # Creating a new cursor for each request is a good practice in web applications
            # Since each request to the server is handled by a separate thread, and cursors are not thread-safe
            # this ensures that each request is handled independently, so that one request does not interfere with another
        
        # THE CURSOR BEFORE EXECUTING A QUERY
            # at this point the cursor is just a pointer to the database
            # but once a query is executed it moves the cursor to the first row of the results

#----------------------------------------------------------------------------------------------------------------------------------------------

#TODO 5: Execute SQL Queries
# Execute SQL commands---------------------------------------------------------------
    # Once you have a cursor, you can execute SQL queries to interact with the database.
    # using the execute() method of the cursor object, you can run SQL commands
    # the execute() method returns a cursor object that can be iterated over to access the results
        # the execute method returns the cursor itself
    # THE CURSOR AFTER EXECUTING A QUERY
        # at this point the cursor is positioned at the first row of the result set
            # once a query is executed 
                # the cursor is moved from pointing to the database
                # and moved to the first row of the results



recipes_cursor = cursor.execute("SELECT * FROM recipes")# send SQL command to the execute function
#recipes_cursor is just a cursor object(<pypyodbc.Cursor object at 0x0000023F2B1C8>B80>), not the actual data
#----------------------------------------------------------------------------------------------------------------------------------------------
#TODO 6: Get Data
    #cursor can be iterated over directly in a for loop
    # for row in cursor:
    #     print(row)
     # this will print each row in the result set as a tuple
        # but there are other ways to get the data from the cursor
        #recipes_cursor.fetchone() will return the next row in the result set as a tuple
        #recipes_cursor.fetchall() will return a list of all rows in the result set
        #recipes_cursor.fetchmany(size) will return a list of the next 'size' rows in the result set
        #these methods allow you to retrieve data from the cursor in different ways, depending on your needs
#----------------------------------------------------------------------------------------------------------------------------------------------
# After executing a SQL query, you can use the fetchone(), fetchall(), or fetchmany() methods of the cursor object to retrieve the results of the query

# fetchmany()------------------------------------------------------------------------------------------------------------------
# fetchmany() method retrieves a specified number of rows from the result set
# it takes an optional parameter size that specifies the number of rows to fetch
# if size is not provided, it defaults to 1, meaning it will fetch one row at a time
# if there are fewer rows remaining in the result set than the specified size,
# it will return all remaining rows
# if there are no more rows to fetch, it returns an empty list
# use when you want to retrieve a specific number of rows at a time,
# especially when dealing with large datasets where loading all rows into memory at once may not be efficient
# allows you to control the amount of data being fetched and processed at once,
# which can help improve performance and reduce memory usage
# rows = cursor.fetchmany(size=3)#retrieving 3 rows at a time, save data to rows variable
# for row in rows:#display data
#     print(row)

#fetchone()------------------------------------------------------------------------------------------------------------------------
# fetchone() method retrieves the next row of a query result set, 
# returning a single tuple representing that row
# if there are no more rows to fetch, it returns None
# use when you want to process each row individually, 
# especially when dealing with large datasets where loading all rows into memory at once may not be efficient
# allows you to iterate through the result set one row at a time, which can be useful for processing or displaying data incrementally



# fetchall() method retrieves all remaining rows of a query result set
# it returns a list of tuples, where each tuple represents a row in the result set
# if there are no rows to fetch, it returns an empty list
# use when you want to retrieve all rows from a query result set at once,
# especially when dealing with small to moderate-sized datasets where loading all rows into memory is feasible
# allows you to easily access and manipulate the entire result set without needing to iterate through it row by row
# rows = cursor.fetchall()#retrieving all rows at once, save data to rows variable
# for row in rows:#display data
#     print(row)


#TODO 7: Commit Changes
# If you make changes to the database (e.g., INSERT, UPDATE, DELETE),
# you need to commit those changes using the commit() method of the connection object
# This ensures that the changes are saved to the database and are visible to other users and applications
# conn.commit()#commit the changes to the database



row = recipes_cursor.fetchone()#retrieving one row at a time, save data to row variable
while row:#display data
    print(row)
    row = recipes_cursor.fetchone()


#TODO 8: Close the Connection




 # Cursors should be closed when they are no longer needed to free up resources
# close() is used to close the connection to the database
conn.close()#close the connection
# important because it releases the resources associated with the connection, 
# such as memory and network connections, back to the system
# Keeping connections open unnecessarily can lead to resource leaks, 
# which can degrade the performance of the application and the database server
# and most database systems have a limit on the number of concurrent connections they can handle, 
# so closing connections when they are no longer needed helps to ensure that other applications or
# users can access the database without running into connection limits
# properly closing connections also helps to maintain data integrity and consistency 
# by ensuring that any pending transactions are either committed or rolled back before the connection is terminated.
# if too many connections are left open, it can exhaust the available resources on the database server, 
# leading to connection limits being reached
# this can prevent other applications or users from accessing the database. Additionally, 
# unclosed connections may leave transactions in an incomplete state, potentially causing data integrity issues. 
# Over time, failing to close connections can result in increased latency, timeouts, and overall instability of 
# the application and database system.    


#Reference: https://pypi.org/project/pypyodbc/
##Quickstart: https://pypi.org/project/pypyodbc/#quickstart
#Driver list: https://learn.microsoft.com/en-us/sql/connect/odbc/windows/microsoft-odbc-driver-for-sql-server?view=sql-server-ver16#download
#Connection String Reference: https://www.connectionstrings.com/sql-server/