# Day 4: Introduction to Image Processing/OpenCV
# Video Link: [Insert Link Here]

"""
Content:
- Introduction to image processing and understanding image arrays.
- Hands-on activities for basic image manipulations.
"""

import sys

import cv2

# Example: Convert an image to grayscale
image = cv2.imread('example.jpg')  # Load an image

# cv2.imread() doesn't raise on a missing/unreadable file -- it silently
# returns None, which then crashes cv2.cvtColor() with a confusing OpenCV
# assertion error. This is the single most common gotcha students hit on
# this exercise (forgetting to place example.jpg next to the script), so
# check explicitly and fail with a clear message instead.
if image is None:
    sys.exit(
        "Could not load 'example.jpg'. Make sure an image named "
        "example.jpg is in the same folder as this script."
    )

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_example.jpg', gray_image)  # Save the grayscale image

# Practice: Load an image and apply a threshold to it.
_, threshold_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('threshold_example.jpg', threshold_image)
