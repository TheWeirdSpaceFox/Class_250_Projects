
"""
     This file will contain a class called CommercialBuilding.

     The CommercialBuilding class takes three input parameters: name, country, floor_area. (Do not change these names or order)

     The class stores the data as attributes, and defines 4 instance methods:
        __lt__(), __eq__(), __add__(),and str().
        Note: For the instance attributes, use the same name as the input parameter!

         -For the less than method you should compare only the floor area.
         -For the equal to method you should compare all 3 instance attributes.
         -For the addition method you should add together the floor areas and return that value
            -If the value passed to the addition method is an integer you should return the floor area combined with that value
            -For all other types return 0.

     The str method should follow the following format: '<name> (<country>) floor area:<area> ft^2'
        Be careful to ensure there are no additional spaces.

    For full credit you should create one additional class in the src1 folder. This class should be
    named OfficeBuilding and should inherit from CommercialBuilding. The file should follow pythonic naming conventions.
        -In addition to name, country, floor_area you should also have instance attributes for floors and height.
             (Do not change these names or order)
        -Override the string method to print out the additional attributes:
            <name> (<country>) floor area:<floor area> ft^2 floors:<floors> height:<height> ft

"""
class CommercialBuilding:
    def __init__(self, name, country, floor_area):
        self.name = name
        self.country = country
        self.floor_area = floor_area

    def __lt__(self, other):
        if self.floor_area < other.floor_area:
            return True
        else:
            return False

    def __eq__(self, other):
        i = 0
        if self.floor_area == other.floor_area:
            i+= 1
        if self.name == other.name:
            i+= 1
        if self.country == other.country:
            i+=1
        if i == 3:
            return True
        if i != 3:
            return False

    def __add__(self, other):
        if type(other) == int:
            new = self.floor_area + other
            return new
        elif isinstance(other, CommercialBuilding):
            return other.floor_area + self.floor_area
        else:
            return 0

    def __str__(self):
        return '{} ({}) floor area:{} ft^2'.format(self.name, self.country, self.floor_area)
