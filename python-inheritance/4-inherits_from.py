#!/usr/bin/python3
"""This module defines a function to check inherited class instance."""


def inherits_from(obj, a_class):
    """Check if object is an instance of a class that inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is instance of a subclass of a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
