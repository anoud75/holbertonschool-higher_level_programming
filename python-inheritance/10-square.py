#!/usr/bin/python3
"""This module defines a Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that defines a square using Rectangle."""

    def __init__(self, size):
        """Initialize the square with size.

        Args:
            size: The size of the square (positive integer).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
