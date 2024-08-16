# diehard.py

# Returns win probability for d1
def winProb(d1, d2):
    wins = 0
    matchups = 0
    for i in range(6):
        for j in range(6):
            if d1[i] != d2[j]: matchups += 1
            if d1[i] > d2[j]: wins += 1
    if matchups == 0: return 0 # Neither could win 
    return wins / matchups

d1 = input().split()
d2 = input().split()
d3 = input().split()

for i in range(6):
    d1[i] = int(d1[i])
    d2[i] = int(d2[i])
    d3[i] = int(d3[i])

if winProb(d1, d2) >= 0.5 and winProb(d1, d3) >= 0.5: print(1)
elif winProb(d2, d1) >= 0.5 and winProb(d2, d3) >= 0.5: print(2)
elif winProb(d3, d1) >= 0.5 and winProb(d3, d2) >= 0.5: print(3)
else: print("No dice")