# 🌍 Real-World Database Examples

## Real-World Example 1: Netflix Database

### The Business Problem
Netflix needs to track:
- Millions of users with subscriptions
- Thousands of shows and movies
- Which user watched what content
- When they watched it
- User ratings and reviews
- Which content is popular

### The Database Design

```sql
CREATE TABLE Users (
    UserID INT PRIMARY KEY IDENTITY(1,1),
    Email NVARCHAR(100) UNIQUE NOT NULL,
    SubscriptionType VARCHAR(20) DEFAULT 'Basic',  -- Basic, Standard, Premium
    JoinDate DATETIME DEFAULT GETDATE(),
    IsActive BIT DEFAULT 1,
    MonthlyPayment DECIMAL(10,2),
    PreferredLanguage VARCHAR(10) DEFAULT 'EN',
    CONSTRAINT CHK_SubType CHECK (SubscriptionType IN ('Basic', 'Standard', 'Premium')),
    CONSTRAINT CHK_Payment CHECK (MonthlyPayment > 0)
);

CREATE TABLE Content (
    ContentID INT PRIMARY KEY IDENTITY(1,1),
    Title NVARCHAR(255) NOT NULL,
    ContentType VARCHAR(20) NOT NULL,  -- Movie, TVShow, Documentary
    Genre VARCHAR(50),
    ReleaseDate DATE,
    DurationMinutes INT,
    Description NVARCHAR(MAX),
    AverageRating DECIMAL(3,1),
    ProductionBudget DECIMAL(15,2),
    CONSTRAINT CHK_ContentType CHECK (ContentType IN ('Movie', 'TVShow', 'Documentary')),
    CONSTRAINT CHK_Rating CHECK (AverageRating BETWEEN 0 AND 10 OR AverageRating IS NULL)
);

CREATE TABLE ViewingHistory (
    HistoryID INT PRIMARY KEY IDENTITY(1,1),
    UserID INT NOT NULL,
    ContentID INT NOT NULL,
    WatchedDate DATETIME DEFAULT GETDATE(),
    MinutesWatched INT,
    IsCompleted BIT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (ContentID) REFERENCES Content(ContentID),
    CONSTRAINT CHK_Minutes CHECK (MinutesWatched >= 0)
);

CREATE TABLE UserRatings (
    RatingID INT PRIMARY KEY IDENTITY(1,1),
    UserID INT NOT NULL,
    ContentID INT NOT NULL,
    Rating DECIMAL(2,1) NOT NULL,
    ReviewText NVARCHAR(MAX),
    RatedDate DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (ContentID) REFERENCES Content(ContentID),
    CONSTRAINT CHK_RatingValue CHECK (Rating BETWEEN 1 AND 10)
);
```

### Real Business Queries Netflix Uses

```sql
-- Who finished The Office recently?
SELECT u.Email, vh.WatchedDate
FROM ViewingHistory vh
JOIN Users u ON vh.UserID = u.UserID
WHERE vh.ContentID = (SELECT ContentID FROM Content WHERE Title = 'The Office')
  AND vh.IsCompleted = 1
ORDER BY vh.WatchedDate DESC;

-- What's the average rating for Stranger Things?
SELECT AVG(Rating) as AverageRating
FROM UserRatings
WHERE ContentID = (SELECT ContentID FROM Content WHERE Title = 'Stranger Things');

-- How many premium users watched last week?
SELECT COUNT(DISTINCT u.UserID)
FROM ViewingHistory vh
JOIN Users u ON vh.UserID = u.UserID
WHERE u.SubscriptionType = 'Premium'
  AND vh.WatchedDate >= DATEADD(DAY, -7, GETDATE());

-- Which genres are most popular?
SELECT c.Genre, COUNT(*) as ViewCount
FROM ViewingHistory vh
JOIN Content c ON vh.ContentID = c.ContentID
GROUP BY c.Genre
ORDER BY ViewCount DESC;
```

### Why This Design Works
- **Efficiency**: Fast queries even with billions of rows
- **Consistency**: Users can't rate content if it doesn't exist (FK constraint)
- **Data Quality**: Ratings must be 1-10 (CHECK constraint)
- **Scalability**: Can add millions of users without redesigning

---

## Real-World Example 2: Amazon E-Commerce

### The Business Problem
Amazon needs to track:
- Millions of customers
- Millions of products
- Orders and order history
- Inventory across warehouses
- Customer reviews and ratings
- Shipping and delivery status

### The Database Design

```sql
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY IDENTITY(1,1),
    Email NVARCHAR(100) UNIQUE NOT NULL,
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    ShippingAddress NVARCHAR(MAX),
    BillingAddress NVARCHAR(MAX),
    PhoneNumber VARCHAR(20),
    JoinDate DATETIME DEFAULT GETDATE(),
    IsActive BIT DEFAULT 1,
    LoyaltyPoints INT DEFAULT 0,
    CONSTRAINT CHK_Loyalty CHECK (LoyaltyPoints >= 0)
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY IDENTITY(1,1),
    SKU VARCHAR(50) UNIQUE NOT NULL,
    ProductName NVARCHAR(255) NOT NULL,
    Category VARCHAR(100),
    Price DECIMAL(10,2) NOT NULL,
    Cost DECIMAL(10,2),
    StockQuantity INT DEFAULT 0,
    ReorderLevel INT,
    AverageRating DECIMAL(3,1),
    ReviewCount INT DEFAULT 0,
    Supplier NVARCHAR(100),
    CONSTRAINT CHK_Price CHECK (Price > 0),
    CONSTRAINT CHK_Cost CHECK (Cost >= 0),
    CONSTRAINT CHK_Stock CHECK (StockQuantity >= 0),
    CONSTRAINT CHK_Review CHECK (AverageRating BETWEEN 0 AND 5 OR AverageRating IS NULL)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY IDENTITY(1,1),
    CustomerID INT NOT NULL,
    OrderDate DATETIME DEFAULT GETDATE(),
    ShippingAddress NVARCHAR(MAX),
    TotalAmount DECIMAL(12,2),
    TaxAmount DECIMAL(10,2),
    ShippingCost DECIMAL(10,2),
    OrderStatus VARCHAR(20) DEFAULT 'Pending',
    TrackingNumber VARCHAR(50),
    EstimatedDelivery DATE,
    ActualDelivery DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    CONSTRAINT CHK_OrderStatus CHECK (OrderStatus IN ('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled', 'Refunded')),
    CONSTRAINT CHK_Amount CHECK (TotalAmount >= 0)
);

CREATE TABLE OrderItems (
    OrderItemID INT PRIMARY KEY IDENTITY(1,1),
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10,2),
    Discount DECIMAL(10,2) DEFAULT 0,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    CONSTRAINT CHK_Quantity CHECK (Quantity > 0),
    CONSTRAINT CHK_Discount CHECK (Discount >= 0)
);

CREATE TABLE ProductReviews (
    ReviewID INT PRIMARY KEY IDENTITY(1,1),
    ProductID INT NOT NULL,
    CustomerID INT NOT NULL,
    Rating TINYINT NOT NULL,
    ReviewTitle NVARCHAR(255),
    ReviewText NVARCHAR(MAX),
    ReviewDate DATETIME DEFAULT GETDATE(),
    HelpfulCount INT DEFAULT 0,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    CONSTRAINT CHK_ReviewRating CHECK (Rating BETWEEN 1 AND 5)
);
```

### Real Business Metrics Amazon Tracks

```sql
-- Revenue this month
SELECT SUM(TotalAmount) as MonthlyRevenue
FROM Orders
WHERE MONTH(OrderDate) = MONTH(GETDATE())
  AND YEAR(OrderDate) = YEAR(GETDATE());

-- Low stock products (need reordering)
SELECT ProductID, ProductName, StockQuantity, ReorderLevel
FROM Products
WHERE StockQuantity <= ReorderLevel;

-- Top 10 best-selling products
SELECT TOP 10 p.ProductID, p.ProductName, SUM(oi.Quantity) as TotalSold
FROM OrderItems oi
JOIN Products p ON oi.ProductID = p.ProductID
GROUP BY p.ProductID, p.ProductName
ORDER BY TotalSold DESC;

-- Customer order history
SELECT o.OrderID, o.OrderDate, o.TotalAmount, o.OrderStatus
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE c.Email = 'customer@example.com'
ORDER BY o.OrderDate DESC;

-- Pending orders by region
SELECT COUNT(*) as PendingCount
FROM Orders
WHERE OrderStatus = 'Pending'
  AND OrderDate >= DATEADD(DAY, -7, GETDATE());
```

---

## Real-World Example 3: Bank Database

### The Business Problem
Banks need to track:
- Customer information and accounts
- Account balances and transactions
- Loans and credit products
- Interest calculations
- Regulatory compliance
- Fraud detection

### The Database Design

```sql
CREATE TABLE BankCustomers (
    CustomerID INT PRIMARY KEY IDENTITY(1,1),
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    SSN VARCHAR(11) UNIQUE NOT NULL,  -- Social Security Number
    DOB DATE NOT NULL,
    PhoneNumber VARCHAR(20),
    Email NVARCHAR(100),
    Address NVARCHAR(MAX),
    JoinDate DATETIME DEFAULT GETDATE(),
    AccountStatus VARCHAR(20) DEFAULT 'Active',
    CONSTRAINT CHK_Status CHECK (AccountStatus IN ('Active', 'Inactive', 'Closed', 'Suspended'))
);

CREATE TABLE BankAccounts (
    AccountID INT PRIMARY KEY IDENTITY(1,1),
    CustomerID INT NOT NULL,
    AccountNumber VARCHAR(20) UNIQUE NOT NULL,
    AccountType VARCHAR(20),  -- Checking, Savings, Money Market
    Balance DECIMAL(15,2) NOT NULL DEFAULT 0,
    InterestRate DECIMAL(5,3),
    CreatedDate DATETIME DEFAULT GETDATE(),
    LastModifiedDate DATETIME,
    IsActive BIT DEFAULT 1,
    FOREIGN KEY (CustomerID) REFERENCES BankCustomers(CustomerID),
    CONSTRAINT CHK_AccountType CHECK (AccountType IN ('Checking', 'Savings', 'MoneyMarket', 'CD')),
    CONSTRAINT CHK_Balance CHECK (Balance >= 0)
);

CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY IDENTITY(1,1),
    AccountID INT NOT NULL,
    TransactionType VARCHAR(20),  -- Deposit, Withdrawal, Transfer, Interest
    Amount DECIMAL(15,2) NOT NULL,
    TransactionDate DATETIME DEFAULT GETDATE(),
    Description NVARCHAR(MAX),
    BalanceAfter DECIMAL(15,2),
    ReferenceNumber VARCHAR(50),
    FOREIGN KEY (AccountID) REFERENCES BankAccounts(AccountID),
    CONSTRAINT CHK_Amount CHECK (Amount > 0),
    CONSTRAINT CHK_TransType CHECK (TransactionType IN ('Deposit', 'Withdrawal', 'Transfer', 'Interest', 'Fee'))
);

CREATE TABLE Loans (
    LoanID INT PRIMARY KEY IDENTITY(1,1),
    CustomerID INT NOT NULL,
    LoanAmount DECIMAL(15,2) NOT NULL,
    InterestRate DECIMAL(5,3) NOT NULL,
    LoanTerm INT NOT NULL,  -- Months
    MonthlyPayment DECIMAL(10,2),
    StartDate DATE NOT NULL,
    EndDate DATE,
    CurrentBalance DECIMAL(15,2),
    LoanStatus VARCHAR(20) DEFAULT 'Active',
    LoanType VARCHAR(20),  -- Mortgage, Auto, Personal
    FOREIGN KEY (CustomerID) REFERENCES BankCustomers(CustomerID),
    CONSTRAINT CHK_LoanAmount CHECK (LoanAmount > 0),
    CONSTRAINT CHK_Rate CHECK (InterestRate >= 0 AND InterestRate <= 15),
    CONSTRAINT CHK_LoanStatus CHECK (LoanStatus IN ('Active', 'Paid Off', 'Defaulted', 'Closed'))
);
```

### Real Business Queries Banks Use

```sql
-- Customer account balances
SELECT ba.AccountNumber, ba.AccountType, ba.Balance
FROM BankAccounts ba
JOIN BankCustomers bc ON ba.CustomerID = bc.CustomerID
WHERE bc.SSN = '123-45-6789';

-- Daily transaction summary
SELECT 
    COUNT(*) as TransactionCount,
    SUM(Amount) as TotalAmount,
    TransactionType
FROM Transactions
WHERE CAST(TransactionDate as DATE) = CAST(GETDATE() as DATE)
GROUP BY TransactionType;

-- Loans in default
SELECT l.LoanID, bc.FirstName, bc.LastName, l.CurrentBalance, l.LoanStatus
FROM Loans l
JOIN BankCustomers bc ON l.CustomerID = bc.CustomerID
WHERE l.LoanStatus = 'Defaulted';

-- Interest accrued this month
SELECT SUM(Amount) as InterestEarned
FROM Transactions
WHERE TransactionType = 'Interest'
  AND MONTH(TransactionDate) = MONTH(GETDATE());

-- High-value customers (over $1M in accounts)
SELECT bc.CustomerID, bc.FirstName, bc.LastName, SUM(ba.Balance) as TotalBalance
FROM BankCustomers bc
JOIN BankAccounts ba ON bc.CustomerID = ba.CustomerID
GROUP BY bc.CustomerID, bc.FirstName, bc.LastName
HAVING SUM(ba.Balance) > 1000000;
```

---

## Real-World Example 4: Hospital Database

### The Business Problem
Hospitals need to track:
- Patient information and medical history
- Doctor schedules and specialties
- Appointments and consultations
- Medical records and diagnoses
- Medications and prescriptions
- Patient billing and insurance

### The Database Design

```sql
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY IDENTITY(1,1),
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    SSN VARCHAR(11) UNIQUE,
    DOB DATE NOT NULL,
    PhoneNumber VARCHAR(20),
    Email NVARCHAR(100),
    EmergencyContact NVARCHAR(100),
    BloodType VARCHAR(5),
    Allergies NVARCHAR(MAX),
    RegistrationDate DATETIME DEFAULT GETDATE(),
    CONSTRAINT CHK_BloodType CHECK (BloodType IN ('O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-'))
);

CREATE TABLE Doctors (
    DoctorID INT PRIMARY KEY IDENTITY(1,1),
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    LicenseNumber VARCHAR(50) UNIQUE NOT NULL,
    Specialty VARCHAR(100),  -- Cardiology, Surgery, etc.
    PhoneNumber VARCHAR(20),
    OfficeNumber VARCHAR(10),
    HireDate DATE NOT NULL,
    IsActive BIT DEFAULT 1
);

CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY IDENTITY(1,1),
    PatientID INT NOT NULL,
    DoctorID INT NOT NULL,
    AppointmentDate DATETIME NOT NULL,
    Duration INT,  -- Minutes
    Reason NVARCHAR(MAX),
    Status VARCHAR(20) DEFAULT 'Scheduled',
    Notes NVARCHAR(MAX),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID),
    CONSTRAINT CHK_Status CHECK (Status IN ('Scheduled', 'Completed', 'Cancelled', 'No-Show'))
);

CREATE TABLE MedicalRecords (
    RecordID INT PRIMARY KEY IDENTITY(1,1),
    PatientID INT NOT NULL,
    DoctorID INT NOT NULL,
    VisitDate DATETIME DEFAULT GETDATE(),
    Diagnosis NVARCHAR(MAX),
    Treatment NVARCHAR(MAX),
    Notes NVARCHAR(MAX),
    FollowUpDate DATE,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
);

CREATE TABLE Prescriptions (
    PrescriptionID INT PRIMARY KEY IDENTITY(1,1),
    RecordID INT NOT NULL,
    PatientID INT NOT NULL,
    MedicationName NVARCHAR(200) NOT NULL,
    Dosage NVARCHAR(100),
    Frequency VARCHAR(50),  -- Once daily, Twice daily
    Duration INT,  -- Days
    PrescriptionDate DATETIME DEFAULT GETDATE(),
    FillDate DATETIME,
    FOREIGN KEY (RecordID) REFERENCES MedicalRecords(RecordID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);
```

### Real Business Queries Hospitals Use

```sql
-- Patient medical history
SELECT mr.VisitDate, d.FirstName + ' ' + d.LastName as Doctor, mr.Diagnosis, mr.Treatment
FROM MedicalRecords mr
JOIN Doctors d ON mr.DoctorID = d.DoctorID
WHERE mr.PatientID = 123
ORDER BY mr.VisitDate DESC;

-- Doctor's schedule today
SELECT a.AppointmentDate, p.FirstName + ' ' + p.LastName as PatientName, a.Reason
FROM Appointments a
JOIN Patients p ON a.PatientID = p.PatientID
WHERE a.DoctorID = 1 AND CAST(a.AppointmentDate as DATE) = CAST(GETDATE() as DATE)
ORDER BY a.AppointmentDate;

-- Patient medications
SELECT pr.MedicationName, pr.Dosage, pr.Frequency
FROM Prescriptions pr
WHERE pr.PatientID = 123;

-- Follow-up appointments due this week
SELECT p.FirstName, p.LastName, mr.FollowUpDate
FROM MedicalRecords mr
JOIN Patients p ON mr.PatientID = p.PatientID
WHERE mr.FollowUpDate BETWEEN GETDATE() AND DATEADD(DAY, 7, GETDATE());
```

---

## Key Insights from Real-World Databases

### 1. **Data Integrity is Critical**
- Banks can't afford data errors
- Hospitals must track accurate medical records
- Constraints enforce rules automatically

### 2. **Performance Matters**
- Netflix needs fast queries with billions of rows
- Amazon handles millions of orders daily
- Good database design = fast performance

### 3. **Relationships are Essential**
- Orders must link to Customers
- Employees must link to Departments
- Medical Records must link to Patients
- Foreign Keys prevent orphaned data

### 4. **Validation Rules Save Money**
- CHECK constraint prevents invalid data
- Default values reduce data entry errors
- NOT NULL ensures completeness
- UNIQUE prevents duplicates

### 5. **Scalability Requires Planning**
- Netflix didn't build one giant table
- Amazon separates Products, Orders, Reviews
- Banks separate Accounts, Transactions, Loans
- Future growth was considered from day 1

---

## Summary

Every major company uses the same database principles:
- **Tables** for different entity types
- **Relationships** to connect them
- **Constraints** for data quality
- **Data Types** for efficiency
- **Keys** for identification and linking

These aren't advanced concepts—they're **fundamental to all professional databases**.
