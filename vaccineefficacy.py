## Problem E
n = int(input())

vax = 0
noVax = 0

aVax = 0
bVax = 0
cVax = 0

aNo = 0
bNo = 0
cNo = 0

for i in range(n):
    s = input()
    if s[0] == "N": 
        noVax += 1
        if s[1] == "Y": aNo += 1
        if s[2] == "Y": bNo += 1
        if s[3] == "Y": cNo += 1
    
    else: 
        vax += 1
        if s[1] == "Y": aVax += 1
        if s[2] == "Y": bVax += 1
        if s[3] == "Y": cVax += 1
            
aRate = aVax / vax
bRate = bVax / vax
cRate = cVax / vax
aNoRate = aNo / noVax
bNoRate = bNo / noVax
cNoRate = cNo / noVax

aRed = 100 * (aNoRate - aRate) / aNoRate
bRed = 100 * (bNoRate - bRate) / bNoRate
cRed = 100 * (cNoRate - cRate) / cNoRate

if aRed <= 0: print("Not Effective")
else: print(aRed)
if bRed <= 0: print("Not Effective")
else: print(bRed)
if cRed <= 0: print("Not Effective")
else: print(cRed)
    