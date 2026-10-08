"""
Program 1

Module defines the functions/methods as defined by docstrings below

@author Amanda Sanders
"""

from src1.commercial_building import CommercialBuilding
from src1.office_building import OfficeBuilding
from given.table import Table

def create_table():
    """
    Create and return an instance of a Table with a length of 2 and width of 4 from the given folder.
    (This is simple; don't overthink it.)

    :return: instance of Rectangle
    """
    return Table(2,4)



def read_city_data(file_path):
    """
        Read the data from a text file given full path file name (including directory)
        The text file contains information to create Building instances
        Create and return a list of Building instances based on the contents of the text file

                Note: Find instructions for creating the Building class in building.py

        Check the header in buildings.txt to get the file format. The square footage should be an integer!
        Note: The header should not be used to create an instance of the Building class.

        :param full_path_name:  text file
        :return: list of instances of the CommercialBuilding class

    """

    buildings = []
    x = 0
    with open(file_path) as file:
        for i in file:
            if x == 0:
                x +=1
            else:
                i = i.strip().split(",")
                buildings.append(CommercialBuilding(i[0], i[1], i[2]))
    return buildings


def create_buildings():

    """
    Create and return a list of 2 commercial buildings and 1 office building. Use any values you would like but I have provided some suggested values.

        For example: The Ferguson center is 249,750 ft^2, Luter Hall is 135,000 ft^2,
            and Christopher Newport Hall is 81,000 ft^2 with 4 floors and is approximately 80 ft tall.

        Note: Find instructions for creating the classes in commercial_building.py.

    :return: List of building instances
    """
    building1 = CommercialBuilding("The Ferguson center", "Luter Hall", 135000)
    building2 = CommercialBuilding("The Ferguson center", "Christopher Newport Hall", 81000)
    building3 = OfficeBuilding("The Ferguson center", "Christopher Newport Hall", 81000, 4, 80)
    list = [building1, building2, building3]
    return list

"""
^^^^^^^^^^^^^^^^^^ your code up here ^^^^^^^^^^^^^^^^^^^^ 
I'm giving you the below code as simple test.  Just leave as is
"""
if __name__ == '__main__':
    """
    Make sure you run this script from the project workspace, not the src1 folder
    """
    import os
    full_path_file_name = os.path.join("data", "buildings.txt")
    print("full path=", full_path_file_name)
    data = read_city_data(full_path_file_name)
    print(data)
    print(" Expect 5 ", len(data))
    for dat in data:
        if not isinstance(dat, CommercialBuilding):
            raise ValueError("Not a CommercialBuilding instance")
        print("   ", dat)
