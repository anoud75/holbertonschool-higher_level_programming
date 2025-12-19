#!/usr/bin/python3
"""This module defines mixin classes and a Dragon class."""


class SwimMixin:
    """A mixin class that provides swimming capability."""

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """A mixin class that provides flying capability."""

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A class representing a dragon that can swim and fly."""

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
