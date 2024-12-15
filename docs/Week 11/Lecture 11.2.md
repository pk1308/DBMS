#  Summary of Lecture 11.2.pdf 
**Summary**
## Failure Classification

Failures can be classified into three categories:

1. **Transaction failures:** These are caused by internal errors within the transaction itself, such as a deadlock or a data integrity violation.
2. **System errors:** These are caused by external factors, such as a power failure or a hardware malfunction.
3. **Disk failures:** These are caused by a physical failure of the disk drive that stores the database.

## Recovery Algorithms

Recovery algorithms have two parts:

1. **Actions taken during normal transaction processing** to ensure enough information exists to recover from failures.
2. **Actions taken after a failure** to recover the database contents to a state that ensures atomicity, consistency, and durability.

## Storage Structure

The storage structure of a database system consists of three types of storage:

1. **Volatile storage:** This storage is not persistent and is lost when the system crashes. Examples of volatile storage include main memory and cache memory.
2. **Nonvolatile storage:** This storage is persistent and survives system crashes. Examples of nonvolatile storage include disk drives and tape drives.
3. **Stable storage:** This storage is a mythical form of storage that never fails. In practice, stable storage is approximated by maintaining multiple copies of each block on separate disks.

## Database Modification Schemes

There are two database modification schemes:

1. **Immediate-modification scheme:** This scheme allows updates of an uncommitted transaction to be made to the buffer or the disk itself before the transaction commits.
2. **Deferred-modification scheme:** This scheme performs updates to the buffer/disk only at the time of transaction commit.

## Undo and Redo Operations

Undo and redo operations are used to recover from failures.

* **Undo** of a log record < Ti, X, V1, V2 > writes the old value V1 to X.
* **Redo** of a log record < Ti, X, V1, V2 > writes the new value V2 to X.

## Checkpoints

Checkpoints are used to streamline the recovery procedure by periodically performing the following actions:

1. Output all log records currently residing in main memory onto stable storage.
2. Output all modified buffer blocks to the disk.
3. Write a log record < checkpoint L > onto stable storage where L is a list of all transactions active at the time of checkpoint.

## Module Summary

* Failures may be due to a variety of sources – each needs a strategy for handling.
* A proper mix and management of volatile, non-volatile, and stable storage can guarantee recovery from failures and ensure Atomicity, Consistency, and Durability.
* Log-based recovery is efficient and effective.
