# Gears and Axels

import math

n = int(input())
d = {}
for i in range(n):
    vals = input().split()
    s, c = int(vals[0]), int(vals[1])
    if s in d.keys(): d[s].append(c)
    else: d[s] = [c]

log = 0
for gearSize in d.keys():
    thisList = d[gearSize]
    l = len(thisList)
    if l <= 1: continue
    thisList = list(sorted(thisList))
    for i in range(int(len(thisList) / 2)):
        log += math.log(thisList[l - 1 - i] / thisList[i])
print(log)