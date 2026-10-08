from given.dairy import Dairy


class Cheese(Dairy):

    def __init__(self, price):
        Dairy.__init__(self, price)
