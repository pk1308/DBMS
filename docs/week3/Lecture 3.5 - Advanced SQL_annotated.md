# Lecture 3.5 - Advanced SQL_annotated.pdf (PDF file)
**Summary**
**Module 15: Advanced SQL**

**Objectives:**

* Familiarize with functions and procedures in SQL
* Understand triggers and their performance issues

**Outline:**

* Functions and Procedural Constructs
* Triggers
* Functionality vs Performance

**Summary:**

**Functions and Procedural Constructs**

* SQL supports functions and control flow statements.
* External language functions can be used for specialized data types.
* SQL functions are parameterized views.

**Triggers**

* Triggers define actions executed in response to insert, update, or delete operations.
* They can enforce data integrity, update other tables, or invoke functions.
* There are two types of triggers: BEFORE and AFTER.
* BEFORE triggers can modify values before database changes, while AFTER triggers can perform additional actions.

**Triggering Events and Actions**

* Triggers can be triggered by inserts, deletes, or updates.
* Update triggers can be specific to certain attributes.
* Values before and after an event can be referenced.

**Performance Issues**

* Triggers can degrade performance, especially with complex code or iterative operations.
* Cascading triggers (triggers calling triggers) should be avoided.
* Consider using row-level triggers instead of statement-level triggers for better efficiency.

**Best Practices for Triggers**

* Use triggers for short, simple operations unrelated to application logic.
* Avoid triggers for complex validation, business rules, or calculations.
* Limit the number of triggers and keep their code concise.
* Be aware of potential performance issues and test triggers thoroughly.
**Lec file**
# Lecture 3.5 - Advanced SQL_annotated.pdf (PDF file)
![Alt text](<./Lecture 3.5 - Advanced SQL_annotated.pdf>){ type=application/pdf style="min-height:100vh;width:100%" }