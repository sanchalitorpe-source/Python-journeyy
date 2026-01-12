# Lambda function to add two numbers
add = lambda x, y: x + y
print("Sum:", add(5, 3))

# Lambda with filter to get even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# Lambda with map to double numbers
doubled = list(map(lambda x: x*2, numbers))
print("Doubled:", doubled)
