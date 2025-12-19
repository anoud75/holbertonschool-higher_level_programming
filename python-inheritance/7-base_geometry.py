#!/usr/bin/python3
"""This module defines a BaseGeometry class."""


class BaseGeometry:
    """A class that defines base geometry with validation."""

    def area(self):
        """Raise an exception indicating area is not implemented.

        Raises:
            Exception: Always raises with message that area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name: The name of the value (always a string).
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
