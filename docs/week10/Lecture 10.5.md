#  Summary of Lecture 10.5.pdf 
**Summary**
**Module 50: Concurrency Control/2**

**Objectives**

* Understand deadlock as a peril of locking and the techniques for detecting, preventing, and recovering from deadlocks
* Introduce a simple time-based protocol that avoids deadlocks

**Deadlock Handling**

* **Definition:** A system is deadlocked if there is a set of transactions such that every transaction in the set is waiting for another transaction in the set.
* **Deadlock Prevention:**
    * **Pre-declaration:** Require each transaction to lock all its data items before it begins execution.
    * **Partial ordering:** Impose a partial ordering of all data items and require that a transaction can lock data items only in the order specified by the partial order.
* **Deadlock Detection:**
    * **Wait-for graph:** A directed graph where each vertex represents a transaction and each edge represents a waiting relationship (e.g., transaction A is waiting for transaction B to release a lock).
    * The system is in a deadlock state if and only if the wait-for graph has a cycle.
* **Deadlock Recovery:**
    * Roll back some transaction (victim) to break the deadlock.
    * Choose the victim that will incur minimum cost and minimize starvation.

**Timestamp-Based Protocols**

* **Principle:** Each transaction is assigned a timestamp when it enters the system. The protocol ensures that conflicting read and write operations are executed in timestamp order.
* **Timestamps:**
    * **W-timestamp(Q):** The largest timestamp of any transaction that successfully executed write(Q).
    * **R-timestamp(Q):** The largest timestamp of any transaction that successfully executed read(Q).
* **Rules:**
    * Read(Q):
        * If TS(transaction) ≤ W-timestamp(Q), reject the read and roll back the transaction (the value of Q was already overwritten).
        * Otherwise, execute the read and set R-timestamp(Q) to max(R-timestamp(Q), TS(transaction)).
    * Write(Q):
        * If TS(transaction) < R-timestamp(Q), reject the write and roll back the transaction (the value of Q is needed elsewhere).
        * If TS(transaction) < W-timestamp(Q), reject the write and roll back the transaction (attempting to write an obsolete value).
        * Otherwise, execute the write and set W-timestamp(Q) to TS(transaction).

**Correctness of Timestamp-Ordering Protocol**

* **Serializability:** Guarantees serializability since all precedence graph arcs are of the form (Ti, Tj) where TS(Ti) < TS(Tj).
* **Freedom from Deadlock:** No transaction ever waits, preventing deadlocks.
* **Limitations:**
    * May not be cascade-free.
    * May not be recoverable.

**Module Summary**

* Deadlocks are perils of locking and need to be handled.
* Deadlock prevention techniques ensure that the system never enters a deadlock state.
* Deadlock detection algorithms can help identify deadlocks for recovery.
* The timestamp-ordering protocol is a simple time-based protocol that avoids deadlocks and guarantees serializability, but may not be cascade-free or recoverable.
