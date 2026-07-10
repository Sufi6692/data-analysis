s1 = {1,True,False,77,98,'Aarav'}
print(s1)

# add : add a element randomly 
# set_name.add(value)

s1.add("Python")
print(s1)

s1.add(1)
print(s1)


#remove : Remove a specfic element
# set_name. remove(value)

s1.remove(77)
print(s1)

# if a value does not exist in the set then it will give an error
# s1.remove(100) it will give an error
print(s1)

#discard: remove a specific element simlar to remove
# difference is discard doesnt give an error if the value is not present
#set_name.discard(value)

print(s1)
s1.discard("Aarav")

print(s1)

s1.discard(120)
print(s1)

#pop(): Delete a random element
#set_name.pop()
s1.pop()
print(s1)
s1.pop()
print(s1)

akhil_fav={"Minions","Spiderman","Batman"}

Aman_fav={"Spiderman","Ironman","Dhurandhar"}

#union: all the values (unique)
# setA.union(setB)
print("union of A and B: ",akhil_fav.union(Aman_fav))


#intersection: common value
# setA.intersection(setB)
print("Intersection of A and B",akhil_fav.intersection(Aman_fav))

#difference= A-B
#setA.difference(setB)

# A
# B

# A-B

# any value which is common is a and b
# that value will be remove and it will print the rest A set


print("A-B:",akhil_fav.difference(Aman_fav))
print("B-A:",Aman_fav.difference(akhil_fav))


#symmetric_difference   # opposite of intersection
print("Symmertric Difference of A and B:",Aman_fav.symmetric_difference(akhil_fav))




#Dictionary: unordered collection of key value pairs
#each key is unique and used to Access associated value

# l=["aarav", "B" , "C" , "D" , "E"]
#     0        1     2     3     4

#    0   =  A
#    1   =  B
#    2   =  C
#   3    =  D
#   4    =  E


# Index page of a text book

# Name        Page
# chapter 1   1
# chapter 2   28
# chapter 3   39
# chapter 4   55



dict1= {
    #key:value
    "Name": "Aarav",
    "Course": "Data Science",
    "Year": 2026,
    "Nickname": "Aarav",  # duplicate values are allowed
    "Name":"lekshmi"    # previous key updates
}

# Name = Aarav
# Course = Data Science
# Year = 2026

print(dict1)

dict2={
    "name":["aarav","jaswant","lekshmi"],   # value can have multiple data with the help of list, tuple, set, dictionaries
    "course":"data science",
    "year":2026
}
print(dict2["name"][1])
print(type(dict2))



#get all your keys of a dict
# .keys()

print(dict1.keys())
print(dict2.keys())



#get all you values of a dict
# .values()

print(dict1.values())
print(dict2.values())


#get all values in (key,value) pair
# .items()

print(dict1.items())
print(dict2.items())



#dictionary inside dictionary
dict1={
    "name":{
        "fname": "Aarav",
        "lname": "Singh"
    }
}


dict1={
    "name":"aarav",
    "course":"data science",
    "year":2026
}
# add or update a key-value pair in dict
# .update(key:value)

print(dict1)
dict1.update({"course":"Full Stack"})   #update a existing key
print(dict1)

dict1.update({"education":"12th Pass"})   # new key-value pair
print(dict1)

dict1["year"]=2027   #without using .update method
print(dict1)


#pop(key): to delete a key-value pair
print(dict1)
dict1.pop("education")
print(dict1)




#user input

a=input("Enter a number:")   #input alway take string value
print(type(a))
print(a)

# sum=a+20
# print(sum)


#conditional Statements
age=int(input("Enter your Age:"))
if(age>=18):
  print("you can vote")
else:
  print("you cant vote")





