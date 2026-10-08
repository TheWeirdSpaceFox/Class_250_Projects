"""
Create goat class as described in README
"""
from src.homework.barnyard.ruminant import Ruminant

class Goat(Ruminant):
    def __init__(self, age):
        Ruminant.__init__(self, age)

    def __str__(self):
        return "{},{}".format(Ruminant.__str__(self),"Goat")

    def make_sound(self):
        return Ruminant.make_sound(self)+ " - " +"baaah"

    def __eq__(self, other):
        return Ruminant.__eq__(self, other)