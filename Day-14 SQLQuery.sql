USE retail;

-- date functions

SELECT * FROM orders;

INSERT INTO orders VALUES
(3052, 3000, '2026-03-15', 2001);


-- Find year wise sales from orders table

SELECT YEAR(odate),SUM(amt) FROM orders
GROUP BY YEAR(odate);


-- Find month wise sales

SELECT YEAR(odate),MONTH(odate),SUM(amt) FROM orders
GROUP BY YEAR(odate),MONTH(odate)
ORDER BY YEAR(odate);

-- Replace month num by month name in the above query

SELECT YEAR(odate), datename(mm,odate),SUM(amt) FROM orders
GROUP BY YEAR(odate), datename(mm,odate),MONTH(odate)
ORDER BY YEAR(odate), MONTH(odate);


-- Find weekday wise sales

select datename(dw, odate), datepart(dw, odate), sum(amt) from orders
group by datename(dw, odate), datepart(dw, odate)
order by datepart(dw, odate);

-- datediff

SELECT datediff(dd, '2026-06-01', '2026-06-01');

--loan amount = 1000000
--rate = 9%
--start date = 01.04.2026
--end date = 10.06.2026
--calc SI

select round(1000000*0.09*(datediff(dd,'2026-04-01','2026-06-10')+1)/365,2)

SELECT YEAR('25-25-2026');

SELECT YEAR('2026-05-25');


create database bank;

use bank;

--create a customer table
CREATE TABLE customer (
cnum INT NOT NULL,
fname VARCHAR(30) NOT NULL,
lname VARCHAR(30) NOT NULL,
addr VARCHAR(100) NOT NULL,
city VARCHAR(100) NOT NULL,
contact VARCHAR(30) NOT NULL,
pincode int NOT NULL,
PRIMARY KEY (cnum)
);


--create a account table
CREATE TABLE account (
account_id VARCHAR(30) NOT NULL,
cnum INT NOT NULL,
type VARCHAR(30) NOT NULL,
balance decimal(10,2) NOT NULL,
PRIMARY KEY (account_id),
FOREIGN KEY (cnum) REFERENCES customer(cnum)
);

--create a transaction table
CREATE TABLE TXN (  
txn_id int identity,
account_id VARCHAR(30) NOT NULL,
txn_dt date NOT NULL,
channel VARCHAR(30) NOT NULL,
amount decimal(10,2) NOT NULL,
PRIMARY KEY (txn_id),
FOREIGN KEY (account_id) REFERENCES account(account_id)
);

--create a new SAVING account for above customer
insert into account values('100-201-3001', 101, 'Savings', 0);
--create a new customer
insert into customer values(101,'John','Smith','123 High Street, M G Road', 'Bangalore', '9876543210', 123456);

t
select * from account;

--create insert trigger
CREATE TRIGGER update_balance ON txn  
AFTER INSERT  
AS  
BEGIN  
	SET NOCOUNT ON; -- it will not return total records affected messages
	declare @amount decimal(10,2); -- local variables
	declare @account_id varchar(30);

	select @account_id=account_id, @amount=amount from inserted; --inserted is a system table which will have last inserted data
	

	update account 
	set balance = balance + @amount
	where account.account_id = @account_id;
END;  

insert into txn (account_id, txn_dt, channel, amount) values ('100-201-3001', '2026-05-18','cash deposit', 40000);


insert into txn (account_id, txn_dt, channel, amount) values 
('100-201-3001', '2026-05-18','UPI Payment', -10000);









