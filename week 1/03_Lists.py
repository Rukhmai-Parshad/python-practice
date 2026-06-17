# =========================================================================
# List = A list stores multiple values in a single variable.
# =========================================================================

# -------------------------------------------------------------------------

# Functions You Must Remember
# append()
# insert()
# extend()
# remove()
# pop()
# sort()
# reverse()
# count()
# index()
# copy()
# len()
# enumerate()
# -------------------------------------------------------------------------

# Characteristics:
# Ordered 
# Mutable 
# Allows duplicates 
# Can store different data types 
# -------------------------------------------------------------------------

# Example
data = ["Cutie", 21, True, 95.5]

numbers = [10,20,30,40,50]

# Accessing Elements
print(numbers[0])   #First element
print(numbers[-1])  #Last element

# Slicing
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])   #Reverse list

# Length
print(len(numbers))

# Add Elements
numbers.append(60)
print(numbers)

numbers.insert(1,15)
print(numbers)

numbers.extend([70,80])
print(numbers)

# Remove Elements
numbers.remove(20)
print(numbers)

numbers.pop()
print(numbers)

numbers.pop(0)
print(numbers)

# Search
print(numbers.index(40))
print(numbers.count(30))

# Sorting
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# Reverse
numbers.reverse()
print(numbers)

# Copy
new_numbers = numbers.copy()
print(new_numbers)

# Membership
print(30 in numbers)
print(100 not in numbers)

# Concatenation
a = [1,2]
b = [3,4]
print(a+b)

# Repetition
print([1,2] * 3)

# Looping Through Lists
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# ===========================================================
# Questions
# ===========================================================
# Largest Element
nums = [4,8,5,2,9]
largest = nums[0]
for num in nums:
    if num > largest:
        largest = num

print(largest)

# Smallest Element
nums = [4,5,2,7,5]
smallest = nums[0]
for num in nums:
    if num < smallest:
        smallest = num
print(smallest)

# Second Largest 
nums = [10, 20, 30, 40]
first = second = float('-inf')
for num in nums:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print(second)

# Reverse List
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# Count even & odd
nums = [1, 2, 3, 4, 5, 6]
even = 0
odd = 0
for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even)
print("Odd:", odd)

# Remove Duplicates
nums = [1,2,2,3,3,4]
unique = list(set(nums))
print(unique)

# Frequency of Elements
nums = [1, 2, 2, 3, 3, 3]
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1
print(freq)