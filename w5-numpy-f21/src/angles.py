"""
Practice File I/O  (input/output) using an angle degrees to radians conversion
@author Amanda Sanders
"""
import math

# def generate_angles():
#     # create an angle in whole degrees (0-360) and equivalent in radian on each line separate with \t
#
def write_angles(file_path):
    """
    Write file containing whole degrees (0 - 360) in 1 degree increments and
    equivalent degree in radians.  Use one line per angle, and separate
    numbers with a tab character ('\t').

    :param file_path: Whole path to file location to write data
    :return : Nothing to return
    """

    # Write out some comments about the steps you need to take to solve

    # write the the code

    degrees = []
    radians = []
    for degree in range(0,361):
        degrees.append(degree)
        radians.append(degree/360 * math.pi * 2)
    # write to file "\t" separated
    with open(file_path, "wt") as file:
        for i in range(len(radians)):
            rad = radians[i]
            deg = degrees[i]
            file.write(f"{deg}\t{rad}\n")

def read_angles(file_path):
    """
    Write file containing whole degrees (0 - 360) in 1 degree increments and
    equivalent degree in radians.
    :param file_path: Whole path to file location to read data
    :return : Tuple containing two lists degrees, and radians
    """
    # Write out some comments about the steps you need to take to solve

    # write the the code
    degs, rads = [], []
    with open(file_path, "rt") as file:
        for line in file.readlines():
            degrees, radians = line.strip().split("\t")
            degs.append(float(degrees))
            rads.append(float(radians))
    return degs, rads


if __name__ == '__main__':

    import os
    relative_file_path = os.path.join("data", "angles.txt")
    print(" File:", relative_file_path)

    write_angles(relative_file_path)

    degs, rads = read_angles(relative_file_path)

    print("Degree Equivalents:")
    print("{:>5s}: {:>8s} : {:>8s}".format("Angle", "Degrees", "Radians"))
    for i, deg in enumerate(degs):
        print(" {:3d} : {:8.2f} : {:8.4f}".format(i, deg, rads[i]))
