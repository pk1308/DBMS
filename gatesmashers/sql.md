# SQL

#### key

- Candidate Key -> Primary Key
- Candidate key -> keys which are not used as primary key are called alternative key

#### Primary Key

- {Unique + Not Null }

#### Foreign Key

- Refrencing Table

  - insert course violation if FK is not in in refrenced table
- Refrenced Table

  - on delete cascade
  - on delete set null
  - on delete no action
  - on update cascade
  - on update set null
  - on update  no action

**Summary of Relational Algebra Operators**

| Operator    | Description                                      |
| ----------- | ------------------------------------------------ |
| σ          | Select                                           |
| π          | Project                                          |
| ∪          | Union                                            |
| −          | Difference                                       |
| ∩          | Intersection                                     |
| ×          | Cartesian Product                                |
| $ \rho$   | Rename                                           |
| $\bowtie$ | Natural Join                                     |
| SUM         | Computes the sum of a specified column           |
| AVG         | Computes the average of a specified column       |
| MAX         | Computes the maximum value of a specified column |
| MIN         | Computes the minimum value of a specified column |

## DDL- Data Definition Language

- Create
- Alter
- Drop
- Truncate
- Rename

## DML - Data Defination Language

- Select
- Insert
- update
- Delete

## DCL - Data Control Language

- Grant
- Revoke

## TCL - Transaction Control Language

- Commit
- Rollback
- save point

## Constraints

- primary key
- foreign key
- check
- unique
- default
- Not null

## Create Table - DDL

```pgsql
 create table <table name> ( col1name  datattype , 
				col2name  datattype ,
				 col1name  datattype);
```

```pgsql
desc tablename;

```

```pgsql
create table student ( ID varchar(5),name varchar(20) not null,
			dept name varchar(20),tot cred numeric(3, 0),
			primary key (ID),
			foreign key (dept name) references department);
```

![1718702547444](image/sql/1718702547444.png)

![1718702694723](image/sql/1718702694723.png)

## Alter - DDL

- add columns
- remove columns
- modify datatype
- modify datatype length
- add constraints
- remove constraints
- rename constraints

![1718702990524](image/sql/1718702990524.png)

![1718703212847](image/sql/1718703212847.png)

![1718703277575](image/sql/1718703277575.png)

![1718703482048](image/sql/1718703482048.png)

## Alter vs Update

- alter - DDL
- update - DML

## Delete Vs Drop Vs Truncate

- Delete - DML
- Drop - DDL - drop table
- Truncate - DDL -   no back up even in roll back

## Constraints

Condition for columns or attribute

- unique
- not null
- primary -> unique + not null
- check
- forgien key
- default

## Nested subquery Vs correlated sub query vs joins

![1718715702472](image/sql/1718715702472.png)

![1718716187738](image/sql/1718716187738.png)

Instructor = e1=

| id | salary |
| -- | ------ |
| 1  | 10000  |
| 2  | 20000  |
| 3  | 20000  |
| 4  | 30000  |
| 5  | 40000  |
| 6  | 5000   |

Instructor = e2=

| id | salary |
| -- | ------ |
| 1  | 10000  |
| 2  | 20000  |
| 3  | 20000  |
| 4  | 30000  |
| 5  | 40000  |
| 6  | 5000   |

**first row**

| id | e1.salary | id | e2.salary | e2.salary > e1.salary | count       |
| -- | --------- | -- | --------- | ---------------------- | ----------- |
| 1  | 10000     | 1  | 10000     | False                  | 0           |
| 1  | 10000     | 2  | 20000     | True                   | 1           |
| 1  | 10000     | 3  | 20000     | True                   | 2           |
| 1  | 10000     | 4  | 30000     | True                   | **2** |
| 1  | 10000     | 5  | 40000     | True                   | 3           |
| 1  | 10000     | 2  | 50000     | True                   | 4           |

**Second row**

| id | e1.salary | id | e2.salary | e2.salary > e1.salary | count       |
| -- | --------- | -- | --------- | ---------------------- | ----------- |
| 2  | 20000     | 1  | 10000     | False                  | 0           |
| 2  | 20000     | 2  | 20000     | False                  | 0           |
| 2  | 20000     | 3  | 20000     | False                  | 0           |
| 2  | 20000     | 4  | 30000     | True                   | **1** |
| 2  | 20000     | 5  | 40000     | True                   | 2           |
| 2  | 20000     | 2  | 50000     | True                   | 3           |

# Joins

employee=

| PK  |        |         |
| --- | ------ | ------- |
| Eno | E-name | Address |
| 1   | Ram    | delhi   |
| 2   | varun  | chd     |
| 3   | Ravi   | chd     |
| 4   | Amrit  | Delhi   |
| 5   | Nitin  | noida   |

Department =

| PK     |         | FK  |
| ------ | ------- | --- |
| Dep_no | Name    | eno |
| D1     | HR      | 1   |
| D2     | IT      | 2   |
| D3     | MRKT    | 4   |
| D4     | FINANCE | 5   |

# Natural join

cross poduct + condition = join

employee natural join  department = cross poduct + condition $empolyee.eno = department.eno$

cross product =

```pgsql
select * from employee , department
```

|              |        |         |        |         |                 |
| ------------ | ------ | ------- | ------ | ------- | --------------- |
| employee.Eno | E-name | Address | Dep_no | Name    | departmment.eno |
| 1            | Ram    | delhi   | D1     | HR      | 1               |
| 1            | Ram    | delhi   | D2     | IT      | 2               |
| 1            | Ram    | delhi   | D3     | MRKT    | 4               |
| 1            | Ram    | delhi   | D4     | FINANCE | 5               |
| 2            | varun  | chd     | D1     | HR      | 1               |
| 2            | varun  | chd     | D2     | IT      | 2               |
| 2            | varun  | chd     | D3     | MRKT    | 4               |
| 2            | varun  | chd     | D4     | FINANCE | 5               |
| 3            | Ravi   | chd     | D1     | HR      | 1               |
| 3            | Ravi   | chd     | D2     | IT      | 2               |
| 3            | Ravi   | chd     | D3     | MRKT    | 4               |
| 3            | Ravi   | chd     | D4     | FINANCE | 5               |
| 4            | Amrit  | Delhi   | D1     | HR      | 1               |
| 4            | Amrit  | Delhi   | D2     | IT      | 2               |
| 4            | Amrit  | Delhi   | D3     | MRKT    | 4               |
| 4            | Amrit  | Delhi   | D4     | FINANCE | 5               |
| 5            | Nitin  | noida   | D1     | HR      | 1               |
| 5            | Nitin  | noida   | D2     | IT      | 2               |
| 5            | Nitin  | noida   | D3     | MRKT    | 4               |
| 5            | Nitin  | noida   | D4     | FINANCE | 5               |

```pgsql
select * from employee  department empolyee.eno = department.eno
```

|     |        |         |        |         |     |                                   |
| --- | ------ | ------- | ------ | ------- | --- | --------------------------------- |
| Eno | E-name | Address | Dep_no | Name    | eno | `empolyee.eno = department.eno` |
| 1   | Ram    | delhi   | D1     | HR      | 1   | True                              |
| 1   | Ram    | delhi   | D2     | IT      | 2   | False                             |
| 1   | Ram    | delhi   | D3     | MRKT    | 4   | False                             |
| 1   | Ram    | delhi   | D4     | FINANCE | 5   | False                             |
| 2   | varun  | chd     | D1     | HR      | 1   | False                             |
| 2   | varun  | chd     | D2     | IT      | 2   | True                              |
| 2   | varun  | chd     | D3     | MRKT    | 4   | False                             |
| 2   | varun  | chd     | D4     | FINANCE | 5   | False                             |
| 3   | Ravi   | chd     | D1     | HR      | 1   | False                             |
| 3   | Ravi   | chd     | D2     | IT      | 2   | False                             |
| 3   | Ravi   | chd     | D3     | MRKT    | 4   | False                             |
| 3   | Ravi   | chd     | D4     | FINANCE | 5   | False                             |
| 4   | Amrit  | Delhi   | D1     | HR      | 1   | False                             |
| 4   | Amrit  | Delhi   | D2     | IT      | 2   | False                             |
| 4   | Amrit  | Delhi   | D3     | MRKT    | 4   | True                              |
| 4   | Amrit  | Delhi   | D4     | FINANCE | 5   | False                             |
| 5   | Nitin  | noida   | D1     | HR      | 1   | False                             |
| 5   | Nitin  | noida   | D2     | IT      | 2   | False                             |
| 5   | Nitin  | noida   | D3     | MRKT    | 4   | False                             |
| 5   | Nitin  | noida   | D4     | FINANCE | 5   | True                              |

### result=

|     |        |         |        |         |     |
| --- | ------ | ------- | ------ | ------- | --- |
| Eno | E-name | Address | Dep_no | Name    | eno |
| 1   | Ram    | delhi   | D1     | HR      | 1   |
| 2   | varun  | chd     | D2     | IT      | 2   |
| 4   | Amrit  | Delhi   | D3     | MRKT    | 4   |
| 5   | Nitin  | noida   | D4     | FINANCE | 5   |

```pgsql
select E-name from employee  natural join department
```

|        |
| ------ |
| E-name |
| Ram    |
| varun  |
| Amrit  |
| Nitin  |

# self Join

| S_id | course_id | since |
| ---- | --------- | ----- |
| s1   | c1        | 2016  |
| s2   | c2        | 2017  |
| s1   | c2        | 2017  |

find student who is enrolled in two courses ?

cross prduct

| S_id (Left) | course_id (Left) | since (Left) | S_id (Right) | course_id (Right) | since (Right) |
| ----------- | ---------------- | ------------ | ------------ | ----------------- | ------------- |
| s1          | c1               | 2016         | s1           | c1                | 2016          |
| s1          | c1               | 2016         | s2           | c2                | 2017          |
| s1          | c1               | 2016         | s1           | c2                | 2017          |
| s2          | c2               | 2017         | s1           | c1                | 2016          |
| s2          | c2               | 2017         | s2           | c2                | 2017          |
| s2          | c2               | 2017         | s1           | c2                | 2017          |
| s1          | c2               | 2017         | s1           | c1                | 2016          |
| s1          | c2               | 2017         | s2           | c2                | 2017          |
| s1          | c2               | 2017         | s1           | c2                | 2017          |

```pgsql
 select LEFT.s_id from 
study as left study as right 
	where left.s_id = right.s_id 
		and left.course_id < > right.course_id 
```

| S_id (Left) | course_id (Left) | since (Left) | S_id (Right) | course_id (Right) | since (Right) | CONDF |
| ----------- | ---------------- | ------------ | ------------ | ----------------- | ------------- | ----- |
| s1          | c1               | 2016         | s1           | c1                | 2016          | FALSE |
| s1          | c1               | 2016         | s2           | c2                | 2017          | FALSE |
| s1          | c1               | 2016         | s1           | c2                | 2017          | TRUE  |
| s2          | c2               | 2017         | s1           | c1                | 2016          | FALSE |
| s2          | c2               | 2017         | s2           | c2                | 2017          | FALSE |
| s2          | c2               | 2017         | s1           | c2                | 2017          | FALSE |
| s1          | c2               | 2017         | s1           | c1                | 2016          | TRUE  |
| s1          | c2               | 2017         | s2           | c2                | 2017          | FALSE |
| s1          | c2               | 2017         | s1           | c2                | 2017          | FALSE |

| S_id (Left) |
| ----------- |
| s1          |

# Equi Join

![1718823323460](image/sql/1718823323460.png)

```pgsql
select e.E_name from emp e dept d where e.address = d.location and e.en_no = d.eno; 
```

![1718823579713](image/sql/1718823579713.png)

# left outer join

A LEFT OUTER JOIN in SQL is a type of join operation that combines rows from two or more tables based on a specified condition and includes unmatched rows from the left table. It allows you to retrieve data from multiple tables based on their related values. Here's a detailed explanation:

### What is a LEFT OUTER JOIN?

A LEFT OUTER JOIN is a type of join operation that combines rows from two or more tables based on a specified condition. It includes all rows from the left table (the "left" or "first" table) and matching rows from the right table (the "right" or "second" table). If there is no match in the right table, the result includes NULL values for the columns of the right table[1][2][3].

### Syntax

The syntax for a LEFT OUTER JOIN in SQL is as follows:

```sql
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
```

### Example

For example, consider a query that retrieves all employees along with their departments and salaries (if available). The Employees table is the left table, and we perform a LEFT OUTER JOIN with the Departments table using the join condition `E.DepartmentID = D.DepartmentID`. This ensures that all employees from the Employees table are included in the result set, regardless of whether they have a matching department. We then perform another LEFT OUTER JOIN with the Salaries table using the join condition `E.EmployeeID = S.EmployeeID`, allowing us to include salary information for employees if it exists[2].

```sql
SELECT E.EmployeeID, E.Name, D.DepartmentName, S.SalaryAmount
FROM Employees E
LEFT OUTER JOIN Departments D ON E.DepartmentID = D.DepartmentID
LEFT OUTER JOIN Salaries S ON E.EmployeeID = S.EmployeeID;
```

### Output

The output of this query would include all employees, even if they do not have a matching department or salary. The unmatched rows in the Employees table would have NULL values in the DepartmentName and SalaryAmount columns[2].

### Key Points

- **Includes all rows from the left table**: A LEFT OUTER JOIN includes all rows from the left table, even if there are no matching rows in the right table.
- **Includes matching rows from the right table**: If there is a match in the right table, the result includes the corresponding row from the right table.
- **Includes NULL values for unmatched rows in the right table**: If there is no match in the right table, the result includes NULL values for the columns of the right table[1][2][3].

### Practical Examples

- **Retrieving all customers, even if they haven't placed any orders**: A LEFT OUTER JOIN can be used to retrieve all customers, even if they haven't placed any orders. The unmatched rows in the Customers table would have NULL values in the OrdersID column[2].

![1718824652242](image/sql/1718824652242.png)


# Right outer join


![1718825047440](image/sql/1718825047440.png)
