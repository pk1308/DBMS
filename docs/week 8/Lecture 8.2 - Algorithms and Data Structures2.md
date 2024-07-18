#  Summary of Lecture 8.2 - Algorithms and Data Structures2.pdf 
**Summary**
## Objectives and Outline

**Learning Objectives:**

* Understand the concept of data structures
* Review linear data structures: arrays, lists, stacks, queues
* Review search algorithms: linear and binary

**Module Outline:**

* Data structures
* Linear data structures
* Search
    * Linear search
    * Binary search

## Data Structure

A data structure specifies the way of organizing and storing in-memory data that enables efficient access and modification of the data.

There are two main types of data structures:

* Linear data structures
* Non-linear data structures

Most data structures have a container for the data and typical operations that it needs to perform:

* Create
* Insert
* Delete
* Find/Search
* Close

Efficiency is measured in terms of time and space taken for these operations.

## Linear Data Structures

Linear data structures have data elements arranged in a linear or sequential manner such that each member element is connected to its previous and next element.

Examples of linear data structures include:

* Array
* Linked list
* Queue
* Stack

## Array

An array is a data structure that stores elements in contiguous memory locations. This allows for fast random access using its index.

**Advantages of Arrays:**

* Efficient random access (O(1))
* Simple implementation

**Disadvantages of Arrays:**

* Fixed size
* Costly insertion/deletion of elements in the middle of the array

## Linked List

A linked list is a data structure that stores elements in non-contiguous memory locations. Instead, each element stores a link (a pointer or a reference) to the location of the next element.

**Advantages of Linked Lists:**

* Flexible size
* Efficient insertion/deletion of elements at any position

**Disadvantages of Linked Lists:**

* Slower random access than arrays
* More complex implementation

## Search

Search algorithms are used to find an element in a data structure.

## Linear Search

Linear search is a sequential search algorithm that starts with the first element and compares each element with the given key until a match is found or the full list is traversed.

**Complexity of Linear Search:**

* Best case: O(1) (when the element is found at the beginning of the list)
* Worst case: O(n) (when the element is not found or is at the end of the list)

## Binary Search

Binary search is a more efficient search algorithm that works only on sorted lists.

Binary search compares the key with the middle element of the list and based on the comparison, it narrows down the search by dividing the list into two halves.

**Complexity of Binary Search:**

* Best case: O(1) (when the element is found at the middle of the list)
* Worst case: O(log n) (when the element is not found or is in either half)
