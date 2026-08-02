# Private access modifier : Can only be accessed in the class 
# we can access and change (data mangling)


# how to create private variable 

# variable (public) ----- _variable(protected) ----- __variable(private)

#put double underscore in front



class Bank_acc:
    def __init__(self,name,acc_no,phone_no):
        self.Name=name
        self.Acc_no=acc_no
        self.Phone_no=phone_no
        self.__Balance = 0

    def deposit(self,money):
        self.__Balance+=money
        print("Deposited",money)

    def check_balance(self):
        print("Balance",self.__Balance)


obj=Bank_acc("mohit","p123","54258435468573")
obj.check_balance()
obj.deposit(1000)
obj.check_balance()

obj.__Balance=1000000 #a new variable is created with the name __Balance but it will not change the balance because it is private variable
print("Balance",obj.__Balance)  # it will not change the balance because it is private variable 
obj.check_balance()  # it will show the balance as 1000 because we can not change the private variable from outside the class

obj.deposit(500)
obj.check_balance()  # it will show the balance as 1500 because we can not change the private variable from outside the class



"""
# data mangling: we can access and modify the private data with the help of data mangling
(in Python OOPs is implemented properly)

# object._ClassName__PrivateVariable

"""


print(obj._Bank_acc__Balance)  # it will show the balance as 1500 because we can access the private variable from outside the class with the help of data mangling
obj.check_balance

print()

obj._Bank_acc__Balance=1000000  # it will change the balance to 1000000 because we can modify the private variable from outside the class with the help of data mangling
obj.check_balance()  # it will show the balance as 1000000 because we can



class A:
    def __init__(self,name):
        self.Name=name
        self.__Secret="This is a secret"

obj = A("mohit")
print(obj.Name)  # it will show the name as mohit because it is public variable
# print(obj.__Secret)  # it will give an error because it is private variable
print(obj._A__Secret)  # it will show the secret because we can access the private variable from outside the class with the help of data mangling

"""

**4. Abstraction**

Abstraction means hiding of unnecessary details and only focusing on important things
- Whenever create a parent class in that class we provide some methods that are important (abstract method)
- whenever a child class is created it is mandartory for the class to put those important functions in that class
- if the child class is not having the important method, we will not able to create the object of that child class


dominos-> farmhouse, classic pizza, peppy paneer

(in every dominos branch, you will be able to see same pizza)

(because the dominos headquater has set the things and the branches has to implement the same)

"""


"""

**abstract method**
- the important functions, that should neccessarily be present in the child class

**abstact class**
- the parent class which contains atleast 1 abstract method
- this class gives the child classes a template

(it becomes compulsary for the child classes to give their own implementation for the abstact method)

(you cant create a object abstract class)

"""

#without abstract

class Bike:
    def __init__(self,model,brand,cc):
        self.Model=model
        self.Brand=brand
        self.CC=cc

    def start(self):
        pass

    def fuel(self):
        pass



class Family_bike(Bike):
    def start(self):
        print(self.Model,"family bike has started")

    def fuel(self):
        print(self.Model,"bike takes petrol as fuel")

class Super_bike(Bike):
    def fuel(self):
        print(self.Model,"bike takes petrol as fuel")

obj=Family_bike("pulsar","bajaj",150)
obj.start()

obj1 =Super_bike("ninja","kawasaki",1000)
obj1.fuel()


"""

how to create a abstract class
1. it should be having atleast 1 abstract method
2. it should inherit from ABC -> abstract base class

note: we cant create object of an abstract class

"""



from abc import ABC,abstractmethod

# we are importing these from abc module

#abc= Abstract methods classes
#ABC= Abstract method class

class Bike(ABC):
    def __init__(self,model,brand,cc):
        self.Model=model
        self.Brand=brand
        self.CC=cc

    @abstractmethod #this is a decorator which is used to create an abstract method
    def start(self):
        pass

    def fuel(self): #it is not an abstract method because it is not decorated with @abstractmethod
        pass

class Super_bike(Bike):
    def start(self):
        print(self.Model,"super bike has started")

    def fuel(self):
        print(self.Model,"bike takes petrol as fuel")



obj =Super_bike("ninja","kawasaki",1000)
obj.start()
obj.fuel()
print(obj.Model)


class Family_bike(Bike):
    def start(self):
        print(self.Model,"family bike has started")

    def fuel(self):
        print(self.Model,"bike takes petrol as fuel")

obj=Family_bike("pulsar","bajaj",150)
obj.start()




#Hands on
#cab booking system(Abstraction)
from abc import ABC,abstractmethod

class Cab(ABC):
  def __init__(self,name,distance):
    self.name = name
    self.distance = distance

  @abstractmethod
  def fare(self):
    pass

class Ola(Cab):
  def fare(self):
    print('Ola fare',self.distance*35)

class Uber(Cab):
  def fare(self,subscription):
    if subscription:
      print('Uber with Subscription',self.distance*20)
    else :
      print('Uber without Subscription',self.distance*40)

class Rapido(Cab):
  def fare(self):
    print('Rapido fare',self.distance*30)

distance=int(input("total distance"))
obj=Uber('uber',distance)
obj.fare(False)
obj=Ola('ola',10)
obj.fare()
obj=Rapido('rapido',10)
obj.fare()



















































































