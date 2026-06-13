# ✅ Module 01: Database & Table Basics - QUIZ

## Quiz Instructions
- **Time**: 10-15 minutes
- **Questions**: 10 (9 multiple choice + 1 short answer)
- **Passing Score**: 8/10 (80%)
- **Instructions**: Answer all questions, then check your answers against the provided solutions

---

## Questions

### Question 1: What is a Primary Key?

**Question**: Which statement best describes a Primary Key?

A) A key to access the database server  
B) A column that uniquely identifies each row in a table  
C) The most important column in the table  
D) The first column created in a table  

**Your Answer**: _______

---

### Question 2: Choosing the Right Data Type

**Question**: You need to store customer email addresses. Which data type is BEST?

A) INT  
B) DECIMAL  
C) VARCHAR or NVARCHAR  
D) BIT  

**Your Answer**: _______

---

### Question 3: Understanding NOT NULL

**Question**: What does the NOT NULL constraint mean?

A) The column cannot store any values  
B) The column is not important  
C) The column must always have a value  
D) The column cannot be used in queries  

**Your Answer**: _______

---

### Question 4: Foreign Key Purpose

**Question**: What is the PRIMARY purpose of a Foreign Key?

A) To back up data from another table  
B) To link data from one table to another table  
C) To speed up database queries  
D) To encrypt sensitive data  

**Your Answer**: _______

---

### Question 5: VARCHAR vs CHAR

**Question**: What is the key difference between VARCHAR and CHAR data types?

A) VARCHAR stores text, CHAR stores numbers  
B) VARCHAR stores numbers, CHAR stores text  
C) VARCHAR is variable-length, CHAR is fixed-length  
D) CHAR is faster than VARCHAR  

**Your Answer**: _______

---

### Question 6: UNIQUE Constraint

**Question**: A table has a UNIQUE constraint on the Email column. What does this mean?

A) Every row must have an email address  
B) Email addresses cannot be more than 50 characters  
C) No two rows can have the same email address  
D) Only one email is allowed per customer  

**Your Answer**: _______

---

### Question 7: DEFAULT Constraint

**Question**: What does a DEFAULT constraint do?

A) Deletes old records automatically  
B) Prevents NULL values from being inserted  
C) Automatically assigns a value if none is provided  
D) Makes the column required  

**Your Answer**: _______

---

### Question 8: Data Type for Money

**Question**: You're building a shopping cart system and need to store product prices. Which data type is BEST for accuracy?

A) INT  
B) FLOAT  
C) DECIMAL(10,2)  
D) VARCHAR  

**Your Answer**: _______

---

### Question 9: CHECK Constraint

**Question**: Which of these could NOT be enforced with a CHECK constraint?

A) Age must be between 18 and 120  
B) Salary must be greater than 0  
C) Email must be unique  
D) Quantity ordered must be greater than 0  

**Your Answer**: _______

---

### Question 10: Short Answer - Design Question

**Question**: You're designing a database for a library. Explain why you would create separate tables for Books, Members, and Checkouts instead of one large table with all information.

**Your Answer** (write 3-4 sentences):

____________________________________________

____________________________________________

____________________________________________

____________________________________________

---

## Answer Key

### Question 1: Primary Key
**Correct Answer**: B - A column that uniquely identifies each row in a table

**Explanation**: 
A Primary Key is a special column (or columns) that uniquely identifies each record. Every row must have a unique Primary Key, and it cannot be NULL. Examples: CustomerID, ProductID, EmployeeID.

---

### Question 2: Choosing the Right Data Type
**Correct Answer**: C - VARCHAR or NVARCHAR

**Explanation**:
- INT is for numbers
- DECIMAL is for precise numbers (like money)
- BIT is for true/false values
- VARCHAR and NVARCHAR are for text strings

Since emails are text, VARCHAR(100) or NVARCHAR(100) would be appropriate.

---

### Question 3: Understanding NOT NULL
**Correct Answer**: C - The column must always have a value

**Explanation**:
NOT NULL is a constraint that requires every row to have a value in that column. You cannot insert or update a row without providing a value for NOT NULL columns. Commonly used for essential fields like FirstName, LastName, Email.

---

### Question 4: Foreign Key Purpose
**Correct Answer**: B - To link data from one table to another table

**Explanation**:
A Foreign Key creates a relationship between two tables. It references the Primary Key of another table, ensuring referential integrity. Example: Orders table has CustomerID that references Customers table's CustomerID.

---

### Question 5: VARCHAR vs CHAR
**Correct Answer**: C - VARCHAR is variable-length, CHAR is fixed-length

**Explanation**:
- CHAR(10): Always takes up 10 characters of space (padded with spaces if needed)
- VARCHAR(10): Takes up only as much space as needed (up to 10 characters)
- Use CHAR for fixed-length data (like country codes: US, UK, CA)
- Use VARCHAR for variable-length data (like names: John, Alexander, Sam)

---

### Question 6: UNIQUE Constraint
**Correct Answer**: C - No two rows can have the same email address

**Explanation**:
UNIQUE constraint ensures that all values in a column are unique (no duplicates). Common uses:
- Email (each customer has unique email)
- Username (each user has unique login)
- SSN (each person has unique social security number)
- ProductSKU (each product has unique stock code)

Note: Unlike Primary Key, UNIQUE can allow NULL values.

---

### Question 7: DEFAULT Constraint
**Correct Answer**: C - Automatically assigns a value if none is provided

**Explanation**:
DEFAULT constraint provides an automatic value when no value is specified. Examples:
```sql
JoinDate DATETIME DEFAULT GETDATE()  -- Current date/time
IsActive BIT DEFAULT 1               -- True/Active
Status VARCHAR(20) DEFAULT 'Pending' -- Pending status
```

This reduces data entry errors and ensures consistency.

---

### Question 8: Data Type for Money
**Correct Answer**: C - DECIMAL(10,2)

**Explanation**:
- INT: Can't store decimal places (whole numbers only)
- FLOAT: Approximate decimals (99.9999999) - precision issues with money
- DECIMAL(10,2): Exact decimals with 2 places ($999,999.99) - PERFECT for money
- VARCHAR: Text only, can't do calculations

DECIMAL is the standard choice for financial data because it preserves exact decimal places.

---

### Question 9: CHECK Constraint
**Correct Answer**: E - Email must be unique

**Explanation**:
CHECK constraint validates that values meet a condition. It can enforce:
- Range checks: Age > 18
- Value restrictions: Status IN ('Active', 'Inactive')
- Numeric constraints: Salary > 0

But UNIQUE is a different constraint type, not a CHECK constraint. Uniqueness requires UNIQUE constraint, not CHECK.

---

### Question 10: Short Answer - Design Question
**Expected Answer**:

Separate tables should be used because:
1. **Avoids repetition**: Book information isn't duplicated for every checkout
2. **Maintains relationships**: Easy to track which member checked out which book
3. **Enables queries**: Can quickly find all books by a member, or all members who borrowed a book
4. **Data integrity**: Foreign keys prevent invalid checkouts (member doesn't exist, book doesn't exist)

**Acceptable variations**:
- Reduces storage space
- Prevents data inconsistencies
- Makes updates easier (change book title once, not multiple times)
- Follows normalization principles

---

## Quiz Scoring

| Questions Correct | Score | Result |
|---|---|---|
| 10/10 | 100% | 🏆 Excellent! Master this module. |
| 9/10 | 90% | ✅ Very Good! Minor gaps exist. |
| 8/10 | 80% | ✅ Passing! Ready to move forward. |
| 7/10 | 70% | ⚠️ Review theory and try again. |
| <7/10 | <70% | ❌ Study theory, then retake. |

---

## What to Do If You Scored Below 80%

1. **Reread** the theory section for questions you missed
2. **Review** the specific concepts that caused confusion
3. **Study** code examples related to those concepts
4. **Retake** the quiz after reviewing
5. **Ask** if any concepts are still unclear

---

## What to Do If You Scored 80% or Higher

✅ Great job! You understand the fundamentals.

**Next Steps**:
- Review the Real-World examples
- Complete the Assessment
- Do all Practice Challenges
- Then move to Module 02: SELECT Clause Fundamentals

---

**Quiz Completion**: After finishing, update SESSION_CHECKPOINTS.md with your score and move to the Assessment section.
