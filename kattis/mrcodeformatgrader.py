vals = input().split()
n = int(vals[0])
e = int(vals[1])
c = n - e

errors = input().split()
for i in range(len(errors)):
    errors[i] = int(errors[i])

outputE = "Errors: "
outputC = "Correct: "
eVals = []
cVals = []

eIndex = 0
curVal = 1

while eIndex < e:
    if errors[eIndex] == curVal:
        minVal = curVal
        while eIndex + 1 < e and errors[eIndex+1] == curVal + 1:
            curVal += 1
            eIndex += 1
        
        if minVal == curVal: # Case 1: Only adding one number
            eVals.append(str(minVal))
            eIndex += 1
            curVal += 1
            continue
        else: # Case 2: Adding multiple numbers
            tempStr = str(minVal) + "-" + str(curVal)
            eIndex += 1
            curVal += 1
            eVals.append(tempStr)
            continue
    else: # Adding to cVals
        maxVal = errors[eIndex] - 1
        tempStr = str(maxVal)
        if maxVal != curVal:
            tempStr = str(curVal) + "-" + str(maxVal)
        cVals.append(tempStr)
        curVal = errors[eIndex] # Not incrementing eIndex

# End while loop
if errors[-1] != n:
    curVal = errors[-1] + 1
    maxVal = n
    tempStr = str(maxVal)
    if maxVal != curVal:
        tempStr = str(curVal) + "-" + str(maxVal)
    cVals.append(tempStr)

if len(eVals) == 1: outputE += eVals[0]
elif len(eVals) == 2: outputE = outputE + eVals[0] + " and " + eVals[2]
else:
    for i in range(len(eVals) - 2):
        outputE = outputE + eVals[i] + ", "
    outputE = outputE + eVals[-2] + " and " + eVals[-1]

if len(cVals) == 1: outputC += cVals[0]
elif len(cVals) == 2: outputC = outputC + cVals[0] + " and " + cVals[2]
else:
    for i in range(len(cVals) - 2):
        outputC = outputC + cVals[i] + ", "
    outputC = outputC + cVals[-2] + " and " + cVals[-1]

print(outputE)
print(outputC)

"""
100 10
2 3 5 10 11 12 25 26 88 89
"""