**Summary**

- The query processor subsystem compiles and executes DDL and DML state-
  ments.
- Transaction management ensures that the database remains in a consistent (cor-
  rect) state despite system failures. The transaction manager ensures that concur-
  rent transaction executions proceed without conﬂicts.
- The architecture of a database system is greatly inﬂuenced by the underlying com-
  puter system on which the database system runs. Database systems can be central-
  ized, or parallel, involving multiple machines. Distributed databases span multiple
  geographically separated machines.
- Database applications are typically broken up into a front-end part that runs at
  client machines and a part that runs at the backend. In two-tier architectures, the
  front end directly communicates with a database running at the back end. In three-
  tier architectures, the back end part is itself broken up into an application server
  and a database server.
- There are four diﬀerent types of database-system users, diﬀerentiated by the way
  they expect to interact with the system. Diﬀerent types of user interfaces have been
  designed for the diﬀerent types of users.
- Data-analysis techniques attempt to automatically discover rules and patterns from
  data. The ﬁeld of data mining combines knowledge-discovery techniques invented
  by artiﬁcial intelligence researchers and statistical analysts with eﬃcient imple-
  mentation techniques that enable them to be used on extremely large databases.
- Database-management system
  (DBMS)
- Database-system applications
- Online transaction processing
- Data analytics
- File-processing systems
- Data inconsistency
- Consistency constraints
- Data abstraction

  - Physical level
  - Logical level
  - View level
- Instance
- Schema

  - Physical schema
  - Logical schema
  - Subschema
- Physical data independence
- Data models
- Entity-relationship model
- Relational data model
- Semi-structured data model
- Object-based data model
- Database languages

  - Data-deﬁnition language
  - Data-manipulation language
    - Procedural DML
    - Declarative DML
    - nonprocedural DML
  - Query language
- Data-deﬁnition language

  - Domain Constraints
  - Referential Integrity
  - Authorization
    - Read authorization
    - Insert authorization
    - Update authorization
    - Delete authorization
- Metadata
- Application program
- Database design

  - Conceptual design
  - Normalization
  - Speciﬁcation of functional re-
    quirements
  - Physical-design phase
- Database Engine

  - Storage manager
    - Authorization and integrity
      manager
    - Transaction manager
    - File manager
    - Buﬀer manager
    - Data ﬁles
    - Data dictionary
    - Indices
- Query processor

  - DDL interpreter
  - DML compiler
  - Query optimization
  - Query evaluation engine
- Transaction

  - Atomicity
  - Consistency
  - Durability
  - Recovery manager
  - Failure recovery
  - Concurrency-control manager
- Database Architecture

  - Centralized
  - Parallel
  - Distributed
- Database Application Architecture

  - Two-tier
  - Three-tier
  - Application server
- Database administrator (DBA)


- 1 This chapter has described several major advantages of a database system. What
are two disadvantages?

- 2List ﬁve ways in which the type declaration system of a language such as Java
or C++ diﬀers from the data deﬁnition language used in a database.

- 3 List six major steps that you would take in setting up a database for a particular
enterprise.
- 4Suppose you want to build a video site similar to YouTube. Consider each of the
points listed in Section - 2 as disadvantages of keeping data in a ﬁle-processing
system. Discuss the relevance of each of these points to the storage of actual
video data, and to metadata about the video, such as title, the user who uploaded
it, tags, and which users viewed it.
- 5Keyword queries used in web search are quite diﬀerent from database queries.
List key diﬀerences between the two, in terms of the way the queries are speciﬁed
and in terms of what is the result of a query.

List four applications you have used that most likely employed a database system
to store persistent data.

- 7List four signiﬁcant diﬀerences between a ﬁle-processing system and a DBMS.
- 8Explain the concept of physical data independence and its importance in
database systems.
- 9List ﬁve responsibilities of a database-management system. For each responsi-
bility, explain the problems that would arise if the responsibility were not dis-
charged.
- 10List at least two reasons why database systems support data manipulation using
a declarative query language such as SQL, instead of just providing a library of
C or C++ functions to carry out data manipulation.
- 11Assume that two students are trying to register for a course in which there is only
one open seat. What component of a database system prevents both students
from being given that last seat?
- 12Explain the diﬀerence between two-tier and three-tier application architectures.
Which is better suited for web applications? Why?
- 13List two features developed in the 2000s and that help database systems handle
data-analytics workloads.
- 14Explain why NoSQL systems emerged in the 2000s, and brieﬂy contrast their
features with traditional database systems.
- 15Describe at least three tables that might be used to store information in a social-
networking system such as Facebook.
