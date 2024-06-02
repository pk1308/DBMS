# Lecture 2.3 - Introduction to SQL1.pdf (PDF file)
**Summary**
**Module 08: Introduction to SQL**

**Objectives:**
- Understand relational query language
- Understand data definition and basic query structure

**Outline:**
- History of SQL
- Data Definition Language (DDL)
- Data Manipulation Language (DML): Query Structure

**Data Definition Language (DDL):**
- Defines information about relations, including:
    - Schema for each relation
    - Domain of values associated with each attribute
    - Integrity constraints
    - Storage structure on disk

**Create Table Construct:**
- `create table r (A1D1, A2D2, . . . , AnDn);`
- `r` is the relation name
- `Ai` is an attribute name
- `Di` is the data type of values in the domain of Ai

**Integrity Constraints:**
- `not null`: ensures an attribute cannot be null
- `primary key (A1, . . . , An)`: ensures that the values of attributes A1, ..., An uniquely identify each tuple in the relation
- `foreign key (Am, . . . , An) references r`: ensures that the values of attributes Am, ..., An must reference existing values in relation r

**Data Manipulation Language (DML): Query Structure:**
- Basic query structure:
    - `select A1, A2, . . . , An`
    - `from r1,r2, ...,rm`
    - `where P`
- Where P is a predicate that specifies conditions the result must satisfy

**Select Clause:**
- Lists the attributes desired in the result
- Can use an asterisk (*) to denote all attributes
- Can rename attributes using the `as` clause

**Where Clause:**
- Specifies conditions that tuples in the result must satisfy
- Uses logical connectives (and, or, not) to combine conditions

**From Clause:**
- Lists the relations involved in the query
- Corresponds to the Cartesian product operation in relational algebra
**Lec file**
# Lecture 2.3 - Introduction to SQL1.pdf (PDF file)
