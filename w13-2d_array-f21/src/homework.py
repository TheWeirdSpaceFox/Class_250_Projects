import scipy.misc
import matplotlib.pyplot as plt
import os

#TODO - implement object-oriented filters
from src.filters.average_filter import AverageFilter
from src.filters.sharpening_filter import SharpeningFilter
from src.filters.filter_from_file import FilterFromFile


###############################################################
#     Demo of Image Manipulation
###############################################################

#TODO - in your code, raise exceptions as defined in each object
# Put all fo the code below into a try/except block to catch the following 3 exception types:
#    FileNotFoundError, ValueError, and TypeError.
# When handling the error, just print the error message


# Load the image, crop to the racoon's face, and do a crufty downsampling
# here, we are just downsampling to increase the execution time, so
# being crufty is OK. Once you have verified your implementation you can
# remove the downsampling code
trash_panda = scipy.misc.face(gray=True)
face = trash_panda[100:500,400:900]
# You may want to do a quick downsampling to speed up your program when debugging
face = face[::8,::8]

# Create an Average Filter, apply it to the image, and display

average_filter = AverageFilter(5)
blurred_face = average_filter.filter(face)
fig = plt.figure()
plt.gray()
plt.imshow(blurred_face)
# TODO - replace first.last.yy with your name and year
plt.title("Face with Average Filtered (Amanda.Sanders.20)")

# Create a Sharpening Filter, apply it to the image, and display
sharpening_filter = SharpeningFilter(3)
sharpened_face = sharpening_filter.filter(face)
fig = plt.figure()
plt.gray()
plt.imshow(sharpened_face)
# TODO - replace first.last.yy with your name and year
plt.title("Face with Sharpen Filter (Amanda.Sanders.20)")

# Create a FilterFromFile, apply it to the image, and display
sobel_filter = FilterFromFile(os.path.join('data','sobel_filter.txt'))
sobel_filtered_face = sobel_filter.filter(face)
fig = plt.figure()
plt.gray()
plt.imshow(sobel_filtered_face)
# TODO - replace first.last.yy with your name and year
plt.title("Face With Filter from File (Amanda.Sanders.20)")

# show the plots
plt.show()




