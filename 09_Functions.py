# ======================================================================================
# Functions = # A function is a reusable block of code
# that performs a specific task.
#
# Instead of writing the same code again and again,
# we can write it once inside a function and call it whenever needed.
# ======================================================================================

# Benefits of Functions

# Code Reusability
# Better Readability
# Easier Debugging
# Easier Maintenance
# Less Code Repetition

# Quick Revision

# def      -> Create Function
# call     -> Execute Function
# parameter -> Variable in function definition
# argument  -> Value passed during function call
# return    -> Send value back
# local     -> Inside function
# global    -> Outside function
# *args     -> Multiple positional arguments
# **kwargs  -> Multiple keyword arguments

# Syntax
# def function_name():
#     # code
# function_name()     

# Function with Parameters

# Parameters are variables that receive values
# when a function is called. 

# ======================================================================================
# Examples
# ======================================================================================

# Single Parameters
def greet(name):
   print("Hello", name)

greet("Rukhmai")
greet("Pardeep")  

# Multiple Parameters
def add(a, b):
    print(a + b)

add(10, 20)
add(70, 30)


# Return Statement
# return sends a value back to the caller.

def add(a, b):
    return a + b
result = add(10, 20)
print(result)

# Default parameters

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Rukhmai")    

# Keyword Arguments
def student(name, age):
    print(name, age)
student(age=21, name="Riya")

# Arbitrary Arguments (*args)
# Allows multiple positional arguments.
def total(*nums):
    print(sum(nums))
total(10, 20, 30)

# Keyword Arbitrary Arguments (**kwargs)
# Allows multiple keyword arguments.
def student(**data):
    print(data)
student(name="Riya", age=21)

# Variable Scope
# Local Variable
def test():
    x = 10
    print(x)
test()
# x exists only inside function.

# Global Variable
x = 100
def test():
    print(x)
test()

# ======================================================================================
# Questions
# ======================================================================================

# Create a function that prints "Hello World".
def greet(name):
    print("Hello",name)

greet("world")  # Without return ststement

def greet(name):
    return name
result = greet("Hello World")
print(result)  #With return statement

# Create a function that takes a name
# and prints a greeting message.
def greet(name):
    print("Hello",name)

greet("Rukhmai") 
greet("Pardeep")

# Create a function that returns
# the sum of two numbers.
def add(a , b):
    return (a + b)

result = add(10, 30)
print(result)

# Create a function that returns
# the square of a number.
def square(a):
    return a * a

result = square(9)
print(result)

# Create a function that checks
# whether a number is even or odd.
def check(num):
    if num%2 == 0:
        print("Number is even")
      #   return("Number is even")
    else:
        print("Number is odd")    
      #   return("Number is odd")    
# result= check(7)    
# print(result)   
check(7) 
check(8)          

# Create a function that finds
# the largest of two numbers.

def big(a, b):
    if (a>b):
      #   print("A is largest")
        return("A is largest")
    else:
      #   print("B is largest")    
        return("B is largest")    

result = big(60,50)
print(result)
# big(30,80) 
# big(40,10)       

# Create a function that counts vowels in a string.

def check(name):
    count = 0
    for ch in name:
        if ch in "aeiou":
            count += 1
   #  print(count)
    return count

# check("rukhmai parshad")
result = check("Pardeep rana")
print(result)

# Create a function that returns the factorial of a number.
def fact(n):
    num = 1
    for i in range(1, n+1):
        num = i * num
    return num
result = fact(3)
print(result)    

# Create a function that returns the largest element in a list.

def big():
    L = [23, 4, 56, 65, 87, 56, 12, 98]
    largest = L[0]
    for ch in L:
        if ch > largest:
            largest = ch
    print(largest)

big()    

# Create a function that checks whether a string is a palindrome.
def check(str):
    if str == str[::-1]:
        print("String is a palindrome")
    else:
        print("String is not a palindrome")    
             
check("madam")    
check("palindrome")    

# Create a function that returns the sum of all numbers in a list.
nums = [10, 20, 30, 40]
def sum():
    sum = 0
    for num in nums:
        sum = sum + num
    return sum
result = sum()
print(result)    

# Create a function that returns  the smallest element in a list.
def find():
    S = [23, 4, 56, 65, 87, 56, 12, 98]
    smallest = S[0]
    for i in S:
        if i < smallest:
            smallest = i
    print(smallest)

find()

# Create a function that returns the count of vowels in a string.
def count():
    char = "rukhmai parshad"
    vowels = 0
    for ch in char:
        if ch in "aeiou":
            vowels += 1
    print(vowels)
count()            

# Create a function that checks whether a number is prime.
def prime(nums):
    for i in range(2, nums):
        if (nums%i) == 0:
            print("Not a prime")
            break
    else:
        print("Prime")    
prime(12)
prime(13)

# Create a function that returns the reverse of a string.
def reverse(char):
    print(char[::-1])

reverse("python")    

# Create a function that returns the frequency of each character.
def char_frequency(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq
print(char_frequency("banana"))

# ======================================================================================
# lambda(), map(), filter(), shorted()
# ======================================================================================

# --------------------------------------------------------------------------------------

# Lambda = # A lambda function is a small anonymous function.
# Anonymous means it has no name.
# It is generally used for short operations.

# Syntax
# lambda parameters: expression

# -------------------------------------------------------------------------------------

# map() = map() applies a function
# to every element of an iterable.

# map() Memory Trick
# map()
# Take every element
# ↓
# Apply function
# ↓
# Return new values

# -------------------------------------------------------------------------------------

# filter() = filter() keeps only those elements for which the condition is True.

# filter() Memory Trick
# filter()
# Check condition
# ↓
# Keep True values
# ↓
# Remove False values

# -------------------------------------------------------------------------------------

# sorted() = sorted() is used to sort elements of an iterable
# and returns a new sorted list.
# By default it sorts in ascending order.
# It can also sort using custom rules with key=.

# sorted() Memory Trick
# Data
#   ↓
# Sort
#   ↓
# Return New List

# Syntax

# sorted(iterable)
# sorted(iterable, reverse=True)
# sorted(iterable, key=function)

# -------------------------------------------------------------------------------------

# Quick Revision

# lambda() -> Anonymous Function
# map() -> Transform Data
# filter() -> Filter Data
# sorted(key=...) -> Custom Sortin

# --------------------------------------------------------------------------------------

# ======================================================================================
# Examples = Lambda(), Map(), filter(), shorted()
# ======================================================================================

# Lambda()
Square = lambda num: num * num
print(Square(3))

is_even = lambda num: num % 2 ==0
print(is_even(10))
print(is_even(7))

# Lambda with condition
check = lambda num: "Even" if num % 2 == 0 else "Odd"
print(check(10))

# map()
nums = [1, 2, 3, 4]
result = list(map(lambda x: x * x, nums))
print(result)

# filter()
nums = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)

# shorted()
names = ["python", "ai", "developer", "code"]
result = sorted(names, key=lambda x: len(x))
print(result)

# ======================================================================================
# Questions = Lambda(), Map(), filter(), shorted()
# ======================================================================================

# Create a lambda function to find square of a number.
square = lambda x: x * x
print(square(3))

# Create a lambda function to add two numbers.
add = lambda a, b: a + b
print(add(20, 30))

# Use map() to double all numbers.
nums = [1, 2, 3, 4, 5]
double = list(map(lambda x: x+x , nums))
print(double)

# Use map() to convert numbers into squares.
nums = [1, 2, 3, 4]
square = list(map(lambda x: x * x, nums))
print(square)

# Use filter() to get even numbers.
nums = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)

# Use filter() to get odd numbers.
nums = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 != 0, nums))
print(result)

# Sort strings according to their length.
names = ["python", "ai", "developer", "code"]
result = sorted(names, key=lambda x: len(x))
print(result)