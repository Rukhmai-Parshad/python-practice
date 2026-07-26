# =================================================================================
# VARIABLE = Variable is a container that stores data.
# =================================================================================

# RULES:
# Cannot start with a number
# Cannot contain special characters (@ # $ %)
# Cannot use Python keywords

# ==================================================================================
# Example
# ==================================================================================

name = "Rukhmai"
age = 20
city = "Karnal"
is_student = True

# Python is a dynamically typed language.
x = 10
print(type(x))

x = "Hello"
print(type(x))

# Multiple Assignment.
a,b,c = 10, 20, 30
print(a)
print(b)
print(c)

# Swapping Variables
a = 10 
b = 20
a, b = b, a
print(a)
print(b)

# The type() Function
name = "Rukhmai"
print(type(name))

# ====================================================================================
# PYTHON DATA TYPES = There are two main categories.
# ====================================================================================

# Immutable Data Types

# The value cannot be changed after creation.
# int
# float
# bool
# str
# tuple

# Mutable Data Types

# The value can be modified after creation.
# list
# set
# dict

# =====================================================================================
# Example
# =====================================================================================

# Integer (int)
age = 20
marks = -50

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# Float
price = 98.90
height = 5.2
print(type(price))

# Complex Numbers
# x = 2 + 3i
# print(type(x))

# String (str)
name = "Rukhmai"
city = "Karnal"

# Access Characters
name = "Python"
print(name[0])
print(name[1])

# String Slicing
text = "Python"
print(text[0:3])
print(text[:4])
print(text[1:])

# Negative Indexing
text = "Python"
print(text[-1])

# Boolean (bool)
# Only two possible values
is_student = True
is_married = False

# Type Conversion
# Implicit Conversion
# Python performs it automatically.
a = 10
b = 2.5
c = a + b
print(type(c))

# Explicit Conversion
# Done manually by the programmer.
age = "21"
age = int(age)
print(type(age))

# Important Conversions
int("10")
float("10")
str(10)
bool(1)
bool(0)

# User Input
name = input("Enter Name: ")
print(name)

# input() always returns a string.
age = input("Enter age: ")
print(type(age))
age = int(input("Enter age: "))

# None Type
# Python's equivalent of a null value.
x = None
print(type(x))

# Identity vs Equality
# A very important interview concept.
# == compares values.
# is compares memory locations (object identity).
a = [1, 2, 3]
b = [1, 2, 3]
# Equality:
print(a == b)
# Identity:
print(a is b)

# =================================================================================
# Questions
# =================================================================================

x = "10"
y = 5
print(x + y) #A string and an integer cannot be added together.

#Store the Student's name, age and gpa and print them with Data Type.

name = input("Enter user name: ") #String
age = int(input("Enter user age: ")) #Integer
gpa= float(input("Enter your gps: ")) #Float
is_student = True #Booleans

print(f"User name : {name}", type(name))
print(f"Age : {age}", type(age))
print(f"GPA : {gpa}", type(gpa))
print(type(is_student))

# Calculate the sum, subtraction, multiplication, division of two numbers.

a = int(input("Enter number 1 :"))
b = int(input("Enter number 2 :"))

print("Sum of two numbers is :", a+b)
print("Subtraction of two numbers is :", a-b)
print("Multiplication of two numbers is :", a*b)
print("Division of two numbers is :", a/b)

#Convert celsius into Fahrenheit.

# Store your weight in a variable and print its type.

weight = int(input("Enter your weight : "))

print(type(weight))

# Take the user's number input and convert it to an integer.

a = input("Enter user's number : ")

b = int(a)
print(type(b))

# Take the total marks and obtained marks from the user and calculate the percentage.

total_marks = int(input("Enter total marks :"))
Obtained_marks = int(input("Enter obtained marks :"))

percentage = (Obtained_marks/total_marks)*100
print(f"Percentage is :{percentage}")

#Swap two variables without third variable.
x = 10
y = 40
x, y = y, x
print(f"x : {x} , y : {y}")

# Make a simple interest calculator.
p = int(input("Enter p :"))
r = int(input("Enter r :"))
t = int(input("Enter t :"))

SI = (p*r*t)/100
print("Simple interest :", SI)    