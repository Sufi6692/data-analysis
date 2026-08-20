# Numpay - > Numerical Python 
# Numpay - > it is powerful library  
# Numpay - > array, Nd Array, Multidimensional Array, Matrix, Linear Algebra, Random Number Generation, Fourier Transform, and more.

 # List -> Storing multiple values 
# Disadvantages of List -> It is slow, consumes more memory, and it is not efficient for mathematical operations.
# it Takes of lot of time to execute because it store actual memory address of elements 
# We can't perform arithmetic operations directly in the list


#Numpay array 

# we can only have one data type in an Array[1,2,3,4,5] -> int, float, string, boolean[1,2,3,4,5,"Sam"] -> [1,2,3,4,5] -> int [1,2,3,4,5] -> int [1.0,2.0,3.0,4.0,5.0] -> float [True,False,True] -> boolean ["Sam","John","Doe"] -> string
# It is very faster in comparison to list because it store actual value of elements in the memory and it is efficient for mathematical operations.
# It provides lots of inbuilt functions for various arithmetic operations


# How to create an numpay array ---->

import numpy as np # -> np is alias name of numpy library


np_arr = np.array([1,2,3,4,5]) # -> 1D array
print(np_arr) # -> [1 2 3 4 5]

print(type(np_arr)) # -> <class 'numpy.ndarray'>

np_array = np.array([[1,2,3],[4,5,6],[7,8,9]]) # -> 2D array
print(np_array) # -> [[1 2 3] [4 5 6] [7 8 9]]


# data type precedence in array 

l = [1,2,3,4,5] # -> int
np_arr3 = np.array(l)
print(np_arr3) # -> [1 2 3 4 5] -> int
np_arr3.dtype # -> dtype('int64')


# float > int

l = [1,2,3,4,6.8,"Sam"] 
np_arr4 = np.array(l)
print(np_arr4) # -> ['1' '2' '3' '4' '6.8' 'Sam'] -> string
np_arr4.dtype # -> dtype('<U32') -> string


#string > float >int

#dtype -> datatype of elements of numpay array 


# N Dimensional Array -> Nd Array

# 0D -> 0 Dimensional Array -> Scalar Value
# It is scaler values means it is just a single point

zero_d = np.array(7)
print(zero_d) # -> 7
print(type(zero_d)) # -> <class 'numpy.ndarray'>


#ndim - > number of dimensions of array

print(zero_d.ndim) # -> 0

print(zero_d.shape) # -> () -> empty tuple means it is 0D array


# 1 -d Array -> 1 Dimensional Array -> Vector
one_d = np.array([1,2,3,4,5])
print(one_d) # -> [1 2 3 4 5]
print(type(one_d)) # -> <class 'numpy.ndarray'>
print(one_d.ndim) # -> 1
print(one_d.shape) # -> (5,) -> tuple with one element means it is 1D array


# 2 -d Array -> 2 Dimensional Array -> Matrix
two_d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(two_d) # -> [[1 2 3] [4 5 6] [7 8 9]]
print(type(two_d)) # -> <class 'numpy.ndarray'>
print(two_d.ndim) # -> 2
print(two_d.shape) # -> (3, 3) -> tuple with two elements means it is 2D array  


# 3 -d Array -> 3 Dimensional Array -> Tensor
three_d = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])
print(three_d) # -> [[[ 1  2  3] [ 4  5  6] [ 7  8  9]] [[10 11 12] [13 14 15] [16 17 18]]]
print(type(three_d)) # -> <class 'numpy.ndarray'>
print(three_d.ndim) # -> 3
print(three_d.shape) # -> (2, 3, 3) -> tuple with three elements means it is 3D array



