# ======================================================================================
# Loops = Loops are used to execute a block of code repeatedly.
# Instead of writing the same code multiple times,
# we use loops to automate repetitive tasks.
# ======================================================================================

# Most Important Concepts

# for loop   -> Known number of iterations
# while loop -> Unknown number of iterations
# break      -> Stop loop immediately
# continue   -> Skip current iteration
# pass       -> Do nothing
# range()    -> Generate numbers
# nested loops

# Types of Loops in python

# for loop
# while loop

# for loop = A for loop is used when we know
# how many times we want to repeat a task.

# for variable in sequence:
    # code

# range()
# range(start, stop, step)

# While loop = A while loop runs as long as
# a condition remains True.

# while condition:
    # code

# break Statement = break immediately terminates the loop.

# continue Statement = continue skips the current iteration
# and moves to the next iteration.

# pass statement = pass is a placeholder.
# It does nothing.

# ======================================================================================
# Examples
# ======================================================================================

# for loop
for i in range(1, 11, 2):
    print(i)

# reverse loop  
for i in range(10, 0, -1):
    print(i)

# Looping Through String
name = "Python"
for ch in name:
    print(ch)    

# Looping Through List
nums = [10, 20, 30, 40]
for num in nums:
    print(num)    

# Looping Through Dictionary
student = {
    "name": "Riya",
    "age": 21
}
for key, value in student.items():
    print(key, value)    

# while loop
count = 1
while count <= 5:
    print(count)
    count += 1    

# Infinite Loop -> This never stops. 
# while True:
#     print("Hello")

# break Statement
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# continue statement 
for i in range(1, 6):
    if i == 3:
        continue
    print(i) 

# Loop Else
for i in range(5):
    print(i)
else:
    print("Loop Completed")    

# ======================================================================================
# Questions
# ======================================================================================

# Print numbers from 1 to 10

for i in range(1, 11):
    print(i)

# Print numbers from 10 to 1    
for i in range(10, 0, -1):
    print(i)

# Print all even numbers from 1 to 20 
for i in range(2, 21, 2):
    print(i)

# Print all odd numbers from 1 to 20    
for i in range(1, 20, 2):
    print(i)

# Calculate sum of numbers from 1 to 100
sum = 0
for i in range(0, 101):
    sum = sum + i
print(sum)        

# Print multiplication table of 7
num = 7
for i in range(1,11):
    print(f"{num} X {i} = {num * i}")

# Count vowels in a string  
name = "rukhmai parshad"
count = 0
for ch in name:
    if ch in "aeiou":
        count += 1
print(count)  

# Find the largest number in a list
nums = [10, 20, 30, 40, 50, 60]
largest = nums[0]
for num in nums :
    if num > largest:
        largest = num
print(largest)     

# Print all characters of a string using loop
name = "python"
for ch in name:
    print(ch)

# Print numbers from 1 to 20
# but skip 10 using continue
for i in range(1, 21):
    if i == 10:
        continue
    print(i)    

# Find the sum of all even numbers from 1 to 100.
sum = 0
for i in range(2, 101, 2):
    sum = sum + i
print(sum)     

# Find the sum of all odd numbers from 1 to 100.
sum = 0
for i in range(1, 100, 2):
    sum = sum + i
print(sum)

# Count how many even numbers exist.
nums = [10, 15, 20, 25, 30, 35, 40]
count = 0
for num in nums:
    if num % 2 ==0:
        count += 1
print(count)       

# Count how many odd numbers exist.
nums = [10, 15, 20, 25, 30, 35, 40]
count = 0
for num in nums:
    if num % 2 != 0:
        count += 1
print(count)

# Find smallest element without min().
nums = [45, 12, 78, 3, 89, 22]
smallest = nums[0]
for num in nums:
    if num < smallest:
        smallest = num
print(smallest)

# Reverse a string
name = "python"
for ch in name[::-1]:
    print(ch)    

# Count total digits
nums = 123456

# Sum of digit
num = 1234


# Find Maximum Without max()
# Find largest element.
nums = [45, 78, 12, 98, 32]
largest = nums[0]
for num in nums:
    if num > largest:
        largest = num
print(largest)

# Print Found if target exists.
# Otherwise print Not Found.
nums = [10, 20, 30, 40, 50]
target = 30

found = False
for num in nums:
    if num == target:
        found = True

if found:
    print("Found")
else:
    print("Not found")            

# Find factorial of 5
# 5! = 5*4*3*2*1

num = 5
fact = 1
for i in range(1, num+1):
    fact = fact * i 
print(fact)    

# Print tables from 1 to 10.
for i in range(1,11): 
   for num in range(1,11):     
      print(f"{num} X {i} = {num * i}")

# Check whether number is Prime or Not Prime.
num = 13
for i in range(2,num):
    if (num%i)==0:
        print("Number is not prime")
        break
else:
    print("Number is prime")

# Print first 10 Fibonacci numbers.
# 0 1 1 2 3 5 8 ...    
num = 10
a = 0
b = 1
c = 0
while(c <=num):
    print(c)
    a = b 
    b = c
    c = a + b
    