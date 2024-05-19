# Deceptive Dice
vals = input().split()
n = int(vals[0])
k = int(vals[1])

evs = [0 for i in range(k+1)]
evs[1] = (n+1) / 2
for i in range(2,k+1):
    thisEv = 0
    for j in range(1,n+1):
        # print(j, max(evs[i-1], j) * (1/n))
        thisEv += (1/n) * max(evs[i-1], j)
    evs[i] = thisEv

# print(evs)
print(evs[-1])