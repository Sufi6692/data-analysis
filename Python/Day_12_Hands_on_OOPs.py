# Question 1
# authentication system
# class = User
# initialize data= username, password

# login function = password== input user gave

# loop until the password is correct





class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f"Welcome, {self.username}! Please log in.")
        while True:
            entered_password = input("Enter your password: ")

            if entered_password == self.password:
                print("Access granted! Login successful.")
                break
            else:
                print("Password is not correct. Please try again.")

my_user = User("PythonDev", "SuperSecret123")
my_user.login()





# Question 2
# same thing as question 1
# but adding one thing while creating a username and password
# when user enters the password check if the password includes
# - Atleast 1 uppercase
# - Atleast 1 lowercase
# - Should be in range of 8-20 length
# - atleat include 1 number

# if any condition didnt match, provide a message "Password is not secure" input the password again


class User:
  def __init__(self, username):
        self.username = username
        self.password = self.create_password()

  def create_password(self):
        while True:
            password = input("Create Password: ")
            if (len(password) >= 8 and len(password) <= 20 and
                any(ch.isupper() for ch in password) and
                any(ch.islower() for ch in password) and
                any(ch.isdigit() for ch in password)):
                print("Password created successfully!")
                return password
            else:
                print("Password is not secure. Enter the password again.")

  def login(self):
      while True:
          entered_password = input("Enter Password: ")
          if entered_password == self.password:
            print("Login Successful!")
            break
          else:
            print("Incorrect Password! Try Again.")

username = input("Enter Username: ")
user = User(username)
print("\nLogin")
user.login()


# Question 3
# Online Shopping Cart
# class = ShoppingCart
# initiize these data= userid,items=[]

# (for each item take user input)
# method:
# add_item: you will add the item in your cart
# Remove_item: you will delete the item from your cart
# checkin_item: you will iterate each item in cart one by one to complete the scan





class shopping_Cart:
  def __init__(self,userid,items=[]):
    self.userid = userid
    self.items = items

  def add_item(self,item):
    self.items.append(item)
    print(f"{item} has been added to your cart")
  
  def remove_item(self,item):
    if(item in self.items):
      self.items.remove(item)
      print(f"{item} has been removed from your cart")
    else:
      print(f"{item} has been not found in your item list")
      
  def checkin_item(self):
    for item in self.items:
      print(f"{item} has been Scanned")
    print(f"End of items in cart,Total items are {len(self.items)}")

cart1 = shopping_Cart(1234,["Milk","Curd","Chicken","Panner"])
cart1.checkin_item()
cart1.add_item("Sugar")
cart1.checkin_item()
cart1.add_item("Cheese")
cart1.remove_item("headphones")
cart1.remove_item("Curd")
cart1.checkin_item()


a=5
b=10
# a=5, b=10
print("a=",a,", b=",b)
print(f"a= {a}, b= {b}")



# #Notification System

# parent class = Notification(property=[message(string),towhom(string)],method=send())

# child classes = SMS, Email, Messager (method=send())

# inside send()
# print this
# SMS send to {towho}
# mesage



class Notification:

    def __init__(self, towhom, message):
        self.towhom = towhom
        self.message = message

    def send(self):
        print(f"Sending generic notification to {self.towhom}")
        print(self.message)


class SMS(Notification):
    def send(self):
        print(f"SMS sent to {self.towhom}")
        print(self.message)
        print("-" * 30)

class Email(Notification):
    def send(self):
        print(f"Email sent to {self.towhom}")
        print(self.message)
        print("-" * 30)

class Messenger(Notification):
    def send(self):
        print(f"Messenger sent to {self.towhom}")
        print(self.message)
        print("-" * 30)

customer_alert = SMS("Akshay", "Your delivery will arrive today between 2 PM and 4 PM.")

report_alert = Email("Renu", "The daily SQL data extraction has completed successfully.")

chat_alert = Messenger("Mumtaz", "Hey! The server is back online, we can resume testing.")


customer_alert.send()
report_alert.send()
chat_alert.send()






# Movie Booking System
# abstract class => BookingSystem

# BookingSystem(property=[MovieName,Seats,SeatCategory], abstractmethod="TicketBill()")

# child class => PVR, cinepolis, INOX
# Seat Category=> silver, gold, platinum

# PVR = silver(399), gold(499), platinum(599)
# Cinepolis = silver(149), gold(199), platinum(299)
# Inox = silver{299}, gold(349), platinum(499)

# ticketbill()
# -----------------
# name= movie_name
# Seat= total_seats
# Type= Seat_Category
# Total_bill = Total_seats*Seat_category

# time till 9:00 AM









from abc import ABC,abstractmethod
class Movie_Booking(ABC):
  def __init__(self,moviename,Seats,SeatCategory):
    self.movie_name = moviename
    self.seats = Seats
    self.seatCategory = SeatCategory

  @abstractmethod
  def TicketBill(self):
    pass


class PVR(Movie_Booking):
  def TicketBill(self):
    if self.seatCategory == 'silver':
      print(self.movie_name, "total bill amount is ", self.seats * 399)
    elif self.seatCategory == 'gold':
      print(self.movie_name,"total bill amount is ", self.seats * 499)
    else:
      print(self.movie_name,"total bill amount is ", self.seats * 599)


class Cinepolis(Movie_Booking):
  def TicketBill(self):
    if self.seatCategory == 'silver':
      print(self.movie_name, "total bill amount is ", self.seats * 149)
    elif self.seatCategory == 'gold':
      print(self.movie_name,"total bill amount is ", self.seats * 199)
    else:
      print(self.movie_name,"total bill amount is ", self.seats * 299)


class INOX(Movie_Booking):
  def TicketBill(self):
    if self.seatCategory == 'silver':
      print(self.movie_name, "total bill amount is ", self.seats * 299)
    elif self.seatCategory == 'gold':
      print(self.movie_name,"total bill amount is ", self.seats * 349)
    else:
      print(self.movie_name,"total bill amount is ", self.seats * 499)

obj = PVR('avengers',5,'silver')
obj.TicketBill()
obj = Cinepolis('avengers',5,'gold')
obj.TicketBill()
obj = INOX('avengers',5,'platinum')
obj.TicketBill()






