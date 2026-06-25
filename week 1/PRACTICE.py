# # ======================================================================================
# # STRINGS
# # ======================================================================================

# # Q1 Reverse a String
# def reverse_string(s):
#    return s[::-1]

# s = input("Enter a string: ")
# print(reverse_string(s))

# # Q2 Check Palindrome String
# def is_palindrome(s):
#    return s == s[::-1]  

# s = input("Enter a string: ")
# if is_palindrome(s):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# # Q3 Count Vowels in String
# def count_vowels(s):
#    count = 0
#    for ch in s.lower():
#       if ch in "aeiou":
#          count += 1
#    return count

# s = input("Enter a string: ")
# result = count_vowels(s)
# print(f"Vowels in a string: {result}")

# # Q4 Count Words in String
# def count_words(s):
#     return len(s.split())

# s = input("Enter a string: ")
# result = count_words(s)
# print(f"Words in a string: {result}")

# # Q5 Remove Spaces from String
# def remove_spaces(s):
#    return "".join(s.split())

# s = input("Enter a string: ")
# result = remove_spaces(s)
# print(result)


# # Q6 Find Duplicate Characters
# def find_duplicate(s):
#     freq = {}
#     for ch in s:
#         freq[ch] = freq.get(ch, 0) + 1

#     duplicate = set()
#     for ch, count in freq.items():
#         if count > 1:
#             duplicate.add(ch)
#     return duplicate      

# s = input("Enter a string: ")
# result = find_duplicate(s)
# print(f"Duplcate characters: {result}")

# # Q7 Count Frequency of Each Character
# def find_frequency(s):
#    freq = {}
#    for ch in s:
#       freq[ch] = freq.get(ch, 0) + 1

#    for ch, char in freq.items() :  
#       print(f"Frequency of Character: {ch} -> {char}")

# s = input("Enter a string: ")
# find_frequency(s)

# # Q8 Find First Non-Repeating Character
# def first_non_repeating(s):

#     freq = {}
#     for ch in s:
#         freq[ch] = freq.get(ch, 0) + 1

#     for ch in s:
#         if freq[ch] == 1:
#             return ch
#     return None      

# s = input("Enter a string: ")
# result = first_non_repeating(s)
# print(f"Non repeated characters: {result}")

# # Q9 Check Anagram
# def is_anagram(s1, s2):
#     return sorted(s1) == sorted(s2)

# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")                     
# if is_anagram(s1, s2):
#     print("Anagram")
# else:
#     print("Not Anagram")

# # Q10 Find Largest Word in a Sentence
# def find_largest(s):
#     words = s.split()
#     if not words:
#         return None
#     largest = words[0]
#     for word in words:
#         if len(word) > len(largest):
#             largest = word
#     return largest     

# s = input("Enter a string: ")
# result = find_largest(s)
# print(f"Largest Word in a Sentence: {result}")      

# ======================================================================================
# LISTS
# ======================================================================================

# Q1 Find Largest Element
# def find_largest(nums):
#     if not nums:
#         return None
#     largest = nums[0]
#     for num in nums:
#         if num > largest:
#             largest = num
#     return largest

# nums = [23, 67, 97, 67, 99, 67, 83, 85]
# result = find_largest(nums)
# print(f"Largest element is: {result}")

# # Q2 Find Smallest Element
# def find_smallest(nums):
#     smallest = nums[0]
#     for num in nums:
#         if num < smallest:
#             smallest = num
#     return smallest

# nums = [23, 67, 97, 67, 99, 67, 83, 85]
# result = find_smallest(nums)
# print(f"Smallest element is: {result}")

# # Q3 Find Second Largest Element
# def find_second_largest(nums):
#     largest = second = float('-inf')
#     for num in nums:
#         if num > largest:
#             second = largest
#             largest = num
#         elif num > second and num != largest:
#             second = num
#     return second

# nums = [23, 45, 45, 98, 67, 56, 54, 34] 
# result = find_second_largest(nums)
# print(f"Second largest element: {result}")   

# # Q4 Reverse a List
# def reverse_list(lst):
#     return lst[::-1]

# lst = [1, 4, 6, 7, 8, 9, 76, 98, 99]
# result = reverse_list(lst)
# print(result)

# # Q5 Remove Duplicates from List
# def remove_duplicates(lst):
#     unique = []
#     for item in lst:
#         if item not in unique:
#             unique.append(item)
#     return unique

# lst = [34, 65, 65, 87, 67, 75, 65, 34, 77]
# result = remove_duplicates(lst)
# print(f"Duplicate element: {result}")

# # Q6 Find Sum of List Elements
# def sum_of_list(lst):
#     total = 0
#     for i in lst:
#         total = total + i
#     return total    

# lst = [34, 65, 65, 87, 67, 75, 65, 34, 77]
# result = sum_of_list(lst)
# print(f"sum of list: {result}")

# # Q7 Find Even Numbers from List
# def find_even(nums):
#     even_numbers = []
#     for n in nums:
#         if (n % 2) == 0:
#             even_numbers.append(n)
#     return even_numbers

# nums = [98, 54, 65, 76, 54, 65, 45]
# result = find_even(nums)
# print(f"Even Numbers: {result}")

# # Q8 Find Common Elements Between Two Lists
# def common_elements(lst1, lst2):
#     common = []
#     for item in lst1:
#         if item in lst2 and item not in common:
#             common.append(item)
#     return common

# lst1 = [34, 45, 34, 65, 87, 98, 97]
# lst2 = [34, 56, 45, 53, 97, 45, 25]
# result = common_elements(lst1, lst2)
# print(f"Common elements: {result}")

# # Q9 Merge Two Lists
# def merge_two_list(lst1, lst2):
#    return (lst1 + lst2)

# lst1 = [98, 78, 54, 32, 32, 56]
# lst2 = [98, 65, 76]
# result = merge_two_list(lst1, lst2)
# print(result)

# # Q10 Count Frequency of Elements
# def count_frequency(lst):
#    freq = {}
#    for ls in lst:
#       freq[ls] = freq.get(ls, 0) + 1

#    for ls, count in freq.items():
#         print(f"Frequency: {ls} -> {count}")

# lst = [23, 32, 56, 43, 43, 65, 23, 78, 65, 23]     
# count_frequency(lst)

# ======================================================================================
# TUPLES
# ====================================================================================== 
#   
# Q1 Find Length of Tuple
def find_length(tpl):
   return len(tpl)

tpl = ("Rukhmai", 21, "BCA", "Karnal")
result = find_length(tpl)
print(f"Length of Tuple: {result}")

# Q2 Find Maximum Element
def find_maximum(tpl):
   return max(tpl)

tpl = (23, 45, 65, 34, 76, 98, 67, 99, 45)
result = find_maximum(tpl)
print(f"Maximum Element: {result}")

# Q3 Find Minimum Element
def find_minimum(tpl):
   return min(tpl)

tpl = (23, 45, 65, 34, 76, 98, 67, 99, 45)
result = find_minimum(tpl)
print(f"Minimum Element: {result}")

# Q4 Count Occurrences of an Element
 

# Q5 Convert Tuple to List
def tuple_to_list(tpl):
   lst = list(tpl)
   return lst

tpl = ("Rukhmai", 21, "Pardeep", 22)
result = tuple_to_list(tpl)
print(f"Tuple to List: {result}")

# Q6 Convert List to Tuple
def list_to_tuple(lst):
   tpl = tuple(lst)
   return tpl

lst = [1, 56, 56, 87, 45, 34, 98, 34, 23, 45]
result = list_to_tuple(lst)
print(f"List to Tuple: {result}")

# Q7 Check Whether Element Exists

# Q8 Find Index of an Element

# Q9 Concatenate Two Tuples

# Q10 Unpack Tuple Values