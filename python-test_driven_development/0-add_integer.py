#!/usr/bin/python3
"""
This module provides a function to add two integers.
It handles type validation and float-to-int conversion.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (cast to integers).

    Args:
        a: First number (int or float)
        b: Second number (int or float), defaults to 98

    Returns:
        Integer sum of a and b

    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float) and (a != a or a == float('inf') or a == -float('inf')):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b != b or b == float('inf') or b == -float('inf')):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
