# Lecture 1.4 - Intro to DBMS1.pdf (PDF file)

**Summary**
This document provides an introduction to Database Management Systems (DBMS) by discussing various concepts and components.

**Levels of Abstraction:**

- Physical level: Database storage and organization.
- Logical level: Data representation and relationships.= type instructor = record
  ID : string;
  name : string;
  dept name : string;
  salary : integer;
  end;
- View level: Application-specific data presentation and security.

**Schema and Instance:**

- Schema: Logical structure of the database, specifying data types, constraints, and relationships.
  - logical schema - Analogous to type information of a variable in a program.
  - Physical schema - The overall physical structure of the database.
- Instance: Actual data stored in the database at a specific time.

**Data Models:**

- Tools for describing data, relationships, semantics, and constraints.
- Relational model: Stores data in tables, with rows representing records and columns representing attributes.

**DDL and DML:**

- Data Definition Language (DDL): Used to create, modify, and delete database structures (e.g., tables).
- Data Manipulation Language (DML): Used to access and manipulate data (e.g., insert, update, delete).

**SQL (Structured Query Language):**

- Commercial DML widely used in database systems. Not Turing-machine equivalent, but often embedded in other programming languages.

**Database Design:**

- Process of creating the database schema and physical layout.
- Logical design: Deciding on the schema, including attributes and relationships.
- Physical design: Determining the physical storage and optimization strategies.
