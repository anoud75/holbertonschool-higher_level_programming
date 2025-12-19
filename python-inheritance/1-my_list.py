#!/usr/bin/python3
"""This module defines a class MyList that inherits from list."""


class MyList(list):
    """A class that inherits from list with sorted print capability."""

    def print_sorted(self):
        """Print the list in ascending sorted order.

        The original list is not modified.
        """
        print(sorted(self))
