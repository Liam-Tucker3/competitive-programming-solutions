## Problem F
vals = input().split()
w = int(vals[0])
p = int(vals[1])

partitions = input().split()
for i in range(len(partitions)): partitions[i] = int(partitions[i])
partitions.append(0)
partitions.append(w)

diffs = {}
for i in partitions:
    for j in partitions:
        diff = i - j
        if diff < 0: diff = j - i
        if diff != 0: diffs[diff] = 1
            
x = list(sorted(diffs.keys()))
# print(x)
for i in range(len(x) - 1):
    print(x[i], end=" ")
print(x[-1], end="")