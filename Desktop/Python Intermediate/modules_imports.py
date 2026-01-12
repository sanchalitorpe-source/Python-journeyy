# Importing built-in modules
import math
import random

print("Square root of 16:", math.sqrt(16))
print("Random number between 1-10:", random.randint(1, 10))

# Importing specific function
from math import factorial
print("Factorial of 5:", factorial(5))

# Import your own module
# Create a file called my_module.py with a function
# def greet(name):
#     print("Hello", name)
# Then:
# from my_module import greet
# greet("Python")
