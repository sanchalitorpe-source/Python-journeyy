from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Map: square each number
squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)

# Filter: keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)

# Reduce: sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print("Total Sum:", total)
