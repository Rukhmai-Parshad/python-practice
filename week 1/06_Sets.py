# ============================================================
# Set = Set is an unordered collection of unique element.
# ============================================================
# ------------------------------------------------------------
# Functions to Remember

# add()
# update()
# remove()
# discard()
# pop()
# clear()
# copy()
# len()
# set()
# ------------------------------------------------------------
# Why Use Set?

# Unordered 
# Mutable 
# Not allow Duplicate values 
# Fast searching 
# ------------------------------------------------------------

# Examples

nums ={10, 20, 30, 40}

# Length
print(len(nums))

# Add element
nums.add(50)
print(nums)

# Update multiple element
nums.update([60, 70])
print(nums)

# Remove element
nums.remove(10)
print(nums)

# Discard element
nums.discard(20)
print(nums)

# Pop random element
nums.pop()
print(nums)

# Copy
new_nums = nums.copy()
print(new_nums)

# Clean 
temp = {1, 2, 3, 4}
temp.clear()
print(temp)

# Empty Set

s = {}
print(type(s))    #<class 'dict'>

s = set()

print(type(s))     #<class 'set'>

# Looping
nums = {10, 20, 30}

for num in nums:
   print(num)

# Membership
nums = {10, 20, 30}

print(20 in nums)
print(100 not in nums)

# ===========================================================
# Questions
# ===========================================================

# Find Union, Find Intersection, Find Difference, Symmetric Difference
a = {1, 2, 3}
b = {3, 4, 5}

print(a|b)
print(a & b)
print(a - b)
print(a ^ b)

# Remove Duplicates
nums = [1, 2, 2, 3, 3, 4]
result = list(set(nums))
print(result)

# Unique Words
sentence = "python is easy and python is powerful"
words = sentence.split()
result = set(words)

print(result)