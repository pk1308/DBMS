#  Summary of Lecture 10.3.pdf 
**Summary**
## Overview of Database Transactions

Database transactions play a crucial role in maintaining data integrity and consistency within a database system. They encompass a series of database operations that are executed as a single unit. The ACID properties (Atomicity, Consistency, Isolation, and Durability) govern transactions, ensuring that data remains reliable even in the face of system failures or errors.

### ACID Properties

* **Atomicity:** Transactions are indivisible units of work. Either all operations within a transaction are completed successfully, or none of them are.
* **Consistency:** Transactions transform the database from one consistent state to another consistent state.
* **Isolation:** Transactions are executed independently of each other, as if they were running in isolation. This ensures that the result of a transaction is not affected by any other concurrent transactions.
* **Durability:** Once a transaction is committed, its changes become permanent and are not lost even in the event of a system failure.

### Transaction Management Commands

To manage transactions in SQL, the following commands are commonly used:

* **COMMIT:** Saves changes made within a transaction and releases database locks.
* **ROLLBACK:** Cancels a transaction and restores the database to the state before the transaction began.
* **SAVEPOINT:** Creates a point within a transaction to which it can be rolled back if needed.
* **SET TRANSACTION:** Used to configure transaction-related parameters, such as isolation level or read-only mode.

### Serializability

Serializability is a key concept in transaction management that ensures that the result of a set of concurrent transactions is equivalent to the result of executing the transactions one after another in a serial order.

* **Conflict Serializability:** A schedule of transactions is conflict serializable if it does not violate any data dependency rules (read-write or write-write conflicts).
* **View Serializability:** A schedule of transactions is view serializable if it is equivalent to a serial schedule in terms of the data items that are read and written.

### Recovery from Failures

Transaction recovery mechanisms ensure that data remains consistent even in the event of system failures.

* **Cascading Rollback:** If one transaction fails, all dependent transactions are also rolled back.
* **Cascadeless Rollback:** Transactions are rolled back only to the point of failure, preserving the work done by other transactions.

### SQL Implementation

In SQL, transactions can be initiated implicitly or explicitly. By default, each SQL statement is considered a separate transaction. However, using the COMMIT and ROLLBACK commands allows for explicit transaction management.

### Conclusion

Database transactions play a critical role in maintaining data integrity and consistency. By understanding the ACID properties, transaction management commands, and serialization concepts, database administrators can ensure that their systems are robust and reliable.
