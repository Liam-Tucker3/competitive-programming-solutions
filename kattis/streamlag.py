numRows = int(input())

data = [-1 for i in range(numRows + 1)]
currTime = 0
lagTime = 0

for i in range(numRows):
    vals = input().split()
    t = int(vals[0])
    i = int(vals[1])
    data[i] = t
    
for i in range(1, len(data)):
    if data[i] > currTime:
        lagTime += data[i] - currTime
        currTime = data[i] + 1
    else:
        currTime += 1
        
print(lagTime - 1)
    