use retail;

--count num of rows customers living in London city
select count(cnum) as 'count of rows' from customer
where city = 'London';

--count num of rows customers living in London and Rome cities
select count(cnum) as 'count of rows' from customer
where city in ('London','Rome');

--count of cust in each city
--group by
select * from customer;
select city, count(cnum) from customer group by city;

--count of cust for each rating
select rating, count(cnum) from customer group by rating;

--composite grouping
--count cust for each city and rating
select city, rating, count(cnum) from customer group by city, rating;

--having [filteration after agg data]
--count of cust for each city where count is 2
select city, count(cnum) from customer 
group by city
having count(cnum) = 2;

--order of task in the above query
--1. group by
--2. count
--3. having

--count of cust for each city in London/Berlin

select * from customer where city in ('London','Berlin');

select city, count(cnum) from customer 
where city in ('London','Berlin')
group by city;

select * from salespeople;

delete from salespeople
where snum = 1009;

--find count of salesperson for each city whose comm less than 20%
--their count should be greater than 1

select * from salespeople where comm < 0.20;

select city, count(snum) from salespeople 
where comm < 0.20
group by city;

select city, count(snum) from salespeople 
where comm < 0.20
group by city
having count(snum) > 1;

--rearrange the output
select * from salespeople;

--order by 
-- display in the order of sname

select * from salespeople order by sname asc;

--display in the order of highest comm
select * from salespeople order by comm desc;

--find count of salesperson for each city whose comm less than 20%
--their count should be equal to 1
--display city in desc order
select city, count(snum) as 'count of sp' from salespeople 
where comm < 0.20
group by city
having count(snum) = 1
order by city desc;

--extract data from 2 tables

--count of customer for each salesperson
select * from salespeople;
select * from customer;

select snum, count(cnum) from customer
group by snum;

--Joins
-- by joining tables we can extract data from many tables
-- join customer with salespeople
--cols = 9
--rows = 7
select * from customer join salespeople
on
customer.snum = salespeople.snum;

--count of customer for each salesperson. Print sname also
select salespeople.snum, sname, count(cnum) from 
customer join salespeople
on
customer.snum = salespeople.snum
group by salespeople.snum, sname;