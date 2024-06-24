#  Summary of Lecture 5.4 - Relational Database Design4.pdf 
**Summary**
**Algorithms for Functional Dependencies**

* **Attribute Set Closure:**
    * Computes the set of attributes that are functionally dependent on a given set of attributes.
    * Algorithm:
        * Start with the given set of attributes.
        * Repeatedly add to the set all attributes that are functionally dependent on the current set, until no new attributes can be added.
* **Extraneous Attributes:**
    * Identifies attributes that can be removed from a functional dependency without changing its meaning.
    * Tests:
        * For an attribute A in the left-hand side:
            * Compute the attribute closure of (α - A)+.
            * If it contains β, then A is extraneous.
        * For an attribute A in the right-hand side:
            * Compute the attribute closure of α+.
            * If it contains A, then A is extraneous.
* **Equivalence of Functional Dependency Sets:**
    * Two sets of functional dependencies are equivalent if they imply the same set of functional dependencies.
    * Tests:
        * **F+ = G+:** F logically implies all dependencies in G, and G logically implies all dependencies in F.
        * **F covers G:** All functional dependencies in G are logically implied by F.
        * **G covers F:** All functional dependencies in F are logically implied by G.

**Canonical Cover of Functional Dependencies**

* A canonical cover is a minimal set of functional dependencies that is equivalent to the original set of dependencies.
* Properties:
    * F+ = Fc+
    * No extraneous attributes
    * Each left-hand side of a functional dependency is unique.
* Algorithm:
    * Repeatedly apply the following steps:
        * Use the union rule to combine dependencies with the same left-hand side.
        * Find a dependency with an extraneous attribute and delete it.
    * Continue until the set of dependencies does not change.

**Practice Problems**

**Functional Dependency Implication:**

* For F = {A → BC, CD → E, E → C, D → AEH, ABH → BD, DH → BC}:
    * Check: BCD → H
    * Check: AED → C
* For F = {AB → CD, AF → D, DE → F, C → G, F → E, G → A}:
    * Check: CF → DF
    * Check: BG → E
    * Check: AF → G
    * Check: AB → EF

**Super Key Identification:**

* R(ABCDE) with F = {AB → C, DE → B, CD → E}
* R(ABCDE) with F = {AB → C, C → D, B → EA}

**Candidate Key Identification:**

* R(ABCDE) with F = {AB → C, DE → B, CD → E}
* R(ABCDE) with F = {AB → C, C → D, B → EA}

**Prime and Non-Prime Attribute Identification:**

* R(ABCDEF) with F = {AB → C, C → D, D → E, F → B, E → F}
* R(ABCDEF) with F = {AB → C, C → DE, E → F, C → B}
* R(ABCDEFGHIJ) with F = {AB → C, A → DE, B → F, F → GH, D → IJ}
* R(ABDLPT) with F = {B → PT, A → D, T → L}
* R(ABCDEFGH) with F = {E → G, AB → C, AC → B, AD → E, B → D, BC → A}
* R(ABCDE) with F = {A → BC, CD → E, B → D, E → A}
* R(ABCDEH) with F = {A → B, BC → D, E → C, D → A}

**Functional Dependency Equivalence:**

* F = {A → C, AC → D, E → AD, E → H}, G = {A → CD, E → AH}
* P = {A → B, AB → C, D → ACE}, Q = {A → BC, D → AE}

**Canonical Cover Computation:**

* F = {AB → CD, BC → D}
* F = {ABCD → E, E → D, AC → D, A → B}
