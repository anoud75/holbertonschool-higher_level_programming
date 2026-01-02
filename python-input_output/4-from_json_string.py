#!/usr/bin/python3
"""This module defines a function to convert JSON string to object."""
import json


def from_json_string(my_str):
    """Return a Python object represented by a JSON string.

    Args:
        my_str: The JSON string to convert.

    Returns:
        The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
