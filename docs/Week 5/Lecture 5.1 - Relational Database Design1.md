# Lecture 5.1 - Relational Database Design1.pdf (PDF file)
**Summary**
This module focuses on principles of relational database design. It emphasizes:

**Features of Good Design:**

* Reflects real-world structure
* Accommodates future data additions
* Avoids redundancy
* Provides efficient data access
* Maintains data integrity

**Redundancy and Anomaly:**

* Redundancy (duplicate data) leads to anomalies:
    * Insertion: Can't add data if unknown data is required
    * Deletion: Losing unrelated information when deleting records
    * Update: Inaccurate changes due to multiple occurrences of data

**Decomposition:**

* Decomposing relations into smaller ones removes redundancy and minimizes dependencies among attributes.
* Good decomposition ensures data preservation and integrity.

**Atomic Domains and First Normal Form (1NF):**

* Atomic domains consist of indivisible elements.
* 1NF requires relations with atomic domains and each attribute holding a single value.
* Non-atomic values complicate storage and encourage redundancy.
