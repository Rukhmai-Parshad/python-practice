# ============================================================
# Dictionary = Dictionary is a collection of key-value pairs.                 
# ============================================================
# ------------------------------------------------------------
# Functions You Must Remember

# get()
# keys()
# values()
# items()
# pop()
# copy()
# clear()
# update()
# len()
# ------------------------------------------------------------

# Why Use Dictionary?

# Mutable 
# Ordered 
# Keys must be unique 
# Values can be duplicate
# ------------------------------------------------------------

# Example:
student = {
   "name": "Rukhmai",
   "age": 21,
   "course": "Python"
}

# Access values
print(student["name"])
print(student["age"])

# get()
print(student.get("course"))

# Add new key
student["city"] = "Delhi"
print(student)

# Update Value
student["age"] = 22
print(student)

# Remove item
student.pop("city")
print(student)

# Delete item
del student["course"]
print(student)

# Length
print(len(student))

# Keys
print(student.keys())

# Values
print(student.values())

# Items
print(student.items())

# Check key exists
print("name" in student)

# Copy Dictionary
new_student = student.copy()
print(new_student)

# Clear Dictionary
# temp = {"a": 1, "b": 2}
# temp.clear()
# print(temp)

# Looping Through Dictionary
for key in student:
   print(key)

# Nested Dictionary
students = {
    101: {
        "name": "Riya",
        "age": 20
    },
    102: {
        "name": "Priya",
        "age": 21
    }
}

print(students[101]["name"])

# =============================================================
# Qustions
# =============================================================
# Frequency counter
text = "banana"

freq ={}
for ch in text:
   freq[ch] = freq.get(ch,0) + 1
print(freq)   
print(max(freq, key=freq.get))    # Find Highest Frequency Character

# Number and Square Dictionary
# Using Loop
nums = [10, 20, 30, 40]
result = {}
for num in nums:
    result[num] = num ** 2
print(result)

# Character and ASCII Dictionary
text = "python"
result = {}
for ch in text:
   result[ch] = ord(ch)
print(result)   

# Invert a Dictionary
student = {
    "name": "Rukhmai",
    "city": "Delhi"
}
new_dict = {}
for key, value in student.items():
    new_dict[value] = key
print(new_dict)

# Merge Two Dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d1.update(d2)
print(d1)