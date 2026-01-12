# Create a list of squares using list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print("Squares:", squares)

# Filter even numbers
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)

# Nested comprehension: multiply each number by 2 in a 2D list
matrix = [[1, 2], [3, 4]]
new_matrix = [[element*2 for element in row] for row in matrix]
print("Updated Matrix:", new_matrix)
