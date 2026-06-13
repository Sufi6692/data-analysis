# 📚 Module 01: Database & Table Basics

## Module Overview
- **Duration**: 1-2 days (3-5 hours)
- **Difficulty**: Beginner
- **Prerequisites**: None
- **Next Module**: Module 02: SELECT Clause Fundamentals

---

## 📖 Section 01: THEORY

### What is a Database?

A **database** is an organized collection of structured data stored and accessed electronically from a computer system.

Think of it like this:
- **Excel Spreadsheet** = Simple database (single table)
- **Database** = Multiple related tables with relationships

#### Real-World Analogy

```
📚 Library System:
├── Books Table (Book ID, Title, Author, Published Date)
├── Members Table (Member ID, Name, Email, Join Date)
└── Rentals Table (Rental ID, Member ID, Book ID, Return Date)

These tables are RELATED:
- A Member can rent multiple Books
- A Book can be rented by multiple Members
```

### Database Characteristics

| Characteristic | Description |
|---|---|
| **Structured** | Data organized in rows & columns |
| **Persistent** | Data survives after program closes |
| **Accessible** | Easy to query and retrieve data |
| **Secure** | Access control and permissions |
| **Consistent** | Data integrity maintained |
| **Scalable** | Can handle large amounts of data |

---

### Relational Database Concepts

A **relational database** organizes data into related tables.

#### Key Concept: Tables

A **table** is a collection of related data entries.

```
CUSTOMERS Table:
┌───────────┬──────────┬────────────┬──────────────┐
│CustomerID │FirstName │ LastName   │ Email        │
├───────────┼──────────┼────────────┼──────────────┤
│    1      │   John   │   Smith    │ john@ex.com  │
│    2      │   Sarah  │   Johnson  │ sarah@ex.com │
│    3      │   Mike   │   Brown    │ mike@ex.com  │
└───────────┴──────────┴────────────┴──────────────┘
```

#### Table Components

1. **Row (Record/Tuple)**: One complete entry
   - Example: John Smith's customer record

2. **Column (Field/Attribute)**: One type of information
   - Example: FirstName column

3. **Cell**: Intersection of row and column
   - Example: "John" cell

---

### Data Types: Why They Matter

Data types define **what kind of data** can be stored and **how much space** it takes.

#### Common SQL Data Types

| Type | Example | Size | Use Case |
|------|---------|------|----------|
| **INT** | 25, -100, 0 | 4 bytes | Ages, counts, IDs |
| **VARCHAR(50)** | "John Smith" | Variable | Names, emails, text |
| **DECIMAL(10,2)** | 99.99, 150.50 | 8 bytes | Money, prices |
| **DATE** | 2026-06-13 | 3 bytes | Birth dates, order dates |
| **DATETIME** | 2026-06-13 14:30:00 | 8 bytes | Full timestamps |
| **BOOLEAN** | TRUE, FALSE | 1 byte | Yes/No flags |
| **TEXT** | Long paragraphs | Variable | Descriptions, comments |

**Why size matters?**
- Smaller types = Faster queries
- Smaller database = Lower storage costs
- Choose appropriate type = Better performance

#### T-SQL Specific Types

```sql
-- Standard SQL
INT              -- Integer
VARCHAR(50)      -- Variable character string, max 50 chars
DATE             -- Date only (YYYY-MM-DD)

-- T-SQL Specific
INT              -- 4-byte integer
BIGINT           -- 8-byte integer
SMALLINT         -- 2-byte integer
TINYINT          -- 1-byte integer
DECIMAL(p,s)     -- Fixed decimal (p=precision, s=scale)
FLOAT            -- Approximate numeric
NVARCHAR(n)      -- Unicode character string
DATETIME         -- Date + Time (accurate to 3.33ms)
DATETIME2        -- Date + Time (more precise)
CHAR(n)          -- Fixed-length string
TEXT             -- Large text data
BIT              -- Boolean (0 or 1)
```

---

### What is a Schema?

A **schema** is like a blueprint that defines:
- What tables exist
- What columns each table has
- What data type each column is
- What relationships exist between tables

```
SCHEMA Example:
─────────────────────────────────────────
CUSTOMERS Table:
  ├─ CustomerID (INT) - Primary Key
  ├─ FirstName (VARCHAR(50))
  ├─ LastName (VARCHAR(50))
  └─ Email (VARCHAR(100))

ORDERS Table:
  ├─ OrderID (INT) - Primary Key
  ├─ CustomerID (INT) - Foreign Key → CUSTOMERS.CustomerID
  ├─ OrderDate (DATETIME)
  └─ TotalAmount (DECIMAL(10,2))

RELATIONSHIP:
  One Customer has Many Orders
```

---

### Constraints: Rules for Data

**Constraints** are rules that enforce data quality and relationships.

#### Types of Constraints

1. **PRIMARY KEY**
   - Uniquely identifies each row
   - Cannot be NULL
   - One per table
   ```
   CustomerID: 1, 2, 3, 4... (each unique, no repeats)
   ```

2. **FOREIGN KEY**
   - Links to another table's primary key
   - Maintains relationships
   ```
   Orders.CustomerID must exist in Customers.CustomerID
   ```

3. **UNIQUE**
   - All values must be different
   - Can be NULL
   ```
   Email: no two customers can have same email
   ```

4. **NOT NULL**
   - Column must always have a value
   - Cannot leave blank
   ```
   FirstName cannot be empty
   ```

5. **CHECK**
   - Value must meet a condition
   ```
   Age must be > 0
   Salary must be < 1000000
   ```

6. **DEFAULT**
   - Automatic value if not provided
   ```
   JoinDate defaults to TODAY
   Status defaults to 'Active'
   ```

#### Real-World Example

```
EMPLOYEES Table with Constraints:
┌────────────┬──────────────┬──────────────┐
│ EmployeeID │ Name         │ Salary       │
├────────────┼──────────────┼──────────────┤
│ 1          │ John (NULL?) │ -5000 (bad)  │
│ 2          │ Sarah        │ 50000        │
└────────────┴──────────────┴──────────────┘

CONSTRAINTS Prevent:
- EmployeeID: 1, 1, 1 (PRIMARY KEY enforces uniqueness)
- Name: NULL (NOT NULL prevents empty)
- Salary: -5000 (CHECK ensures > 0)
```

---

### Real-World Database Examples

#### Example 1: E-Commerce Database

```
Products Table
├─ ProductID (INT)
├─ ProductName (VARCHAR)
├─ Price (DECIMAL)
└─ StockQuantity (INT)

Customers Table
├─ CustomerID (INT)
├─ Email (VARCHAR) UNIQUE
├─ JoinDate (DATE)
└─ IsActive (BIT)

Orders Table
├─ OrderID (INT)
├─ CustomerID (INT) → Links to Customers
├─ OrderDate (DATETIME)
└─ TotalAmount (DECIMAL)

OrderItems Table
├─ OrderItemID (INT)
├─ OrderID (INT) → Links to Orders
├─ ProductID (INT) → Links to Products
└─ Quantity (INT)
```

#### Example 2: Hospital Database

```
Patients Table
├─ PatientID (INT)
├─ FirstName (VARCHAR)
├─ LastName (VARCHAR)
└─ DOB (DATE)

Doctors Table
├─ DoctorID (INT)
├─ FullName (VARCHAR)
└─ Specialty (VARCHAR)

Appointments Table
├─ AppointmentID (INT)
├─ PatientID (INT) → Links to Patients
├─ DoctorID (INT) → Links to Doctors
├─ AppointmentDate (DATETIME)
└─ Reason (TEXT)
```

---

### Key Takeaways from Theory

✅ Database = Organized data collection  
✅ Tables = Collections of related records  
✅ Rows = Individual records  
✅ Columns = Fields/Attributes  
✅ Data Types = Define what can be stored  
✅ Schema = Blueprint of database structure  
✅ Constraints = Rules for data quality  
✅ Relationships = Tables connected by keys

---

## 💻 Section 02: CODE EXAMPLES

### Part 1: Basic SQL Setup

#### Creating a Database

```sql
-- Create a new database
CREATE DATABASE CompanyDB;

-- Use this database for subsequent commands
USE CompanyDB;
```

#### Creating Tables with Data Types

```sql
-- Create EMPLOYEES table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,           -- Primary key, auto-identifies
    FirstName VARCHAR(50) NOT NULL,       -- Required, max 50 characters
    LastName VARCHAR(50) NOT NULL,        -- Required, max 50 characters
    Email VARCHAR(100) UNIQUE,            -- Each email must be unique
    DOB DATE,                             -- Birth date (nullable)
    Salary DECIMAL(10,2),                 -- Money with 2 decimals
    HireDate DATETIME NOT NULL,           -- When they were hired
    IsActive BIT DEFAULT 1                -- 1=Active, 0=Inactive (defaults to 1)
);
```

**Breakdown:**
- `INT PRIMARY KEY` = Unique identifier for each employee
- `VARCHAR(50) NOT NULL` = Name required, maximum 50 characters
- `DECIMAL(10,2)` = Money: 10 total digits, 2 after decimal
- `BIT DEFAULT 1` = Boolean (true/false) that defaults to true

---

#### Creating Related Tables

```sql
-- Create DEPARTMENTS table
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100) NOT NULL,
    ManagerID INT                         -- Will reference Employees
);

-- Create PROJECTS table with Foreign Key
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY,
    ProjectName VARCHAR(100) NOT NULL,
    DepartmentID INT NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE,
    Budget DECIMAL(12,2),
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
    -- This creates a relationship: Projects belong to Departments
);
```

**Breakdown:**
- `FOREIGN KEY` = Links this table to another
- `REFERENCES` = Points to which table/column to link to
- This enforces: You can only add a ProjectID if DepartmentID exists

---

### Part 2: Understanding Constraints

```sql
-- Create CUSTOMERS table with comprehensive constraints
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY IDENTITY(1,1),  -- Auto-increment from 1
    FirstName NVARCHAR(50) NOT NULL,           -- Required
    LastName NVARCHAR(50) NOT NULL,            -- Required
    Email NVARCHAR(100) UNIQUE NOT NULL,       -- Unique + Required
    PhoneNumber VARCHAR(20),                   -- Optional
    DateOfBirth DATE,                          -- Optional
    RegistrationDate DATETIME DEFAULT GETDATE(),  -- Defaults to current date/time
    IsActive BIT DEFAULT 1,                    -- Defaults to 1 (active)
    CONSTRAINT CHK_Age CHECK (
        DATEDIFF(YEAR, DateOfBirth, GETDATE()) >= 18
    )
    -- Ensures customers are 18+ years old
);
```

**Key Points:**
- `IDENTITY(1,1)` = Auto-increment starting at 1, incrementing by 1
- `DEFAULT GETDATE()` = Current date/time
- `CONSTRAINT CHK_Age` = Named constraint for age validation
- `CHECK` = Business rule enforcement

---

### Part 3: Real Data Types in Action

```sql
-- EMPLOYEES table with various data types
CREATE TABLE EmployeesComplete (
    -- Integer types
    EmployeeID INT PRIMARY KEY,
    EmployeeNumber BIGINT UNIQUE,           -- Large number
    DepartmentCode TINYINT,                 -- Small number (0-255)
    
    -- String types
    FirstName VARCHAR(50) NOT NULL,         -- ASCII characters
    LastName VARCHAR(50) NOT NULL,
    MiddleInitial CHAR(1),                  -- Fixed 1 character
    Email NVARCHAR(100),                    -- Unicode (supports all languages)
    
    -- Date/Time types
    DateOfBirth DATE,                       -- Just date
    HireTime TIME,                          -- Just time
    LastLoginDateTime DATETIME,             -- Date and time
    LastModifiedDateTime DATETIME2,         -- More precise time
    
    -- Numeric types for calculations
    BaseSalary DECIMAL(10,2),               -- $999,999.99 (precision=10, scale=2)
    CommissionRate FLOAT,                   -- Approximate: 0.15 (15%)
    EmployeeScore NUMERIC(3,1),             -- 99.9 (smaller numbers)
    
    -- Boolean
    IsFullTime BIT,                         -- 1=true, 0=false
    
    -- Large text
    Biography TEXT,                         -- Long description
    Comments NVARCHAR(MAX),                 -- Very long text, Unicode
    
    -- Binary data
    PhotoData VARBINARY(MAX)                -- Image, file, etc.
);
```

**Data Type Selection Guide:**

```
Choosing between:
- VARCHAR vs NVARCHAR: Use NVARCHAR if international characters needed
- INT vs BIGINT: Use BIGINT only if numbers exceed 2 billion
- DECIMAL vs FLOAT: Use DECIMAL for money, FLOAT for approximations
- DATETIME vs DATETIME2: Use DATETIME2 for precision, DATETIME for older compatibility
- CHAR vs VARCHAR: Use CHAR for fixed-length (like country codes), VARCHAR for variable
```

---

### Part 4: Inserting Sample Data

```sql
-- Insert into EMPLOYEES
INSERT INTO Employees VALUES (
    1,                              -- EmployeeID
    'John',                         -- FirstName
    'Smith',                        -- LastName
    'john.smith@company.com',       -- Email
    '1990-05-15',                   -- DOB
    75000.00,                       -- Salary
    '2020-01-10',                   -- HireDate
    1                               -- IsActive (1 = true)
);

-- Multiple inserts at once
INSERT INTO Employees 
(EmployeeID, FirstName, LastName, Email, DOB, Salary, HireDate, IsActive)
VALUES
    (2, 'Sarah', 'Johnson', 'sarah.j@company.com', '1992-03-22', 68000, '2019-06-15', 1),
    (3, 'Mike', 'Brown', 'mike.b@company.com', '1988-11-30', 82000, '2018-09-20', 1),
    (4, 'Emily', 'Davis', 'emily.d@company.com', '1995-07-08', 55000, '2021-02-01', 0);

-- Insert with DEFAULT values
INSERT INTO Customers 
(FirstName, LastName, Email, RegistrationDate, IsActive)
VALUES
    ('Alex', 'Wilson', 'alex@email.com', GETDATE(), DEFAULT);
    -- RegistrationDate = Current date, IsActive = 1 (default)
```

---

### Part 5: Viewing Table Structure

```sql
-- T-SQL: View table structure
EXEC sp_help 'Employees';

-- T-SQL: View all columns and data types
SELECT 
    COLUMN_NAME, 
    DATA_TYPE, 
    IS_NULLABLE,
    COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Employees';

-- Result:
/*
COLUMN_NAME        DATA_TYPE   IS_NULLABLE  COLUMN_DEFAULT
EmployeeID         int         NO           NULL
FirstName          varchar     NO           NULL
LastName           varchar     NO           NULL
Email              varchar     YES          NULL
DOB                date        YES          NULL
Salary             decimal     YES          NULL
HireDate           datetime    NO           NULL
IsActive           bit         YES          1
*/
```

---

### Part 6: Understanding Relationships

```sql
-- Create related tables that work together

-- Step 1: Create DEPARTMENTS
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100) NOT NULL,
    DepartmentBudget DECIMAL(15,2)
);

-- Step 2: Create EMPLOYEES with Foreign Key to DEPARTMENTS
CREATE TABLE EmployeesWithDept (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DepartmentID INT NOT NULL,
    Salary DECIMAL(10,2),
    -- This foreign key creates a relationship
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Step 3: Insert DEPARTMENTS
INSERT INTO Departments VALUES
    (1, 'Sales', 500000),
    (2, 'Engineering', 800000),
    (3, 'Human Resources', 300000);

-- Step 4: Insert EMPLOYEES (DepartmentID must exist)
INSERT INTO EmployeesWithDept VALUES
    (1, 'John', 'Smith', 1, 75000),      -- Sales department
    (2, 'Sarah', 'Johnson', 2, 85000),   -- Engineering department
    (3, 'Mike', 'Brown', 1, 70000);      -- Sales department

-- Step 5: This would FAIL (Department 99 doesn't exist)
-- INSERT INTO EmployeesWithDept VALUES (4, 'Emily', 'Davis', 99, 60000);
-- Error: The INSERT, UPDATE, or DELETE statement conflicted with a FOREIGN KEY constraint
```

---

### Part 7: Common Database Operations

```sql
-- Check if table exists and delete it
IF OBJECT_ID('Employees', 'U') IS NOT NULL
    DROP TABLE Employees;

-- Alter existing table (add new column)
ALTER TABLE Employees
ADD Department VARCHAR(50);

-- Modify column (change data type)
ALTER TABLE Employees
ALTER COLUMN Department VARCHAR(100);

-- Rename table
EXEC sp_rename 'Employees', 'Staff';

-- View all tables in database
SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_TYPE = 'BASE TABLE';
```

---

### Key Code Concepts

✅ `CREATE TABLE` = Define table structure  
✅ `PRIMARY KEY` = Unique identifier  
✅ `FOREIGN KEY` = Link between tables  
✅ `NOT NULL` = Required field  
✅ `UNIQUE` = No duplicates  
✅ `DEFAULT` = Automatic value  
✅ `CHECK` = Business rule  
✅ `INSERT` = Add data  

---

## 🌍 Section 03: REAL-WORLD EXAMPLES

### Real-World Example 1: Netflix Database

Netflix stores massive amounts of data about users, shows, and viewing habits.

```
Netflix Simplified Schema:

USERS Table
├─ UserID (INT, Primary Key)
├─ Email (NVARCHAR, Unique)
├─ SubscriptionType (VARCHAR) - 'Basic', 'Premium', 'Standard'
├─ JoinDate (DATETIME)
├─ IsActive (BIT)
├─ MonthlyBudget (DECIMAL)
└─ PreferredLanguage (VARCHAR)

SHOWS Table
├─ ShowID (INT, Primary Key)
├─ Title (NVARCHAR)
├─ Genre (VARCHAR)
├─ ReleaseDate (DATE)
├─ AverageRating (DECIMAL)
└─ ProductionBudget (DECIMAL)

SEASONS Table
├─ SeasonID (INT, Primary Key)
├─ ShowID (INT, Foreign Key → SHOWS)
├─ SeasonNumber (TINYINT)
└─ ReleaseDate (DATE)

EPISODES Table
├─ EpisodeID (INT, Primary Key)
├─ SeasonID (INT, Foreign Key → SEASONS)
├─ EpisodeNumber (TINYINT)
├─ Title (NVARCHAR)
└─ Duration (INT)  -- in minutes

VIEWING_HISTORY Table
├─ HistoryID (INT, Primary Key)
├─ UserID (INT, Foreign Key → USERS)
├─ EpisodeID (INT, Foreign Key → EPISODES)
├─ WatchedDate (DATETIME)
├─ MinutesWatched (INT)
└─ Completed (BIT)

RATINGS Table
├─ RatingID (INT, Primary Key)
├─ UserID (INT, Foreign Key → USERS)
├─ ShowID (INT, Foreign Key → SHOWS)
├─ Rating (DECIMAL(2,1))  -- 1.0 to 10.0
└─ ReviewText (NVARCHAR(MAX))
```

**Real Business Questions Netflix Answers:**
- Which user finished The Office most recently?
- What's the average rating for Stranger Things?
- How many hours did John_Doe watch this month?
- What genres does Sarah prefer?
- Which episodes are most popular?

---

### Real-World Example 2: Amazon E-Commerce Database

```
Amazon Simplified Schema:

CUSTOMERS Table
├─ CustomerID (INT, Primary Key)
├─ Email (NVARCHAR, Unique)
├─ FirstName (NVARCHAR)
├─ LastName (NVARCHAR)
├─ PhoneNumber (VARCHAR)
├─ JoinDate (DATETIME)
└─ IsActive (BIT)

PRODUCTS Table
├─ ProductID (INT, Primary Key)
├─ ProductName (NVARCHAR)
├─ Category (VARCHAR)
├─ Price (DECIMAL)
├─ StockQuantity (INT)
├─ ManufacturerID (INT, Foreign Key)
└─ AverageRating (DECIMAL)

ORDERS Table
├─ OrderID (INT, Primary Key)
├─ CustomerID (INT, Foreign Key → CUSTOMERS)
├─ OrderDate (DATETIME)
├─ ShippingAddress (NVARCHAR(MAX))
├─ TotalAmount (DECIMAL)
├─ OrderStatus (VARCHAR)  -- 'Pending', 'Shipped', 'Delivered'
└─ TrackingNumber (VARCHAR)

ORDER_ITEMS Table
├─ OrderItemID (INT, Primary Key)
├─ OrderID (INT, Foreign Key → ORDERS)
├─ ProductID (INT, Foreign Key → PRODUCTS)
├─ Quantity (INT)
├─ UnitPrice (DECIMAL)
└─ Discount (DECIMAL)

REVIEWS Table
├─ ReviewID (INT, Primary Key)
├─ ProductID (INT, Foreign Key → PRODUCTS)
├─ CustomerID (INT, Foreign Key → CUSTOMERS)
├─ Rating (TINYINT)  -- 1 to 5
├─ ReviewText (NVARCHAR(MAX))
├─ ReviewDate (DATETIME)
└─ HelpfulCount (INT)
```

**Real Business Questions Amazon Answers:**
- How many items sold this month?
- What's total revenue by category?
- Which products have low stock?
- What's John's order history?
- Which products have the highest ratings?
- How many orders haven't shipped?

---

### Real-World Example 3: Bank Database

```
Bank Simplified Schema:

CUSTOMERS Table
├─ CustomerID (INT, Primary Key)
├─ FirstName (NVARCHAR)
├─ LastName (NVARCHAR)
├─ SSN (VARCHAR, Unique)  -- Social Security Number
├─ DOB (DATE)
├─ Email (VARCHAR, Unique)
├─ PhoneNumber (VARCHAR)
├─ JoinDate (DATETIME)
└─ Status (VARCHAR)  -- 'Active', 'Inactive', 'Closed'

ACCOUNTS Table
├─ AccountID (INT, Primary Key)
├─ CustomerID (INT, Foreign Key → CUSTOMERS)
├─ AccountType (VARCHAR)  -- 'Checking', 'Savings', 'CD'
├─ Balance (DECIMAL)
├─ InterestRate (DECIMAL)
├─ CreatedDate (DATETIME)
└─ LastModifiedDate (DATETIME)

TRANSACTIONS Table
├─ TransactionID (INT, Primary Key)
├─ AccountID (INT, Foreign Key → ACCOUNTS)
├─ TransactionType (VARCHAR)  -- 'Deposit', 'Withdrawal', 'Transfer'
├─ Amount (DECIMAL)
├─ TransactionDate (DATETIME)
├─ Description (VARCHAR)
└─ BalanceAfter (DECIMAL)

LOANS Table
├─ LoanID (INT, Primary Key)
├─ CustomerID (INT, Foreign Key → CUSTOMERS)
├─ LoanAmount (DECIMAL)
├─ InterestRate (DECIMAL)
├─ StartDate (DATE)
├─ EndDate (DATE)
├─ Status (VARCHAR)  -- 'Active', 'Paid Off', 'Defaulted'
└─ MonthlyPayment (DECIMAL)
```

**Real Business Questions Bank Answers:**
- What's John's total balance across all accounts?
- How many transactions happened today?
- Which loans are in default?
- What's total interest collected this month?
- Which accounts haven't been accessed in 6 months?

---

### Real-World Example 4: Hospital Database

```
Hospital Simplified Schema:

PATIENTS Table
├─ PatientID (INT, Primary Key)
├─ FirstName (NVARCHAR)
├─ LastName (NVARCHAR)
├─ SSN (VARCHAR, Unique)
├─ DOB (DATE)
├─ PhoneNumber (VARCHAR)
├─ Email (VARCHAR)
├─ EmergencyContact (NVARCHAR)
└─ InsuranceProvider (VARCHAR)

DOCTORS Table
├─ DoctorID (INT, Primary Key)
├─ FirstName (NVARCHAR)
├─ LastName (NVARCHAR)
├─ Specialty (VARCHAR)  -- 'Cardiology', 'Surgery', etc.
├─ LicenseNumber (VARCHAR, Unique)
├─ StartDate (DATE)
├─ OfficeNumber (VARCHAR)
└─ PhoneNumber (VARCHAR)

APPOINTMENTS Table
├─ AppointmentID (INT, Primary Key)
├─ PatientID (INT, Foreign Key → PATIENTS)
├─ DoctorID (INT, Foreign Key → DOCTORS)
├─ AppointmentDate (DATETIME)
├─ Reason (NVARCHAR(MAX))
├─ Notes (NVARCHAR(MAX))
├─ Status (VARCHAR)  -- 'Scheduled', 'Completed', 'Cancelled'
└─ Duration (INT)  -- minutes

MEDICAL_RECORDS Table
├─ RecordID (INT, Primary Key)
├─ PatientID (INT, Foreign Key → PATIENTS)
├─ DoctorID (INT, Foreign Key → DOCTORS)
├─ RecordDate (DATETIME)
├─ Diagnosis (NVARCHAR(MAX))
├─ Treatment (NVARCHAR(MAX))
├─ MedicationsPresribed (NVARCHAR(MAX))
└─ FollowUpDate (DATE)

MEDICATIONS Table
├─ MedicationID (INT, Primary Key)
├─ MedicationName (NVARCHAR)
├─ Dosage (VARCHAR)
├─ Frequency (VARCHAR)  -- 'Once daily', 'Twice daily'
└─ SideEffects (NVARCHAR(MAX))
```

**Real Business Questions Hospital Answers:**
- How many appointments does Dr. Smith have today?
- What's the patient history for Sarah?
- Which medications are most prescribed?
- How many patients visited Cardiology last month?
- Who's due for a follow-up appointment?

---

### Why Database Design Matters

**Good Database Design:**
- ✅ Fast queries
- ✅ Saves storage space
- ✅ Prevents data errors
- ✅ Supports business growth
- ✅ Easy to maintain

**Poor Database Design:**
- ❌ Slow queries
- ❌ Duplicate data (wasteful)
- ❌ Data inconsistencies
- ❌ Hard to add features
- ❌ Expensive to fix later

---

## ✅ Section 04: QUIZ

### Knowledge Check Questions

**Question 1: What is a Primary Key?**
- A) A key to your database server
- B) A column that uniquely identifies each row
- C) The most important column
- D) The first column in a table

**Answer**: B - A column that uniquely identifies each row

---

**Question 2: Which data type should you use for storing money?**
- A) INT
- B) FLOAT
- C) DECIMAL
- D) VARCHAR

**Answer**: C - DECIMAL (preserves exact decimal places for accuracy)

---

**Question 3: What does NOT NULL constraint mean?**
- A) The column must be empty
- B) The column can store no values
- C) The column must always have a value
- D) The column must store NULL

**Answer**: C - The column must always have a value

---

**Question 4: What is a Foreign Key?**
- A) A key to open the database
- B) A column that links to another table's Primary Key
- C) A password for the database
- D) A backup key

**Answer**: B - A column that links to another table's Primary Key

---

**Question 5: What's the difference between VARCHAR and CHAR?**
- A) They are identical
- B) VARCHAR is for numbers, CHAR is for letters
- C) VARCHAR is variable-length, CHAR is fixed-length
- D) There is no difference

**Answer**: C - VARCHAR is variable-length, CHAR is fixed-length

---

**Question 6: In the Netflix database, how many tables need a Foreign Key to Users?**
- A) 0
- B) 2
- C) 3
- D) 4 or more

**Answer**: D - Viewing_History, Ratings, and likely more

---

**Question 7: What is a UNIQUE constraint used for?**
- A) Making a column the most important
- B) Ensuring no two rows have the same value in that column
- C) Making queries faster
- D) Limiting the number of rows

**Answer**: B - Ensuring no two rows have the same value

---

**Question 8: What does DEFAULT constraint do?**
- A) Uses the most common value
- B) Prevents NULL values
- C) Provides an automatic value if none is specified
- D) Deletes old records

**Answer**: C - Provides an automatic value if none is specified

---

**Question 9: Short Answer: Why would a bank use separate tables for Customers, Accounts, and Transactions instead of one big table?**

Expected Answer:
- Avoids repeating customer info for every transaction
- Easier to query specific data
- Better organization
- Prevents errors
- Saves storage space

---

**Question 10: True or False: A table can have multiple Primary Keys**

**Answer**: False - A table can have only ONE Primary Key (but can have multiple UNIQUE constraints)

---

### Quiz Summary
- **Questions**: 10
- **Time to Complete**: 10-15 minutes
- **Passing Score**: 8/10 (80%)

---

## 📊 Section 05: ASSESSMENT

### Scenario-Based Assessment

**Scenario 1: Design a Library Database**

You're hired to design a database for a public library. The library needs to track:
- Books (Title, Author, ISBN, PublishDate, TotalCopies)
- Members (Name, Email, MembershipDate, MembershipType)
- Checkouts (Which member checked out which book, when, due date)
- Returns (When books were returned)

**Task 1.1**: List all tables needed
**Task 1.2**: Identify Primary Keys for each table
**Task 1.3**: Identify Foreign Keys and relationships
**Task 1.4**: Choose appropriate data types for each column

**Expected Answer Example**:
```
Tables:
1. BOOKS (BookID INT PK, ISBN VARCHAR UNIQUE, Title VARCHAR NOT NULL, ...)
2. MEMBERS (MemberID INT PK, Email VARCHAR UNIQUE, ...)
3. CHECKOUTS (CheckoutID INT PK, MemberID INT FK, BookID INT FK, ...)
```

---

**Scenario 2: Fix This Bad Design**

Someone created this table:
```sql
CREATE TABLE CustomerOrders (
    Data VARCHAR(MAX),  -- "John, Smith, john@email.com, 01/15/2024, Order123, Product1, 50.00"
    MoreData VARCHAR(MAX)
);
```

**Task 2.1**: Identify problems with this design
**Task 2.2**: Redesign it properly with multiple tables
**Task 2.3**: Add appropriate constraints

**Expected Problems**:
- All data crammed into one text field
- Hard to query
- Data duplication
- No way to represent relationships
- Poor performance

---

**Scenario 3: Real-World Database**

You work for an airline. Design a database to track:
- Passengers
- Flights
- Aircraft
- Crew members
- Bookings

**Task 3.1**: Create a schema (list tables and columns)
**Task 3.2**: Define Primary and Foreign Keys
**Task 3.3**: Add constraints for data quality
**Task 3.4**: Write CREATE TABLE statements

---

### Grading Rubric

| Criteria | Points | Requirements |
|----------|--------|--------------|
| Table Design | 20 | Proper separation of concerns |
| Primary Keys | 15 | Correct PK for each table |
| Foreign Keys | 20 | Relationships properly defined |
| Data Types | 20 | Appropriate for data |
| Constraints | 15 | NOT NULL, UNIQUE, etc. used correctly |
| Documentation | 10 | Clear, understandable |
| **Total** | **100** | |

**Passing Score**: 70/100

---

## 🎯 Section 06: PRACTICE

### Practice Challenge 1 (Easy): Bank Account System

**Objective**: Create a basic bank database

**Requirements**:
- Create a CUSTOMERS table
- Create an ACCOUNTS table
- Create a TRANSACTIONS table
- Set up relationships

**Starter Code**:
```sql
-- Create database
CREATE DATABASE BankDB;
USE BankDB;

-- TODO: Create CUSTOMERS table
-- Columns: CustomerID, FirstName, LastName, Email, PhoneNumber, JoinDate, IsActive
-- Constraints: CustomerID is PK, Email is UNIQUE, IsActive defaults to 1

-- TODO: Create ACCOUNTS table
-- Columns: AccountID, CustomerID, AccountType, Balance, CreatedDate
-- Constraints: AccountID is PK, CustomerID is FK, AccountType defaults to 'Checking'

-- TODO: Create TRANSACTIONS table
-- Columns: TransactionID, AccountID, Amount, TransactionType, TransactionDate, Description
-- Constraints: TransactionID is PK, AccountID is FK, Amount must be > 0

-- TODO: Insert sample data (at least 3 customers, 3 accounts, 5 transactions)

-- TODO: View all tables to verify structure
SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE';
```

**Solution**:
[Available in solutions folder]

---

### Practice Challenge 2 (Medium): E-Commerce Database

**Objective**: Design a complete e-commerce system

**Requirements**:
- CATEGORIES table
- PRODUCTS table (linked to CATEGORIES)
- CUSTOMERS table
- ORDERS table (linked to CUSTOMERS)
- ORDER_ITEMS table (linked to ORDERS and PRODUCTS)
- REVIEWS table (linked to CUSTOMERS and PRODUCTS)

**Constraints to Add**:
- Product price must be > 0
- Order status should be one of specific values
- Review rating 1-5
- Stock quantity >= 0

**Your Task**: Write complete CREATE TABLE statements with all constraints

---

### Practice Challenge 3 (Hard): Hospital Management System

**Objective**: Create a complex healthcare database

**Requirements**:
- PATIENTS table
- DOCTORS table (with Specialty)
- DEPARTMENTS table
- APPOINTMENTS table
- MEDICAL_RECORDS table
- MEDICATIONS table

**Advanced Requirements**:
- Ensure referential integrity
- Prevent invalid appointments (date must be future)
- Track appointment status (Scheduled, Completed, Cancelled)
- Handle multiple specialties for doctors

**Your Task**: Design schema, write CREATE statements, add sample data

---

### Practice Challenge 4 (Expert): Social Media Database

**Objective**: Design Instagram-like social media database

**Consider**:
- Users with profiles
- Posts by users
- Comments on posts
- Likes on posts and comments
- Followers (user relationships)
- Direct messages
- Hashtags
- Photos

**Your Challenge**:
1. Identify all necessary tables
2. Plan all relationships
3. Write complete schema
4. Insert realistic sample data
5. Document your design choices

---

### Challenge 5: Compare Designs

**Scenario**: Two developers created different designs for a bookstore:

**Design A**: One table with all data  
**Design B**: 10 separate normalized tables

**Your Task**:
1. Explain pros and cons of each
2. Which is better for a bookstore?
3. What would happen if bookstore grows?
4. What queries would be easier/harder in each?

---

### Practice Data Sets

**Option 1**: Download sample data sets:
- [SQL Sample Database (AdventureWorks)](https://learn.microsoft.com/sql/samples/adventureworks-install-configure)
- Uses realistic business scenarios
- Good for practice

**Option 2**: Create your own dataset:
- Think of a business (restaurant, gym, university)
- List what data they need
- Design tables and relationships
- Create sample data

---

## 🏁 Module 01: Completion Checklist

- [ ] Read all THEORY sections (Understanding database concepts)
- [ ] Study CODE EXAMPLES (Creating tables, constraints, relationships)
- [ ] Review REAL-WORLD examples (Netflix, Amazon, Bank, Hospital)
- [ ] Complete QUIZ (Score 8/10 or higher)
- [ ] Complete ASSESSMENT (Score 70/100 or higher)
- [ ] Finish all 5 PRACTICE Challenges
- [ ] Understand why each constraint matters
- [ ] Can explain relationships between tables
- [ ] Ready for Module 02: SELECT Clause

---

## 📝 Notes & Reflections

**After completing this module, answer:**

1. What was most confusing?
2. Which real-world example resonated with you?
3. What challenges did you find difficult?
4. What do you want to review again?

---

**Module 01 Created**: 2026-06-13  
**Difficulty**: Beginner  
**Estimated Time**: 3-5 hours  
**Next Module**: Module 02 - SELECT Clause Fundamentals

