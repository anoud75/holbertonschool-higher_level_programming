#!/usr/bin/python3
"""This module defines a CountedIterator class."""


class CountedIterator:
    """An iterator that keeps track of the number of items iterated."""

    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable.

        Args:
            iterable: The iterable to iterate over.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator object.

        Returns:
            Self as the iterator.
        """
        return self

    def __next__(self):
        """Fetch the next item and increment the counter.

        Returns:
            The next item from the iterator.

        Raises:
            StopIteration: When there are no more items.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the current count of iterated items.

        Returns:
            The number of items that have been iterated.
        """
        return self.count
