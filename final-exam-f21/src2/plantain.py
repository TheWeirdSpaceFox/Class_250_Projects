from given.imported import Imported
from given.grocery import Grocery


class Plantain(Grocery,Imported):
    def __init__(self, price, origin):
        Grocery.__init__(self,price)
        Imported.__init__(self, origin)

    def __str__(self):
        return "{}, {}".format(Grocery.__str__(self), Imported.__str__(self))