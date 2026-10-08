class Grocery:

    def __init__(self, price):
        self.unit_cost = price

    def __str__(self):
        return "{} (${:.2f})".format(self.__class__.__name__, self.unit_cost)

    def per_unit_cost(self):
        """
        Return the price or "per unit cost"
        :return: unit cost
        """
        return self.unit_cost

    def __eq__(self, other):
        if not isinstance(other, Grocery):
            return False
        return self.unit_cost == other.unit_cost
