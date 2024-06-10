# Lecture 2.5 - Introduction to SQL3.pdf (PDF file)
**Summary**
**Introduction**

This module provides an overview of set operations, null values, and aggregation in SQL/3. It introduces the concepts of set union, intersection, and exception, as well as the handling of null values and aggregate functions. The module concludes with a summary of the key points covered.

**Objectives**

Upon completion of this module, students will be able to:

* Understand and apply set operations (union, intersection, except)
* Handle null values in SQL queries
* Use aggregate functions (avg, min, max, sum, count)
* Group data using the GROUP BY clause
* Filter grouped data using the HAVING clause

**Outline**

1. Set Operations
2. Null Values
3. Three-Valued Logic
4. Aggregate Functions
5. GROUP BY
6. HAVING
7. Null Values with Aggregates

**Set Operations**

Set operations in SQL/3 allow you to combine or compare the results of two or more queries. The three most common set operations are union, intersection, and except.

* **Union:** Returns all unique rows from both input queries.
* **Intersection:** Returns only the rows that are common to both input queries.
* **Except:** Returns all rows from the first input query that are not present in the second input query.

**Null Values**

Null values represent the absence of a value or an unknown value in SQL/3. They are distinct from zero or empty strings.

**Three-Valued Logic**

Due to the inclusion of null values, SQL/3 uses a three-valued logic system, where a predicate can be evaluated as true, false, or unknown.

* True: If the predicate is satisfied without any null values.
* False: If the predicate is not satisfied, or if it involves null values.
* Unknown: If the predicate involves a comparison with a null value.

**Aggregate Functions**

Aggregate functions operate on a group of values and return a single result. Some common aggregate functions include:

* **AVG:** Average value
* **MIN:** Minimum value
* **MAX:** Maximum value
* **SUM:** Sum of values
* **COUNT:** Number of values

**GROUP BY**

The GROUP BY clause is used to group the results of a query based on one or more attributes. It allows for aggregation and filtering of data within each group.

**HAVING**

The HAVING clause is similar to the WHERE clause, but it is used to filter grouped data. It applies predicates to the aggregate values rather than the individual rows.

**Null Values with Aggregates**

Aggregate functions ignore null values unless the COUNT(*) function is used. COUNT(*) counts all rows, regardless of whether they contain null values.

**Module Summary**

This module has covered the following key concepts:

* Set operations (union, intersection, except)
* Null values and three-valued logic
* Aggregate functions (avg, min, max, sum, count)
* GROUP BY and HAVING clauses
* Handling null values with aggregates

These concepts are essential for working with data in SQL/3. Understanding these concepts will enable you to perform complex data analysis and manipulation tasks efficiently.
