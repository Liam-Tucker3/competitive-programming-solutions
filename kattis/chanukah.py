## Problem C
n = int(input())
for i in range(n):
    vals = input().split()
    x = vals[0]
    y = int(vals[1])
    z = int(y * (y+1) / 2) + y
    
    print(x, z)
