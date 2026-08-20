"""Day 1: Program Introduction and Python Basics.

This module covers fundamental Python concepts including data types,
conditionals, and loops. It serves as an introduction to the MIT-MISTI
AI Vision Quest program.

Program Introduction:
- Overview of MIT-MISTI and AI Vision Quest.
- Instructor introductions and curriculum overview.
- Icebreaker activity: Brainstorm AI vision applications.
"""


def check_even_odd(number):
    """Determine whether a number is even or odd.

    Args:
        number: An integer to check.

    Returns:
        A string indicating "Even" if the number is divisible by 2,
        "Odd" otherwise.
    """
    return "Even" if number % 2 == 0 else "Odd"


# Python Basics Review
# Data types, conditionals, loops examples

# Example: Data Types
my_string = "Hello, AI Vision Quest!"
my_int = 42
my_float = 3.14
print(type(my_string), type(my_int), type(my_float))

# Practice: Write a function that checks if a number is even or odd.
# Call the function
print(check_even_odd(10))  # Example usage
