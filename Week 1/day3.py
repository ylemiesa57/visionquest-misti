"""Day 3: Introduction to NumPy.

This module introduces NumPy arrays and basic operations for numerical
computing. Students learn array creation, manipulation, and operations
to understand how images are represented as numerical data.

Reference:
- NumPy documentation: https://numpy.org/doc/
"""

import numpy as np


def matrix_sum_example():
    """Create a 2D NumPy array and find the sum of its elements.

    Returns:
        The sum of all elements in a 2D array example.
    """
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    return np.sum(matrix)


# Example: Array Creation
array = np.array([1, 2, 3, 4, 5])
print(array)

# Example: Basic Operations
array2 = np.array([5, 4, 3, 2, 1])
print(array + array2)

# Practice: Create a 2D NumPy array and find the sum of its elements.
print(matrix_sum_example())
