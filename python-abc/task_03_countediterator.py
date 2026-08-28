#!/usr/bin/python3
"""Defines CountedIterator, an iterator that counts the items it yields."""


class CountedIterator:
    """Wraps an iterable and tracks how many items have been iterated."""

    def __init__(self, iterable):
        """Initialize the underlying iterator and the item counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the number of items fetched so far."""
        return self.count

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Return the next item, incrementing the counter.

        Raises:
            StopIteration: When the underlying iterator is exhausted.
        """
        item = next(self.iterator)
        self.count += 1
        return item
