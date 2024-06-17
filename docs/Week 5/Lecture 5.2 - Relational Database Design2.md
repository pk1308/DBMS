# Lecture 5.2: Relational Database Design

## Functional Dependencies

### Definition

- Constraints on the set of legal relations.
- Require that the value for a certain set of attributes determines uniquely the value for another set of attributes.
- A generalization of the notion of a key.

### Formal Definition

- For a relation schema ( R ), ( $\\alpha \\subseteq R$ ) and ( $\\beta \\subseteq R $).
- The functional dependency ( $\\alpha \\to \\beta $) holds on ( R ) if for any legal relations ( r(R) ), whenever any two tuples ( $t_1$ ) and ( $t_2$ ) of ( $r$ ) agree on the attributes ( $ \\alpha $ ), they also agree on the attributes ( $\\beta$ ).
- Example: ( $A \\to B$ ) does not hold, but ( $B \\to A$ ) holds for a certain instance.

### Keys

- **Superkey:** ( $K$ ) is a superkey for relation schema ( $R$ ) if and only if ($ K \\to R \\ $).
- **Candidate Key:** ( K ) is a candidate key for ( R ) if and only if ( $K \\to R$ ) and for no ($\\alpha \\subset K $), ( $\\alpha \\to R $).

### Practical Examples

- **Schema:** `inst_dept(ID, name, salary, dept_name, building, budget)`
- Expected FDs:
  - `dept_name → building`
  - `dept_name → budget`
  - `ID → budget`
- Unexpected FD:
  - `dept_name → salary`

### Trivial Functional Dependencies

- A functional dependency is trivial if it is satisfied by all instances of a relation.
- Example: ( $\\text{ID, name} \\to \\text{ID} $) and ( $\\text{name} \\to \\text{name} $).
- Generally, ( $\\alpha \\to \\beta $ ) is trivial if ( $\\beta \\subseteq \\alpha $).

______________________________________________________________________

## Armstrong’s Axioms

### Definition

- Given a set of FDs ( F ), infer new dependencies using:
  - **Reflexivity:** If ( $\\beta \\subseteq \\alpha$ ), then ( \\alpha \\to \\beta ).
  - **Augmentation:** If ( $\\alpha \\to \\beta $ ), then ( $\\gamma\\alpha \\to \\gamma\\beta $).
  - **Transitivity:** If ( $\\alpha \\to \\beta $) and ( $\\beta \\to \\gamma $), then ( $\\alpha \\to \\gamma $).

### Closure

- The closure of a set of FDs ( $F$ ) is the set ( $F^+ $) of all FDs logically implied by ( F ).
- Example:
  - ( $F = { A \\to B, B \\to C }$ )
  - ( $F^+ = { A \\to B, B \\to C, A \\to C } $)

### Properties

- Axioms are **sound** (generate only FDs that hold) and **complete** (generate all FDs that hold).

______________________________________________________________________

## Module Summary

- Introduced the notion of Functional Dependencies.
- Explained Armstrong’s Axioms and their application to infer new FDs.
- Discussed the concept of the closure of a set of FDs.
