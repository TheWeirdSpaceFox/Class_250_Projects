"""
TODO - implement an ImageFilter class here.
 An ImageFilter is a base class that holds image filter functionality.
 This functionality includes:

 a constuctor, which sets the single instance attribute, kernel which is a 2D NumPy array
 an __add__(self, other) method which adds one ImageFilter to another
 a __subtract__(self, other) method which subtracts on ImageFilter from another
 a filter(self, image) method which applies an image filter to a NumPy array representation of an image

 You should Ensure the following:
    in __add__ ensure other is an instance of ImageFilter. If it is not, raise a TypeError
      with the error message: "Error: other must be an instance of ImageFilter in ImageFilter.__add__"

     in __sub__ ensure other is an instance of ImageFilter. If it is not, raise a TypeError
       with the error message: "Error: other must be an instance of ImageFilter in ImageFilter.__sub__"

    in filter ensure the image is a NumPy array. If it isn't then raise a TypeError
     with the error message: "Error: A filter must be applied to a NumPy Array"

"""

import numpy as np

class ImageFilter:
    def __init__(self, size):
        self.size = size
        self.kernel = np.ones((self.size, self.size)) / (self.size * self.size)

    def __add__(self, other):
        if not isinstance(other, ImageFilter):
            raise TypeError("Error: other must be an instance of ImageFilter in ImageFilter.__add__")
        return ImageFilter(self.kernel + other.kernel)

    def __sub__(self, other):
        if not isinstance(other, ImageFilter):
            raise TypeError("Error: other must be an instance of ImageFilter in ImageFilter.__sub__")
        return ImageFilter(self.kernel - other.kernel)

    def filter(self, image):
        #convolve image with self.kernel
        if not isinstance(image, ImageFilter):
            raise TypeError("Error: A filter must be applied to a NumPy Array")
        output = np.zeros(image.shape)


        k = self.kernel.shape[0] // 2

        # Two nested for loops for iterating through all pixels in given image
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                # print(f"Image value as {i},{j}: {image[i,j]}")
                # normalization value
                norm = 0.0

                # Two nested for loops for iterating through kernel
                for u in range(-k, k + 1):
                    ii = i - u
                    if 0 <= ii < image.shape[0]:
                        for v in range(-k, k + 1):
                            jj = j - v
                            if 0 <= jj < image.shape[1]:
                                output[i, j] += self.kernel[u + k, v + k] * image[ii, jj]
                                norm += self.kernel[u + k, v + k]
                output[i, j] = output[i, j] / norm
                output[i, j] = np.array(output[i, j])

        return output
        # make sure image is numpy array take some from made and edit
