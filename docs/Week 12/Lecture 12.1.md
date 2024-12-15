#  Summary of Lecture 12.1.pdf 
**Summary**
**Query Processing Overview**

Query processing involves three basic steps:

1. Parsing and translation: The query is translated into its internal form, which is then translated into relational algebra. The parser checks syntax and verifies relations.
2. Optimization: The query-execution engine takes a query-evaluation plan, executes that plan, and returns the answers to the query.
3. Evaluation: The query-evaluation engine takes a query-evaluation plan, executes that plan, and returns the answers to the query.

**Measures of Query Cost**

Query cost is generally measured as total elapsed time for answering a query. Factors that contribute to time cost include:

* Disk accesses
* CPU
* Network communication

Disk access is typically the predominant cost and is relatively easy to estimate. It is measured by taking into account:

* Number of seeks * average-seek-cost
* Number of blocks read * average-block-read-cost
* Number of blocks written * average-block-write-cost

**Selection Operations**

* **Linear Search:** Scans the file sequentially.
* **Primary Index, Equality on Key:** Uses an index to find the record directly.
* **Primary Index, Equality on Nonkey:** Reads all blocks in the index and then reads the data blocks.
* **Secondary Index, Equality on Key:** Similar to primary index, but requires an additional seek for the data block.
* **Secondary Index, Equality on Nonkey:** Can be very expensive if the number of records fetched is large.
* **Primary Index, Comparison:** Similar to equality on nonkey.
* **Secondary Index, Comparison:** Similar to equality on nonkey.

**Complex Selections: Conjunction**

* Use a combination of indices and scan algorithms that result in the least cost for each condition.
* Use a composite index if available.
* Use intersection of identifiers if indices have record pointers.

**Complex Selections: Disjunction**

* Use union of identifiers if all conditions have available indices. Otherwise, use linear scan.
* Negation: Use linear scan. If few records satisfy the negation and an index is applicable to the original condition, use the index and fetch from file.

**Sorting**

* Can be done using an index and reading the relation in sorted order.
* For relations that fit in memory, techniques like quicksort can be used.
* For large relations, external sort-merge is a good choice.

**External Sort-Merge**

1. Create sorted runs by repeatedly reading blocks of the relation, sorting them, and writing them to a run file.
2. Merge the runs by repeatedly reading one block from each run file, comparing tuples, and writing the smallest tuple to the output.
3. Repeat step 2 until all runs are merged into one.

**Join Operation**

Several different algorithms exist to implement joins:

* **Nested-Loop Join:** Expensive since it examines every pair of tuples.
* **Block Nested-Loop Join:** Variant of nested-loop join where every block of the inner relation is paired with every block of the outer relation.
* **Indexed Nested-Loop Join:** Uses an index on the inner relation to reduce the number of comparisons.
* **Merge-Join:** Similar to external sort-merge, but used for joins.
* **Hash-Join:** Partitions the tuples based on a hash function and performs joins within each partition.

**Other Operations**

* **Duplicate Elimination:** Can be implemented via hashing or sorting.
* **Projection:** Performs projection on each tuple followed by duplicate elimination.
* **Aggregation:** Similar to duplicate elimination, but aggregate functions are applied on groups of tuples.
* **Set Operations:** Implemented using temporary tables and set operations on those tables.
* **Outer Join:** Join that includes tuples from both relations even if they do not match on the join condition.
