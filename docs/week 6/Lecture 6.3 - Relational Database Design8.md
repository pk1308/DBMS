#  Summary of Lecture 6.3 - Relational Database Design8.pdf 
**Summary**
**Introduction**

The objective of this module is to design a relational database schema for a Library Information System (LIS) of an Institute. The LIS should manage the books, the members, and the issue-return process.

**Entity Sets**

* **books**: Each book has title, author, publisher, year of publication, ISBN number, and accession number.
* **students**: Each student has name, roll number, department, gender, mobile number, date of birth, and degree.
* **faculty**: Each faculty has name, employee id, department, gender, mobile number, and date of joining.
* **members**: Each member has a membership number and a member type (student, faculty, research scholar, etc.).
* **quota**: Each member type has a maximum quota for the number of books they can issue and the maximum duration for which they can issue books.
* **staff**: Library staff have a name, id, gender, mobile number, and date of joining.

**Relationships**

* **book issue**: A book can be issued by a member.
* **members**: A member can belong to a member type and has a quota.
* **students**: A student is a member and has a roll number.
* **faculty**: A faculty is a member and has an employee id.
* **staff**: A staff member is a member and has an id.

**Relational Schema**

* **book catalogue**: (title, author fname, author lname, publisher, year, ISBN no)
* **book copies**: (ISBN no, accession no)
* **book issue**: (member no, accession no, doi)
* **quota**: (member type, max books, max duration)
* **members**: (member no, member class, member type, roll no, id)
* **students**: (student fname, student lname, roll no, department, gender, mobile no, dob, degree)
* **faculty**: (faculty fname, faculty lname, id, department, gender, mobile no, doj)
* **staff**: (staff fname, staff lname, id, gender, mobile no, doj)

**Schema Refinement**

The initial relational schema is refined to ensure that it is in BCNF. The following steps are taken:

* The book catalogue relation is decomposed into two relations: book catalogue and book copies.
* The members relation is decomposed into two relations: members and students/faculty.

**Final Schema**

The final relational schema is as follows:

* **book catalogue**: (title, author fname, author lname, publisher, year, ISBN no)
* **book copies**: (ISBN no, accession no)
* **book issue**: (member no, accession no, doi)
* **quota**: (member type, max books, max duration)
* **members**: (member no, member class, member type, roll no, id)
* **students**: (student fname, student lname, roll no, department, gender, mobile no, dob, degree)
* **faculty**: (faculty fname, faculty lname, id, department, gender, mobile no, doj)
* **staff**: (staff fname, staff lname, id, gender, mobile no, doj)

**Module Summary**

The module illustrates how a schema can be designed and refined for an LIS. The final schema is in BCNF and supports the required queries.
