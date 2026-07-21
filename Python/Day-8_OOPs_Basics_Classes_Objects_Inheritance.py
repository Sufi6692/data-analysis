# What is OOPs

"""
OOPs (Object-oriented Programming) is a way of writing the code where we represent
real-world things using objects and class

Instead of writing everything in functions, we organize code like:

1. Real world entity
2.with properties/attribute(data)
3.Actions/Method(function)

"""

# Attributes: Property(data) of the object
#Method: Functions of the object

"""
1. Brezz

Property:
Brand = "Maruti"
model = "Brezza"
color = "White"
fuel = "Petrol"
etc

Methods:
Start()
Stop()
Accelerate()
Breke()
..etc

"""




"""

2. Audi Car

Property:
Brand="Audi"
Model="R8"
Color="Red"
Fule="Petrol"
.. Etc

Methods:
Start()
Stop()
Accelerate()
Brake()


"""


# we can Create a blueprint of what a car is like, and we create multiple cars using that blueprint

"""
Blueprint of a car

Properties/attributes/variable/data
-----------------------------------
Brand
Model
color
fuel
milage
type
... etc

functions/ method/ action
-------------------------
start()
stop()
accelerate()
brake()
... etc

"""
# Class

"""
The blueprint which are used to create real world thing(Object)
They are a container which contains properties and functions for a object


"""


"""
# Object

They are the real things that we create using class

They are also called as Instance of a class

eg: The actual cars that we create using the blueprint of a car is called as object
"""


"""
# pseudo code

#blueprint
class Car:
  #properties -> Variables
  Brand
  Model
  color

  #methods (functions which are written inside a class)
  start()
  Stop()

#Creating Objects of Car class
Brezza = Car()
BMW_m4 = Car()
Ennova = Car()
# brezza, BMW_m4, Ennova are objects of Car class

"""


class Car:
    #Properties
    Brand = "Maruti"
    Model = "Shift"
    Color = "Red"
    Year = 2025

    #Methods

    def Start(self):
        print("Car has started")
        
    def Stop(self):
        print("car has stopped")
    

    #creating objects
    c1 =Car()
    c1.Start() #Start(c1)
    c1.stop()
    print(c1)

    c2 =Car() #2nd object
    c2.Start()
    print(c2)
    

class car:
  #Properties
  Brand="Maruti"
  Model="Shift"
  Color="Red"
  Year=2025

  #Methods
  def Start(aarav):
    print("Car has started")
    print(aarav)

  def Stop(obj):
    print("car has stopped")



#creating objects
cc1=car()
cc1.Start()  #Start(cc1)
# cc1.Stop()
print(cc1)

cc2=car() #2nd object
cc2.Start()
print(cc2)




"""
#Self 

it is a parameter holding the address of the current object

self is the reference of the object 

>> First parameter of method of the class always hold the address of the object ,
Why ?? >> Because the Address is automatically passed as the first argument when the function is called

>> We can write anything as the first address parameter eg: self,obj,Address

"""

class Car :
   def Getdata(self,Model,Color):  #extra method to initialize the properties
      self.model = Model
      self.color = Color

   def Start(self):
      print("Car has Started")
  
   def Stop(self):
      print("Car has stopped")

   def Car_info(self):
      print("My Car is", self.model,"with color",self.color)


c1 = Car()
c1.Getdata("I20","Grey")
c1.Start()
c1.Car_info()


c2 = Car()
c2.Getdata("Thar","Black")
c2.Start()
c2.Stop()
c2.Car_info()

print(c2.model)
print(c1.model)
print(c1.color)


"""
# Constructor(init Function) it is a special type of function which is used to initialize the properties of an object

# Special ?

It automatically runs whenever an object is created

# constructor = __init__()

"""


class car:
   def __init__(self, Model, Color):        # Constructor to initialize the properties
      self.model = Model
      self.color = Color

   def Start(self):
      print("Car has Started")

   def Stop(self):
      print("Car has stopped")

   def Car_info(self):
      print("My Car is", self.model, "With color", self.color)

c1 = car("Scorpio", "Black")
c1.Start()
c1.Car_info()


c2 = car("Civic", "Blue")
c2.Start()
c2.Stop()
c2.Car_info()
      
"""

## 4. Pillars of OOP:

1. Inheritance
2. Polymorphism
3. Encapsulation
4. Abstraction

"""

"""
## 1. Inheritance

Properties in which a child class as inherit to the things of parent class 

we Derive the properties of parent class in child class


"""

class A:  #parent class
   a = 20
   def fun(self):
      print("function from parent")

class B:     #Child class
   b = 40
   def fun1(self):
      print("Function from child")

obj=B()
print(obj.b)
 #print(obj.a) it will give an error due to we have are trying to access the prenet prop with inheritance 



class A:        #Parent class
   a=20
   def fun(self):
      print("Function from parent")

#Class Child(Parent):
class B(A):     #Child class
   b = 50
   def fun(self):
      print("Function from the child")

obj = B()
print(obj.b)
print(obj.a)



"""
## Types of Inheritance:

1.Single Inheritance: One parent one child


"""


class Animal:   #parent
   def walk(self):
      print("Animals can walk")
class Dog(Animal)
   def bark(self):
      print("Dog can Bark")

d=Dog()
d.bark()
d.walk()












































































