# ======================================================================
# Recursion = Recursion is a technique in which a function calls itself.
# ======================================================================
# Correct Recursion Example
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)

# Print 1 to N
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)
print_numbers(5)

# Factorial Using Recursion
def factorial(n):

    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Sum of Numbers 1 to N
def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)

print(total(5))

# Power Function
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(power(2, 3))

# Reverse String
def reverse_string(text):
    if len(text) == 0:
        return ""
    return reverse_string(text[1:]) + text[0]

print(reverse_string("python"))

# Print numbers from 5 to 1 using recursion.
def num(n):
    if n == 0:
        return
    print(n)
    num(n - 1)
num(8)    
