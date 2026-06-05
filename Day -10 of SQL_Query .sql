USE retail;
-- Count num of rows customers living in London city 
SELECT COUNT(cnum) AS 'Count of rows' 
FROM customer
WHERE city IN ('London','Rome');


-- Count of cust in each city
--Group by 

SELECT  city, COUNT(cnum) AS 'Count of Customers' FROM customer
GROUP BY city;


-- Count of cust for each rating

SELECT rating, Count(snum) AS 'Count of Customers' FROM customer
GROUP BY rating;



-- Composite grouping

-- Count cust for each city and rating

SELECT city,rating,COUNT(cnum)AS 'Count of Customers' FROM customer
GROUP BY city,rating;


-- Having [filteration after agg data]

--Count of cust for each city where count is 2

SELECT city,COUNT(cnum)AS 'Count of customers' FROM customer
GROUP  BY city
HAVING COUNT(cnum) =2;


-- Order of task in the above query 
-- 1. Group by 
-- 2. Count 
-- 3. Having 


SELECT * FROM customer;
SELECT * FROM salespeople;