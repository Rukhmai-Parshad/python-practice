# =======================================================================================
# What is OOP?
# =======================================================================================

# OOP (Object-Oriented Programming) is a programming paradigm
# that organizes code using Classes and Objects.
#
# It helps make code reusable, maintainable,
# secure, and scalable.

# ---------------------------------------------------------------------------------------
# What is a Class?
# ---------------------------------------------------------------------------------------

# A Class is a blueprint or template used to create objects.
#
# It defines attributes (data)
# and methods (behavior) that objects will have.
#
# Example:
#
# class Student:
#     pass

# ---------------------------------------------------------------------------------------
# What is an Object?
# ---------------------------------------------------------------------------------------

# An Object is an instance of a class.
#
# It contains actual data and can access
# methods defined in the class.
#
# Example:
#
# s1 = Student()

# ---------------------------------------------------------------------------------------
# Difference Between Class and Object
# ---------------------------------------------------------------------------------------

# Class:
# Blueprint or template.
#
# Object:
# Real instance created from a class.
#
# Example:
#
# Class -> Car
#
# Objects ->
# BMW
# Audi
# Tesla

# ---------------------------------------------------------------------------------------
# What is self?
# ---------------------------------------------------------------------------------------

# self refers to the current object.
#
# It is used to access object attributes
# and methods inside a class.
#
# Example:
#
# self.name
# self.salary

# ---------------------------------------------------------------------------------------
# What is __init__()?
# ---------------------------------------------------------------------------------------

# __init__() is a constructor.
#
# It executes automatically when an object is created.
#
# It is used to initialize object attributes.
#
# Example:
#
# def __init__(self, name):
#     self.name = name

# ---------------------------------------------------------------------------------------
# What is a Constructor?
# ---------------------------------------------------------------------------------------
# A Constructor is a special method
# that executes automatically when
# an object is created.
#
# In Python:
#
# __init__()

# ---------------------------------------------------------------------------------------
# What are Attributes?
# ---------------------------------------------------------------------------------------

# Attributes are variables inside a class.
#
# They store information about an object.
#
# Example:
#
# self.name
# self.age

# ---------------------------------------------------------------------------------------
# What are Methods?
# ---------------------------------------------------------------------------------------

# Methods are functions defined inside a class.
#
# They describe the behavior of an object.
#
# Example:
#
# greet()
# deposit()
# withdraw()

# ---------------------------------------------------------------------------------------
# What is Inheritance?
# ---------------------------------------------------------------------------------------

# Inheritance allows a child class
# to acquire properties and methods
# of a parent class.
#
# It promotes code reusability.
#
# Example:
#
# Vehicle -> Car

# ---------------------------------------------------------------------------------------
# Benefits of Inheritance
# ---------------------------------------------------------------------------------------

# 1. Code Reusability
# 2. Reduced Redundancy
# 3. Easy Maintenance
# 4. Better Organization

# ---------------------------------------------------------------------------------------
# Types of Inheritance
# ---------------------------------------------------------------------------------------

# 1. Single Inheritance
#
# A -> B

# 2. Multilevel Inheritance
#
# A -> B -> C

# 3. Multiple Inheritance
#
# A
#  \
#   \
#    C
#   /
#  /
# B

# 4. Hierarchical Inheritance
#
#      A
#     / \
#    B   C

# ---------------------------------------------------------------------------------------
# What is super()?
# ---------------------------------------------------------------------------------------

# super() is used to access
# parent class methods and constructors.
#
# Example:
#
# super().__init__(name)

# ---------------------------------------------------------------------------------------
# What is Polymorphism?
# ---------------------------------------------------------------------------------------

# Polymorphism means
# "One Interface, Multiple Forms".
#
# The same method name can perform
# different actions in different classes.
#
# Example:
#
# Dog.sound()
# Cat.sound()

# ---------------------------------------------------------------------------------------
# What is Method Overriding?
# ---------------------------------------------------------------------------------------

# Method Overriding occurs when
# a child class provides its own
# implementation of a parent class method.
#
# Example:
#
# Parent -> sound()
#
# Child -> sound()
#
# Child version replaces parent version.

# ---------------------------------------------------------------------------------------
# What is Encapsulation?
# ---------------------------------------------------------------------------------------

# Encapsulation means wrapping
# data and methods into a single unit (Class)
# and restricting direct access to data.
#
# It provides data security.

# ---------------------------------------------------------------------------------------
# What is a Private Variable?
# ---------------------------------------------------------------------------------------

# A private variable starts with
# double underscore (__).
#
# It cannot be accessed directly
# outside the class.
#
# Example:
#
# self.__balance

# ---------------------------------------------------------------------------------------
# Why Use Private Variables?
# ---------------------------------------------------------------------------------------

# To protect sensitive data.
#
# Example:
#
# Bank Balance
# Password
# Salary

# ---------------------------------------------------------------------------------------
# What is a Getter Method?
# ---------------------------------------------------------------------------------------
# A Getter Method is used
# to access private variables safely.
#
# Example:
#
# get_balance()

# ---------------------------------------------------------------------------------------
# What is a Setter Method?
# ---------------------------------------------------------------------------------------

# A Setter Method is used
# to modify private variables safely.
#
# Example:
#
# set_balance()

# ---------------------------------------------------------------------------------------
# What is an Instance Variable?
# ---------------------------------------------------------------------------------------

# Instance Variables belong
# to individual objects.
#
# Each object can have different values.
#
# Example:
#
# self.name
# self.age

# ---------------------------------------------------------------------------------------
# What is a Class Variable?
# ---------------------------------------------------------------------------------------

# Class Variables belong to the class itself.
#
# They are shared by all objects.
#
# Example:
#
# class Student:
#     school = "ABC School"

# ---------------------------------------------------------------------------------------
# Difference Between Instance Variable and Class Variable
# ---------------------------------------------------------------------------------------

# Instance Variable:
#
# Different value for each object.
#
# Example:
#
# self.name

# Class Variable:
#
# Same value shared by all objects.
#
# Example:
#
# school = "ABC School"

# ---------------------------------------------------------------------------------------
# What are Magic Methods (Dunder Methods)?
# ---------------------------------------------------------------------------------------

# Magic Methods are special methods
# that start and end with double underscores.
#
# Examples:
#
# __init__()
# __str__()
# __len__()
# __add__()

# ---------------------------------------------------------------------------------------
# What is __str__()?
# ---------------------------------------------------------------------------------------

# __str__() controls what gets printed
# when an object is displayed.
#
# Example:
#
# print(obj)

# ---------------------------------------------------------------------------------------
# What are the Four Pillars of OOP?
# ---------------------------------------------------------------------------------------

# 1. Encapsulation
# 2. Inheritance
# 3. Polymorphism
# 4. Abstraction

# ---------------------------------------------------------------------------------------
# What is Abstraction?
# ---------------------------------------------------------------------------------------

# Abstraction means hiding
# implementation details
# and showing only essential features.
#
# Example:
#
# We drive a car without knowing
# how the engine works internally.

# ---------------------------------------------------------------------------------------
# Advantages of OOP
# ---------------------------------------------------------------------------------------

# 1. Reusability
# 2. Scalability
# 3. Security
# 4. Easy Maintenance
# 5. Better Code Organization

# ---------------------------------------------------------------------------------------
# Importent Questions
# ---------------------------------------------------------------------------------------

# What is OOP?
# What is a Class?
# What is an Object?
# What is self?
# What is __init__()?
# What is Inheritance?
# What is super()?
# What is Polymorphism?
# What is Method Overriding?
# What is Encapsulation?
# What is a Private Variable?
# What are Getter and Setter Methods?
# What is Abstraction?
# What are the Four Pillars of OOP?
# Difference Between Class and Object?
# Difference Between Instance and Class Variables?

# =====================================================================================
# QUESTIONS
# =====================================================================================

# Q1 Create Student Class
# class Student
# Attributes:
# name
# age
# Method:
# display()
# greet()

class Student:
   def __init__(self, name, age):
      self.name = name
      self.age = age  

   def display(self):  
       print(f"Name: {self.name}")
       print(f"Age: {self.age}")

   def greet(self):
      print("Hello", self.name)   

s1 = Student("Rukhmai", 21) 
s1.display()
s1.greet()

# Q2 Employee Class
# class Employee
# name
# salary
# show_details()

     
class Employee:
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary

   def increment_salary(self, amount):
      self.salary += amount
  
   def show_details(self):
      print("Name: ", self.name)
      print("Salary: ", self.salary)

emp1 = Employee("Rukhmai", 50000) 
emp1.increment_salary(5000)
emp1.show_details()   

# Q3 Rectangle Area
# class Rectangle
# length
# width 
# area()

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Area of Rectangle = {self.length * self.width}")

A1 = Rectangle(5, 10)
A1.area()

# Q4 Circle Class
# class Circle
# radius
# area()
# circumference()

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pie = 3.14

    def area(self):
        print(f"Area of Circle = {self.pie * self.radius * self.radius}") 

    def circumference(self):    
        print(f"Circumference = {2 * self.pie * self.radius}") 

c1 = Circle(5)
c1.area()
c1.circumference()

# Q5 Bank Account 
# Private balance
# deposit()
# withdraw()
# get_balance()  

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private Variable

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient Balance")


# Object Creation
account = BankAccount(1000)

# Check Initial Balance
print("Current Balance:", account.get_balance())

# Deposit Money
account.deposit(500)
print("Current Balance:", account.get_balance())

# Withdraw Money
account.withdraw(200)
print("Current Balance:", account.get_balance())

# Insufficient Balance Example
account.withdraw(2000)
print("Current Balance:", account.get_balance())

# Q6 Inheritance Question 
# Parent:
# Vehicle
# start_engine()

# Child:
# Car
# drive()

class Vehicle:
   def start_engine(self):
      print("Engine Started")

class Car(Vehicle):
   def drive(self):
      print("Car is Driving")      

car = Car()
car.start_engine()
car.drive()

# Q7 Person → Employee
# Use : super()

class Person:
   def __init__(self, name):
      self.name = name

class Employee(Person):
   def __init__(self, name, salary):
      super().__init__(name)
      self.salary = salary

   def show_details(self):
       print(f"Name: {self.name}")
       print(f"Salary: {self.salary}")

emp = Employee("Rukhmai", 500000)
emp.show_details()

# Q8 Method Overriding 
# Parent:
# Animal
# sound()
  
# Child:
# Dog
# sound()

class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

dog = Dog()
dog.sound()      

# Q9 Library Book System
# class Book
# title
# author
# display_book()

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book(self):
        print(f"Book title: {self.title}") 
        print(f"Author: {self.author}")   

book = Book("Gunahon ka Devta", "Dharamveer Bharti")        
book.display_book()

# Q10 Student Grade System
# class Student
# marks
# calculate_grade()

class Student:
    def __init__(self, marks):
        self.marks = marks

    def claculate_grade(self):
        if self.marks >= 90:
            print("Grade A")
        elif self.marks >= 75:
            print("Grade B")
        elif self.marks >= 60:
            print("Grade C")
        elif self.marks >= 40:
            print("Grade D") 
        else:
            print("Fail")                    

s1 = Student(89)
s1.claculate_grade()    

# Q11 ATM System
# class ATM
# __balance
# deposit()
# withdraw()
# check_balance()

class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposite(self, amount):
        self.__balance += amount

    def transfer(self, other_account, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            other_account.deposite(amount)    

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance") 

    def check_balance(self):
        print(f"Balance: {self.__balance}")

atm = ATM(20000)
atm1 = ATM(2000)
atm.transfer(atm1, 2000)
atm.deposite(5000)
atm.withdraw(3000)
atm.check_balance()
print(atm.check_balance())
print(atm1.check_balance())

# Q12 Shopping Cart
# class ShoppingCart
# add_item()
# remove_item()
# show_cart()

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def show_cart(self):
        print(self.items)

cart = ShoppingCart()
cart.add_item("Laptop")
cart.add_item("Mouse")
cart.show_cart()
cart.remove_item("Mouse")
cart.show_cart()

# Q13 Movie Ticket Booking
# class MovieTicket
# book_ticket()
# cancel_ticket()
# show_available_seats()

class MovieTicket:
    def __init__(self, seats):
        self.seats = seats

    def book_ticket(self):
        if self.seats > 0:
            self.seats -= 1
            print("Ticket Booked!")
        else:
            print("House Full!")    

    def cancle_ticket(self):
        self.seats += 1 
        print("Ticket cancle successfully!")   

    def show_available_seats(self):
        print("Available Seats", self.seats)

movie = MovieTicket(5)
movie.book_ticket()
movie.cancle_ticket()
movie.show_available_seats()
                