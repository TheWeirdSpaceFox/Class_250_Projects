"""
Practice File input and plotting using Matplot lib
@author Amanda Sanders
"""

import os
import angles
import math
import matplotlib.pyplot as plt

# Read the file
relative_file_path = os.path.join("data", "angles.txt")
print(" File:", relative_file_path)
degs, rads = angles.read_angles(relative_file_path)

# Calculate the cosine terms
print("TODO : Calculate the cosine of angle ")
cos = rads[:]
for i, rad in enumerate(rads):
    cos[i] = math.cos(rad)

# Plot the data
fig = plt.figure()
plt.xkcd()
plt.plot(degs, cos, 'b-', label='cosine')
plt.xlabel('Degrees')
plt.ylabel('Value')
plt.title(' Cosine (Amanda.Sanders.20)')
plt.grid(True, lw=0.75) # By default, xkcd has lw=0.0
plt.tight_layout() # Needed to avoid x/y label cutoff
fig.savefig(os.path.join("data", "cosine_angles.png"))
plt.show()

