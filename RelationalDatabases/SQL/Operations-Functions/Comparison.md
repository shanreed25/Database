# Comparism
- comparison operators are used to compare values and return a Boolean result(true, false)
- `WHERE` clauses are commonly used to filter data based on specific conditions
- When comparing numeric values, do not enclose them in quotes.
- When comparing text strings, enclose them in single quotes. String comparisons are typically case-sensitive unless the database collation settings specify otherwise.
- While comparison operators can be used with text strings, the results of `>` or `<` operations are based on alphabetical order, which may not always align with intuitive "greater than" or "less than" concepts for text

#### The Primary SQL comparison operators
- **Equal to (=):** Checks if two values are equal
- **Not equal to (<> or !=):** Checks if two values are not equal. Both operators achieve the same result, though <> is generally considered more standard
- **Greater than (>):** Checks if the left operand is greater than the right operand
- **Less than (<):** Checks if the left operand is less than the right operand
- **Greater than or equal to (>=):** Checks if the left operand is greater than or equal to the right operand
- **Less than or equal to (<=):** Checks if the left operand is less than or equal to the right operand
- **NULL-safe equal (<=>):** This operator, specific to some SQL dialects like MySQL, performs an equality comparison but handles NULL values differently. It returns 1 (true) if both operands are NULL, and 0 (false) if one operand is NULL and the other is not