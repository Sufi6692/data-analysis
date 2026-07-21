# Find the biggest number out of 3 numbers without using max()

def FunctionMax(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)


a = 12
b = 23
c = 45

FunctionMax(a, b, c)






Largest = a

if b > Largest :
     Largest = b
if c > Largest :
    Largest = c

print(Largest)





# Multiplication table with help of loops, take user input of number

num = int(input("Enter your Number"))

for i in range(1,num):
    print(num,"*",i,"=",num*i)



    # Check for Prime number take user input (loops and if statement)

a = int(input("Enter your number :"))

for i in range(1,a+1):
    if(a%i==0):
        c+=1
if(c==2):
    print("Prime Number")
else:
    print("Not a  prime Number")


num = int(input("Enter a number :"))

if num == 1:
    print(num,"Is not a prime number")
elif(num<=0):
    print("Invalid Number")
else:
    is_prime = True


    for i in range(2,num)
     if num % i == 0:
         is_prime = False
         break
     

     if is_prime:
         print(num,"Is a prime Number")
    else:
        print(num,"Is not a prime number")


# Find Smallest element without using min inside a list

list1 = [70,100,3,101,5]
Min = list1[0]

for i in range(0,len(list1)):
    if(Min>list1[i]):
        Min=list1[i]
    
print(Min)



# count even and odd number from a list

l=[65,30,89,45,54,10,18]

even =0
odd = 0

for i in range(i,len(l)):
    if(l[i]%2 ==0):
        even+=1
    else:
        odd+=1


print("Even Count : ",even)
print("Odd Count : ",odd)


lst= [-2, 65,32, 89, 0, 45, 54, 10, 18, 1, 21]
oddCounter = 0
evenCounter = 0
for i in range(0, len(lst)):
  if(lst[i] <= 0):
    continue
  else:
    if(lst[i] % 2 == 0):
      evenCounter += 1
    else:
      oddCounter += 1
print('Even numbers are', evenCounter)
print('Odd numbers are', oddCounter)