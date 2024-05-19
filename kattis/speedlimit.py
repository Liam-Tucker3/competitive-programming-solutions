##### Problem B
while True:
    x = int(input())
    if x == -1: break
        
    lastTime = 0
    dist = 0
    for i in range(x):
        vals = input().split()
        dist += int(vals[0]) * (int(vals[1]) - lastTime)
        lastTime = int(vals[1])
    
    print(dist, "miles")