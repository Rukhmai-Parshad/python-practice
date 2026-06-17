# =========================================================
# Conditional Statements = # Conditional statements are used to make decisions in a program.
# They execute different blocks of code based on whether a condition
# is True or False.
# =========================================================
# ---------------------------------------------------------
# Real-life example:

# Agar baarish ho rahi hai:
#     Umbrella le jao
# Warna:
#     Umbrella mat le jao
# ---------------------------------------------------------
#       Comparison Operators

#         ==    Equal To
#         !=    Not Equal To
#         >     Greater Than
#         <     Less Than
#         >=    Greater Than Equal To
#         <=    Less Than Equal To
# ---------------------------------------------------------
# Conditional Statements = Decision Making

# if        -> One condition
# if-else   -> Two possible outcomes
# elif      -> Multiple conditions
# nested if -> if inside another if

# and       -> All conditions must be True
# or        -> At least one condition must be True
# not       -> Reverses the result

# ternary   -> One-line if-else
# ----------------------------------------------------------
# Examples

is_raining = True
if is_raining:
   print("Take umnrella")
else:
   print("No need")   

# if Statement
# Used when you want to execute a block of code
# only if a condition is True.

marks = 85
if marks >= 50:
    print("Pass")   

# if-else Statement
# Used when there are two possible outcomes.
# One block runs if the condition is True,
# and another block runs if the condition is False.

age = 10

if age >=18:
   print("Adulte")
else:
   print("Minor")

# if-elif-else Statement
# Used when multiple conditions need to be checked.
# Python checks conditions from top to bottom.
# Once a condition becomes True, the remaining conditions are skipped.

marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail") 

# Nested if Statement
# A nested if is an if statement inside another if statement.
# It is used when one condition depends on another condition.

age = 22
salary = 40000
if age >= 18:
    if salary >= 30000:
        print("Eligible")

# Logical AND Operator
# Returns True only when all conditions are True.

age = 22
salary = 40000
if age >= 18 and salary >= 30000:
    print("Eligible")

# Logical OR Operator
# Returns True if at least one condition is True.
age = 15
salary = 40000
if age >= 18 or salary >= 30000:
    print("Eligible")

# Logical NOT Operator
# Reverses the result.
# True becomes False and False becomes True.
is_banned = False
if not is_banned:
    print("Access Granted") 

# Ternary Operator
# A short way to write if-else in one line.
age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)

# Truthy and Falsy Values

# These values are treated as False in Python:
# False
# 0
# 0.0
# ""
# []
# ()
# {}
# set()
# None

name = ""
if name:
    print("Data Exists")
else:
    print("Empty")

# =========================================================
# Questions
# =========================================================
# Check whether a number is Positive, Negative, or Zero.
num = -15

if num > 0:
    print("Number is Positive")
elif num == 0:
    print("Number is Zero")
else:
    print("Number is Negative")
    
# Check whether a number is Even or Odd.

num = 27

if num % 2 == 0:
    print("Number is even") 
else:
    print("Number is odd")   

# Find the largest number between two numbers.

a = 45
b = 78      
if a > b:
    print("A is largest")
elif a == b:
    print("A is equal to B")
else:
    print("B is largest")    

# Check whether a person is eligible to vote.
# A person can vote if age is 18 or above.

age = 20

if age >=18:
    print("Eligible to vote")
else:
    print("Not eligible") 

# Check whether a number is divisible by 5.

num = 35
if num % 5 ==0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5") 

# Find the largest among three numbers.

a = 25
b = 67
c = 95

if a > b and a > c:
    print("A is largest")
elif b > a and b > c:
    print("B is largest")
else:
    print("C is largest")        

# Find the smallest among three numbers.

a = 25
b = 67
c = 45    

if a < b and a < c:
    print("A is smallest")
elif b < a and b < c:
    print("B is smallest")
else:
    print("C is smallest")

# Check whether a year is a Leap Year.

year = 2024   
# A leap year is:
# Divisible by 400
# OR divisible by 4 but not by 100

year = 2024

if year % 400 == 0:
    print("Leap Year")

elif year % 4 == 0 and year % 100 != 0:
    print("Leap Year")

else:
    print("Not Leap Year")

# Check whether a number is divisible by both 5 and 7.

num = 70

if num % 5 == 0:
    if num % 7 == 0:
        print("Number is divisible by both 5 and 7")
else:
    print("Not divisible by 5 and 7 or both")

# Check whether a character is a vowel or consonant.

char = "a"    

if char in "aeiou":
    print("Character is a vowel")
else:
    print("Character is a consonant")    


# Create a simple login system.

username = "admin"
password = "1234"

# Print Login Successful or Invalid Credentials

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")    

# Loan Eligibility System
# Conditions:
# Age >= 21
# Salary >= 30000

age = 25
salary = 40000    

if age >= 21 and salary >=30000:
    print("Eligible for loan")
else:
    print("Not eligible")    

# ATM Withdrawal System

balance = 10000
withdraw_amount = 7000

# Print:
# Transaction Successful
# or
# Insufficient Balance   

if withdraw_amount <= balance:
    print("Transaction Successful")
else:
    print("Insufficient Balance") 

# Shopping Discount System
# If amount >= 5000 → 20% discount
# If amount >= 3000 → 10% discount
# Otherwise no discount

amount = 4500

if amount >= 5000:
    print("20% discount")
elif amount >=3000:
    print("10% discount")
else:
    print("No discount")

# Check whether a student passed or failed.
# Pass marks = 40

marks = 55            
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# User can enter exam only if:
# Age >= 18
# AND has Admit Card

age = 20
has_admit_card = True       

if age >= 18 and has_admit_card:
        print("User can enter in exam")
else:
    print("Not enter in exam")        

# A user can apply for a job only if:
# Age >= 21
# Degree Available

age = 23
has_degree = True

if age >= 21:
    if has_degree == True:
        print("User can apply for a job")
else:
    print("Not eligible for job")

# Check whether a person is eligible for marriage.
# Male -> Age >= 21
# Female -> Age >= 18

gender = "female"
age = 19            

if gender == "female":
    if age >= 18:
        print("Eligible for marriage")
    else:
        print("Not eligible")
        
elif gender == "male":
    if age >=21:
        print("Eligible for marriage")    
    else:
        print("Not eligible")  
 
# Calculate Grade
# 90+  -> A
# 75+  -> B
# 60+  -> C
# 40+  -> D
# Below 40 -> Fail

marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C") 
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")               

# Electricity Bill System
# Units <= 100      -> ₹5 per unit
# Units <= 300      -> ₹7 per unit
# Units > 300       -> ₹10 per unit

units = 250
total_bill = 0
# Calculate total bill    
if units <= 100:
    total_bill = units*5
elif units <= 300:
    total_bill = units*7 
elif units > 300:
    total_bill = units*10

print(total_bill)

# Find the largest among four numbers without using max().

a = 10
b = 45
c = 32
d = 78    

if a>b and a>c and a>d :
    print("A is largest")
elif b>a and b>c and b>d :
    print("B is largest")
elif c>a and c>b and c>d :
    print("C is largest")   
else:
    print("D is largest")         

# Check whether a number is a 3-digit number.

num = 456

if 100 <= num <= 999:
    print("3 Digit Number")
else:
    print("Not 3 Digit")

# Check whether a number lies between 100 and 500.

num = 350
if 100 <= num <= 500:
    print("Number lies between 100 and 500")
else:
    print("Outside Range")

# Check whether a person is eligible for a driving license.
# Conditions:
# Age >= 18
# Has valid ID proof

age = 20
has_id = True    
if age >= 18:
    if has_id == True:
        print("Person is eligible for driving licence")
else:
    print("Not eligible")        

# Create a mini calculator using if-elif-else.

num1 = 10
num2 = 5
operator = "+"    

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print("Invalid choice")            
