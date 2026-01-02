#!/usr/bin/python3
"""This module defines a CustomObject class with pickle serialization."""
import pickle


class CustomObject:
    """A custom class that can be serialized with pickle."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject with name, age, and is_student.

        Args:
            name: A string representing the name.
            age: An integer representing the age.
            is_student: A boolean indicating if the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print out the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current instance and save to a file.

        Args:
            filename: The filename to save the serialized object to.
        """
        try:
            with open(filename, mode="wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance of CustomObject from a file.

        Args:
            filename: The filename to load the object from.

        Returns:
            An instance of CustomObject, or None if an error occurs.
        """
        try:
            with open(filename, mode="rb") as f:
                return pickle.load(f)
        except Exception:
            return None
