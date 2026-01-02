#!/usr/bin/python3
"""This module defines a Student class."""


class Student:
    """A class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student with first_name, last_name, and age.

        Args:
            first_name: The first name of the student.
            last_name: The last name of the student.
            age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs: Optional list of attribute names to retrieve.

        Returns:
            Dictionary containing requested attributes of the student.
        """
        if attrs is None:
            return self.__dict__
        if isinstance(attrs, list):
            result = {}
            for attr in attrs:
                if isinstance(attr, str) and hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dictionary.

        Args:
            json: Dictionary with attribute names as keys and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
