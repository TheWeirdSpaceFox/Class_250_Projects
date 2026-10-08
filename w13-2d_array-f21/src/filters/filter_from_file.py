"""
 TODO - implement an FilterFromFile class here.
 This class loads a kernel fro a comma separated text file

 FilterFromFile inherits from ImageFilter
 You should only need to implement its constructor. All other functionality
   can be implemented in the ImageFilter Class. The constructor takes a single
   argument, file_path which specifies the path of the text file to load kernel from

 Ensure the file_path exists, if it doesn't, raise a FileNotFoundError with the message:
    "Error: file_path for image filter not found: " + file_path
 Hint: you can check if a file exists using:  os.path.isfile(file_path)

 Ensure the kernel has correct dimensions. Specifically perform the following checks:
    Ensure the kernel has > 0 number of rows. If not,
        raise a ValueError with the message: "Error: Filter must have greater than zero rows"

    Ensure the kernel has a > 0 number of columns. If not,
        raise a ValueError with the message: "Error: Filter must have greater than zero columns"

    Ensure the kernel has the same number of rows as columns. If not,
        raise a valueError with the message: "Error: Filter number of rows should be equal to the number of columns"


 Ensure the size of the filter is odd. If it isn't, raise a ValueError,
   with the message "Error: kernel size must be odd"
"""

from src.filters.image_filter import ImageFilter
import csv
import os
import numpy as np
class FilterFromFile(ImageFilter):
    def __init__(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError("Error: file_path for image filter not found: " + file_path)
        else:
            with open(file_path, "rt") as file:
                rows = 0
                columns = 0
                row1 = []
                i = 0
                for row in file:
                    rows += 1
                    row = row.strip().split(",")
                    if i == 0:
                        row1.append(row)
                        i += 1
                    for column in row1:
                        columns += 1
                if rows <= 0:
                    raise ValueError("Error: Filter must have greater than zero rows")
                if columns <= 0:
                    raise ValueError("Error: Filter must have greater than zero columns")
                if rows != columns:
                    raise ValueError("Error: Filter number of rows should be equal to the number of columns")
                if rows / 2 == 0:
                    raise ValueError("Error: kernel size must be odd")
                self.size = rows

    def __add__(self, other):
        ImageFilter.__add__(self, other)

    def __sub__(self, other):
        ImageFilter.__sub__(self, other)


if __name__ == '__main__':
    import scipy.misc
    trash_panda = scipy.misc.face(gray=True)
    face = trash_panda[100:500, 400:900]
    # You may want to do a quick downsampling to speed up your program when debugging
    face = face[::8, ::8]

    sobel_filter = FilterFromFile(os.path.join('data', 'sobel_filter.txt'))
    sobel_filtered_face = sobel_filter.filter(face)