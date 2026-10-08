"""
Provide some methods that you will need

DO NOT CHANGE CODE HERE - JUST FOR TESTING

"""
import csv

def read_polygon_data(file_path):
    """
    @param file_path : file path name
    @return tuple with 4 lists containing
        name of polygons   (strings)
        number of sides     (int )
        area      (float)
        perimeter (float) (sum of all side lengths)
    """
    pass
    with open(file_path, "r") as fin:
        reader = csv.reader(fin,delimiter='\t')
        names = []
        sides = []
        area = []
        peri = []
        for line in reader:
            names.append(line[0])
            sides.append(int(line[1]))
            area.append(float(line[2]))
            peri.append(float(line[3]))
        return names, sides, area, peri

def polygon_names():
    """
    Map number of sides to name
    :return: dictionary of sides to name for first 12 polygons
    """
    return { 3:"triangle",
             4:"square",
             5:"pentagon",
             6:"hexagon",
             7:"heptagon",
             8:"octagon",
             9:"nonagon",
             10:"decagon",
             11:"undecagon",
             12:"dodecagon"}

if __name__ == '__main__':

    import os
    file_path =  os.path.join("data", "polygon_data.csv")

    names, sides, area, perimeter = \
        read_polygon_data(file_path)

    for i, name in enumerate(names):
        print(name, sides[i], area[i], perimeter[i])
