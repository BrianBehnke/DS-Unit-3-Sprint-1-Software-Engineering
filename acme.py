#!/usr/bin/env python
"""
Python module for Acme Corporation.
"""

from random import randrange


class Product:
    """Python class for products at Acme
    """
    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=randrange(1000000, 9999999)):
        self.name = str(name)
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flammability)
        self.identifier = int(identifier)

    def stealability(self):
        swipeable = self.price / self.weight
        if swipeable < 0.5:
            print("No so stealable...")
        elif swipeable > 0.5 and swipeable <= 1.0:
            print("Kinda Stealable.")
        else:
            print("Very stealable!")

    def explode(self):
        dynomite = self.flammability * self.weight
        if dynomite < 10:
            print("...fizzle.")
        elif dynomite >= 10 and dynomite < 50:
            print("...boom!")
        else:
            print("...BABOOM!!")


class BoxingGlove(Product):

    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=randrange(1000000, 9999999)):
        self.name = str(name)
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flammability)
        self.identifier = int(identifier)

    def explode(self):
        print("...it's a glove.")

    def punch(self):
        if self.weight < 5:
            print("That tickles.")
        elif self.weight >= 5 and self.weight < 15:
            print("Hey that hurt!")
        else:
            print("OUCH!")
