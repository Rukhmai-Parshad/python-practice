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
# # Q1 Find Length of Tuple
# def find_length(tpl):
#    return len(tpl)

# tpl = ("Rukhmai", 21, "BCA", "Karnal")
# result = find_length(tpl)
# print(f"Length of Tuple: {result}")

# # Q2 Find Maximum Element
# def find_maximum(tpl):
#    return max(tpl)

# tpl = (23, 45, 65, 34, 76, 98, 67, 99, 45)
# result = find_maximum(tpl)
# print(f"Maximum Element: {result}")

# # Q3 Find Minimum Element
# def find_minimum(tpl):
#    return min(tpl)

# tpl = (23, 45, 65, 34, 76, 98, 67, 99, 45)
# result = find_minimum(tpl)
# print(f"Minimum Element: {result}")

# # Q4 Count Occurrences of an Element
# def count_occurrences(tpl, element):
#    return tpl.count(element)

# tpl = (1, 2, 3, 2, 4, 2)
# print(count_occurrences(tpl, 2))

# # Q5 Convert Tuple to List
# def tuple_to_list(tpl):
#    lst = list(tpl)
#    return lst

# tpl = ("Rukhmai", 21, "Pardeep", 22)
# result = tuple_to_list(tpl)
# print(f"Tuple to List: {result}")

# # Q6 Convert List to Tuple
# def list_to_tuple(lst):
#    tpl = tuple(lst)
#    return tpl

# lst = [1, 56, 56, 87, 45, 34, 98, 34, 23, 45]
# result = list_to_tuple(lst)
# print(f"List to Tuple: {result}")

# # Q7 Check Whether Element Exists
# def element_exists(tpl, element):
#     return element in tpl

# tpl = (10, 20, 30, 40)
# print(element_exists(tpl, 20))

# # Q8 Find Index of an Element
# def find_index(tpl, element):
#     if element in tpl:
#         return tpl.index(element)
#     return -1

# tpl = (10, 20, 30, 40)
# print(find_index(tpl, 30))

# # Q9 Concatenate Two Tuples
# def concatenate_tuples(tpl1, tpl2):
#     return tpl1 + tpl2

# tpl1 = (1, 2, 3)
# tpl2 = (4, 5, 6)
# print(concatenate_tuples(tpl1, tpl2))

# # Q10 Unpack Tuple Values
# tpl = ("Rukhmai", 21, "BCA")
# name, age, course = tpl

# print(name)
# print(age)
# print(course)

# ======================================================================================
# DICTIONARY
# ======================================================================================

# # Q1 Count Frequency of Characters
# def count_frequency(s):
#    freq = {}
#    for ch in s:
#       freq[ch] = freq.get(ch, 0) + 1
#    return freq

# s = input("Enter some data: ")
# result = count_frequency(s)
# print(f"Frequency of character: {result}")

# # Q2 Count Frequency of Words
# def count_word_Frequency(words):
#    freq = {}
#    wd = words.split()
#    for w in wd:
#       freq[w] = freq.get(w, 0) + 1
#    return freq

# words = input("Enter some data: ")
# result = count_word_Frequency(words)
# print(result)

# # Q3 Merge Two Dictionaries
# def merge_dictionaries(dic1, dic2):
#    dic1.update(dic2)
#    return dic1

# dic1 = {'a' : 2, 'b' : 3, 'c' : 3} 
# dic2 = {'d' : 5, 'e' : 6, 'f' : 5}
# result = merge_dictionaries(dic1, dic2)
# print(result)

# # Q4 Find Key with Maximum Value
# def count_max_value(s):
#    freq = {}
#    for ch in s:
#       freq[ch] = freq.get(ch, 0) + 1
#    return max(freq, key = freq.get)

# s = input("Enter some data: ")
# result = count_max_value(s)
# print(f"Key with Maximum Value: {result}")  

# # Q5 Find Key with Minimum Value
# def count_min_value(s):
#    freq = {}
#    for ch in s:
#       freq[ch] = freq.get(ch, 0) + 1
#    return min(freq, key = freq.get)

# s = input("Enter some data: ")
# result = count_min_value(s)
# print(f"Key with Minimum Value: {result}") 

# # Q6 Invert Dictionary
# def invert_dictionary(student):
#    new_dic = {}
#    for key, value in student.items():
#       new_dic[value] = key
#    return new_dic

# student = {
#    "name" : "rukhmai",
#    "city" : "karnal",
#    "age" : 21
# }      
# result = invert_dictionary(student)
# print(f"Inverted Dictionary: {result}")

# # Q7 Sort Dictionary by Value
# def sort_by_value(dic):
#     return dict(sorted(dic.items(), key=lambda item: item[1]))

# dic = {
#     "a": 5,
#     "b": 2,
#     "c": 8
# }
# result = sort_by_value(dic)
# print(result)

# # Q8 Check if Key Exists
# def check_key(dic, key):
#     return key in dic

# dic1 = {
#    "name" : "rukhmai",
#    "city" : "karnal",
#    "age" : 21
# }
# if check_key(dic1, "name"):
#     print("Key Exists")
# else:
#     print("Key Does Not Exist")

# # Q9 Sum All Dictionary Values
# def sum_values(dic):
#     return sum(dic.values())

# dic = {'a' : 2, 'b' : 3, 'c' : 3} 
# result = sum_values(dic) 
# print(f"Sum All Dictionary Values: {result}")
 
# # Q10 Create Dictionary from Two Lists
# def create_dictionary(keys, values):
#    return dict(zip(keys, values))

# keys = ["name", "age", "city"]
# values = ["Rukhmai", 21, "Karnal"]
# result = create_dictionary(keys, values)
# print(f"Dictionary from Two Lists: {result}")

# ======================================================================================
# SETS
# ======================================================================================

# Q1 Remove Duplicates from List using Set
def remove_duplicates(lst):
   new_lst = list(set(lst))
   return new_lst

lst = [12, 34, 34, 67, 45, 23, 45, 23, 76, 76, 76, 32, 23, 34]
result = remove_duplicates(lst)
print(result)

# Q2 Find Union of Two Sets
def find_union(s1, s2):
   s = (s1 | s2)
   return s

s1 = {12, 34, 54, 65, 12, 34}
s2 = {12, 23, 34, 56 ,76, 34}
result = find_union(s1, s2)
print(f"Union of Two Sets: {result}")

# Q3 Find Intersection of Two Sets
def find_intersection(s1, s2):
   s = (s1 & s2)
   return s

s1 = {12, 34, 54, 65, 12, 34}
s2 = {12, 23, 34, 56 ,76, 34}
result = find_intersection(s1, s2)
print(f"Intersection of Two Sets: {result}")

# Q4 Find Difference of Two Sets
def find_difference(s1, s2):
   s = (s1 - s2)
   return s

s1 = {12, 34, 54, 65, 12, 34}
s2 = {12, 23, 34, 56 ,76, 34}
result = find_difference(s1, s2)
print(f"Difference of Two Sets: {result}")

# Q5 Find Symmetric Difference
def symmetric_difference(s1, s2):
   s = (s1 ^ s2)
   return s

s1 = {12, 34, 54, 65, 12, 34}
s2 = {12, 23, 34, 56 ,76, 34}
result = symmetric_difference(s1, s2)
print(f"Symmetric Difference of Two Sets: {result}")

# Q6 Check Subset
def check_subset(s1, s2):
   return s1.issubset(s2)
# def check_subset(s1, s2):
#     return s1 <= s2

s1 = {12, 34}
s2 = {12, 23, 34, 56 ,76, 34}
if check_subset(s1, s2):
   print("S1 is subset of S2")
else:
   print("S1 is not a subset of S2")   

# Q7 Check Superset
def check_superset(s1, s2):
   return s1.issuperset(s2)
# def check_superset(s1, s2):
#     return s1 >= s2

s1 = {98, 78, 67, 54, 45, 54}
s2 = {12, 23, 34, 56 ,76, 34}
if check_superset(s1, s2):
   print("S1 is superset of S2")
else:
   print("S1 is not a superset of S2")

# Q8 Find Unique Elements
def find_unique(s):
   s1 = s.split()
   return set(s1)

s = "python is an easy language and python is powerful"
result = find_unique(s)
print(result)

# Q9 Remove an Element from Set
def remove_element(s1, element):
   s1.remove(element)
   return s1

s1 = {23, 45, 65, 34, 65, 34, 34, 24, 3, 56 ,65, 65, 56}
result = remove_element(s1, 34)
print(result)

# Q10 Convert Set to List
def set_to_list(s1):
    return list(s1)

s1 = {23, 54 ,65, 34, 76, 56, 45}
result = set_to_list(s1) 
print(result)  
