# 📊 Module 01: Database & Table Basics - ASSESSMENT

## Assessment Instructions
- **Type**: Practical scenario-based evaluation
- **Time**: 30-45 minutes
- **Difficulty**: Medium
- **Passing Score**: 70/100
- **Format**: 3 comprehensive scenarios

---

## Scenario 1: Library Management System (30 points)

### Context
You work for a public library and need to design a database to manage:
- Books in the library collection
- Members who borrow books
- Checkout records (which member borrowed which book, when)
- Return records (when books were returned)
- Fines for late returns

### Your Tasks

**Task 1.1 (10 points): Identify Tables and Entities**

List all the tables you would create and briefly describe what each stores:

```
Table 1: ___________________
Purpose: ___________________

Table 2: ___________________
Purpose: ___________________

Table 3: ___________________
Purpose: ___________________

Table 4: ___________________
Purpose: ___________________

Table 5: ___________________
Purpose: ___________________
```

**Expected Answer**:
1. BOOKS - Store book information (title, author, ISBN, etc.)
2. MEMBERS - Store member information (name, email, join date, etc.)
3. CHECKOUTS - Track which member checked out which book and when
4. RETURNS - Track when books were returned
5. FINES - Track late fees for members

---

**Task 1.2 (10 points): Design Primary and Foreign Keys**

For each table, identify:
- Primary Key (what uniquely identifies each record)
- Foreign Keys (links to other tables)

```
Table: BOOKS
Primary Key: ___________________
Foreign Keys: ___________________

Table: MEMBERS
Primary Key: ___________________
Foreign Keys: ___________________

Table: CHECKOUTS
Primary Key: ___________________
Foreign Keys: ___________________

Table: RETURNS
Primary Key: ___________________
Foreign Keys: ___________________

Table: FINES
Primary Key: ___________________
Foreign Keys: ___________________
```

**Expected Answer**:
```
BOOKS:
- PK: BookID
- FK: None (parent table)

MEMBERS:
- PK: MemberID
- FK: None (parent table)

CHECKOUTS:
- PK: CheckoutID
- FK: BookID → BOOKS, MemberID → MEMBERS

RETURNS:
- PK: ReturnID
- FK: CheckoutID → CHECKOUTS

FINES:
- PK: FineID
- FK: MemberID → MEMBERS, ReturnID → RETURNS
```

---

**Task 1.3 (10 points): Add Appropriate Constraints**

For the CHECKOUTS table, identify what constraints should be added and why:

```
Column: CheckoutDate
Constraint Type: ___________________
Reason: ___________________

Column: DueDate
Constraint Type: ___________________
Reason: ___________________

Column: MemberID
Constraint Type: ___________________
Reason: ___________________

Column: BookID
Constraint Type: ___________________
Reason: ___________________
```

**Expected Answer**:
```
CheckoutDate: NOT NULL - Must record when book was checked out
DueDate: NOT NULL - Must have a due date
MemberID: NOT NULL + FOREIGN KEY - Must know who checked out
BookID: NOT NULL + FOREIGN KEY - Must know which book was checked out
```

---

## Scenario 2: Fix This Bad Database Design (35 points)

### Context
A junior developer created this table:

```sql
CREATE TABLE AllLibraryData (
    DataID INT PRIMARY KEY,
    AllData VARCHAR(MAX)  -- "Book123|Harry Potter|J.K. Rowling|2023-01-15|John Smith|Member456|2023-01-15|2023-02-15|False"
);
```

The table stores everything as one big text string separated by pipe characters (|).

### Your Tasks

**Task 2.1 (10 points): Identify Problems**

List at least 5 problems with this design:

1. ___________________
2. ___________________
3. ___________________
4. ___________________
5. ___________________

**Expected Problems**:
1. All data crammed into one text field - impossible to query
2. Data duplication - book info repeated for every checkout
3. Cannot query "Which books did John borrow?" easily
4. Cannot enforce data validity - bad data isn't caught
5. Difficult to update (change book title = find and replace in massive text)
6. No relationships between data
7. Storage is inefficient
8. Cannot prevent orphaned data

---

**Task 2.2 (15 points): Redesign Properly**

Write CREATE TABLE statements for a proper design:

```sql
-- YOUR CODE HERE

```

**Expected Answer**:
```sql
CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Author VARCHAR(100) NOT NULL,
    ISBN VARCHAR(20) UNIQUE,
    PublishDate DATE
);

CREATE TABLE Members (
    MemberID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    JoinDate DATETIME DEFAULT GETDATE()
);

CREATE TABLE Checkouts (
    CheckoutID INT PRIMARY KEY,
    BookID INT NOT NULL,
    MemberID INT NOT NULL,
    CheckoutDate DATETIME NOT NULL,
    DueDate DATE NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Books(BookID),
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
);
```

---

**Task 2.3 (10 points): Add Constraints for Data Quality**

For the redesigned tables, add appropriate constraints:

```sql
-- Add constraints to BOOKS
ALTER TABLE Books
ADD CONSTRAINT CHK_BookID CHECK (BookID > 0);

-- Add constraints to MEMBERS
-- YOUR CODE HERE

-- Add constraints to CHECKOUTS
-- YOUR CODE HERE
```

**Expected Answer**:
```sql
ALTER TABLE Members
ADD CONSTRAINT CHK_MemberID CHECK (MemberID > 0);

ALTER TABLE Checkouts
ADD CONSTRAINT CHK_DueAfterCheckout CHECK (DueDate > CheckoutDate);
```

---

## Scenario 3: Design for an E-Commerce Platform (35 points)

### Context
You're hired to design a database for an online store that needs to track:
- Customers and their information
- Products in the store
- Orders placed by customers
- Items within each order
- Customer reviews of products

The store has these business rules:
- Each customer must have a unique email
- Product prices must be positive
- Orders can have multiple items
- Customers can rate products 1-5 stars
- Order status must be one of: Pending, Processing, Shipped, Delivered

### Your Tasks

**Task 3.1 (15 points): Create Complete Schema**

Write CREATE TABLE statements for all 5 entities with:
- Appropriate data types
- Primary keys
- Foreign keys
- Constraints (NOT NULL, UNIQUE, DEFAULT, CHECK)

```sql
-- YOUR CODE HERE

```

**Expected Answer**:
```sql
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY IDENTITY(1,1),
    Email NVARCHAR(100) UNIQUE NOT NULL,
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    PhoneNumber VARCHAR(20),
    JoinDate DATETIME DEFAULT GETDATE(),
    IsActive BIT DEFAULT 1
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY IDENTITY(1,1),
    ProductName NVARCHAR(255) NOT NULL,
    Description NVARCHAR(MAX),
    Price DECIMAL(10,2) NOT NULL,
    StockQuantity INT DEFAULT 0,
    CONSTRAINT CHK_Price CHECK (Price > 0),
    CONSTRAINT CHK_Stock CHECK (StockQuantity >= 0)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY IDENTITY(1,1),
    CustomerID INT NOT NULL,
    OrderDate DATETIME DEFAULT GETDATE(),
    TotalAmount DECIMAL(12,2),
    OrderStatus VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    CONSTRAINT CHK_Status CHECK (OrderStatus IN ('Pending', 'Processing', 'Shipped', 'Delivered'))
);

CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY IDENTITY(1,1),
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    CONSTRAINT CHK_Quantity CHECK (Quantity > 0)
);

CREATE TABLE Reviews (
    ReviewID INT PRIMARY KEY IDENTITY(1,1),
    ProductID INT NOT NULL,
    CustomerID INT NOT NULL,
    Rating TINYINT NOT NULL,
    ReviewText NVARCHAR(MAX),
    ReviewDate DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    CONSTRAINT CHK_Rating CHECK (Rating BETWEEN 1 AND 5)
);
```

---

**Task 3.2 (10 points): Write Sample INSERT Statements**

Write INSERT statements to populate sample data:

```sql
-- Insert sample customers
-- YOUR CODE HERE

-- Insert sample products
-- YOUR CODE HERE

-- Create a sample order with items
-- YOUR CODE HERE
```

**Expected Answer**:
```sql
INSERT INTO Customers (Email, FirstName, LastName, PhoneNumber)
VALUES 
    ('john@email.com', 'John', 'Smith', '555-1234'),
    ('sarah@email.com', 'Sarah', 'Johnson', '555-5678');

INSERT INTO Products (ProductName, Price, StockQuantity)
VALUES 
    ('Laptop', 999.99, 10),
    ('Mouse', 29.99, 50),
    ('Keyboard', 149.99, 25);

INSERT INTO Orders (CustomerID, OrderStatus)
VALUES (1, 'Pending');

INSERT INTO OrderItems (OrderID, ProductID, Quantity, UnitPrice)
VALUES 
    (1, 1, 1, 999.99),
    (1, 2, 2, 29.99);
```

---

**Task 3.3 (10 points): Explain Design Choices**

Explain your design decisions:

1. Why did you choose those Primary Keys?
   - ___________________

2. Why are certain columns NOT NULL?
   - ___________________

3. Why did you include Foreign Keys?
   - ___________________

4. What constraints protect data quality?
   - ___________________

---

## Grading Rubric

### Scenario 1: Library System (30 points)
| Criterion | Points | Your Score |
|-----------|--------|------------|
| Table Identification | 10 | _____ |
| PK/FK Design | 10 | _____ |
| Constraint Design | 10 | _____ |
| **Subtotal** | **30** | **_____** |

### Scenario 2: Fix Bad Design (35 points)
| Criterion | Points | Your Score |
|-----------|--------|------------|
| Identify Problems | 10 | _____ |
| Redesign Properly | 15 | _____ |
| Add Constraints | 10 | _____ |
| **Subtotal** | **35** | **_____** |

### Scenario 3: E-Commerce Schema (35 points)
| Criterion | Points | Your Score |
|-----------|--------|------------|
| Complete Schema | 15 | _____ |
| Sample Data | 10 | _____ |
| Design Explanation | 10 | _____ |
| **Subtotal** | **35** | **_____** |

---

## Total Score

**Points Achieved**: _____ / 100

**Percentage**: _____%

**Result**:
- 90-100: 🏆 **Excellent** - Ready for advanced topics
- 80-89: ✅ **Very Good** - Minor gaps exist, move forward
- 70-79: ✅ **Passing** - Understand core concepts, review weak areas
- <70: ⚠️ **Review Needed** - Study theory and scenarios again

---

## What to Do Next

### If Score ≥ 70:
✅ **Passed!** You understand database design fundamentals.

**Next Steps**:
1. Review the PRACTICE section
2. Complete all 5 practice challenges
3. Move to Module 02: SELECT Clause Fundamentals

### If Score < 70:
⚠️ **Review Required** - Don't move forward yet.

**What to Do**:
1. Reread the THEORY section
2. Study the CODE EXAMPLES again
3. Review this ASSESSMENT
4. Retake when ready
5. Ask if concepts are unclear

---

## Reflection Questions

1. What was your biggest challenge in this assessment?
   - ___________________

2. Which scenario felt easiest? Why?
   - ___________________

3. What concept do you need to practice more?
   - ___________________

4. Are you ready to move to Module 02?
   - ___________________

---

**Assessment Version**: 1.0  
**Difficulty**: Medium  
**Time to Complete**: 30-45 minutes  
**Status**: Ready for evaluation
