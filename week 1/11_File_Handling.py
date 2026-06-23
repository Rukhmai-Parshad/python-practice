# =============================================================
# File Handling = # File handling allows us to:
#
# Read data from files
# Write data to files
# Update files
# Store data permanently
# ==========================================================
# ----------------------------------------------------------
# Most Important Concepts

# open()
# read()
# readline()
# readlines()
# write()
# append()
# with open()
# file modes

"r"   # Read
# File must exist
# FileNotFoundError if missing

"w"   # Write
# Creates file if not exists
# Deletes old content

"a"   # Append
# Creates file if not exists
# Adds data at end

"r+"  # Read + Write
# File must exist
# Does not delete content
# ------------------------------------------------------------

# Opening and read a file 
# file = open("week 1\\data.txt","r")
# print(file.read())
# file.close()

# Read line by line
# file = open("week 1\\data.txt", "r")

# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()

# Write file = "w" mode deletes old content and writes new content.

# file = open("week 1\\data.txt", "w")
# file.write("Hello python")
# file.close

# Append file
# file = open("week 1\\data.txt", "a")
# file.write("\nHello Django")
# file.close()

# ----------------------------------------------
# Best Practice → with
# Instead of:

# file = open("data.txt", "r")
# print(file.read())
# file.close()

# Use:

# with open("data.txt", "r") as file:
#     print(file.read())

# Why?
# File automatically closes.
# ----------------------------------------------

# Check file exists
# import os
# if os.path.exists("week 1\\data.txt"):
#    print("File Exists")
# else:
#    print("File Not Found")   
# ---------------------------------------------

# Practical Example
# Create a file named data.txt and write your name into it.
# Read data.txt and print its content.
# Append your city name into data.txt.

with open("week 1\\data.txt", "r+") as file:
   file.write("Hello, I'm Rukhmai")
   file.seek(0)
   print(file.read())

with open("week 1\\data.txt", "a") as file:
   file.write("\nKarnal, Haryana") 

# Count total number of lines in a file.
# Count total words in a file.
# Count total characters in a file.

with open("week 1\\data.txt", "r") as file:
   content = file.read()
   lines = content.split("\n")
   words = content.split()
   characters = len(content)
print(content)
print("Lines:", len(lines))
print("Words:", len(words)) 
print("Characters:", characters)  

# Create a simple Notes App.

# 1. User enters note.
# 2. Save note in notes.txt.
# 3. Show all notes.

# note = input("Enter Note: ")

# with open("notes.txt", "a") as file:
#     file.write(note + "\n")

# with open("notes.txt", "r") as file:
#     print(file.read())

