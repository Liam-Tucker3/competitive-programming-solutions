# divyvingup.py

numContests = int(input())
prizeAmounts = input().split()

totalPrize = 0
for p in prizeAmounts: totalPrize += int(p)

if totalPrize % 3 == 0: print('yes')
else: print("no")