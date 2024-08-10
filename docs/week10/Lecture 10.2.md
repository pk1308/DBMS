#  Summary of Lecture 10.2.pdf 
**Summary**
## Transactions and Serializability

### Transaction Execution

- Transactions are autonomous units of execution.
- They consist of a series of database actions that must be completed as a whole.
- Transactions are typically executed concurrently to improve performance.

### Serializability

- **Serializable schedules** guarantee that the outcome of a set of concurrent transactions is the same as if the transactions had executed in isolation.
- Serializable schedules are important because they ensure that the database remains consistent even when multiple transactions are executing concurrently.

### Conflicting Instructions

- **Conflicting instructions** are pairs of instructions in different transactions that access the same data item and at least one of the instructions writes to the data item.
- Conflicting instructions must be ordered in a way that maintains data consistency.

### Conflict Serializability

- A schedule is **conflict serializable** if it can be transformed into a serial schedule by swapping non-conflicting instructions.

### Precedence Graph

- A **precedence graph** is a directed graph that represents the conflicts between instructions in a schedule.
- The vertices of the graph are the transactions, and the edges represent the conflicts between instructions.

### Tests for Conflict Serializability

- A schedule is conflict serializable if and only if its precedence graph is acyclic (has no cycles).
- If the precedence graph is acyclic, a topological sort of the graph can be used to find a serial schedule that is conflict equivalent to the original schedule.

### Example

- Consider the following schedule:

```
T1: read(A), write(A)
T2: write(A)
T3: read(A)
```

- The precedence graph for this schedule is:

```
T1 -> T2
T2 -> T3
```

- The precedence graph is cyclic, which means that the schedule is not conflict serializable.

### Conclusion

- Serializability is essential for ensuring the consistency of a database in the face of concurrent transactions.
- Conflict serializability is a common way to test for serializability.
- Precedence graphs can be used to represent the conflicts between instructions in a schedule.
- Acyclic precedence graphs indicate that a schedule is conflict serializable.
