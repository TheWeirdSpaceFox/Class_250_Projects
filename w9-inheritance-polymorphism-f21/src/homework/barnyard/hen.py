"""
Create hen class as described in README
"""


from src.homework.barnyard.chicken import Chicken

class Hen(Chicken):
    def __init__(self, age):
        Chicken.__init__(self, age)

    def __str__(self):
        return "{},{}".format(Chicken.__str__(self),"Hen")

    def make_sound(self):
        return Chicken.make_sound(self)+ " - " +"squawk!"

    def __eq__(self, other):
        return Chicken.__eq__(self, other)
