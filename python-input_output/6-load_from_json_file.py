#!/usr/bin/python3
"""This module defines a function to load object from JSON file."""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file.

    Args:
        filename: The name of the JSON file to read from.

    Returns:
        The Python object represented by the JSON file.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
