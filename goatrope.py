# Problem C
import math
vals = input().split()
x = int(vals[0])
y = int(vals[1])
x1 = int(vals[2])
y1 = int(vals[3])
x2 = int(vals[4])
y2 = int(vals[5])

distance = 99999
options = []
options.append(math.sqrt((x-x1)**2 + (y-y1)**2))
options.append(math.sqrt((x-x2)**2 + (y-y1)**2))
options.append(math.sqrt((x-x1)**2 + (y-y2)**2))
options.append(math.sqrt((x-x2)**2 + (y-y2)**2))

if x > x1 and x < x2:
    options.append(max(y - y1, y1-y))
    options.append(max(y-y2, y2-y))
if y > y1 and y < y2:
    options.append(max(x - x1, x1-x))
    options.append(max(x-x2, x2-x))
    
print(min(options))