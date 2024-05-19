# Problem D
str = input()

allUP = 0
allDOWN = 0
allYOU = 0

if str[1] != str[0]:
    allUP += 1
    allDOWN += 1
    allYOU += 1
if str[1] == "U":
    allDOWN += 1
if str[1] == "D":
    allUP += 1

for i in range(2, len(str)):
    thisCH = str[i]
    lastCH = str[i-1]
    
    if thisCH != lastCH: allYOU += 1
    if thisCH == "U": allDOWN += 2
    if thisCH == "D": allUP += 2
        
print(allUP)
print(allDOWN)
print(allYOU)