The Library Information System (LIS) is a relational database schema for an academic library managing books, members, and issues. The system enforces several rules:
* Unique ISBNs identify book titles, with multiple copies (accession numbers) per title.
* Books have multiple authors but only one publisher and publication year.
* Members can be students or faculty with specific types (UG, PG, RS, FC).
* Books cannot be issued to members already holding a copy of the same book.
* Only one member can issue a specific book copy, and each member has limits on issued books and duration.
* Issues cannot be made if existing borrowed books exceed the duration or quota.
* The LIS is managed by library staff.# Library Information System.pdf (PDF file)
![Alt text](<./Library Information System.pdf>){ type=application/pdf style="min-height:100vh;width:100%" }