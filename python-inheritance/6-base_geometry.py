#!/usr/bin/python3
"""This module defines a BaseGeometry class."""


class BaseGeometry:
    """A class that defines base geometry with area method."""

    def area(self):
        """Raise an exception indicating area is not implemented.

        Raises:
            Exception: Always raises with message that area is not implemented.
        """
        raise Exception("area() is not implemented")
