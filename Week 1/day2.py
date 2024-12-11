# Day 2: Python Functions and List Comprehensions
# Video Link: [Insert Link Here]

"""
Content:
- Defining functions, arguments, and return values.
- List comprehensions for compact code.
"""

# Example: Defining Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("AI Vision Quest"))

# Example: List Comprehension
squares = [x**2 for x in range(10)]
print(squares)

# Practice: Write a function to sum all elements in a list using a list comprehension.
def sum_list(numbers):
    return sum([num for num in numbers])

# Call the function
print(sum_list([1, 2, 3, 4, 5]))  # Example usage
