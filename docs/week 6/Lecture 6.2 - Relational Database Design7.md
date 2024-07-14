#  Summary of Lecture 6.2 - Relational Database Design7.pdf 
**Summary**
**Module 27: Relational Database Design/7: Normal Forms**

**Objectives:**

- Learn the Decomposition Algorithm for a Relation to 3NF
- Learn the Decomposition Algorithm for a Relation to BCNF

**Outline:**

- Decomposition to 3NF
    - Test
    - Algorithm
    - Practice Problem
- Decomposition to BCNF
    - Test
    - Algorithm
    - Practice Problem
- Comparison
- Module Summary

**Decomposition to 3NF**

**Motivation:**

- In certain situations,
    - BCNF is not dependency preserving, and
    - Efficient checking for FD violation on updates is important.
- Solution: define a weaker normal form, called Third Normal Form (3NF)
    - Allows some redundancy (with resultant problems; as seen above)
    - But functional dependencies can be checked on individual relations without computing a join
    - There is always a lossless-join, dependency-preserving decomposition into 3NF.

**3NF Definition:**

- A relational schema R is in 3NF if for every FD X → A associated with R either
    - A ⊆ X (that is, the FD is trivial) or
    - X is a superkey of R or
    - A is part of some candidate key (not just superkey!).

- A relation in 3NF is naturally in 2NF.

**Testing for 3NF:**

- Optimization: Need to check only FDs in F, need not check all FDs in F+.
- Use attribute closure to check for each dependency α → β, if α is a superkey.
- If α is not a superkey, we have to verify if each attribute in β is contained in a candidate key of R.
    - This test is rather more expensive, since it involves finding candidate keys.
    - Testing for 3NF has been shown to be NP-hard.
    - Decomposition into 3NF can be done in polynomial time.

**Algorithm:**

- Given: relation R, set F of functional dependencies
- Find: decomposition of R into a set of 3NF relation Ri
- Algorithm:
    a) Eliminate redundant FDs, resulting in a canonical cover Fc of F.
    b) Create a relation Ri = XY for each FD X → Y in Fc.
    c) If the key K of R does not occur in any relation Ri, create one more relation Ri = K.

**Example:**

- Relation schema:
    - cust banker branch = (customer id, employee id, branch name, type)
- Functional dependencies:
    a) customer id, employee id → branch name, type
    b) employee id → branch name
    c) customer id, branch name → employee id
- The for loop generates following 3NF schema:
    - (customer id, employee id, type)
    - (employee id, branch name)
    - (customer id, branch name, employee id)

**Practice Problems:**

- R = ABCDEFGH
    - FDs = {A → B, ABCD → E, EF → GH, ACDF → EG}
- R = CSJDPQV
    - FDs = {C → CSJDPQV, SD → P, JP → C, J → S}
- R = ABCDEFGH
    - F = {A → CD, ACF → G, AD → BEF, BCG → D, CF → AH, CH → G, D → B, H → DEG}
- R = ABCDE
    - F = {A → B, A → C, C → D, A → E}
- R = ABCDE
    - F = {A → BC, CD → E, B → D, E → A}
- R = ABCD
    - F = {A → D, AB → C, AD → C, B → C, D → AB}

**Decomposition to BCNF**

**BCNF Definition:**

- A relation schema R is in BCNF with respect to a set F of FDs if for all FDs in F+ of the form α → β, where α ⊆ R and β ⊆ R at least one of the following holds:
    - α → β is trivial (that is, β ⊆ α).
    - α is a superkey for R.

**Testing for BCNF:**

- To check if a non-trivial dependency α → β causes a violation of BCNF
    a) Compute α+ (the attribute closure of α), and
    b) Verify that it includes all attributes of R, that is, it is a superkey of R.
- Simplified test: To check if a relation schema R is in BCNF, it suffices to check only the dependencies in the given set F for violation of BCNF, rather than checking all dependencies in F+.
- However, simplified test using only F is incorrect when testing a relation in a decomposition of R.

**Testing for BCNF Decomposition:**

- To check if a relation Ri in a decomposition of R is in BCNF,
    - Either test Ri for BCNF with respect to the restriction of F to Ri (that is, all FDs in F+ that contain only attributes from Ri),
    - Or use the original set of dependencies F that hold on R, but with the following test:
        - For every set of attributes α ⊆ Ri, check that α+ (the attribute closure of α)
            - Either includes no attribute of Ri − α, or
            - Includes all attributes of Ri.
        - If the condition is violated by some α → β in F, the dependency α → (α+ − α) ∩ Ri can be shown to hold on Ri, and Ri violates BCNF.
            - We use above dependency to decompose Ri.

**Testing Dependency Preservation:**

- Using Closure Set of FD (Exp. Algo.):
    - Consider the example given below, we will apply both the algorithms to check dependency preservation and will discuss the results.
    - R (A, B, C, D)
    - F = {A → B, B → C, C → D, D → A}
    - Decomposition: R1(A, B) R2(B, C) R3(C, D)
        - A → B is preserved on table R1
        - B → C is preserved on table R2
        - C → D is preserved on table R3
        - We have to check whether the one remaining FD: D→A is preserved or not.
    - R1
        - F1={A → AB, B → BA}
    - R2
        - F2={B → BC, C → CB}
    - R3
        - F3={C → CD, D → DC}
        - F0 = F1 ∪ F2 ∪ F3.
        - Checking for: D → A in F0+
        . D → C (from R3), C → B (from R2), B → A (from R1) : D→ A (By Transitivity)
    - Hence all dependencies are preserved.
- Using Closure of Attributes (Poly. Algo.):
    - R(ABCD) :. F = {A → B, B → C, C → D, D → A}
    - Decomp = {AB, BC, CD}
    - On projections:
        - (D) + /F1 = D. (D) + /F2 = D. (D) + /F3 = D. So, D → A could not be preserved.
    - In the previous method we saw the dependency was preserved. In reality also it is preserved.
    - Therefore the polynomial time algorithm may not work in case of all examples. To prove preservation, Algo 2 is sufficient but not necessary whereas Algo 1 is both sufficient as well as necessary.

**Algorithm:**

a) For all dependencies A → B in F+, check if A is a superkey
- By using attribute closure
b) If not, then
- Choose a dependency in F+ that breaks the BCNF rules, say A → B
- Create R1 = AB
- Create R2 = (R − (B − A))
- Note that: R1 ∩ R2 = A and A → AB (= R1), so this is lossless decomposition
c) Repeat for R1, and R2
- By defining F1+ to be all dependencies in F that contain only attributes in R1
- Similarly F2+

**Example:**

- R = (A, B, C)
- F = {A → B, B → C}
- Key = {A}
- R is not in BCNF (B → C but B is not superkey)
- Decomposition
    - R1 = (B, C)
    - R2 = (A, B)

**Practice Problems:**

- R = ABCDE. F = {A → B, BC → D}
- R = ABCDEH. F = {A → BC, E → HA}
- R = CSJDPQV. F = {C → CSJDPQV, SD → P, JP → C, J → S}
- R = ABCD. F = {C → D, C → A, B → C}

**Comparison of BCNF and 3NF**

| Feature | 3NF | B
