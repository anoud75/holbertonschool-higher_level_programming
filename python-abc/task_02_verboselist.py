#!/usr/bin/python3
"""This module defines a VerboseList class that extends list."""


class VerboseList(list):
    """A list subclass that prints notifications on modifications."""

    def append(self, item):
        """Add an item to the list and print a notification.

        Args:
            item: The item to add to the list.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and print a notification.

        Args:
            iterable: The iterable to extend the list with.
        """
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Remove an item from the list and print a notification.

        Args:
            item: The item to remove from the list.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list and print a notification.

        Args:
            index: The index of the item to pop (default is last item).

        Returns:
            The popped item.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
