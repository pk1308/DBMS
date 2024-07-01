#  Summary of Lecture 5.5 - Relational Database Design5.pdf 
**Summary**
**Lossless Join Decomposition**

* **Definition:** A decomposition of a relation R into two relations R1 and R2 is lossless join if the natural join of R1 and R2 is equal to R.
* **Conditions for Lossless Join Decomposition:**
    * R1 ∪ R2 = R
    * R1 ∩ R2 ≠ ∅
    * R1 ∩ R2 → R1 or R1 ∩ R2 → R2

**Dependency Preservation**

* **Definition:** A decomposition of a relation R into two relations R1 and R2 preserves dependencies if every dependency in F (the set of functional dependencies on R) also holds in (F1 ∪ F2), where F1 and F2 are the sets of functional dependencies on R1 and R2, respectively.
* **Conditions for Dependency Preservation:**
    * (F1 ∪ F2 ∪ ... ∪ Fn)⁺ = F⁺
    * If (F1 ∪ F2 ∪ ... ∪ Fn)⁺ ⊂ F⁺, then the decomposition is not dependency preserving.
    * If (F1 ∪ F2 ∪ ... ∪ Fn)⁺ ⊃ F⁺, then this is not possible.

**Testing for Lossless Join Decomposition**

To determine whether a decomposition is lossless, check the following conditions:

* R1 ∪ R2 = R
* R1 ∩ R2 ≠ ∅
* R1 ∩ R2 → R1 or R1 ∩ R2 → R2

**Testing for Dependency Preservation Using Attribute Closure**

To test for dependency preservation, follow these steps:

* Compute F⁺, F1⁺, F2⁺, and so on.
* If (F1⁺ ∪ F2⁺ ∪ ... ∪ Fn⁺) = F⁺, then the decomposition preserves dependencies.
* If (F1⁺ ∪ F2⁺ ∪ ... ∪ Fn⁺) ⊂ F⁺, then the decomposition does not preserve dependencies.
* If (F1⁺ ∪ F2⁺ ∪ ... ∪ Fn⁺) ⊃ F⁺, then this is not possible.

**Testing for Dependency Preservation Using a Polynomial-Time Algorithm**

A more efficient method for testing dependency preservation is to use the following steps:

* Initialize result = α (the dependency to be tested)
* While changes occur to result, do the following:
    * For each Ri in the decomposition
        * t = (result ∩ Ri)⁺ ∩ Ri
        * result = result ∪ t
* If result contains all attributes in β (the right-hand side of the dependency), then the decomposition preserves the dependency.

**Practice Problems**

**Lossless Join Decomposition:**

* Check if the following decomposition of R is lossless:
    * R(ABC): F = {A → B, B → C}
    * D = {AB, BC}

**Dependency Preservation:**

* Check if the following decomposition of R preserves dependencies:
    * R(ABCDEF): F = {A → BC, B → C, C → D, D → E, E → F}
    * D = {AB, CDE, EF}
