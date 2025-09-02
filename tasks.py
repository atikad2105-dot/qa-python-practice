# 1. Sum of two numbers
def add_numbers(a, b):
    return a + b

print(add_numbers(3, 5))   # expect 8
print(add_numbers(-1, 1))  # expect 0


# 2. Check if a number is even
def is_even(n):
    return n % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False


# 3. Convert Celsius to Fahrenheit
def c_to_f(c):
    return (c * 9/5) + 32

print(c_to_f(0))    # 32
print(c_to_f(25))   # 77


# 4. Factorial of a number
def factorial(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r

print(factorial(5))  # 120


# 5. String information
def string_info(s):
    return len(s), s.upper(), s.lower()

print(string_info("QA Automation"))
# (13, 'QA AUTOMATION', 'qa automation')

