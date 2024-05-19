import math
# Problem G
num_cases = int(input())
for i in range(num_cases):
    vals = input().split()
    
    w = int(vals[0])
    g = int(vals[1])
    h = int(vals[2])
    r = int(vals[3])
    
    min_distance = math.sqrt(w*w + (g-h) * (g-h))
    min_distance = round(min_distance, 8)
    
    cutoff = 0
    if g != r or h != r: cutoff = w * (g - r) / (g + h - r - r)
    max_distance = math.sqrt(cutoff * cutoff + (g - r) * (g - r)) + math.sqrt((w - cutoff) * (w - cutoff) + (h-r) * (h-r))
    max_distance = round(max_distance, 8)
    
    print(f"{min_distance} {max_distance}")