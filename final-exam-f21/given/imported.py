class Imported:

    def __init__(self, origin):
        self.origin = origin

    def __eq__(self, other):
        if not isinstance(other, Imported):
            return False
        return self.origin == other.origin


    def __str__(self):

        return "Country of origin ({})".format(self.origin)