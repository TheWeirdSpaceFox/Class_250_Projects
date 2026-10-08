import os, csv

fpath = os.path.join("data", "small_data.txt")
print("path:", fpath)

c1=[]
c2=[]
c3=[]
# with open(fpath, 'rt') as file:
#     reader = csv.reader(file, delimiter='|')
#     for line in reader:
#         #print(line)
#         c1.append(int(line[0]))
#         c2.append(int(line[1]))
#         c3.append(int(line[2]))
#
#     print(c1)
#     print(c2)
#     print(c3)
#
#
# mx = max(c1)
# print("max = ", mx)
# with open(fpath, 'at') as file:
#     writer = csv.writer(file, delimiter='|')
#     for i in range(mx+1, 33):
#         writer.writerow([i, i*i, i*i*i])
#
