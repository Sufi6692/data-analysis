-- =============================================================================
-- MODULE 01: DATABASE & TABLE BASICS - CODE EXAMPLES
-- =============================================================================
-- This file contains runnable T-SQL code for creating databases, tables, 
-- and understanding data types, constraints, and relationships.
--
-- You can copy and paste each example into SQL Server Management Studio (SSMS)
-- and execute them one by one.
-- =============================================================================

-- ============================================================================
-- EXAMPLE 1: Creating a Basic Database
-- ============================================================================

-- Create a new database
CREATE DATABASE CompanyDB;

-- Switch to using that database
USE CompanyDB;

-- Verify database was created
SELECT * FROM sys.databases WHERE name = 'CompanyDB';


-- ============================================================================
-- EXAMPLE 2: Understanding Data Types - Create a Sample Table
-- ============================================================================

-- Create EMPLOYEES table with various data types
CREATE TABLE Employees (
    -- Integer types
    EmployeeID INT PRIMARY KEY,              -- Whole numbers, unique identifier
    EmployeeNumber BIGINT UNIQUE,            -- Large whole number (optional)
    DepartmentCode TINYINT,                  -- Small whole number (0-255)
    
    -- String/Text types
    FirstName VARCHAR(50) NOT NULL,          -- Variable text, max 50 chars, required
    LastName VARCHAR(50) NOT NULL,           -- Variable text, max 50 chars, required
    MiddleInitial CHAR(1),                   -- Fixed 1 character
    Email NVARCHAR(100) UNIQUE,              -- Unicode text, must be unique
    
    -- Date/Time types
    DateOfBirth DATE,                        -- Just the date (YYYY-MM-DD)
    HireTime TIME,                           -- Just the time (HH:MM:SS)
    LastLoginDateTime DATETIME,              -- Date and time together
    LastModifiedDateTime DATETIME2,          -- More precise date/time
    
    -- Numeric/Decimal types
    BaseSalary DECIMAL(10,2),                -- 10 total digits, 2 after decimal ($9,999,999.99)
    CommissionRate FLOAT,                    -- Approximate decimal (0.15 for 15%)
    PerformanceScore NUMERIC(3,1),           -- 3 total digits, 1 decimal (99.9)
    
    -- Boolean type
    IsFullTime BIT,                          -- 1=true, 0=false
    IsActive BIT DEFAULT 1,                  -- Default to 1 (true/active)
    
    -- Large text types
    Biography TEXT,                          -- Long description (up to 2GB)
    Comments NVARCHAR(MAX)                   -- Very long unicode text (up to 2GB)
);

-- Verify table was created
SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_NAME = 'Employees';

-- View the structure of the table
EXEC sp_help 'Employees';

-- Alternative: View column details
SELECT 
    COLUMN_NAME, 
    DATA_TYPE, 
    IS_NULLABLE,
    COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Employees'
ORDER BY ORDINAL_POSITION;


-- ============================================================================
-- EXAMPLE 3: Understanding Constraints
-- ============================================================================

-- Create CUSTOMERS table with comprehensive constraints
CREATE TABLE Customers (
    -- Primary Key with IDENTITY (auto-increment)
    CustomerID INT PRIMARY KEY IDENTITY(1,1),  -- Auto-increment starting at 1
    
    -- NOT NULL constraints
    FirstName NVARCHAR(50) NOT NULL,           -- Must have a value
    LastName NVARCHAR(50) NOT NULL,            -- Must have a value
    
    -- UNIQUE constraint
    Email NVARCHAR(100) UNIQUE NOT NULL,       -- No duplicates allowed + required
    
    -- Optional columns (nullable)
    PhoneNumber VARCHAR(20),                   -- Can be NULL
    DateOfBirth DATE,                          -- Can be NULL
    
    -- DEFAULT constraint
    RegistrationDate DATETIME DEFAULT GETDATE(),  -- Defaults to current date/time
    IsActive BIT DEFAULT 1,                    -- Defaults to 1 (active)
    
    -- CHECK constraint (custom validation rule)
    CONSTRAINT CHK_CustomerAge CHECK (
        -- Ensures customer is at least 18 years old
        DATEDIFF(YEAR, DateOfBirth, GETDATE()) >= 18
        OR DateOfBirth IS NULL  -- Allow NULL if not provided
    )
);

-- Verify table structure
EXEC sp_help 'Customers';


-- ============================================================================
-- EXAMPLE 4: Understanding Foreign Keys & Relationships
-- ============================================================================

-- Create DEPARTMENTS table (parent table)
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100) NOT NULL,
    DepartmentBudget DECIMAL(15,2),
    ManagerEmployeeID INT  -- Will reference Employees table
);

-- Create EMPLOYEES table with Foreign Key (child table)
CREATE TABLE EmployeesWithDept (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    DepartmentID INT NOT NULL,
    Salary DECIMAL(10,2),
    HireDate DATETIME,
    
    -- Foreign Key constraint
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
    -- This enforces: DepartmentID must exist in Departments table
);


-- ============================================================================
-- EXAMPLE 5: Inserting Data into Tables
-- ============================================================================

-- Single INSERT statement
INSERT INTO Departments VALUES (1, 'Sales', 500000, NULL);
INSERT INTO Departments VALUES (2, 'Engineering', 800000, NULL);
INSERT INTO Departments VALUES (3, 'Human Resources', 300000, NULL);

-- Multiple inserts in one statement
INSERT INTO EmployeesWithDept 
(EmployeeID, FirstName, LastName, Email, DepartmentID, Salary, HireDate)
VALUES
    (1, 'John', 'Smith', 'john.smith@company.com', 1, 75000, '2020-01-10'),
    (2, 'Sarah', 'Johnson', 'sarah.j@company.com', 2, 85000, '2019-06-15'),
    (3, 'Mike', 'Brown', 'mike.b@company.com', 1, 70000, '2018-09-20'),
    (4, 'Emily', 'Davis', 'emily.d@company.com', 2, 82000, '2021-02-01');

-- Insert using DEFAULT values
INSERT INTO Customers (FirstName, LastName, Email, PhoneNumber, DateOfBirth)
VALUES ('Alex', 'Wilson', 'alex@email.com', '555-1234', '1990-05-15');
-- RegistrationDate and IsActive will use their DEFAULT values

-- Verify inserts
SELECT * FROM Departments;
SELECT * FROM EmployeesWithDept;
SELECT * FROM Customers;


-- ============================================================================
-- EXAMPLE 6: Foreign Key Constraint Enforcement
-- ============================================================================

-- This INSERT will SUCCEED (Department 2 exists)
INSERT INTO EmployeesWithDept 
VALUES (5, 'Jessica', 'Martinez', 'jessica.m@company.com', 2, 78000, '2022-03-05');

-- This INSERT will FAIL (Department 99 doesn't exist)
-- Uncomment to see the error:
-- INSERT INTO EmployeesWithDept 
-- VALUES (6, 'Tom', 'Anderson', 'tom.a@company.com', 99, 80000, '2022-04-10');
-- Error: The INSERT, UPDATE, or DELETE statement conflicted with a FOREIGN KEY constraint

-- Verify the successful insert
SELECT * FROM EmployeesWithDept WHERE EmployeeID = 5;


-- ============================================================================
-- EXAMPLE 7: Checking Constraints in Action
-- ============================================================================

-- This INSERT will SUCCEED (Customer is 18+)
INSERT INTO Customers (FirstName, LastName, Email, DateOfBirth)
VALUES ('Robert', 'Taylor', 'robert@email.com', '1990-01-15');

-- This INSERT will FAIL (Customer is under 18)
-- Uncomment to see the error:
-- INSERT INTO Customers (FirstName, LastName, Email, DateOfBirth)
-- VALUES ('Tommy', 'Youth', 'tommy@email.com', '2015-06-20');
-- Error: The INSERT statement conflicted with CHECK constraint

-- NULL values are allowed by CHECK constraint
INSERT INTO Customers (FirstName, LastName, Email)
VALUES ('Patricia', 'Unknown', 'patricia@email.com');
-- DateOfBirth is NULL, which is allowed


-- ============================================================================
-- EXAMPLE 8: Unique Constraint
-- ============================================================================

-- This INSERT will SUCCEED (unique email)
INSERT INTO Customers (FirstName, LastName, Email)
VALUES ('David', 'Green', 'david@email.com');

-- This INSERT will FAIL (duplicate email)
-- Uncomment to see the error:
-- INSERT INTO Customers (FirstName, LastName, Email)
-- VALUES ('Daniel', 'Duplicate', 'david@email.com');
-- Error: Violation of UNIQUE KEY constraint


-- ============================================================================
-- EXAMPLE 9: NOT NULL Constraint
-- ============================================================================

-- This INSERT will SUCCEED (all NOT NULL columns provided)
INSERT INTO Customers (FirstName, LastName, Email)
VALUES ('Lisa', 'Brown', 'lisa@email.com');

-- This INSERT will FAIL (missing LastName, which is NOT NULL)
-- Uncomment to see the error:
-- INSERT INTO Customers (FirstName, Email)
-- VALUES ('James', 'james@email.com');
-- Error: Cannot insert NULL into column


-- ============================================================================
-- EXAMPLE 10: DEFAULT Values in Action
-- ============================================================================

-- Insert with explicit DEFAULT
INSERT INTO Customers (FirstName, LastName, Email, RegistrationDate, IsActive)
VALUES ('Mark', 'Wilson', 'mark@email.com', DEFAULT, DEFAULT);
-- RegistrationDate = TODAY, IsActive = 1

-- Insert without specifying DEFAULT columns
INSERT INTO Customers (FirstName, LastName, Email)
VALUES ('Sandra', 'Moore', 'sandra@email.com');
-- RegistrationDate = TODAY (default), IsActive = 1 (default)

-- Verify defaults were applied
SELECT CustomerID, FirstName, Email, RegistrationDate, IsActive 
FROM Customers 
WHERE FirstName IN ('Mark', 'Sandra');


-- ============================================================================
-- EXAMPLE 11: Viewing All Data
-- ============================================================================

-- View all customers
SELECT * FROM Customers;

-- View all employees with their departments
SELECT * FROM EmployeesWithDept;

-- View all departments
SELECT * FROM Departments;


-- ============================================================================
-- EXAMPLE 12: Modifying Table Structure (ALTER TABLE)
-- ============================================================================

-- Add a new column to existing table
ALTER TABLE Employees
ADD DepartmentID INT;

-- Modify column data type
ALTER TABLE Employees
ALTER COLUMN FirstName VARCHAR(100);  -- Increase from 50 to 100

-- Add a constraint to existing table
ALTER TABLE Employees
ADD CONSTRAINT CHK_Salary CHECK (BaseSalary > 0);

-- Drop a column (if it exists)
-- ALTER TABLE Employees DROP COLUMN DepartmentID;


-- ============================================================================
-- EXAMPLE 13: Identifying Database Objects
-- ============================================================================

-- View all tables in current database
SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_TYPE = 'BASE TABLE'
ORDER BY TABLE_NAME;

-- View all columns in a specific table
SELECT 
    COLUMN_NAME,
    DATA_TYPE,
    CHARACTER_MAXIMUM_LENGTH,
    IS_NULLABLE,
    COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Employees'
ORDER BY ORDINAL_POSITION;

-- View all constraints on a table
SELECT 
    CONSTRAINT_NAME,
    CONSTRAINT_TYPE,
    TABLE_NAME
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME = 'Customers';


-- ============================================================================
-- EXAMPLE 14: Practical Scenario - E-Commerce Database
-- ============================================================================

-- Create simplified e-commerce schema
CREATE TABLE Products (
    ProductID INT PRIMARY KEY IDENTITY(1,1),
    ProductName NVARCHAR(200) NOT NULL,
    Description NVARCHAR(MAX),
    Price DECIMAL(10,2) NOT NULL,
    StockQuantity INT DEFAULT 0,
    IsActive BIT DEFAULT 1,
    CONSTRAINT CHK_Price CHECK (Price > 0),
    CONSTRAINT CHK_Stock CHECK (StockQuantity >= 0)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY IDENTITY(1,1),
    CustomerID INT NOT NULL,
    OrderDate DATETIME DEFAULT GETDATE(),
    TotalAmount DECIMAL(10,2),
    OrderStatus VARCHAR(20) DEFAULT 'Pending',
    CONSTRAINT FK_Customer FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    CONSTRAINT CHK_Status CHECK (OrderStatus IN ('Pending', 'Shipped', 'Delivered', 'Cancelled'))
);

CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY IDENTITY(1,1),
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10,2) NOT NULL,
    CONSTRAINT FK_Order FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    CONSTRAINT FK_Product FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    CONSTRAINT CHK_Quantity CHECK (Quantity > 0),
    CONSTRAINT CHK_Price2 CHECK (UnitPrice > 0)
);

-- Insert sample products
INSERT INTO Products (ProductName, Description, Price, StockQuantity)
VALUES 
    ('Laptop', 'High-performance laptop for work', 999.99, 10),
    ('Mouse', 'Wireless mouse with 5 buttons', 29.99, 50),
    ('Keyboard', 'Mechanical RGB keyboard', 149.99, 25);

-- Create an order
INSERT INTO Orders (CustomerID, OrderStatus)
VALUES (1, 'Pending');

-- Add items to order
INSERT INTO OrderItems (OrderID, ProductID, Quantity, UnitPrice)
VALUES 
    (1, 1, 1, 999.99),
    (1, 2, 2, 29.99);

-- View the data
SELECT * FROM Products;
SELECT * FROM Orders;
SELECT * FROM OrderItems;


-- ============================================================================
-- EXAMPLE 15: Cleanup (Optional - for learning/testing)
-- ============================================================================

-- View all tables before cleanup
SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';

-- To DELETE data from tables (keeping structure):
-- DELETE FROM OrderItems;
-- DELETE FROM Orders;
-- DELETE FROM Products;
-- DELETE FROM Customers;
-- DELETE FROM EmployeesWithDept;
-- DELETE FROM Departments;

-- To DROP entire tables (removing structure):
-- DROP TABLE OrderItems;  -- Must drop dependent table first
-- DROP TABLE Orders;
-- DROP TABLE Products;

-- To DROP entire database (all data and tables):
-- DROP DATABASE CompanyDB;

-- ============================================================================
-- KEY TAKEAWAYS FROM CODE EXAMPLES
-- ============================================================================
/*
✅ CREATE DATABASE - Create new database
✅ CREATE TABLE - Define table structure
✅ PRIMARY KEY - Unique identifier
✅ FOREIGN KEY - Relationships between tables
✅ NOT NULL - Required values
✅ UNIQUE - No duplicates
✅ DEFAULT - Automatic values
✅ CHECK - Business rule validation
✅ INSERT - Add data
✅ IDENTITY - Auto-increment
✅ Data Types - INT, VARCHAR, DECIMAL, DATE, DATETIME, BIT, etc.
✅ CONSTRAINT - Enforce data quality
✅ ALTER TABLE - Modify existing tables
✅ INFORMATION_SCHEMA - View database structure
*/
