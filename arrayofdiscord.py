""" Array of Discord """
n = int(input())
vals = input().split()
for i in range(n):
    vals[i] = int(vals[i])

sol = False

for i in range(n):
    thisStr = str(vals[i])
    for j in range(len(thisStr)):
        
        # Checking against previous number
        if i != 0:
            if j == 0 and len(thisStr) > 1:
                newInt = int("1"+thisStr[1:])
                if newInt < vals[i-1]:#
                    vals[i] = newInt
                    sol = True
                    break
            else:
                newInt = int(thisStr[:j] + "0" + thisStr[j+1:])
                if newInt < vals[i-1]:
                    vals[i] = newInt
                    sol = True
                    break
        if i+1 < n:
            newInt = int(thisStr[:j] + "9" + thisStr[j+1:])
            if newInt > vals[i+1]:
                vals[i] = newInt
                sol = True
                break
                    
    if sol: break
        
if sol:
    for i in range(len(vals)):
        vals[i] = str(vals[i])
    print(" ".join(vals))
else:
    print("impossible")