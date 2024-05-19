str = input()

aCount = 0
bCount = 0
cCount = 0

score = 0

for ch in str:
    if ch == 'a' or ch == "A": aCount += 1
    if ch == 'b' or ch == "B": bCount += 1
    if ch == 'c' or ch == "C": cCount += 1

    score = max(score, aCount, bCount, cCount)
    dec = min(aCount, bCount, cCount)
    if dec >= 1:
        aCount -= 1
        bCount -= 1
        cCount -= 1

print(score)
