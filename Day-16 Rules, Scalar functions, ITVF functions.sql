USE retail;

INSERT INTO orders VALUES (3055, -5000,'2026-05-18',2001);

SELECT * FROM orders;

-- Rules 
GO
CREATE rule CITYNAME
as @city in ('London','Rome','LA','Bangalore');


-- Bind the rule

EXEC SP_BINDRULE 'dbo.CITYNAME', 'customer.city';

INSERT INTO customer VALUES (2050, 'John', 'London', 100, 1001);

GO
CREATE rule num_above_zero
as @num > 0;

EXEC SP_BINDRULE 'dbo.num_above_zero', 'orders.amt';

INSERT INTO orders VALUES(-3056,10,'2026--05-18',2001)

SELECT * FROM orders;

-- scalar UDF

CREATE TABLE order_items(
order_id int not null primary key,
prod_id varchar(10),
quantity int,
list_price decimal(10,2),
discount decimal(4,2)
);

INSERT INTO order_items VALUES (1,'P001',100,50,2.5);
INSERT INTO order_items VALUES (2,'P002',50,40,4.0);
INSERT INTO order_items VALUES (3,'P004',1000,25,0);
INSERT INTO order_items VALUES (4,'P001',200,50,2.5);


SELECT * FROM order_items;

GO
CREATE FUNCTION udfNetSale(
	@quantity INT,
	@list_price DEC(10,2),
	@discount DEC(4,2)
)
RETURNS DEC(10,2)
AS
BEGIN
	RETURN @quantity * @list_price * ((100 - @discount)/100);

END;

GO
SELECT dbo.udfNetSale(1000,10,5);

SELECT *, dbo.udfNetSale(quantity,list_price,discount) as Net_Sale FROM order_items;


-- ITVF

CREATE TABLE Student 
( 
	Id INT PRIMARY KEY,
	Name VARCHAR(50) NOT NULL,
	Marks INT NOT NULL
	);



INSERT INTO Student 
VALUES
(1,'Tushar',60),
(2,'Kunal',80),
(3,'Shivam',30),
(4,'Rushi',45),
(5,'Mahesh',60),
(6,'Shubham',39),
(7,'Rahul',97);


SELECT * FROM Student;

GO
CREATE FUNCTION dbo.GetNameByMarks(@mark int)
RETURNS Table
AS
RETURN
(
select id,name,marks from Student
where marks >= @mark

);

SELECT * FROM dbo.GetNameByMarks(45)


CREATE FUNCTION dbo.DisplayStudentDetails()
RETURNS Table
AS
RETURN
(
select name,marks from Student
);

SELECT * FROM dbo.DisplayStudentDetails()
WHERE marks >= 80;



CREATE FUNCTION dbo.DispalyStudnetDetails_above45()
RETURNS Table
AS
RETURN
(
select * from dbo.GetNameByMarks(45)
);

SELECT * FROM dbo.DispalyStudnetDetails_above45();


















