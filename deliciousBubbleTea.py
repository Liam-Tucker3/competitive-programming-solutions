teaCount = int(input())
teas = input().split()
toppingCount = int(input())
toppings = input().split()

for i in range(len(teas)):
    teas[i] = int(teas[i])
for i in range(len(toppings)):
    toppings[i] = int(toppings[i])

for i in range(len(teas)):
    t = input().split()
    t = t[1:]
    mC = 1001
    for j in range(len(t)):
        thisToppingIndex = int(t[j])
        thisTopping = toppings[thisToppingIndex - 1]
        if thisTopping < mC:
            mC = thisTopping
    teas[i] += mC
    
money = int(input())
minCost = 2001
for i in range(len(teas)):
    if teas[i] < minCost:
        minCost = teas[i]
num = int(money / minCost)
if num == 0: print(0)
else: print(num-1)