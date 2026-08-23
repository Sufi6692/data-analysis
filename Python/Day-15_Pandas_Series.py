# ============================================================
# Day - 15
# Topic - Pandas Introduction and Series
# ============================================================


# ------------------------------------------------------------
# Pandas
# ------------------------------------------------------------

"""
Pandas is a Python library used for:

1. Data Manipulation
2. Data Analysis
3. Data Cleaning
4. Data Transformation
5. Data Exploration

Pandas is commonly used when working with real-world datasets.

Real-world data can contain:
- Missing values
- Duplicate values
- Incorrect values
- Different data types
- CSV files
- Excel files
- Large datasets


Why was Pandas created?

NumPy is very powerful for:
- Numerical calculations
- Arrays
- Mathematical operations

But real-world data is not always just numbers.

For example, a dataset may contain:
- Names
- Age
- Salary
- Dates
- Missing values
- Categories
- Text

Pandas was created to make working with this type of
structured and real-world data easier.


Pandas helps us to:

1. Load datasets
   - CSV
   - Excel
   - etc.

2. Clean data
   - Handle missing values
   - Remove duplicates
   - Correct incorrect values

3. Manipulate data
   - Filter
   - Sort
   - Group
   - Merge

4. Analyze data
   - Calculate statistics
   - Find patterns
   - Prepare data for further analysis
"""


# ------------------------------------------------------------
# Import Pandas
# ------------------------------------------------------------

import pandas as pd


# ------------------------------------------------------------
# Pandas Data Structures
# ------------------------------------------------------------

"""
Pandas mainly provides two important data structures:

1. Series
2. DataFrame


Series
------
A Series is a one-dimensional labeled data structure.

We can think of a Series as:

Data + Index

Example:

Index    Data
  0       30
  1       40
  2       50
  3       60
"""


# ------------------------------------------------------------
# 1. Creating a Series from a List
# ------------------------------------------------------------

s = pd.Series([30, 40, 50, 60, 61, 80, 90])

print(s)

print(type(s))


# ------------------------------------------------------------
# 2. Creating a Series from a Dictionary
# ------------------------------------------------------------

"""
In a dictionary:

Keys   -> become Series labels/index
Values -> become Series data
"""

d1 = {
    'A': 101,
    'hii': 102,
    103: 'Hello'
}

s2 = pd.Series(d1)

print(s2)


# ------------------------------------------------------------
# 3. Creating a Series from a Tuple
# ------------------------------------------------------------

t = (31, 32, 33, 34, 46)

s4 = pd.Series(t)

print(s4)


# ------------------------------------------------------------
# Series can contain different types of objects
# ------------------------------------------------------------

s = pd.Series([10, 20, [30, 40], 50])

print(s)

print(type(s))


# ------------------------------------------------------------
# 4. Creating a Series with Custom Labels / Index
# ------------------------------------------------------------

a1 = pd.Series(
    [100, 200, 300, 400],
    index=['a', 'b', 'c', 'd']
)

print(a1)


# ------------------------------------------------------------
# Accessing Elements in a Series
# ------------------------------------------------------------


# ------------------------------------------------------------
# 1. Label-Based Access
# ------------------------------------------------------------

a1 = pd.Series(
    [100, 200, 300, 400],
    index=['a', 'b', 'c', 'd']
)

print(a1)

print(a1['d'])


# ------------------------------------------------------------
# 2. Position-Based Access
# ------------------------------------------------------------

a1 = pd.Series(
    [100, 200, 300, 400],
    index=['a', 'b', 'c', 'd']
)

print(a1)

# Position 0 -> 100
# Position 1 -> 200
# Position 2 -> 300
# Position 3 -> 400

# print(a1[3])


# ------------------------------------------------------------
# Slicing a Series
# ------------------------------------------------------------

print(a1)


# Position-based slicing

print(a1[1:4])


# Label-based slicing

print(a1['b':'d'])


# ------------------------------------------------------------
# .loc - Label Based Access
# ------------------------------------------------------------

"""
.loc is used when we want to access data
using index labels.
"""

x1 = pd.Series(
    [100, 200, 300, 400, 500],
    index=['a', 'b', 'c', 'd', 'e']
)

print(x1)


# Access one value using label

print(x1.loc['d'])


# Access multiple values using labels

print(x1.loc[['a', 'b', 'd']])


# Label-based slicing

print(x1.loc['b':'d'])


# ------------------------------------------------------------
# .iloc - Integer Position Based Access
# ------------------------------------------------------------

"""
.iloc is used when we want to access data
using integer positions.

Position starts from 0.
"""

x1 = pd.Series(
    [100, 200, 300, 400, 500],
    index=['a', 'b', 'c', 'd', 'e']
)

print(x1)


# Access value at position 3

print(x1.iloc[3])


# Access multiple positions

print(x1.iloc[[2, 3, 4]])


# ------------------------------------------------------------
# Operations on a Series
# ------------------------------------------------------------

x1 = pd.Series(
    [100, 200, 300, 400, 500],
    index=['a', 'b', 'c', 'd', 'e']
)

print(x1)


# ------------------------------------------------------------
# Scalar Addition
# ------------------------------------------------------------

print(x1 + 5)


# ------------------------------------------------------------
# Scalar Subtraction
# ------------------------------------------------------------

print(x1 - 5)


# ------------------------------------------------------------
# Multiplication
# ------------------------------------------------------------

print(x1 * 2)


# ------------------------------------------------------------
# Division
# ------------------------------------------------------------

print(x1 / 2)


# ------------------------------------------------------------
# Operations Between Two Series
# ------------------------------------------------------------

s1 = pd.Series([100, 200, 300, 400])

s2 = pd.Series([500, 600, 700, 800])


# Element-wise Addition

print(s1 + s2)


# Element-wise Subtraction

print(s1 - s2)


# ============================================================
# End of Day - 15
# ============================================================