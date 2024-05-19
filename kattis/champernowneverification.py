n = input()
lenn = len(n)

i = 1
thisIndex = 0
thisLen = 1

valid=True
while True:
    if thisIndex+thisLen > lenn:
        valid = False
        break
    if int(n[thisIndex:thisIndex+thisLen]) == i:
        if thisIndex + thisLen == lenn:
            break
        i += 1
        thisIndex += thisLen
        thisLen = len(str(i))
    else:
        valid = False
        break
    

if not valid: print("-1")
else: print(i)