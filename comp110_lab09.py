"""
Module: comp110_lab09

Modules with some functions for Lab 09 practice problems.
"""
from cImage import *
import math

def horizontal_flip(oldimage):
    """
    Returns a new image that is a copy of oldImage, but flipped about a
    horizontal line through the center of the image.
    """
    num_cols = oldimage.getWidth()
    num_rows = oldimage.getHeight()

    newim = EmptyImage(num_cols, num_rows)

    for row in range(num_rows):
        for col in range(num_cols):

            oldpixel = oldimage.getPixel(col, num_rows - row - 1)

            newim.setPixel(col, row, oldpixel)

    return newim

def diagonal_mirror(image):
    """
    Image is mirrored about the diagonal line running from upper left to lower
    right.  image must be square
    """

def flip_test(imageFile):
    """
    Code to test the horizontal_flip function.
    """
    old_image = FileImage(imageFile)
    image_window = ImageWin("Image Processing", old_image.getWidth(), old_image.getHeight())
    old_image.draw(image_window)

    flip_image = horizontal_flip(old_image)
    flip_image_window = ImageWin("Image Processing",
                                 flip_image.getWidth(), flip_image.getHeight())
    flip_image.draw(flip_image_window)

    image_window.exitOnClick()
    flip_image_window.exitOnClick()

def diagonal_mirror_test(imageFile):
    """
    Code to test the diagonal_mirror function.
    """
    image = FileImage(imageFile)
    image_window = ImageWin("Before Mirroring", image.getWidth(), image.getHeight())
    image.draw(image_window)

    diagonal_mirror(image)
    mirror_image_window = ImageWin("After Mirroring",
                                   image.getWidth(), image.getHeight()) 
    image.draw(mirror_image_window)

    image_window.exitOnClick()
    mirror_image_window.exitOnClick()

# Call the test functions
if __name__ == "__main__":
    flip_test("green-bird.gif")
