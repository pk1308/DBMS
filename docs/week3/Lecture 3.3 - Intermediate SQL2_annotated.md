# Lecture 3.3 - Intermediate SQL2_annotated.pdf (PDF file)
**Summary**
**Module 13: Intermediate SQL**

**Objectives:**

* Learn SQL expressions for joins
* Learn SQL expressions for views

**Outline:**

* Join Expressions
    * Cross join
    * Inner join
    * Outer join
        * Left outer join
        * Right outer join
        * Full outer join
* Views
    * View definition
    * View expansion
    * View update
    * Materialized views

**Join Expressions:**

* Join operations return a relation by combining two relations based on a matching condition.
* Types of joins:
    * **Cross join:** Cartesian product of rows from both tables.
    * **Inner join:** Only returns rows that match in both tables.
    * **Outer join:** Preserves unmatched rows using null values.
        * Left outer join: Includes all rows from the left table and unmatched rows from the right table.
        * Right outer join: Includes all rows from the right table and unmatched rows from the left table.
        * Full outer join: Includes all rows from both tables, even if unmatched.

**Views:**

* Virtual relations that provide a different perspective on the data.
* Defined using the `create view` statement as an SQL query.
* Can be used in queries and other views.
* Updates to views are translated into updates on the underlying relations.

**Some Views Cannot Be Updated:**

* Updates to some views may not be translatable into valid updates on the underlying relations, such as views with multiple tables or complex expressions.

**Materialized Views:**

* Physical tables that store the results of a view query.
* Provide faster query performance but need to be maintained when the underlying data changes.
**Lec file**
# Lecture 3.3 - Intermediate SQL2_annotated.pdf (PDF file)
![Alt text](<./Lecture 3.3 - Intermediate SQL2_annotated.pdf>){ type=application/pdf style="min-height:100vh;width:100%" }