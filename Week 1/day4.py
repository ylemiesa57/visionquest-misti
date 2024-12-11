# Day 4: Introduction to Image Processing/OpenCV
# Video Link: [Insert Link Here]

"""
Content:
- Introduction to image processing and understanding image arrays.
- Hands-on activities for basic image manipulations.
"""

import numpy as np
import cv2

# Example: Convert an image to grayscale
image = cv2.imread('example.jpg')  # Load an image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_example.jpg', gray_image)  # Save the grayscale image

# Practice: Load an image and apply a threshold to it.
_, threshold_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('threshold_example.jpg', threshold_image)
