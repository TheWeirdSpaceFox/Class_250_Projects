"""
Create duck class as described in README
"""
from src.homework.barnyard.winged_animal import WingedAnimal


class Duck(WingedAnimal):
    def __init__(self, age):
        WingedAnimal.__init__(self, age)

    def __str__(self):
        return "{},{}".format(WingedAnimal.__str__(self),"Duck")

    def make_sound(self):
        return WingedAnimal.make_sound(self)+" - " +"quack, quack"

    def __eq__(self, other):
        return WingedAnimal.__eq__(self, other)

