"""
Program 1




@author Amanda Sanders
 vvvvvvvvvvv you code below here vvvvvvvvvvvvvv
"""
# pylint: disable=C0103

import os
from given.car import Car


def load_text(file_path):
    """
    Given a filepath of a text file, read in data into 4 lists of numbers, the first two columns are floats, the last two columns are ints.
    You should return the column headers (in the line that starts with #) as a list of strings.

    # col1:col2:col3:col4
    val1, val2, val3, val4

    :param file_path:
    :return: the four lists of data AND the column names
    """
    header = []
    col1 = []
    col2 = []
    col3 = []
    col4 = []
    i = 0
    with open(file_path, "rt") as file:
        file = file.readlines()
        for line in file:
            print("line",line)
            if i == 0:
                header.append(line)
                i+=1
            line.split(",")
            col1.append(line[0])
            col2.append(line[1])
            col3.append(line[2])
            col4.append(line[3])
    return header, col1, col2, col3, col4



def write_text_file(file_path, cars):
    """
    Given a file_path and a list of Car objects (defined in the given folder) write the car's attributes to a text file.
        You should use a colon ":" to separate the values, each line should contain only one car.
        Use the order provided in Car's constructor.

    :param filepath:
    :param cars:
    """
    with open(file_path, "wt") as file:
        file.write("{}:{}".format(cars[0],cars[1]))


if __name__ == '__main__':
    filepath = os.path.join("data", "data.txt")
    print(load_text(filepath))

    # Example code for write_data()
    data_filepath = os.path.join("data", "cars.txt")
    cars = [Car("Ford", "Focus", 2017, "Grey"), Car("Ford", "Explorer", 2019, "Red")]
    write_text_file(data_filepath, cars)