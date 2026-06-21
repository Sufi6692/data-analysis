CREATE DATABASE SalesDataBase;

USE SalesDataBase;

CREATE TABLE Customers
(
	CustomerId INT IDENTITY(1,1) PRIMARY KEY,
	CustomerName VARCHAR(50) NOT NULL,
	Address VARCHAR(255) NOT NULL,
	Pincode VARCHAR(10) NOT NULL,
	Contact VARCHAR(15) UNIQUE NOT NULL
);


CREATE TABLE Products
(
	ProductID INT IDENTITY(1,1) PRIMARY KEY,
	ProductName VARCHAR(50) NOT NULL,
	Qty_In_Stock INT NOT NULL,
	Re_Order_Level INT NOT NULL
);

CREATE TABLE Vendors
(
	VendorId INT IDENTITY(1,1) PRIMARY KEY,
	VendorName VARCHAR(50) NOT NULL,
	Address VARCHAR(250) NOT NULL,
	Contact VARCHAR(15) UNIQUE NOT NULL
);
	 

CREATE TABLE PurchaseTable
(
	PurchaseId INT IDENTITY (1,1) PRIMARY KEY,
	PurchaseDate DATE NOT NULL,
	VendorId INT NOT NULL,
	ProductId INT NOT NULL,
	Qty_Purchased INT NOT NULL,
	Unit_Price DECIMAL(8,2),

	FOREIGN KEY(ProductId) REFERENCES Products(ProductID),
	FOREIGN KEY(VendorId) REFERENCES Vendors (VendorId)

	);



	
	CREATE TABLE Orders
(
	OrderId INT IDENTITY(1001,1)  PRIMARY KEY,
	OrderDate DATE NOT NULL,
	CustomerId INT NOT NULL,
	Amount DECIMAL(10,2) NOT NULL,

	FOREIGN KEY(CustomerId) REFERENCES Customers(CustomerId)
);


CREATE TABLE Order_Details
(
	Order_Detail_Id INT IDENTITY(1001,1) PRIMARY KEY,
	Order_Num INT NOT NULL,
	Product_Id INT NOT NULL,
	Qty_Sold INT NOT NULL,
	Unit_Price Decimal(10,2),
	
	FOREIGN KEY(Order_Num) REFERENCES Orders(OrderId),
	FOREIGN KEY(Product_Id) REFERENCES Products(ProductID)
);




--create insert trigger

CREATE TRIGGER Update_Order_Amount
ON Order_Details
AFTER INSERT
AS
BEGIN 
SET NOCOUNT ON;

DECLARE @order_num INT;
DECLARE @qty INT;
DECLARE @price DECIMAL(10,2);

	SELECT 
	@order_num = order_Num,
	@qty = Qty_Sold,
	@price = Unit_Price
	FROM inserted;

	UPDATE orders
	SET amount = Amount + (@qty * @price)
	WHERE orderid = @order_num;

	END;


	CREATE TRIGGER Update_Stock
	ON PurchaseTable
	AFTER INSERT
	AS
	BEGIN 
	SET NOCOUNT ON;

	DECLARE @product_id INT;
	DECLARE @qty INT;

	SELECT 
		@product_id = ProductId,
		@qty = Qty_Purchased
	FROM inserted;

	UPDATE Products
	SET Qty_In_Stock = Qty_In_Stock + @qty
	WHERE ProductID = @product_id;
	
	END;


	INSERT INTO Customers(CustomerName, Address, Pincode, Contact)
VALUES
('Rahul Sharma', 'Bangalore', '560001', '9876543210'),
('Priya Verma', 'Hyderabad', '500001', '9876543211'),
('Amit Khan', 'Mumbai', '400001', '9876543212');

INSERT INTO Products(ProductName, Qty_In_Stock, Re_Order_Level)
VALUES
('Laptop', 10, 3),
('Mouse', 50, 10),
('Keyboard', 25, 5);

INSERT INTO Vendors(VendorName, Address, Contact)
VALUES
('Dell Supplier', 'Delhi', '9999991111'),
('Tech Distributors', 'Pune', '9999992222');

INSERT INTO Orders(OrderDate, CustomerId, Amount)
VALUES
('2026-06-21', 1, 0),
('2026-06-21', 2, 0);



INSERT INTO PurchaseTable
(PurchaseDate, VendorId, ProductId, Qty_Purchased, Unit_Price)
VALUES
('2026-06-21', 1, 1, 5, 45000),
('2026-06-21', 2, 2, 20, 500);


INSERT INTO Order_Details
(Order_Num, Product_Id, Qty_Sold, Unit_Price)
VALUES
(1001, 1, 2, 50000),
(1002, 2, 3, 700);