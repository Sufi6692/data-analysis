-- create database command
CREATE DATABASE retail;

-- selection of database
USE retail;

-- create table for the salesperson
CREATE TABLE  salesperson (
snum int not null,
sname varchar(30) not null,
cit varchar(30) not null,
comm dec(4,2) not null,
primary key (snum));

EXEC sp_rename 'salesperson', 'salespeople';


SELECT * FROM salespeople;


-- add first row in the salespeople table
INSERT INTO salespeople VALUES (1001,'Peel','London',0.12);

INSERT INTO salespeople VALUES
(1002, 'Serres', 'San Jose', 0.13),
(1004, 'Motika', 'London', 0.11),
(1007, 'Rifkin', 'Barcelona', 0.15),
(1003, 'AxelRod', 'New York', 0.10),
(1005, 'Fran', 'London', 0.26);

SELECT * FROM salespeople;

--display only snum and sname
SELECT  snum, sname FROM salespeople;


--update command for edit in a table
--modify Peel city to Berlin
-- where condition will target selective records

EXEC sp_rename 'salespeople.cit', 'city', 'COLUMN';

UPDATE salespeople
SET city = 'Berlin'
WHERE snum = 1001;

--update Peel city to London and comm to 20%


UPDATE salespeople
SET city = 'London', 
	comm = 20
WHERE snum = 1001;

--delete command
insert into  salespeople values (1008, 'John', 'London', 0.15);

DELETE FROM salespeople
where snum = 1008;

SELECT * FROM salespeople;
