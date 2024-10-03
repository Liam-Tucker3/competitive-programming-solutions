import math
vals = input().split()

v1 = int(vals[0])
v2 = int(vals[1])
g = math.gcd(v1, v2)

if v1*v2/g <= int(vals[2]): print("yes")
else: print("no")