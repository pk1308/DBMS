# Welcome to DBMS

# **Chapters**

1. Chapter 1: Introduction
1. Chapter 2: Introduction to Relational Languages
1. Chapter 3: Introduction to SQL
1. Chapter 4: Intermediate SQL
1. Chapter 5: Advanced SQL
   Sections 5.4 onwards may be omitted.
1. Chapter 6: Entity-Relationship Model
1. Chapter 7: Relational Database Design
1. Chapter 8: Complex Data Types
1. Chapter 9: Application Design
1. Chapter 10: Big Data
1. Chapter 11: Data Analytics
1. Chapter 12: Physical Storage Systems
1. Chapter 13: Storage and File Structure
1. Chapter 14: Indexing
1. Chapter 15: Query Processing
1. Chapter 16: Query Optimization
1. Chapter 17: Transactions
1. Chapter 18: Concurrency Control
   Section 18.8 (Snapshot Isolation), Section 18.9 (Weak Levels of Consistency) may be omitted.
1. Chapter 19: Recovery System
   Section 19.8 (ARIES) may be omitted.

## PostgreSQL Cheatsheet (Markdown)

This cheatsheet summarizes some essential PostgreSQL commands for managing databases, users, tables, and data.

**Connection:**

- `psql -h <hostname> -p <port> -d <database> -U <username>`: Connect to a PostgreSQL server (replace placeholders with actual values).

**Databases:**

- `CREATE DATABASE <database_name>`: Create a new database.
- `DROP DATABASE <database_name>`: Delete an existing database (use with caution!).
- `\l`: List all databases.
- `\connect <database_name>`: Switch to a different database within the same session.

**Users and Roles:**

- `CREATE ROLE <username> [WITH PASSWORD '<password>']`: Create a new user.
- `GRANT <privilege> ON <object> TO <username>`: Grant specific privileges (e.g., SELECT, INSERT, UPDATE, DELETE) on a database object (table, schema) to a user.
- `REVOKE <privilege> ON <object> FROM <username>`: Revoke privileges from a user.
- `\du`: List all roles (users).

**Tables:**

- `CREATE TABLE <table_name> ( <column_name> <data_type> [CONSTRAINT], ...);`: Create a new table with columns and constraints.
- `DESCRIBE <table_name>`: Show the structure of a table.
- `DROP TABLE <table_name>`: Delete a table (use with caution!).
- `\dt`: List all tables in the current schema.

**Data Manipulation:**

- `INSERT INTO <table_name> (<column1>, <column2>, ...) VALUES (<value1>, <value2>, ...);`: Insert data into a table.
- `SELECT * FROM <table_name> [WHERE <condition>];`: Retrieve data from a table (all columns by default, with optional filtering).
- `UPDATE <table_name> SET <column_name> = <new_value> [WHERE <condition>];`: Update existing data in a table.
- `DELETE FROM <table_name> [WHERE <condition>];`: Delete rows from a table.

**Other Useful Commands:**

- `\q`: Quit the psql client.
- `\h`: Get help on a specific command (e.g.,`\h CREATE TABLE`).
- `\conninfo`: Display connection information.

**Additional Notes:**

- Remember to replace placeholders like `<database_name>`,`<username>`, etc. with actual values.
- This is a basic cheatsheet. PostgreSQL offers many more commands and functionalities. Refer to the official documentation for in-depth details:[https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)
