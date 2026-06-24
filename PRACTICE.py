# ======================================================================================
# STRINGS
# ======================================================================================

# Q1 Reverse a String
# def reverse_string(s):
#    return s[::-1]

# s = input("Enter a string: ")
# print(reverse_string(s))

# Q2 Check Palindrome String
# def is_palindrome(s):
#    return s == s[::-1]  

# s = input("Enter a string: ")
# if is_palindrome(s):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# Q3 Count Vowels in String
# def count_vowels(s):
#    count = 0
#    for ch in s.lower():
#       if ch in "aeiou":
#          count += 1
#    return count

# s = input("Enter a string: ")
# result = count_vowels(s)
# print(f"Vowels in a string: {result}")

# Q4 Count Words in String
# def count_words(s):
#     return len(s.split())

# s = input("Enter a string: ")
# result = count_words(s)
# print(f"Words in a string: {result}")

# Q5 Remove Spaces from String
def remove_spaces(s):
   return s.replace(" ", "")

s = input("Enter a string: ")
result = remove_spaces(s)
print(result)


# Q6 Find Duplicate Characters

# Q7 Count Frequency of Each Character

# Q8 Find First Non-Repeating Character

# Q9 Check Anagram

# Q10 Find Largest Word in a Sentence