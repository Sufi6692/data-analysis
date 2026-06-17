USE retail;

--  CTE 
WITH sp_cust_order AS (
SELECT onum,amt,odate,o.cnum,c.city AS 'customer_City',
rating, c.snum,sname,s.city AS 'salesperson_city', comm

FROM orders o join customer c
ON
o.cnum = c.cnum 

JOIN salespeople s
ON 
s.snum = c.snum)
SELECT snum,sname,SUM(amt*comm) FROM sp_cust_order GROUP BY snum,sname;


-- Using CTE display the total amt spent by each cust

WITH cust_orders AS(
SELECT onum,amt,odate,o.cnum,cname
FROM orders o JOIN customer c
ON
o.cnum = c.cnum)
SELECT cnum,cname, SUM(amt) FROM cust_orders GROUP BY cnum,cname;



-- Find total value for all orders for customer who are living in London

WITH cust_orders AS (
SELECT onum,amt,odate,o.cnum,cname
FROM orders o JOIN customer c
ON
o.cnum = c.cnum
where city = 'London')
SELECT cnum,cname,SUM(amt) FROM cust_orders GROUP BY cnum,cname;



SET STATISTICS IO ON;
SET STATISTICS TIME ON;
GO

SET STATISTICS IO OFF;
SET STATISTICS TIME OFF;
GO


SELECT SUM(amt) FROM orders;



EXEC sp_help customer;

SELECT * FROM salespeople;

INSERT INTO salespeople VALUES (1006,'A','London',0.15);


SELECT * FROM salespeople WHERE snum = 1007;

-- Output = 1
-- Read = 1

SELECT * FROM salespeople WHERE city = 'London';


CREATE NONCLUSTERED INDEX IX_salespeople_city
ON dbo.salespeople (city);

exec sp_help salespeople;



-- Error Handling 


--error handling
CREATE TABLE dbo.DB_Error_Log (
    LogID INT IDENTITY(1,1) PRIMARY KEY,
    UserName NVARCHAR(100),
    ErrorNumber INT,
    ErrorSeverity INT,
    ErrorState INT,
    ErrorLine INT,
    ErrorProcedure NVARCHAR(128),
    ErrorMessage NVARCHAR(4000),
    LogDate DATETIME DEFAULT GETDATE()
);
GO

exec add_order 4001, 0, '2026-05-19', 'Hoffman';


CREATE PROCEDURE add_order_with_errors_handling
@onum int,
@amt decimal(10,2),
@odate date,
@cname varchar(50)
AS
BEGIN
    -- Best Practice: Automatically abort execution on unhandled transaction errors
    SET XACT_ABORT ON; 

    BEGIN TRY
        -- Start explicit transaction
        BEGIN TRANSACTION;

	insert into orders values 
	(@onum,@amt,@odate,(select cnum from customer where cname = @cname));

        -- Commit changes if everything succeeds
        COMMIT TRANSACTION;
        PRINT 'Transaction committed successfully.';
    END TRY
    BEGIN CATCH
        -- Check if there is an active transaction that needs rolling back
        IF @@TRANCOUNT > 0
        BEGIN
            ROLLBACK TRANSACTION;
            PRINT 'Transaction rolled back due to an error.';
        END;

        -- Log the precise error properties into the table
        INSERT INTO dbo.DB_Error_Log (
            UserName, ErrorNumber, ErrorSeverity, ErrorState, ErrorLine, ErrorProcedure, ErrorMessage
        )
        VALUES (
            SUSER_SNAME(),
            ERROR_NUMBER(),
            ERROR_SEVERITY(),
            ERROR_STATE(),
            ERROR_LINE(),
            ERROR_PROCEDURE(),
            ERROR_MESSAGE()
        );


        -- The THROW statement requires a preceding semicolon if not placed first
        THROW; 
    END CATCH
END;
GO

EXEC add_order_with_errors_handling 3099, 0, '2026-05-19', 'Hoffman';

select * from DB_Error_Log;

EXEC add_order_with_errors_handling 4001, 4000, '2026-05-19', 'Hoffman';

select * from orders;

select * from emp;

select * from retail.dbo.emp;

select * from bank.dbo.account;

select * from student_finance;



















































































