#  Summary of Lecture 9.5.pdf 
**Summary**
**Index Definition in SQL**

In SQL, an index is a data structure that helps speed up the retrieval of data from a database. It is created on a specific column or columns of a table and consists of a set of entries, each of which contains the value of the indexed column(s) and a pointer to the corresponding row in the table.

To create an index, you use the `CREATE INDEX` statement. The syntax of the statement is as follows:

```sql
CREATE INDEX <index_name> ON <table_name> (<column_list>)
```

For example, the following statement creates an index named `idx_name` on the `name` column of the `student` table:

```sql
CREATE INDEX idx_name ON student (name)
```

**Multiple-Key Access**

A composite index is an index that is created on multiple columns of a table. This can be useful for speeding up queries that involve multiple columns, such as a query that searches for rows based on both the first name and last name of a person.

To create a composite index, you use the `CREATE INDEX` statement and specify the multiple columns in the `column_list` parameter. For example, the following statement creates a composite index named `idx_name_age` on the `name` and `age` columns of the `student` table:

```sql
CREATE INDEX idx_name_age ON student (name, age)
```

**Privileges**

To create an index, you must have the `CREATE INDEX` privilege on the table. This privilege is typically granted to database administrators and other users who need to create and manage indexes.

**Guidelines for Indexing**

There are a number of factors to consider when deciding whether to create an index on a particular column or set of columns. These factors include:

* The frequency with which the column(s) are used in queries
* The number of distinct values in the column(s)
* The size of the table
* The impact of the index on the performance of other operations, such as inserts and updates

**Ground Rules**

The following are some general guidelines for indexing:

* **Rule 0:** Indexes lead to an access-update tradeoff. Creating an index can speed up queries, but it can also slow down inserts, updates, and deletes.
* **Rule 1:** Index the correct tables. Only index tables that are frequently queried.
* **Rule 2:** Index the correct columns. Index columns that are frequently used in queries and that have a wide range of values.
* **Rule 3:** Limit the number of indexes for each table. Too many indexes can slow down updates and inserts.
* **Rule 4:** Choose the order of columns in composite indexes. The order of the columns in a composite index can affect the performance of queries.
* **Rule 5:** Gather statistics to make index usage more accurate. The database can use indexes more effectively when it has statistical information about the tables involved in the queries.
* **Rule 6:** Drop indexes that are no longer required. If an index is no longer used, it should be dropped to free up space and improve performance.

**Module Summary**

In this module, we have learned about the following concepts:

* How to create indexes in SQL
* The different types of indexes, including single-column indexes and composite indexes
* The privileges required to create indexes
* The guidelines for indexing
* The ground rules for indexing
