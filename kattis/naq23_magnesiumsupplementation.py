# Problem H
import math

vals = input().split()
n = int(vals[0])
k = int(vals[1])
p = int(vals[2])

minList = []
maxList = []

for i in range(1, 1 + int(math.sqrt(n))):
    if n % i == 0:
        if n/i <= k and n/i >= n/p:
            maxList.append(int(n/i))
        if i <= k and i >= n/p:
            minList.append(i)
            
while True:
    if len(maxList) > 0 and len(minList) > 0 and maxList[-1] <= minList[-1]:
        maxList = maxList[:-1]
    else:
        break
    

count = len(minList) + len(maxList)
print(count)

for i in minList:
    print(i)

for i in reversed(list(maxList)):
    print(i)
