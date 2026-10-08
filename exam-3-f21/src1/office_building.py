from src1.commercial_building import CommercialBuilding

class OfficeBuilding(CommercialBuilding):
    def __init__(self, name, country, floor_area, floors, height):
        CommercialBuilding.__init__(self, name, country, floor_area)
        self.floors = floors
        self.height = height

    def __str__(self):
        return "{} floors:{} height:{} ft".format(CommercialBuilding.__str__(self), self.floors, self.height)
