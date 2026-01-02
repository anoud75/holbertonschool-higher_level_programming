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

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance.

        Returns:
            Dictionary containing all attributes of the student.
        """
        return self.__dict__
