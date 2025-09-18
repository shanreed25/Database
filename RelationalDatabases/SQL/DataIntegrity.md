# Data Integrity
**Data integrity in SQL refers to the accuracy, consistency, and reliability of data stored within a SQL database**
- ensures that the data is valid and adheres to predefined rules and relationships, preventing inconsistencies, errors, and unauthorized modifications
- in a relational database everything is connected
- we could just create one large table with hundreds of attributes types
    - single table attempting to store diverse entities often leads to repeating data across rows, violating normalization principles
    - redundancy increases storage space and makes data updates more complex, raising the risk of inconsistencies if not all instances are updated correctly
- instead of a single large table, a normalized database design, utilizing multiple smaller, related tables, offers better data integrity, performance, and maintainability

# How to achevie Data Integrity
**A database must have these three features to achevie Data integrity.**
1. No Repeating Values
2. No Incorrect Values
3. No Broken Relationships between tables
**You can achevie this by**
- breaking up the data into multiple, manageable, and unique tables
- then connect the tables through relationships

## Relationships
- **One to One**
    - One state has one Passport and one Passport has one Person
- **One to Many**
    - A mother can have many childern but a child can only have one mother
- **Many to Many**
    - A student can have many classes and a class can have many students

### Parent-Child relationships
- **One to One** parent-child dynamic is not interchangeable because the passport cannot exist without a person
    - Parent: A person can exist without a passport
    - Child: A passport cannot exist without a person
    - This creates a mandatory dependency from the child (Passport) to the parent (Person). 
- **One to Many** one cannot exsit without the other
    - Parent: A mother cannot be a mother without a child
    - Child: A child cannot be a child without a mother
- **Many to Many** parent child relationship here is misleading
    - this type of relationship is non-hierarchical and bidirectional
    - multiple records in one table can be related to multiple records in another table, and vice-versa
    - there is no clear parent or child, as both entities are on equal footing
    - the concepts of a many-to-many relationship and a parent-child relationship are fundamentally at odds
    - true parent-child structure implies a clear hierarchy, a many-to-many relationship, by definition, has no such hierarchy
    - so a true many-to-many relationship has no inherent parent or child
    - many-to-many parent-child, is likely describing one of two database patterns, but using contradictory language
#### A standard many-to-many relationship
- is achevied by two tables being linked by a third, "joining" table
- the third, "joining" table, also called a junction or associative table, 
- this breaks the many-to-many into two separate one-to-many relationships so you can have a clear parent and child
- you would have a Students table, a Classes table and a third table, Student_Classes, that links the Student and Classes tables
- You can't say whether Students or Classes is the parent; they are just two entities linked by a third
- the Student-Classes table would be a child to both the students table and the classes table

#### A complex, self-referencing relationship
- many-to-many relationship within a single table
- a single entity (like a product part) can be both a "parent" to its sub-components and a "child" of a larger assembly
- creates a network rather than a clear hierarchy, which again contradicts the definitive, singular "parent" implied by a parent-child relationship
**Many-to-many relationship, use when multiple records from two different tables are related to each other, requiring a junction table for implementation**
**Self-referencing relationship: Use when records within a single table are related to each other, forming a hierarchical or network structure** 