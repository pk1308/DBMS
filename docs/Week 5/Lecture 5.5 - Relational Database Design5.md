# Lecture 5.5 - Relational Database Design5.pdf (PDF file)
**Summary**
**Relational Database Design**

**Lossless Join Decomposition**

* A decomposition of a relation R into R1 and R2 is lossless if either R1 ∩ R2 → R1 or R1 ∩ R2 → R2 is in the set of functional dependencies (FDs) for R.
* This condition ensures that the original relation can be reconstructed by joining R1 and R2.

**Dependency Preservation**

* A decomposition of R into D = {R1, R2, ..., Rn} is dependency preserving if (F1 ∪ F2 ∪ ... ∪ Fn) = F, where:
    * Fi is the set of FDs including attributes only in Ri
* This ensures that all FDs in F are preserved in the decomposition.

**Testing Dependency Preservation**

* Test if a dependency α → β is preserved by:
    * Computing F0 = F1 ∪ F2 ∪ ... ∪ Fn
    * Check if β is in the attribute closure of α with respect to F0

**Practice Problems**

**Lossless Join Decomposition**

* Determine if the following decompositions are lossless:
    * R(ABC) : F = {A → B, A → C} → {R1(AB), R2(BC)}
    * R(ABCDEF) : F = {A → B, B → C, C → D, E → F} → {R1(AB), R2(BCD), R3(DEF)}
    * R(ABCDEF) : F = {A → B, C → DE, AC → F} → {R1(BE), R2(ACDEF)}
    * R(ABCDEG) : F = {AB → C, AC → B, AD → E, B → D, BC → A, E → G} → {R1(AB), R2(BC), R3(ABDE), R4(EG)}
    * R(ABCDEFGHIJ) : F = {AB → C, B → F, D → IJ, A → DE, F → GH} → {R1(ABC), R2(ADE), R3(BF), R4(FGH), R5(DIJ)}

**Dependency Preservation**

* Verify if the following decompositions preserve dependencies:
    * R(ABCD) : F = {A → B, B → C, C → D, D → A} → {AB, BC, CD}
    * R(ABCDEF) : F = {AB → CD, C → D, D → E, E → F} → {AB, CDE, EF}
    * R(ABCDEG) : F = {AB → C, AC → B, BC → A, AD → E, B → D, E → G} → {ABC, ACDE, ADG}
    * R(ABCD) : F = {A → B, B → C, C → D, D → B} → {AB, BC, BD}
    * R(ABCDE) : F = {A → BC, CD → E, B → D, E → A} → {ABCE, BD}
