""" Run-Length Encoding Run """
vals = input().split()
s = vals[1]
# print(s)

outputList = []
if vals[0] == "E":
    i = 0
    while i < len(s):
        thisCh = s[i]
        thisCount = 1
        while i+1 < len(s) and s[i+1] == thisCh:
            i += 1
            thisCount += 1
        outputList.append(thisCh)
        outputList.append(str(thisCount))
        i += 1
        
else:
    for i in range(0, len(s), 2):
        for j in range(int(s[i+1])):
            outputList.append(s[i])
    
print(''.join(outputList))