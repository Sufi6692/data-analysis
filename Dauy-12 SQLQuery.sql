USE retail



SELECT customer.cnum,cname,SUM(amt) AS 'Amount'FROM orders
JOIN customer
ON customer.cnum = orders.cnum
GROUP BY customer.cnum,cname;


-- add number of orders placed by each cust

SELECT customer.cnum,cname,SUM(amt),COUNT(onum)
FROM orders JOIN customer
ON orders.cnum = customer.cnum
GROUP BY customer.cnum,cname;

-- Table join
SELECT * FROM orders 
JOIN customer
ON orders.cnum = customer.cnum

RIGHT JOIN salespeople
ON salespeople.snum =customer.snum;

-- Find comm earned by each sp
SELECT salespeople.snum,sname,SUM(comm*amt) AS 'Total' FROM orders 
JOIN customer
ON orders.cnum = customer.cnum

RIGHT JOIN salespeople
ON salespeople.snum =customer.snum
GROUP BY salespeople.snum,sname;

-- Change the display of NULL -- > coalesce

SELECT salespeople.snum,sname,COALESCE(SUM(comm*amt),0) AS 'Total' FROM orders 
JOIN customer
ON orders.cnum = customer.cnum

RIGHT JOIN salespeople
ON salespeople.snum =customer.snum
GROUP BY salespeople.snum,sname;

