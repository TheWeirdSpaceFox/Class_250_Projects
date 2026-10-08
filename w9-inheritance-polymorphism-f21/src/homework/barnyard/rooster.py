"""
Create rooster class as described in README
"""

from src.homework.barnyard.chicken import Chicken
from src.homework.barnyard.winged_animal import WingedAnimal

class Rooster(WingedAnimal):
    def __init__(self, age):
        WingedAnimal.__init__(self, age)

    def __str__(self):
        return "{},{}".format(WingedAnimal.__str__(self),"Rooster")

    def make_sound(self):
        return WingedAnimal.make_sound(self) + " - " +"cock-a-doodle doo!"

    def __eq__(self, other):
        return WingedAnimal.__eq__(self, other)
