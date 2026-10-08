"""
Sample file for binary I/O
"""
import os
import struct
import numpy as np
import matplotlib.pyplot as plt
# Follow along in class as we analyze the mystery data in file

format = ">iii"
file_name = os.path.join("data", "mystery_data.dat")

c0, c1, c2 = [], [], []
with open(file_name, "rb") as file:
    ba = bytearray(file.read())

    n_bytes = len(ba)
    cs = struct.calcsize(format)
    n_chunks = n_bytes//cs

    for i in range(n_chunks):
        tup = struct.unpack(format, ba[cs*i: cs*(i+1)])
        c0.append(tup[0])
        c1.append(tup[1])
        c2.append(tup[2])

print(c0[:5])
print(c1[:5])
print(c2[:5])

time_array = np.array(c0)-c0[0] + np.array(c1)*1e-9
data = np.array(c2)

#convert radians
data = data/1024 * np.pi*2

data[data> np.pi] = data[data> np.pi] - 2*np.pi
fig = plt.figure()
plt.plot(time_array[time_array < 20.0],data[time_array < 20.0])
plt.xlabel("Time [s]")
plt.ylabel("Pendulum Angle [radians]")
plt.title("Pendulum Angle vs Time (amanda.sanders.20)")
fig.savefig(os.path.join("data", "Pendulum Angle vs Time.png"))
plt.show()