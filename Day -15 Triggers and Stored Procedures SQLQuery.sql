USE bank;

SELECT * FROM account;
SELECT * FROM txn;

-- trigger after update 

GO
CREATE TRIGGER update_balance_2 ON txn

AFTER UPDATE
AS
BEGIN
		
		SET NOCOUNT ON;
		declare @amount decimal(10,2);
		declare @account_id varchar(30);
		declare @old_amount decimal(10,2);
		declare @old_account_id varchar(30);


		SELECT @old_account_id = account_id,  @old_amount = amount from deleted
		

		-- Reverse the old txn
		UPDATE account 
		SET balance = balance - @old_amount 
		WHERE account.account_id = @old_account_id;

	select @account_id=account_id, @amount=amount from inserted; 

	UPDATE account
	SET balance = balance + @amount
	WHERE account.account_id = @account_id;

END;

update txn
set amount = 35000
where txn_id = 1;

select * from account;
select * from txn;


GO
CREATE TRIGGER udpate_balance_3 ON txn

AFTER DELETE 
AS
BEGIN

	SET NOCOUNT ON;
	declare @old_amount decimal(10,2);
	declare @old_account_id varchar(30);

	SELECT @old_account_id = account_id, @old_amount = amount FROM deleted

	
	UPDATE account 
	SET balance = balance - @old_amount
	WHERE account.account_id = @old_account_id;

	END;

delete from txn
where txn_id = 2;


USE retail;

select * from customer where city = 'London';


GO
CREATE PROCEDURE city_customer

	@city varchar(50)

AS

	SET NOCOUNT ON;
	SELECT *
	FROM customer
	WHERE city = @city;

GO

EXECUTE  city_customer 'London';
EXECUTE city_customer 'Berlin';


SELECT * FROM orders;

GO 
CREATE PROCEDURE add_order
@onum int,
@amt decimal(10,2),
@odate date,
@cname varchar(50)
AS 
BEGIN

	SET NOCOUNT ON;
	INSERT INTO orders VALUES
	(@onum,@amt,@odate,(select cnum from customer where cname = @cname));

END


select * from customer;

exec add_order 3099, 4000, '2026-05-19', 'Hoffman';


select * from orders;

GO
CREATE PROCEDURE update_order
@onum int,
@amt decimal(10,2),
@odate date,
@cname varchar(50)

AS
BEGIN

		SET NOCOUNT ON;

		UPDATE orders
		SET amt = @amt, odate = @odate, cnum = (SELECT cnum FROM customer WHERE cname = @cname)

				WHERE onum = @onum
END
GO

EXEC update_order 3099,3000,'2026-05-19','Grass'

select * from customer;
select * from orders;

GO
CREATE PROCEDURE delete_order
@onum int
AS
BEGIN 
	
	SET NOCOUNT ON;

	DELETE FROM orders
	WHERE onum = @onum
END

GO

EXEC delete_order 3099;

SELECT * FROM orders;


























