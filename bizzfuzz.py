""" BizzFuzz """
import math
vals = input().split()
a = int(vals[0])
b = int(vals[1])
c = int(vals[2])
d = int(vals[3])

val = math.lcm(c,d)

minInt = 0
if a % val == 0: minInt = a
else: minInt = val * (int(a/val) + 1)
    
intRange = b - minInt
rangeCount = int((intRange / val) + 1)
print(rangeCount)