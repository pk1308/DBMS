#  Summary of Lecture 8.1 - Algorithms and Data Structures1.pdf 
**Summary**
**Module 36: Algorithms and Data Structures/1: Algorithms and Complexity Analysis**

**Objectives**

* Define Algorithms and their difference with Programs
* Analyze algorithms for performance of time, space, power, etc.
* Introduce Asymptotic notation for representation of complexity
* Consider complexity of common algorithms

**Outline**

* Algorithms and Programs
* Analysis of Algorithms
* Complexity Chart

**Algorithms and Programs**

* **Algorithm:** A finite sequence of well-defined, computer-implementable instructions, typically to solve a class of specific problems or to perform a computation.
* **Program:** A collection of instructions that can be executed by a computer to perform a specific task.
* A program implements an algorithm.
* A program may or may not terminate.

**Analysis of Algorithms**

* **Why Analyze?**
    * Practical reasons:
        * Resources are scarce
        * Greed to do more with less
        * Avoid performance bugs
    * Core Issues:
        * Predict performance
        * Compare algorithms
        * Provide guarantees
        * Understand theoretical basis
* **What to Analyze?**
    * Time
    * Space
* **How to Analyze?**
    * Counting Models
    * Asymptotic Analysis
* **Where to Analyze?**
    * Best Case
    * Worst Case
    * Average Case
    * Probabilistic Case
    * Amortized Case

**Counting Models**

* Core Idea: Total running time = Sum of cost × frequency for all operations
* Need to analyze program to determine set of operations
* Cost depends on machine, compiler
* Frequency depends on algorithm, input data

**Asymptotic Analysis**

* Core Idea: Cannot compare actual times; hence compare Growth or how time increases with input size
* Function Approximation (tilde (˜) notation)
* Common Growth Functions
* Big-Oh (O(.)), Big-Omega (Ω(.)), and Big-Theta (Θ(.)) Notations
* Solve recurrence with Growth Functions

**Complexity Chart**

* Presents the complexity of common algorithms in terms of time and space requirements
* Big-O notation is used to represent the worst-case complexity of an algorithm
* Different complexities are denoted by different symbols, e.g., O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n)

**Module Summary**

* Importance of analyzing algorithms for performance and efficiency
* Asymptotic notation for representing algorithm complexity
* Different types of analysis scenarios (best case, worst case, etc.)
* Complexity Chart for comparing common algorithms
