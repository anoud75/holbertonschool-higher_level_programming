#!/usr/bin/python3
"""This module defines abstract Animal class and its subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that should return the sound the animal makes."""
        pass


class Dog(Animal):
    """A class representing a dog."""

    def sound(self):
        """Return the sound a dog makes.

        Returns:
            The string 'Bark'.
        """
        return "Bark"


class Cat(Animal):
    """A class representing a cat."""

    def sound(self):
        """Return the sound a cat makes.

        Returns:
            The string 'Meow'.
        """
        return "Meow"
