import os, csv


from src import small_data

fpath = os.path.join("data", "small_data.txt")
print("path:", fpath)


c1,c2,c3 = small_data.read_data(fpath)
print(c1)
print(c2)
print(c3)

# # #Phase 2 - Visualize the data
import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot(c1[:14], c1[:14], 'r-',label='x')   # Limit to [:14]
plt.plot(c1[:10], c2[:10], 'g.',label='x^2') # Limit to [:10]
plt.plot(c1[:7], c3[:7], 'b:',label='x^3')   # Limit to [:7]
plt.legend(fontsize=12)
plt.xlabel('x',fontsize=24)
plt.ylabel('Value',fontsize=24)
plt.grid()
plt.title("My first plot (first.last.yy)")
fig.savefig("data/plot_data.png")
plt.show()
