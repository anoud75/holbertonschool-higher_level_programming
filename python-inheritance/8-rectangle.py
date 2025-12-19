#!/usr/bin/python3
"""This module defines a Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height.

        Args:
            width: The width of the rectangle (positive integer).
            height: The height of the rectangle (positive integer).
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
