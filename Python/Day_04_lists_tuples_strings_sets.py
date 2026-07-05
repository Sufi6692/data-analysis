# DELETE THE ELEMENT FROM A LIST

z = ['HELLO', 'hii', 'python', 10,11,'python','red']
print(z)

# 1- remove() -> it will remove the specific value from the list
# it will always remove the first occurred value
# syntax - listname.remove('value')
# DELETE THE ELEMENT FROM A LIST
z.remove('python')
print(z)

# 2- pop() - remove the value but based on index
# syntax - listname.pop(index)
print(z)
z.pop(2)
print(z)
# 3- del -> delete the value based on range  - it will help to delete multiple values
# syntax - del listname[start : stop (end+1)]
print(z)
del z[1:3]      
print(z)
# 4- clear() -> it will remove all the elements from the list
print(z)
z.clear()
print(z)
# SOME OTHER FUNCTIONS
# 1- len() -> it will return the length of the sequence
# total number of elements
a1 = ['a','b','abc','intellipaat','python',10,19,28]
print(len(a1))
# 2- count() -> give the frequency of element (occurrence of element)
a2 = ['a','a','a','hii',9.4,80 , 'morning']
len(a2)
print(a2.count('a'))
print(a2.count(9.4))
# 3- index() - it will return the index of value
l1 = [10,1,2,3,4,5,6,7,'python']
l1.index(10)
l1.index(5)
l1.index('python')


'''
2. Tuples - used to store multiple elements in a single variable
- created using () - parenthesis
- Ordered collection of elements
- tuples are heterogenous(store values of different data types)
- can have duplicate values
- tuples are immutable - we cannot change the values of tuple once created
- tuples are faster than list
'''
t1 = (10 , 'hii' , 'first example' , 'June','June')
print(t1)
print(type(t1))
# ACCESS THE ELEMENT OF TUPLE
t2 = ('red','misha' , 'akhila', 30 , 40 , 50)
print(t2)
t2[2]
t2[-4]
# multiple elements from a tuple
t2
t2[1 : 4]
print(t2)
# t2[0] = 'pink'
# IF WE TRY TO MODIFY THE TUPLE IT WILL GIVE ERROR BECAUSE TUPLES ARE IMMUTABLE

# TYPECASTING -> WE CAN CONVERT TUPLE INTO A LIST AND MAKE THE CHANGES
print(t2)
l1 = list(t2)
print(l1)
l1[0] = 'pink'
print(l1)
t2 = tuple(l1)
print(t2)

# we can also use len , count , index for tuples
'''
3- STRINGS -** sequence of characters encolsed in single , double or triple quotes

- ordered collection of elements

- immutabe (can't change them)

'''

s = 'Yasmin'
print(s)
print(type(s))
# ACCESS THE ELEMENT OF STRING?
s1 = 'Hello World'
s1[1]
s1[5]
s1[6]
s1[4:7]
a = "i love python"
len(a)
a.index('o')
# STRING FUNCTIONS:-
# 1- lower() -> convert string into lower case
# syntax - string.lower()
a2 = 'HELLO'
a2.lower()
# 2- upper() -> convert string into upper case
# syntax - string.upper()
a3 = 'hello world'
a3.upper()
# 3- capitalize() -> will convert the first letter of string into upper case
# syntax - string.capitalize()
print(a3.capitalize())
# 4- title() -> it will capitalize every first word in a sentence
a4 = ' i am learning python'
a4.title()
# 5- strip() -> remove the blank space from the start and end of string
a = '           python      '
print(a)
print(a.strip())
# 6- lstrip() -> remove the whitespace from the beginning of string
b = "    hello python"
print(b)
print(b.lstrip())
# 7 - rstrip() -> remove the whitespace from the end of string

c = " hello python           "
print(c)
print(c.rstrip())
# replace() -> we can replace any value

x1 = " hello   world"
x1.replace("   ","")
a = 'hii'
b = a.replace('h','H')
b
# STRING OPERATIONS

# 1- Concatenation -> used to combine two or more strings

h1 = 'Manish '
h2 = 'Kumar'
print(h1 + h2)

# 2- Repetition -> string * number ---> string will repeat n number of times

s = 'hiii ' * 2

print(s)
b="We***are*******learning*****Pythonconcept"
ans = b.replace('*'," ")
print(ans)

res = " ".join(ans.split())
print(res)
'''
**NON-SEQUENTIAL DATA TYPE -** elements are not arranged in a sequence or arrange in an ordered way (no specific position/index)

- **set , dictionary**

'''

'''
**1- set -** unordered collection of distinct elements

- it stores unique values (no duplicate values are allowed in set)

- created using {}

- mutable (but they only support - add an element , delete any element)

'''

s1 = {1,'hii' , 'red' , 9.2 , 4 , 1 ,2 ,'red'}
s1

print(type(s1))

s1 = {1, 'hii', 'red', 9.2, 4, 1, 2, 'red'}
# print(s1[3]) # unordered collection of elements












