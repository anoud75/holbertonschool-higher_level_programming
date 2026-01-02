#!/usr/bin/python3
"""This module defines a function to convert object to JSON string."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string).

    Args:
        my_obj: The object to convert to JSON string.

    Returns:
        The JSON string representation of the object.
    """
    return json.dumps(my_obj)
