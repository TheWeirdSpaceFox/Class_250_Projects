"""
Program 2

Write functions as defined by docstrings below

You can use lists instead of Numpy arrays on this Exam (but not later exams)
But, you life will be simpler if you use Numpy

@author Amanda Sanders
"""


import csv
import numpy as np
import os
import math
# You might need to import more!

def define_numpy_sides(max_val):
    """
    return list or Numpy array from 3 to max value
    include max val in array
    :param max_val: integer max value (inclusive!)
    :return: list or numpy array of 3, 4, ..., max_val

    """
    list_temp = []
    for i in range(3,max_val+1):
        list_temp.append(i)
    array = np.array(list_temp)
    return array
     # @TODO - Fix this function as described in doc string

def calc_area(num_sides):
    """
    Assume radius = 1
    calculate area as
    angle = 2 pi / num_sides
    area = num_sides * cos(angle/2) * sin(angle/2)

    :param sides: either list or numpy array of number of sides
    :return: list or numpy array of areas
    """
    angle = (2*np.pi)/num_sides
    area = num_sides * np.cos(angle/2) * np.sin(angle/2)
    return area
    # @TODO - Fix this function as described in doc string

def calc_perimeter(num_sides):
    """
    Assume radius = 1
    calculate perimeter of object
    angle = 2 pi / num_sides
    length of side = 2 * sin(angle/2)
    perimeter = num sides * length of side
    :param sides: list or numpy array of number of sides
    :return: list or numpy array of perimeters
    """
    angle = (2*np.pi)/num_sides
    length_of_side = 2 * np.sin(angle/2)
    perimeter = num_sides * length_of_side
    return perimeter
    # @TODO - Fix this function as described in doc string

def write_polygon_data(file_path, max_sides):
    """
    Use the functions above as either lists or numpy arrays
    and write a tab separated data to file where each line contains
        name of polygon   (string)
        number of sides     (int )
        area      (float)
        perimeter (float)

    Starts with 3 sides up to and including max sides

    For polygon name, you can use "n-gon"
    e.g. "3-gon" for triangle, "5-gon" for pentagon

    For maximum credit, use the dictionary of
    names given in the given/polygons.py file
    for the first 12 names

    e.g.
    ...
    undecagon	11	2.9735244960057865	6.198116250511453
    dodecagon	12	2.9999999999999996	6.211657082460498
    13-gon	13	3.0207006182844953	6.222207271476501
    14-gon	14	3.037186173822907	6.230586150776803
    ...

    :param file_path:
    :param max_sides: max calculated sides
    :return: number of rows written
    """

    # Use the methods defined above to get data
    # I'll give you this code
    sides = define_numpy_sides(max_sides)
    area = calc_area(sides)
    peri = calc_perimeter(sides)
    # file_names = []
    # file_sides = []
    # file_areas = []
    # file_peri = []
    # with open(file_path) as file:
    #     lines = file.readlines()
    #     for line in lines:
    #         line = line.split()
    #         file_names.append(line[0])
    #         file_sides.append(line[1])
    #         file_areas.append(line[2])
    #         file_peri.append(line[3])
    #         print('lines', line)

    with open(file_path, "wt") as file:
        for i in range(3, max_sides+1):
            # print(sides[i])
            # print(area[i])
            # print(peri[i])
            agon = "{}-gon".format(sides[i])
            writer = csv.writer(file, delimiter = ' ')
            writer.writerow("{} {} {} {}".format(agon, sides[i], area[i], peri[i]))
    # Now write the data to the files
    pass # @TODO - Fix this function as described in doc string



if __name__ == '__main__':
    # No need to modify this code below
    # Just given to help you test

    sides = define_numpy_sides(6)
    print("   sides = ", type(sides), sides, "  should be [3 4 5 6]!")

    area = calc_area(sides)
    print("   area = ", type(area), area)

    peri = calc_perimeter(sides)
    print("   peri = ", type(peri), peri)
    print("       area and peri should match the values in data/polygon_data.csv file")

    file_path = os.path.join("data","polygon_data.csv")
    num_written = write_polygon_data(file_path, 20)
    print(" num written = ", num_written, " should be 18!")
