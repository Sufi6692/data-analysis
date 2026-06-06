USE retail;
--cust wise sales

SELECT cnum, SUM(amt) FROM orders
GROUP BY cnum;

-- Print the cust name in the above query 
select * from orders o join customer c
on
o.cnum = c.cnum;

select c.cnum, cname, sum(amt) 
from orders o join customer c
on
o.cnum = c.cnum
group by c.cnum, cname;

-- Add number of orders placed by each cust

SELECT c.cnum,cname,SUM(amt),count(onum) AS 'Count'
FROM orders as o JOIN customer as c
ON o.cnum = c.cnum
GROUP BY c.cnum,cname;


-- 3 Table joins

SELECT * FROM orders as o 
JOIN customer AS c
ON o.cnum = c.cnum

RIGHT OUTER JOIN salespeople as s
ON s.snum = c.snum;

-- find comm earned by each sp

SELECT s.snum,sname, SUM(amt*comm)
FROM orders as o join customer as c
ON o.cnum =c.cnum
RIGHT OUTER JOIN salespeople as s
ON s.snum = c.snum
GROUP BY s.snum,sname;


-- change the display of NULL ---> coalesce

SELECT s.snum,sname, COALESCE(SUM(amt*comm),0)
FROM orders as o join customer as c
ON o.cnum =c.cnum
RIGHT OUTER JOIN salespeople as s
ON s.snum = c.snum
GROUP BY s.snum,sname;

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

create table temp1(
id int,
cname varchar(100),
city varchar(100));

insert into temp1 values(1, 'John', 'London');
insert into temp1 values(2, null, 'NY');
insert into temp1 values(3, 'Alan', null);

select * from temp1;

select id, coalesce(cname, 'NA'), coalesce(city,'NA')
from temp1;









SELECT* FROM customer;
SELECT * FROM salespeople;
