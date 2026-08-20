"""Day 2: Python Functions and List Comprehensions.

This module covers defining functions with arguments, return values,
and using list comprehensions to write compact, efficient code.
"""


def greet(name):
    """Return a greeting message for the given name.

    Args:
        name: A string representing a person's name.

    Returns:
        A formatted greeting string.
    """
    return f"Hello, {name}!"


def sum_list(numbers):
    """Calculate the sum of all elements in a list using list comprehension.

    Args:
        numbers: A list of numeric values.

    Returns:
        The sum of all elements in the list.
    """
    return sum([num for num in numbers])


print(greet("AI Vision Quest"))

# Example: List Comprehension
squares = [x**2 for x in range(10)]
print(squares)

# Call the function
print(sum_list([1, 2, 3, 4, 5]))  # Example usage
