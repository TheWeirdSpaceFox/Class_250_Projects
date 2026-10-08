"""
Practice File input and plotting using Matplot lib
@author <your name here>
"""

import angles_module
#import math
import matplotlib.pyplot as plt
import numpy as np
import os

# Read the file
relative_file_path = os.path.join("data", "angles_module.txt")
print(" File:", relative_file_path)
degs, rads = angles_module.read_angles(relative_file_path)
print("rads=", degs)



# # Calculate the sine terms
print("TODO - Calculate sine function using numpy ")
sin = rads[:]
for i, rad in enumerate(rads):
    sin[i] = np.sin(rad)


# Plot the data
fig = plt.figure()
plt.xkcd()
plt.plot(degs, sin, 'b-', label='sine')
plt.xlabel('Degrees')
plt.ylabel('Value')
plt.title(' Sine Function (Amanda.Sanders.20)')
plt.tight_layout() # Needed to avoid x/y label cutoff
plt.grid(True, lw=1.0) # By default, xkcd has lw=0.0
fig.savefig(os.path.join("data", "sine_angles_module.png"))
plt.show()
