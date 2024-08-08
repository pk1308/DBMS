#  Summary of Lecture 9.3.pdf 
**Summary**
**Introduction**

B+-Tree Index Files are a generalization of 2-3-4 Tree, allowing for efficient external data storage in database and index tables.

**Properties of B+-Tree Index Files**

* Balanced binary search trees
* Multi-level index format
* Leaf nodes contain actual data pointers
* Leaf nodes are linked using a linked list, supporting both random access and sequential access
* Internal nodes contain pointers to child nodes and key values
* Leaf nodes store record pointers and key values
* Intermediate nodes branch from a range of values

**Search**

* Traverses intermediary nodes to locate the leaf node containing the target record
* Sequential search is performed at the leaf node

**Insertion**

* Inserts new records by splitting leaf nodes to maintain fill factor, balance, and order
* If the leaf node is full, it is split, and a new leaf node is created
* The intermediate node is also split, if necessary, to add a branch to the new leaf node

**Deletion**

* Removes records by redistributing entries or merging underfull leaf nodes
* If a node becomes underfull, it is merged with a sibling node
* Intermediate nodes are also updated to reflect the changes

**File Organization**

* B+-Tree index files automatically reorganize themselves, unlike indexed-sequential files (ISAM)
* Small, local changes can be made during insertions and deletions, without the need for periodic reorganization of the entire file

**Handling Non-Unique Keys**

* Duplicate search keys are allowed
* Search keys in internal nodes may not be unique, but they are guaranteed to be less than or equal to the following key value
* Modified find procedure is used to traverse consecutive leaves to find all occurrences of a duplicate key

**Updates**

**Insertion**

* Finds the leaf node where the search-key value belongs
* Inserts the new entry into the leaf node
* If the leaf node is full, splits the node and propagates the split upwards

**Deletion**

* Removes the record from the main file and from the bucket (if present)
* Removes the search-key value and pointer from the leaf node
* Merges underfull nodes or redistributes entries to maintain balance

**File Organization**

* B+-Tree File Organization uses leaf nodes to store records instead of pointers
* Leaf nodes are required to be half full
* Insertion and deletion are handled similarly to B+-Tree index updates

**Non-Unique Keys**

* Alternatives to storing duplicate keys in buckets include:
    * Buckets on separate blocks (not recommended)
    * List of tuple pointers with each key (extra code, deletion overhead)
    * Making the search key unique by adding a record-identifier (extra storage overhead, simpler code)

**Record Relocation and Secondary Indices**

* If a record moves, secondary indices using record pointers must be updated
* To reduce the cost of node splits, the primary-index search key can be used in the secondary index instead of the record pointer
* Extra traversal of the primary index is required, but node splits are cheaper

**Indexing Strings**

* Variable length strings as keys introduce challenges:
    * Variable fanout
    * Prefix compression:
        * Key values at internal nodes can be prefixes of full keys
        * Keys in leaf nodes can be compressed by sharing common prefixes
