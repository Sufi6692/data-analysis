# 🎯 Module 01: Database & Table Basics - PRACTICE CHALLENGES

## Practice Instructions
- **Total Challenges**: 5 (Easy to Expert)
- **Time**: 45-90 minutes
- **Format**: Hands-on SQL coding
- **Requirement**: Write and execute SQL code
- **Tools**: SQL Server Management Studio (SSMS) or similar

---

## Challenge 1: Bank Account System (Easy - 15 minutes)

### Objective
Create a simple database for a bank to track customers and their accounts.

### Requirements
1. Create a CUSTOMERS table
2. Create an ACCOUNTS table linked to customers
3. Add appropriate constraints
4. Insert sample data
5. Verify the data

### Starter Code

```sql
-- Step 1: Create database
CREATE DATABASE BankDB;
USE BankDB;

-- Step 2: Create CUSTOMERS table
-- TODO: Define the table with:
-- - CustomerID (INT, Primary Key, auto-increment)
-- - FirstName (VARCHAR, NOT NULL)
-- - LastName (VARCHAR, NOT NULL)
-- - Email (VARCHAR, UNIQUE, NOT NULL)
-- - PhoneNumber (VARCHAR, optional)
-- - JoinDate (DATETIME, default to today)
-- - IsActive (BIT, default to 1)

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY IDENTITY(1,1),
    -- YOUR COLUMNS HERE
);

-- Step 3: Create ACCOUNTS table
-- TODO: Define the table with:
-- - AccountID (INT, Primary Key)
-- - CustomerID (INT, Foreign Key to Customers)
-- - AccountType (VARCHAR) - 'Checking', 'Savings'
-- - Balance (DECIMAL, default 0, must be >= 0)
-- - CreatedDate (DATETIME, default today)

CREATE TABLE Accounts (
    -- YOUR TABLE DEFINITION HERE
);

-- Step 4: Insert sample data (at least 3 customers)
-- TODO: Write INSERT statements

-- Step 5: Insert sample accounts (2-3 accounts per customer)
-- TODO: Write INSERT statements

-- Step 6: Verify data
SELECT * FROM Customers;
SELECT * FROM Accounts;

-- Step 7: Query to show customer with all accounts
SELECT c.FirstName, c.LastName, a.AccountType, a.Balance
FROM Customers c
JOIN Accounts a ON c.CustomerID = a.CustomerID;
```

### Solution

```sql
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY IDENTITY(1,1),
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(20),
    JoinDate DATETIME DEFAULT GETDATE(),
    IsActive BIT DEFAULT 1
);

CREATE TABLE Accounts (
    AccountID INT PRIMARY KEY,
    CustomerID INT NOT NULL,
    AccountType VARCHAR(20) NOT NULL,
    Balance DECIMAL(15,2) DEFAULT 0,
    CreatedDate DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    CONSTRAINT CHK_Balance CHECK (Balance >= 0),
    CONSTRAINT CHK_AccountType CHECK (AccountType IN ('Checking', 'Savings'))
);

INSERT INTO Customers (FirstName, LastName, Email, PhoneNumber)
VALUES
    ('John', 'Smith', 'john@bank.com', '555-1001'),
    ('Sarah', 'Johnson', 'sarah@bank.com', '555-1002'),
    ('Mike', 'Brown', 'mike@bank.com', '555-1003');

INSERT INTO Accounts (AccountID, CustomerID, AccountType, Balance)
VALUES
    (1001, 1, 'Checking', 5000.00),
    (1002, 1, 'Savings', 15000.00),
    (1003, 2, 'Checking', 2500.50),
    (1004, 3, 'Savings', 25000.00);
```

---

## Challenge 2: Online Store (Medium - 20 minutes)

### Objective
Design a database for an online store with products, customers, and orders.

### Requirements
1. PRODUCTS table (ID, Name, Category, Price, Stock)
2. CUSTOMERS table (ID, Name, Email, Address)
3. ORDERS table (ID, CustomerID, OrderDate, TotalAmount)
4. All appropriate constraints
5. Sample data with at least 2 orders

### Your Task

```sql
-- Create database
CREATE DATABASE OnlineStore;
USE OnlineStore;

-- TODO: Create PRODUCTS table
-- TODO: Create CUSTOMERS table
-- TODO: Create ORDERS table

-- TODO: Insert sample products (at least 5)
-- TODO: Insert sample customers (at least 3)
-- TODO: Insert sample orders (at least 2)

-- TODO: Write a query showing:
-- - Customer name
-- - Order date
-- - Total amount
-- ORDER BY OrderDate DESC
```

### Hints

- Product price must be > 0
- Stock quantity must be >= 0
- Order status should be one of: 'Pending', 'Shipped', 'Delivered'
- Use FOREIGN KEY to link Orders to Customers
- Use DEFAULT GETDATE() for dates

### Testing Query

```sql
-- Should show all orders with customer info
SELECT c.FirstName + ' ' + c.LastName as CustomerName, o.OrderDate, o.TotalAmount
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
ORDER BY o.OrderDate DESC;
```

---

## Challenge 3: Hospital System (Medium - 25 minutes)

### Objective
Create a medical records database for a hospital.

### Requirements
1. PATIENTS table
2. DOCTORS table
3. APPOINTMENTS table (links patients and doctors)
4. MEDICAL_RECORDS table (tracks visits and diagnoses)
5. All constraints to ensure data quality
6. Sample data representing a realistic scenario

### Business Rules
- Each patient has a unique email
- Each doctor has a unique license number
- Appointment times must be in the future
- Appointment status: 'Scheduled', 'Completed', 'Cancelled'
- Doctor specialties: 'Cardiology', 'Orthopedics', 'Neurology', 'General Practice'

### Your Task

```sql
CREATE DATABASE HospitalDB;
USE HospitalDB;

-- TODO: Create all tables with proper constraints

-- TODO: Insert sample data
-- - At least 3 patients
-- - At least 3 doctors with different specialties
-- - At least 4 appointments
-- - At least 2 medical records

-- TODO: Query 1 - Show doctor's schedule
SELECT -- Your query here

-- TODO: Query 2 - Show patient's medical history
SELECT -- Your query here
```

### Expected Schema

```
PATIENTS
├─ PatientID (PK)
├─ FirstName
├─ LastName
├─ Email (UNIQUE)
└─ DOB

DOCTORS
├─ DoctorID (PK)
├─ FirstName
├─ LastName
├─ LicenseNumber (UNIQUE)
└─ Specialty

APPOINTMENTS
├─ AppointmentID (PK)
├─ PatientID (FK)
├─ DoctorID (FK)
├─ AppointmentDate
└─ Status

MEDICAL_RECORDS
├─ RecordID (PK)
├─ PatientID (FK)
├─ DoctorID (FK)
├─ VisitDate
├─ Diagnosis
└─ Treatment
```

---

## Challenge 4: University System (Hard - 30 minutes)

### Objective
Design a comprehensive database for a university.

### Requirements
1. STUDENTS table (ID, Name, Email, EnrollmentDate)
2. COURSES table (ID, CourseName, Credits, DepartmentID)
3. DEPARTMENTS table (ID, DepartmentName, Budget)
4. ENROLLMENTS table (StudentID, CourseID, Grade, Semester)
5. INSTRUCTORS table (ID, Name, Specialty, DepartmentID)
6. All appropriate relationships and constraints
7. Realistic sample data

### Business Rules
- Students have unique emails
- Courses belong to departments
- Each course has an instructor (add InstructorID to COURSES)
- Grades: 'A', 'B', 'C', 'D', 'F', 'Incomplete'
- Credits must be 1-4
- GPA calculation depends on grades

### Your Task

```sql
CREATE DATABASE UniversityDB;
USE UniversityDB;

-- TODO: Create all 5 tables with relationships

-- TODO: Insert sample data
-- - At least 2 departments
-- - At least 5 courses
-- - At least 3 instructors
-- - At least 10 students
-- - Enroll students in courses

-- TODO: Query 1 - List all students in Computer Science
SELECT -- Your query

-- TODO: Query 2 - Show courses and their instructors
SELECT -- Your query

-- TODO: Query 3 - Count students per department
SELECT -- Your query
```

### Challenge Extension

Add a CHECK constraint for valid GPA ranges:
```sql
-- A = 4.0, B = 3.0, C = 2.0, D = 1.0, F = 0.0
-- Incomplete = NULL
```

---

## Challenge 5: Real-World Integration (Expert - 45 minutes)

### Objective
Design a multi-table database for a social media platform (like Twitter/X).

### Requirements
1. USERS table
2. POSTS table (what users post)
3. COMMENTS table (comments on posts)
4. LIKES table (likes on posts)
5. FOLLOWERS table (user relationships)
6. All relationships and constraints
7. Comprehensive sample data

### Business Rules
- Usernames must be unique
- Posts can't be empty or very long
- A user can like a post only once
- Users can follow each other
- Comments are limited to 500 characters
- Posts timestamp automatically
- All content should track creation date

### Your Task

```sql
CREATE DATABASE SocialMediaDB;
USE SocialMediaDB;

-- TODO: Design and create all 5 tables
-- Hint: Think about relationships:
-- - POSTS links to USERS (who posted)
-- - COMMENTS link to USERS (who commented) and POSTS (which post)
-- - LIKES link to USERS (who liked) and POSTS (which post)
-- - FOLLOWERS link USERS to USERS (follower to following)

-- TODO: Insert realistic sample data
-- - 5 users
-- - 10 posts
-- - 15 comments
-- - 12 likes
-- - 8 follow relationships

-- TODO: Query 1 - Show user's timeline (posts they see)
SELECT -- Your query

-- TODO: Query 2 - Show most liked posts
SELECT -- Your query

-- TODO: Query 3 - Show user's followers
SELECT -- Your query

-- TODO: Query 4 - Show posts and their comment count
SELECT -- Your query
```

### Advanced Constraints to Consider

```sql
-- Users can't follow themselves
ALTER TABLE Followers
ADD CONSTRAINT CHK_NoSelfFollow CHECK (FollowerUserID != FollowingUserID);

-- Posts must have content
ALTER TABLE Posts
ADD CONSTRAINT CHK_PostContent CHECK (LEN(PostContent) > 0 AND LEN(PostContent) <= 280);

-- Comments must have content
ALTER TABLE Comments
ADD CONSTRAINT CHK_CommentContent CHECK (LEN(CommentContent) > 0 AND LEN(CommentContent) <= 500);
```

---

## Challenge Progression Guide

| Challenge | Difficulty | Concepts | Time |
|-----------|-----------|----------|------|
| 1. Bank | Easy | Basic tables, FK, constraints | 15 min |
| 2. Store | Medium | Multiple tables, relationships | 20 min |
| 3. Hospital | Medium | Complex relationships, business rules | 25 min |
| 4. University | Hard | 5+ tables, advanced relationships | 30 min |
| 5. Social Media | Expert | Full-stack design, self-references | 45 min |

---

## How to Approach These Challenges

### Step 1: Plan Before Coding
- Draw entities and their relationships
- Identify Primary Keys
- Identify Foreign Keys
- List constraints needed

### Step 2: Create Tables
- Start with independent tables (no FKs)
- Then create dependent tables (with FKs)
- Add constraints gradually

### Step 3: Insert Data
- Insert parent data first
- Then child data
- Verify each insert

### Step 4: Test
- Write SELECT queries
- Verify relationships work
- Try invalid inserts to test constraints

### Step 5: Document
- Add comments to code
- Explain your design choices
- Note any assumptions

---

## Testing Your Constraints

### Test NOT NULL
```sql
-- This should FAIL
INSERT INTO Customers (LastName, Email) VALUES ('Smith', 'test@email.com');
```

### Test UNIQUE
```sql
-- This should FAIL
INSERT INTO Customers (FirstName, LastName, Email) VALUES ('John', 'Smith', 'john@email.com');
INSERT INTO Customers (FirstName, LastName, Email) VALUES ('Jane', 'Smith', 'john@email.com');  -- Duplicate email
```

### Test CHECK
```sql
-- This should FAIL
INSERT INTO Accounts (AccountID, CustomerID, AccountType, Balance) 
VALUES (999, 1, 'Invalid', -100);  -- Invalid type and negative balance
```

### Test FOREIGN KEY
```sql
-- This should FAIL
INSERT INTO Accounts (AccountID, CustomerID, AccountType)
VALUES (999, 999, 'Checking');  -- CustomerID 999 doesn't exist
```

---

## Submission Checklist

For each challenge, you should have:
- [ ] All tables created with proper structure
- [ ] All Primary Keys defined
- [ ] All Foreign Keys defined
- [ ] All constraints (NOT NULL, UNIQUE, CHECK, DEFAULT) added
- [ ] Sample data inserted (realistic quantities)
- [ ] At least 2 query examples that demonstrate relationships
- [ ] Comments explaining the design
- [ ] Code runs without errors
- [ ] Constraints prevent invalid data

---

## Success Criteria

✅ **Challenge 1 (Easy)**: Can create simple related tables  
✅ **Challenge 2 (Medium)**: Can design 3-4 table systems  
✅ **Challenge 3 (Medium)**: Can handle complex relationships  
✅ **Challenge 4 (Hard)**: Can design 5+ table systems  
✅ **Challenge 5 (Expert)**: Can design self-referencing tables and complex queries  

---

## Getting Help

If you get stuck:

1. **Read the Error Message** - It tells you what went wrong
2. **Review the Theory** - Go back to 01_THEORY.md
3. **Study the Code Examples** - See how it's done in 02_CODE_EXAMPLES.sql
4. **Check Real-World Examples** - Look at 03_REAL_WORLD.md
5. **Ask for Help** - I'm here to explain any concept

---

**Practice Section Complete?**

When you finish all challenges:

1. Update SESSION_CHECKPOINTS.md with your progress
2. Note which challenges you completed
3. Identify any difficult areas
4. You're ready to move to **Module 02: SELECT Clause Fundamentals**!

---

**Practice Version**: 1.0  
**Total Challenges**: 5  
**Difficulty Range**: Easy to Expert  
**Status**: Ready for execution
