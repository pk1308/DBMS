# Lecture 4.1 - Formal Relational Query Languages1_annotated.pdf (PDF file)
**Summary**
**Introduction to Relational Algebra**

Relational algebra is a formal language used to manipulate and query relational data. It is a procedural language, meaning that it specifies the steps to be taken to perform a query, rather than simply stating the result.

**Basic Operators**

Relational algebra has six basic operators:

1. **Select (σ)**: Filters rows based on a specified condition. Syntax: σp(r), where p is the selection predicate and r is the relation.
2. **Project (Π)**: Selects specific columns from a relation. Syntax: ΠA1,A2,...Ak(r), where A1, A2, ... Ak are the selected attribute names and r is the relation.
3. **Union (∪)**: Combines two relations with the same schema. Syntax: r ∪ s, where r and s are the relations to be joined.
4. **Difference (–)**: Removes rows from one relation that are also present in another relation. Syntax: r - s, where r is the relation from which rows are to be removed and s is the relation containing the rows to be removed.
5. **Intersection (∩)**: Finds rows that are present in both relations. Syntax: r ∩ s, where r and s are the relations to be intersected.
6. **Cartesian Product (×)**: Combines all rows from two relations, creating a new relation with all possible pairings of rows. Syntax: r × s, where r and s are the relations to be joined.

**Additional Operators**

In addition to the six basic operators, relational algebra also has several additional operators, such as:

1. **Rename (ρ)**: Changes the name of a relation or its attributes.
2. **Division (÷)**: Finds rows in one relation that correspond to all rows in another relation. Syntax: r ÷ s, where r is the relation to be divided and s is the relation containing the rows to be used as the divisor.

**Query Examples**

Here are some examples of queries using relational algebra:

* Find all students who are enrolled in the Physics department: σdept_name = 'Physics' (student)
* Find the names and salaries of instructors: Πname, salary (instructor)
* Find all courses taught in the Fall 2009 semester: Πcourse_id(σsemester = 'Fall' and year = 2009 (section))
* Find all courses taught in the Fall 2009 semester, but not in the Spring 2010 semester: Πcourse_id(σsemester = 'Fall' and year = 2009 (section)) - Πcourse_id(σsemester = 'Spring' and year = 2010 (section))

**Benefits of Using Relational Algebra**

Relational algebra is a powerful tool for querying relational data because it provides a concise and expressive way to specify queries. It is also independent of any particular database management system, making it portable across different systems.

**Limitations of Relational Algebra**

One limitation of relational algebra is that it can be difficult to read and understand complex queries. Additionally, relational algebra does not support recursion or subqueries.

**Alternatives to Relational Algebra**

There are several other formal query languages that can be used to query relational data, including tuple relational calculus and domain relational calculus. Tuple relational calculus is a non-procedural language that uses a tuple-oriented syntax to specify queries. Domain relational calculus is a non-procedural language that uses a domain-oriented syntax to specify queries.
