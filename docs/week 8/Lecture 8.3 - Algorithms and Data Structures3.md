#  Summary of Lecture 8.3 - Algorithms and Data Structures3.pdf 
**Summary**
**Module 38: Algorithms and Data Structures**

**Objectives and Outline**

* **Objective:**
    * Introduce non-linear data structures: graph, tree, hash table
    * Explore Binary Search Tree (BST)
    * Compare linear and non-linear data structures
* **Outline:**
    * Non-linear Data Structures
    * Binary Search Trees
    * Comparison of Linear and Non-Linear Data Structures

**Data Structure**

* A data structure organizes and stores data in memory for efficient access and modification.
* Types of data structures:
    * Linear Data Structures (e.g., array, list, stack, queue)
    * Non-linear Data Structures (e.g., graph, tree, hash table)
* Common operations: create, insert, delete, find/search, close
* Efficiency measured in time and space for these operations

**Non-linear Data Structures**

* Non-linear data structures allow for multiple paths to connect elements.
* Elements may not have a single path to connect to others.
* Common types include:
    * Graph: Undirected or Directed, Unweighted or Weighted
    * Tree: Rooted or Unrooted, Binary or n-ary, Balanced or Unbalanced
    * Hash Table: Array with lists and hash functions
    * Skip List: Multi-layered interconnected linked lists

**Non-linear Data Structures: Why?**

* Provide a balanced trade-off between extreme complexities of linear data structures.
* Offer satisfactory complexity for multiple operations.

**Graph**

* Collection of vertices (which store elements) and connecting edges (links): G =< V, E > where E ⊆ V × V
* Types: undirected/directed, unweighted/weighted, cyclic/acyclic, disconnected/connected

**Tree**

* Connected acyclic graph representing hierarchical relationships.
* Types: rooted/unrooted, binary/n-ary, balanced/unbalanced, disconnected (forest)/connected

**Tree Terminology**

* Root: topmost node
* Parent: node with a predecessor
* Child: node with a descendant
* Leaf: node with no children
* Level: distance of a node from the root

**Hash Table**

* Implements associative array abstract data type
* Uses a hash function to compute an index into an array of buckets or slots
* Types: static or dynamic schemes, open addressing, 2-choice hashing

**Binary Search Tree**

* Tree where all nodes hold the following properties:
    * Value of each node in the left subtree is less than the value of its root
    * Value of each node in the right subtree is greater than the value of its root

**Searching a Key in BST**

* Compare key with the root element.
* Recursively search the left or right subtree depending on the comparison result.
* Worst-case complexity: O(n)
* Best-case complexity: O(lg n)

**Comparison of Linear and Non-Linear Data Structures**

| Feature | Linear Data Structure | Non-Linear Data Structure |
|---|---|---|
| Data Arrangement | Linear order | Hierarchical or networked |
| Levels | Single level | Multiple levels |
| Implementation Complexity | Easy | Complex |
| Traversability | One way | Multiple ways |
| Examples | Array, stack, queue, linked list | Trees, graphs, skip list, hash map |

**Module Summary**

* Introduced non-linear data structures: graph, tree, hash table
* Explored Binary Search Tree as an adaptation of binary search
* Compared Linear and Non-Linear Data Structures
