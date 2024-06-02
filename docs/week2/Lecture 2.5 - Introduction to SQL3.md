# Lecture 2.5 - Introduction to SQL3.pdf (PDF file)
**Summary**
Module 10 of Database Management Systems covers set operations, null values, three-valued logic, aggregate functions, and null values in aggregates.

**Set Operations:**
* Union, intersect, and except operators combine sets of rows.
* Multiset versions (e.g., union all) retain all duplicates.

**Null Values:**
* Unknown or non-existent attribute values.
* Arithmetic expressions involving nulls result in null.
* Null values are represented as is null or is not null, not with comparison operators.

**Three-Valued Logic:**
* Three values: true, false, unknown.
* Comparison with nulls returns unknown.
* Three-valued logic is applied to OR, AND, and NOT operators.

**Aggregate Functions:**
* Operate on rows in a column to return a single value.
* Functions include avg, min, max, sum, and count.
* Null values are ignored in most aggregate functions.

**Group By:**
* Groups rows by selected attributes and computes aggregate functions separately for each group.
* Attributes in the select clause must appear in the group by list.

**Having Clause:**
* Specifies conditions to filter groups based on aggregate function results.
* Applied after group formation.

**Null Values and Aggregates:**
* Aggregate functions ignore rows with null values in the aggregated attribute.
* Count(*) returns 0 for empty collections and null for null-only collections.
**Lec file**
# Lecture 2.5 - Introduction to SQL3.pdf (PDF file)
