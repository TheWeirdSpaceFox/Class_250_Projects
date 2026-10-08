"""
Homework - Review

NOTE: First, fix the function names as described below

@author Amanda Sanders
"""


def get_rectangle_perimeter(length, width):

    """
    Return the perimeter of a rectangle

    Note: you can assume that length and width are valid numbers (either an int or a float)

    :param length:
    :param width:
    :return: perimeter of a rectangle - perimeter = 2*length + 2*width
    """

    return 2*length + 2*width


    #TO_DO_FIX_THIS_FUNCTION_NAME_AND_SIGNATURE
def get_box_volume_and_area(length, width, height):

    """
    Using standard Python naming conventions,
    create a function to "Get Box Volume and Area"


    Note: you can assume that length, width, and height are valid numbers (either an int or a float)

    volume of a rectangular box volume = length*width*height
    surface area of a rectangular box (Add up the area of each of the 6 sides)

    :param length:
    :param width:
    :param height:
    :return: a tuple with (volume, area)
    """
    volume = length*width*height
    area = 2*length*width + 2*length*height + 2*height*width
    tuple_va = (volume, area)
    return tuple_va


    #TO_DO_FIX_THIS_FUNCTION_NAME_AND_SIGNATURE
def get_coulomb_force(charge1, charge2, radius):
    """
    Using standard Python naming conventions,
    create a function to "Get Coulomb Force"

    The order of the arguments matters here.
    The correct order is: charge1, charge2, with the radius last.
    
    Use 8.987E9 for coulomb's constant, k.

    :param q1: charge1
    :param q2: charge2
    :param radius:
    :return: coulomb force F=k*(q1*q2)/r^2
    """
    k = 8.987E9
    radius_2 = radius*radius
    return k*(charge1*charge2)/radius_2


def get_last_names(names):
    """
    Given a list of strings, return a new list with only the last name
    Important: Name strings may contain middle names, so be sure you are returning the last name

    e.g. given ["Dwight Schrute", "Michael Scott", "Pam Beesly", "Jim Halpert", "Angela Noelle Martin"]
         return ["Schrute", "Scott", "Beesly", "Halpert", "Martin"]

    :param names:
    :return: a list of last names
    """
    i = 0
    list = []
    while i <= len(names)-1:
        name = names[i]
        name = name.split()
        list.append(name[-1])
        i += 1
    return list


def get_initials(names):
    """
    Given a list of strings, return a new list with the person's initials
    Important: Name strings may contain middle names. Middle names should be included in initials as shown in the example below

    e.g. given ["Dwight Schrute", "Michael Scott", "Pam Beesly", "Jim Halpert", "Angela Noelle Martin"]
         return ["DS", "MS", "PB", "JH", "ANM"]

    :param names:
    :return: a list of initials
    """
    i = 0
    list = []
    while i <= len(names)-1:
        name = names[i]
        name = name.split()
        name1 = name[0]
        name2 = name[1]
        if len(name) == 3:
            name3 = name[2]
            initials = name1[0] + name2[0] + name3[0]
        else:
            initials = name1[0] + name2[0]
        list.append(initials)
        i += 1
    return list

if __name__ == '__main__':
    print("rectangle perimeter:", get_rectangle_perimeter(5,10)," Should be 30")
    # print("box volume/area:", get_box_volume_and_area(5,10,10)," Should be (500,400)") # Be sure to check when width != height
    # print("coloumb's force:", get_coulomb_force(1.60217662E-19,1.60217662E-19,1E-10)," Should be ~2.3069E-08")

    sample_names = ["Dwight Schrute", "Michael Scott", "Pam Beesly", "Jim Halpert", "Angela Noelle Martin"]

    last_names = get_last_names(sample_names)
    print("Actual:  ", last_names)
    print("Expected:", ["Schrute", "Scott", "Beesly", "Halpert", "Martin"])

    initials = get_initials(sample_names)
    print("Actual:  ", initials)
    print("Expected:", ["DS", "MS", "PB", "JH", "ANM"])

