"""
Create farm_animal class as described in README
"""
class FarmAnimal:
    def __init__(self, age):
        self.age = float(age)
    def __str__(self):
        return "{}".format(self.age)
    def make_sound(self):
        return ""
    def __eq__(self, other):
        if self.age == other.age:
            return True
        else:
            return False