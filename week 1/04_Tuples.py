# ==========================================================
# Tuples = Tuple is an ordered, immutable collection of items.
# ==========================================================
# ----------------------------------------------------------
# Common Functions
# len()
# count()
# index()
# max()
# min()
# sum()
# tuple()
# list()
# ----------------------------------------------------------

# Why Use Tuple?

# Ordered
# Immutable 
# Allows duplicates 
# Faster than lists 
# Store different data types 
# Safer
# ----------------------------------------------------------

# Example

# Single Element Tuple
t1 = (10,)
print(type(t1))
# Not a Tuple
t2 = (10)
print(type(t2))

person = ("Rukhmai", 21, "Python")

# Accessing
print(person[0])     #First element
print(person[-1])    #Last element

# Slicing
print(person[1:2])
print(person[:2])
print(person[1:])
print(person[::-1])   #reverse tuple

# Length
print(len(person))

# count
nums =(1, 2, 2, 2, 3)
print(nums.count(2))

# Index
print(nums.index(3))

# Membership
print(2 in nums)
print(10 not in nums)

# Looping
for item in person:
   print(item)

# Tuple unpacking
name, age, skill = person

print(name)
print(age)
print(skill)

#  Swapping
a = 10
b = 20
a,b = b,a
print(a,b)

# Tuple -> List
nums = (1,2,3)
print(list(nums))

# List -> Tuple
nums = [1, 2, 3]
print(tuple(nums))

# ===============================================================
# Questions
# ===============================================================

# Print first and last element
t = (10, 20, 30, 40, 50)
print(t[0])
print(t[-1])

# Reverse Tuple
t = (1, 2, 3, 4)
print(t[::-1])

# Maximum Element
t = (10, 50, 20, 90)
print(max(t))

# Minimum Element
t = (10, 50, 20, 90)
print(min(t))

# Sum of Tuple
t = (10, 20, 30)
print(sum(t))