#  Summary of Tutorial 4.4.pdf 
**Summary**
**Entities and Attributes**

In an entity-relationship (E-R) diagram, an entity represents a real-world object or concept. Entities are composed of a set of attributes, which are specific characteristics or properties that describe the entity. An entity set is a collection of entities of the same type, sharing similar attributes.

**Relationships**

Relationships establish associations between entities. A relationship set is a collection of relationships of a particular type. Cardinality describes the number of entities involved in a relationship. Cardinality constraints define the maximum and minimum number of entities that can participate in a relationship.

**Mapping Constraints**

Mapping constraints specify the relationships between entities and specify the cardinality constraints for each relationship. The most common mapping constraints are:

* Many-to-many: Both entities can have multiple relationships with each other.
* One-to-one: Each entity can have only one relationship with the other entity.
* One-to-many: Each entity in one set can have multiple relationships with entities in the other set, but each entity in the other set can have only one relationship with an entity in the first set.
* Many-to-one: Each entity in one set can have multiple relationships with an entity in the other set, but each entity in the other set can have only one relationship with an entity in the first set.

**Participation Constraints**

Participation constraints specify whether an entity must participate in a relationship. Total participation indicates that every entity in the entity set must participate in at least one relationship. Partial participation indicates that not all entities in the entity set must participate in a relationship.

**E-R Diagram Symbols**

E-R diagrams use specific symbols to represent entities, attributes, relationships, and constraints:

* Entity: A rectangle
* Attribute: An oval inside an entity
* Relationship: A diamond connected to entities
* Cardinality: Numbers or symbols on relationship lines
* Participation: Lines connecting entities to relationships

**Steps to Draw an E-R Diagram**

To create an E-R diagram, follow these steps:

1. **Identify Entities**: Determine the real-world objects or concepts involved and represent each as an entity.
2. **Add Attributes**: List the relevant characteristics or properties for each entity.
3. **Identify Relationships**: Determine the associations between entities and represent each as a relationship.
4. **Add Cardinality**: Specify the maximum and minimum number of entities that can participate in each relationship.

**Case Study**

**Scenario:** The Prescriptions-R-X pharmacy chain has requested a database design to manage its operations. Requirements are as follows:

* **Patients:**
    * Identified by SSN
    * Attribute: Name, Address, Age
* **Doctors:**
    * Identified by SSN
    * Attribute: Name, Specialty, Years of Experience
* **Relationship:**
    * Every patient has a primary physician (one-to-many)
    * Every doctor has at least one patient (one-to-many)
* **Prescriptions:**
    * Date, Quantity
    * Doctor prescribes one or more drugs for several patients (many-to-many)
    * Patient obtains prescriptions from several doctors (many-to-many)
* **Pharmaceutical Companies:**
    * Attribute: Name, Phone Number
* **Drugs:**
    * Attribute: Trade Name, Formula
    * Each drug sold by a specific pharmaceutical company (one-to-many)
* **Pharmacies:**
    * Attribute: Name, Address, Phone Number
* **Contracts:**
    * Relationship between pharmaceutical companies and pharmacies (many-to-many)
    * Attribute: Start Date, End Date, Contract Text
* **Contract Supervisors:**
    * Appointed by pharmacies for each contract (one-to-one)
* **Drug Prices:**
    * Relationship between drugs and pharmacies (many-to-many)
    * Attribute: Price

**E-R Diagram**

Using the provided requirements, an E-R diagram can be constructed as follows:

* **Entities:** Patient, Doctor, Prescription, Pharmaceutical Company, Drug, Pharmacy, Contract, Contract Supervisor
* **Attributes:** As per the requirements
* **Relationships:**
    * Patient - Prescribes - Prescription (many-to-many)
    * Doctor - Prescribes - Prescription (many-to-many)
    * Pharmaceutical Company - Sells - Drug (one-to-many)
    * Pharmacy - Contracts - Contract (many-to-many)
    * Contract - Supervised By - Contract Supervisor (one-to-one)
    * Pharmacy - Sells - Drug (many-to-many)
* **Cardinality and Participation:**
    * Patient - Doctor (one-to-many, mandatory)
    * Doctor - Patient (one-to-many, mandatory)
    * Prescription - Doctor (many-to-many, optional)
    * Prescription - Patient (many-to-many, optional)
    * Drug - Pharmaceutical Company (one-to-many, mandatory)
    * Contract - Pharmaceutical Company (many-to-many, optional)
    * Contract - Pharmacy (many-to-many, optional)
    * Contract - Contract Supervisor (one-to-one, mandatory)
    * Drug - Pharmacy (many-to-many, optional)
