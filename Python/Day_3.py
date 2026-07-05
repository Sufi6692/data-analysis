# 5. Membership Operators - tells us whether a value exists inside a sequence or collection.
# . Output is boolean value
# . IN, NOT IN

name = 'Abhishek'
print('A' in name)  # True
print('Z' not in name)  # True

# 6. Identity Operators - check whether the value shares the same memory address or  same locations
# . Output is boolean value
#. IS, IS NOT
a = 1290
b = 1290
print(a == b)  
c = a

print(a is b)  # False
print(a is c)  # True
print(id(a))  # 140711679882608
print(id(b))  # 140711679882608

print(a is not b)  # True

# Small integers ------ > -5 to 256 are stored in the memory and reused, so they will have the same memory address. 
x1 = 110
x2 = 110
print(x1 is x2)  # True

print(id(x1))  # 140711679882608
print(id(x2))  # 140711679882608

#Type Casting - converting one data type to another data type
# ex -- > price = 198.99 ----- >
# . Variable_name = datatype(data)

v1 = '98'
type (v1)  # str

age = '22'
new_age = int(age)  # converting str to int
print(new_age)  # 22
print(type(new_age))  # <class 'int'>

a = 'a'
# b = int(a)  # ValueError: invalid literal for int() with base 10: 'a' 
print(a)  # 'a'


# SEQUENTIAL DATA TYPES

# Whenever we have data or values in a sequence or collection, we can use indexing to access the values.

# . LIST - ordered, mutable, allows duplicate values
# . TUPLE - ordered, immutable, allows duplicate values
# . STRING - ordered, immutable, allows duplicate values

# 1. List - ordered, mutable, allows duplicate values
# . List is a collection of values or items enclosed in square brackets [] and separated by commas
# . List can contain any data type - int, float, str, bool, list, tuple, dict, set
# . List is mutable - we can change the values of a list after it is created
#. List allows duplicate values - we can have multiple occurrences of the same value in a list
#. List is ordered - the order of the values in a list is preserved
#. List can be accessed using indexing - index starts from 0
#. List can be sliced - we can get a subset of the list using slicing
#. List can be iterated using for loop - we can loop through the values of a list using for loop
#. List can be nested - we can have a list inside a list

list = [1, 2, 3, 4, 5]
print(list)  # [1, 2, 3, 4, 5]
list1 = [10,30,'a','red','Python']
print(list1)  # [10, 30, 'a', 'red', 'Python']
type(list1)  # <class 'list'>

list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(list2[0])  # 10
print(list2[-1])  # 100
list2[0] = 1000  # changing the value of the first element
print(list2)  # [1000, 20, 30, 40,

# slicing -> is a process of accessing multiple elements based on index
# syntax - listname[start : stop (end +1) : step]
# start -> starting index
# stop  -> end +1 --> why? because end/stop index is excluded
# step  -> how much gap you need / jump -----> by default step =1


l1 = ['g','hello',9 , 10 , 'orange']
# listname [start : stop (end +1) : step
l1[0:3]  # ['g', 'hello', 9]
l1[0:5:2]  # ['g', 9, 'orange']
# try to give negative index
l1[-5:-1]  # ['g', 'hello', 9, 10]

# if start index is not defined ------> start from the very first value
l1[:3]  # ['g', 'hello', 9]
# if stop index is not defined ------> go till the very last value
l1[2:]  # [9, 10, 'orange']
l1[:]  # ['g', 'hello', 9, 10, 'orange']

# WHEN STEP = + ive ------- > left to right 
# WHEN STEP = - ive ------- > right to left
l1 = ['g','hello',9 , 10 , 'orange']
print(l1)

# 
# this will give an error due to start from positive index and coming back   l1 [2: 5: -1] 
# why empty list above ? -> because starting index is less than end index
l1 [4 : 2 : -1]

l1[-3 : -1 : 1]  # [10, 9, 'hello', 'g']

# CHANGE/ UPDATE THE ELEMENT OF A LIST

x1 = ['P' , 'Y' , 'T' , 'H' , 'O' , 'N']
print(x1)

# listname [ position] = new value
x1 [2] = 'python'

print(x1)  # ['P', 'Y', 'python', 'H', 'O', 'N']

# change multiple values

x2 = ['a' , 'b' , 'python' , 99]
print(x2)
x2 [1:3] = ['Mango' , 20]
print(x2)  # ['a', 'Mango', 20, 99]
x2[1:4] = ['banana' , 10]
print(x2)  # ['a', 'banana', 10]

# ADD A NEW ELEMENT IN A LIST?

l1 = ['rishav', 'ayush', 'abhishek', 'sachin']
print(l1)

# 1- append() -> add a single element at the end of the list
# syntax -> listname.append('new_value')

l1.append('Sufiyan')
print(l1)

# 2- extend() -> add multiple elements at the end of the list
# syntax -> listname.extend([]'new values'])

print(l1)

l1.extend(['Rohit', 'Rahul'])
print(l1)  # ['rishav', 'ayush', 'abhishek', 'sachin', 'Sufiyan', 'Rohit', 'Rahul']

# 3- insert() -> it is used to insert/add the value at a specif position
# syntax -> listname.insert(index , 'new_value')

l1.insert(2, 'Ramesh')
print(l1)  # ['rishav', 'ayush', 'Ramesh', 'abhishek', 'sachin', 'Sufiyan', 'Rohit', 'Rahul']


























