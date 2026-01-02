#!/usr/bin/python3
"""This module defines a function to convert class to JSON dictionary."""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        Dictionary with all serializable attributes of the object.
    """
    return obj.__dict__
