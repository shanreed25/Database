# Operations and functions

##### [Comparism](./Comparison.md)
- comparison operators are used to compare values and return a Boolean result(true, false)

##### [Text Manipulation](./TextManipulation.md)
- text manipulation functions can be used to format, extract, and modify strings

##### [SQL Aggregation](./Aggregation.md)
- performing calculations on a set of values (rows) to return a single summary value


#### Others
- `DISTINCT` - use to ensure there ar no duplicate values
- `ROUND()` function is used to round the number to the desired precision
- `CAST()` - used for explicit data type conversion, allowing a value of one data type to be converted into a value of a different, specified data type
    - part of the ANSI SQL standard, meaning its syntax and functionality are largely consistent across various database management systems like MySQL, SQL Server, PostgreSQL, and Oracle
    - `CAST(expression AS target_data_type[(length)])`
    - ensures data types are compatible for operations like comparisons, aggregations, or joins
    - present data in a specific format for reporting or display, such as rounding decimal values or converting dates to a desired string format
    - when automatic (implicit) data type conversion might lead to unexpected results or errors
    - Converting data to the required type for specific function arguments

#### Wildcards
- special characters to represent multiple characters at once
- allow for flexible and powerful pattern matching beyond exact value comparisons
- used with the LIKE operator when searching for data
- often used with the LIKE operator in a WHERE clause to search for patterns in string data

###### Common Wildcards
- `%` (Percent Sign) represents zero or more characters
- `_` (Underscore) represents a single character
- `[]` (Brackets) represents any single character within the specified set
    - `WHERE FirstName LIKE '[ABC]%'` will find names starting with 'A', 'B', or 'C'
- `^` (Caret) used within brackets to represent any single character not within the specified set
    - `WHERE City LIKE '[^A-C]%'` will find cities that do not start with 'A', 'B', or 'C'
- `-` (Hyphen) used within brackets to define a range of characters
    - `WHERE LastName LIKE '[M-P]%'` will find last names starting with any letter from 'M' to 'P'

###### Escaping Wildcards
- if you need to search for the literal `%` or `_` characters within your data, you need to use an `ESCAPE `clause to define an escape character
    - `!%` is interpreted as the literal characters `!%` rather than the wildcard and the escape character