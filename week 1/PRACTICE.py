# # ======================================================================================
# # STRINGS
# # ======================================================================================

# # Q1 Reverse a String
def reverse_string(s):
   return s[::-1]

s = input("Enter a string: ")
print(reverse_string(s))

# # Q2 Check Palindrome String
def is_palindrome(s):
   return s == s[::-1]  

s = input("Enter a string: ")
if is_palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")


# # Q3 Count Vowels in String
def count_vowels(s):
   count = 0
   for ch in s.lower():
      if ch in "aeiou":
         count += 1
   return count

s = input("Enter a string: ")
result = count_vowels(s)
print(f"Vowels in a string: {result}")

# # Q4 Count Words in String
def count_words(s):
    return len(s.split())

s = input("Enter a string: ")
result = count_words(s)
print(f"Words in a string: {result}")

# # Q5 Remove Spaces from String
def remove_spaces(s):
   return "".join(s.split())

s = input("Enter a string: ")
result = remove_spaces(s)
print(result)


# # Q6 Find Duplicate Characters
def find_duplicate(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    duplicate = set()
    for ch, count in freq.items():
        if count > 1:
            duplicate.add(ch)
    return duplicate      

s = input("Enter a string: ")
result = find_duplicate(s)
print(f"Duplcate characters: {result}")

# Q7 Count Frequency of Each Character
def find_frequency(s):
   freq = {}
   for ch in s:
      freq[ch] = freq.get(ch, 0) + 1

   for ch, char in freq.items() :  
      print(f"Frequency of Character: {ch} -> {char}")

s = input("Enter a string: ")
find_frequency(s)

# Q8 Find First Non-Repeating Character
def first_non_repeating(s):

    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch
    return None      

s = input("Enter a string: ")
result = first_non_repeating(s)
print(f"Non repeated characters: {result}")

# Q9 Check Anagram
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")                     
if is_anagram(s1, s2):
    print("Anagram")
else:
    print("Not Anagram")

# Q10 Find Largest Word in a Sentence
def find_largest(s):
    words = s.split()
    if not words:
        return None
    largest = words[0]
    for word in words:
        if len(word) > len(largest):
            largest = word
    return largest     

s = input("Enter a string: ")
result = find_largest(s)
print(f"Largest Word in a Sentence: {result}")      

