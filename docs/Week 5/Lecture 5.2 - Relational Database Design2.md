# Lecture 5.2 - Relational Database Design2.pdf (PDF file)
**Summary**
Module 22 of Database Management Systems introduces the concept of Functional Dependencies (FDs), which are constraints on legal relations. FDs stipulate that values for a set of attributes (α) uniquely determine values for another set of attributes (β).

Armstrong's Axioms form the basis for deducing new FDs from existing ones. These axioms include Reflexivity (α→α if α⊆β), Augmentation (if α→β, then γα→γβ), and Transitivity (if α→β and β→γ, then α→γ).

The Closure of a set of FDs (F+) represents all FDs that can be logically inferred from the given FDs. Generating F+ involves applying Armstrong's Axioms until no new FDs can be derived. This process is both sound (generating only valid FDs) and complete (eventually deriving all valid FDs).

By understanding FDs, database designers can determine if a relation is in a "good" form and decompose it into a set of relations that satisfy lossless-join decomposition. This ensures data integrity and efficient data processing.
