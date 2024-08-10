#  Summary of Lecture 10.1.pdf 
**Summary**
**Week Recap**

**Objectives & Outline:**

* To understand the concept of transaction – ‘doing a task in a database’ and its state
* To explore issues in concurrent execution of transactions

**Transaction Concept:**

**Definition:** A transaction is a unit of program execution that accesses and, possibly updates, various data items

**Example:**
```
Transaction to transfer $50 from account A to account B:
1. read(A)
2. A := A − 50
3. write(A)
4. read(B)
5. B := B + 50
6. write(B)
```

**Issues:**
* Failures of various kinds (hardware failures, system crashes)
* Concurrent execution of multiple transactions

**ACID Properties:**

**Required properties of a transaction to ensure data integrity and consistency:**

* **Atomicity:** All operations in a transaction are treated as a single unit; either succeeds completely or fails completely
* **Consistency:** The transaction brings the database from one valid state to another, maintaining database invariants
* **Isolation:** Concurrent execution of transactions leaves the database in the same state as if they were executed sequentially
* **Durability:** Once a transaction has been committed, its updates will remain committed even in the case of a system failure

**Transaction States:**

* **Active:** Initial state, transaction is executing
* **Partially committed:** After the final statement has been executed
* **Failed:** After normal execution can no longer proceed
* **Aborted:** After the transaction has been rolled back
* **Committed:** After successful completion
* **Terminated:** After it has been committed or aborted

**State Transitions:**

* Active to partially committed: After the final statement has executed
* Partially committed to committed: After the transaction has successfully completed
* Partially committed or active to aborted: After the transaction has failed or been aborted
* Partially committed or active to failed: After the transaction has failed
* Committed or aborted to terminated: After the transaction has completed

**Concurrent Executions:**

* Multiple transactions can run concurrently in the system for increased throughput and reduced average response time
* Concurrency Control Schemes: Mechanisms to achieve isolation and prevent concurrent transactions from destroying database consistency

**Schedules:**

* A sequence of instructions that specify the order in which instructions of concurrent transactions are executed
* Preserve the order of instructions within each individual transaction
* A transaction has a commit instruction as its last statement if it successfully completes, or an abort instruction if it fails

**Example Schedules:**

* **Serial Schedule:** Transactions are executed one after the other
* **Equivalent Schedule:** Transactions are executed in a different order but produce the same results as a serial schedule
* **Non-serial Schedule:** A schedule that does not satisfy the properties of a serial schedule
