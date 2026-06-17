

USE retail;


-- Find list of order for customers who live in London

SELECT * FROM orders;


-- Join Query 
SELECT onum,amt,odate,c.cnum,c.cname FROM orders o JOIN customer c
ON 
O.cnum = c.cnum
WHERE city = 'London';


-- SubQuery

SELECT * FROM orders WHERE 
cnum IN (SELECT cnum FROM customer WHERE city = 'London');



SELECT * FROM orders WHERE
cnum IN (2001,2006,2050);


-- Find customer whose avg order value is above 20000

SELECT * FROM customer WHERE 

cnum IN (

	SELECT cnum FROM orders 
	GROUP BY cnum 
	HAVING AVG(amt) > 2000

	);

	-- Find the such orders whose order value is greater than
	-- Avg order value


SELECT * FROM  orders WHERE amt >
(SELECT AVG(amt) FROM orders);


-- Find the max order value detail

SELECT * FROM orders WHERE amt =(
SELECT MAX(amt) FROM orders);

-- Find the 2nd highest order value detail

SELECT *
FROM orders
WHERE amt =
(
    SELECT MAX(amt)
    FROM orders
    WHERE amt <
    (
        SELECT MAX(amt)
        FROM orders
    )
);


-- Find top 2 orders

SELECT top 2 * FROM orders ORDER BY amt DESC;


-- Display highest order value customer name

SELECT * FROM customer
WHERE cnum in 
(
    SELECT cnum FROM orders
    WHERE amt = 
        ( 
        SELECT MAX(amt) FROM orders
        )
  );



  --Rank function
CREATE TABLE rank_table (Name VARCHAR(10));

INSERT INTO rank_table (Name) 
 VALUES('A'), ('C'), ('C'), ('B'), ('B'), ('D'), ('E');

select * from rank_table;


SELECT Name,
RANK () OVER(
ORDER BY Name
) AS Rank_no
FROM rank_table;


-- Find 2nd Rank

SELECT name,rank_no FROM 
(SELECT Name,
RANK () OVER(ORDER BY Name)
AS Rank_no
FROM rank_table) t1
WHERE rank_no = 2;



--FIND DENSE_RANK()
SELECT Name, 
DENSE_RANK () OVER (
ORDER BY Name
) AS Rank_no 
FROM rank_table;



--find top 5
select name, rank_no from (
SELECT Name, 
RANK () OVER (
ORDER BY Name
) AS Rank_no 
FROM rank_table) x where Rank_no <=5;


CREATE TABLE rank_table2 (Name VARCHAR(10), value int );

INSERT INTO rank_table2 (Name, value) 
 VALUES('A',90), ('B',80), ('C',100), ('D',40), ('E',60);

select * from rank_table2;

SELECT Name,value,
RANK() OVER(ORDER BY value DESC)
FROM rank_table2;


CREATE TABLE students (Name VARCHAR(10), value int, section char(1));

INSERT INTO students (Name, value, section) 
 VALUES('John',90, 'B'), ('Amy',80, 'B'), ('Alan',100, 'A'), ('Henry',40, 'B'), ('Mary',60, 'A');

 select * from students;


 SELECT section,name,value,
 RANK() OVER (PARTITION BY section ORDER BY value DESC) AS rank
 FROM students;












