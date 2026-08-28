#!/usr/bin/python3
"""Explores multiple inheritance and MRO with a FlyingFish class."""


class Fish:
    """A fish that swims and lives in water."""

    def swim(self):
        """Print that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print where the fish lives."""
        print("The fish lives in water")


class Bird:
    """A bird that flies and lives in the sky."""

    def fly(self):
        """Print that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print where the bird lives."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A fish that can also fly, inheriting from both Fish and Bird."""

    def swim(self):
        """Print that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def fly(self):
        """Print that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Print where the flying fish lives."""
        print("The flying fish lives both in water and the sky!")
