#!/usr/bin/python3
"""This module defines a function to check class or inherited instance."""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance of, or inherited from, a class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or its subclass, else False.
    """
    return isinstance(obj, a_class)
