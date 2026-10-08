"""
Create ruminant class as described in README
"""

from src.homework.barnyard.farm_animal import FarmAnimal


class Ruminant(FarmAnimal):
    def __init__(self, age):
        FarmAnimal.__init__(self, age)

    def __str__(self):
        return "{},{}".format(FarmAnimal.__str__(self),"Ruminant")

    def make_sound(self):
        return "burp"

    def __eq__(self, other):
        return FarmAnimal.__eq__(self, other)

