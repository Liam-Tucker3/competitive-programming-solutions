import math

numCases = int(input())
for i in range(numCases):
    vals = input().split()
    a = int(vals[0])
    b = int(vals[1])
    d = int(vals[2])
    
    if d % math.gcd(a,b) == 0: print("Yes")
    else: print("No")