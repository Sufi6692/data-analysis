CREATE DATABASE tmp;

USE tmp;

CREATE TABLE salesman(
salesmanID int null,
salesman_name varchar (30) null,
city varchar (30) null);

CREATE TABLE customer(
custID int null,
Customername varchar (30) null,
salesmanID int null);

-- To Change the data type

ALTER TABLE salesman ALTER COLUMN salesmanID INT NOT NULL;

-- To Add make column as primary key

ALTER TABLE salesman ADD PRIMARY KEY (salesmanID);

-- To add new clumn in table 

ALTER TABLE salesman ADD comm decimal(4,2) NULL;

-- To add Consttaint for the cloumn if file have null value to replace that null with given defualt  value 

ALTER TABLE salesman ADD CONSTRAINT DF_city DEFAULT 'London' FOR city;

-- Command for view complete table strucure 

exec sp_help salesman;


INSERT INTO salesman(salesmanID,salesman_name,comm) VALUES (1001,'john',0.15);

SELECT * FROM salesman;

INSERT INTO salesman (salesmanID,salesman_name,city) VALUES(1002,'Alan', 'New York');

ALTER TABLE customer
ADD FOREIGN KEY (salesmanID)
REFERENCES salesman (salesmanID);

exec sp_help customer;

INSERT INTO customer VALUES (2001,'Mr B', 1001);

SELECT * FROM salesman;
SELECT * FROM customer;

insert into customer values (2002, 'Mr C', 1001);

-- Add not null constraint and change length in customer_name column for the customer table.

ALTER TABLE customer alter column Customername varchar(255) NOT NULL; 

-- Renaming the cloum
EXEC sp_rename 'dbo.salesman.comm','commission','COLUMN';

-- Renaming the table 

EXEC sp_rename 'dbo.salesman', 'salespeople';


ALTER DATABASE tmp MODIFY NAME = temp;

exec sp_who;
kill 55

USE retail;


USE temp;


--drop one table
drop table salespeople; -- not allowed

drop table customer;

select * from salespeople;

truncate table salespeople;