# Summary of Lecture 4.2 - Formal Relational Query Languages2_annotated.pdf

**Summary**
**Predicate Logic**

Predicate logic, also known as predicate calculus, extends propositional logic or Boolean algebra. It introduces the concepts of predicates and quantifiers to better capture the meaning of statements that cannot be adequately expressed by propositional logic. Tuple Relational Calculus and Domain Relational Calculus are based on Predicate Calculus.

**Predicates**

A predicate is a property that a subject of a statement can have. It is a function that tells the truth value of the statement at the subject.

**Quantifiers**

Quantifiers are used in predicate logic to express the extent to which a predicate is true over a range of elements. There are two types of quantifiers:

- Universal Quantifier (∀): Asserts that a property is true for all values of a variable in a particular domain.
- Existential Quantifier (∃): Asserts that there is at least one element with a certain property.

**Tuple Relational Calculus (TRC)**

TRC is a non-procedural query language where each query is in the form:

```
{t | P(t)}
```

where:

- t = resulting tuples
- P(t) = predicate that specifies the conditions used to fetch t.

**TRC Example**

Find the first names of students whose age is greater than 21:

```
{t.Fname | Student(t) ∧ t.age > 21}
```

**Domain Relational Calculus (DRC)**

DRC is a non-procedural query language equivalent to TRC. Each query is expressed as:

```
{< x1, x2, . . . , xn > |P(x1, x2, . . . , xn)}
```

where:

- x1, x2, . . . , xn are domain variables
- P is a formula similar to the predicate calculus

**Equivalence of Relational Algebra (RA), TRC, and DRC**

The expressive power of RA, TRC, and DRC is equivalent. This equivalence means that any query that can be expressed in one language can be expressed in the other two languages. This equivalence is important for database theory and for understanding the different ways to query data.
