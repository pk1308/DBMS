#  Summary of Lecture 9.1.pdf 
**Summary**
**Introduction to Indexing**

Indexing is a technique used to speed up data retrieval in databases by organizing data in a way that enables efficient searching. An index contains a set of entries, each consisting of a search key and a pointer to the corresponding data record.

**Metrics for Evaluating Indices**

Indices can be evaluated based on:

* Access types supported, such as equality, range, or partial match queries
* Access time, the time taken to retrieve data using the index
* Insertion time, the time taken to add a new entry to the index
* Deletion time, the time taken to remove an entry from the index
* Space overhead, the additional storage space required for the index

**Ordered Indices**

Ordered indices store index entries in sorted order based on the search key. They include:

* **Primary index:** Specifies the sequential order of the file and is usually but not necessarily the primary key.
* **Secondary index:** Specifies an order different from the sequential order of the file.

**Dense Index Files**

Dense index files contain an index record for every search key value in the file, providing fast access to all data records.

**Sparse Index Files**

Sparse index files contain index records only for some search key values. They are applicable when records are sequentially ordered on the search key.

**Primary and Secondary Indices**

* **Primary index:** Enables efficient sequential scanning but is expensive for non-sequential access.
* **Secondary index:** Supports non-sequential access but is less efficient than a primary index for sequential scanning.

**Multilevel Index**

When the primary index is too large to fit in memory, a multilevel index can be created with a sparse index of the primary index called an outer index and the primary index as the inner index.

**Index Update**

Indices must be updated when data records are modified, which can affect the performance and overhead of database operations.

**Example**

Consider a table with attributes "Name" and "Phone". An index on "Name" allows for efficient retrieval of phone numbers given a name, while an index on "Phone" enables the lookup of names by phone number.

**Benefits and Limitations of Indexing**

* Benefits include faster data retrieval, improved query performance, and reduced I/O operations.
* Limitations include additional storage requirements, maintenance overhead during data modifications, and potential performance degradation for non-indexed data access patterns.

**Secondary Indices for Non-Key Fields**

Secondary indices can be created on non-key fields to facilitate efficient retrieval of records based on specific attributes, such as finding all instructors in a particular department or with a specified salary range.
