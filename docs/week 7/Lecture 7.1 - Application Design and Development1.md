#  Summary of Lecture 7.1 - Application Design and Development1.pdf 
**Summary**
**Module 31: Application Design and Development**

**Objectives and Outline**

* Understand the diversity and commonality of application programs
* Classify and understand the evolution of application architectures
* Examine the architecture of sample applications

**Application Programs and Architecture**

**Application Programs**

Application programs encompass a wide range of domains and functionalities, including:

* Financial: netbanking, share market, insurance, payment gateways
* Travel and tourism: travel reservations, accommodation, transportation, navigation
* Communication: live interaction, intermittent interaction, mail, social media
* Knowledge discovery: static, Q&A
* Sports: cricket, tennis
* Software engineering: issue tracking, VCS, online IDE
* Library: digital library, archives
* Education: eLearning, MOOCs
* Document processing: editing, website/blog
* Health: telemedicine, national healthcare apps
* Organizational ERP: students, faculty, course, patient, doctor, inventory, customers

**Characteristic of Application Programs**

Despite their diversity, application programs share commonalities:

* **Diversity:** Domain, functionality, user base, response time, scale
* **Unity:**
    * Use relational database management systems (RDBMS) like Oracle, DB2 MySQL, PostgreSQL
    * Functionally split into frontend, middle, and backend layers

**Application Architecture**

**Frontend/Presentation Layer/Tier**

* Interacts with the user: display/view, input/output
* Interfaces can be browser-based, mobile app, or custom

**Middle/Application/Business Logic Layer/Tier**

* Implements the functionality of the application
* Links front and backend layers
* Authentication, search/browse logic, pricing, cart management, payment handling, order management, delivery management

**Backend/Data Access Layer/Tier**

* Manages persistent data
* User, cart, inventory, order, vendor databases

**Application Architectures: Layers**

* **Presentation Layer / Tier:**
    * Model-View-Controller (MVC) architecture
        * Model: business logic
        * View: presentation of data, depends on display device
        * Controller: receives events, executes actions, and returns a view to the user
* **Business Logic Layer / Tier:**
    * Provides high level view of data and actions on data
    * Often using an object data model
* **Data Access Layer / Tier:**
    * Interfaces between business logic layer and the underlying database
    * Provides mapping from object model of business layer to relational model of database

**Application Architecture (2): MVC**

MVC architecture separates the application into three components:

* Model: Business logic
* View: Presentation of data
* Controller: Handles user interactions and updates the view

**Application Architecture (3): User Interface**

* Web browsers have become the de-facto user interface to databases
* Mobile devices are becoming increasingly popular

**Application Architecture (4): Business Logic Layer**

* Provides abstractions of entities
* Enforces business rules for carrying out actions
* Supports workflows for carrying out tasks involving multiple participants

**Application Architecture (5): Object-Relational Mapping**

* Allows application code to be written on top of object-oriented data model while storing data in a relational database
* Schema designer provides a mapping between object data and relational schema

**Application Architecture (6): Data Access Layer**

* Issues of data access and update will be discussed later

**Architecture Classification**

**1-Tier Architecture**

* All components (interface, middleware, back-end data) are located on a single server or platform

**2-Tier Architecture**

* Client-server architecture
* Direct communication between client and server

**3-Tier Architecture**

* Separates presentation, logic, and data access tiers
* Most widely used architecture for DBMS design

**n-Tier Architecture**

* Distributes components of the 3 tiers between different servers and adds interfaces tiers

**Sample Applications in Multiple Tiers**

* Financial: 3-tier
* Travel and tourism: 3-tier
* Communication: 3-tier
* Knowledge discovery: 2-tier
* Sports: 2-tier
* Software engineering: 3-tier
* Library: 3-tier
* Education: 3-tier
* Document processing: 3-tier
* Health: 3-tier
* Organizational ERP: 3-tier
