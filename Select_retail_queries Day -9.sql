USE retail;

--  * Means all colums 

UPDATE salespeople 
set comm = 0.15
WHERE snum = 1001;
SELECT * FROM salespeople;


-- Find salesperson living in London 

SELECT * FROM salespeople 
WHERE city = 'London';

 -- Read 6 rows
 -- Output 3 rows


-- Find salesperson living in London and New York

SELECT * FROM salespeople
WHERE city ='London' OR city ='New York';


-- AND means all the conditions should be true
-- OR means either of the condition should be true


-- Find people living in London and comm should be less than 15 %

SELECT * FROM salespeople 
WHERE city = 'London' AND comm < 0.15;


-- Find people living in London and comm should be upto 15 %

SELECT * FROM salespeople 
WHERE city = 'London' AND comm <= 0.15;


-- Find people living in London/New York and comm should be upto 15 %

SELECT * FROM salespeople
WHERE  (city = 'London' OR city = 'New York') AND comm <= 0.15;

-- IN (in place of OR)

SELECT * FROM salespeople
WHERE city IN ('London','New York') AND comm <= 0.15;


-- Find people whose comm is above 10 and less than 20


SELECT * FROM salespeople
WHERE comm >  0.10 AND comm <0.20;


-- Find people whose comm is  10 and less than or equal to 20

SELECT * FROM salespeople
WHERE comm >=  0.10 AND comm <=0.20;

-- Between
SELECT * FROM salespeople 
WHERE comm BETWEEN  0.10 AND 0.20;


ALTER TABLE salespeople ALTER COLUMN comm dec(4,2) null;


INSERT INTO salespeople VALUES (1009,'John','London',null);

--Find all people whose comm upto 15 %

SELECT * FROM salespeople 
WHERE comm <= 0.15;


-- Search rows for NULL values

SELECT * FROM salespeople
WHERE comm IS NULL;

-- Search rows without NULL values

SELECT * FROM salespeople 
WHERE comm IS NOT NULL;


-- Find people living in other than London city

SELECT * FROM salespeople
WHERE city != 'London';


SELECT * FROM salespeople
WHERE city <> 'London';


SELECT * FROM salespeople
WHERE city NOT IN ('London');

--create customer table
CREATE TABLE customer (
cnum INT NOT NULL,
cname VARCHAR(30) NOT NULL,
city VARCHAR(30) NOT NULL,
rating int not null,
snum int NOT NULL,
PRIMARY KEY (cnum),
FOREIGN KEY (snum) REFERENCES salespeople(snum)
);

INSERT INTO customer VALUES (2001, 'Hoffman', 'London',100, 1001);


SELECT * FROM customer;

INSERT INTO customer VALUES (2002, 'Giovanni', 'Rome',200, 1003);
INSERT INTO customer VALUES (2003, 'Liu', 'San Jose',200, 1002);
INSERT INTO customer VALUES (2004, 'Grass', 'Berlin',300, 1002);
INSERT INTO customer VALUES (2006, 'Clemens', 'London',100, 1001);
INSERT INTO customer VALUES (2008, 'Cisneros', 'San Jose',300, 1007);
INSERT INTO customer VALUES (2007, 'Pereira', 'Rome',100, 1004);


-- Count function (returns num of rows in the query)

SELECT count(cnum) as 'Count of rows' FROM customer;


-- Count num of rows customers living in London city 

SELECT count(cnum) AS 'Count of rows' FROM customer
WHERE city = 'London';


SELECT COUNT(snum) FROM salespeople;

-- Null won't count 
SELECT COUNT(comm) FROM salespeople;

SELECT * FROM salespeople;

update salespeople
set city = ''
where snum = 1009;

select count(city) from salespeople;










