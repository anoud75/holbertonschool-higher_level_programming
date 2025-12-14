#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """A class that defines a square with position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position.

        Args:
            size: The size of the square (must be integer >= 0).
            position: The position of the square (tuple of 2 positive ints).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value: The new size (must be integer >= 0).

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square.

        Returns:
            The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value: The new position (tuple of 2 positive integers).

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            The area of the square (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square with # characters at the given position.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
