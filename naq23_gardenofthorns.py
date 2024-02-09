# Problem D
import math

vals = input().split()
n = int(vals[0])
radius = int(vals[1])
w = int(vals[2])
h = int(vals[3])

score = 0

for i in range(n):
    vals = input().split()
    x = int(vals[0])
    y = int(vals[1])
    v  = int(vals[2])
    
    # print(x, y, v)
    
    thisArea = 0
    thisAngle = 2 * math.pi
    
    if (x == 0 or x == w) and (y == 0 or y == h): thisAngle = math.pi/2
    elif (x == 0 or x == w) or (y == 0 or y == h): thisAngle = math.pi
    
    # Case 1: Bottom
    if radius> y and y != 0:
        offset = math.sqrt(radius**2 - y**2)
        l = max(0, x-offset)
        r = min(x+offset, w)
        
        thisArea += y*(r-l)/2
        thisAngle -= math.acos(y/math.sqrt(y**2 + ((r-x))**2))
        thisAngle -= math.acos(y/math.sqrt(y**2 + ((l-x))**2))
        
        # print("CASE1", l, r, thisArea, thisAngle)
        
    # Case 2: Left
    if radius> x and x != 0:
        offset = math.sqrt(radius**2 - x**2)
        b = max(0, y-offset)
        t = min(y+offset, h)
        
        thisArea += x*(t-b)/2
        thisAngle -= math.acos(x/math.sqrt(x**2 + ((t-y))**2))   
        thisAngle -= math.acos(x/math.sqrt(x**2 + ((b-y))**2))
        
        # print("CASE2", l, r, thisArea, thisAngle)
        
    # Case 3: Top
    if radius> (h-y) and y != h:
        offset = math.sqrt(radius**2 - (h-y)**2)
        l = max(0, x-offset)
        r = min(x+offset, w)
        
        thisArea += (h-y)*(r-l)/2
        thisAngle -= math.acos((h-y)/math.sqrt((h-y)**2 + ((r-x))**2))
        thisAngle -= math.acos((h-y)/math.sqrt((h-y)**2 + ((l-x))**2))
        
        # print("CASE3", l, r, thisArea, thisAngle)
        
    # Case 4: Right
    if radius> (w-x) and x != w:
        offset = math.sqrt(radius**2 - (w-x)**2)
        b = max(0, y-offset)
        t = min(y+offset, h)
        
        thisArea += (w-x)*(t-b)/2
        thisAngle -= math.acos((w-x)/math.sqrt((w-x)**2 + ((t-y))**2))   
        thisAngle -= math.acos((w-x)/math.sqrt((w-x)**2 + ((b-y))**2)) 
        
        # print("CASE4", l, r, thisArea, thisAngle)
        
    # print(thisArea, thisAngle, i)
        
    thisArea += (thisAngle / (2 * math.pi)) * radius * radius * math.pi
    score += thisArea * v / (w * h)
    
print(score)
