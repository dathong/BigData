import numpy as np
from scipy import spatial

disDict = {}

def major(l,k):
    sum = 0
    for i in range(0,k):
        sum+= l[i][1]
    if sum >= k/2:
        return 1
    return 0

# X1 = np.loadtxt('./big_data_files/x00001b.csv',dtype=np.int8)
# X2 = np.loadtxt('./big_data_files/x00001b.csv',dtype=np.int8)
# y = np.loadtxt('./big_data_files/y00001.csv',dtype=np.int8)

X1 = np.random.randint(9, size=(5, 1))
X2 = np.random.randint(9, size=(5, 1))
y = np.random.randint(2, size=5)


print(X1)
print(X2)
print(y)

k = 1

resDict = {}

for p1 in range(X1.shape[0]):

    dict = {}
    pList = []
    for p2 in range(X2.shape[0]):
        pList.append([spatial.distance.euclidean(X1[p1],X2[p2]),y[p2]])
    pList.sort(key = lambda row: row[0])
    resDict[p1] = major(pList,k)
    print((p1,resDict[p1]))

