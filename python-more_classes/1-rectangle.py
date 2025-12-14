#!/usr/bin/python3
"""This module defines a Rectangle class."""


class Rectangle:
    """A class that defines a rectangle by width and height."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with width and height.

        Args:
            width: The width of the rectangle (must be integer >= 0).
            height: The height of the rectangle (must be integer >= 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle.

        Returns:
            The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation.

        Args:
            value: The new width (must be integer >= 0).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle.

        Returns:
            The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation.

        Args:
            value: The new height (must be integer >= 0).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
