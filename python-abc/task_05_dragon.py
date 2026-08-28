#!/usr/bin/python3
"""Demonstrates composing behavior with mixins on a Dragon class."""


class SwimMixin:
    """Mixin that grants swimming ability."""

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that grants flying ability."""

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can swim and fly thanks to its mixins."""

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
