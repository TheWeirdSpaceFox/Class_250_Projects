from __init__ import encoder_decoder
import os
from matplotlib import pyplot as plt

key = 2
#
declaration = encoder_decoder(key)
declaration.encode("declaration.txt", "data", "declaration", "encoded")
declaration.decode("declaration.enc", "encoded", "declaration", "decoded")
print("declaration dec vs original")
print(declaration.compare("declaration.txt", "data", "declaration.dec", "decoded"))
print(declaration.validate("declaration.txt", "data", "declaration.dec", "decoded"))
print("declaration enc vs original")
print(declaration.compare("declaration.txt", "data", "declaration.enc", "encoded"))
print(declaration.validate("declaration.txt", "data", "declaration.enc", "encoded"))

#plot
# source = []
# encoded = []
# decoded = []





dream = encoder_decoder(key)
dream.encode("dream.txt", "data", "dream", "encoded")
dream.decode("dream.enc", "encoded", "dream", "decoded")
print("dream dec vs original")
print(dream.compare("dream.txt", "data", "dream.dec", "decoded"))
print(dream.validate("dream.txt", "data", "dream.dec", "decoded"))
print("dream enc vs original")
print(dream.validate("dream.txt", "data", "dream.enc", "encoded"))
print(dream.compare("dream.txt", "data", "dream.enc", "encoded"))

farewell = encoder_decoder(key)
farewell.encode("farewell.txt", "data", "farewell", "encoded")
farewell.decode("farewell.enc", "encoded", "farewell", "decoded")
print("farewell dec vs original")
print(farewell.compare("farewell.txt", "data", "farewell.dec", "decoded"))
print(farewell.validate("farewell.txt", "data", "farewell.dec", "decoded"))
print("farewell enc vs original")
print(farewell.validate("farewell.txt", "data", "farewell.enc", "encoded"))
print(farewell.compare("farewell.txt", "data", "farewell.enc", "encoded"))


inaugural = encoder_decoder(key)
inaugural.encode("inaugural.txt", "data", "inaugural", "encoded")
inaugural.decode("inaugural.enc", "encoded", "inaugural", "decoded")
print("inaugural dec vs original")
print(inaugural.compare("inaugural.txt", "data", "inaugural.dec", "decoded"))
print(inaugural.validate("inaugural.txt", "data", "inaugural.dec", "decoded"))
print("inaugural enc vs original")
print(inaugural.validate("inaugural.txt", "data", "inaugural.enc", "encoded"))
print(inaugural.compare("inaugural.txt", "data", "inaugural.enc", "encoded"))

promissory = encoder_decoder(key)
promissory.encode("promissory.txt", "data", "promissory", "encoded")
promissory.decode("promissory.enc", "encoded", "promissory", "decoded")
print("promissory dec vs original")
print(promissory.compare("promissory.txt", "data", "promissory.dec", "decoded"))
print(promissory.validate("promissory.txt", "data", "promissory.dec", "decoded"))
print("validate enc vs original")
print(promissory.compare("promissory.txt", "data", "promissory.enc", "encoded"))
print(promissory.validate("promissory.txt", "data", "promissory.enc", "encoded"))

vote = encoder_decoder(key)
vote.encode("vote.txt", "data", "vote", "encoded")
vote.decode("vote.enc", "encoded", "vote", "decoded")
print("validate dec vs original")
print(vote.compare("vote.txt", "data", "vote.dec", "decoded"))
print(vote.validate("vote.txt", "data", "vote.dec", "decoded"))
print("validate enc vs original")
print(vote.validate("vote.txt", "data", "vote.enc", "encoded"))
print(vote.compare("vote.txt", "data", "vote.enc", "encoded"))

woman = encoder_decoder(key)
woman.encode("woman.txt", "data", "woman", "encoded")
woman.decode("woman.enc", "encoded", "woman", "decoded")
print("woman dec vs original")
print(woman.validate("woman.txt", "data", "woman.dec", "decoded"))
print(woman.compare("woman.txt", "data", "woman.dec", "decoded"))
print("woman enc vs original")
print(woman.validate("woman.txt", "data", "woman.enc", "encoded"))
print(woman.compare("woman.txt", "data", "woman.enc", "encoded"))


fourth = encoder_decoder(key)
fourth.encode("fourth.txt", "data", "fourth", "encoded")
fourth.decode("fourth.enc", "encoded", "fourth", "decoded")
print("fourth dec vs original")
print(fourth.compare("fourth.txt", "data", "fourth.dec", "decoded"))
print(fourth.validate("fourth.txt", "data", "fourth.dec", "decoded"))
print("fourth enc vs original")
print(fourth.validate("fourth.txt", "data", "fourth.enc", "encoded"))
print(fourth.compare("fourth.txt", "data", "fourth.enc", "encoded"))

# #plot sim
points = []

x = [1,2,3,4,5,6,7,8]
points.append(fourth.compare("fourth.txt", "data", "fourth.enc", "encoded")[1])
points.append(woman.compare("woman.txt", "data", "woman.enc", "encoded")[1])
points.append(vote.compare("vote.txt", "data", "vote.enc", "encoded")[1])
points.append(promissory.compare("promissory.txt", "data", "promissory.enc", "encoded")[1])
points.append(inaugural.compare("inaugural.txt", "data", "inaugural.enc", "encoded")[1])
points.append(farewell.compare("farewell.txt", "data", "farewell.enc", "encoded")[1])
points.append(dream.compare("dream.txt", "data", "dream.enc", "encoded")[1])
points.append(declaration.compare("declaration.txt", "data", "declaration.enc", "encoded")[1])

plt.scatter(x,points)
plt.title("Similarity Scores")
plt.xlabel("Different Files")
plt.ylabel("Scores")
plt.show()

