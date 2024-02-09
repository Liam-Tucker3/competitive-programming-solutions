# Problem A: Illuminated City

n = int(input())
x = int(input())
y = int(input())
aveLen = y / x

vals = input().split()
for i in range(len(vals)): vals[i] = int(vals[i])
    
vals = sorted(vals)

currCount = 0
currSum = 0

while True:
    if currCount >= len(vals):
        print(currCount)
        break
    if (currSum + vals[currCount]) / (currCount + 1) > aveLen:
        print(currCount)
        break
    else:
        currSum += vals[currCount]
        currCount += 1
