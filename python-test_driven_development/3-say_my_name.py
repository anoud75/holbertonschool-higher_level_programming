#!/usr/bin/python3
"""
This module provides a function to print a name.
It validates that inputs are strings.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first_name> <last_name>.

    Args:
        first_name: First name (must be a string)
        last_name: Last name (must be a string), defaults to ""

    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
