vals = input().split()
n = int(vals[0])
s = int(vals[1])

currLevel = s
count = 0

for i in range(n):
    thisVal = input()
    if len(thisVal) == 1:
        thisVal = int(thisVal)
    else:
        thisVal = 1 + int(thisVal[0])
    
    if currLevel < thisVal:
        count += 1
        currLevel = s - thisVal
    else:
        currLevel -= thisVal
print(count)