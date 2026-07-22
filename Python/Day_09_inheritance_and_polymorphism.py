"""
2.Multiple Inheritance: << Multiple parents class, single child

(A,B) -> C

C = Child
(Mother,Father) = Child


"""








class Mother:
    def fun1(self):
        print("Nature is polite")

class Father:
    def fun2(self):
        print("Hight is tall")

class child(Mother,Father):
    def fun3(self):
        print("Child  is Gamer")

obj = child()
obj.fun3()
obj.fun2()
obj.fun1()

"""
3.Hierarchical  Inheritance: << Single Parent with Multiple Children

(All the child inherits from a single parent)

Company -> CEO, Manager,Developers

Animal -> Dog, Cat, Cow

Vehicle -> Car,Bike,Truck,Train

Meta -> Whatsapp, Facebook, Instagram



"""


class Animal:   #Parent
    def __init__(self, name, legs):
        self.Legs = legs
        self.Name = name

    def breath(self):
        print(self.Name,"can Breath")

    def sleep(self):
        print(self.Name,"can Sleep")

class Dog(Animal):          #Child 1
    def bark(self):
        print("Dog can Bark")

    def info(self):
        print("Dog has",self.Legs,"legs")


class Cat(Animal):      #Child 2
    def meow(self):
        print("Cats can meow")

    def info(self):
        print("Cats has",self.Legs,"legs")


obj = Cat("Cat","4")
obj.meow()
obj.info()
obj.sleep()

print()

obj1=Dog("Dog","4")
obj1.bark()
obj1.info()



"""
4.Multi Level Inheritance : << (A -> B -> C) C is child of B,B is child of A

GrandParent -> Parent -> Child


"""



class GrandParent:
    def Property1(self):
        print("Property in Mumbai")
class Parent(GrandParent):
    def Property2(self):
        print("Property in Bengaluru")
class Child(Parent):
    def Property3(self):
        print("Property in Pune")

obj=Child()
obj.Property3()
obj.Property2()
obj.Property1()





"""
5.Hybrid  Inheritance : << Mixture of 3 or more types of inheritance

"""








"""

**Polymorphism**

Polymorphism means "one Thing, many forms"

Think of a person:
- As a teacher -> Teach
- As a parent -> Take care of Family and kids
- As a friend -> Spend time with Friends

In programming, it means the same function/method name behave differently depending on the object


"""


"""
**Types of Polymorphism:**
- Method overloading
- Method Overriding


"""




"""

**1. Method Overloading:** Multiple functions with same names, different parameters. which one to run depends on how many arguments you are passing

----not present in python-----

Method Overloading is not supported by Python


"""





def sum():
  print("abc")

def sum(a):
  print(a+7)

def sum(a,b):
  print(a+b)

## sum(6) it will give an error due to 
"""
It is wrong logically because the function is being redefined, and the final version requires two parameters.

The problem is that Python does not support function overloading the way some other languages do.
"""





a=5
a=25
a=110
print(a)





# default arguments
def sum(a,b=6):
  print(a+b)

sum(5)   #one argument




def sum():
  print("abc")

def sum(a):
  print(a+7)

def sum(a,b=17):
  print(a+b)

sum(6)