# Dishonest Lottery

n = int(input())

d = {}
for i in range(1,51):
    d[i] = 0
for i in range(10*n):
    vals = input().split()
    for j in range(5):
        v = int(vals[j])
        d[v] += 1

output = []
for i in range(1,51):
    if d[i] > 2*n: output.append(str(i))
if len(output) == 0: print(-1)
else: print(' '.join(output))