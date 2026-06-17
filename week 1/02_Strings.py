# ============================================================================
# Strings = A string is a sequence of characters.
# ============================================================================

# ----------------------------------------------------------------------------
# Most Important Functions
# len()
# upper()
# lower()
# replace()
# split()
# join()
# find()
# count()
# startswith()
# endswith()
# strip()


name = "Cutie"

# Each character has an index.
# text = "Python"

# P  y  t  h  o  n
# 0  1  2  3  4  5

# Negative indexing:

# P  y  t  h  o  n
# -6 -5 -4 -3 -2 -1

# Important Rules
# 1. Strings are Immutable
# Once created, a string cannot be modified.

# name = "Python"
# name[0] = "J"   #Error

# 2. Strings are Ordered
# Characters maintain their position.

text = "Python"
print(text[0])
print(text[3])

# Accessing Characters
text = "Python"

print(text[0])
print(text[1])
print(text[-1])
print(text[-2])

# String Slicing
# string[start:end:step]

#String functions
name = "rukhmai parshad"
print(name[::-1]) #Reverse a string
print(name == name[::-1]) #Palindrome Check
print(len(name)) #Length of string
print(name.upper()) #Converts to uppercase
print(name.lower()) #Converts to lowercase
print(name.title()) # Capitalizes first letter of each word
print(name.capitalize()) # Capitalize only first letter of first word.
print(name.strip()) # removes spaces from both ends
print(name.lstrip()) # Left spaces remove
print(name.rstrip()) #Right spaces remove
print(name.replace("parshad", "prasad")) # Replace string
print(name.split()) # Convert string to list
print(name.find("p")) #Returns index.
print(name.count("a")) #Counts occurrences.
print(name.startswith("ru")) #Starts with
print(name.endswith("ad")) #Ends with
print("Python".isalpha()) # Checks if only letters.
print("123".isdigit()) # Checks if only digits.
print("Python123".isalnum()) # Checks if only letters + numbers.
print("python".islower()) # Checks is string in lowercase.
print("PYTHON".isupper()) # Checks if only letters.
print("Python".isupper()) # Checks if only letters.
print(f"Hello, I'm {name}, a python developer.") #String Formatting

# ===================================================================================
# Questions
# ===================================================================================

# Reverse a string
a = input("Enter a string : ")        
print(a[::-1]) 

# Check palindrome
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Count vowels
text = "python developer"
count = 0
for ch in text:
   if ch.lower() in "aeiou":
      count += 1
print(count)      

# Count Characters
text = "banana"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

# Starts With
text = "Python Developer"
print(text.startswith("Py"))

# Remove Spaces
text = "    Python     "
print(text.strip())

# Join List
fruits = ["apple", "mango", "banana"]
print(",".join(fruits))                   

# Count Words
sentence = "I love python programming"
words = sentence.split()
print(words)
print(len(words))

# Replace a Word
text = "I love Java"
new_text = text.replace("java","python")
print(new_text)

# Remove Spaces from string 

a = input("Enter a String : ")
no = a.replace(" " , "")
print(no)

# f-String
name = "Cutie"
age = 21
print(f"My name is {name} and I am {age} years old")