CREATE DATABASE Assignments;

USE Assignments;

-- 1. Create a customer table which comprises of these columns; 'Customer_id',
-- 'First_name', 'Last_name', 'Email', 'Address', 'City', 'State','Zip'


CREATE TABLE customer 
(
customer_Id INT,
First_name VARCHAR(30),
Last_name VARCHAR(40),
Email VARCHAR(50),
Address VARCHAR(50),
City VARCHAR(40),
State VARCHAR(30),
Zip CHAR(6)

);



INSERT INTO customer (customer_id, first_name, last_name, email, address, city, state, zip)
VALUES
(1, 'Ravi', 'Miller', 'george.miller@gmail.com', '123 Elm St', 'SanJose', 'CA', '951126'),
(2, 'Grace', 'Anderson', 'grace.anderson@yahoo.com', '45 Oak Ave', 'SanJose', 'CA', '951236'),
(3, 'Gary', 'Holt', 'gary.holt@gmail.com', '78 Pine Rd', 'LosAngeles', 'CA', '900019'),
(4, 'Rosy', 'Garcia', 'linda.garcia@gmail.com', '56 Maple St', 'SanJose', 'CA', '951100'),
(5, 'David', 'Brown', 'david.brown@hotmail.com', '90 Birch Blvd', 'Sacramento', 'CA', '958142');

SELECT * FROM customer;


--3. Select only the ‘first_name’ and ‘last_name’ columns fromthe customer table
	
	SELECT First_name,Last_name FROM customer;

	--4. Select those records where ‘first_name’ starts with “G” and city is ‘SanJose’.

	SELECT * FROM customer
	WHERE First_name LIKE 'G%' AND city = 'SanJose';

	--Let's say if the question is find the customer with first_name having that contains only 4 character.

	SELECT * FROM customer
	WHERE First_name LIKE '____';

	--5. Select those records where Email has only ‘gmail’.

	SELECT  * FROM customer
	WHERE Email LIKE '%gmail%';

	--6. Select those records where the ‘last_name’ doesn't end with “A”.

	SELECT * FROM customer
	WHERE Last_name NOT LIKE '%A';


--1. Create an ‘Orders’ table which comprises of these columns: ‘order_id’, ‘order_date’, ‘amount’, ‘customer_id’.


CREATE TABLE orders(

order_id INT primary key,
order_date DATE,
amount float,
customer_Id INT 
);

--insert the following records

INSERT INTO Orders (order_id, order_date, amount, customer_id)
VALUES
(101, '2025-10-01', 250.50, 1),
(102, '2025-10-05', 175.00, 2),
(103, '2025-10-10', 320.00, 3),
(104, '2025-10-15', 450.75, 7),
(105, '2025-10-20', 200.00, 5);


SELECT * FROM orders;

--3. Make an inner join on ‘Customer’ and ‘Orders’ tables on the ‘customer_id’ column.


SELECT * FROM customer c
INNER JOIN orders O
ON c.customer_Id = o.customer_Id;



--4. Make left and right joins on ‘Customer’ and ‘Orders’ tables on the‘customer_id’ column.

-- RIGHT JOIN

SELECT * FROM customer C 
RIGHT JOIN orders O
ON C.customer_Id = O.customer_Id


-- LEFT JOIN
SELECT * FROM customer C 
LEFT JOIN orders O
ON  C.customer_Id = O.customer_Id



--5. Make a full outer join on ‘Customer’ and ‘Orders’ table on the ‘customer_id’ column.


SELECT * FROM customer C
FULL OUTER JOIN orders O
ON C.customer_Id = O.customer_Id;


--6. Update the ‘Orders’ table and set the amount to be 100 where‘customer_id’ is 3.


UPDATE orders
SET amount = 100
WHERE customer_Id = 3;









