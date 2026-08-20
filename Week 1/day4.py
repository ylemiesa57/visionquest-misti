"""Day 4: Introduction to Image Processing with OpenCV.

This module introduces basic image processing concepts using OpenCV (cv2).
Students learn how to load images, convert them to grayscale, and apply
thresholding operations for image manipulation.

Important: cv2.imread() silently returns None if the file cannot be loaded.
This module includes proper error handling to catch this common issue early.

Reference:
- OpenCV documentation: https://docs.opencv.org/
"""

import sys

import cv2


def load_and_process_image(image_path):
    """Load an image and convert it to grayscale.

    Args:
        image_path: Path to the image file to load.

    Returns:
        The grayscale image array, or None if the image could not be loaded.

    Raises:
        SystemExit: If the image file cannot be found or loaded.
    """
    image = cv2.imread(image_path)

    # cv2.imread() doesn't raise on a missing/unreadable file -- it silently
    # returns None, which then crashes cv2.cvtColor() with a confusing OpenCV
    # assertion error. This is the single most common gotcha students hit on
    # this exercise (forgetting to place example.jpg next to the script), so
    # check explicitly and fail with a clear message instead.
    if image is None:
        sys.exit(
            f"Could not load '{image_path}'. Make sure an image file exists "
            f"at that path and is in a supported format."
        )

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image


# Example: Convert an image to grayscale
image = cv2.imread('example.jpg')  # Load an image

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
