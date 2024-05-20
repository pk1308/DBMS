# Lecture 4.4 - Entity-Relationship Model2_annotated.pdf (PDF file)
**Summary**
**Entity-Relationship (ER) Diagram**

**Components:**

* **Entity Sets:** Represent real-world entities (e.g., Student, Course).
* **Relationship Sets:** Represent relationships between entities (e.g., Advisor).

**ERD Notation:**

* Rectangles: Entity sets
* Diamonds: Relationship sets
* Underlining: Primary key attributes
* Roles: Labels on lines connecting entities to relationship sets
* Minimum and maximum cardinality constraints: l..h (e.g., 1..*, 0..1)
* Total participation: Double line
* Partial participation: Single line

**Entity Sets:**

* Strong entity sets: Every entity must participate in the set.
* Weak entity sets: Entities dependent on another entity set (identifying entity set).

**Relationship Sets:**

* One-to-one: Each entity in one set relates to exactly one entity in the other set.
* Many-to-one: Each entity in one set relates to multiple entities in the other set.
* Many-to-many: Entities in both sets relate to multiple entities in the other set.

**ER Model to Relational Schema Translation:**

* Entity sets are represented by tables with the same attributes.
* Relationship sets are represented by tables with the primary keys of the participating entity sets.
* Complex attributes are flattened into separate attributes.
* Multivalued attributes are represented by a separate table.

**Redundancy in Schema:**

* Many-to-one/one-to-many relationships can be represented by adding an attribute to the "many" side instead of creating a separate schema.
* Weak entity sets are redundant and can be represented by the identifying entity set.
**Lec file**
# Lecture 4.4 - Entity-Relationship Model2_annotated.pdf (PDF file)
![Alt text](<./Lecture 4.4 - Entity-Relationship Model2_annotated.pdf>){ type=application/pdf style="min-height:100vh;width:100%" }