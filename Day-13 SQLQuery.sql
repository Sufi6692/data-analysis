USE retail;

SELECT * FROM orders;

SELECT sum(amt) from orders;

SELECT * FROM customer;

-- String Fucntions
-- Upper Functions

SELECT UPPER(cname) FROM customer;


-- Lower Functions

SELECT LOWER(city) FROM customer;

-- Len Fucntion

SELECT concat('John',' ','Smith');

--Combine cname and city in one sting

SELECT CONCAT(cname,' ',city) FROM customer;

SELECT ASCII('A');

--Trim function 

SELECT * FROM salespeople;

UPDATE salespeople 
SET city = ' London'
WHERE snum = 1001;


SELECT * FROM salespeople WHERE city = 'London';
SELECT LEN(' London');
SELECT LEN('London');

-- Print all rows with city as London

SELECT * FROM salespeople WHERE trim(city) = 'london';

-- pattern match using like
-- find sname where e letter is found

SELECT * FROM salespeople
WHERE sname LIKE '%e%';

-- Find sname where an is found

SELECT * FROM salespeople 
WHERE sname LIKE '%an%';

SELECT * FROM salespeople 
WHERE city LIKE '%ose%';

SELECT * FROM salespeople 
WHERE city LIKE '%London%';


--print all the names starts with letter r


SELECT * FROM salespeople
WHERE sname LIKE 'r%';

--print all the names ends with letter L

SELECT * FROM salespeople
WHERE sname LIKE '%L';

SELECT 'mr','john','smith';

select concat(upper(substring('mr',1,1)), substring('mr',2,1), ' ', 
upper(substring('john',1,1)), substring('john',2,len('john')-1),  ' ', 
upper(substring('smith',1,1)), substring('smith',2,len('smith')-1))

-- Mathematical Functions

-- ABS
SELECT abs(-500);

--ROUND
SELECT ROUND(25.457,2);

--Avg value of all orders

SELECT AVG(amt) FROM orders;


SELECT CONVERT(dec(10,2),ROUND(avg(amt),2)) FROM orders;


select round(456.1264,2);

--square func
select square(7);

--power
select power(2,3);

--principal = 100000
--rate = 7.00%
--duration = 2 years
--compound - after 3 months
--cycles per year - 4

--calc comp int
select 100000*(power(1+ (0.07/4), 8)) - 100000;

--calc simple int
select 100000*0.07*2;

--date functions
select * from orders;

select *, year(odate) from orders;

select *, year(odate), month(odate), datename(mm, odate),
datename(dw, odate) from orders;

select getdate();

