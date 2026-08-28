#!/usr/bin/env python3
from abc import ABC, abstractmethod

# 1. Abstract Base Class-in yaradılması
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# 2. Dog (İt) subclass-ının yaradılması
class Dog(Animal):
    def sound(self):
        return "Bark"

# 3. Cat (Pişik) subclass-ının yaradılması
class Cat(Animal):
    def sound(self):
        return "Meow"
