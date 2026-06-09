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

--create a view for 3 table join output
create view orders_cust_sp as
select onum, amt, odate, c.cnum,
cname, c.city as 'cust_city', rating, 
s.snum, sname, s.city as 'sp_city', comm
from orders o join customer c
on
o.cnum = c.cnum

right outer join salespeople s
on
s.snum = c.snum;

--how to read view
select * from orders_cust_sp;

insert into orders values (3050, 1000, '2026-06-05', 2001);

--find comm earned by each sp using view
select snum, sname, coalesce(sum(comm*amt),0)
from
orders_cust_sp
group by snum, sname;

create table temp2(
id int,
cname varchar(100),
city varchar(100));

SELECT * FROM temp1;

insert into temp1 values(1, 'John', 'London');
insert into temp1 values(2, null, 'NY');
insert into temp1 values(3, 'Alan', null);

select * from temp1;

select id, coalesce(cname, 'NA'), coalesce(city,'NA')
from temp1;

