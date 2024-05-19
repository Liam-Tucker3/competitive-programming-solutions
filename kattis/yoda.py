# Yoda
n = input()
m = input()

nRev = ""
for ch in n: nRev = ch + nRev
mRev = ""
for ch in m: mRev = ch + mRev

# print(nRev, mRev)

for i in range(min(len(nRev), len(mRev))):
    if int(nRev[i]) < int(mRev[i]): nRev = nRev[:i] + "X" + nRev[i+1:]
    elif int(nRev[i]) > int(mRev[i]): mRev = mRev[:i] + "X" + mRev[i+1:]

n = reversed(nRev)
m = reversed(mRev)

# print(n)
# print(m)
        
newM = ""
for ch in m:
    if ch != "X": newM = newM + ch

newN = ""
for ch in n:
    if ch != "X": newN = newN + ch
        
if len(newN) == 0: print("YODA")
else: print(int(newN))

if len(newM) == 0: print("YODA")
else: print(int(newM))  