# conditional Statements
from ast import While


age = int(input("Enter your age : "))
if (age >= 18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


    #elif: grading: A,B,C,...F
    #if (condition1):
     # code
    #elif (condition2):
     # code
    # else : 
        # code
marks=int(input("Enter your Marks : "))

if (marks>=85):
    print("Grade : A")
elif (marks>=65):
    print("Grade : B")
elif(marks>=45):
    print("Grade : C")
else:
    print("Grade : F, Fail")


#c1: 78>=85 no
#c2 : 78>=65 yes -> block will be executed

# c1: 35>=85 no
# c2: 35>=65 no
# c3: 35>=45 no
# if no condition statisfy then go to else

# c1: 75>=85 no
# c2: 75>=45 yes


#Nested if : if statement inside a if statement

attendance = 60 
marks = 67

if(attendance>=75):
    if(marks>=85 and marks<=100):
        print("Grade : A")
    elif(marks>=65 and marks<84):
        print("Grade : B")
    elif(marks>=45 and marks<=64):
        print("Grade : C")
    else:
        print("Grade : F, Fail")
else:
    print("You are not eligible for exam due to low attendance.")

# 91>=75 yes
#   67>=85 and 67<=100 no
#   67>=65 and 67<=84  yes


# loops statements : #
# for, while 
# for: Iterates through a sequence (list, tuple, dictionary, set, or string)
# for : (starting, ending, increment)

for i in range(1, 11):
    print(i)


for i in range(1, 11, 2):
    print(i)


# 10 -1
for i in range(10, 0,-1):
    print(i)


    for i in range(1, 4,2):
        print("Hello Welcome to sufi's World")
        print(i)

L = ["Python", "Java", "C", "C++"]
for i in range(0,len(L)):
    print(i,"indexed value is",L[i])

#reverse order
for i in range(len(L)-1,-1,-1):
    print(i,"Indexed value is",L[i])


L = ["Python", "Java", "C", "C++"]
for i in L:
    print(i)



# While : Runs till a condition is True

# while(condition):
#     code

# 1 - 5

n = 1
while(n<=5):        #1<=5
    print(n)    
    n+=1


n = 5
#if the while loop condition is false it will never go inside the loop
while(n>=1):
    print(n)
    n-=1


n = 5
while(n==1):
    print(n)
    n-=1

#Control Statements 

#break : Stop the loop and come out of the loop
#continue : Skip the current iteration and go to next iteration


# Break Example
for i in range(1, 11):
    if(i ==6):
        break
    print(i)


    # Continue Example

for i in range(1, 11):
    if(i == 6):
        continue
    print(i)


#functions: a block of code that perform a specific task, and these can be reused


def Greet():
    print("Hello Welcome to Sufi's World")
    print("Have a nice day")

    Greet()


def sum(): 
    a = 30
    b = 50  
    print("Sum of a and b is : ", a+b)

    sum()




































































