#  Summary of Lecture 5.5 - Relational Database Design5.pdf 
**Summary**
**Lossless Join Decomposition**

**Definition:**

A decomposition of a relation R into R1 and R2 is lossless join if the natural join of R1 and R2 is equal to R.

**Necessary and Sufficient Conditions:**

For the case of R = (R1, R2), we require that for all possible relations r on schema R,

```
r = πR1(r) ./ πR2(r)
```

A decomposition of R into R1 and R2 is lossless join if at least one of the following dependencies is in F:

```
R1 ∩ R2 → R1
R1 ∩ R2 → R2
```

**Example:**

Consider the Supplier Parts schema:

```
Supplier Parts(S#, Sname, City, P#, Qty)
```

Having dependencies:

```
S# → Sname
S# → City
(S#, P#) → Qty
```

Decompose as:

```
Supplier(S#, Sname, City, Qty)
Parts(P#, Qty)
```

Take Natural Join to reconstruct:

```
Supplier ./ Parts
```

We get back the original relation. Join is Lossless.

Common attribute S# is a superkey in Supplier.

Preserves all dependencies.

**Dependency Preservation**

**Definition:**

A decomposition of a relation R into D = {R1, R2, ..., Rn} is dependency preserving if:

```
(F1 ∪ F2 ∪ ... ∪ Fn)+ = F+
```

where Fi is the set of dependencies F+ that include only attributes in Ri.

**Testing:**

To check if a dependency α → β is preserved in a decomposition of R into D = {R1, R2, ..., Rn}, we apply the following test:

1. Compute F+.
2. For each schema Ri in D, compute Fi, the restriction of F+ to Ri.
3. Initialize F0 = φ.
4. For each restriction Fi, compute F0 = F0 ∪ Fi.
5. Compute F0+.
6. If F0+ = F+, then return true.
7. Otherwise, return false.

**Example:**

Consider the relation R(A, B, C, D, E, F) with dependencies:

```
F = {A → BCD, A → EF, BC → AD, BC → E, BC → F, B → F, D → E}
```

Decompose into:

```
R1(A, B, C, D)
R2(B, F)
R3(D, E)
```

Check if the dependency A → E is preserved:

1. Compute F+ as {A → BCD, A → EF, BC → AD, BC → E, BC → F, B → F, D → E}.
2. Compute F1 as {A → ABCD, B → B, C → C, D → D, AB → ABCD, BC → ABCD, CD → CD, AD → ABCD, ABC → ABCD, ABD → ABCD, ACD → ABCD, BCD → ABCD}
3. Compute F2 as {B → BF, F → F}
4. Compute F3 as {D → DE, E → E}
5. Compute F0 as F1 ∪ F2 ∪ F3 = {A → ABCD, B → B, C → C, D → D, AB → ABCD, BC → ABCD, CD → CD, AD → ABCD, ABC → ABCD, ABD → ABCD, ACD → ABCD, BCD → ABCD, B → BF, F → F, D → DE, E → E}
6. Compute F0+ as {A → ABCD, A → BF, A → DE, B → B, B → F, C → C, D → D, D → E, E → E, AB → ABCD, ABC → ABCD, ABD → ABCD, ACD → ABCD, AD → ABCD, BC → ABCD, BC → DE, BD → ABCD, CD → CD, DF → F}
7. Compare F0+ and F+: F0+ does not equal F+, so the dependency A → E is not preserved.

**Practice Problems**

**Lossless Join Decomposition**

1. Check if the decomposition of R into D is lossless:
   a) R(ABC) : F = {A → B, A → C}. D = R1(AB), R2(BC)
   b) R(ABCDEF) : F = {A → B, B → C, C → D, E → F}. D = R1(AB), R2(BCD), R3(DEF)
   c) R(ABCDEF) : F = {A → B, C → DE, AC → F}. D = R1(BE), R2(ACDEF)
   d) R(ABCDEG) : F = {AB → C, AC → B, AD → E, B → D, BC → A, E → G}
   i) D1 = R1(AB), R2(BC), R3(ABDE), R4(EG)
   ii) D2 = R1(ABC), R2(ACDE), R3(ADG)
   e) R(ABCDEFGHIJ) : F = {AB → C, B → F, D → IJ, A → DE, F → GH}
   i) D1 = R1(ABC), R2(ADE), R3(BF), R4(FGH), R5(DIJ)
   ii) D2 = R1(ABCDE), R2(BFGH), R3(DIJ)
   iii) D3 = R1(ABCD), R2(DE), R3(BF), R4(FGH), R5(DIJ)

**Dependency Preservation**

1. Check whether the decomposition of R into D is preserving dependency:
   a) R(ABCD) : F = {A → B, B → C, C → D, D → A}. D = {AB, BC, CD}
   b) R(ABCDEF) : F = {AB → CD, C → D, D → E, E → F}. D = {AB, CDE, EF}
   c) R(ABCDEG) : F = {AB → C, AC → B, BC → A, AD → E, B → D, E → G}. D = {ABC, ACDE, ADG}
   d) R(ABCD) : F = {A → B, B → C, C → D, D → B}. D = {AB, BC, BD}
   e) R(ABCDE) : F = {A → BC, CD → E, B → D, E → A}. D = {ABCE, BD}
