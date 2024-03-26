n = int(input())

diffs = []
for i in range(n):
    diffs.append(int(input()))

answers = []

for k in range(2,n+1):
    if n % k != 0: continue

    size = int(n/k)

    # Only looking at factors
    thisMax = -1
    for j in range(0, size):
        thisMax = max(thisMax, diffs[j])

    isValid = True
    for j in range(1,k):
        newMax = -1
        for index in range(j*size, (j+1)*size):
            newMax = max(newMax, diffs[index])
            if diffs[index] < thisMax: isValid = False
        thisMax = newMax
    
    if isValid: answers.append(k)

if len(answers) == 0: print(-1)
else:
    for a in answers:
        print(a)
