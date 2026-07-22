"""
## 2 Method Overriding : << Parent and child class has same function name, in this when we call that function, Child function overrides(overrules) the parent function

When we create an object of the child class and call the function, the parent function is got going to run, the child functions is going to run(child function overrides the parent function)

"""

class A:
    def fun(self):
        print("A")
class B(A):
    def fun(self):
        print("B")

obj=B()
obj.fun()


"""
calling a function of parent in child class 

##Super() function => When we want to access something of  parent class in child class,we can use super function

super().function_name()

goes to the parent and search for function


"""


class A:
    def fun(self):
        print("A")

class B(A):
    def fun(self):
        super().fun()
        print("B")

obj=B()
obj.fun()


class A:
    def fun(self):
        print("A")
class B:
    def fun1(self):
        print("B")

class C(A,B):
    def fun1(self):
        super().fun1()

obj=C()
obj.fun1()


class GrandParent:
    def Property(self):
        print("Property in Mumbai")

class Parent(GrandParent):
    def Property(self):
        print("Property in Bengaluru")

class Child(Parent):
    def Property(self):
        #print("Property in Pune")
        super().Property()

obj=Child()
obj.Property()



class Mother:
    def Quality(self):
        print("Nature is Polite")

class Father:
    def Quality(self):
        print("Nature is disciplined")

class Son(Father,Mother):              #Method Resolution Order(MRO)
    def Quality(self):
        return super().Quality()        #First Parent class Quality function will be executed

obj=Son()
obj.Quality()

#Method Resolution Order: it is the order in which Python Search for Method especially in multiple inheritance


class Mother:
  def Quality(self):
    print("Nature is Polite")
    super().Quality()

class Father:
  def Quality(self):
    print("Nature is disciplined")

class Son(Mother,Father):   #Method Resolution Order(MRO)
  def Quality(self):
    super().Quality()   #First Parent class Quality function will be executed with super class

obj=Son()
obj.Quality()




"""

**3. Encapsulation:**

Encapsulation means, putting the data(Properties[variables], Method[functions]) inside a single container to protect from outside sources

**Access Modifiers**

Tell us who can access and change the data and who can't. they are used to the direct access of data

**types of access modifiers:**
1. **Public:** Anyone can Access and modify
2. **Protected:** Access and modidy only inside the child and self
3. **Private:** No one can access and modify, execept the self class(the class, where the data is created)


"""



class Bank_acc:
    def __init__(self,name,acc_no):
        self.Name=name
        self.ACC_no=acc_no
        self.Balance = 0

    def Deposit(self,money):
        self.Balance+=money
        #self.Balance=self.Balance+=money
        print("Deposited",money)

    def withdraw(self,money):
        if money>self.Balance:
            print("Insufficient Balance")
        else:
            self.Balance-=money
            print("Withdrawn",money)

    def check_balance(self):
        print("Balance =",self.Balance)


user=Bank_acc("sufi","55")

user.check_balance()
user.Deposit(50000)
user.check_balance()
user.withdraw(100000)
user.check_balance()


print(user.Balance)
user.Balance =955545648684


user.check_balance()



"""
Protected -> data can be accessed only inside derived and self class

(not implemented properly in python)

variable(public) -----> _variable(protected)

in Python we can access and change the protected data outside the child and parent class as well

Protected in python is used to suggest that this variable is important, please dont try to change it.(although we can, but dont)

"""


class A:   #parent class
  def __init__(self):
    self._var=10  #protected data

class B(A): #child class
  def fun(self):
    self._var+=5    #modifing the protected data (from parent)
    print(self._var)  #accessing the protected data

obj=B()
obj.fun()

obj._var=999999    #99999+5 1000004
obj.fun()



#Practice Question

#Employee Management System
#class - Employee (name, employee_id, Salary, domain)  (constructor)
#class - Manager, developer, Intern
# each child class must have a specific action like creating_meeting(), Writting_codes(), Learning()

# (Employee) -> Manager, developer, intern

# time till 8:50 AM


class Employee:
    def __init__(self,name,employee_id,salary,domain):
        self.Name = name
        self.Employee_id = employee_id
        self.Salary = salary
        self.Domain = domain

class Manager(Employee):
    def whoAmI(self):
        print(self.Name,'has created a new meeting')

    def create_meetings(self):
        print(self.Name,'has created a new meeting')


class Developer(Employee):
    def whoAmI(self):
        print(self.Name,'is a Developer, in domain ',self.Domain)

    def writing_codes(self):
        print(self.Name,'has created a new code and is ready for review')

class Intern(Employee):
    def whoAmI(self):
        print(self.Name,'has finished a course')

    def Learning(self):
        print(self.Name, 'has finished a course')


manager1 = Manager('Manager One', 225, 2050202, 'IT Operations')

manager1.whoAmI()
manager1.create_meetings()

print()

dev1 = Developer('Developer One', 123, 100000, 'IT Dev')
dev1.whoAmI()
dev1.writing_codes()

print()

intern1 = Intern('New Intern One', 'T123', 50000, 'AWS')
intern1.whoAmI()
intern1.Learning()




