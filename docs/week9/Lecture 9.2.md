#  Summary of Lecture 9.2.pdf 
**Summary**
**Module 42: Indexing and Hashing/2: Indexing/2**

**Objectives**

* To recap Balanced Binary Search Trees as options for optimal in-memory search data structures
* To understand the issues relating to external search data structures for persistent data
* To study 2-3-4 Tree as a precursor to B/B+-Tree for an efficient external data structure for database and index tables

**Module Recap**

* Appreciated the reasons for indexing database tables
* Understood the ordered indexes

**Module Outline**

* Balanced Binary Search Trees
* 2-3-4 Tree

**Balanced Binary Search Trees**

* Search Data Structures
    * Linear Search: O(n)
    * Binary Search: O(lg n)
* Balanced Binary Search Trees
    * Height of the tree (h) ∼ O(lg n)
    * Worst case time (n data items in the data structure):
        * Search: O(h) ∼ O(lg n)
* Balancing Guarantees
    * Worst-case: AVL Tree
    * Randomized: Randomized BST, Skip List
    * Amortized: Splay

**2-3-4 Tree**

* All leaves are at the same depth (the bottom level): Height, h ∼ O(lg n)
* All data is kept in sorted order
* Every node (leaf or internal) is a 2-node, 3-node or a 4-node (based on the number of links or children), and holds one, two, or three data elements, respectively
* Generalizes easily to larger nodes
* Extends to external data structures

**2-3-4 Trees: Search**

* Simple and natural extension of search in BST

**2-3-4 Trees: Insert**

* Search to find expected location
    * If it is a 2 node, change to 3 node and insert
    * If it is a 3 node, change to 4 node and insert
    * If it is a 4 node, split the node by moving the middle item to parent node, then insert
* Node Splitting
    * A 4-node is split as soon as it is encountered during a search from the root to a leaf
    * The 4-node that is split will
        * Be the root, or
        * Have a 2-node parent, or
        * Have a 3-node parent

**2-3-4 Trees: Insert: Example**

* Insert 10, 30, 60, 20, 50, 40, 70, 80, 15, 90, 100

**2-3-4 Trees: Delete**

* Locate the node n that contains the item theItem
* Find theItem’s inorder successor and swap it with theItem (deletion will always be at a leaf)
* If that leaf is a 3-node or a 4-node, remove theItem
* To ensure that theItem does not occur in a 2-node
    * Transform each 2-node encountered into a 3-node or a 4-node
    * Reverse different cases illustrated for splitting

**2-3-4 Tree**

* Advantages
    * All leaves are at the same depth (the bottom level): Height, h ∼ O(lg n)
    * Complexity of search, insert and delete: O(h) ∼ O(lg n)
    * All data is kept in sorted order
    * Generalizes easily to larger nodes
    * Extends to external data structures
* Disadvantages
    * Uses variety of node types – need to destruct and construct multiple nodes for converting a 2 Node to 3 Node, a 3 Node to 4 Node, for splitting etc.

**2-3-4 Trees**

* Consider only one node type with space for 3 items and 4 links
    * Internal node (non-root) has 2 to 4 children (links)
    * Leaf node has 1 to 3 items
    * Wastes some space, but has several advantages for external data structure
* Generalizes easily to larger nodes
    * All paths from root to leaf are of the same length
    * Each node that is not a root or a leaf has between \(\frac{n}{2}\) and n children.
    * A leaf node has between \((\frac{n-1}{2})\) and n − 1 values
    * Special cases:
        * If the root is not a leaf, it has at least 2 children.
        * If the root is a leaf, it can have between 0 and (n − 1) values.
* Extends to external data structures
    * B-Tree
    * 2-3-4 Tree is a B-Tree where n = 4

**Module Summary**

* Recapitulated the notions of Balanced Binary Search Trees as options for optimal in-memory search data structures
* Understood the issues relating to external data structures for persistent data
* Explored 2-3-4 Tree in depth as a precursor to B/B+-Tree for an efficient external data structure for database and index tables

**Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors.**

**Edited and new slides are marked with “PPD”.**
