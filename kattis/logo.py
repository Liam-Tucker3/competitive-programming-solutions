# Logo
import math
twopi = 2 * math.pi

t = int(input())
for i in range(t):
    n = int(input())
    x = 0
    y = 0
    deg = 90
    for j in range(n):
        line = input().split()
        
        if line[0] == "fd":
            x += int(line[1]) * math.cos(deg*twopi/360)
            y += int(line[1]) * math.sin(deg*twopi/360)
        elif line[0] == "bk":
            x -= int(line[1]) * math.cos(deg*twopi/360)
            y -= int(line[1]) * math.sin(deg*twopi/360)
        elif line[0] == "lt":
            deg += int(line[1])
        elif line[0] == "rt":
            deg -= int(line[1])
        else:
            assert False # Should never happen
    
    dist = math.sqrt(x*x + y*y)
    print(int(dist + 0.5))
