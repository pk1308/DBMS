#  Summary of Lecture 12.2.pdf 
**Summary**
## Query Optimization

Database systems aim to provide efficient and timely responses to queries from end-users. To achieve this, the database system employs a query optimizer, responsible for devising an efficient execution plan for a given query. This process involves several steps:

**1. Transformation of Relational Expressions:**

* Equivalent expressions can be generated using equivalence rules.
* Different algorithms can be used for each operation.

**2. Evaluation Plan:**

* Defines the specific algorithm used for each operation.
* Specifies how the execution of operations is coordinated.

**3. Query Cost Estimation:**

* Calculate the cost of an execution plan based on:
    * Statistical information about relations (e.g., number of tuples, distinct values)
    * Statistics estimation for intermediate results
    * Cost formulae for algorithms

**Equivalence Rules:**

Equivalence rules specify that two relational algebra expressions are equivalent if they generate the same set of tuples on every legal database instance.
Some important equivalence rules are:
1. Conjunctive Selection operations can be broken into individual selections.
2. Selection operations are commutative.
3. Only the last in a sequence of projection operations is needed.
4. Selections can be combined with Cartesian products and theta joins.
5. Theta-join operations (and natural joins) are commutative.
6. Natural join operations are associative.
7. Theta joins are associative under certain conditions.
8. The selection operation distributes over the theta join operation under certain conditions.
9. The projection operation distributes over the theta join operation under certain conditions.
10. Set operations union and intersection are commutative and associative.
11. The selection operation distributes over union, intersection, and difference.
12. The projection operation distributes over union.

**Example:**

Consider a query to find the names of instructors in the Music department and the titles of courses they teach:

```
πname,title (σdept name="Music" (instructor on teaches on πcourse id,title (course)))
```

**Transformation Example:**

* **Pushing Selections:** Perform the selection on the instructor relation as early as possible to reduce the size of the relation to be joined.
```
πname,title ((σdept name="Music" (instructor)) on (teaches on πcourse id,title (course)))
```
* **Pushing Projections:** Perform the projection on the course relation as early as possible to reduce the size of the relation to be joined.
```
πname,title (πname,course id (σdept name="Music" (instructor) on teaches)) on
πcourse id,title (course)
```

**Join Ordering:**

The order in which relations are joined can significantly impact the efficiency of the query. By leveraging join associativity and commutativity, the query optimizer can choose the most efficient join order.

**Enumeration of Equivalent Expressions:**

Query optimizers employ equivalence rules to systematically generate expressions equivalent to the given expression. However, enumerating all possible equivalent expressions can be time-consuming.

**Implementing Transformation-Based Optimization:**

To reduce space and time requirements during transformation-based optimization, the following techniques are employed:

* **Sharing Common Sub-Expressions:** Equivalent expressions often share common sub-expressions, which can be shared using pointers to optimize space utilization.
* **Dynamic Programming:** Dynamic programming is employed to avoid generating duplicate sub-expressions, further reducing optimization time.

**Conclusion:**

Query optimization is a critical aspect of database management systems. By utilizing equivalence rules, generating execution plans, estimating costs, and applying transformation-based optimization techniques, query optimizers strive to deliver efficient and timely responses to user queries.
