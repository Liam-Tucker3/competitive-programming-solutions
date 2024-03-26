""" EpigDanceOff """
vals = input().split()
n = int(vals[0])
m = int(vals[1])

rows = []
for i in range(n):
    rows.append(input())

danceCount = 0
for j in range(m):
    allDash = True
    for i in range(n):
        if rows[i][j] != "_": allDash = False
    if allDash: danceCount += 1
print(danceCount + 1)