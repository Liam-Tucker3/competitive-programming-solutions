# Problem C: Bobby's bet
import math
n = int(input())

# Creating static list of factorials
factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

# Creating table of nCx counts
chooseTable = [[0 for i in range(11)] for j in range(11)]
for y in range(11):
    for x in range(y+1):
        chooseTable[y][x] = factorials[y] / (factorials[x] * factorials[y - x])

for i in range(n):
    vals = input().split()
    r = int(vals[0])
    s = int(vals[1])
    x = int(vals[2])
    y = int(vals[3])
    w = int(vals[4])
    
    prob = (s + 1 - r) / s
    
    cumOdds = 0
    for j in range(x, y+1):
        cumOdds += (prob ** j) * ((1-prob) ** (y-j)) * chooseTable[y][j]
    if cumOdds * w > 1: print("yes")
    else: print("no")
