## In this program you will generate a plot
from given import polygons
import os
file_path = os.path.join("data", "polygon_data.csv")
# Using methods from program 1
names = polygons.polygon_names()
x = polygons.read_polygon_data(file_path)
sides = x[1]
area = x[2]
peri = x[3]
print(names)
print(sides)
# Plot the area and perimeter of polygon as function of
# number of sides in polygon

# Label and title plot as expected
# Upload the finished image to scholar

# NOTE: IF you cannot get Program 1 to work,
# you may upload the data using method in given/polygons.py
#
# If program1 is working, then you DO NOT need to read data from file,
# just use the methods to generate the needed data!
