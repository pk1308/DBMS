# Lecture 5.3 - Relational Database Design3.pdf (PDF file)
**Summary**
This module discusses relational database design using functional dependencies (FDs).

**FD Theory:**
- Armstrong's Axioms are used to derive new FDs from a given set.
- Closure of FDs generates all FDs logically implied by a set.
- Closure of attributes determines the attributes functionally determined by a set of attributes.

**Decomposition Using FDs:**
- Boyce-Codd Normal Form (BCNF) ensures that non-trivial FDs involve superkeys or attributes in candidate keys.
- Decomposing relations into BCNF guarantees lossless join but may not preserve dependencies.

**3NF (Third Normal Form):**
- Relaxes BCNF by allowing attributes in candidate keys but enforces dependency preservation.

**Normalization Goals:**
- Evaluate relation schemes for "good" form.
- Decompose schemes into lossless-join and dependency-preserving relations.

**Problems with Decomposition:**
- Potential lossiness, dependency checking issues, and query performance concerns exist.

**Limitations of BCNF:**
- BCNF may not prevent insertion anomalies in certain scenarios, suggesting the need for higher normal forms like 4NF.
