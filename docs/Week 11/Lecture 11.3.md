#  Summary of Lecture 11.3.pdf 
**Summary**
**Transactional Logging**

Transactional logging involves continuously recording the operations performed on the database during normal execution. Each transaction is identified, and the operations within the transaction are logged in sequence. In the event of a failure, the system can recover by replaying these logged operations, ensuring that the database is restored to a consistent state.

**Hot Backup**

Hot backup refers to backing up a database while it is running, allowing users to continue working with the database during the backup process. This is particularly beneficial for systems that require high availability and cannot afford downtime for data backups.

**Recovery Algorithm**

**Data Access**

Transactions access data by reading from and writing to the database. During normal operation, the database management system (DBMS) manages concurrent access to data by ensuring that multiple transactions do not modify the same data item simultaneously.

**Checkpoint**

A checkpoint periodically writes all dirty pages (pages modified but not yet written to disk) to the database files on disk. Checkpoints help ensure that data loss is limited to the changes made since the last checkpoint in the event of a system crash.

**Redo Phase**

The redo phase is part of the recovery process where the DBMS replays all logged operations from the beginning of the log up to the point where the system crashed or failed. This phase ensures that all committed transactions are restored, and the database is brought back to a consistent state.

**Undo Phase**

The undo phase is part of the recovery process where the DBMS undoes the operations logged for incomplete transactions (those that were active at the time of the crash). This phase ensures that the database is returned to a state where only committed transactions have been applied.

**Example**

Consider the following scenario:

* Transaction T1 updates data item X from 10 to 20.
* A checkpoint occurs, writing all dirty pages to disk.
* Transaction T2 updates data item Y from 30 to 40.
* The system crashes before T2 commits or aborts.

**Recovery Process**

In the event of a crash:

* The redo phase would replay the log records to restore the changes made by T1.
* The undo phase would undo the changes made by T2 since it was incomplete at the time of the crash.

As a result, the database would be restored to a consistent state, where the change made by T1 is reflected, and the change made by T2 is undone.

**Module Summary**

* Transactional logging and hot backup enable efficient and effective database recovery.
* The recovery algorithm consists of two phases: redo and undo, which ensure that committed transactions are restored and incomplete transactions are undone.
* Checkpoints help minimize data loss in the event of a crash.
* Understanding these concepts is crucial for designing and managing reliable database systems.
