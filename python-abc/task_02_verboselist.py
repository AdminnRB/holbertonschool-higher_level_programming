#!/usr/bin/python3
"""Defines VerboseList, a list subclass that announces its mutations."""


class VerboseList(list):
    """A list that prints a notification on every add or remove operation."""

    def append(self, item):
        """Append an item and announce it."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and announce how many items were added."""
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Announce and then remove the first occurrence of an item."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Announce and then pop the item at the given index (default last)."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
