#!/usr/bin/python3
"""Module for lookup function."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: Any object to inspect.

    Returns:
        A list containing the names of all attributes and methods
        available for the given object.
    """
    return dir(obj)
