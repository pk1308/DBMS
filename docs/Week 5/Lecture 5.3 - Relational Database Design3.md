#  Summary of Lecture 5.3 - Relational Database Design3.pdf 
**Summary**
## Module 23: Relational Database Design/3

### Objectives & Outline

- Functional Dependency Theory
- Armstrong's Axioms
- Closure of FDs
- Closure of Attributes
- Decomposition using FDs
- BCNF
- 3NF
- Normalization

### Functional Dependency Theory

**Definition:** A functional dependency (FD) α → β on a relation schema R is a constraint that, for any two tuples t1 and t2 in R, if t1[α] = t2[α], then t1[β] = t2[β].

### Armstrong's Axioms

Armstrong's axioms are a set of rules that can be used to infer new FDs from a given set of FDs.

- **Reflexivity:** If β ⊆ α, then α → β.
- **Augmentation:** If α → β, then γα → γβ.
- **Transitivity:** If α → β and β → γ, then α → γ.

### Closure of FDs

The closure of a set of FDs F, denoted F+, is the set of all FDs that can be inferred from F using Armstrong's axioms.

### Closure of Attributes

The closure of a set of attributes α, denoted α+, is the set of all attributes that are functionally determined by α under F.

### Decomposition using FDs

Decomposition is the process of breaking down a relation schema into smaller relation schemas. Decomposition using FDs can be used to ensure that the resulting relation schemas are in a "good" form, such as BCNF or 3NF.

### BCNF (Boyce-Codd Normal Form)

A relation schema R is in BCNF with respect to a set F of FDs if, for all FDs in F+ of the form α → β, where α ⊆ R and β ⊆ R, at least one of the following holds:

- α → β is trivial (that is, β ⊆ α).
- α is a superkey for R.

### 3NF (Third Normal Form)

A relation schema R is in 3NF if, for all α → β ∈ F+, at least one of the following holds:

- α → β is trivial (that is, β ⊆ α).
- α is a superkey for R.
- Each attribute A in β - α is contained in a candidate key for R.

### Normalization

Normalization is the process of decomposing a relation schema into a set of relation schemas that are in a "good" form, such as BCNF or 3NF. Normalization can help to reduce redundancy and improve the efficiency of queries.

### Problems with Decomposition

There are three potential problems to consider when decomposing a relation schema:

- **Lossiness:** The decomposition may result in a loss of data.
- **Dependency checking:** Dependency checking may require joins.
- **Query performance:** Some queries may become more expensive to execute.

### How good is BCNF?

BCNF is a good normal form, but it is not perfect. There are some database schemas in BCNF that do not seem to be sufficiently normalized. This suggests the need for higher normal forms, such as the Fourth Normal Form (4NF).

### Module Summary

- Introduced the theory of functional dependencies.
- Discussed issues in "good" design in the context of functional dependencies.
