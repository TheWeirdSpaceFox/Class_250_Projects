"""
 TODO - implement an SharpeningFilter class here.
 A sharpening filter is described in the class slides

 SharpeningFilter inherits from ImageFilter
 You should only need to implement its constructor. All other functionality
   can be implemented in the ImageFilter Class

 Ensure the size of the filter is odd. If it isn't, raise a ValueError,
   with the message "Error: kernel size must be odd"
"""

from src.filters.image_filter import ImageFilter
import numpy as np
class SharpeningFilter(ImageFilter):
    def __init__(self, kernel):
        ImageFilter.__init__(self, kernel)

    def __add__(self, other):
        ImageFilter.__add__(self, other)

    def __sub__(self, other):
        ImageFilter.__sub__(self, other)

    def filter(self, image):
        if self.size / 2 == 0:
            raise ValueError("Error: kernel size must be odd")
        output = np.zeros(image.shape)

        k = (self.kernel.shape[0] // 2)

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