# Bikes and barricades

n = int(input())

minY = 1000

for i in range(n):
    vals = input().split()
    x1 = int(vals[0])
    y1 = int(vals[1])
    x2 = int(vals[2])
    y2 = int(vals[3])

    if x2 > 0 and x1 > 0: continue
    if x2 < 0 and x1 < 0: continue

    yIntersect = 0
    if x1 < 0:
        yIntersect = y1 + (y2-y1) * (-1 * x1) / (x2 - x1)
    if x2 < 0: 
        yIntersect = y2 + (y1-y2) * (-1 * x2) / (x1 - x2)
    # print(yIntersect)
    if yIntersect <= 0: continue
    minY = min(yIntersect, minY)

if minY == 1000: print("-1.0")
else: print(minY)

"""
2
-10 7 5 19
-1 -1 8 21
"""

"""
2
4 -6 -12 -1
3 5 8 8
"""


