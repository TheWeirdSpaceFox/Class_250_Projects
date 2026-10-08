import scipy.misc
import numpy as np
import matplotlib.pyplot as plt

###############################################################
#     Demo of Image Manipulation
###############################################################

# SciPy has some sample images for us to work with
# let's load an image of a racoon face
trash_panda = scipy.misc.face(gray=True)

# The image is actually stored as a two-dimensional numpy array
# Each value in the array is a value of a grayscale pixel
# and the size of the array is the length x width in pixels.
# pixel values are stored as uint8 (typically values between 0-255)
print("Original Image:")
print("   Type: ", type(trash_panda))
print("   Shape: ", trash_panda.shape)
print("   dtype:", trash_panda.dtype)
print("   sample value is: ", trash_panda[767][1023])

# Find the maximum and minimum values
max_value = trash_panda.max()
min_value = trash_panda.min()
print("   min_value = ", min_value)
print("   max_value = ", max_value)

# Let's create a plot of the image
# and make the colormap gray. Colormap just tells us
# how we should map the data (integer values) to color.
# so, essentially its a one-to-one mapping of number value
# to color value. In this case, we are using a grayscale image
# so, gray makes sense. However if you are visualizing other data,
# particularly data with a large range of values, other color maps
# may be more informative to use.
fig = plt.figure()
plt.gray()  # Set color map to grayscale
# plt.hsv() #hsv (color-colorscale) coloring
# plt.set_cmap('PiYG') #change color map to anything specified in the documentation with this commend
plt.imshow(trash_panda)
plt.title("Original Image")

# TODO - part 1 = loading and displaying an image.
#  Try different color mappings
#  Delete exit() and comment out plt.show() once done
plt.show()
exit()

###############################################################
#     Image Cropping
###############################################################

# Crop the picture to just the racoon's face
# To do this, we are slicing the image. We slice on each
# dimension as "start:stop"
face = trash_panda[100:500, 400:900]  # Slice
print("Cropped Image:")
print("   Type: ", type(face))
print("   Shape: ", face.shape)

# Show the cropped image
fig = plt.figure()
plt.gray()
plt.imshow(face)
plt.title("Cropped Image")

# TODO - part 2 = cropping an image. Delete exit() and comment out plt.show once done
plt.show()
exit()

###############################################################
#     Image Down-sampling using Slicing
###############################################################
# Now, let's sample the image. We can sample the image using
# array slicing. Remember, slicing is performed as: "start:stop:step"
# Sample the whole image at 1/8 size
fig = plt.figure()
plt.gray()
plt.imshow(trash_panda[::8, ::8])
plt.title("Trash Panda Eighth Size")

# Sample the face at 1/8th size
fig = plt.figure(4)
plt.gray()
plt.imshow(face[::8, ::8])
plt.title("Trash Panda Face Eighth Size")

# TODO - part 3 = Image Downsampling.
#  Notice how crufty the image looks
plt.show()
