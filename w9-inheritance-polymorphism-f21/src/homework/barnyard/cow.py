"""
Create cow class as described in README
"""

from src.homework.barnyard.ruminant import Ruminant

class Cow(Ruminant):
    def __init__(self, age):
        Ruminant.__init__(self, age)

    def __str__(self):
        return "{},{}".format(Ruminant.__str__(self), "Cow")

    def make_sound(self):
        return Ruminant.make_sound(self)+" - " +"moo"

    def __eq__(self, other):
        return Ruminant.__eq__(self, other)