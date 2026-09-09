# ============================================================
# LINEAR ALGEBRA
# ============================================================

"""
Linear Algebra
--------------

Linear Algebra is a branch of mathematics that deals with:

1. Vectors
2. Matrices
3. Linear equations
4. Matrix operations
5. Transformations

In Data Science and Machine Learning, Linear Algebra is very
important because datasets are often represented using matrices.

Examples:
    - Student marks
    - Sales data
    - Image pixels
    - Machine Learning datasets
    - Neural networks
"""


# ============================================================
# 1. MATRIX
# ============================================================

"""
What is a Matrix?
-----------------

A Matrix is a rectangular arrangement of elements/numbers
organized into rows and columns.

Example:

        Column 1   Column 2   Column 3
        --------------------------------
Row 1      10         20         30
Row 2      40         50         60


Matrix A:

        A = [10  20  30
             40  50  60]


Here:

Number of rows    = 2
Number of columns = 3

Therefore:

Order of Matrix = 2 x 3
"""


# ============================================================
# 2. ROWS
# ============================================================

"""
Rows
----

A row is a horizontal arrangement of elements.

Example:

A = [10  20  30  40]

This matrix contains:

Rows    = 1
Columns = 4

Therefore:

Order = 1 x 4
"""


# ============================================================
# 3. COLUMNS
# ============================================================

"""
Columns
-------

A column is a vertical arrangement of elements.

Example:

A = [10
     20
     30
     40]

This matrix contains:

Rows    = 4
Columns = 1

Therefore:

Order = 4 x 1
"""


# ============================================================
# 4. DIMENSION OF A MATRIX
# ============================================================

"""
Dimension of Matrix
-------------------

If a matrix has:

    m = number of rows
    n = number of columns

Then its dimension is:

    m x n

Example:

A = [10  20  30
     40  50  60]

Rows    = 2
Columns = 3

Dimension = 2 x 3
"""


# ============================================================
# 5. ORDER OF A MATRIX
# ============================================================

"""
Order of Matrix
---------------

The order of a matrix is represented as:

    Number of Rows x Number of Columns

Example:

A = [1  2  3
     4  5  6]

Rows    = 2
Columns = 3

Order = 2 x 3


IMPORTANT:
Do NOT write m x m unless the matrix has the same number
of rows and columns.

General matrix:

    m x n

Square matrix:

    n x n
"""


# ============================================================
# 6. MATRIX NOTATION
# ============================================================

"""
Matrix Notation
---------------

Matrices are generally represented using capital letters.

Common notation:

A, B, C, D, X, Y, etc.

Example:

        [1  2]
A  =    [3  4]


Individual elements can be represented as:

A[i][j]

where:

i = row position
j = column position

For example:

        [10  20
A  =    30  40]

A[1][2] = 20

(Depending on the mathematical notation, indexing may start
from 1. In Python, indexing starts from 0.)
"""


# ============================================================
# 7. REAL-WORLD EXAMPLES OF MATRICES
# ============================================================

"""
Real-World Applications
-----------------------

1. STUDENT MARKS

Rows    -> Students
Columns -> Subjects

Example:

             Maths   English   Science
Student 1      80       75        90
Student 2      70       85        88
Student 3      92       78        95


This can be represented as a matrix.


2. SALES DATA

Rows    -> Products
Columns -> Months

Example:

             Jan   Feb   Mar
Product A    100   120   150
Product B    200   180   220


3. HOSPITAL DATA

Rows    -> Patients
Columns -> Medical tests

Example:

             BP   Sugar   Heart Rate
Patient 1    120   90        72
Patient 2    130   110       80


4. IMAGE DATA

A grayscale image can be represented as a matrix.

Each element represents the intensity of a pixel.

Example:

    [  0   50  100
     150  200  255
      50  100  200]


5. MACHINE LEARNING

A dataset is commonly represented as a matrix:

Rows    -> Observations / Records
Columns -> Features

Example:

             Age   Salary   Experience
Person 1      21    30000       1
Person 2      25    45000       3
Person 3      30    60000       6
"""


# ============================================================
# 8. TYPES OF MATRICES
# ============================================================

"""
There are different types of matrices based on their
dimensions and values.
"""


# ============================================================
# 8.1 ROW MATRIX
# ============================================================

"""
Row Matrix
----------

A matrix having only ONE row is called a Row Matrix.

Example:

A = [10  20  30  40]

Rows    = 1
Columns = 4

Order = 1 x 4


Real-world example:

Marks of one student:

A = [85  90  78  88]

Each value represents marks in a different subject.
"""


# ============================================================
# 8.2 COLUMN MATRIX
# ============================================================

"""
Column Matrix
-------------

A matrix having only ONE column is called a Column Matrix.

Example:

A = [10
     20
     30
     40]

Rows    = 4
Columns = 1

Order = 4 x 1


Real-world example:

Temperature readings:

A = [25
     27
     29
     30]
"""


# ============================================================
# 8.3 RECTANGULAR MATRIX
# ============================================================

"""
Rectangular Matrix
------------------

A matrix in which:

    Number of rows != Number of columns

is called a Rectangular Matrix.

Example:

A = [1  2  3
     4  5  6]

Rows    = 2
Columns = 3

Order = 2 x 3

Since:

    2 != 3

It is a rectangular matrix.


Another example:

A = [1  2
     3  4
     5  6]

Order = 3 x 2

This is also a rectangular matrix.
"""


# ============================================================
# 8.4 SQUARE MATRIX
# ============================================================

"""
Square Matrix
-------------

A matrix in which:

    Number of rows = Number of columns

is called a Square Matrix.

Example:

A = [1  2
     3  4]

Rows    = 2
Columns = 2

Order = 2 x 2


Another example:

A = [1  2  3
     4  5  6
     7  8  9]

Order = 3 x 3

This is a square matrix.
"""


# ============================================================
# 8.5 ZERO MATRIX / NULL MATRIX
# ============================================================

"""
Zero Matrix / Null Matrix
-------------------------

A matrix in which ALL elements are zero is called a
Zero Matrix or Null Matrix.

Example:

A = [0  0
     0  0]

Another example:

A = [0  0  0
     0  0  0]

Important:

A zero matrix can be rectangular or square.

Example:

2 x 3 zero matrix:

A = [0  0  0
     0  0  0]
"""


# ============================================================
# 8.6 IDENTITY MATRIX / UNIT MATRIX
# ============================================================

"""
Identity Matrix
---------------

An Identity Matrix is a square matrix where:

1. All elements on the main diagonal are 1.
2. All other elements are 0.

Example:

        [1  0  0
A  =    0  1  0
        0  0  1]


Main diagonal:

1
   1
      1

Order = 3 x 3


Important:

Identity Matrix is always a SQUARE MATRIX.

Identity matrix is represented by:

I


Important property:

A x I = A

and

I x A = A

provided the matrix dimensions are compatible.


Example:

A = [2  3
     4  5]

I = [1  0
     0  1]

A x I = A
"""


# ============================================================
# 8.7 DIAGONAL MATRIX
# ============================================================

"""
Diagonal Matrix
---------------

A Diagonal Matrix is a square matrix in which:

    All NON-DIAGONAL elements are zero.

The diagonal elements can contain any values.

Example:

A = [5  0  0
     0  8  0
     0  0  3]

This is a diagonal matrix.


Notice:

Main diagonal = 5, 8, 3

All elements outside the main diagonal = 0.


IMPORTANT:

Diagonal matrix must be a SQUARE MATRIX.
"""


# ============================================================
# 8.8 SCALAR MATRIX
# ============================================================

"""
Scalar Matrix
-------------

A Scalar Matrix is a diagonal matrix where:

    ALL diagonal elements are equal.

Example:

A = [5  0  0
     0  5  0
     0  0  5]

Diagonal elements:

5, 5, 5

All are equal.

Therefore, this is a Scalar Matrix.


IMPORTANT RELATIONSHIP:

Every Scalar Matrix is a Diagonal Matrix.

Every Diagonal Matrix is a Square Matrix.

Therefore:

Scalar Matrix
      ↓
Diagonal Matrix
      ↓
Square Matrix


Special case:

Identity Matrix is also a Scalar Matrix because:

I = [1  0
     0  1]

All diagonal elements are equal to 1.


Therefore:

Identity Matrix
      ↓
Scalar Matrix
      ↓
Diagonal Matrix
      ↓
Square Matrix
"""


# ============================================================
# 8.9 UPPER TRIANGULAR MATRIX
# ============================================================

"""
Upper Triangular Matrix
-----------------------

An Upper Triangular Matrix is a square matrix in which:

    ALL elements BELOW the main diagonal are zero.

Example:

A = [2  4  6
     0  5  7
     0  0  8]


Main diagonal:

2
   5
      8

Everything BELOW the main diagonal is 0.

Therefore, it is an Upper Triangular Matrix.


Applications:

1. Solving systems of linear equations
2. Gaussian elimination
3. LU decomposition
4. Numerical computation
"""


# ============================================================
# 8.10 LOWER TRIANGULAR MATRIX
# ============================================================

"""
Lower Triangular Matrix
-----------------------

A Lower Triangular Matrix is a square matrix in which:

    ALL elements ABOVE the main diagonal are zero.

Example:

A = [2  0  0
     4  5  0
     6  7  8]


Everything ABOVE the main diagonal is 0.

Therefore, it is a Lower Triangular Matrix.


Applications:

1. Solving linear equations
2. LU decomposition
3. Numerical computation
"""


# ============================================================
# 8.11 SYMMETRIC MATRIX
# ============================================================

"""
Symmetric Matrix
----------------

A square matrix is called a Symmetric Matrix if:

    A = Aᵀ

where:

Aᵀ = Transpose of A


Example:

A = [1  2  3
     2  4  5
     3  5  6]


Transpose:

Aᵀ = [1  2  3
      2  4  5
      3  5  6]


Since:

    A = Aᵀ

Therefore, A is a Symmetric Matrix.


IMPORTANT:

Every symmetric matrix must be a SQUARE MATRIX.
"""


# ============================================================
# 9. TRANSPOSE OF A MATRIX
# ============================================================

"""
Transpose
---------

The transpose of a matrix is obtained by:

    Converting rows into columns
    and
    columns into rows.

It is represented as:

    Aᵀ

Example:

A = [1  2  3
     4  5  6]


Transpose:

Aᵀ = [1  4
      2  5
      3  6]


Original order:

2 x 3

Transpose order:

3 x 2
"""


# ============================================================
# 10. MATRIX OPERATIONS
# ============================================================

"""
Common Matrix Operations
------------------------

We can perform several operations on matrices:

1. Matrix Addition
2. Matrix Subtraction
3. Scalar Multiplication
4. Matrix Multiplication
5. Transpose
6. Determinant
7. Inverse
"""


# ============================================================
# 10.1 MATRIX ADDITION
# ============================================================

"""
Matrix Addition
---------------

Two matrices can be added only when they have the SAME
dimensions.

Example:

A = [1  2
     3  4]

B = [5  6
     7  8]


A + B:

[1+5   2+6
 3+7   4+8]

= [6   8
   10  12]


Rule:

Same number of rows
        AND
Same number of columns
"""


# ============================================================
# 10.2 MATRIX SUBTRACTION
# ============================================================

"""
Matrix Subtraction
------------------

Like addition, subtraction requires matrices with the
same dimensions.

A = [5  6
     7  8]

B = [1  2
     3  4]


A - B:

[5-1   6-2
 7-3   8-4]

= [4  4
   4  4]
"""


# ============================================================
# 10.3 SCALAR MULTIPLICATION
# ============================================================

"""
Scalar Multiplication
---------------------

A scalar is a single number.

Example:

A = [1  2
     3  4]

Scalar = 5


5A:

[5*1   5*2
 5*3   5*4]

= [5   10
   15  20]


Every element of the matrix is multiplied by the scalar.
"""


# ============================================================
# 10.4 MATRIX MULTIPLICATION
# ============================================================

"""
Matrix Multiplication
---------------------

Matrix multiplication is different from normal
element-by-element multiplication.

For:

A = m x n

and

B = n x p

the multiplication:

A x B

is possible.

The INNER dimensions must be the same.

Example:

A = 2 x 3

B = 3 x 2

Therefore:

A x B = 2 x 2


Rule:

(m x n) x (n x p) = (m x p)


Example:

A = [1  2
     3  4]

B = [5  6
     7  8]


A x B:

First element:

(1 x 5) + (2 x 7)
= 5 + 14
= 19

Therefore:

A x B = [19  22
         43  50]
"""


# ============================================================
# 11. IMPORTANT MATRIX TERMINOLOGY
# ============================================================

"""
Main Diagonal
-------------

The main diagonal runs from:

Top-left → Bottom-right

Example:

A = [1  2  3
     4  5  6
     7  8  9]

Main diagonal:

1, 5, 9


Diagonal elements:

A[1][1]
A[2][2]
A[3][3]
"""


# ============================================================
# 12. MATRIX HIERARCHY
# ============================================================

"""
Important Relationship Between Matrix Types
--------------------------------------------

Identity Matrix
       ↓
Scalar Matrix
       ↓
Diagonal Matrix
       ↓
Square Matrix


Remember:

Every Identity Matrix is a Scalar Matrix.

Every Scalar Matrix is a Diagonal Matrix.

Every Diagonal Matrix is a Square Matrix.

But the reverse is NOT necessarily true.

For example:

A Square Matrix does NOT have to be diagonal.

A = [1  2
     3  4]

It is square, but not diagonal.
"""


# ============================================================
# 13. WHY LINEAR ALGEBRA IS IMPORTANT IN DATA SCIENCE
# ============================================================

"""
Linear Algebra in Data Science
------------------------------

Linear Algebra is heavily used in:

1. Machine Learning
2. Deep Learning
3. Computer Vision
4. Natural Language Processing
5. Recommendation Systems
6. Data Transformation
7. Statistics


Examples:

Machine Learning:

Dataset → Matrix

Features → Columns

Observations → Rows


Computer Vision:

Image → Matrix of pixel values


Neural Networks:

Weights → Matrices

Inputs → Vectors

Calculations → Matrix operations


Recommendation Systems:

Users × Products → Matrix


Therefore:

Linear Algebra is one of the mathematical foundations
of Data Science and Machine Learning.
"""


# ============================================================
# END OF NOTES
# ============================================================

"""
BREAK POINT
-----------

Covered until approximately 8:21:

1. Linear Algebra
2. Matrix
3. Rows
4. Columns
5. Dimension
6. Order
7. Matrix notation
8. Real-world applications
9. Types of matrices
10. Matrix operations
11. Transpose
12. Matrix multiplication
13. Importance of Linear Algebra in Data Science
"""



import numpy as np


# ============================================================
# 1. CREATING A MATRIX
# ============================================================

a1 = np.array([
    [1, 2, 3],
    [5, 6, 7]
])

print("Matrix A1:")
print(a1)


# ============================================================
# 2. OPERATIONS ON MATRICES
# ============================================================

m1 = np.array([
    [30, 40, 50],
    [10, 15, 30]
])

m2 = np.array([
    [5, 6, 7],
    [8, 9, 10]
])

print("\nMatrix M1:")
print(m1)

print("\nMatrix M2:")
print(m2)


# ============================================================
# 3. MATRIX ADDITION
# ============================================================

# Rule:
# Two matrices can be added if and only if
# they have the same dimensions (same number of rows and columns).

print("\nAddition:")
print(m1 + m2)


# ============================================================
# 4. MATRIX SUBTRACTION
# ============================================================

# Rule:
# Two matrices can be subtracted if and only if
# they have the same dimensions.

print("\nSubtraction:")
print(m1 - m2)


# ============================================================
# 5. SCALAR MULTIPLICATION
# ============================================================

# Scalar Multiplication:
# Multiplying every element of a matrix by a single number.

m2 = np.array([
    [100, 200, 300],
    [10, 30, 40]
])

print("\nMatrix M2:")
print(m2)

print("\nScalar Multiplication (M2 × 2):")
print(m2 * 2)


# ============================================================
# 6. DOT PRODUCT / MATRIX MULTIPLICATION
# ============================================================

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5],
    [6]
])

print("\nMatrix A:")
print(a)

print("\nMatrix B:")
print(b)

print("\nDot Product:")
print(np.dot(a, b))


# ============================================================
# 7. TRANSPOSE OF A MATRIX
# ============================================================

m3 = np.array([
    [100, 10, 90, 80],
    [40, 50, 60, 70]
])

print("\nOriginal Matrix M3:")
print(m3)

print("\nTranspose of Matrix M3:")
print(m3.T)


# ============================================================
# 8. TRACE OF A MATRIX
# ============================================================

# Trace:
# The trace of a square matrix is the sum of its
# main diagonal elements.
#
# Example:
#
#     [1  2]
#     [3  4]
#
# Main diagonal = 1 and 4
# Trace = 1 + 4 = 5

m4 = np.array([
    [1, 2],
    [3, 4]
])

print("\nMatrix M4:")
print(m4)

print("\nTrace of M4:")
print(np.trace(m4))


# ============================================================
# 9. ANOTHER MATRIX FOR TRACE
# ============================================================

m5 = np.array([
    [1, 2],
    [3, 4]
])

print("\nMatrix M5:")
print(m5)

print("\nTrace of M5:")
print(np.trace(m5))


# ============================================================
# IMPORTANT NOTE ABOUT TRACE
# ============================================================

# m3 is a 2 × 4 matrix, so it is NOT a square matrix.
#
# Although NumPy can return np.trace(m3), mathematically,
# when learning the standard definition of matrix trace,
# trace is defined for square matrices.

print("\nM3 is a 2 × 4 matrix, so it is not a square matrix.")
print("Trace is normally defined for square matrices.")


# m2 is also a 2 × 3 matrix, so it is not square.

print("\nM2 is a 2 × 3 matrix, so it is not a square matrix.")
print("Trace is normally defined for square matrices.")





























































































































